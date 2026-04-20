#!/usr/bin/env python3
"""财报窗口专项分析 — 隐含波动 + Beat/Miss 历史 + Post-Earnings Drift (PEAD)

用法: python3 earnings_setup.py [TICKER1,TICKER2,...]
默认: META,AAPL,CVX（下月财报三连）
"""
import sys
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from curl_cffi import requests

SESSION = requests.Session(impersonate="chrome")

def get_next_earnings_date(tk):
    try:
        cal = tk.calendar
        if cal is None:
            return None
        if isinstance(cal, dict):
            ed = cal.get('Earnings Date')
        elif isinstance(cal, pd.DataFrame):
            ed = cal.loc['Earnings Date'].iloc[0] if 'Earnings Date' in cal.index else None
        else:
            return None
        if isinstance(ed, list) and ed:
            return pd.Timestamp(ed[0])
        if ed:
            return pd.Timestamp(ed)
    except Exception:
        pass
    return None

def implied_move_from_straddle(tk, earnings_date):
    """ATM straddle price / spot ≈ 市场预期的财报后波动幅度"""
    try:
        expirations = tk.options
        if not expirations:
            return None, None
        ed = earnings_date.date() if hasattr(earnings_date, 'date') else earnings_date
        target = None
        for exp in expirations:
            exp_dt = datetime.strptime(exp, '%Y-%m-%d').date()
            if exp_dt >= ed:
                target = exp
                break
        if not target:
            return None, None

        chain = tk.option_chain(target)
        hist = tk.history(period='1d')
        if hist.empty:
            return None, None
        spot = hist['Close'].iloc[-1]

        calls = chain.calls.copy()
        puts = chain.puts.copy()
        calls['diff'] = (calls['strike'] - spot).abs()
        puts['diff'] = (puts['strike'] - spot).abs()
        atm_call_price = calls.nsmallest(1, 'diff').iloc[0]['lastPrice']
        atm_put_price = puts.nsmallest(1, 'diff').iloc[0]['lastPrice']
        straddle = atm_call_price + atm_put_price
        return (straddle / spot) * 100, target
    except Exception:
        return None, None

def earnings_history(tk, n=8):
    try:
        eh = tk.earnings_dates
        if eh is None or eh.empty:
            return None
        past = eh[eh.index < datetime.now(tz=eh.index.tz)].head(n)
        return past
    except Exception:
        return None

def post_earnings_drift(tk, n=8):
    try:
        eh = tk.earnings_dates
        if eh is None or eh.empty:
            return []
        past = eh[eh.index < datetime.now(tz=eh.index.tz) - timedelta(days=7)].head(n)
        if past.empty:
            return []
        hist = tk.history(period='5y')
        if hist.empty:
            return []
        if hist.index.tz is not None:
            hist.index = hist.index.tz_localize(None)
        results = []
        for edate in past.index:
            ed_naive = edate.tz_localize(None) if edate.tzinfo is not None else edate
            before = hist[hist.index < ed_naive].tail(1)
            after = hist[hist.index > ed_naive].head(5)
            if before.empty or after.empty:
                continue
            t_minus_1 = before['Close'].iloc[-1]
            t_plus_5 = after['Close'].iloc[-1]
            drift_pct = (t_plus_5 / t_minus_1 - 1) * 100
            surp = past.loc[edate].get('Surprise(%)') if 'Surprise(%)' in past.columns else None
            results.append({
                'date': ed_naive.strftime('%Y-%m-%d'),
                'drift_5d_pct': drift_pct,
                'surprise_pct': float(surp) if pd.notna(surp) else None,
            })
        return results
    except Exception:
        return []

def analyze(ticker):
    print(f"\n{'=' * 70}")
    print(f"Ticker: {ticker}")
    print('=' * 70)

    tk = yf.Ticker(ticker, session=SESSION)

    ed = get_next_earnings_date(tk)
    if ed is None:
        print("下次财报: 未知（yfinance calendar 无数据）")
    else:
        days = (ed - pd.Timestamp.now(tz=ed.tz if hasattr(ed, 'tz') else None)).days
        print(f"下次财报: {ed.date()} ({days:+d}d from today)")

    if ed is not None:
        imp_move, exp = implied_move_from_straddle(tk, ed)
        if imp_move is not None:
            print(f"Implied Move (straddle @ {exp}): ±{imp_move:.1f}%")
            print(f"  市场预期 gap: {imp_move:.1f}% → 实际 gap 超这个值才算'意外'")
        else:
            print("Implied Move: 期权数据不可用")

    eh = earnings_history(tk, 8)
    if eh is not None and not eh.empty:
        print(f"\n过去 8 季度 Beat/Miss 历史:")
        surprises = []
        for date, row in eh.iterrows():
            surp = row.get('Surprise(%)')
            est = row.get('EPS Estimate')
            act = row.get('Reported EPS')
            if pd.notna(surp):
                marker = "✅ BEAT" if surp > 0 else "❌ MISS"
                surprises.append(float(surp))
                est_str = f"${est:.2f}" if pd.notna(est) else "—"
                act_str = f"${act:.2f}" if pd.notna(act) else "—"
                print(f"  {date.date()}: est {est_str:>8}  act {act_str:>8}  "
                      f"surp {surp:+6.1f}%  {marker}")
        if surprises:
            beats = sum(1 for s in surprises if s > 0)
            avg_surp = sum(surprises) / len(surprises)
            print(f"  ─ Beat 率: {beats}/{len(surprises)} = {beats/len(surprises)*100:.0f}%")
            print(f"  ─ 平均 surprise: {avg_surp:+.1f}%")
    else:
        print("\n过去财报: yfinance 无数据")

    drifts = post_earnings_drift(tk, 8)
    if drifts:
        print(f"\nPost-Earnings Drift (T+5 相对 T-1):")
        all_drifts = []
        for d in drifts:
            surp = d['surprise_pct']
            surp_str = f" (surp {surp:+.1f}%)" if surp is not None else ""
            print(f"  {d['date']}: T+5 {d['drift_5d_pct']:+6.2f}%{surp_str}")
            all_drifts.append(d['drift_5d_pct'])
        avg_drift = sum(all_drifts) / len(all_drifts)
        positive = sum(1 for d in all_drifts if d > 0)
        print(f"  ─ 平均 5 日漂移: {avg_drift:+.2f}%")
        print(f"  ─ 正漂移占比: {positive}/{len(all_drifts)}")

def main():
    tickers = (sys.argv[1] if len(sys.argv) > 1 else 'META,AAPL,CVX').split(',')
    for t in tickers:
        try:
            analyze(t.strip().upper())
        except Exception as e:
            print(f"\n{t}: ERROR {type(e).__name__}: {e}")

if __name__ == '__main__':
    main()

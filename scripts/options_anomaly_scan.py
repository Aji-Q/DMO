#!/usr/bin/env python3
"""异常期权活动扫描 — Vol/OI 突变 + P/C 比率 (暗池信号近似)

用法: python3 options_anomaly_scan.py [TICKER1,TICKER2,...]
默认: holdings + watchlist

输出每只股票:
- 现价
- Calls/Puts 总 volume + OI
- P/C 比率（vol 和 oi）
- Vol/OI > 2 的异常合约（新建仓信号）
- 净方向性（偏多/偏空/中性）
"""
import sys
import yfinance as yf
import pandas as pd
from curl_cffi import requests

SESSION = requests.Session(impersonate="chrome")

def analyze_ticker(ticker, max_expirations=2):
    tk = yf.Ticker(ticker, session=SESSION)

    try:
        expirations = tk.options
        if not expirations:
            return {'ticker': ticker, 'error': '无期权链'}
    except Exception as e:
        return {'ticker': ticker, 'error': f'options fetch: {type(e).__name__}'}

    try:
        hist = tk.history(period='2d')
        if hist.empty:
            return {'ticker': ticker, 'error': '无现价'}
        spot = float(hist['Close'].iloc[-1])
    except Exception as e:
        return {'ticker': ticker, 'error': f'price fetch: {type(e).__name__}'}

    near_exps = expirations[:max_expirations]

    all_calls_vol = 0
    all_calls_oi = 0
    all_puts_vol = 0
    all_puts_oi = 0
    anomalies = []

    for exp in near_exps:
        try:
            chain = tk.option_chain(exp)
        except Exception:
            continue

        for df, opt_type in [(chain.calls, 'C'), (chain.puts, 'P')]:
            if df is None or df.empty:
                continue
            df = df.fillna(0)
            for _, row in df.iterrows():
                try:
                    vol = int(row.get('volume', 0) or 0)
                    oi = int(row.get('openInterest', 0) or 0)
                    strike = float(row.get('strike', 0) or 0)
                    iv = float(row.get('impliedVolatility', 0) or 0)
                except (ValueError, TypeError):
                    continue

                if opt_type == 'C':
                    all_calls_vol += vol
                    all_calls_oi += oi
                else:
                    all_puts_vol += vol
                    all_puts_oi += oi

                # 异常: OI 有一定存量 & 今日 Vol/OI > 2 = 激进新建仓
                if oi >= 100 and vol >= 100 and (vol / oi) > 2.0:
                    moneyness_pct = (strike - spot) / spot * 100
                    if opt_type == 'C':
                        itm_otm = 'ITM' if moneyness_pct < 0 else 'OTM'
                    else:
                        itm_otm = 'ITM' if moneyness_pct > 0 else 'OTM'
                    anomalies.append({
                        'exp': exp, 'type': opt_type, 'strike': strike,
                        'vol': vol, 'oi': oi, 'vol_oi': vol / oi,
                        'moneyness_pct': moneyness_pct,
                        'itm_otm': itm_otm, 'iv': iv,
                    })

    pc_vol = (all_puts_vol / all_calls_vol) if all_calls_vol > 0 else None
    pc_oi = (all_puts_oi / all_calls_oi) if all_calls_oi > 0 else None

    signals = []
    if pc_vol is not None:
        if pc_vol > 1.3:
            signals.append(f"🔴 P/C vol {pc_vol:.2f} (偏空)")
        elif pc_vol < 0.5:
            signals.append(f"🟢 P/C vol {pc_vol:.2f} (偏多)")

    anomalies.sort(key=lambda x: -x['vol_oi'])

    # 方向性：看 Top 10 异常中多空倾向
    top10 = anomalies[:10]
    bull_points = sum(1 for a in top10 if a['type'] == 'C' and a['moneyness_pct'] >= -10)
    bear_points = sum(1 for a in top10 if a['type'] == 'P' and a['moneyness_pct'] <= 10)

    if bull_points >= 3 and bull_points > bear_points:
        signals.append(f"🟢 {bull_points} 个激进 call 异常")
    if bear_points >= 3 and bear_points > bull_points:
        signals.append(f"🔴 {bear_points} 个激进 put 异常")

    return {
        'ticker': ticker, 'spot': spot,
        'calls_vol': all_calls_vol, 'puts_vol': all_puts_vol,
        'calls_oi': all_calls_oi, 'puts_oi': all_puts_oi,
        'pc_vol': pc_vol, 'pc_oi': pc_oi,
        'anomalies': anomalies,
        'signals': signals,
    }

def main():
    tickers = (sys.argv[1] if len(sys.argv) > 1
               else 'NVDA,SPY,AAPL,META,TSM,CVX,GLD,SCHD,MU,OXY,AMD').split(',')

    print(f"扫描 {len(tickers)} 只股票的异常期权活动...\n")

    results = []
    for t in tickers:
        r = analyze_ticker(t.strip().upper())
        results.append(r)

    print(f"{'Ticker':<8}{'Spot':>9}{'CallsV':>10}{'PutsV':>10}"
          f"{'P/C Vol':>9}{'P/C OI':>9}{'#Anom':>7}  Signals")
    print('-' * 100)
    for r in results:
        if r.get('error'):
            print(f"{r['ticker']:<8} {r['error']}")
            continue
        pc_v = f"{r['pc_vol']:.2f}" if r['pc_vol'] is not None else "—"
        pc_o = f"{r['pc_oi']:.2f}" if r['pc_oi'] is not None else "—"
        sig = ' | '.join(r['signals']) if r['signals'] else '—'
        print(f"{r['ticker']:<8}${r['spot']:>7.2f}"
              f"{r['calls_vol']:>10,}{r['puts_vol']:>10,}"
              f"{pc_v:>9}{pc_o:>9}{len(r['anomalies']):>7}  {sig}")

    # 异常明细
    for r in results:
        if not r.get('anomalies'):
            continue
        print(f"\n{r['ticker']} Top 5 异常（Vol/OI > 2，新建仓信号）:")
        for a in r['anomalies'][:5]:
            direction = "多头" if a['type'] == 'C' else "空头"
            print(f"  {a['exp']} {a['type']} ${a['strike']:.2f} "
                  f"({a['itm_otm']} {a['moneyness_pct']:+.1f}%): "
                  f"Vol {a['vol']:,} vs OI {a['oi']:,} = {a['vol_oi']:.1f}x  "
                  f"IV {a['iv']*100:.0f}%  → {direction}")

    print("\n解读:")
    print("  P/C Vol > 1.3: 整体看空情绪；< 0.5: 整体看多")
    print("  Vol/OI > 2: 今日新开仓数量超过既有未平仓的 2 倍 — 强信号")
    print("  Top 5 异常集中在 call OTM → 市场赌上涨")
    print("  Top 5 异常集中在 put OTM → 市场赌下跌或对冲")
    print("  ⚠️ 单日数据噪声大；跨多日同方向累积才是真信号")

if __name__ == '__main__':
    main()

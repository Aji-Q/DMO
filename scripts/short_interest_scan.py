#!/usr/bin/env python3
"""FINRA Reg SHO 每日做空数据扫描 — T+1 延迟，近似暗池的快速信号

用法: python3 short_interest_scan.py [TICKER1,TICKER2,...] [days_window]
默认: holdings + watchlist, 25 天窗口

输出每只股票:
- 最新一日 short volume / total volume 比率
- 20 日滚动均值 + 标准差
- Z-score (今日偏离历史均值几个 σ)
- 信号分级（做空激增 / 空头回补 / 正常）
"""
import sys, urllib.request, urllib.error
from datetime import datetime, timedelta
from collections import defaultdict
from statistics import mean, stdev

UA = {"User-Agent": "DMO Research research-contact@gmail.com"}
BASE_URL = "https://cdn.finra.org/equity/regsho/daily/CNMSshvol{yyyymmdd}.txt"

def fetch_day(date):
    url = BASE_URL.format(yyyymmdd=date.strftime('%Y%m%d'))
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode('utf-8', errors='ignore')
    except urllib.error.HTTPError:
        return None
    except urllib.error.URLError:
        return None

def parse_day(text, tickers_set):
    """FINRA 文件格式: Date|Symbol|ShortVolume|ShortExemptVolume|TotalVolume|Market"""
    result = {}
    for line in text.splitlines()[1:]:  # skip header
        parts = line.split('|')
        if len(parts) < 5:
            continue
        try:
            symbol = parts[1].strip().upper()
            if symbol not in tickers_set:
                continue
            short_vol = int(parts[2])
            total_vol = int(parts[4])
            if total_vol > 0:
                result[symbol] = (short_vol, total_vol)
        except (ValueError, IndexError):
            continue
    return result

def collect_series(tickers, days_window=25):
    tickers_set = set(t.upper() for t in tickers)
    data = defaultdict(list)

    today = datetime.now().date()
    current = today
    found = 0
    attempts = 0

    print(f"拉取 FINRA Reg SHO 每日做空数据 (目标 {days_window} 天)...", flush=True)
    while found < days_window and attempts < days_window * 2 + 10:
        if current.weekday() < 5:  # Mon-Fri
            text = fetch_day(current)
            if text:
                daily = parse_day(text, tickers_set)
                for sym, (sv, tv) in daily.items():
                    data[sym].append((current, sv / tv))
                found += 1
                if found % 5 == 0:
                    print(f"  已拉取 {found} 天 (最新 {current.isoformat()})", flush=True)
        current -= timedelta(days=1)
        attempts += 1

    return data, found

def analyze(data, tickers):
    results = []
    for ticker in tickers:
        t = ticker.upper()
        series = sorted(data.get(t, []))
        if len(series) < 5:
            results.append({'ticker': ticker, 'error': f'数据不足 ({len(series)} 天)'})
            continue

        ratios = [r for (_, r) in series]
        today_ratio = ratios[-1]
        historical = ratios[:-1]

        mu = mean(historical)
        sigma = stdev(historical) if len(historical) > 1 else 0
        z = (today_ratio - mu) / sigma if sigma > 0 else 0

        if z > 2.0:
            signal = f"🔴 做空激增 (z={z:+.1f})"
        elif z > 1.5:
            signal = f"🟠 做空偏高 (z={z:+.1f})"
        elif z < -2.0:
            signal = f"🟢 空头回补强 (z={z:+.1f})"
        elif z < -1.5:
            signal = f"🟡 空头减弱 (z={z:+.1f})"
        else:
            signal = "—"

        results.append({
            'ticker': ticker, 'days': len(series),
            'latest_date': series[-1][0],
            'today_ratio': today_ratio,
            'mean': mu, 'stdev': sigma, 'z': z,
            'signal': signal,
        })
    return results

def main():
    tickers = (sys.argv[1] if len(sys.argv) > 1
               else 'NVDA,SPY,AAPL,META,TSM,CVX,GLD,SCHD,MU,OXY,AMD').split(',')
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 25

    data, found = collect_series([t.strip() for t in tickers], days)
    print(f"\n共拉到 {found} 天数据。")

    results = analyze(data, tickers)

    print(f"\n{'Ticker':<8}{'Latest':<12}{'Days':>5}{'Today%':>9}{'Mean%':>9}"
          f"{'±1σ%':>8}{'Z':>7}  Signal")
    print("-" * 90)
    for r in results:
        if r.get('error'):
            print(f"{r['ticker']:<8} {r['error']}")
            continue
        print(f"{r['ticker']:<8}{r['latest_date'].isoformat():<12}{r['days']:>5}"
              f"{r['today_ratio']*100:>8.1f}%{r['mean']*100:>8.1f}%"
              f"{r['stdev']*100:>7.1f}%{r['z']:>+7.1f}  {r['signal']}")

    print("\n解读:")
    print("  🔴 做空激增 (z>2): 机构对冲或做空新建 — 查最新新闻/财报")
    print("  🟠 偏高 (z>1.5): 关注但不独立决策")
    print("  🟢 空头回补强 (z<-2): 可能挤空前兆或空头认输")
    print("  Short Volume 含市场制造商对冲，绝对数 ~40-60% 是正常")
    print("  关键是【变化率】而非绝对值")

if __name__ == '__main__':
    main()

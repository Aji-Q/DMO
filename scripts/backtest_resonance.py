#!/usr/bin/env python3
"""DMO 共振信号回测 — 验证 🟢🟢🟢 三派共振是否真的跑赢 SPY

方法: 用 8 个基金最近 N 个季度的 13F，为 universe 里每个 (quarter, ticker)
      计算共振信号（Triple/Double/Single/Multi-exit），然后测 3 个月 forward return
      vs SPY，聚合统计。

用法: python3 backtest_resonance.py [n_quarters] [universe_tickers]
默认: 8 季度 + 持仓+观察池 universe
"""
import sys, re, time, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta
import yfinance as yf
from curl_cffi import requests

SESSION = requests.Session(impersonate="chrome")
UA = {"User-Agent": "DMO Research research-contact@gmail.com"}

# 基金 + 派系分类
MANAGERS = {
    'Berkshire':    ('0001067983', 'value'),
    'Pershing':     ('0001336528', 'value'),
    'Third Point':  ('0001040273', 'value'),
    'Renaissance':  ('0001037389', 'quant'),
    'Bridgewater':  ('0001350694', 'quant'),
    'Appaloosa':    ('0001656456', 'subjective'),
    'Scion':        ('0001649339', 'subjective'),
    'Tiger Global': ('0001167483', 'subjective'),
}

TICKER_NAME = {
    'NVDA': ['NVIDIA'], 'AAPL': ['APPLE INC'], 'META': ['META PLATFORMS'],
    'TSM':  ['TAIWAN SEMICONDUCTOR'], 'CVX': ['CHEVRON'], 'MU': ['MICRON'],
    'OXY':  ['OCCIDENTAL'], 'AMD': ['ADVANCED MICRO'], 'GOOGL': ['ALPHABET'],
    'MSFT': ['MICROSOFT'], 'AMZN': ['AMAZON'], 'JNJ': ['JOHNSON & JOHNSON'],
    'XOM':  ['EXXON'], 'MSTR': ['MICROSTRATEGY', 'STRATEGY INC'],
    'SPY':  ['SPDR S&P 500'], 'GLD': ['SPDR GOLD'],
}

def fetch(url, retries=3):
    for i in range(retries):
        try:
            time.sleep(0.15)
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=30).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < retries - 1:
                time.sleep(2 ** i); continue
            raise

def get_13f_filings(cik, max_filings=20):
    url = (f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}"
           f"&type=13F-HR&dateb=&owner=include&count={max_filings}&output=atom")
    try:
        data = fetch(url).decode()
    except Exception:
        return []
    accs = re.findall(r'<accession-number>([\d-]+)</accession-number>', data)
    dates = re.findall(r'<filing-date>([\d-]+)</filing-date>', data)
    return list(zip(accs, dates))

def parse_13f(cik, accession):
    acc_no = accession.replace('-', '')
    idx_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no}/"
    try:
        idx = fetch(idx_url).decode()
    except Exception:
        return {}
    xmls = re.findall(r'href="([^"]+\.xml)"', idx)
    info_xml = [x for x in xmls if 'primary_doc' not in x.lower()]
    if not info_xml:
        return {}
    xml_url = ("https://www.sec.gov" + info_xml[0]
               if info_xml[0].startswith('/') else idx_url + info_xml[0])
    try:
        data = fetch(xml_url)
        ns = {'x': 'http://www.sec.gov/edgar/document/thirteenf/informationtable'}
        root = ET.fromstring(data)
        holdings = defaultdict(int)
        for it in root.findall('x:infoTable', ns):
            name_el = it.find('x:nameOfIssuer', ns)
            shares_el = it.find('x:shrsOrPrnAmt/x:sshPrnamt', ns)
            if name_el is None or shares_el is None:
                continue
            name = (name_el.text or '').strip().upper()
            try:
                shares = int(shares_el.text)
            except (TypeError, ValueError):
                continue
            holdings[name] += shares
        return dict(holdings)
    except Exception:
        return {}

def match_shares(holdings, ticker):
    names = TICKER_NAME.get(ticker.upper(), [ticker.upper()])
    return sum(pos for issuer, pos in holdings.items()
               if any(n in issuer for n in names))

def classify_signal(delta_per_faction):
    """delta_per_faction: {'value': 'buy'|'sell'|'neutral', ...}"""
    buying = {f for f, d in delta_per_faction.items() if d == 'buy'}
    selling = {f for f, d in delta_per_faction.items() if d == 'sell'}
    if len(buying) >= 3:
        return 'Triple-Buy'
    if len(buying) == 2:
        return 'Double-Buy'
    if len(buying) == 1 and not selling:
        return 'Single-Buy'
    if len(selling) >= 2:
        return 'Multi-Exit'
    return None

def compute_signal(ticker, all_filings, q_idx):
    """For quarter q_idx (0=latest), compute resonance vs q_idx+1"""
    faction_action = defaultdict(list)  # faction -> list of actions
    for mgr, (_, faction) in MANAGERS.items():
        filings = all_filings.get(mgr, [])
        if q_idx + 1 >= len(filings):
            continue
        h_new = filings[q_idx][2]
        h_old = filings[q_idx + 1][2]
        s_new = match_shares(h_new, ticker)
        s_old = match_shares(h_old, ticker)
        if s_new == 0 and s_old == 0:
            continue
        if s_old == 0 and s_new > 0:
            action = 'buy'
        elif s_new == 0 and s_old > 0:
            action = 'sell'
        elif s_new > s_old * 1.02:
            action = 'buy'
        elif s_new < s_old * 0.98:
            action = 'sell'
        else:
            action = 'neutral'
        faction_action[faction].append(action)

    # Each faction's net: buy if majority action is buy, etc.
    net_per_faction = {}
    for faction, actions in faction_action.items():
        buys = sum(1 for a in actions if a == 'buy')
        sells = sum(1 for a in actions if a == 'sell')
        if buys > sells:
            net_per_faction[faction] = 'buy'
        elif sells > buys:
            net_per_faction[faction] = 'sell'
        else:
            net_per_faction[faction] = 'neutral'
    return classify_signal(net_per_faction), net_per_faction

def forward_return(ticker, start_date_str, months=3):
    try:
        start = datetime.strptime(start_date_str, '%Y-%m-%d')
        end = start + timedelta(days=months * 31)
        tk = yf.Ticker(ticker, session=SESSION)
        hist = tk.history(start=start.strftime('%Y-%m-%d'),
                          end=end.strftime('%Y-%m-%d'))
        if hist.empty or len(hist) < 2:
            return None
        return (hist['Close'].iloc[-1] / hist['Close'].iloc[0] - 1) * 100
    except Exception:
        return None

def main():
    n_quarters = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    universe_arg = sys.argv[2] if len(sys.argv) > 2 else (
        'NVDA,AAPL,META,TSM,CVX,MU,OXY,AMD,GOOGL,MSFT,JNJ,XOM,AMZN,MSTR')
    universe = [t.strip().upper() for t in universe_arg.split(',')]

    print(f"[1/3] Fetching 13F filings for {len(MANAGERS)} funds × {n_quarters + 1} quarters...")
    all_filings = {}
    for mgr, (cik, _) in MANAGERS.items():
        print(f"      {mgr}...", end=' ', flush=True)
        listings = get_13f_filings(cik, max_filings=n_quarters + 2)[:n_quarters + 1]
        parsed = []
        for acc, date in listings:
            h = parse_13f(cik, acc)
            parsed.append((acc, date, h))
        all_filings[mgr] = parsed
        print(f"{len(parsed)} filings")

    print(f"\n[2/3] Scoring {len(universe)} tickers × {n_quarters} quarters...")
    results = []
    for q in range(n_quarters):
        filing_dates = []
        for mgr in all_filings:
            if q < len(all_filings[mgr]):
                filing_dates.append(all_filings[mgr][q][1])
        if not filing_dates:
            continue
        ref_date = max(filing_dates)

        for ticker in universe:
            signal, _ = compute_signal(ticker, all_filings, q)
            if signal is None:
                continue
            ret = forward_return(ticker, ref_date, months=3)
            spy_ret = forward_return('SPY', ref_date, months=3)
            if ret is None or spy_ret is None:
                continue
            results.append({
                'quarter': ref_date, 'ticker': ticker, 'signal': signal,
                'fwd_ret': ret, 'spy_ret': spy_ret, 'alpha': ret - spy_ret,
            })

    print(f"\n[3/3] 聚合统计（{len(results)} 个 (quarter, ticker) 样本）\n")

    print(f"{'Signal':<14}{'N':>5}{'AvgFwd%':>10}{'SPY%':>10}{'Alpha%':>10}{'HitRate':>10}{'Median α%':>12}")
    print("-" * 75)

    by_signal = defaultdict(list)
    for r in results:
        by_signal[r['signal']].append(r)

    for sig in ['Triple-Buy', 'Double-Buy', 'Single-Buy', 'Multi-Exit']:
        rs = by_signal.get(sig, [])
        if not rs:
            print(f"{sig:<14}{0:>5}  (no samples)")
            continue
        n = len(rs)
        avg_ret = sum(r['fwd_ret'] for r in rs) / n
        avg_spy = sum(r['spy_ret'] for r in rs) / n
        avg_alpha = sum(r['alpha'] for r in rs) / n
        hits = sum(1 for r in rs if r['alpha'] > 0)
        sorted_alphas = sorted([r['alpha'] for r in rs])
        median = sorted_alphas[n // 2]
        print(f"{sig:<14}{n:>5}{avg_ret:>9.1f}%{avg_spy:>9.1f}%{avg_alpha:>9.1f}%"
              f"{hits:>4}/{n:<4}{median:>11.1f}%")

    print("\n详细案例（按 alpha 排序）:")
    print(f"{'Quarter':<12}{'Ticker':<7}{'Signal':<14}{'FwdRet':>10}{'SPYRet':>10}{'Alpha':>10}")
    print("-" * 65)
    for r in sorted(results, key=lambda x: -x['alpha']):
        print(f"{r['quarter']:<12}{r['ticker']:<7}{r['signal']:<14}"
              f"{r['fwd_ret']:>9.1f}%{r['spy_ret']:>9.1f}%{r['alpha']:>9.1f}%")

    print("\n=== 解读提示 ===")
    print("若 Triple-Buy 平均 alpha > 0 且 hit rate > 60%：方法论有效，继续重仓用")
    print("若 Triple-Buy 平均 alpha ≈ 0：方法论无独立 alpha，退化为 SPY 伪装")
    print("若 Triple-Buy 平均 alpha < 0：方法论反向 — 立刻停用")
    print("样本 <10 不具统计显著性，需扩大 universe 或 quarter 数")

if __name__ == '__main__':
    main()

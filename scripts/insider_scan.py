#!/usr/bin/env python3
"""SEC Form 4 内部人交易扫描 — 补足 13F 的 45 天延迟

用法: python3 insider_scan.py [TICKER1,TICKER2,...] [lookback_days]
默认: holdings 全量 + 90 天回看
"""
import sys, re, time, json, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta

UA = {"User-Agent": "DMO Research research-contact@gmail.com"}
TICKER_CIK_URL = "https://www.sec.gov/files/company_tickers.json"

def fetch(url, retries=3):
    for i in range(retries):
        try:
            time.sleep(0.15)  # SEC rate limit: 10 req/s max
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=30).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and i < retries - 1:
                time.sleep(2 ** i); continue
            raise

def load_ticker_cik_map():
    data = json.loads(fetch(TICKER_CIK_URL).decode())
    return {v['ticker'].upper(): str(v['cik_str']).zfill(10) for v in data.values()}

def get_recent_form4s(cik, lookback_days=90):
    url = (f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}"
           f"&type=4&dateb=&owner=include&count=60&output=atom")
    try:
        data = fetch(url).decode()
    except Exception:
        return []
    accs = re.findall(r'<accession-number>([\d-]+)</accession-number>', data)
    dates = re.findall(r'<filing-date>([\d-]+)</filing-date>', data)
    cutoff = datetime.now() - timedelta(days=lookback_days)
    return [(a, d) for a, d in zip(accs, dates)
            if datetime.strptime(d, '%Y-%m-%d') >= cutoff]

def parse_form4(cik, accession):
    acc_no = accession.replace('-', '')
    idx_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no}/"
    try:
        idx = fetch(idx_url).decode()
    except Exception:
        return None
    xml_files = re.findall(r'href="([^"]+\.xml)"', idx)
    xml_files.sort(key=lambda x: (0 if 'form4' in x.lower() or 'edgar' in x.lower() else 1, x))
    if not xml_files:
        return None
    xml_url = ("https://www.sec.gov" + xml_files[0]
               if xml_files[0].startswith('/') else idx_url + xml_files[0])
    try:
        data = fetch(xml_url)
        root = ET.fromstring(data)
    except Exception:
        return None

    owner_name = root.findtext('.//reportingOwner/reportingOwnerId/rptOwnerName', '') or ''
    is_director = root.findtext('.//reportingOwnerRelationship/isDirector', '0')
    is_officer = root.findtext('.//reportingOwnerRelationship/isOfficer', '0')
    officer_title = root.findtext('.//reportingOwnerRelationship/officerTitle', '') or ''
    is_ten_pct = root.findtext('.//reportingOwnerRelationship/isTenPercentOwner', '0')

    def truthy(x):
        return x in ('1', 'true', 'True')

    txns = []
    for t in root.findall('.//nonDerivativeTransaction'):
        code = t.findtext('.//transactionCoding/transactionCode', '') or ''
        shares = t.findtext('.//transactionAmounts/transactionShares/value', '0') or '0'
        price = t.findtext('.//transactionAmounts/transactionPricePerShare/value', '0') or '0'
        try:
            txns.append({'code': code, 'shares': float(shares), 'price': float(price)})
        except ValueError:
            continue

    return {
        'owner': owner_name,
        'is_officer': truthy(is_officer),
        'is_director': truthy(is_director),
        'is_ten_pct': truthy(is_ten_pct),
        'title': officer_title,
        'transactions': txns,
    }

def analyze_ticker(ticker, cik_map, lookback_days=90):
    cik = cik_map.get(ticker.upper())
    if not cik:
        return {'ticker': ticker, 'error': 'CIK not found'}

    filings = get_recent_form4s(cik, lookback_days)
    total_buy_value = 0.0
    total_sell_value = 0.0
    c_suite_buys = []
    c_suite_sells = []
    insiders = set()

    for acc, date in filings:
        d = parse_form4(cik, acc)
        if not d:
            continue
        insiders.add(d['owner'])
        title_lower = d['title'].lower()
        is_c_suite = (d['is_officer'] and
                      any(k in title_lower for k in
                          ['chief', 'ceo', 'cfo', 'coo', 'president']))

        for tx in d['transactions']:
            value = tx['shares'] * tx['price']
            # P = open market purchase, S = open market sale (real economic signal)
            # A/M (award/option exercise) not counted (not discretionary buy)
            if tx['code'] == 'P' and value > 0:
                total_buy_value += value
                if is_c_suite:
                    c_suite_buys.append({
                        'date': date, 'title': d['title'], 'owner': d['owner'],
                        'shares': tx['shares'], 'value': value,
                    })
            elif tx['code'] == 'S' and value > 0:
                total_sell_value += value
                if is_c_suite:
                    c_suite_sells.append({
                        'date': date, 'title': d['title'], 'owner': d['owner'],
                        'shares': tx['shares'], 'value': value,
                    })

    return {
        'ticker': ticker,
        'filings': len(filings),
        'unique_insiders': len(insiders),
        'buy_usd': total_buy_value,
        'sell_usd': total_sell_value,
        'net_usd': total_buy_value - total_sell_value,
        'c_suite_buys': c_suite_buys,
        'c_suite_sells': c_suite_sells,
    }

def signal_label(r):
    if r.get('error'):
        return r['error']
    if r['c_suite_buys']:
        total_csb = sum(b['value'] for b in r['c_suite_buys'])
        return f"🔥 {len(r['c_suite_buys'])} C-suite buys (${total_csb/1e3:.0f}K)"
    if r['net_usd'] > 500_000:
        return "🟢 net insider buying"
    if r['net_usd'] < -5_000_000:
        return "🔴 heavy insider selling"
    if r['c_suite_sells'] and not r['c_suite_buys']:
        total_css = sum(s['value'] for s in r['c_suite_sells'])
        return f"⚠️ {len(r['c_suite_sells'])} C-suite sells (${total_css/1e3:.0f}K)"
    return "—"

def main():
    tickers = (sys.argv[1] if len(sys.argv) > 1
               else 'NVDA,SPY,AAPL,META,TSM,CVX,GLD,SCHD,MU,OXY,AMD').split(',')
    lookback = int(sys.argv[2]) if len(sys.argv) > 2 else 90

    print(f"Loading SEC ticker-CIK map...")
    cik_map = load_ticker_cik_map()

    print(f"\nInsider scan: {len(tickers)} tickers × {lookback}d lookback")
    print(f"{'Ticker':<8}{'Filings':>8}{'Insiders':>10}{'Buy $K':>10}{'Sell $K':>10}{'Net $K':>10}  Signal")
    print("-" * 90)

    all_c_suite_buys = []
    all_c_suite_sells = []
    for t in tickers:
        t = t.strip().upper()
        try:
            r = analyze_ticker(t, cik_map, lookback)
            if r.get('error'):
                print(f"{t:<8} {r['error']}")
                continue
            print(f"{t:<8}{r['filings']:>8}{r['unique_insiders']:>10}"
                  f"{r['buy_usd']/1e3:>10.0f}{r['sell_usd']/1e3:>10.0f}"
                  f"{r['net_usd']/1e3:>10.0f}  {signal_label(r)}")
            for b in r['c_suite_buys']:
                all_c_suite_buys.append((t, b))
            for s in r['c_suite_sells']:
                all_c_suite_sells.append((t, s))
        except Exception as e:
            print(f"{t:<8} ERROR {type(e).__name__}: {str(e)[:60]}")

    if all_c_suite_buys:
        print(f"\n🔥 C-suite BUYS (最近 {lookback} 天):")
        for ticker, b in sorted(all_c_suite_buys, key=lambda x: -x[1]['value']):
            print(f"  {ticker:<6} {b['date']}: {b['title']:<30} {b['owner']:<25} "
                  f"{b['shares']:>10,.0f} sh @ ${b['price'] if 'price' in b else b['value']/b['shares']:.2f} = ${b['value']/1e3:.0f}K")

    if all_c_suite_sells:
        print(f"\n⚠️  C-suite SELLS (最近 {lookback} 天):")
        for ticker, s in sorted(all_c_suite_sells, key=lambda x: -x[1]['value'])[:20]:
            print(f"  {ticker:<6} {s['date']}: {s['title']:<30} {s['owner']:<25} "
                  f"{s['shares']:>10,.0f} sh = ${s['value']/1e3:.0f}K")

if __name__ == '__main__':
    main()

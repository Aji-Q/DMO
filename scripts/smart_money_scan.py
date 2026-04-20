#!/usr/bin/env python3
"""SEC 13F 机构持仓追踪 - 免费替代 WhaleWisdom"""
import sys, re, time, urllib.request, xml.etree.ElementTree as ET
from collections import defaultdict

UA = {"User-Agent": "Portfolio Research research-contact@gmail.com"}

MANAGERS = {
    'Berkshire (Buffett)': '0001067983',
    'Scion (Burry)':       '0001649339',
    'Pershing (Ackman)':   '0001336528',
    'Appaloosa (Tepper)':  '0001656456',
    'Bridgewater (Dalio)': '0001350694',
    'Renaissance':         '0001037389',
    'Third Point (Loeb)':  '0001040273',
    'Tiger Global':        '0001167483',
}

TICKER_TO_NAME = {
    'NVDA': ['NVIDIA'], 'AAPL': ['APPLE INC'], 'META': ['META PLATFORMS'],
    'TSM':  ['TAIWAN SEMICONDUCTOR'], 'CVX': ['CHEVRON CORP'],
    'GOOGL':['ALPHABET'], 'MSFT': ['MICROSOFT'], 'AMZN': ['AMAZON'],
}

def fetch(url, retries=3):
    for i in range(retries):
        try:
            time.sleep(0.2)
            req = urllib.request.Request(url, headers=UA)
            return urllib.request.urlopen(req, timeout=20).read()
        except urllib.error.HTTPError as e:
            if e.code == 503 and i < retries - 1:
                time.sleep(2 ** i); continue
            raise

def get_recent_13f(cik):
    url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=13F-HR&dateb=&owner=include&count=5&output=atom"
    data = fetch(url).decode()
    accs = re.findall(r'<accession-number>([\d-]+)</accession-number>', data)
    dates = re.findall(r'<filing-date>([\d-]+)</filing-date>', data)
    return list(zip(accs, dates))[:2]

def parse_13f(cik, accession):
    acc_no = accession.replace('-', '')
    idx_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_no}/"
    idx = fetch(idx_url).decode()
    xmls = re.findall(r'href="([^"]+\.xml)"', idx)
    info_xml = [x for x in xmls if 'primary_doc' not in x.lower()]
    if not info_xml: return {}
    xml_url = "https://www.sec.gov" + info_xml[0] if info_xml[0].startswith('/') else idx_url + info_xml[0]
    data = fetch(xml_url)
    ns = {'x': 'http://www.sec.gov/edgar/document/thirteenf/informationtable'}
    root = ET.fromstring(data)
    holdings = defaultdict(lambda: {'shares':0, 'value':0})
    for it in root.findall('x:infoTable', ns):
        name = it.find('x:nameOfIssuer', ns).text.strip().upper()
        shares = int(it.find('x:shrsOrPrnAmt/x:sshPrnamt', ns).text)
        value = int(it.find('x:value', ns).text)
        holdings[name]['shares'] += shares
        holdings[name]['value'] += value
    return dict(holdings)

def match_ticker(holdings, ticker):
    keywords = TICKER_TO_NAME.get(ticker, [ticker])
    return sum(pos['shares'] for issuer, pos in holdings.items()
               if any(kw in issuer for kw in keywords))

def fmt_change(s_new, s_old):
    if s_new == 0 and s_old == 0: return "—"
    if s_old == 0: return f"{s_new/1e6:.1f}M NEW"
    if s_new == 0: return "EXIT"
    delta_pct = (s_new - s_old) / s_old * 100
    sign = "+" if delta_pct >= 0 else ""
    arrow = "^" if delta_pct > 2 else "v" if delta_pct < -2 else "="
    return f"{s_new/1e6:.1f}M {arrow}{sign}{delta_pct:.0f}%"

def main():
    tickers = (sys.argv[1] if len(sys.argv)>1 else 'NVDA,AAPL,META,TSM,CVX').split(',')
    tickers = [t.strip().upper() for t in tickers]
    print(f"{'Manager':<22}{'Filed':<12}", end='')
    for t in tickers: print(f"{t:>14}", end='')
    print()
    print("-" * (34 + 14*len(tickers)))
    for mgr_name, cik in MANAGERS.items():
        try:
            filings = get_recent_13f(cik)
            if len(filings) < 2:
                print(f"{mgr_name:<22} (insufficient data)"); continue
            q_new, date_new = filings[0]; q_old, date_old = filings[1]
            h_new = parse_13f(cik, q_new); h_old = parse_13f(cik, q_old)
            print(f"{mgr_name:<22}{date_new:<12}", end='')
            for t in tickers:
                print(f"{fmt_change(match_ticker(h_new, t), match_ticker(h_old, t)):>14}", end='')
            print()
        except Exception as e:
            print(f"{mgr_name:<22} ERROR: {type(e).__name__}: {str(e)[:50]}")

if __name__ == '__main__':
    main()

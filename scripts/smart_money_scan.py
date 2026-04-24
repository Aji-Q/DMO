#!/usr/bin/env python3
"""SEC 13F 机构持仓追踪 — 免费替代 WhaleWisdom

v2 升级（2026-04-24）：
- 用 CUSIP 主匹配 + issuer name 备选匹配（修复 OXY/Berkshire 等漏匹配）
- Debug 模式打印实际匹配到的 issuer name 变体，便于诊断
"""
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

# CUSIP = 9 位唯一识别码，13F 原始字段，跨所有 filer 一致
# name_variants = 已知 issuer name 变体（作为 CUSIP 备选）
TICKER_META = {
    'NVDA':  {'cusip': '67066G104', 'names': ['NVIDIA']},
    'SPY':   {'cusip': '78462F103', 'names': ['SPDR S&P 500', 'SPDR S&P500']},
    'AAPL':  {'cusip': '037833100', 'names': ['APPLE INC']},
    'META':  {'cusip': '30303M102', 'names': ['META PLATFORMS']},
    'TSM':   {'cusip': '874039100', 'names': ['TAIWAN SEMICONDUCTOR']},
    'CVX':   {'cusip': '166764100', 'names': ['CHEVRON CORP', 'CHEVRON CORPORATION', 'CHEVRON NEW']},
    'GLD':   {'cusip': '78463V107', 'names': ['SPDR GOLD']},
    'SCHD':  {'cusip': '808524797', 'names': ['SCHWAB US DIVIDEND']},
    'MU':    {'cusip': '595112103', 'names': ['MICRON']},
    # OXY 有多种变体：OCCIDENTAL PETROLEUM CORP / OCCIDENTAL PETE CORP / OCCIDENTAL PETE CORP NEW
    'OXY':   {'cusip': '674599105', 'names': ['OCCIDENTAL PETROLEUM', 'OCCIDENTAL PETE']},
    'AMD':   {'cusip': '007903107', 'names': ['ADVANCED MICRO DEVICES']},
    'GOOGL': {'cusip': '02079K305', 'names': ['ALPHABET INC CL A', 'ALPHABET INC A', 'ALPHABET CL A']},
    'GOOG':  {'cusip': '02079K107', 'names': ['ALPHABET INC CL C', 'ALPHABET INC C', 'ALPHABET CL C']},
    'MSFT':  {'cusip': '594918104', 'names': ['MICROSOFT']},
    'AMZN':  {'cusip': '023135106', 'names': ['AMAZON COM', 'AMAZON.COM']},
    'JNJ':   {'cusip': '478160104', 'names': ['JOHNSON & JOHNSON']},
    'XOM':   {'cusip': '30231G102', 'names': ['EXXON MOBIL']},
    'MSTR':  {'cusip': '594972408', 'names': ['MICROSTRATEGY', 'STRATEGY INC']},  # CUSIP 2025 年改名可能变
    'AVGO':  {'cusip': '11135F101', 'names': ['BROADCOM']},
    'COIN':  {'cusip': '19260Q107', 'names': ['COINBASE']},
    'PLTR':  {'cusip': '69608A108', 'names': ['PALANTIR']},
    'SMCI':  {'cusip': '86800U302', 'names': ['SUPER MICRO']},
    'TSLA':  {'cusip': '88160R101', 'names': ['TESLA']},
    'NFLX':  {'cusip': '64110L106', 'names': ['NETFLIX']},
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
    """返回 {(issuer_name, cusip): {'shares': n, 'value': v}}"""
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
    holdings = defaultdict(lambda: {'shares': 0, 'value': 0})
    for it in root.findall('x:infoTable', ns):
        name_el = it.find('x:nameOfIssuer', ns)
        cusip_el = it.find('x:cusip', ns)
        shares_el = it.find('x:shrsOrPrnAmt/x:sshPrnamt', ns)
        value_el = it.find('x:value', ns)
        if name_el is None or shares_el is None:
            continue
        name = (name_el.text or '').strip().upper()
        cusip = (cusip_el.text or '').strip().upper() if cusip_el is not None else ''
        try:
            shares = int(shares_el.text)
            value = int(value_el.text) if value_el is not None else 0
        except (TypeError, ValueError):
            continue
        key = (name, cusip)
        holdings[key]['shares'] += shares
        holdings[key]['value'] += value
    return dict(holdings)

def match_ticker(holdings, ticker, debug=False):
    """CUSIP 主匹配 + name 备选匹配"""
    meta = TICKER_META.get(ticker.upper(), {})
    target_cusip = meta.get('cusip', '').upper()
    target_names = [n.upper() for n in meta.get('names', [ticker.upper()])]

    total_shares = 0
    matched_variants = []
    for (name, cusip), pos in holdings.items():
        matched = False
        # CUSIP 优先（精确匹配）
        if target_cusip and cusip == target_cusip:
            matched = True
        # name 备选：必须 startswith（避免 "APPLE INC" 误匹配到 "MAUI LD & PINEAPPLE INC"）
        # 仅当 holding 本身没有 CUSIP（rare）或我们的 map 没 CUSIP 时使用
        elif (not cusip or not target_cusip) and any(name.startswith(tn) for tn in target_names):
            matched = True
        if matched:
            total_shares += pos['shares']
            if debug and (name, cusip) not in matched_variants:
                matched_variants.append((name, cusip))

    if debug and matched_variants:
        for n, c in matched_variants:
            print(f"    [debug] {ticker} matched: {n[:40]:<40} CUSIP={c}", file=sys.stderr)
    return total_shares

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
    debug = '--debug' in sys.argv

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
                print(f"{fmt_change(match_ticker(h_new, t, debug=debug), match_ticker(h_old, t)):>14}", end='')
            print()
        except Exception as e:
            print(f"{mgr_name:<22} ERROR: {type(e).__name__}: {str(e)[:50]}")

    if debug:
        print("\n[debug] 运行完成。检查 stderr 看每只股匹配到的 issuer name + CUSIP。", file=sys.stderr)

if __name__ == '__main__':
    main()

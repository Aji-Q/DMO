#!/usr/bin/env python3
"""宏观情绪 / 风险环境扫描 — VIX / 信用利差 / 收益率曲线 / 相对强度

给每份 DMO 周报加一个"宏观环境"上下文（Risk ON / OFF / Neutral），
帮助判断当前是追涨安全的环境 vs 该减仓防御的环境。

数据源：yfinance（全免费）
"""
import sys
import yfinance as yf
import pandas as pd
from curl_cffi import requests

SESSION = requests.Session(impersonate="chrome")

# 宏观指标池
INDICATORS = {
    # 波动率
    'VIX':   ('^VIX',   '恐慌指数（SPX 30d IV）'),
    'VVIX':  ('^VVIX',  'VIX 的 VIX（恐慌的恐慌）'),
    'VXN':   ('^VXN',   'Nasdaq 100 恐慌指数'),
    'GVZ':   ('^GVZ',   'GLD 恐慌指数（黄金隐波）'),
    # 信用利差（代理）
    'HYG':   ('HYG',    '高收益债 ETF'),
    'LQD':   ('LQD',    '投资级债 ETF'),
    # 收益率曲线
    'TLT':   ('TLT',    '20Y+ 国债'),
    'SHY':   ('SHY',    '1-3Y 国债'),
    # 大盘 & 板块轮动
    'SPY':   ('SPY',    'S&P 500'),
    'IWM':   ('IWM',    'Russell 2000 小盘'),
    'QQQ':   ('QQQ',    'Nasdaq 100'),
    'XLK':   ('XLK',    '科技板块'),
    'XLE':   ('XLE',    '能源板块'),
    'XLU':   ('XLU',    '公用事业（防御）'),
    # 美元 & 大宗
    'UUP':   ('UUP',    '美元指数 ETF'),
    'GLD':   ('GLD',    '黄金'),
    'USO':   ('USO',    '原油'),
}

def fetch(ticker, period='3mo'):
    try:
        tk = yf.Ticker(ticker, session=SESSION)
        h = tk.history(period=period)
        if h.empty:
            return None
        return h
    except Exception:
        return None

def compute_change(h, days):
    """h: DataFrame with 'Close'. days: 回看天数"""
    if h is None or len(h) < days + 1:
        return None
    return (h['Close'].iloc[-1] / h['Close'].iloc[-(days+1)] - 1) * 100

def compute_percentile_52w(h):
    """当前值在过去 52 周（~252 日）的百分位"""
    if h is None or len(h) < 60:
        return None
    window = h['Close'].tail(252)
    current = window.iloc[-1]
    rank = (window <= current).sum() / len(window) * 100
    return rank

def classify_risk_regime(data):
    """根据核心指标分类风险环境"""
    vix = data.get('VIX', {}).get('close')
    vix_5d = data.get('VIX', {}).get('chg_5d')
    hyg_5d = data.get('HYG', {}).get('chg_5d')
    lqd_5d = data.get('LQD', {}).get('chg_5d')
    spy_5d = data.get('SPY', {}).get('chg_5d')

    if vix is None or hyg_5d is None:
        return ("❓ 数据不足", "无法分类")

    # HYG/LQD 变化差 = 信用利差变化代理
    credit_spread_chg = (lqd_5d - hyg_5d) if (lqd_5d is not None and hyg_5d is not None) else None

    # 硬规则分类
    if vix < 15 and hyg_5d > 0 and (credit_spread_chg is None or credit_spread_chg < 0.5):
        return ("🟢 Risk ON",
                "VIX <15 低位 + 高收益债走强 + 信用利差稳定。市场贪婪，"
                "SOP 在此环境可适度追涨多头持仓，但要警惕均值回归。")
    elif vix > 25 or hyg_5d < -1.5 or (credit_spread_chg and credit_spread_chg > 1.0):
        return ("🔴 Risk OFF",
                "VIX 激增 或 高收益债大跌 或 信用利差走阔 >1%。"
                "SOP 在此环境应减仓多头、提高现金、加仓防御 (SCHD/GLD)。")
    elif vix > 20 and hyg_5d < -0.5:
        return ("🟠 Caution",
                "VIX 偏高 + 信用有压力，偏向谨慎。"
                "SOP 暂缓加仓，监控止损线。")
    else:
        return ("🟡 Neutral",
                "无明显 Risk ON/OFF 信号。按正常 SOP 执行，"
                "所有操作都要配合止损。")

def main():
    print("拉取宏观情绪指标...", flush=True)
    data = {}
    for key, (ticker, desc) in INDICATORS.items():
        h = fetch(ticker)
        if h is None:
            data[key] = {'close': None, 'desc': desc}
            continue
        data[key] = {
            'close': float(h['Close'].iloc[-1]),
            'chg_1d': compute_change(h, 1),
            'chg_5d': compute_change(h, 5),
            'chg_20d': compute_change(h, 20),
            'pct_52w': compute_percentile_52w(h),
            'desc': desc,
        }

    # 输出主表
    print(f"\n{'指标':<8}{'最新值':>10}{'1D%':>8}{'5D%':>8}{'20D%':>8}{'52w分位':>10}  说明")
    print("-" * 90)
    for key in INDICATORS.keys():
        d = data.get(key)
        if d is None or d['close'] is None:
            print(f"{key:<8}  无数据                                        {INDICATORS[key][1]}")
            continue
        chg1 = f"{d['chg_1d']:+.1f}%" if d['chg_1d'] is not None else "—"
        chg5 = f"{d['chg_5d']:+.1f}%" if d['chg_5d'] is not None else "—"
        chg20 = f"{d['chg_20d']:+.1f}%" if d['chg_20d'] is not None else "—"
        pct = f"{d['pct_52w']:.0f}%" if d['pct_52w'] is not None else "—"
        print(f"{key:<8}{d['close']:>10.2f}{chg1:>8}{chg5:>8}{chg20:>8}{pct:>10}  {d['desc']}")

    # 派生比率
    print('\n派生比率:')
    if data.get('HYG', {}).get('close') and data.get('LQD', {}).get('close'):
        hyg_lqd = data['HYG']['close'] / data['LQD']['close']
        hyg_5d = data['HYG'].get('chg_5d', 0) or 0
        lqd_5d = data['LQD'].get('chg_5d', 0) or 0
        credit_proxy = lqd_5d - hyg_5d
        print(f"  HYG/LQD = {hyg_lqd:.4f}（信用利差代理，下降=信用利好）")
        print(f"  LQD 5D - HYG 5D = {credit_proxy:+.2f}%（>1% 提示信用利差走阔）")
    if data.get('TLT', {}).get('close') and data.get('SHY', {}).get('close'):
        tlt_shy = data['TLT']['close'] / data['SHY']['close']
        print(f"  TLT/SHY = {tlt_shy:.4f}（收益率曲线代理，下降=短期 > 长期 = 倒挂）")
    if data.get('QQQ', {}).get('chg_20d') is not None and data.get('SPY', {}).get('chg_20d') is not None:
        qqq_spy_rel = data['QQQ']['chg_20d'] - data['SPY']['chg_20d']
        print(f"  QQQ 20D - SPY 20D = {qqq_spy_rel:+.2f}%（>0 = 科技相对强势）")
    if data.get('IWM', {}).get('chg_20d') is not None and data.get('SPY', {}).get('chg_20d') is not None:
        iwm_spy_rel = data['IWM']['chg_20d'] - data['SPY']['chg_20d']
        print(f"  IWM 20D - SPY 20D = {iwm_spy_rel:+.2f}%（>0 = 小盘相对强势 = 风险偏好高）")

    # 风险环境分类
    regime, note = classify_risk_regime(data)
    print(f'\n=== 当前风险环境: {regime} ===')
    print(f"  {note}")
    print('\n规则（供 DMO agent 整合进周报）:')
    print('  🟢 Risk ON  → 追涨安全，多头持仓可加，对冲可减')
    print('  🟡 Neutral  → 正常 SOP 执行，标配风控')
    print('  🟠 Caution  → 暂缓加仓，监控止损')
    print('  🔴 Risk OFF → 减仓多头，提高现金，加仓 SCHD/GLD')

if __name__ == '__main__':
    main()

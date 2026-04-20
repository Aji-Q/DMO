#!/usr/bin/env python3
"""持仓技术面扫描 - 用法: python3 portfolio_scan.py [NVDA,SPY,...]"""
import sys
import yfinance as yf
import pandas as pd
from curl_cffi import requests

SESSION = requests.Session(impersonate="chrome")

def wilder(s, period=14):
    return s.ewm(alpha=1/period, adjust=False).mean()

def analyze(t):
    h = yf.Ticker(t, session=SESSION).history(period="1y")
    if h.empty:
        return None
    c, hi, lo, v = h['Close'], h['High'], h['Low'], h['Volume']
    price = c.iloc[-1]
    ema50 = c.ewm(span=50, adjust=False).mean().iloc[-1]
    ema200 = c.ewm(span=200, adjust=False).mean().iloc[-1]
    tr = pd.concat([hi-lo, (hi-c.shift()).abs(), (lo-c.shift()).abs()], axis=1).max(axis=1)
    atr = wilder(tr).iloc[-1]
    d = c.diff()
    rsi = (100 - 100/(1 + wilder(d.where(d>0,0))/wilder(-d.where(d<0,0)))).iloc[-1]
    if price > ema50 > ema200:   trend = "多头"
    elif price < ema50 < ema200: trend = "空头"
    else:                        trend = "盘整"
    bb_mid = c.rolling(20).mean().iloc[-1]
    bb_std = c.rolling(20).std().iloc[-1]
    bb_upper, bb_lower = bb_mid + 2*bb_std, bb_mid - 2*bb_std
    bb_pos = (price - bb_lower) / (bb_upper - bb_lower) * 100
    vol_ratio = v.iloc[-1] / v.tail(20).mean()
    return dict(
        ticker=t, price=price, ema50=ema50, ema200=ema200,
        atr=atr, atr_pct=atr/price*100, rsi=rsi, trend=trend,
        stop_atr=price - 1.5*atr,
        sup60=c.tail(60).min(), res60=c.tail(60).max(),
        bb_pos=bb_pos, vol_ratio=vol_ratio,
    )

tickers = (sys.argv[1] if len(sys.argv)>1 else 'NVDA,SPY,AAPL,GLD,SCHD,TSM,META,CVX').split(',')

print(f"{'T':<6}{'Price':>8}{'EMA50':>8}{'EMA200':>8}{'ATR%':>6}{'RSI':>6}  {'Trend':<6}{'ATR-Stop':>10}{'BB%':>6}{'Vol':>6}")
print("-" * 78)
for t in tickers:
    try:
        r = analyze(t.strip())
        if r:
            print(f"{r['ticker']:<6}{r['price']:>8.2f}{r['ema50']:>8.2f}{r['ema200']:>8.2f}"
                  f"{r['atr_pct']:>5.1f}%{r['rsi']:>6.1f}  {r['trend']:<6}{r['stop_atr']:>10.2f}"
                  f"{r['bb_pos']:>5.0f}%{r['vol_ratio']:>5.1f}x")
    except Exception as e:
        print(f"{t:<6} ERROR {type(e).__name__}: {str(e)[:40]}")

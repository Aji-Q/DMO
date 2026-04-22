#!/usr/bin/env python3
"""账户资产变化折线图 — 可持续运行的每日估值引擎

读取 data/transactions.csv（append-only ledger）+ yfinance 历史价格，
生成每日净值曲线 + matplotlib 折线图 + SPY benchmark 对比。

用法:
    python3 scripts/track_portfolio.py                    # 估值区间 = 首次 DEPOSIT → 今天
    python3 scripts/track_portfolio.py --end 2026-05-31   # 指定结束日期

输出:
    data/daily_valuation.csv                              # 每日净值（覆盖，每次全量重算，保证幂等）
    reports/YYYY-MM-DD-portfolio-chart.png                # 日期版图表（快照归档）
    reports/portfolio-chart-latest.png                    # 最新版图表（易访问）

每次新交易后，append 一行到 transactions.csv 再跑本脚本即可，历史曲线自动扩展。
"""
import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf
from curl_cffi import requests

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    # macOS 中文字体：PingFang 在 .ttc 不被 matplotlib 识别，改用 Arial Unicode MS（包含中日韩）
    plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "Heiti TC", "Songti SC", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
except ImportError:
    print("ERROR: matplotlib 未安装。运行: pip install matplotlib")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from calculate_fees import calculate_moomoo_fees

REPO_ROOT = Path(__file__).resolve().parent.parent
TX_CSV = REPO_ROOT / "data" / "transactions.csv"
OUT_CSV = REPO_ROOT / "data" / "daily_valuation.csv"
REPORTS_DIR = REPO_ROOT / "reports"

# 现金利息：默认不自动按日复利（moomoo cash sweep 生效时间与比例难预测）
# 用户可以在 transactions.csv 手动追加 INTEREST 行，按 moomoo 对账实际数录入
# 如果希望开启自动复利，把 CASH_APY 改成 0.0335
CASH_APY = 0.0
DAILY_INTEREST_RATE = CASH_APY / 365

SESSION = requests.Session(impersonate="chrome")


def load_transactions() -> pd.DataFrame:
    """读取流水，解析日期时间。"""
    df = pd.read_csv(TX_CSV)
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time_et"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("datetime").reset_index(drop=True)
    return df


def fetch_price_history(tickers: list[str], start: datetime, end: datetime) -> pd.DataFrame:
    """一次性拉取所有 ticker 的历史日收盘价。返回 date × ticker 矩阵。"""
    tickers = sorted(set(t for t in tickers if t and t != "-"))
    if not tickers:
        return pd.DataFrame()
    print(f"  拉取 {len(tickers)} 个 ticker 的历史价格: {', '.join(tickers)}")
    # yfinance multi-ticker 下载
    data = yf.download(
        tickers,
        start=start - timedelta(days=5),
        end=end + timedelta(days=1),
        session=SESSION,
        progress=False,
        auto_adjust=False,
    )
    if isinstance(data.columns, pd.MultiIndex):
        prices = data["Close"]
    else:
        prices = data[["Close"]].rename(columns={"Close": tickers[0]})
    # 前向填充非交易日
    prices = prices.ffill()
    return prices


def build_daily_valuation(tx: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    """从交易流水 + 历史价格 → 每日净值曲线。"""
    start = tx["date"].min().date()
    end = datetime.now().date()

    # 所有日历日（含周末节假日，持仓值用 ffill）
    all_dates = pd.date_range(start=start, end=end, freq="D")
    daily = pd.DataFrame(index=all_dates)

    # 当前持仓 shares 字典 + 现金 + 累计手续费 + 累计利息 + 累计实现盈亏
    shares = {}  # ticker → shares
    cash = 0.0
    cum_fees = 0.0
    cum_interest = 0.0
    cum_realized = 0.0
    cost_basis = {}  # ticker → avg cost per share

    # 事件按日期聚合后逐日遍历
    tx_by_date = dict(tuple(tx.groupby(tx["date"].dt.date)))

    rows = []
    for d in all_dates:
        d_date = d.date()

        # 1. 处理当天的事件
        if d_date in tx_by_date:
            for _, row in tx_by_date[d_date].iterrows():
                action = row["action"]
                ticker = row["ticker"]
                s = float(row["shares"]) if pd.notna(row["shares"]) else 0.0
                p = float(row["price"]) if pd.notna(row["price"]) else 0.0
                gross = float(row["gross_usd"])

                if action == "DEPOSIT":
                    cash += gross
                elif action == "WITHDRAW":
                    cash -= gross
                elif action == "DIVIDEND":
                    cash += gross
                elif action == "INTEREST":
                    # 手动录入的 moomoo cash sweep 累计利息增量
                    cash += gross
                    cum_interest += gross
                elif action == "BUY":
                    fees = calculate_moomoo_fees(s, p, is_sell=False)["total"]
                    cash -= (gross + fees)
                    cum_fees += fees
                    # 更新加权平均成本
                    old_shares = shares.get(ticker, 0.0)
                    old_cost = cost_basis.get(ticker, 0.0)
                    new_total_cost = old_shares * old_cost + gross
                    new_shares = old_shares + s
                    cost_basis[ticker] = new_total_cost / new_shares if new_shares > 0 else 0.0
                    shares[ticker] = new_shares
                elif action == "SELL":
                    fees = calculate_moomoo_fees(s, p, is_sell=True)["total"]
                    cash += (gross - fees)
                    cum_fees += fees
                    # 实现盈亏 = (售价 - 平均成本) * 股数 - 手续费
                    avg_cost = cost_basis.get(ticker, 0.0)
                    realized = (p - avg_cost) * s - fees
                    cum_realized += realized
                    shares[ticker] = max(0.0, shares.get(ticker, 0.0) - s)
                    if shares[ticker] < 1e-6:
                        shares[ticker] = 0.0

        # 2. 计算当日现金利息（仅正余额）
        if cash > 0:
            interest = cash * DAILY_INTEREST_RATE
            cash += interest
            cum_interest += interest

        # 3. 估值当日持仓（用当日或最近交易日收盘价）
        securities_value = 0.0
        for ticker, sh in shares.items():
            if sh <= 0:
                continue
            if ticker in prices.columns:
                # 找 <= d 的最近有价格的日期
                available = prices[ticker].loc[:d].dropna()
                if len(available) > 0:
                    securities_value += sh * available.iloc[-1]

        total = securities_value + cash

        # 4. 未实现盈亏
        unrealized = 0.0
        for ticker, sh in shares.items():
            if sh <= 0:
                continue
            if ticker in prices.columns:
                available = prices[ticker].loc[:d].dropna()
                if len(available) > 0:
                    unrealized += sh * (available.iloc[-1] - cost_basis.get(ticker, 0.0))

        rows.append({
            "date": d_date,
            "total_assets": round(total, 4),
            "securities_value": round(securities_value, 4),
            "cash": round(cash, 4),
            "cum_fees": round(cum_fees, 4),
            "cum_interest": round(cum_interest, 4),
            "cum_realized_pnl": round(cum_realized, 4),
            "unrealized_pnl": round(unrealized, 4),
        })

    return pd.DataFrame(rows)


def build_spy_benchmark(tx: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    """SPY 买入持有基准：首次 DEPOSIT 全额买入 SPY，持有到今天。"""
    deposits = tx[tx["action"] == "DEPOSIT"]
    if deposits.empty:
        return pd.DataFrame()
    first_deposit = deposits.iloc[0]
    deposit_date = first_deposit["date"].date()
    deposit_amount = float(first_deposit["gross_usd"])

    # 以首个 DEPOSIT 当日或下一交易日 SPY 收盘价建仓
    if "SPY" not in prices.columns:
        return pd.DataFrame()
    spy_from = prices["SPY"].loc[pd.Timestamp(deposit_date):].dropna()
    if len(spy_from) == 0:
        return pd.DataFrame()
    entry_price = spy_from.iloc[0]
    shares = deposit_amount / entry_price

    # 每日净值 = shares × 当日 SPY 价格（含前填充）
    all_dates = pd.date_range(start=deposit_date, end=datetime.now().date(), freq="D")
    spy_series = prices["SPY"].reindex(all_dates, method="ffill")
    spy_bench = shares * spy_series
    return pd.DataFrame({"date": all_dates.date, "spy_benchmark": spy_bench.values})


def plot_chart(valuation: pd.DataFrame, spy_bench: pd.DataFrame, tx: pd.DataFrame, out_paths: list[Path]):
    """精简设计：总资产 vs SPY 基准 + alpha 填色；手续费横向甘特风格独立面板。"""
    # 现代化调色 + 字号
    BG = "#fafafa"
    INK = "#1a1a1a"
    MUTED = "#6b7280"
    GRID = "#e5e7eb"
    POS = "#10b981"   # 绿（跑赢）
    NEG = "#ef4444"   # 红（跑输 / 手续费）
    BENCH = "#9ca3af" # 灰（基准）

    fig = plt.figure(figsize=(14, 8), facecolor=BG)
    gs = fig.add_gridspec(2, 1, height_ratios=[5, 1], hspace=0.15)
    ax_main = fig.add_subplot(gs[0], facecolor=BG)
    ax_fees = fig.add_subplot(gs[1], sharex=ax_main, facecolor=BG)

    dates = pd.to_datetime(valuation["date"])
    total = valuation["total_assets"].values

    # ---------------- 主图 ----------------
    # SPY 基准（用日期对齐）
    if not spy_bench.empty:
        bench_dates = pd.to_datetime(spy_bench["date"])
        bench_values = spy_bench["spy_benchmark"].values

        # 用共同时间轴对齐两条曲线（取交集以画 alpha 填色）
        bench_series = pd.Series(bench_values, index=bench_dates)
        total_series = pd.Series(total, index=dates)
        aligned = pd.concat([total_series.rename("total"), bench_series.rename("bench")], axis=1).ffill().dropna()

        # Alpha 填色：total > bench 绿色，<  bench 红色
        ax_main.fill_between(
            aligned.index, aligned["total"], aligned["bench"],
            where=aligned["total"] >= aligned["bench"],
            interpolate=True, color=POS, alpha=0.12, linewidth=0,
        )
        ax_main.fill_between(
            aligned.index, aligned["total"], aligned["bench"],
            where=aligned["total"] < aligned["bench"],
            interpolate=True, color=NEG, alpha=0.12, linewidth=0,
        )

        ax_main.plot(
            bench_dates, bench_values, color=BENCH, linewidth=1.6,
            linestyle=(0, (6, 3)), label="SPY 买入持有基准", zorder=3,
        )

    # 主曲线：总资产
    ax_main.plot(dates, total, color=INK, linewidth=2.4, label="账户总资产", zorder=5)

    # 买卖事件：极简圆点（不喧宾夺主）
    event_tx = tx[tx["action"].isin(["BUY", "SELL"])]
    for _, row in event_tx.iterrows():
        d = row["date"]
        val_on_day = valuation[pd.to_datetime(valuation["date"]) == d]
        if val_on_day.empty:
            continue
        y = val_on_day["total_assets"].values[0]
        color = POS if row["action"] == "BUY" else NEG
        ax_main.scatter(d, y, s=14, color=color, alpha=0.55, zorder=7, edgecolors="none")

    # 端点标注
    latest = valuation.iloc[-1]
    last_date = dates.iloc[-1]
    ax_main.scatter([last_date], [latest["total_assets"]], s=72, color=INK, zorder=10, edgecolors=BG, linewidths=2)
    ax_main.annotate(
        f"  ${latest['total_assets']:,.0f}",
        xy=(last_date, latest["total_assets"]),
        xytext=(8, 0), textcoords="offset points",
        fontsize=12, fontweight="bold", color=INK,
        ha="left", va="center",
    )
    if not spy_bench.empty:
        bench_last = spy_bench.iloc[-1]["spy_benchmark"]
        ax_main.annotate(
            f"  ${bench_last:,.0f}",
            xy=(pd.to_datetime(spy_bench.iloc[-1]["date"]), bench_last),
            xytext=(8, 0), textcoords="offset points",
            fontsize=10, color=MUTED, ha="left", va="center",
        )

    # 计算 alpha
    if not spy_bench.empty:
        initial = spy_bench.iloc[0]["spy_benchmark"]
        acct_return_pct = (latest["total_assets"] / initial - 1) * 100
        bench_return_pct = (bench_last / initial - 1) * 100
        alpha = acct_return_pct - bench_return_pct
        alpha_txt = f"{alpha:+.2f}%"
        alpha_color = POS if alpha >= 0 else NEG
    else:
        acct_return_pct = bench_return_pct = 0
        alpha_txt, alpha_color = "n/a", MUTED

    # 标题 —— 简洁，只写关键数字
    start_date = dates.iloc[0].date()
    end_date = last_date.date()
    ax_main.set_title(
        f"DMO 账户资产曲线  ·  {start_date}  →  {end_date}",
        fontsize=14, fontweight="bold", color=INK, loc="left", pad=14,
    )
    # 副标题：左边灰色自有/基准回报，右边彩色超额
    ax_main.text(
        0.0, 1.015,
        f"账户 {acct_return_pct:+.2f}%     SPY {bench_return_pct:+.2f}%",
        transform=ax_main.transAxes,
        fontsize=10.5, color=MUTED, va="bottom",
    )
    ax_main.text(
        1.0, 1.015,
        f"超额 {alpha_txt}",
        transform=ax_main.transAxes,
        fontsize=10.5, color=alpha_color, fontweight="bold", va="bottom", ha="right",
    )

    # 美化 spines
    for sp in ["top", "right"]:
        ax_main.spines[sp].set_visible(False)
    for sp in ["left", "bottom"]:
        ax_main.spines[sp].set_color(MUTED)
        ax_main.spines[sp].set_linewidth(0.8)

    ax_main.tick_params(colors=MUTED, labelsize=10)
    ax_main.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax_main.grid(True, axis="y", color=GRID, linestyle="-", linewidth=0.7, alpha=0.8)
    ax_main.set_axisbelow(True)

    # 只在合适 y 范围内显示（裁掉早期 cash dip 无关区间 — 因为不再画 cash 线）
    y_min = min(total.min(), spy_bench["spy_benchmark"].min() if not spy_bench.empty else total.min())
    y_max = max(total.max(), spy_bench["spy_benchmark"].max() if not spy_bench.empty else total.max())
    y_pad = (y_max - y_min) * 0.12
    ax_main.set_ylim(y_min - y_pad, y_max + y_pad)

    ax_main.legend(
        loc="lower right", frameon=False, fontsize=10,
        labelcolor=INK, handlelength=1.8,
    )

    # ---------------- 副图：手续费累计阶梯 ----------------
    # 设计：阶梯式填充区域 + 端点数字；每次交易即看到一个"台阶"
    ax_fees.fill_between(
        dates, 0, valuation["cum_fees"],
        step="post", color=NEG, alpha=0.18, linewidth=0,
    )
    ax_fees.step(
        dates, valuation["cum_fees"],
        where="post", color=NEG, linewidth=1.6,
    )
    # 端点点 + 标注
    cum_fee_final = latest["cum_fees"]
    pct_of_assets = cum_fee_final / latest["total_assets"] * 100
    ax_fees.scatter([last_date], [cum_fee_final], s=36, color=NEG, zorder=5, edgecolors=BG, linewidths=1.5)
    ax_fees.annotate(
        f"累计 ${cum_fee_final:.2f}   ·   {pct_of_assets:.2f}% of NAV",
        xy=(last_date, cum_fee_final),
        xytext=(8, 0), textcoords="offset points",
        fontsize=9.5, color=NEG, fontweight="bold", va="center",
    )

    ax_fees.set_ylim(0, max(valuation["cum_fees"].max() * 1.25, 1))
    for sp in ["top", "right"]:
        ax_fees.spines[sp].set_visible(False)
    for sp in ["left", "bottom"]:
        ax_fees.spines[sp].set_color(MUTED)
        ax_fees.spines[sp].set_linewidth(0.8)
    ax_fees.tick_params(colors=MUTED, labelsize=9)
    ax_fees.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:.0f}"))
    ax_fees.set_ylabel("手续费", fontsize=10, color=MUTED)
    ax_fees.grid(True, axis="y", color=GRID, linestyle="-", linewidth=0.6, alpha=0.8)
    ax_fees.set_axisbelow(True)

    # X 轴
    ax_fees.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    ax_fees.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    for lbl in ax_fees.get_xticklabels():
        lbl.set_rotation(0)

    # 右边留空给端点标注
    x_pad = (dates.iloc[-1] - dates.iloc[0]).days * 0.06
    ax_fees.set_xlim(dates.iloc[0], dates.iloc[-1] + pd.Timedelta(days=x_pad))

    plt.tight_layout()
    for path in out_paths:
        plt.savefig(path, dpi=140, bbox_inches="tight", facecolor=BG)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="账户资产曲线生成器")
    parser.add_argument("--end", type=str, default=None, help="估值结束日期 YYYY-MM-DD（默认今天）")
    args = parser.parse_args()

    print("[1/5] 读取交易流水...")
    tx = load_transactions()
    print(f"      共 {len(tx)} 条记录，首笔 {tx.iloc[0]['date'].date()}，末笔 {tx.iloc[-1]['date'].date()}")

    print("[2/5] 拉取历史价格...")
    tickers = [t for t in tx["ticker"].unique() if t != "-"]
    if "SPY" not in tickers:
        tickers.append("SPY")
    start = tx["date"].min()
    end = pd.to_datetime(args.end) if args.end else datetime.now()
    prices = fetch_price_history(tickers, start, end)

    print("[3/5] 重建每日净值...")
    valuation = build_daily_valuation(tx, prices)
    valuation.to_csv(OUT_CSV, index=False)
    print(f"      写入 {OUT_CSV}（{len(valuation)} 行）")

    print("[4/5] 计算 SPY benchmark...")
    spy_bench = build_spy_benchmark(tx, prices)

    print("[5/5] 绘图...")
    today = datetime.now().strftime("%Y-%m-%d")
    dated_png = REPORTS_DIR / f"{today}-portfolio-chart.png"
    latest_png = REPORTS_DIR / "portfolio-chart-latest.png"
    plot_chart(valuation, spy_bench, tx, [dated_png, latest_png])
    print(f"      写入 {dated_png}")
    print(f"      写入 {latest_png}")

    latest = valuation.iloc[-1]
    print("\n=== 最新对账 ===")
    print(f"  估值日期:     {latest['date']}")
    print(f"  总资产:       ${latest['total_assets']:.2f}")
    print(f"  证券市值:     ${latest['securities_value']:.2f}")
    print(f"  现金:         ${latest['cash']:.2f}")
    print(f"  累计利息:     ${latest['cum_interest']:.2f}")
    print(f"  累计手续费:   ${latest['cum_fees']:.2f}")
    print(f"  实现盈亏:     ${latest['cum_realized_pnl']:+.2f}")
    print(f"  未实现盈亏:   ${latest['unrealized_pnl']:+.2f}")
    print("\n对比 moomoo 实际（截图 2026-04-22 11:41 ET）：")
    print("  总资产 $2,553.48 / 证券 $2,499.53 / 现金 $51.19 / 持仓盈亏 +$71.92 / 累计利息 $0.19")


if __name__ == "__main__":
    main()

# DMO 账户资产曲线 — 初始 Baseline (2026-04-22)

> 首次完整回填全部历史交易（2026-01-30 开户 → 2026-04-22），重建每日净值曲线。
> 数据源：moomoo app 历史订单截图 + yfinance 历史收盘价 + 用户对账确认。

---

## 🎯 最新对账

| 指标 | 我的计算 | moomoo 实际 | 差 | 说明 |
|---|---|---|---|---|
| **总资产** | $2,527.15 | **$2,553.48** | -$26.33 | 综合下方差 |
| 证券市值 | $2,495.73 | $2,499.53 | -$3.80 | yfinance 收盘 vs moomoo 盘中 11:41 报价 |
| 现金 | $31.42 | $51.19 | -$19.77 | **moomoo 新用户免佣导致费用过计** |
| 累计利息 | $0.19 | $0.19 | ±0.00 ✅ | 手动录入 INTEREST 交易 |
| 累计手续费 | $31.73 | ~$12 (推算) | +$19.73 | 见下 |
| 实现盈亏 | -$15.39 | N/A | — | 包含我计算的过高手续费 |
| 未实现盈亏 | +$62.59 | +$71.92 | -$9.33 | yfinance/moomoo 报价差 |

**结论**：曲线形状准确，数值级别接近，**主要差异来源已定位**。

---

## 🔍 差异来源分析

### 1. 手续费过计 ~$19.77（核心原因）
- 我按 `config/holdings.yaml` 声明的费率（$0.99/单最低）计算：31 笔 × $0.99 = $30.69
- moomoo 实际只收了 ~$12（31 笔均摊仅 $0.39/单）
- **最可能原因**：moomoo 新用户免佣活动（常见 30-90 天）或 dollar-order 特殊费率
- **修复建议**：确认 moomoo 当前计费后，在 `scripts/calculate_fees.py` 调整（或等促销结束后重启默认费率）

### 2. 证券估值差 ~$3.80
- yfinance 拉的是 **当日收盘价**（或最近已收盘交易日）
- moomoo 11:41 显示的是 **盘中实时价**
- 市场继续波动 → 永远有 $5-20 量级差，正常

### 3. 利息 $0.19 ✅
- 脚本**不**自动按日复利（APY 设为 0），因为 moomoo cash sweep 实际生效时间比开户日晚
- 用户定期（月度）看 moomoo 累计利息后，在 `transactions.csv` 追加 INTEREST 增量行即可

---

## 📊 账户演化关键节点

| 日期 | 事件 | 累计总资产 |
|---|---|---|
| 2026-01-30 | 首次入金 $2,500 + 买 TSLA/SPY/AAPL | ~$2,500 |
| 2026-02-02 | 大额建仓 AMD/SPY/GS/NVDA（共 $2,000） | ~$2,478 |
| 2026-02-05 | ORCL 建仓 $200 | ~$2,465 |
| 2026-02-11 | TSLA 清仓 → AMZN 建仓 | ~$2,451 |
| 2026-02-23 - 2026-02-25 | 多次 ORCL/NVDA/AMD 换仓 | ~$2,470 |
| 2026-03-25 | AMD 部分减仓 → 加 NVDA | ~$2,497 |
| 2026-04-08 - 2026-04-13 | **5 日大调仓**：清仓 AMD/AMZN/GS + 建仓 GLD/CVX/SCHD | ~$2,504 |
| 2026-04-20 | 建仓 TSM/META + SPY 部分减仓 + CVX 加仓 $300 | ~$2,530 |
| 2026-04-22 | 当前 | **$2,553.48** (moomoo) |

---

## 💰 已实现盈亏（5 只已清仓个股）

| 股票 | 累计买入 | 累计卖出 | 盈亏 | 持有时长 |
|---|---|---|---|---|
| TSLA | $130.33 | $127.75 | -$2.58 | 12 天 |
| ORCL | $200.00 | $204.69 | +$4.69 | 18 天 |
| AMZN | $136.96 | $153.33 | +$16.37 | 58 天 |
| GS | $500.00 | $471.36 | -$28.64 | 70 天 |
| AMD | $338.59 | $339.68 | +$1.09 | 70 天 |
| **合计** | **$1,305.88** | **$1,296.81** | **-$9.07** | — |

（不含手续费；若按 moomoo 实际 ~$12 手续费核减 ~$4，实现盈亏 ≈ -$13）

---

## 🧱 数据架构

```
data/
  transactions.csv           # 34 行：DEPOSIT + 31 BUY/SELL + 1 INTEREST（今日对账 $0.19）
                              # 未来每笔新交易 append 一行即可
  daily_valuation.csv        # 83 行：每日（含周末）的净值快照（覆盖式重算）

scripts/
  calculate_fees.py          # moomoo 费率工具（独立可用：python3 scripts/calculate_fees.py 1 200 buy）
  track_portfolio.py         # 主引擎 → reads tx csv + fetches prices + emits chart

reports/
  YYYY-MM-DD-portfolio-chart.png    # 日期快照（归档）
  portfolio-chart-latest.png        # 最新版（覆盖式）
```

## 🔁 未来追加交易的工作流

**用户操作 → 2 步**：

1. 在对话里告诉我 → 我追加一行到 `data/transactions.csv`
   ```
   2026-04-24,10:30:00,SCHD,BUY,16,31.20,499.20,加仓 dry powder 首批
   ```
2. 我跑 `python3 scripts/track_portfolio.py`，曲线 & 对账表自动扩展

**定期对账**（建议每月 1 次）：
- 用户截图 moomoo 当月对账单 / Cash Sweep 累计利息
- 我录入 INTEREST 增量行（例如下月发现累计 $0.80，录 +$0.61 的 INTEREST 行）

**如果 moomoo 费率发生变化**（promo 结束等）：
- 修改 `scripts/calculate_fees.py` 的 `PLATFORM_FEE_PER_SHARE` / `PLATFORM_FEE_MIN`
- 不需要回填旧数据（历史已付固定）—— 只影响新交易

---

## 🆕 本版主要改动到 holdings.yaml

- `account.total_assets_usd`：$2,541.53 → $2,553.48
- `account.cash_total_usd`：$353.18 → $51.19
- 新增 `account.account_opened`、`initial_deposit_usd`、`cash_sweep_accumulated_interest_usd`
- CVX：1 股 @ $191.69 → **2.6371 股 @ $186.451**（4/20 加仓 $300 后均摊）
- TSM：0.33763 → 0.3376（moomoo 显示精度）
- GLD：0.46054 → 0.4606
- 全部持仓补上 `purchase_dates` 字段
- 删除 `fees_paid_usd: null`，改为具体估计值（后续根据 moomoo 对账单精修）

---

## ⏭️ 下一步候选

- [ ] SCHD 加仓 $500（纪律化执行，加仓后更新 ledger）
- [ ] META 财报前减半（4/28 EOD 前）
- [ ] 定期每周五跑一次 `track_portfolio.py` 更新曲线
- [ ] 确认 moomoo 费率（免佣活动有效期 / 剩余天数）后校准 `calculate_fees.py`
- [ ] 考虑 $10K dry powder 转入后如何嵌入纪律计划（大额一次性 DCA 还是分批）

---

*Baseline 版本：v1.0（2026-04-22）*
*后续每次跑 `track_portfolio.py` 会自动覆盖 `daily_valuation.csv` + 刷新图表*

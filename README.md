# DMO — 投资组合分析归档

个人投资组合的决策归档、分析报告、扫描脚本。

## 目录结构

```
DMO/
├── scripts/                        # 扫描工具
│   ├── portfolio_scan.py           # 技术面扫描（EMA/RSI/ATR/布林带）
│   ├── smart_money_scan.py         # 13F 机构持仓 Q-over-Q（45 天延迟）
│   ├── insider_scan.py             # Form 4 内部人交易（2 天延迟）
│   ├── short_interest_scan.py      # FINRA Reg SHO 每日做空（T+1 延迟）
│   ├── options_anomaly_scan.py     # 异常期权活动 + P/C 比率
│   ├── earnings_setup.py           # 财报窗口：隐含波动 + 历史 beat/miss + PEAD
│   └── backtest_resonance.py       # 验证 🟢🟢🟢 共振信号的历史 alpha
├── config/
│   └── holdings.yaml               # 持仓、观察池、扩展宇宙、财报日历
├── docs/
│   └── METHODOLOGY_v2.md           # DMO v2 方法论
└── reports/                        # 自动归档的分析报告（按日期）
```

## 脚本一览

### 1. `portfolio_scan.py` — 实时技术面
```bash
python3 scripts/portfolio_scan.py            # 默认 8 只持仓
python3 scripts/portfolio_scan.py NVDA,META  # 自定义
```
输出：EMA50/EMA200、RSI、ATR、趋势、ATR 止损、BB%、Vol 比。
数据：yfinance（需 `curl_cffi` 绕 Yahoo 反爬）。

### 2. `smart_money_scan.py` — 13F 机构持仓变动
```bash
python3 scripts/smart_money_scan.py
```
覆盖 8 基金（Berkshire / Pershing / Third Point / Renaissance / Bridgewater / Appaloosa / Scion / Tiger Global）最近 2 季度。
数据：SEC EDGAR 13F-HR XML。**局限：45 天披露延迟**。

### 3. `insider_scan.py` — Form 4 内部人交易（新）
```bash
python3 scripts/insider_scan.py [tickers] [lookback_days]
# 默认: 持仓+候选池，90 天回看
```
**补足 13F 延迟**：Form 4 要求 2 个交易日内披露。CEO/CFO 开盘价买入（code=P）是所有合法数据里最快的强信号。
输出：每只股票 90 天内 buy/sell 总额、C-suite 高管买入明细。
数据：SEC EDGAR。

### 4. `short_interest_scan.py` — 每日做空异动（新）
```bash
python3 scripts/short_interest_scan.py [tickers] [days_window]
# 默认: 持仓+候选池，25 天窗口
```
FINRA Reg SHO **T+1 发布**每只股票的做空成交量。Z-score 机制识别做空激增（看空新建）和空头回补（挤空前兆）。绝对值 40-60% 是市场制造商对冲造成的，所以**只看变化率**，不看水平。
数据：FINRA 官方 CDN，免费。

### 5. `options_anomaly_scan.py` — 异常期权活动（新）
```bash
python3 scripts/options_anomaly_scan.py [tickers]
```
两层信号：
- **P/C Vol 比率** (整体情绪)：>1.3 偏空 / <0.5 偏多
- **Vol/OI > 2 的合约**：今日新开仓超过既有未平仓 2 倍 = 激进新建仓，接近暗池机构信号
输出 Top 5 异常合约（含 Strike、Moneyness、IV）。
数据：yfinance option_chain。

### 6. `earnings_setup.py` — 财报专项（新）
```bash
python3 scripts/earnings_setup.py META,AAPL,CVX
```
三件事：
- **Implied Move**：从 ATM 跨式期权算市场预期的财报后涨跌幅
- **Beat/Miss 历史**：过去 8 季度 EPS surprise + beat 率
- **Post-Earnings Drift (PEAD)**：T+5 相对 T-1 的价格漂移
用于"META 跌 5% 是正常噪声还是真警讯"这类问题。

### 7. `backtest_resonance.py` — 方法论自证（新）
```bash
python3 scripts/backtest_resonance.py [n_quarters] [universe]
# 默认: 8 季度 + 14 只股票 universe
```
回测 `🟢🟢🟢 三派共振 / 🟢🟢 双派 / 🟡 单派 / 🔴 多派撤退` 这四类信号的 3 个月前瞻 alpha vs SPY。**初次运行需 2-3 分钟**（拉 64+ 个 13F 文件）。

解读：
- Triple-Buy 平均 alpha > 0 且 hit rate > 60% → 方法论有效
- Triple-Buy 平均 alpha ≈ 0 → 伪 alpha，退化成 SPY beta
- Triple-Buy 平均 alpha < 0 → 反向信号，立刻停用

## 前置环境

```bash
python3 -m pip install --upgrade yfinance curl_cffi pandas
```
要求：`yfinance >= 0.2.50`，`curl_cffi >= 0.7`（Yahoo 2025 反爬必需）。

## 方法论

完整 v2 方法论见 [`docs/METHODOLOGY_v2.md`](docs/METHODOLOGY_v2.md)。核心：

1. **分析 = 持仓 + 扩展池**，找机会 ≠ 盯现有持仓
2. **多层证据共振**：技术面 🟢 + 智钱层 🟢🟢/🟢🟢🟢 + 内部人 🔥 + 基本面 → 硬结论
3. **派系分级**：价值派（Buffett/Ackman/Loeb）+ 量化派（Renaissance/Bridgewater）+ 主观派（Tepper/Burry/Tiger）
4. **财报周降级**：±3 天内所有结论降到摇摆区；先看 `earnings_setup.py` 的 implied move
5. **纪律机制**：每次分析产出可执行触发点清单

## 数据限制

| 数据源 | 延迟 | 用途 | 替代方案 |
|---|---|---|---|
| yfinance K 线 | 实时（15 分钟）| 技术面 | 无必要升级 |
| SEC 13F-HR | 45 天 | 基金建仓/清仓趋势 | — |
| SEC Form 4 | 2 天 | 内部人交易 | 唯一的高速信号 |
| yfinance 期权链 | 盘中 | Implied Move + 异常活动 | CBOE DataShop（付费） |
| FINRA Reg SHO | T+1 | 做空量/总量比 | — |
| FINRA ATS 暗池 | 2 周 | 暗池占比（未采用，延迟太大）| Unusual Whales（付费） |

## 自动化

两个 claude.ai Remote Triggers（云端运行，不依赖本地设备）：

- **DMO-Weekday-Tech-Scan**：工作日 17:00 ET，跑 `portfolio_scan.py` 检异常 → Gmail
- **DMO-Weekly-Deep-Report**：周日 21:00 ET，跑完整方法论（4 个脚本 + 搜索）→ 归档到 `reports/` + Gmail + Google Calendar 同步财报

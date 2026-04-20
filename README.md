# DMO — 投资组合分析归档

个人投资组合的决策归档、分析报告、扫描脚本。

## 目录结构

```
DMO/
├── scripts/                            # 扫描工具
│   ├── portfolio_scan.py               # 技术面扫描（yfinance + curl_cffi）
│   └── smart_money_scan.py             # 13F 机构持仓追踪（SEC EDGAR）
└── reports/                            # 分析报告（按日期命名）
    ├── 2026-04-20_v1_portfolio_analysis.md   # 初版 8 只持仓分析（文本搜索）
    ├── 2026-04-20_kline_correction.md        # K 线实测修正 v1 的偏差
    ├── 2026-04-20_13f_smart_money.md         # 13F 机构持仓原始输出 + 解读
    ├── 2026-04-20_deep_dive_CVX_META.md      # CVX/META 深度分析（K线+13F融合）
    └── 2026-04-20_v2_opportunity_radar.md    # 扩展版机会雷达（40 只股票扫描）
```

## 脚本使用

### 前置环境（Mac）

```bash
python3 -m pip install --upgrade yfinance curl_cffi pandas
```

要求：`yfinance >= 0.2.50`，`curl_cffi >= 0.7`（Yahoo 2025 反爬必需）。

### 技术面扫描

```bash
# 默认扫描 8 只持仓
python3 scripts/portfolio_scan.py

# 自定义
python3 scripts/portfolio_scan.py NVDA,META,TSLA
```

输出：EMA50/EMA200、RSI、ATR、趋势判断、ATR 止损、布林带位置、成交量比。

### 13F 智钱追踪

```bash
# 默认扫描 8 个基金对 5 只股票的最近 2 个季度变动
python3 scripts/smart_money_scan.py

# 自定义
python3 scripts/smart_money_scan.py MU,OXY,AMD
```

数据源：SEC EDGAR 官方 13F-HR XML。覆盖基金：Berkshire、Scion、Pershing、Appaloosa、Bridgewater、Renaissance、Third Point、Tiger Global。

## 方法论

1. **每次分析 = 当前持仓扫描 + 扩展股票池扫描**，找机会 ≠ 盯现有持仓
2. **三层证据共振**：技术面 + 智钱层 + 基本面，三层同向才上硬结论
3. **派系共振识别**：价值派 + 量化派同向 = 最罕见信号；主观派 vs 量化派分裂 = 不决策
4. **财报周降级规则**：财报 ±3 天内，所有结论降到"摇摆区"
5. **纪律书机制**：每次分析产出可执行触发点清单，自查执行

## 数据限制

- 13F 有 45 天披露延迟
- yfinance 免费数据无盘前盘后、无期权链、无暗池
- 只覆盖美股多头持仓，空头 / 期权 / 国际头寸看不到

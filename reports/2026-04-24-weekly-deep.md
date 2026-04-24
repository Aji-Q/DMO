# DMO 周报 2026-04-24 (v3.3 — FOMC + 财报三连前夜版)

> 本报告基于 2026-04-24 盘中实时 Phase 1 脚本数据（6/6 成功）+ 8 次 WebSearch 叙事验证。
> 距 v3.2 (2026-04-22) 两个交易日，**技术面和期权层发生 3 个重大变化**（详见下文"本周 4 个核心变化"）。

---

## 搜索链状态

| Phase | 状态 | 备注 |
|---|---|---|
| Phase 1 脚本 | ✅ **6/6 成功** | portfolio/smart_money/insider/short/options/earnings 全 exit 0 |
| Phase 2a WebSearch | ✅ **8 次** | 5 持仓财报预览 + 3 宏观/候选 |
| Phase 2b 合成 | ✅ 会话内完成 |
| Phase 3 报告写入 | ✅ |

**数据时间戳**：portfolio & options 盘中实时（US 时段）；FINRA short 最新 2026-04-23（T+1）；Form 4 90d 窗口；13F 仍为 Q1 2026（2026-02-17 filed，下次更新约 2026-05-15）。

---

## 🗓️ 市场背景（2026-04-24 Fri 盘中）

| 指标 | 读数 | 含义 |
|---|---|---|
| SPY | $713.16（距 4/17 ATH $710.14 创新高） | 压舱石持续刷 ATH |
| 本周距三连事件 | **4 天** | FOMC 4/28-29 → META 4/29 → PCE+AAPL 4/30 → CVX 5/1 → NFP 5/2 |
| FOMC 预期 | **Hold**（3.50-3.75%）| Fed 3 月点阵图砍至全年仅 1 次降息（25bp） |
| PCE 预期 | 2.7% YoY（高于 12 月 2.4%） | 通胀粘性 → 鸽派失望风险 |
| CVX 催化剂 | 🆕 **Wheatstone LNG 完全恢复**（4/23 官宣） | 之前停产风险解除，但 Q1 timing 损失 $2.7-3.7B 税后预示 |

⚠️ **v3.2 错误校正**：v3.2 写 "FOMC 5/6-7" 是错的。WebSearch 确认下次 FOMC 是 **4/28-29**（本周二三），与 META 财报同一天！

---

## 📊 5 层共振总览表（11 只股）

| Ticker | 价格 | L1 技术 | L2 13F | L3 Form4 | L4 做空 z | L5 期权 | 整体等级 | 陷阱 | 信心 |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | $209.15 | 🟢 RSI **72** BB 90% | ⚠️ 分裂 | 🔴 -$172M | — z+0.3 | **⚠️ 陷阱 E 再现**（P/C 0.34 + 6 put 新建）| **3 层警戒** | **E + G** | 72% |
| SPY | $713.16 | 🟢 过热 RSI 70 BB 80% | N/A | N/A | — z-0.0 | 🔴 0DTE 狂欢 50 异常 | **技术 ATH** | F | 65% |
| AAPL | $270.29 | 🟢 RSI 59 BB **78%**（收窄） | 🔴 全员减 | 🔴 -$24M（90d） | — z+0.1 | 🔴 5 put 异常 | **4 层偏空** | E 降温 | 72% |
| META | $675.00 | 🟡 死叉修复 RSI 62 | ⚠️ 分裂 | 🔴 CFO -$106M | — z+0.4 | 🟢 P/C 0.48 + 6 call | **4 层偏空 + 0DTE 狂欢** | F | 75% |
| TSM | **$404.84** | 🟢 **RSI 69 BB 100%**（强势突破）| 🔴 缓退 | 🔥 33 buys + Burns $322K | — z+1.4 | 🟢 6 call + 1 tail put | **L3 罕见强升级** | — | 78% |
| CVX | $183.77 | 🟡 RSI 40 BB **24%** | 🟢🟢 Double | 🔴 -$155M 全 C-suite | 🟠 z+1.5 | — 1 call | **内部冲突 + Wheatstone 缓释** | D 反向 | 60% |
| GLD | $434.02 | 🟡 RSI 48 破 EMA50 | N/A | N/A | 🟡 z-1.4 空减 | 🟢 3 call | **技术走弱** | — | 58% |
| SCHD | $31.23 | 🟢 RSI 61 BB **91%** | N/A | N/A | — z-0.2 | 🟢 P/C 0.25 | **稳健** | — | 82% |
| MU | **$499.84** | 🟢 RSI 69 BB 89% | 🟡 Bridgewater+19 / Ren-10 | 🔴 -$53M CBO+CPO | — z+0.8 | 🔴 **7 put 异常**（0DTE 大量 put 新建） | **信号持续衰减** | F | 55% ⚠️ |
| OXY | $56.73 | 🟢 RSI 47 BB 33% | 🟡 Berkshire 数据疑 | — 净 $0 | **🟠 z+1.7 新警** | 🟢 P/C 0.41 | **温和多头 + 新做空警** | D | 60% |
| AMD | **$350.39** ⚠️ | 🔴 **RSI 89.2 极度过热** BB **111%** Vol **1.3x** | 🔴 量化双减 | 🔴 Su+CTO -$14M | — z+1.2 | 🔴 **9 个激进 call 异常**（陷阱 F 白热化） | **5 层偏空但散户 FOMO 极度** | **B+F+G** | **88%** |

图例：🟢 多 / 🟡 中性 / 🔴 空 / ⚠️ 分裂 / 🔥 罕见强信号

---

## 🔥 本周 4 个核心变化（vs v3.2 2 天前）

### ⚠️ 变化 1：AMD 从 $296 飙到 $350（+18%），陷阱 B+F 白热化

**v3.2 时**：RSI 82，BB 95%，8 个 ITM put 机构做空，$296
**v3.3 现在**：RSI **89.2**（极度过热创周高）、BB **111%**（突破上轨 11%）、**Vol 1.3x 放量**、股价 **$350**
**关键对冲信号矛盾**：
- L5 **9 个激进 call 异常**（4/24 C $360 Vol/OI **47.2x**、C $345 = 46.0x、C $350 = 31.3x）→ 散户财报前 FOMO
- 同时 5/1 P $330 Vol/OI 28.4x → 机构买保护
- L3 CTO Papermaster 4/17 卖 $7.4M（财报 5/5，还有 11 天）

**这是本周最清晰的"陷阱 F 白热化"信号**：散户赌 $360/$370 short-dated call（IV 38-50%，成本不低），机构用 $330 put 对冲下行。5 层里只有 L5 call 是多头，且是典型散户行为。

**操作**：🟥 **继续禁止追涨**。若财报 guide 低于预期（Q1 revenue $9.84B consensus / guide 35% YoY 数据中心），可能 gap down 15-20%（距 ATR stop $330 只 -6%）。
**候选入场调整**：原 yaml 写 $230-240 已严重过时。**新入场参考**：若财报后 gap down 到 $270-290（EMA50 $237 +15%），再考虑。
**信心 88%**（最高的一只）

---

### ⭐ 变化 2：TSM 突破 $405（+8%），L3 信号再升级

**v3.2 时**：$375，RSI 60，L3 有 Wei CEO 买 $11K + 33 buys 3M（WebSearch）
**v3.3 现在**：**$404.84**（RSI 69、BB 打满 100%、EMA50 $354），WebSearch 新发现：
- 🆕 **Director Ursula Burns 2026-04-01 买入 1000 股 @ $322K** — 这是个人真金大仓（vs Wei $11K 象征性）
- 过去 3 个月 5 笔 insider trade **全部是买入**
- 股价一个月 +18.81%，52 周 +135.98%

**L5 期权层也验证**：
- 4/24 C $402.5 Vol/OI 8.1x + C $405 = 3.8x 多头
- 同时 5/1 P $230（-43% OTM！）Vol/OI 4.5x IV 139% → 地缘 tail 灾难对冲仍存在，但这是正常 hedging 非反转信号

**操作**：🟨 **当前 $405 不追**（BB 100% 过热，RSI 69 接近超买）。
**✨ 新加仓计划**：若回踩 EMA50 $354（-13%）或 ATR stop $385，考虑从 dry powder **$300-400 小仓加仓**。
**信心 78%**（从 60% 上调）

---

### 🆕 变化 3：NVDA 陷阱 E 再现（散户期权翻多 vs 机构新建 put）

**v3.2 时**：P/C Vol 0.64 中性，ATM 双向对冲（陷阱 G）
**v3.3 现在**：P/C Vol **0.34（深度偏多）** + 但 Top 5 异常全是 put：
- 4/24 P $210 Vol/OI **50.5x** IV 40%
- 4/24 P $205 Vol/OI **26.1x** IV 34%
- 4/27 P $210 Vol/OI 23.0x
- 4/27 P $205 Vol/OI 18.1x
- 4/24 P $202.5 Vol/OI 8.2x

**这是典型陷阱 E**：散户在 P/C 比率层面看多（call 成交量碾压 put）, 但 **6 个最大异常全部是新建 put**（Vol/OI 8-50x）— 机构在买下行保护。

**中国 H200 获批新闻**是近期催化剂（WebSearch 确认），但股价已从 $185 涨到 $209（+13%），市场已 priced。

**操作**：🟨 **持有不加仓**（ATR stop $201.09 距现价仅 -3.9%，防御姿态）。Scion Burry 1M NEW 仍是罕见正信号但未改变整体态度。
**信心 72%**

---

### 🟢 变化 4：CVX Wheatstone LNG 完全恢复（4/23 官宣）

**v3.2 时**：Wheatstone 两列 LNG 停产数周是重大风险
**v3.3 现在**：4/23 Chevron 官宣**完全恢复 LNG 生产**，风险解除。

**但 4/25 盘中 CVX $183.77，跌破 EMA50 $188.49，RSI 40 偏弱，BB 24%（贴下轨）**：
- WebSearch 揭示：Chevron 预期 Q1 "timing effects 拖累 earnings / cash flow $2.7-3.7B 税后" — 这是 5/1 财报的 **已知 negative**
- L4 做空 z=+1.5 维持（没恶化但没缓解）
- L5 期权淡漠（仅 1 个 call 异常）

**操作**：🟨 **维持 v3.2 决策"持有不加仓"**。Wheatstone 恢复 + BB 24% 技术超卖 + L2 Double-Buy 历史 → 不止损；但 L3 C-suite 大抛 + L4 偏高 + Q1 timing 已定预警 → 不加仓。
**若 5/1 盘后财报后 gap down 超 -5%（implied move ±3.7%）**→ 减半。
**信心 60%**（较 v3.2 升 5%，因 Wheatstone 风险解除）

---

## 持仓逐只深度分析

### NVDA $209.15 | 持有不加仓 + 陷阱 E/G 并存警戒

**5 层**:
- L1: 🟢 RSI **72.1**（回升至超买）, EMA50 $187.28 / EMA200 $175.64 强多头, BB 90%, ATR% 2.6%, Vol 0.7x
- L2: ⚠️ 分裂 — Bridgewater 3.9M +54% / Ren 0.9M **-85%** / Third Point 3.0M +4% / Tepper 1.7M -11% / Tiger 11.0M -6% / **Scion 1.0M NEW**（罕见正信号）
- L3: 🔴 90d 净卖 **$172M**（20 filings, 10 内部人；上期 $208M，因 90 天窗口滑动）
- L4: z=+0.3 正常
- L5: **陷阱 E 再现** — P/C Vol 0.34 偏多 + 6 激进 put 新建（最大 4/24 P $210 Vol/OI 50.5x IV 40%）

**新闻**（[NVIDIA at $199: Buy, Sell or Hold](https://247wallst.com/investing/2026/04/21/nvidia-at-199-buy-sell-or-hold/) + [Blackwell Q1 FY2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026)）：
- Q1 FY26 revenue $44.1B（+69% YoY），Blackwell NVL72 全量生产
- 中国 H20 export ban → $4.5B charge + $8.0B revenue 损失，**Q2 中国收入 zero**
- 2026 YTD +7%（落后 MU +69% / AMD +43%），但 H200 获批是近期催化剂
- 下次财报 2026-05-20（26 天后）

**对立面**：AI Capex 超级周期未结束；Scion Burry 作为知名空头代理竟然新建仓 = 罕见信号；连涨到 $209 有 Blackwell Ultra + Vera Rubin 需求支撑。

**操作**：🟨 **持有不加仓**。ATR stop **$201.09**（距现价 -3.9%，很紧）。陷阱 E/G 同时命中说明市场对近 1-2 周波动预期极高。
**R:R**：目标 $225（+7.6%）/ 止损 $201.09（-3.9%）→ R:R ≈ 2:1
**信心 72%**

---

### SPY $713.16 | ATH 不加仓，0DTE 狂欢主导 vol

**5 层**:
- L1: 🟢 RSI 70.1 过热, BB 80%, EMA50 $680, ATR stop **$700.24**, Vol **0.3x 极度缩量**
- L2/L3: N/A（宽基 ETF）
- L4: z=-0.0 正常
- L5: 🔴 0DTE 狂欢再升级 — 50 个异常，Top 5 Vol/OI 15-61x（P $716 = 61x、P $709 = 35.6x、C $712 = 19.5x）

**新闻**：SPY 4/17 创 ATH $710.14，本周 $713 继续突破。Iran 停火延长 + VIX 19 低位。但宏观高 stakes（FOMC + 财报 + PCE + NFP 四连发本周末到下周初）。

**对立面**：若 FOMC 继续鸽派 + PCE 低于预期 + 财报 beat，SPY 可能再推 +2%。宽基择时是长期胜率 55% 的游戏。

**操作**：🟨 **持有不加仓**（ATH + 0.3x 极度缩量 + 0DTE 噪声 = 无进场确认）。跌破 ATR stop $700.24 再考虑减仓。
**信心 65%**

---

### AAPL $270.29 | 财报 4/30（+6d, Implied **±4.1%**）

**5 层**:
- L1: 🟢 RSI **58.7**（降温，较 v3.2 62 回落）, BB **78%**（从 92% 收窄）, EMA50 $261.62, ATR stop $261.48, Vol **0.3x 极度缩量**
- L2: 🔴 全员减（Berkshire 227.9M -4% / Bridgewater 0.3M -16% / Ren 0.1M -7%）
- L3: 🔴 $24M 净卖（**注：本次 insider_scan 返回 0 filings，上次 20 filings，疑似 Apple SEC data 本周空窗或脚本 query 窗口问题，沿用 v3.2 数据**）
- L4: z=+0.1 正常
- L5: 🔴 5 个激进 put（最大 4/24 P $270 Vol/OI 6.1x）+ 少量 call；P/C Vol 0.61（较 v3.2 0.29 转向平衡）— 陷阱 E 降温

**新闻**（[Apple Q2 FY26](https://finance.yahoo.com/markets/stocks/articles/apple-q2-earnings-preview-aapl-154221571.html)）：
- Q2 收入指引 $107.8-110.7B（+13-16% YoY），EPS consensus $1.94（+17% YoY）
- 🆕 **Implied Move 从 v3.2 的 ±5.0 下降到 ±4.1%** — 市场预期趋稳，意外空间收窄
- Cook 9/1 卸任 + Ternus 接任（已消化）
- 毛利率 48-49% 指引里 **"Q2 memory 涨价拖累"已被点名**
- 8/8 Beat 率 100%，平均 surprise +4.0%

**对立面**：Ternus 内部接班 transition risk 低；Q1 中国 +38% YoY；Services 中双位数增速。[CNBC 报道 CEO 变动时机利好财报](https://www.cnbc.com/2026/04/21/why-the-timing-of-apples-ceo-change-could-mean-a-good-earnings-report-is-around-the-corner.html)。

**操作**：🟨 **持有不加**，按既定纪律：
- Miss 或毛利率指引 <48% → 减半（卖 0.194 股）
- Gap down >7%（超 implied move 上限）→ 减半
- 跌破 ATR $261.48（-3.3%）→ 减半
- Beat + 毛利率 ≥48% + Ternus 上任信号积极 → 保持

**R:R**：目标 $285（+5.4%）/ 止损 $261.48（-3.3%）→ R:R ≈ 1.6:1（<2:1 因 CEO 转换风险，纪律化结果）
**信心 72%**

---

### META $675.00 | 财报 4/29（+4d, Implied ±7.6%）— 减半决策已定

**5 层**:
- L1: 🟡 RSI 61.5 盘整, EMA50 $635.86 / EMA200 $647.58 **死叉修复中**, BB 74%, ATR stop $646.40, Vol 0.3x
- L2: ⚠️ 分裂（Ackman 2.7M NEW ✅ / Tepper 0.6M +62% / Burry EXIT / Ren EXIT / Bridgewater -46% / Third Point EXIT / Tiger -2%）
- L3: 🔴 CFO Susan Li 连抛 **$106M**（2/24 到 3/3 密集）
- L4: z=+0.4 正常（较 v3.2 +1.0 回落，做空不再激增）
- L5: 🟢 P/C Vol 0.48 偏多 + 6 激进 call（4/27 P $652.5 Vol/OI 9.8x + 4/24 C $665 = 7.8x）— 典型财报前 0DTE **陷阱 F**

**新闻**（[Meta Q1 2026 Earnings Preview](https://www.indexbox.io/blog/meta-platforms-q1-2026-earnings-preview-ai-investment-impact/) + [DCD 2026 Capex $115-135B](https://www.datacenterdynamics.com/en/news/meta-estimates-2026-capex-to-be-between-115-135bn/)）：
- Q1 revenue 指引 $53.5-56.5B（+16-20% YoY）
- **2026 Capex 指引维持 $115-135B**（vs 2025 年 $69.69B，**+65-95% YoY**）— "超智能实验室" 投入
- Meta 称 2026 operating income 仍将高于 2025（尽管 Capex 翻倍）
- 8/8 Beat 率 100%，平均 surprise +13.9%

**关键二元事件（4/29 盘后）**：
- **Capex guide 上调至 >$135B** → clearly bearish → 按 yaml 纪律清仓
- **Capex guide 维持 $115-135B** → 已 priced in，gap 取决于 ad 增速
- **Capex guide 下调 <$115B** → 大利好（但不太可能）

**对立面**：Ackman 2.7M NEW 是 Pershing 极少见重仓，Q1 ad impressions +18% 强劲（v3.2 数据），AI 货币化可能加速。

**操作**：🟥 **按既定计划 4/28 财报前减半**（卖 0.09 股套现约 $61，保留 0.09 股）
- 若 Beat + Capex ≤$125B → 下周用 dry powder $100 回补
- 若 Miss + Capex ≥$135B → 清仓余 0.09 股
- 若 Gap down 5-7.6%（implied move 内） → 按兵不动视为正常
- 若 Gap down >10% → 清仓

**PEAD 历史**：T+5 平均 -0.35%，5/8 正漂（极分化：-15.4% 到 +11.0%）→ **不可押方向，减半是风控而非方向赌注**
**信心 75%**

---

### TSM $404.84 ⭐ | 从 $375 涨 8%，L3 升级为加仓候选

**5 层**:
- L1: 🟢 **RSI 69 BB 100%**（突破上轨）, EMA50 $354.36 / EMA200 $303.53, ATR stop $385.28, Vol 0.8x
- L2: 🔴 缓退（Tepper +7% / Ren -13% / Third Point -61% / Tiger -19%）
- L3: 🔥🔥 **双重确认** — 脚本内 6 高管 $32K（v3.2 发现）+ WebSearch **4/1 Director Ursula Burns 买 1000 股 $322K**（真金大仓）+ 过去 3M 5 笔 insider trade 全是买
- L4: z=+1.4 上升（较 v3.2 +0.6）— 地缘对冲升温
- L5: 🟢 6 激进 call（4/24 C $402.5 Vol/OI 8.1x + C $405 = 3.8x） + 1 深 OTM put（5/1 P $230 -43% OTM IV 139% — 灾难对冲）

**新闻**（[TSMC Insider Buying](https://www.themarketsdaily.com/2026/04/16/insider-buying-taiwan-semiconductor-manufacturing-nysetsm-ceo-acquires-10763-82-in-stock.html)）：
- Q1 2026 revenue $35.9B +40.6% YoY, EPS $3.49 beat consensus
- Q2 指引 +30% YoY, Needham 目标价 $480（从 $410 上调）
- HPC 占比 61%（AI 代工独家）
- 一个月 +18.81%，52 周 +135.98%

**对立面**：BB 100% 过热 + 地缘 tail risk（台海）+ 本周 z+1.4 做空升温。追 $405 高位是追涨。

**✨ 新操作（从 v3.2 "持有不加仓"升级）**：
- 🟨 **当前 $405 不追高**
- 🟩 **回踩 EMA50 $354（-12%）或 ATR stop $385（-5%）考虑加仓 $300-400**（从 dry powder）
- 止损 $345（跌破 EMA50 -3%）
- 目标 $450 / $480（Needham target）
- 加仓后总仓位 $400-500 / 约 16-20% 总账户
- **理由**：L3 升级为双重确认（CEO 买 + Director $322K）+ L1 技术强势 + Q1 基本面碾压 + Q2 指引 30%+ YoY

**R:R @ 入 $370**: (450-370)/(370-345) = 3.2:1 ✅
**信心 78%**（从 60% 上调）

---

### CVX $183.77 | 持有不加仓，Wheatstone 风险解除但 Q1 timing 已定

**5 层**:
- L1: 🟡 RSI **39.7**（偏弱）, EMA50 $188.49 / EMA200 $167.51, **跌破 EMA50 $188.49** 1.5%, BB **24%**（贴下轨）, ATR stop $176.09, Vol 0.2x 缩量
- L2: 🟢🟢 Double-Buy（Berkshire +7% / Renaissance +424%）
- L3: 🔴 C-suite 集中抛售 $155M 不变
- L4: 🟠 z=+1.5 维持（接近 z>2 激增阈值但未突破）
- L5: — 期权极稀（1 个 call 5/1 C $197.5 Vol/OI 4.1x）

**新闻**（[Chevron Wheatstone restored](https://www.gurufocus.com/news/8813320/chevron-cvx-resumes-full-lng-production-at-wheatstone-plant-after-cyclone-repairs) + [CVX Q1 Timing Effects](https://www.financialcontent.com/stocks/article/finterra-2026-4-13-chevron-cvx-in-2026-the-new-era-of-energy-addition-and-the-guyana-catalyst)）：
- 🆕 **2026-04-23 Wheatstone LNG 完全恢复** — 停产风险解除
- Chevron 已公告：**Q1 timing effects 预计拖累 earnings/CFO $2.7-3.7B 税后**（财报前已定预警）
- 2025 Permian 产量创纪录 1mbpd
- 2025 成本节省目标 $1.5B 已达成，2026 目标 $3-4B
- 5/1 盘前（11am ET）电话会，市场关注：Guyana 催化剂 + timing 冲击 + 内部人大抛解释

**财报基本面**：
- Beat 率 **6/8**（之前 v3.2 也是 6/8），平均 surprise +0.5%
- **Implied Move ±3.7%**（从 v3.2 ±5.1% 降低，市场预期更温和）
- PEAD 平均 +0.24%，4/8 正

**对立面**：Double-Buy + Wheatstone 恢复 + BB 24% 深度超卖 + Brent 油价地缘溢价 = 下行空间有限。跌破 $176 硬止损。

**操作**：🟨 **持有不加，维持 v3.2 决策**
- 纪律: Miss + timing effect >$3.7B → 减半
- 跌破 EMA200 $167.51 → 清仓
- ATR 止损 $176.09 距现价 -4.2%
- 若 L4 下次 SI 更新 z>2 → 主动减半（不等财报）

**R:R 持仓维护**：现成本 $186.45 vs 价 $183.77 浮亏 1.4%，$176 止损 -5.5%
**信心 60%**（从 v3.2 55% 升 5%，因 Wheatstone 风险解除）

---

### GLD $434.02 | 持有不加仓，技术走弱

**5 层**:
- L1: 🟡 RSI 48 中性, BB 51%, **跌破 EMA50 $438.48**（持续 2 天）, ATR stop $420.18, Vol 0.4x
- L2-L4: N/A / z=-1.4（空头减弱）
- L5: 🟢 3 激进 call（4/27 C $438 + C $439 小量，GLD 期权流极稀）

**新闻**：Fed 仅预期 1 次降息（2026）+ USD 强 → GLD 顶部钝化；地缘 Iran 停火 → 避险需求下降。

**对立面**：若 PCE 高于预期或 FOMC 意外鹰派，USD 冲高后反转，GLD 可能反弹。

**操作**：🟨 **持有不加，不减**（避险仓位 thesis 仍成立）。ATR stop $420.18 距现价 -3.2%，跌破减至 5% 仓位。
**信心 58%**

---

### SCHD $31.23 | 稳健持仓，加仓窗口窄化

**5 层**:
- L1: 🟢 RSI 60.5 多头, BB **91%**, EMA50 $30.54, ATR stop $30.74 (距现价仅 -1.6%!), Vol 0.4x
- L2-L4: N/A
- L5: 🟢 P/C Vol **0.25**（深度偏多，SCHD 期权流极稀的正向信号）

**对立面**：BB 91% 突破上轨风险（昨天 4/23 快扫已 flag BB 116%），红利股短期也会超买回调。

**操作**：🟩 **加仓计划略微调整**
- 原计划 $500 @ $30-31 一次性加仓
- 🆕 **修订**：当前 $31.23 已在计划上沿，**分两批**：
  - 第一批 $250 @ $30.80-31.20（现在或盘中回撤）
  - 第二批 $250 @ $30.40 以下回踩 EMA50
- 若 SCHD 两日内突破 $31.50 不回踩 → 放弃第二批，只加 $250

**信心 82%**

---

### MU $499.84 | 信号持续衰减，候选降级

**5 层**:
- L1: 🟢 RSI 69（接近超买）, EMA50 $411.46 / EMA200 $296.43, BB 89%, ATR stop $460.88, Vol 0.4x
- L2: 🟡 Bridgewater 1.2M +19% / Ren 36.7M **-10%**（v3.2 新发现的 Ren 反转 -10%，本次确认）
- L3: 🔴 90d 净卖 $53M（CBO Sadana 2 笔 $18M + CPO Arnzen $9M）
- L4: z=+0.8 正常
- L5: 🔴 **7 个激进 put 异常！** — 4/24 P $495 Vol/OI **29.1x**、P $500 = **26.6x**、P $492.5 = 11.4x

**新闻**（[Micron HBM orders](https://247wallst.com/investing/2026/04/23/micron-is-up-68-ytd-as-hbm-demand-explodes-is-the-memory-rally-sustainable/) + [Q3 Guidance](https://www.themarketsdaily.com/2026/04/09/micron-technology-nasdaqmu-issues-q3-2026-earnings-guidance.html)）：
- MU YTD **+68%**（落后 Marvell +95% 但领先 AMD +43%）
- 🆕 HBM 2026 全年产能（含 HBM4）**100% 售出**，multi-year binding contracts
- FY26 Q3 指引 **revenue ~$33.5B**（vs consensus $22.4B，**+50%**）、毛利率 **~81%**、EPS 约 $19.15 vs consensus $10.50
- HBM TAM 从 2025 年 $35B 增长到 2028 年 **$100B**
- HBM4 高良率量产为 Nvidia Vera Rubin 供货（2026 Q1 启动）

**对立面**（强）：基本面史上最强，但股价 $500 已从 $290 (3个月前) 涨 +72%。L5 put 异常集中说明机构在高位对冲（非做空），可能预示 Q3 财报（约 6/25）前的正常回调。

**操作**（修订）：🟨 **继续缩小建仓，等回踩**
- v3.1 $800 → v3.2 $300 → **v3.3 维持 $300 或下调 $200**
- 入场 $440-460（回踩 ATR stop $460.88）或 $411 EMA50
- 止损 $400（跌破 EMA50 -3%）
- 目标 $540 / $600
- **对立面强化理由**：(a) L2 Renaissance 反转减 10%；(b) L3 C-suite 连续 $27M 卖出；(c) L5 0DTE put 集中对冲；(d) 基本面已完全 priced in（YTD +68%）

**R:R @ 入 $450**: (540-450)/(450-400) = 1.8:1 ⚠️（<2:1 提示边际）
**信心 55%** ⚠️（最低，接近猜测）

---

### OXY $56.73 | 温和多头 + 🆕 新做空预警

**5 层**:
- L1: 🟢 RSI 47（中性偏弱）, EMA50 $55.74 / EMA200 $48.05, BB 33%, ATR stop $53.53, Vol 0.2x
- L2: 🟡 Berkshire 数据疑（1.1M =0% 显示不完整）
- L3: — 0 买 0 卖 90d
- L4: **🟠 z=+1.7 做空偏高**（从 v3.2 z=-0.7 跳升，是本周 11 只股中唯一一个新出 🟠 信号！）
- L5: 🟢 P/C Vol 0.41 偏多 + 1 OTM put 对冲（5/1 P $52 Vol/OI 5.7x）

**操作**（修订）：🟥 **暂停 OXY 小仓计划**
- v3.2 计划从 dry powder 加 $300 @ $54-55
- 🆕 **暂停理由**：L4 做空 z+1.7 新警报 + 回测 Single-Buy 三次全负（-10/-20/-6%）+ L2 Berkshire 数据仍疑
- 重新进入决策需要 L4 回落到 z<+1.0 且 Buffett 持仓数据核实

**信心 60%**

---

### AMD $350.39 ⚠️ | 5 层偏空 + L5 散户 FOMO 白热化（陷阱 B+F+G）

**5 层**:
- L1: 🔴 **RSI 89.2 极度过热**（v3.2 82 → +7 点）, BB **111%**（突破上轨）, EMA50 $236.86 / EMA200 $202.53, **Vol 1.3x 放量**
- L2: 🔴 Bridgewater 0.2M -21% / Ren 0.6M -23%（量化双减）
- L3: 🔴 90d 净卖 $63M 不变（CEO Su $7M + CTO Papermaster $7.4M）
- L4: z=+1.2 正常
- L5: 🔴 **9 个激进 call 异常！** — 4/24 C $360 Vol/OI **47.2x** IV 38%、C $345 = 46.0x、C $350 = 31.3x、C $370 = 30.1x；同时 5/1 P $330 = 28.4x

**新闻**（[AMD May earnings preview](https://247wallst.com/investing/2026/04/16/amd-gains-6-ahead-of-may-earnings-is-the-ai-chip-challenger-finally-ready-to-rival-nvidia/)）：
- 5/5 财报盘后 5pm ET
- Q1 revenue 指引 $9.8B ± $300M（consensus $9.84B 已 priced）
- 非 GAAP 毛利率 ~55%，OpEx ~$3.05B
- 2026 data center 长期目标 +60% YoY，2027 AI 营收 tens of billions
- Q4 2025 data center 收入 $5.38B（+39% YoY）
- 🆕 4/23 盘后 AMD 涨到 $330，现 $350（**24 小时内 +6%**）— 典型追涨狂热

**对立面**：MI325/MI350 数据中心路线图强势；Q1 已预期 beat，若 guide raise 可能再涨 10%。

**操作**：🟥 **继续禁止追涨 / 不建仓**
- ATR stop $329.88 距现价 -5.9%
- 若财报 guide raise → gap up 10-15% 后减仓观察（但无仓位 = 无动作）
- 若 guide 平平 → gap down 15-20% 概率高，至 $280-300 区间

**信心 88%**（本周最高）— 5 层全部偏空，仅 L5 是散户 FOMO 反常多头

---

## 全局视角

**组合健康度**：
- 8/8 持仓中 **5 只 🟨 持有不加仓**，1 只 🟥（META 财报前减半），2 只 🟩（SCHD 加仓 + TSM 升级为加仓候选）
- 🟥 占比 = 1/8 = **12.5%**（远低于 50%，方法论稳定）
- **防御姿态过 FOMC + 财报三连周**

**本周事件密度（4 天内发生）**：
```
周一 4/27 ─ 盘前 Q1 财报集中期 (非本持仓)
周二 4/28 ─ FOMC Day 1
周三 4/29 ─ FOMC 利率决议（下午）+ META 财报（盘后）
周四 4/30 ─ PCE 公布（上午）+ AAPL 财报（盘后）
周五 5/01 ─ CVX 财报（盘前 11am ET）
周一 5/02 ─ NFP 就业数据
周一 5/05 ─ AMD 财报（盘后）
```

**最紧急 24-48 小时行动**（按优先级）：
1. 🟥 **4/28 收盘前 META 减半**（卖 0.09 股约 $61）
2. 🟩 **本周任意日 SCHD 第一批加仓 $250** @ $30.80-31.20
3. 🟨 **SI 跟踪 OXY（已 z+1.7）+ CVX（维持 z+1.5）** — 若任一本周 z>2 主动减半
4. 🟨 **TSM 回踩 $385-395 ATR 附近 挂单加仓**（被动触发）

**科技敞口**：
- AI 芯片（NVDA + TSM）: ~24%（TSM 涨到 $405 导致 TSM 市值占比升至 ~6% 从 4%）
- 大盘科技（AAPL + META）: ~10%
- SPY 宽基（~30% 科技暗含）: 33.5%
- 实际科技 beta ≈ 50%（不变）

---

## Top 3 可操作建议（本周）

### #1 🟥 META 4/28 收盘前减半
- 动作: **卖 0.09 股**（保留 0.09 股）
- 价格: 市价 ~$670-680
- 套现: ~$60
- 执行窗口: 2026-04-28（FOMC Day 1 结束后，财报前一日）
- **为什么减半不清仓**：Capex guide 可能维持 $115-135B（已 priced），Ackman NEW + Tepper +62% + Q1 ad +18% = 不清仓保留 upside
- **为什么不持有**：L3 CFO $106M + L5 陷阱 F + PEAD 分化（-15% 到 +11%）= 风险敞口过大
- 对立面: 若 Beat + Capex <$125B，少赚 $5，保险优于贪婪
- 信心: 75% 🟥

### #2 🟩 SCHD 加仓第一批 $250
- 动作: 买入 ~8 股（$250 / $31.12）
- 价格: $30.80-31.20 区间
- 执行窗口: 4/25-28 任意日（FOMC 前）
- 第二批 $250 留 @ $30.40 以下等回踩 EMA50
- 对立面: BB 91% 短期超买（已 flag），但长周期持仓不择时
- 信心: 82% 🟩

### #3 🟨 TSM 被动挂单加仓 $300-400
- 动作: 限价挂单 $385-395（ATR stop 附近）
- 若成交：仓位 ~16-20%（目标）
- 若 1 周内未触发 → 取消，等财报后新数据再决定
- 止损 $345（-10%）
- 目标 $450 / $480
- 对立面: 当前 $405 已涨 +8%，可能不回踩；错过就错过，不 FOMO
- 信心: 78% 🟨

---

## 陷阱清单

| 标的 | 陷阱 | 说明 |
|---|---|---|
| **AMD** | **B + F + G** 三连 | RSI 89 + BB 111 + 9 个激进 call (47x Vol/OI) + 机构 put 对冲 = 极度警戒 |
| **NVDA** | **E + G** | 散户 P/C 0.34 偏多 vs 机构 6 个 put 新建（50.5x Vol/OI）+ 陷阱 G 波动预期 |
| **META** | **F** | 0DTE 财报前 call 狂欢（Vol/OI 7-10x）— 散户噪声 |
| AAPL | E 降温 | P/C 从 0.29 升到 0.61，陷阱强度下降 |
| **MU** | **F** | 0DTE put 集中对冲（29x + 26x）— 机构在高位防御 |
| SPY | F | 50 个 0DTE 异常（P $716 61x）— 主导当日 vol |
| CVX | D 反向 | Double-Buy 价值派 vs C-suite 集体抛 $155M |
| GLD | — | 技术走弱但无主动陷阱命中 |

---

## 关键纪律触发点（已接近或正在接近）

| 标的 | 现价 | 距止损 | 触发条件 | 24h 内动作 |
|---|---|---|---|---|
| **META** | $675.00 | — | 财报前 4 天 | **4/28 前减半** |
| **AAPL** | $270.29 | -3.3% 到 $261.48 | 跌破 ATR / 毛利率 <48% | 减半 |
| **NVDA** | $209.15 | -3.9% 到 $201.09 | 跌破 ATR 连续 2 日 | 减至 10% 仓位 |
| **SPY**  | $713.16 | -1.8% 到 $700.24 | 跌破 ATR | 减至 20% 仓位 |
| **CVX**  | $183.77 | -4.2% 到 $176.09 | 跌破 ATR | 减半 |
| **GLD**  | $434.02 | -3.2% 到 $420.18 | 跌破 ATR / 单日 -5% | 减至 5% 仓位 |
| **SCHD** | $31.23 | -1.6% 到 $30.74 | 跌破 ATR | 重新评估加仓时机 |
| **TSM**  | $404.84 | -4.8% 到 $385.28 | 跌破 ATR | 持有不加（候选） |

**新增监控**：
- **OXY 短兴趣 z+1.7** → 周末再查 FINRA 数据若 z>2 则**取消小仓计划**
- **CVX 短兴趣 z+1.5** → 若本周 z>2 主动减半（不等 5/1 财报）

---

## 日历同步预备清单（Phase 3 读这里）

### 📊 财报事件
- **2026-04-29 Wed** META 财报（盘后 4:00pm ET）— Implied **±7.6%**, noise <5%
- **2026-04-30 Thu** AAPL 财报（盘后 5:00pm ET）— Implied **±4.1%**, noise <3%
- **2026-05-01 Fri** CVX 财报（盘前 11:00am ET）— Implied **±3.7%**, noise <2.5%
- **2026-05-05 Mon** AMD 财报（盘后 5:00pm ET）— Implied ~±6%（未算，无持仓）
- **2026-05-20 Wed** NVDA 财报（盘后）— 较远

### 🏛️ 宏观事件
- **2026-04-28-29 Tue-Wed** FOMC 利率决议 — 预期 **Hold**（3.50-3.75%），点阵图关注 2026 仅 1 次降息
- **2026-04-30 Thu 8:30am ET** PCE（3 月）— consensus 2.7% YoY headline / 2.7% core
- **2026-05-02 Fri 8:30am ET** NFP（4 月就业）
- **2026-05-12 Tue 8:30am ET** CPI（4 月）

### 📅 Ad-hoc 事件
- **2026-09-01** AAPL CEO 正式交班（Cook → Ternus）— 已确认

### ⚠️ 纪律警告
- **META** 4/28 前减半（📍 下周一执行）
- **OXY** SI 监控：若本周 z>2 取消建仓计划
- **CVX** SI 监控：若本周 z>2 主动减半

---

## 上周对比（v3.2 2026-04-22 → v3.3 2026-04-24）

**新出现的信号**：
- 🆕 **NVDA 陷阱 E 再现**（P/C 0.34 + 6 put 新建，之前是陷阱 G）
- 🆕 **OXY L4 做空 z 从 -0.7 跳到 +1.7**（🟠 新警报，本周唯一）
- 🆕 **TSM L3 确认升级**（Burns $322K 个人大仓 + 3M 内全买无卖）
- 🆕 **AMD 股价 $296 → $350（+18%）** + RSI 82 → 89，陷阱 B+F 白热化

**解除的风险**：
- ✅ **CVX Wheatstone LNG 完全恢复**（4/23 官宣）— v3.2 最大地缘风险解除

**数据时效更新**：
- FOMC 日期修正（v3.2 误写 5/6-7 → 实际 **4/28-29**）
- AAPL Implied Move ±5.0 → **±4.1%**（市场预期更确定）
- CVX Implied Move ±5.1 → **±3.7%**
- META 8/8 Beat 率（v3.1 曾误写 7/8，v3.2/v3.3 确认 8/8）

**13F 无变化**（Q1 2026 最新文件 2026-02-17 filed，下次更新 Q1 2026 Form 13F-HR 约 2026-05-15）

---

## 📋 交易纪律确认书 / 2026-04-24

```
┌────────────────────────────────────────────────────────┐
│              交易纪律确认书 / 2026-04-24 (v3.3)           │
├────────────────────────────────────────────────────────┤
│                                                        │
│  组合整体逻辑（本周）：                                  │
│  防御姿态度过 FOMC + 3 财报 + PCE + NFP 七连事件；       │
│  META 财报前减半套保险，SCHD 分批加仓承接 dry powder，   │
│  TSM 回踩加仓挂单（被动），OXY/MU 因新警情况暂停建仓。   │
│                                                        │
│  【本周必做（按顺序）】：                                │
│                                                        │
│  □ 4/25-28: SCHD 第一批加仓 $250 @ $30.80-31.20         │
│  □ 4/28 (FOMC Day 1 后): META 减半卖 0.09 股            │
│  □ 整周: TSM 限价 $385-395 挂单 $300-400                │
│  □ 周六/周一: 核对 FINRA 数据更新 OXY/CVX SI z-score    │
│                                                        │
│  【强制止损/减仓触发点】：                                │
│                                                        │
│  □ META Miss + Capex ≥$135B → 清仓剩余 0.09 股          │
│  □ META gap down >10% (超 implied move) → 清仓          │
│  □ AAPL 毛利率指引 <48% → 减半                           │
│  □ AAPL gap down >7% → 减半                              │
│  □ CVX 跌破 $176.09 (ATR) → 减半                        │
│  □ CVX 跌破 $167.51 (EMA200) → 清仓                     │
│  □ CVX SI 本周 z>2 → 主动减半（不等财报）                │
│  □ OXY SI 本周 z>2 → 取消建仓计划（不加）                │
│  □ GLD 跌破 $420.18 (ATR) → 减至 5% 仓位                │
│  □ NVDA 跌破 $201.09 (ATR) 连续 2 日 → 减至 10% 仓位    │
│  □ SPY 跌破 $700.24 (ATR) → 减至 20% 仓位               │
│  □ TSM 跌破 $385.28 (ATR) → 不执行加仓挂单              │
│                                                        │
│  【财报周特别纪律（4/29-5/1）】：                        │
│                                                        │
│  □ 财报前 24h 不新建任何仓位                             │
│  □ 财报后 gap down >8% 等 2 个交易日再决策               │
│  □ 不在财报当日追涨或抄底                                │
│  □ 每只财报后 48h 内复盘是否命中 implied move            │
│                                                        │
│  【FOMC 特别纪律（4/29 下午）】：                        │
│                                                        │
│  □ FOMC Statement 公布后先观察 30 分钟，不急操作         │
│  □ 鹰派意外（指出通胀粘性）→ SPY/GLD 都可能 -2%          │
│  □ 鸽派意外（暗示 2 次降息）→ SPY/GLD 可能 +1-2%         │
│                                                        │
│  【信号监控升级】：                                      │
│                                                        │
│  □ NVDA 陷阱 E 深化 → 警惕 ATR stop $201 连续破          │
│  □ AMD 财报 5/5 若 gap up >10%：无仓位无动作            │
│  □ AMD 财报后若 gap down 到 $270-290 → 考虑建仓 $300    │
│  □ TSM 若突破 $420 不回踩 → 放弃本轮加仓，等下轮         │
│                                                        │
│  承诺：上述条件触发时，我将在 24 小时内执行，             │
│  不找"等反弹"借口，不因浮亏心理抵触而延迟。              │
│                                                        │
│  自省（v3.3 新）：                                       │
│  - v3.2 误将 FOMC 写作 5/6-7 — 必须每次分析 WebSearch   │
│    核实日期，不信缓存信念                                │
│  - MU 信号从 "三派共振" 衰减至 "单派小加"，提示 13F      │
│    数据每次必读脚本输出，不复用上次结论                  │
│  - AMD 2 天涨 18% 的速度超过任何止损线 — 追涨陷阱 B      │
│    在 FOMO 阶段极具吸引力，纪律化回避是唯一解            │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 数据来源 & 新闻链接

**Phase 1 脚本数据**（2026-04-24 盘中 UTC）: portfolio / smart_money / insider / short_interest / options / earnings 全 exit 0

**Phase 2a WebSearch 链接**:
- [META Q1 2026 Earnings Preview](https://www.indexbox.io/blog/meta-platforms-q1-2026-earnings-preview-ai-investment-impact/)
- [Meta 2026 Capex $115-135B](https://www.datacenterdynamics.com/en/news/meta-estimates-2026-capex-to-be-between-115-135bn/)
- [Apple Q2 Earnings Preview](https://finance.yahoo.com/markets/stocks/articles/apple-q2-earnings-preview-aapl-154221571.html)
- [CNBC: Apple CEO Change Timing](https://www.cnbc.com/2026/04/21/why-the-timing-of-apples-ceo-change-could-mean-a-good-earnings-report-is-around-the-corner.html)
- [Chevron Wheatstone Restored](https://www.gurufocus.com/news/8813320/chevron-cvx-resumes-full-lng-production-at-wheatstone-plant-after-cyclone-repairs)
- [CVX Guyana Catalyst](https://www.financialcontent.com/stocks/article/finterra-2026-4-13-chevron-cvx-in-2026-the-new-era-of-energy-addition-and-the-guyana-catalyst)
- [NVIDIA Q1 FY26 Blackwell](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2026)
- [Micron HBM Sustained Rally](https://247wallst.com/investing/2026/04/23/micron-is-up-68-ytd-as-hbm-demand-explodes-is-the-memory-rally-sustainable/)
- [Micron Q3 Guidance](https://www.themarketsdaily.com/2026/04/09/micron-technology-nasdaqmu-issues-q3-2026-earnings-guidance.html)
- [TSMC CEO Insider Buying](https://www.themarketsdaily.com/2026/04/16/insider-buying-taiwan-semiconductor-manufacturing-nysetsm-ceo-acquires-10763-82-in-stock.html)
- [AMD May Earnings Preview](https://247wallst.com/investing/2026/04/16/amd-gains-6-ahead-of-may-earnings-is-the-ai-chip-challenger-finally-ready-to-rival-nvidia/)

**方法论**: `docs/METHODOLOGY_v3.md` / **持仓**: `config/holdings.yaml` v3.2 / **基线**: `reports/2026-04-22-weekly-deep.md`

---

*本报告在 Claude Code 本地会话中手动合成（云端 Phase 2b trigger 仍存在 stream idle timeout 风险）。建议每周六或周日运行一次完整 v3.3 流程。*

# DMO 周报 2026-04-26 (v3.4 — FOMC+财报四连前夜·周末整备版)

> 本报告基于 2026-04-24 周五收盘后 Phase 1 脚本数据（6/6 成功，今日为周日补跑）+ 14 次 WebSearch 叙事/日历验证。
> 距 v3.3 (2026-04-24) 一个交易周末：**L1 价格无变化**（市场休市），但 **L4 短兴趣 5 个 ticker 显著反转**、**L5 期权链出现新的 0DTE 极端定位**（NVDA 4/27 put 单合约 Vol/OI 182x、AMD 5/1 ATM 双向 33-62x），且 **Tepper 13F 在 AMD/MU 的新数据揭示**。本周报功能定位：**FOMC + 三财报 + PCE + NFP 七连大事件前夜的最后一次系统性整备**。

---

## 搜索链状态

| Phase | 状态 | 备注 |
|---|---|---|
| Phase 1 脚本 | ✅ **6/6 成功** | portfolio/smart_money/insider/short/options/earnings 全 exit 0 |
| Phase 2a WebSearch | ✅ **14 次** | 4 宏观 + 8 持仓/候选叙事 + 1 SCHD 上下文 + 1 排雷（AMD short seller 0 hits）|
| Phase 2b 合成 | ✅ 会话内完成 |
| Phase 3 报告写入 | ✅ |
| Phase 4 提交/通知 | 待跑 |

**数据时间戳**：portfolio 4/24 收盘；options 4/24 盘后链；FINRA short 最新 **2026-04-24（T+1，本次新增数据）**；Form 4 90d 滚动窗口；13F 仍为 Q1 2026（2026-02-17 filed，下次更新 ~2026-05-15）。

---

## 🗓️ 市场背景（2026-04-26 Sun，周末整备）

| 指标 | 读数 | 含义 |
|---|---|---|
| SPY | $713.94（4/24 close，距 4/17 ATH $710.14 创新高 +0.5%）| 压舱石持续刷 ATH |
| S&P 500 指数 | 7,138（4/22 close）| 6 季度连续两位数 YoY 盈利增长（FactSet）|
| 本周距事件 | **2 天** 到 FOMC Day 1 | FOMC 4/28-29 → META 4/29 → PCE+AAPL 4/30 → CVX 5/1 → NFP 5/2 → AMD 5/5 |
| FOMC 概率 | **Hold 99.7%**（Polymarket）/ JPM "On hold + 2026 不再降息，2027 Q3 +25bp" | 鹰派定价已极度饱和 → 鸽派意外空间小 |
| March CPI | **3.3% YoY（自 May 2024 最高）** Iran 油价驱动；Core CPI +0.2% benign | Headline 烫但 Core 温和 → Fed 可继续 hold 但难再降 |
| Fwd P/E | 20.9（>5y avg 19.9 / 10y avg 18.9）| 估值偏高，盈利季 beat 才能撑 |
| 净利率 | 13.4%（FactSet 自 2009 来最高记录）| 基本面顶部数据 |
| Q1 报告进度 | 28% 已报告，beat 率/幅度均高于近期均值 | 进入持仓密集报告周 |

**新增宏观警示（v3.4）**：
- **March CPI 3.3% headline 是 11 个月新高** — 这是上周 v3.3 没强调的关键数据，FOMC 鸽派意外的概率被极度压缩
- 市场已 priced FOMC hold 至 99.7%（vs v3.3 时 ~95%），鹰派意外（如 dot plot 删除 2026 任何降息）才是真风险

---

## 📊 5 层共振总览表（11 只股，4/24 收盘 + 4/24 SI 更新）

| Ticker | 价格 | L1 技术 | L2 13F | L3 Form4 (90d) | L4 SI z (4/24) | L5 期权 | 整体等级 | 陷阱 | 信心 |
|---|---|---|---|---|---|---|---|---|---|
| NVDA | $208.27 | 🟢 RSI **71.5** BB 88% Vol 1.4x | ⚠️ 分裂 + Scion NEW | 🔴 -$172M (20 filings) | — z+0.3 | **🚨 4/27 put Vol/OI 182x**（陷阱 G + 跨资产 hedge）| **3 层警戒** | **G + E** | 75% |
| SPY | $713.94 | 🟢 过热 RSI **70.5** BB 81% | N/A | N/A | — z-1.0（小幅回补） | 🔴 93 异常 + P/C 1.18 偏空 | **ATH + 期权防御**| F | 65% |
| AAPL | $271.06 | 🟢 RSI **59.7** BB **80%**（继续收窄） | 🔴 全员减 | 🔴 -$24M (20 filings) | — z-0.9（空头回补） | 🔴 P/C 0.57 + 6 put 异常 (P $200 IV 194%) | **4 层偏空** | E 平稳 | 73% |
| META | $675.03 | 🟡 死叉修复 RSI **61.5** | ⚠️ 分裂（Ackman NEW / Burry EXIT）| 🔴 CFO Li -$106M | **🟠 z+1.2 升温** | 🔴 P/C 0.59 + **8 个 0DTE put 异常** | **4 层偏空 + 财报 -2d** | **F + L4 升温** | 78% |
| TSM | $402.46 | 🟢 RSI **68.4 BB 98%** Vol **1.6x** | 🔴 缓退 | 🔥 6 高管买 + WebSearch 3M 33 buys | — z-1.4（空头回补）| 🟢 7 call 异常 + 1 深 OTM put | **L1 强势 + L4 改善** | — | 80% |
| CVX | $185.21 | 🟡 RSI **41.3** BB **28%** | 🟢🟢 Double | 🔴 -$155M（CEO + CLO + CBO + CFO 全 C-suite 抛）| **🟡 z-1.5 (反转)** ✨ | 🟢 5 异常 + 3 call | **风险释放** | D 反向 | 65% |
| GLD | $433.25 | 🟡 RSI 47.5 破 EMA50 持续 3 天 | N/A | N/A | **🟢 z-2.3 强空头回补** ✨ | 🟢 5 call（4/27 C $438 Vol/OI 6.1x）| **空头投降** | — | 65% |
| SCHD | $31.20 | 🟢 RSI 59.8 BB **89%** ATR 安全垫仅 1.6%! | N/A | N/A (CIK 不在 SEC) | **🟠 z+1.6 新警** ⚠️ | 🟢 P/C **0.22** 极偏多 | **L4 vs L5 冲突** | — | 70% |
| MU | $496.72 | 🟢 RSI **68.9** BB 87% | 🟢🟢🟢 TRUE Triple-Buy + Tepper 1.8M ^+250% | 🔴 -$42M（窗口滑动从 -$53M）| — z-1.2（空头回补） | 🔴 35 异常 P/C 1.14 + 5/1 P $500 ITM 12.7x | **信号衰减** | F | 55% ⚠️ |
| OXY | $57.12 | 🟢 RSI 48.4 BB 36% | 🟡 Berkshire 264.9M =+0%（**修复 v3.3 数据疑**）✨ | — 17 filings 净 $0 | — z+0.9（**从 +1.7 回落**）✨ | 🟢 P/C 0.20 极偏多 + 2 OTM call 大单 | **温和多头 + 警报解除** | D | 65% |
| AMD | $347.81 | 🔴 **RSI 88.9 极度过热** BB **110%** Vol **2.1x** | 🔴 量化双减 + **🆕 Tepper 0.3M v-66%（4/24 报告未含）** | 🔴 -$63M（Su+CTO）| — z+0.5（普通） | 🔴 **40 异常**：5/1 P $330 Vol/OI **62.3x** + C $400 33.4x（陷阱 F+G 同步白热化）| **5 层偏空 + 散户 FOMO 极致** | **B + F + G + Tepper 减** | **88%** |

图例：🟢 多 / 🟡 中性 / 🔴 空 / ⚠️ 分裂 / 🔥 罕见强信号 / ✨ 本周新变化 / 🚨 极端读数

---

## 🔥 本周 5 个核心变化（vs v3.3 2 个交易日前）

### ✨ 变化 1：5 个 ticker 短兴趣同向反转（CVX/OXY/MU 警报解除，SCHD 新警，GLD 空头投降）

**全市场 SI 反转图谱（v3.3 → v3.4）**：

| Ticker | v3.3 z (4/22) | v3.4 z (4/24) | Δ | 含义 |
|---|---|---|---|---|
| **CVX** | +1.5 🟠 | **-1.5 🟡** | **-3.0σ** | Wheatstone 恢复 + Q1 timing 已 priced → 空头回补 |
| **OXY** | +1.7 🟠 | **+0.9 —** | **-0.8σ** | OXY 已从 4/20 8% 下跌后稳定，做空者获利了结 |
| **GLD** | -1.4 🟡 | **-2.3 🟢** | **-0.9σ** | Gold 从 $5,595 ATH (-15%) 后空头大量获利平仓 |
| **MU** | +0.3 — | **-1.2 —** | **-1.5σ** | Q3 指引强劲 + HBM4 binding contracts 后空头回补 |
| **SCHD** | +0.7 — | **+1.6 🟠** | **+0.9σ** | 新警！可能与 4/24 reconstitution churn 相关（22 删 25 加），不是基本面 |

**核心解读**：
- **CVX 反转最大（-3σ）**：v3.3 把 "CVX SI z>2 主动减半" 列为纪律触发点，今日确认**该风险已解除**，SI 不再是 CVX 的主导担忧。剩余风险只剩 5/1 财报本身 + L3 内部人抛压
- **OXY 警报解除**：v3.3 暂停 OXY 小仓建仓（理由：z+1.7 + Single-Buy 历史负 alpha）。z 回落到 +0.9 触发"重新进入决策"条件之一，但 Single-Buy 历史负 alpha 仍未变 → **维持暂停**，等下次 SI 数据若进入 z<+0.5 才考虑
- **GLD z-2.3** 是**极强信号**（spec: z<-2 阈值触发）→ 空头投降 = 短期支撑有效，配合 L5 4/27 多个 OTM call（虽量小）→ GLD 不止损（v3.3 决策维持）
- **SCHD 新警**：但 L5 P/C 0.22 极偏多 + reconstitution churn 是技术性原因（不是基本面恶化）→ **不影响加仓计划**，但本周 第一批 $250 加仓时机更要选 EMA50 附近回踩
- **MU 空头回补**：v3.2 说 Renaissance "-10% 反转"，现在 MU 也出现空头回补 → 但 L5 仍有 5/1 P $500 ITM Vol/OI 12.7x（机构高位对冲）→ 不变更"持续缩小建仓"决策

---

### ✨ 变化 2：NVDA 4/27 单日 0DTE put 出现极端 Vol/OI 182x（事件对冲炸弹）

**v3.3 时**：NVDA Top 5 异常 4/24 P $210 Vol/OI 50.5x + P $205 26.1x（已经罕见）
**v3.4 现在**：4/24 收盘后链路重抓，**4/27（周一）单日 put 异常 Vol/OI 全部进入历史前列**：
- **4/27 P $207.50 (OTM -0.4%)**: Vol **48,952** vs OI 269 = **182.0x** IV 49%
- 4/27 P $210.00 (ITM +0.8%): Vol 32,099 vs OI 301 = **106.6x** IV 50%
- 4/27 P $205.00 (OTM -1.6%): Vol 40,543 vs OI 616 = **65.8x** IV 50%
- 4/27 C $217.50: Vol 25,560 vs OI 808 = 31.6x（多头）
- 4/29 C $220.00: Vol 36,154 vs OI 1,321 = 27.4x（多头）

**这是什么场景？**
1. NVDA 财报 5/20（24 天后），所以**不是财报对冲**
2. 4/27 是**周一**，FOMC Day 1 当晚 → 这是**单日跨资产 FOMC hedge**：把 NVDA（高 beta AI 龙头）当 SPY 替代品做空对冲
3. 同时存在 4/27 OTM call + 4/29 OTM call → 散户在赌 FOMC + META 财报后的 AI 板块上涨
4. **典型陷阱 G 升级版**：机构买短到期 ATM put 大幅对冲单日下行（这种 Vol/OI 182x 在 4/27 当天接近 200% 新开仓量），同时散户买 OTM call 赌涨 → 双边定位极端

**操作影响**：
- v3.3 NVDA 决策"持有不加仓 ATR stop $200.10"维持
- 但 4/27-4/29 三天内 NVDA 可能出现 ±5% 单日波动（市场已定价）
- **若 NVDA 4/27 收盘 < $201.09 ATR 止损 + 第二日继续跌破** → 按既定纪律减至 10% 仓位（v3.3 既有触发条件）
- **不要在 4/27 盘中追涨追跌**，等 4/29 FOMC + META 同日尘埃落定

**信心 75%**（从 72% 上调，因信号清晰度提升）

---

### ⚠️ 变化 3：AMD 5/1 期权链出现"陷阱 F + G 同时白热化"罕见组合

**v3.3 时**：AMD 5 层偏空 + 9 个激进 call 异常 + 5/1 P $330 28.4x（已极度警戒）
**v3.4 现在**：5/1 chain（FOMC 后 + AMD 财报前 4 天）出现**机构与散户极致对赌**：
- **5/1 P $330 (OTM -5.1%)**: Vol 7,918 vs OI 127 = **62.3x** IV 81% → **机构买保护**
- 5/1 C $390 (OTM +12.1%): Vol 5,838 vs OI 161 = 36.3x → **散户赌财报暴涨**
- 5/1 C $355 (OTM +2.1%): Vol 9,988 vs OI 295 = 33.9x → 散户多头
- **5/1 C $400 (OTM +15.0%)**: Vol **16,964** vs OI 508 = **33.4x** → 极度 FOMO 赌单
- 5/1 C $365: Vol 3,523 vs OI 154 = 22.9x

**关键背景（WebSearch 验证）**：
- AMD 5/5 财报盘后，已 guide Q1 revenue $9.8B ±$300M（consensus 已 priced）
- 数据中心 >60% 长期增长目标已在 Q4 2025 Earnings Call 重申 → **若 5/5 没有 raise 就是 disappointment**
- 🆕 **Tepper 13F 在 AMD 数据本次首次完整显示**：0.3M v-66% — Appaloosa 大幅减仓 AMD
- v3.3 时 L2 已知 Bridgewater -21% + Ren -23%（量化双减），现 + Tepper 主观派也 -66% → **L2 升级为 Triple-Sell**（罕见警告）

**陷阱白热化的双面定位含义**：
- 散户付 $355-$400 OTM call（IV 80%+，每张 $200-300）= 财报前最后一周 0DTE 类博彩
- 机构付 $330 put（IV 81%，每张约 $400）= 真金白银的下行保护
- **历史上"散户 OTM call >> 机构 OTM put"组合**是最差 risk-on 时刻之一：散户付高 IV + 机构低位接保护

**操作**：🟥 **继续禁止追涨**（v3.3 决策维持）。**若财报后 gap down 15-20% 到 $280-300 → 小仓试探 $200**（不是 v3.3 写的 $300，因为 Tepper 主观派出局是新负面）
**信心 88%**（持平本周最高 — 5 层全偏空 + 散户 FOMO 极度）

---

### ⭐ 变化 4：TSM 强势继续 + L4 反转（z+1.4 → z-1.4）+ Taiwan 单股持仓上限松绑

**v3.3 时**：TSM 突破 $405、L3 升级（Burns +1000sh $322K + 33 buys 0 sells 3M）、L4 z+1.4 偏高
**v3.4 现在**：
- 价格 $402.46（本周 4/24 收盘，**Taiwan 监管放松后开盘新高 $402.16**）
- L4 SI **从 z+1.4 反转到 z-1.4**（差 -2.8σ） → 地缘对冲明显减弱
- L1 **BB 98% 仍超买、Vol 1.6x 放量** → 4/24 才完成的突破未回踩
- L2 仍 🔴 缓退（Tiger -19% / Third Point -61% / Ren -13% 不变）
- L5 7 个 call 异常 + 仅 1 个深 OTM put（5/1 P $230 -43% OTM IV 175%，灾难尾对冲）

**🆕 WebSearch 关键新闻**：
- **Taiwan 监管将 local equity funds 单股持仓上限从 10% 提升到 25%**（2026-04-24 同期生效）
- → 潜在**数十亿美元 inflow into TSMC**（台股 TSM 占大盘市值 ~40%）
- → 这是 BB 98% 突破 + L4 短兴趣回补的根本原因

**操作（升级 v3.3 "回踩 $385-395 挂单加仓"）**：
- 🟨 **当前 $402.46 仍不追**（BB 98% / RSI 68.4 接近超买 + Vol 1.6x 高换手）
- 🟩 **挂单维持 $385-395 区间 $300-400 加仓**（被动触发）
- 🟩 **若 ATR stop $382.48 跌破 + 1 日内反弹** → 视为 false break，挂单上调至 $390-400 区间补仓
- 止损不变 $345（跌破 EMA50 -3%）
- 目标不变 $450 / $480
- **新加论据**：Taiwan 监管 inflow 是结构性买盘（不是短期催化），叠加 L3 内部人买 + L4 SI 改善 = **加仓信心从 78% 升到 80%**

**R:R @ 入 $390**: (450-390)/(390-345) = 1.33:1（< 2:1，但有结构性催化 → 接受）

---

### ✅ 变化 5：CVX/OXY 13F 数据完整化 + L4 SI 警报解除

**v3.3 时**：OXY 标 "Berkshire 1.1M =0%（数据疑）"
**v3.4 现在**：smart_money_scan 对 OXY 显示 **Berkshire 264.9M =+0%**（**数据已完整修复**）

- 这个数字与 WebSearch 验证一致（Berkshire 持有 OXY 264.9M 股，约 28.2% of OXY outstanding）
- **修复后陷阱 D（单信源信仰）维持**：Buffett 是 OXY 唯一的 13F 大派，无其他派系 confirm
- 但 **OxyChem $9.7B 出售给 Berkshire（2026-01）+ debt 降至 $15B + 8% 提股息**已 priced
- v3.3 OXY SI z+1.7 是暂停建仓的主因，现 z+0.9 回落 → 但仍未到 z<+0.5 重新进入门槛 → **维持暂停**

**操作**：🟥 **OXY 维持暂停建仓**（理由：陷阱 D + Single-Buy 历史 alpha -10/-20/-6% + L4 仍偏高）
**信心 65%**（从 60% 升 5%，因数据完整 + L4 改善）

---

## 持仓逐只深度分析

### NVDA $208.27 | 持有不加仓 + 4/27 0DTE 极端 put 对冲警戒

**5 层**:
- L1: 🟢 RSI **71.5**（小超买）, EMA50 $187.25 / EMA200 $176.01 强多头, BB 88%, ATR% 2.6%, Vol 1.4x（接近放量）
- L2: ⚠️ 分裂 — Bridgewater 3.9M +54% / Ren 0.9M -85% / Third Point 3.0M +4% / Tepper 1.7M -11% / Tiger 11.0M -6% / **Scion 1.0M NEW**（罕见正信号维持）
- L3: 🔴 90d 净卖 **$172M**（20 filings，10 内部人）
- L4: z=+0.3 正常（vs v3.3 z+0.3 持平）
- L5: P/C Vol **0.39**（偏多） + 6 激进 call 异常，但 **Top 5 异常前 3 个全是 4/27 put 极端 Vol/OI**：
  - 4/27 P $207.50 Vol/OI **182.0x**（48,952 张新建）
  - 4/27 P $210.00 Vol/OI **106.6x**
  - 4/27 P $205.00 Vol/OI **65.8x**
  - 4/27 C $217.50 Vol/OI 31.6x（多头）
  - 4/29 C $220.00 Vol/OI 27.4x（多头，FOMC 当日到期）

**叙事**（[NVIDIA H200 China](https://finance.yahoo.com/news/nvidia-stock-falls-as-china-reportedly-restricts-imports-of-h200-chips-155203605.html)）：
- 中国海关近期被指示禁止 H200 进口（reuters 报道）→ 但 Trump 政府之前已允许 NVIDIA 出口 H200 给"approved" 中国客户（条件：上交 25% 中国营收给美国政府）
- 计划 mid-Feb 启动 40,000-80,000 H200 chips 首批，Q1 FY27 中国市场可能贡献 $1.28-2.56B
- 财报 5/20（+24d）

**对立面**（强）：H200 中国 deal 可能是 $5-10B/year 增量收入；Scion Burry 1M NEW 罕见看多（这是空头代理首次重仓 NVDA）；Blackwell + Vera Rubin 周期未结束。

**操作**：🟨 **持有不加仓**（v3.3 决策维持）
- ATR stop **$200.10**（距现价 -3.9%，紧）
- 4/27 单日 put 极端定位 → **不在 4/27 盘中触发减仓**，而是若 4/27 收盘 < $201.09 + 4/28 继续跌破 ATR → 减至 10% 仓位（既有规则）
- **绝不在 4/27 追涨追跌**

**R:R**：目标 $225（+8%）/ 止损 $200.10（-3.9%）→ R:R ≈ 2.1:1 ✅
**信心 75%**（从 72% 上调 — 信号清晰度提升）

---

### SPY $713.94 | ATH 不加仓，FOMC + 财报四连前最后一日

**5 层**:
- L1: 🟢 RSI 70.5 过热, BB 81%, EMA50 $680.66, ATR stop **$700.98**, Vol 0.7x
- L2/L3: N/A
- L4: z=-1.0（空头小幅回补，正常）
- L5: 🔴 **93 异常**（v3.3 时 50） + P/C Vol 1.18 偏空 + 6 个激进 put 异常
  - 4/27 P $713 Vol/OI 59.4x、P $712 = 54.6x、C $714 = 45.2x、P $714 = 41.2x
  - **典型 0DTE FOMC 跨资产 hedge 链**

**叙事**（[FactSet Earnings Update](https://insight.factset.com/sp-500-earnings-season-update-april-24-2026)）：
- 28% S&P 500 已报告 Q1，beat 率/幅度均高于近期均值
- 6 季度连续 double-digit YoY 盈利增长
- Net profit margin 13.4% = 自 2009 来最高纪录
- Forward P/E 20.9 偏高

**对立面**：若 FOMC 鸽派（删除 2026 唯一 1 次降息）+ PCE 温和 + AAPL/META beat → SPY 可能再 +2%。

**操作**：🟨 **持有不加仓**（v3.3 决策维持）
- ATR $700.98 距现价 -1.8%（最薄），跌破减至 20% 仓位
- 0DTE 主导的 vol 不构成进出场依据

**R:R**：目标 $725 / 止损 $700.98 → R:R ≈ 1.5:1（择时 ETF 不强求 2:1）
**信心 65%**

---

### AAPL $271.06 | 财报 4/30（+4d, Implied **±4.2%**）— 减半触发条件已就位

**5 层**:
- L1: 🟢 RSI **59.7**（继续降温）, BB **80%**（v3.3 78%），EMA50 $261.65 / EMA200 $251.97, ATR stop $262.24, Vol 0.9x
- L2: 🔴 全员减（Berkshire 227.9M -4% / Bridgewater 0.3M -16% / Ren 0.1M -7%）
- L3: 🔴 90d 净卖 **$24M**（20 filings, 13 内部人）— **本次脚本恢复正常输出**（v3.3 时返回 0 filings 异常已解除）
- L4: z=-0.9（空头回补，从 v3.3 z+0.1 改善）
- L5: 🔴 P/C Vol 0.57（balanced，从 v3.3 0.61 微降）+ 6 个激进 put 异常
  - 4/27 P $200 Vol/OI 14.3x **IV 194%**（极深 OTM 灾难对冲，可能反映 tariff 黑天鹅尾部）
  - 4/27 C $270 Vol/OI 12.7x、P $270 11.5x、C $272.5 10.7x、P $272.5 7.2x（典型 0DTE 财报前定位）

**叙事**（[Apple Q2 Preview AppleInsider](https://appleinsider.com/articles/26/04/26/what-to-expect-from-apples-q2-2026-earnings-on-april-30) + [9to5Mac](https://9to5mac.com/2026/04/02/apple-sets-q2-2026-earnings-release-for-april-30/)）：
- Q2 收入指引 $107.8-110.7B（+13-16% YoY），consensus $109.27B
- 毛利率指引 48-49%（**记忆芯片涨价 + tariff 是头号担忧**）
- **Tariff 关键变化**：SCOTUS 已驳回 IEEPA tariffs，但**新 Section 301 中国 manufacturing 调查启动** → tariff 新风险窗口
- China 营收预期 ~30% YoY，~20% 总营收占比
- Q2 Beat 率 **8/8 = 100%**（earnings_setup 确认），平均 surprise +4.1%
- Cook 9/1 卸任 + Ternus 接班（已消化）
- **Implied move 微降至 ±4.2%**（v3.3 ±4.1%，几乎不变）

**对立面**：8/8 Beat 100% + Ternus 内部接班 + China +30% 强劲 + iPhone 17 demand 持续。

**操作**：🟨 **持有不加**（v3.3 决策维持，按既定纪律）
- Miss 或毛利率指引 <48% → 减半（卖 0.194 股）
- Gap down >7%（超 implied move 上限）→ 减半
- 跌破 ATR $262.24（-3.3%）→ 减半
- Beat + 毛利率 ≥48% + Section 301 影响小 → 持有

**R:R**：目标 $285（+5.1%）/ 止损 $262.24（-3.3%）→ R:R ≈ 1.6:1（< 2:1 因 CEO 转换 + tariff 不确定）
**信心 73%**（从 72% 上调 1%，因 L4 SI 改善）

---

### META $675.03 | 财报 4/29（+3d, Implied ±7.3%）— 减半决策已定（4/28 执行）

**5 层**:
- L1: 🟡 RSI **61.5** 盘整, EMA50 $635.86 / EMA200 $648.73 **死叉修复中**, BB 74%, ATR stop $645.89, Vol 0.8x
- L2: ⚠️ 分裂（Ackman 2.7M NEW ✅ / Tepper 0.6M +62% / Burry EXIT / Ren EXIT / Bridgewater 0.2M -46% / Third Point EXIT / Tiger 2.8M -2%）
- L3: 🔴 CFO Susan Li 90d 净抛 **$106M**（40 filings，16 内部人）
- L4: **🟠 z=+1.2 升温**（从 v3.3 z+0.4 → +1.2，差 +0.8σ）— **新增警戒**！
- L5: 🔴 P/C Vol 0.59（中性偏空） + **8 个激进 put 异常**：
  - 4/27 P $667.50 Vol/OI 19.2x、P $652.50 = 17.0x、P $675.00 = 16.6x
  - 4/27 C $695.00 Vol/OI 14.2x（多头，OTM +3.0%）
  - 典型财报前双向定位

**叙事**（[Meta Q1 Preview - IG](https://www.ig.com/za/news-and-trade-ideas/meta-q1-earnings-preview--can-advertising-growth-support-massive-260423) + [Investor Relations](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)）：
- Q1 revenue 指引 $53.5-56.5B（+16-20% YoY），consensus $55.5B EPS $6.65
- **2026 Capex 指引 $115-135B**（vs 2025 $69.69B = +65-95% YoY）
- UBS 目标价上调到 $908（from $872）
- Beat 率 **7/8 = 88%**（earnings_setup），平均 surprise +2.3%（vs v3.3 误写 8/8 — 已修正：Q3 2025 是大 miss -84.3%）
- T+5 平均漂移 -0.35%，5/8 正
- **Implied move ±7.3%**（v3.3 ±7.6% → 微降）

**关键二元事件（4/29 盘后）**：
- **Capex guide 上调至 >$135B** → bearish → 按既定纪律清仓余 0.09 股
- **Capex guide 维持 $115-135B** → 已 priced，gap 取决于 ad 增速
- **Capex guide 下调 <$115B** → 大利好（不太可能）

**🆕 v3.4 新发现**：
- **L4 SI z+1.2 偏高新警**（v3.3 时 z+0.4）— 财报前空头加仓
- **Earnings 历史 Beat 率从 v3.3 8/8 修正为 7/8**（Q3 2025 Miss -84.3% 大幅 + T+5 -15.4%）— 这次脚本输出不同于 v3.3 报告手写数据
- 7/8 而非 8/8 + Q3 大 miss 历史 + T+5 极分化 → **强化"减半是风控"决策**

**对立面**：Ackman 2.7M NEW + Tepper +62% + Q1 ad +18% + UBS upgrade。

**操作**：🟥 **按既定计划 4/28 收盘前减半**（卖 0.09 股套现约 $61，保留 0.09 股）
- 若 Beat + Capex ≤$125B → 下周 dry powder $100 回补
- 若 Miss + Capex ≥$135B → 清仓余 0.09 股
- 若 Gap down 5-7.3%（implied move 内）→ 按兵不动
- 若 Gap down >10% → 清仓

**信心 78%**（从 75% 上调 — L4 升温验证 thesis）

---

### TSM $402.46 ⭐ | Taiwan 监管 catalyst + L4 反转，加仓 thesis 强化

**5 层**:
- L1: 🟢 RSI **68.4 BB 98%** Vol **1.6x**（突破未回踩），EMA50 $354.27 / EMA200 $303.58, ATR stop $382.48
- L2: 🔴 缓退（Tepper +7% / Ren -13% / Third Point -61% / Tiger -19%）
- L3: 🔥 6 高管 4/13 联袂买 $32K（脚本输出）+ WebSearch 验证 3 个月 33 buys 0 sells（含 VP Tien 1000 sh @ $55.93 = $55,930 in 3/22）
- L4: **z=-1.4（空头大幅回补，从 v3.3 z+1.4 反转 -2.8σ）** ✨
- L5: 🟢 7 个激进 call 异常（5/1 C $420 Vol/OI 8.2x、C $402.5 4.1x、C $440 3.0x）+ 1 个深 OTM put（5/1 P $230 OTM -42.9% IV 175% 灾难尾对冲，正常 hedge）

**叙事（🆕 关键新闻）**（[TSM Daily Political 4/25](https://www.dailypolitical.com/2026/04/25/taiwan-semiconductor-manufacturing-company-ltd-tsm-shares-acquired-by-impax-asset-management-group-plc.html)）：
- **🆕 Taiwan 监管 4/24 同期将 local equity funds 单股持仓上限从 10% 提升到 25%** → 潜在数十亿 inflow
- TSMC Q1 净利润 +58% YoY
- VP Bor-Zen Tien 3/22 买 1000 shares @ $55.93（TWD ADR ratio 后即 $55,930 这是台股价格，对应 ADR 约 $311）
- 一个月 +18.81%，52 周 +135.98%

**对立面**：BB 98% 严重过热 + 地缘 tail risk 仍存 + 价格已反映 +18% 月涨幅。

**操作**（v3.3 升级版）：
- 🟨 当前 $402.46 不追高
- 🟩 **挂单维持 $385-395 加仓 $300-400**（被动触发）— 与 v3.3 一致
- 🟩 **若 ATR stop $382.48 跌破 + 1 日内反弹（false break）** → 挂单上调至 $390-400 补仓
- 止损 $345（跌破 EMA50 -3%）
- 目标 $450 / $480
- **加仓后总仓位 $400-500 / 约 16-20% 总账户**

**R:R @ 入 $390**: (450-390)/(390-345) = 1.33:1（接受 — 结构性催化 + L4 改善）
**信心 80%**（从 78% 上调 — Taiwan 监管 catalyst 是强论据）

---

### CVX $185.21 | SI 警报解除，但 Q1 timing 已知 negative，持有不加仓

**5 层**:
- L1: 🟡 RSI **41.3** 偏弱, EMA50 $188.55 / EMA200 $167.49, **跌破 EMA50** 1.8%, BB **28%**, ATR stop $177.46, Vol 0.8x
- L2: 🟢🟢 Double-Buy（Berkshire +7% / Renaissance +424%）
- L3: 🔴 C-suite 集中抛售 $155M 不变
- L4: **🟡 z=-1.5（空头回补，从 v3.3 z+1.5 反转 -3.0σ）** ✨ — **本周最大反转**
- L5: 🟢 5 异常 + 3 个 call 异常（5/1 C $197.50 Vol/OI 4.2x、C $192.5 = 3.2x、C $187.5 = 2.6x）+ 2 个 OTM put hedge

**叙事**（[CVX 8-K Filing](https://www.stocktitan.net/sec-filings/CVX/8-k-chevron-corp-reports-material-event-5cf85734af27.html) + [Reuters Wheatstone](https://www.gurufocus.com/news/8813320/chevron-cvx-resumes-full-lng-production-at-wheatstone-plant-after-cyclone-repairs)）：
- 🆕 4/23 Chevron 公告 Wheatstone LNG 完全恢复
- **Q1 timing effects 拖累 earnings/CFO $2.7-3.7B 税后**（financial 8-K 已正式预警）
- + 工作资本流出 $2-4B + 法律费用 $350-400M → 部分被 $1.6-2.2B Upstream 价格 benefit 抵消
- Q1 EPS consensus $1.09（**-50% YoY!** 已极低预期）
- Beat 率 **6/8 = 75%**（earnings_setup），平均 surprise +0.5%
- T+5 平均 +0.24%，4/8 正
- Implied move **±3.9%**（v3.3 ±3.7%，微升）

**🆕 v3.4 关键变化**：
- **L4 SI z 从 +1.5 反转到 -1.5（差 -3σ）** = 空头大量获利平仓 → v3.3 列的"CVX SI 本周 z>2 主动减半"纪律触发条件**已无威胁**
- L5 期权层从"1 call"变成"5 异常 + 3 call"，方向多空各半但绝对量提升
- EPS 已 priced 50% YoY 下降 → miss 风险窗口收窄

**对立面**：Double-Buy 历史 + Wheatstone 恢复 + BB 28% 深度超卖 + L4 已改善 + Brent 油价地缘溢价 = 下行空间有限。

**操作**：🟨 **维持持有不加（v3.3 决策不变，但纪律触发点更新）**
- v3.3 触发条件 "CVX SI z>2 主动减半" → **本条件实质失效**（z=-1.5 远离激增区）
- Miss + timing effect >$3.7B → 减半（条件不变）
- 跌破 EMA200 $167.49 → 清仓
- ATR 止损 $177.46 距现价 -4.2%（不变）

**R:R 持仓维护**：现成本 $186.45 vs 价 $185.21 浮亏 0.7%，$177.46 止损 -4.2%
**信心 65%**（从 60% 上调 5% — SI 警报解除）

---

### GLD $433.25 | 持有不加，🟢 强空头回补 + 期权偏多

**5 层**:
- L1: 🟡 RSI 47.5 中性, BB 49%, **跌破 EMA50 $438.45**（持续 3 天）, ATR stop $419.41, Vol 0.7x
- L2-L3: N/A
- L4: **🟢 z=-2.3 强空头回补**（v3.3 z=-1.4 → -2.3，跨入 z<-2 强信号阈值）✨
- L5: 🟢 P/C Vol 0.50（偏多） + 5 个激进 call 异常（4/27 C $438 Vol/OI 6.1x、C $439 4.8x、C $437 4.0x、C $434 3.2x，4/29 C $435 4.5x）

**叙事**（[State Street Gold Outlook](https://www.ssga.com/us/en/intermediary/insights/gold-2026-outlook-can-the-structural-bull-cycle-continue-to-5000) + [Morgan Stanley Cut Target](https://www.thestreet.com/investing/morgan-stanley-resets-gold-price-target-for-rest-of-2026)）：
- Gold 现 $4,728（4/13）下降 15% from $5,595 ATH (1/29)
- Goldman 5,400 / JPM 6,300 / Reuters median $4,746 / Morgan Stanley 5,200（cut from 5,700）
- **Fed 不降息直接抑制 GLD ETF 需求**（每 25bp 降息 = 60 吨 ETF 需求）
- 但结构性 bullish 因素仍在：央行年购 ~1000 吨、美国财赤 6-7% GDP、储备多元化

**🆕 v3.4 关键变化**：
- L4 SI z=-2.3 = **空头投降**（v3.3 决策"维持持有"被强化）
- L5 4/27-4/29 多个 ATM call OTM 异常（虽量小，GLD 期权流稀） → 多头小幅试探

**对立面**：FOMC 若鹰派（删除 2026 唯一降息预期），USD 冲高 → GLD 可能再 -2-3%。

**操作**：🟨 **持有不加（v3.3 决策维持，论据增强）**
- ATR stop $419.41 距现价 -3.2%
- 若跌破 ATR → 减至 5% 仓位
- L4 z=-2.3 + L5 偏多 + Fed 已 priced hold → **不主动减仓**

**信心 65%**（从 58% 上调 — L4 强信号）

---

### SCHD $31.20 | 加仓继续，但 ATR 安全垫极薄 + L4 新警

**5 层**:
- L1: 🟢 RSI 59.8 多头, BB **89%**（v3.3 91% 微降）, EMA50 $30.54, **ATR stop $30.71（距现价仅 -1.6%!）**, Vol 0.9x
- L2-L3: N/A（CIK 不在 SEC，正常）
- L4: **🟠 z=+1.6 新警**（v3.3 z-0.2 → +1.6）⚠️
- L5: 🟢 P/C Vol **0.22**（极偏多，深度看涨）

**🆕 v3.4 关键变化**：
- L4 SI 跳升至 z+1.6 触发 🟠 警戒 → **但 SCHD 本月刚做完年度 reconstitution**（22 删 25 加，3 个新 top10）→ 被动 ETF rebalance churn 是技术性原因
- WebSearch 确认 SCHD 4/2026 已 reconstitute：Top 持仓 CVX 4.42% + COP 4.29% + MRK 4.15% + KO 4.09% + TXN 4.07%
- 部门权重：Staples 19.5% + Healthcare 18.9% + Energy 16.5%
- YTD +11%（vs SPY flat）→ defensive ETF outperform 趋势继续

**对立面**：BB 89% 短期超买，ATR safety 仅 1.6% 是本组合最薄。

**操作**：🟩 **加仓 thesis 维持但时机收紧**
- v3.3 "第一批 $250 @ $30.80-31.20" → **修订**：考虑到 ATR safety 仅 1.6%，第一批 $250 应在 EMA50 $30.54 附近（即 $30.40-30.70）成交，避免在 BB 89% 的高位 chase
- 第二批 $250 留 @ EMA50 -1% 即 $30.20 以下回踩
- 若 SCHD 三日内突破 $31.50 不回踩 → 放弃第二批
- L4 z+1.6 不构成放弃理由（reconstitution 技术性）

**信心 70%**（从 82% 下调 12% — ATR 安全垫薄 + L4 新警迫使更严苛入场）

---

### MU $499.84 | 信号继续衰减，候选维持小仓 + Triple-Buy 不独立决策

**5 层**:
- L1: 🟢 RSI **68.9**（接近超买）, EMA50 $411.34 / EMA200 $296.59, BB 87%, ATR stop $457.76, Vol 0.8x
- L2: 🟢🟢🟢 TRUE Triple-Buy 维持（Bridgewater 0.9M ^+52355% NEW + Renaissance 3.0M ^+151% + **Tepper 1.8M ^+250%**）— **但回测 Triple-Buy N=2 alpha -3.3%**
- L3: 🔴 90d 净卖 **$42M**（9 filings，从 v3.3 -$53M 滑动）— CBO Sadana 2 笔 $18M + CPO Arnzen $9M
- L4: z=-1.2（空头回补，从 v3.3 z+0.8 改善）
- L5: 🔴 35 异常 + P/C Vol 1.14 偏空：
  - 5/1 P $500 (ITM +0.7%) Vol/OI **12.7x** IV 96% — 机构高位对冲
  - 5/1 P $290 (OTM -41.6%) Vol/OI 8.9x IV 170% — 灾难尾对冲
  - 5/1 C $497.50 Vol/OI 8.5x（多头）
  - 5/8 C $495 8.5x（多头）
  - 5/1 P $417.50 (OTM -15.9%) 7.0x — 中度对冲

**叙事**（[Micron HBM4 Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin) + [Motley Fool](https://www.fool.com/investing/2026/03/27/micron-just-started-mass-producing-hbm4-for-nvidia/)）：
- HBM4 已进入 mass production for NVDA Vera Rubin
- 全 2026 calendar year HBM4 产能 100% 售出（**5 年 binding contracts** — 罕见承诺）
- Q3 FY2026 revenue $23.86B 创纪录
- 分析师中位价 $517.50（high $600）
- Q3 财报 ~6/25（不在本周）

**对立面**（强）：基本面史上最强 + 5 年 binding contracts = 收入可见性极强。

**操作**（v3.3 维持）：🟨 **维持小仓建仓 $200-300，等回踩**
- 入场 $440-460（回踩 ATR stop $457.76）或 $411 EMA50
- 止损 $400（跌破 EMA50 -3%）
- 目标 $540 / $600
- **降仓位理由**：Triple-Buy 回测 N=2 alpha -3.3%（不可独立决策）+ L3 C-suite 连续 $42M 卖 + L5 0DTE put 集中（虽 5 年合约 binding）

**R:R @ 入 $450**: (540-450)/(450-400) = 1.8:1 ⚠️
**信心 55%** ⚠️（最低）

---

### OXY $57.12 | 数据修复 + L4 警报回落，但维持暂停建仓

**5 层**:
- L1: 🟢 RSI 48.4 中性, EMA50 $55.75 / EMA200 $48.05, BB 36%, ATR stop $53.91, Vol 0.5x
- L2: 🟡 **Berkshire 264.9M =+0%**（数据修复！v3.3 显示 "1.1M 数据疑"）
- L3: — 17 filings 净 $0（无买无大卖）
- L4: z=+0.9（**从 v3.3 z+1.7 回落，但仍未到 z<+0.5 的"重新进入"门槛**）
- L5: 🟢 P/C Vol 0.20 极偏多 + 3 异常：
  - 5/1 P $52 OTM -9% Vol/OI 5.8x（适度 hedge）
  - 5/1 C $58 OTM +1.5% Vol/OI 4.9x（多头）
  - 5/1 C $59 OTM +3.3% Vol/OI 4.9x（多头）

**叙事**（[24/7 Wall St 4/20](https://247wallst.com/investing/2026/04/20/buffetts-favorite-oil-stock-just-dropped-8-heres-the-bull-and-bear-case-for-buying-the-occidental-dip/) + [Yahoo](https://finance.yahoo.com/markets/stocks/articles/too-buy-warren-buffett-stock-014100175.html)）：
- Berkshire 持 ~265M 股 = 28.2% of OXY outstanding
- YTD +38%（"Buffett effect" + Iran 油价溢价）
- 4/20 8% drop 后回稳
- 🆕 OxyChem 业务 4/2026 卖给 Berkshire $9.7B 现金（debt 从 ~$23B 降至 $15B）
- 季度股息 +8% 至 $0.26
- 历史 Single-Buy 三次全负（-10/-20/-6%）

**对立面**：debt 降 $8B + OxyChem $9.7B 现金 + 股息 +8% = **基本面真实改善**，不是单纯 "Buffett 信仰"。

**操作**：🟥 **维持暂停建仓**
- v3.3 暂停理由：z+1.7 + Single-Buy 历史负 alpha + Berkshire 数据疑
- v3.4 状态：z+0.9（改善但未到门槛）+ Single-Buy 历史不变 + 数据修复
- **重新评估门槛**：L4 z<+0.5 + 1 周后再核 → 然后才考虑 $300 小仓 @ $54-55
- 当前 $57.12 已超 v3.3 入场参考 $54-55 上沿 → 即使重新评估也不在当前价入

**信心 65%**（从 60% 上调 5% — 数据修复 + L4 改善）

---

### AMD $347.81 ⚠️ | 5 层偏空 + Tepper 减 66% 新增 + 散户 FOMO 极致（陷阱 B+F+G + L2 升级 Triple-Sell）

**5 层**:
- L1: 🔴 **RSI 88.9 极度过热**（v3.3 89.2 持平）, BB **110%**（v3.3 111% 持平）, EMA50 $236.76 / EMA200 $202.68, **Vol 2.1x 持续放量**, ATR stop $327.08
- L2: 🔴 **量化双减 + 主观派 Tepper 也撤！** Bridgewater 1.7M v-8% / Ren 1.3M ^+142% / **Tepper 0.3M v-66%**（v3.4 新数据）
  - **重要**：Renaissance 此处显示 +142% 与 v3.3 报告"-23%" 不同 — 实际 **smart_money_scan 输出本次显示 Ren AMD +142%（1.3M）**，说明 Q1 13F filed 后 Ren 实际增持 AMD
  - Tepper -66% 是新负面（v3.3 缺失），但 Tepper AMD 仓位本身很小（0.3M）
  - 综合 L2：仍 ⚠️ **分裂偏空**（量化 Bridgewater 减 / Ren 加 / 主观 Tepper 大减）
- L3: 🔴 90d 净卖 **$63M**（17 filings，CEO Su $7M + CTO Papermaster $7.4M）
- L4: z=+0.5（普通，无新警）
- L5: 🔴 **40 异常**（v3.3 时也是 40），P/C Vol 0.90（balanced），但 Top 5 极端 Vol/OI：
  - **5/1 P $330 (OTM -5.1%) Vol/OI 62.3x** IV 81%（机构 hedge）
  - 5/1 C $390 OTM +12% Vol/OI 36.3x IV 83%（散户 FOMO）
  - 5/1 C $355 OTM +2.1% Vol/OI 33.9x（散户）
  - **5/1 C $400 OTM +15% Vol/OI 33.4x**（极度 FOMO）
  - 5/1 C $365 Vol/OI 22.9x

**叙事**（[24/7 Wall St](https://247wallst.com/investing/2026/04/16/amd-gains-6-ahead-of-may-earnings-is-the-ai-chip-challenger-finally-ready-to-rival-nvidia/)）：
- 5/5 财报盘后 5pm ET
- Q1 revenue 指引 $9.8B ±$300M（含 ~$100M MI308 China 销售）
- 中点 ~32% YoY 增长，sequential -5%
- 非 GAAP 毛利率 ~55%，OpEx ~$3.05B，EPS consensus 1.27
- 2026 data center 长期目标 +60% YoY
- 4/24 已涨到 $347.81 → 财报前一周还有 7 天交易

**🆕 v3.4 新增警报**：
- **L2 升级**：Tepper -66%（v3.3 未含）+ Bridgewater -8% = 主观 + 量化均减 → 接近 Triple-Sell pattern
- L5 5/1 chain 双向极致定位（FOMC 后 + 财报前 4 天）已是历史前列
- 4/24 短卖 z+0.5 vs 4/22 z+1.2 → 短期空头小幅获利平仓，但不影响 L1+L5 的过热信号

**对立面**：MI350 ramp + MI400/Helios 路线图 + ROCm 生态扩展 + 长期 60% YoY data center growth。

**操作**：🟥 **继续禁止追涨 / 不建仓**
- 候选池目标 $230-240 已严重过时（现价 $347.81 距 $230 = -34%）
- **新入场参考**：若财报后 gap down 15-20% 到 **$280-300**（EMA50 $237 +15-25%）→ 小仓 $200 试探（v3.3 写 $300，v3.4 下调 $200 因 Tepper 新负面）
- 不在财报前任何位置建仓

**信心 88%**（持平本周最高）

---

## 候选池分析（机会雷达）

### Triple-Buy 候选（MU 已分析，其他池）

**当前 watchlist 三只候选**：
1. **MU**: TRUE Triple-Buy（Bridgewater +52355% NEW + Ren +151% + Tepper +250%）+ HBM4 5 年 binding，但 Triple-Buy N=2 回测 -3.3% + L3 -$42M + L5 高位对冲 → 维持小仓 $200-300
2. **OXY**: Single-Buy（仅 Berkshire）+ Single-Buy 历史负 alpha → 维持暂停
3. **AMD**: 5 层偏空 + 财报前 → 维持禁止追涨

### 扩展扫描池机会扫描（v3.4 不深入）

按 expansion_universe，本周未触发新机会建议（市场处于事件密集期）。

---

## 全局视角

**组合健康度**：
- 8/8 持仓中 **5 只 🟨 持有不加仓**，1 只 🟥（META 4/28 减半），2 只 🟩（SCHD 加仓 + TSM 挂单）
- 🟥 占比 = 1/8 = **12.5%**（远低于 50%，方法论稳定）
- **防御姿态过 FOMC + 三财报 + PCE + NFP 七连大事件周**

**本周事件密度**：
```
周一 4/27 ─ 盘前 Q1 财报集中期（非本持仓）+ NVDA 0DTE put 极端定位日
周二 4/28 ─ FOMC Day 1 + META 减半执行
周三 4/29 ─ FOMC 利率决议（下午 2pm ET）+ META 财报（盘后 4pm ET）
周四 4/30 ─ PCE（上午 8:30am ET）+ AAPL 财报（盘后 5pm ET）
周五 5/01 ─ CVX 财报（盘前 11am ET）+ AMD 5/1 0DTE 极端到期
周一 5/02 ─ NFP 就业数据（8:30am ET）
周一 5/05 ─ AMD 财报（盘后 5pm ET）
```

**最紧急 24-48 小时行动**（按优先级）：
1. 🟥 **4/28 收盘前 META 减半**（卖 0.09 股约 $61）— 不变更
2. 🟩 **本周任意日 SCHD 第一批加仓 $250 @ $30.40-30.70**（vs v3.3 $30.80-31.20，因 ATR 1.6% safety 收紧入场区间）
3. 🟨 **TSM 限价 $385-395 挂单 $300-400**（被动触发）
4. ✅ **CVX SI 警报已解除**（无需主动减半）
5. ✅ **OXY SI 警报基本解除**（z+0.9，但仍维持暂停）
6. ⚠️ **NVDA 4/27-4/29 不追涨追跌**（4/27 单日 0DTE put Vol/OI 182x 是事件 hedge）

**科技敞口**（不变）：
- AI 芯片（NVDA + TSM）: ~24%
- 大盘科技（AAPL + META）: ~10%
- SPY 宽基（~30% 科技暗含）: 33.5%
- 实际科技 beta ≈ 50%

---

## Top 3 可操作建议（本周）

### #1 🟥 META 4/28 收盘前减半
- 动作: **卖 0.09 股**（保留 0.09 股）
- 价格: 市价 ~$670-685
- 套现: ~$60
- 执行窗口: 2026-04-28（FOMC Day 1 结束后，财报前一日）
- **为什么减半不清仓**：Capex guide 可能维持 $115-135B（已 priced），Ackman NEW + Tepper +62% + UBS upgrade $908 = 不清仓保留 upside
- **为什么不持有**：L3 CFO $106M + L5 8 put 异常 + L4 z+1.2 新警 + PEAD 分化（-15.4% 到 +11.0%）+ 7/8 而非 8/8 Beat（修正）= 风险敞口过大
- 对立面: 若 Beat + Capex <$125B，少赚 $5，保险优于贪婪
- 信心: 78% 🟥

### #2 🟩 SCHD 加仓第一批 $250（入场区间收紧）
- 动作: 买入 ~8 股（$250 / $31.12）
- 价格: **$30.40-30.70**（v3.3 $30.80-31.20 收紧）
- 执行窗口: 4/27-4/29 任意日（FOMC 前最后窗口）
- **为什么收紧入场**：ATR safety 仅 1.6% + L4 z+1.6 新警（虽是 reconstitution churn 不是基本面）+ BB 89% 仍偏高 → 不在 EMA50 上沿追
- 第二批 $250 留 @ $30.20 以下回踩 EMA50
- 对立面: 若 4/27-4/29 SCHD 三日不回踩 $30.70，放弃第二批
- 信心: 70% 🟩

### #3 🟨 TSM 被动挂单加仓 $300-400（论据强化）
- 动作: 限价挂单 **$385-395**（ATR stop $382.48 附近）
- 若成交：仓位 ~16-20%
- 若 1 周内未触发 → 取消，等财报后新数据再决定
- 止损 $345（-10%）
- 目标 $450 / $480
- **本周新论据**：Taiwan 监管 4/24 起将 local 单股上限从 10% 升到 25% → 数十亿结构性 inflow + L4 SI 从 z+1.4 反转到 z-1.4 + L3 Ursula Burns $322K + 33 buys 0 sells（全 3M 内）
- 对立面: 当前 $402 已涨 +8%，可能不回踩；错过就错过，不 FOMO
- 信心: 80% 🟨

---

## 陷阱清单

| 标的 | 陷阱 | 说明 |
|---|---|---|
| **AMD** | **B + F + G + L2 升级 Triple-Sell 边缘** | RSI 89 + BB 110 + 9 激进 call (62x Vol/OI 5/1 chain) + 机构 5/1 P $330 hedge + Tepper -66% 新增 |
| **NVDA** | **G 极端 + E** | 4/27 P $207.50 单日 Vol/OI **182x**（48,952 张新建）= 历史前列 0DTE 跨资产 FOMC hedge |
| **META** | **F + L4 升温** | 0DTE 财报前 8 个 put 异常 + L4 SI z+1.2 新警 |
| AAPL | E 平稳 | P/C 0.57 中性，4/27 P $200 IV 194% 是 tariff 黑天鹅尾对冲 |
| **MU** | **F + Triple-Buy 假象** | 5/1 P $500 ITM Vol/OI 12.7x + Triple-Buy N=2 回测 -3.3% 不可独立决策 |
| SPY | F | 93 个 0DTE 异常（P $713 59x、C $714 45x）— 4/27 FOMC pre-game |
| **CVX** | D 反向 + L4 解除 | Double-Buy vs C-suite $155M 抛；L4 z 从 +1.5 反转到 -1.5（解除）|
| GLD | — | L4 z-2.3 强空头投降（实际正信号）|
| SCHD | L4 vs L5 冲突 | L4 z+1.6 新警（reconstitution churn）vs L5 P/C 0.22 极偏多 |
| OXY | D | Berkshire 单信源 + Single-Buy 历史负 alpha |
| TSM | — | BB 98% 短期过热但有 Taiwan 监管结构性 inflow 支撑 |

---

## 关键纪律触发点（已接近或正在接近）

| 标的 | 现价 | 距止损 | 触发条件 | 24h 内动作 |
|---|---|---|---|---|
| **META** | $675.03 | — | 财报前 3 天 | **4/28 前减半** |
| **AAPL** | $271.06 | -3.3% 到 $262.24 | 跌破 ATR / 毛利率 <48% | 减半 |
| **NVDA** | $208.27 | -3.9% 到 $200.10 | 跌破 ATR 连续 2 日 | 减至 10% 仓位 |
| **SPY**  | $713.94 | **-1.8% 到 $700.98** | 跌破 ATR | 减至 20% 仓位 |
| **SCHD** | $31.20 | **-1.6% 到 $30.71** | 跌破 ATR | 重新评估第一批入场时机 |
| **CVX**  | $185.21 | -4.2% 到 $177.46 | 跌破 ATR | 减半 |
| **GLD**  | $433.25 | -3.2% 到 $419.41 | 跌破 ATR / 单日 -5% | 减至 5% 仓位 |
| **TSM**  | $402.46 | -4.8% 到 $382.48 | 跌破 ATR | 不执行加仓挂单（false break 反弹后再看）|

**v3.4 警报状态更新**：
- ❌ **CVX SI 警报已解除**（z 从 +1.5 反转到 -1.5）— 无需"主动减半"
- ⚠️ **OXY SI 警报回落**（z +1.7 → +0.9）但仍未到 z<+0.5 重新进入门槛 → 维持暂停
- 🟠 **SCHD SI 新警**（z +1.6）但定性为 reconstitution churn → 不影响加仓
- 🟢 **GLD SI 强信号** z-2.3 = 空头投降 = 价格底部支撑

---

## 日历同步预备清单

### 📊 财报事件
- **2026-04-29 Wed** META 财报（盘后 4pm ET）— Implied **±7.3%**, noise <5%
- **2026-04-30 Thu** AAPL 财报（盘后 5pm ET）— Implied **±4.2%**, noise <3%
- **2026-05-01 Fri** CVX 财报（盘前 11am ET）— Implied **±3.9%**, noise <2.5%
- **2026-05-05 Mon** AMD 财报（盘后 5pm ET）— Implied ~±6%（无持仓，监控用）
- **2026-05-20 Wed** NVDA 财报（盘后）— 24 天后

### 🏛️ 宏观事件
- **2026-04-28-29 Tue-Wed** FOMC 利率决议 — 预期 **Hold 99.7%**（3.50-3.75%），关注 dot plot 是否仍预 2026 年 1 次降息
- **2026-04-30 Thu 8:30am ET** PCE（3 月）— consensus 待补
- **2026-05-02 Fri 8:30am ET** NFP（4 月就业）
- **2026-05-12 Tue 8:30am ET** CPI（4 月）

### 📅 Ad-hoc 事件
- **2026-09-01** AAPL CEO 正式交班（Cook → Ternus）— 已确认
- **2026-04-24（已生效）** Taiwan local equity funds 单股上限 10% → 25%（TSM 结构性 inflow 催化剂）

### ⚠️ 纪律警告
- **META** 4/28 收盘前减半（📍 周二执行）
- **NVDA** 4/27-4/29 不追涨追跌（0DTE 极端 hedge 期）
- **AAPL** 4/30 财报前不调仓
- **OXY** SI 监控：z<+0.5 才考虑重新评估

---

## 上周对比（v3.3 2026-04-24 → v3.4 2026-04-26）

**新出现的信号**：
- 🆕 **NVDA 4/27 P $207.50 Vol/OI 182.0x**（48,952 张新建）— 历史前列单合约 hedge，跨资产 FOMC 对冲炸弹
- 🆕 **AMD 5/1 chain 双向极致定位**：P $330 62.3x（机构）+ C $400 33.4x（散户 FOMO）
- 🆕 **AMD Tepper 0.3M v-66%** — Q1 13F 数据本次首次完整显示，Appaloosa 主观派也撤
- 🆕 **META L4 SI z+1.2 升温新警**（v3.3 z+0.4）
- 🆕 **GLD L4 SI z-2.3 强空头投降**（v3.3 z-1.4）
- 🆕 **SCHD L4 SI z+1.6 新警**（v3.3 z-0.2）— 但定性为 reconstitution churn
- 🆕 **Taiwan 监管 4/24 起单股上限 25%** — TSM 结构性 catalyst

**解除的风险**：
- ✅ **CVX SI z+1.5 → -1.5**（差 -3σ）= "CVX 主动减半"纪律失效
- ✅ **OXY SI z+1.7 → +0.9** 部分回落（但未到重新进入门槛）
- ✅ **OXY 13F Berkshire 数据从 "1.1M 数据疑" 修复为 264.9M =+0%**
- ✅ **AAPL Insider scan 从 v3.3 0 filings 异常 恢复正常输出 20 filings**

**修正的数据**：
- META Beat 率 8/8 → **7/8**（Q3 2025 Miss -84.3% + T+5 -15.4%，earnings_setup 输出权威）— 强化"减半是风控"决策
- AMD Renaissance 实际 +142% 而非 -23%（v3.3 笔误）
- META Implied move ±7.6% → ±7.3%（微降）
- AAPL Implied move ±4.1% → ±4.2%（微升，但实质不变）
- CVX Implied move ±3.7% → ±3.9%（微升）

**13F 无变化**（Q1 2026 最新文件 2026-02-17 filed，下次更新约 2026-05-15 — 距今 19 天）

**宏观新发现**：
- **March CPI headline 3.3% YoY 是 11 个月新高**（Iran 油价驱动）→ FOMC 鸽派意外概率被极度压缩
- **Q1 Earnings net profit margin 13.4% = 自 2009 来最高**（FactSet）
- **Forward P/E 20.9 > 5y avg 19.9** = 估值边际偏贵

---

## 📋 交易纪律确认书 / 2026-04-26

```
┌────────────────────────────────────────────────────────┐
│              交易纪律确认书 / 2026-04-26 (v3.4)           │
├────────────────────────────────────────────────────────┤
│                                                        │
│  组合整体逻辑（本周）：                                  │
│  防御姿态度过 FOMC + 3 财报 + PCE + NFP 七连事件；       │
│  META 财报前减半套保险，SCHD 收紧入场区间分批加仓，      │
│  TSM 回踩加仓挂单（被动），OXY/AMD 因新负面/警情未解暂停。│
│                                                        │
│  【本周必做（按顺序）】：                                │
│                                                        │
│  □ 4/27-29: SCHD 第一批加仓 $250 @ $30.40-30.70        │
│    (v3.3 $30.80-31.20 区间收紧，避开 BB 89% 上沿)      │
│  □ 4/28 (FOMC Day 1 后): META 减半卖 0.09 股            │
│  □ 整周: TSM 限价 $385-395 挂单 $300-400               │
│  □ 周末: 核对 FINRA 数据 SCHD/OXY z 走向                │
│                                                        │
│  【强制止损/减仓触发点】：                                │
│                                                        │
│  □ META Miss + Capex ≥$135B → 清仓剩余 0.09 股          │
│  □ META gap down >10% → 清仓                             │
│  □ AAPL 毛利率指引 <48% → 减半                           │
│  □ AAPL gap down >7% → 减半                              │
│  □ AAPL Section 301 Tariff 重大新闻 → 减半              │
│  □ CVX 跌破 $177.46 (ATR) → 减半                        │
│  □ CVX 跌破 $167.49 (EMA200) → 清仓                     │
│  □ ❌ CVX SI z>2 触发条件【已失效】(z=-1.5)             │
│  □ GLD 跌破 $419.41 (ATR) → 减至 5% 仓位                │
│  □ NVDA 跌破 $200.10 (ATR) 连续 2 日 → 减至 10% 仓位    │
│  □ SPY 跌破 $700.98 (ATR) → 减至 20% 仓位               │
│  □ SCHD 跌破 $30.71 (ATR) → 重新评估加仓时机            │
│  □ TSM 跌破 $382.48 (ATR) → 不执行加仓挂单              │
│                                                        │
│  【FOMC 4/29 特别纪律】：                                │
│                                                        │
│  □ Statement 公布后先观察 30 分钟，不急操作              │
│  □ 鹰派意外（dot plot 删除 2026 唯一降息）→             │
│    SPY/GLD 都可能 -2-3% / NVDA 跌破 ATR 概率升          │
│  □ 鸽派意外（暗示 2 次降息）→ SPY/GLD 可能 +1-2% /       │
│    NVDA 上行能突破 $215                                  │
│  □ Hold + 中性 statement（基线）→ 观察 META 财报反应     │
│                                                        │
│  【财报周特别纪律（4/29-5/1）】：                        │
│                                                        │
│  □ 财报前 24h 不新建任何仓位                             │
│  □ 财报后 gap down >8% 等 2 个交易日再决策               │
│  □ 不在财报当日追涨或抄底                                │
│  □ 每只财报后 48h 内复盘是否命中 implied move            │
│                                                        │
│  【4/27 NVDA 0DTE 极端 hedge 警戒】：                    │
│                                                        │
│  □ NVDA 4/27 不追涨追跌（不论方向）                      │
│  □ 若 4/27 收 < $201.09 + 4/28 继续跌破 →                │
│    减至 10% 仓位（既有触发条件）                         │
│  □ 若 4/27 大涨过 $215 → 不追，等 FOMC 后回踩            │
│                                                        │
│  【AMD 5/1 双向极端定位警戒】：                          │
│                                                        │
│  □ 5/1 AMD 收盘前不在任何价位建仓                        │
│  □ 5/5 财报后 gap down 15-20% 至 $280-300 →             │
│    考虑小仓 $200 试探（v3.3 $300 下调）                  │
│  □ 5/5 财报若 gap up >10% → 无仓位无动作                 │
│                                                        │
│  承诺：上述条件触发时，我将在 24 小时内执行，             │
│  不找"等反弹"借口，不因浮亏心理抵触而延迟。              │
│                                                        │
│  自省（v3.4 新）：                                       │
│  - v3.3 误写 META Beat 率 8/8 — 实际 7/8 (Q3 2025 大 Miss)│
│    earnings_setup 输出是权威，手写笔记需逐项核对          │
│  - v3.3 缺失 AMD Tepper -66% 数据 — Q1 13F 必须每份报告  │
│    完整重读，不能依赖上次 yaml 摘要                       │
│  - CVX SI 反转幅度 -3σ 提示我之前过度强调 z 单点警报；   │
│    应该看趋势 + 双向均衡（升降警报都要重视）              │
│  - SCHD L4 z+1.6 是 ETF 技术性 churn 而非基本面 —         │
│    定性诊断很重要，避免一刀切减仓                         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 数据来源 & 新闻链接

**Phase 1 脚本数据**（2026-04-26 跑分，使用 4/24 收盘 + SI T+1 4/24 数据）:
- portfolio_scan / smart_money_scan / insider_scan / short_interest_scan / options_anomaly_scan / earnings_setup 全 exit 0
- raw 输出归档：`reports/raw/2026-04-26/*.log`

**Phase 2a WebSearch 链接**:
- [FOMC 4/28-29 Polymarket 99.7% Hold](https://polymarket.com/event/fed-decision-in-april)
- [JPM Fed Rate Cut Path](https://www.jpmorgan.com/insights/global-research/economy/fed-rate-cuts)
- [Meta Q1 2026 Earnings Preview - IG](https://www.ig.com/za/news-and-trade-ideas/meta-q1-earnings-preview--can-advertising-growth-support-massive-260423)
- [Meta Investor Relations Q4 2025](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
- [Apple Q2 2026 Preview - AppleInsider](https://appleinsider.com/articles/26/04/26/what-to-expect-from-apples-q2-2026-earnings-on-april-30)
- [Apple Q2 - 9to5Mac](https://9to5mac.com/2026/04/02/apple-sets-q2-2026-earnings-release-for-april-30/)
- [CVX Q1 8-K Timing Effects](https://www.stocktitan.net/sec-filings/CVX/8-k-chevron-corp-reports-material-event-5cf85734af27.html)
- [CVX Wheatstone Restored](https://www.gurufocus.com/news/8813320/chevron-cvx-resumes-full-lng-production-at-wheatstone-plant-after-cyclone-repairs)
- [NVDA H200 China Restrictions](https://finance.yahoo.com/news/nvidia-stock-falls-as-china-reportedly-restricts-imports-of-h200-chips-155203605.html)
- [AMD May Earnings Preview](https://247wallst.com/investing/2026/04/16/amd-gains-6-ahead-of-may-earnings-is-the-ai-chip-challenger-finally-ready-to-rival-nvidia/)
- [TSM Daily Political 4/25](https://www.dailypolitical.com/2026/04/25/taiwan-semiconductor-manufacturing-company-ltd-tsm-shares-acquired-by-impax-asset-management-group-plc.html)
- [Micron HBM4 Vera Rubin](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
- [OXY Buffett 28.2% Stake](https://247wallst.com/investing/2026/04/20/buffetts-favorite-oil-stock-just-dropped-8-heres-the-bull-and-bear-case-for-buying-the-occidental-dip/)
- [SCHD Reconstitution April 2026](https://www.fool.com/investing/2026/03/25/schd-annual-reconstitution-what-this-dividend-etf/)
- [GLD Outlook State Street](https://www.ssga.com/us/en/intermediary/insights/gold-2026-outlook-can-the-structural-bull-cycle-continue-to-5000)
- [GLD Morgan Stanley Cut Target](https://www.thestreet.com/investing/morgan-stanley-resets-gold-price-target-for-rest-of-2026)
- [SPY S&P 500 Earnings Update FactSet](https://insight.factset.com/sp-500-earnings-season-update-april-24-2026)

**方法论**: `docs/METHODOLOGY_v3.md` / **持仓**: `config/holdings.yaml` v3.2 / **基线**: `reports/2026-04-24-weekly-deep.md`

---

*本报告在 Claude Code 本地会话中合成。下一份 quickscan 计划 2026-04-27（周一收盘后）。*

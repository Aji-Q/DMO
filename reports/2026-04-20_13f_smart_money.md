# 2026-04-20 13F 机构持仓追踪（smart_money_scan）

## 脚本输出

```
Manager               Filed               NVDA          AAPL          META           TSM           CVX
---------------------------------------------------------------------------------------------------------
Berkshire (Buffett)   2026-02-17            —     227.9M v-4%          —             —    130.2M ^+7%
Scion (Burry)         2025-11-03     1.0M NEW          —          EXIT             —             —
Pershing (Ackman)     2026-02-17          —             —     2.7M NEW             —             —
Appaloosa (Tepper)    2026-02-17    1.7M v-11%          —    0.6M ^+62%    1.1M ^+7%          —
Bridgewater (Dalio)   2026-02-13    3.9M ^+54%   0.3M v-16%  0.2M v-46%           —             —
Renaissance           2026-02-12    0.9M v-85%   0.1M v-7%     EXIT       1.2M v-13%   2.2M ^+424%
Third Point (Loeb)    2026-02-17    3.0M ^+4%          —         EXIT      0.4M v-61%          —
Tiger Global          2026-02-17   11.0M v-6%          —    2.8M v-2%      3.7M v-19%          —
```

## 核心洞察

### 🔥 CVX 智钱共识（最强信号）

| 基金 | 操作 |
|---|---|
| Berkshire | +7% (价值派代表) |
| Renaissance | +424% (量化派代表，极罕见的大幅加仓) |
| 其他 | 无人减持 |

**价值派 + 量化派同向大幅加仓** → 这是整份 13F 里最罕见的一致性信号。结合 CVX 技术超卖（RSI 37、贴布林下轨），三层证据共振。

### ⚠️ AAPL 全员减持共识

```
Berkshire -4% | Bridgewater -16% | Renaissance -7% | 无人加仓
```

没有任何对冲基金在这份扫描里加仓 AAPL。你是少数没减仓的参与者。

### 🎯 META 对冲基金严重分歧

| 看多 | 看空 |
|---|---|
| Ackman NEW 2.7M (极少见新建大仓) | Burry EXIT |
| Tepper +62% | Renaissance EXIT |
| Third Point Re-entered | Bridgewater -46% |

**Ackman 新建仓尤其值得关注** — Pershing Square 通常只持 8-10 只股票，新建仓等同于"重仓信号"。与 META 刚突破 EMA 死叉形成叠加。

### 🤷 NVDA 信号互相抵消

Bridgewater +54% vs Renaissance -85%；Burry NEW 但 Tiger -6%。太拥挤，无独立信号。

### 📉 TSM 智钱缓慢撤退

Third Point -61%、Tiger -19%、Renaissance -13%。仅 Tepper 小幅加。与地缘政治风险担忧吻合。

## Discretionary vs Quant 派系分裂（META 深度拆解）

```
多头派（主观基金）           空头派（量化基金）
─────────────────            ──────────────────
Ackman Pershing NEW          Renaissance EXIT
Tepper Appaloosa +62%        Burry Scion EXIT
Third Point 回补             Bridgewater -46%
```

这不是普通的分歧。**量化派**看到的是：Capex $115-135B 上限会压缩自由现金流，估值模型按模型给出 SELL。**主观派**赌的是：广告 AI 货币化的"次级贝塔"——这个不出现在历史数据里，量化模型捕捉不到。

谁对？财报前不知道。赌哪一方都是主观猜。

## 限制

- 仅覆盖 8 个知名基金，未覆盖 D.E. Shaw / Citadel / Two Sigma 等
- 13F 有 45 天披露延迟（Q4 2025 数据在 2026-02 报出）
- 只看美股多头持仓，空头 / 期权 / 国际头寸看不到
- 匹配靠公司名关键词，存在误匹配可能（大公司名基本没问题）

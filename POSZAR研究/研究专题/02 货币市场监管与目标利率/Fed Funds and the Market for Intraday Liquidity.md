---
tags:
  - Pozsar
  - 货币市场
  - 日内流动性
日期: 2018-10
---

# Fed Funds and the Market for Intraday Liquidity（GMN#18，联邦基金与日内流动性市场）

> [!quote] 原文链接
> [[Fed Funds and the Market for Intraday Liquidity.pdf]]

## 摘要

GMN#18，Pozsar 发现（并命名）了一个市场眼皮底下的"影子市场"——**IBDA（interest-bearing deposit accounts，生息存款账户）**：美国 G-SIB 向 FHLB 借入**全天锁定的准备金**以满足处置流动性（resolution liquidity）的日内需求，成交价约 **IOR+8~10bp——远在目标区间之上**。当所有人盯着隔夜监测屏说"除了 GCF 都还在区间内、kind of 没事"时，**边际上真正的银行融资市场已经在区间外交易了**。结论：EFFR 年内出区间、波动率上升，是"清晰而现实的危险"（clear and present danger）——两个月后年底回购/FF 剧震兑现。

## 核心论点详解

### 1. 大行司库们的三个关键词

与美国 G-SIB 司库的交流中反复出现：

1. **处置流动性成为新的硬约束**——LCR 看日末快照，resolution liquidity 还要看**日内**流动性需求，直接抬高 HQLA（更准确地说是**准备金**）的需求量，因为**准备金是唯一能在日内任何时点提供流动性的 HQLA**；
2. 银行开始紧盯日内流动性、优化支付流；
3. 一句神秘的话："**flows are changing**"（流变了）。

### 2. IBDA：为什么它比 o/n FF 对双方都好

- **对 FHLB**：FF 交易清晨 5:30–6:00 就要回款，钱在美联储零息账户里躺几小时、中午前再借回去——**每天有数小时零收益**。IBDA 钱全天留在 G-SIB 账上、全天候生息，需要时仍能早上取。
- **对 G-SIB**：FF 的清晨回款 = 每天有几小时准备金账户被掏空 = **日内流动性敞口上升**；而 resolution liquidity 考核的是**累计峰值日内敞口**——"每分钟账户余额偏低都算数"。IBDA 全天锁定准备金，直接降低日内敞口。
- 于是形成了一个 FHLB 出借、G-SIB 借入的全新银行间市场：2018 年 8 月日均量已达 **150 亿**（对比 FF 市场约 500 亿），价格 **IOR+8~10bp**。
- 隐忧（Pozsar 自己加的脚注）：**危机时 FHLB 恰恰会抽走 IBDA**，正是 G-SIB 最需要的时候——"值得所有人深思：G-SIB、美联储、FHLB 及其监管者 FHFA"。

### 3. FF 市场进化的三个里程碑——"准备金还超额吗"的试金石

| 阶段 | 借方 | 动机 |
|---|---|---|
| 1 | 外国银行 | 套利 IOR（季内无 SLR 约束） |
| 2 | 超级区域行/区域行 | 月末补充**日末** LCR |
| 3 | G-SIB | 补充**日内**处置流动性（更高阶的 LCR） |

"从套利（玩转超额流动性），到补日末流动性，到补日内流动性……这是一个清晰的路径，也是思考'准备金是否仍然超额'的好方法。"

### 4. "流变了"的机制

- 财政部充实 TGA + 美联储缩表 → 银行体系失去准备金（唯一有日内流动性的 HQLA）、得到国债（没有日内流动性）；
- 银行于是通过融资市场**把失去的日内流动性买回来**——这就是 IBDA 需求之源；
- 美联储内部目标冲突（某司库语）："**纽约的市场部门降 IOR 是想让我们把准备金借出去，华盛顿的监管部门却在激励我们多囤准备金。**"
- 推论：靠压 IOR 来"摊平准备金分布"不会奏效——在监管驱动的囤准备金时代，量的分配不由价格决定。

### 5. 结论：跳跃风险

- 供给侧（FHLB  captive 600 亿底线 + 套利流向）与需求侧（借方从外资行扩到美国行、动机从 IOR 套利扩展到结算与 LCR/日内需求）同时收紧；
- **EFFR 年底前出区间**、波动率上升 → OIS 曲线波动与斜率受压 → 缩表空间进一步收窄。

## 关键数据卡

| 指标 | 数值 |
|---|---|
| IBDA 日均量（2018-08） | ~150 亿 |
| IBDA 成交价 | **IOR+8~10bp（区间外）** |
| o/n FF 市场规模 | ~500 亿 |
| FHLB captive 出借底线 | ≥600 亿 |

## 核心概念

- **IBDA**：G-SIB 为日内流动性向 FHLB 全天候借准备金的工具——本笔记首次系统描述。
- **Resolution liquidity**：比 LCR 更高阶的约束，按日内峰值敞口考核。
- **日内流动性溢价**：准备金 > 国债的根本原因之一；只有准备金能"全天任何时点"结算。
- **三阶段进化**：套利→日末 LCR→日内流动性，准备金从"超额"变"必需"的活证据。

## 金句摘录

> "The IBDA market – where banks source intraday liquidity on the margin – is trading well outside the band!"

> "The markets folks in New York are cutting IOR because they want us to lend our reserves, and the regulatory folks in D.C. are incentivizing us to top up and hold on to our reserves."

## 关联阅读

- [[Monetary Policy with Excess Collateral]] —— FHLB 套利/流动性双簿框架的出处
- [[The Revenge of the Plumbing]] —— 年底跳跃风险的兑现（紧接本篇）
- [[Countdown to QE4？]] —— 终局推演
- [[案例研究 · 2019回购危机预言兑现清单]]

## 阅读价值

展示了 Pozsar 情报网络的独特价值：通过司库访谈捕捉到一个**不在任何公开数据里、却已在区间外交易的市场**。对"准备金何时从充裕变稀缺"这一问题，IBDA 利率是比任何官方统计都早的先行指标。

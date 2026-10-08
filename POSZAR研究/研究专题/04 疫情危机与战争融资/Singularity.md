---
tags:
  - Pozsar
  - 疫情危机
  - Libor
日期: 2020-05
---

# Singularity（GMN#30，奇点）

> [!quote] 原文链接
> [[Singularity.pdf]]

## 摘要

GMN#30，2020 年 5 月 14 日，对美元 Libor-OIS 飙升与回落全过程的"**发病回顾**"（morbidity review），以及对**零利率下限（ZLB）时代利率体系**的前瞻：当一切短端利率都被压到零，过去分散的利率星座塌缩成一个"**奇点**"。四部分：①Libor-OIS 先飙后收的三阶段复盘；②估算 ZLB 处 Libor-OIS 的**上限**；③战争融资的内部机制——为什么金融体系能相当轻松地吸收 **1.25 万亿美元国库券**；④结论。这篇是 Pozsar 疫情系列的技术高峰：完整复盘了外国银行如何在三个私人融资渠道间"换挡"，以及互换额度如何把美国压力**出口**到 EURIBOR-OIS。

## 核心论点详解

### Part I：Libor-OIS 的三阶段病程

**阶段一（3 月后两周）——爆裂**：优先货基两周流出 1500 亿；外国银行转向美国一级交易商发短债，交易商从"承销分销"变"**承销持有**"——**以 2.5% 承销 CD/CP、用 3 月 17 日开门的 PDCF 以 25bp 融资**，库存两周增 200 亿。Libor-OIS 走阔 120bp，3 月 31 日 Libor 见顶 145bp。

**阶段二（4 月上半月）——拐点**：美联储 3 月 20 日改每日操作+扩名单，但**日本财年结算日**让 FX swap 市场紧绷到 3 月底（美元出借人都去赚日元端的高隐含收益）；4 月第一周日本年关过去 + 互换额度达到**临界规模** → FX swap 隐含收益率普降 → 外国银行打开第二融资渠道（本地筹资换美元）→ 摆脱交易商的"天价"。副作用：**Libor-Libor 基差大幅转正，把无担保融资压力出口到了 EURIBOR-OIS**——"美联储通过互换额度向世界灌美元，出口的副产品是别人家的融资压力"。

**阶段三（4 月中起）——自由落体**：FX swap 成本下降被外国银行当作**对优先货基压价的杠杆**；优先货基意外大幅回流（4 月后两周逆转一半流出）；**外国银行一个月内从价格接受者变成价格制定者**——CD/CP 从 2.5% 跌到 50bp，Libor-OIS 两周收窄 62bp。

### Part II：ZLB 处 Libor-OIS 的上限

- 零利率下 OIS 已无下行空间，Libor-OIS 的上限由**套利结构**决定：互换额度价格（OIS+25）+ 各辖区无担保溢价 + 货基行为约束；
-  Pozsar 的测算逻辑：ZLB 上 Libor-OIS 不可能回到 3 月的 140bp——互换额度+货基回流+交易商 PDCF 三道闸把它封在更窄区间（具体上限测算见原文图）。

### Part III：战争融资的内部机制——1.25 万亿 bill 怎么消化

- 财政部以 bill 形式为 CARES 法案筹资，1.25 万亿供给看似吓人；
- 但吸收路径清晰：**政府货基 + 准备金体系 + SLR 豁免后的银行 HQLA 组合**；bill 是唯一能在零利率下为现金池提供正收益且不碰交易商表的工具；
- "fairly easily" 的判断依据：货基改革后政府货基 3 万亿+ 的胃口、RRP 兜底、以及美联储扩表制造的准备金——**赤字融资与货币体系已在战争融资范式下融为一体**。

### Part IV：奇点

- 当 OIS=0、repo≈0、bill≈0、Libor 被压到 50bp 以内，曾经层级分明的利率星座塌缩——**一切利率趋同于零，是为奇点**；
- 但奇点不等于和谐：层级只是被压扁、并未消失；任何扰动（发债节奏、季末、监管约束）都会在扁平结构上制造新的褶皱——这正是此后 2021 年 RRP 海啸与 2023 年 SVB 的预告。

## 关键数据卡

| 指标 | 数值 |
|---|---|
| Libor-OIS 峰值 | 145bp（3 月 31 日）→ 4 月底收窄 62bp |
| 交易商危机承销利差 | 2.5% 承销 vs 25bp PDCF 融资 |
| 优先货基流出/回流 | −1500 亿（3 月两周）/ 回流一半 |
| 待吸收 bill 供给 | 1.25 万亿 |

## 核心概念

- **三阶段病程**：交易商兜底→互换额度开通第二渠道→货基回流反转定价权。
- **压力出口论**：美联储灌美元救世界，副产品是别国 Libor 体系承压。
- **奇点**：ZLB 上利率层级的引力塌缩。
- **战争融资消化术**：bill 供给 × 货基 × 准备金 × SLR 豁免的合流。

## 金句摘录

> "Dealers went from 'underwrite and distribute' to 'underwrite and hold' – for a spread."

> "Foreign banks went from being price takers in late March, to being price makers by mid-April."

> "As the Fed flooded the world with dollars through the swap lines, it exported unsecured funding pressures as a byproduct."

## 关联阅读

- [[U.S. Dollar Libor and War Finance]] —— 蛋糕模型与收窄预测（前篇，本篇是其复盘）
- [[U.S. Dollar Libor and Swap Line Rollovers]] —— 互换额度的滚动风险
- [[Taper and the “Mix-Capacity-Target” Trinity]] —— "dollar singularity"概念的呼应
- [[The Money Market Under Government Control]] —— 政府化货币市场的最终形态

## 阅读价值

危机叙事与利率结构分析结合得最完整的一篇：读完你能复盘 2020 年 3–5 月每个基点的来龙去脉，也能理解"零利率不是平静，而是层级被压扁后更危险的状态"。

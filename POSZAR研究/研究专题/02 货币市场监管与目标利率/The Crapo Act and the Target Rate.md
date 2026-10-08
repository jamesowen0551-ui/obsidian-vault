---
tags:
  - Pozsar
  - 货币市场
  - 回购
日期: 2018-09
---

# The Crapo Act and the Target Rate（GMN#17，Crapo 法案与目标利率）

> [!quote] 原文链接
> [[The Crapo Act and the Target Rate.pdf]]

## 摘要

GMN#17，聚焦当时刚兴起的**赞助回购（sponsored repo）**——FICC 允许资本充足的银行会员"保荐"货基和买方直接成为净额结算会员。Crapo 法案（2018 年 S.2155）对托管行杠杆率的松绑是这场变革的制度推手：**托管行（BoNY、State Street）的赞助回购账簿完全不占用 eSLR——在 Basel III 体系里这是罕见的"资产负债表全中性"生意**。Pozsar 在文中画出了季末回购市场的完整食物链（"小鱼→梭鱼→鲨鱼"），并预警：**赞助回购正在把 tri-party repo 利率与联邦基金利率焊在一起，未来季末 FF 利率可能出现尖峰，而且期货没有为此定价**。

## 核心论点详解

### Part I：Basel III 时代的回购层级

- 交易商匹配簿：tri-party 融入（借）→ GC / 双边融出（贷）。三个利差层级：**tri-party 对 o/n RRP、GC 对 tri-party、双边对 GC**。参与者层级同理：货基在最底层拿最低利率；一级交易商拿最便宜的钱；非一级交易商和买方逐级加价。
- 一级交易商内部还有层级：法律实体在**银行（分行）里的交易商（法兴、加系等）**可以在 tri-party 与 **o/n FF** 之间选便宜的资金；实体在券商里的交易商只能走 tri-party——这是 repo 与 FF 两个市场连通的暗管。
- **季末问题**：外资一级交易商按季度报表面临缩表，缩表主要靠**净额结算（netting）**而非完全关账——而美国只有 FICC 中央清算的交易可轧差。于是季末交易商把 tri-party 资金换成 FICC 清算的 GC 资金 → GC 资金需求暴增 → 银行从 HQLA 组合拆出准备金去放 GC repo，**收取对 IOR 的高额利差** → 图 6 中 GC repo 季末巨峰。

**季末食物链**（o/n GC repo 的出借方层级）：

| 层级 | 主体 | 出借条件 |
|---|---|---|
| 小鱼（minnows） | 准备金远超美元 HQLA 需求的外国银行 | IOR + 1–2bp 就肯放 |
| 梭鱼（barracudas） | 流动性"不那么超额"的更大银行 | 要更宽利差 |
| 鲨鱼（sharks） | 美国 G-SIB（控制最多准备金、表最贵） | 最宽利差 |

- 季末风大浪急时，流动性需求沿食物链一路上移。"It takes a minnow to catch a barracuda, a barracuda to catch a shark…"
- **全球只有 25 家银行**能在 GC repo 市场出借——它们在准备金与 GC repo 之间切换的灵活度，决定季末能流进多少钱。
- 季末赢家输家：货基输（被交易商拒之门外，只能去 RRP）；一级交易商输（被迫付 GC 高价）；银行赢（从赚 IOR 变成赚 IOR+高利差）。

### Part II：赞助回购如何压平层级

- 机制：FICC 的**银行会员**把现金出借方（货基）与现金借入方（固收基金、对冲基金）保荐为净额会员；托管行日终将两侧交易 novate 给 FICC → **匹配簿（GC-tri-party、双边-tri-party）不触碰托管行的 eSLR**。
- 为什么只有两家能做：FICC 会员多为券商不能保荐；外资行纽约分行不算资本充足银行实体；美国大行保荐会推高 G-SIB 附加资本（JPM 2.5%、Citi/BoA 2.0%）——**只有 BoNY 与 State Street 两家托管行（附加仅 1.0%）合适**，成为赞助回购的双寡头。
- 规模：两家托管行回购市场份额**从零做到约 500 亿**——相当于某法/加系交易商账簿翻倍。2017 年下半年客户反映"回购资产负债表突然变宽裕了"，源头可能正是赞助回购。
- 价格行为后果：托管行的赞助簿**季内季末都中性**——它们不在季末撤退，改变了"季末 GC 尖峰"的旧格局，但也把 tri-party 利率与 FF 利率更紧地绑在一起。

### Part III–IV：FF 利率的季末尖峰风险

- 银行实体的交易商在 tri-party 与 FF 之间套利 → 回购压力直接传导进 FF 市场；
- 季末 FF 出借方（FHLB）资金被分流/要价上移 → **EFFR 季末尖峰**风险，且会常态化、幅度可能加大；
- 市场（FF/OIS 期货）尚未为此定价——"Futures are not priced for that…"

## 关键数据卡

| 指标 | 数值 |
|---|---|
| 托管行赞助回购规模 | 0 → ~500 亿 |
| 全球 GC repo 出借银行 | 仅 25 家 |
| G-SIB 附加 | JPM 2.5% / Citi、BoA 2.0% / 托管行 1.0% |
| 季末 GC repo 利差 | 对 IOR 高额尖峰（见图 6） |

## 核心概念

- **赞助回购（sponsored repo）**：货基/买方直达 FICC 净额结算，托管行表外撮合。
- **季末食物链**：minnow→barracuda→shark 的准备金出借层级。
- **净额结算约束**：美国只有 FICC 同对手交易可轧差——季末挤向 GC 的制度根源。
- **Crapo 法案效应**：托管行存放央行的资产获 SLR 豁免类待遇，释放赞助回购产能。

## 金句摘录

> "It takes a minnow to catch a barracuda, a barracuda to catch a shark…"

> "Sponsored repo is a totally balance sheet neutral activity. In a system subject to Basel III that is a rarity."

> "Futures are not priced for that…"

## 关联阅读

- [[Taper and the “Mix-Capacity-Target” Trinity]] —— 同期缩表背景
- [[Design Options for an on Repo Facility]] —— 季末尖峰的政策应对：常设回购便利
- [[The Revenge of the Plumbing]] —— 尖峰风险的年终兑现
- [[案例研究 · 2019回购危机预言兑现清单]]

## 阅读价值

理解美国回购市场微观结构的最佳单篇：谁融给谁、谁季末撤退、谁在食物链第几层、为什么只有两家托管行能做中性生意。季末尖峰预警在随后几个季度反复兑现，最终指向 SRF（常设回购便利）的设立。

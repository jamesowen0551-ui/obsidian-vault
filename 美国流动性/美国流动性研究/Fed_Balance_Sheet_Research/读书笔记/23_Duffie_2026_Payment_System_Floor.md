---
tags: [paper, BPEA, 支付系统, 准备金下限, Fedwire, 流动性节约机制]
paper: "The Payment System Puts a Floor on the Fed's Balance Sheet"
authors: [Darrell Duffie]
year: 2026
venue: Brookings Papers on Economic Activity（Spring 2026 会议，2026-03-26/27）
---

# Duffie (2026)：支付系统给联储资产负债表划了地板

> 一句话：大银行彼此**及时付款**所需的准备金量，才是联储资产负债表真正的下限；联储事实上已在"跟着支付系统需求扩表"。若要更小，处方是四件事：**临时 OMO 对冲供给冲击 + Fedwire 引入流动性节约机制 + 改流动性监管 + 准备金分层付息**。

## 核心论证

- 准备金的首要功能不是货币政策，而是**支付结算**：当准备金对大银行间的及时支付不足时，货币市场利率就会剧烈波动或跳空（2019 年即如此）。
- 因此联储实际上已经进入一种**"支付系统决定表规模"**的均衡：支付需求随名义 GDP 与金融活动增长 → 准备金需求增长 → 表只能跟着长。
- "下限"不是固定数，而是**支付技术、监管与制度安排的函数**——移动下限要从这些源头入手。

## 四项缩表处方

| 处方 | 机制 |
|---|---|
| **临时 OMO 对冲** | 用短期回购操作中和 TGA 等外生因素对准备金供给的冲击（呼应 [[#Vissing-Jorgensen (2025)]]） |
| **Fedwire 流动性节约机制（LSM）** | 学英国央行 CHAPS：支付排队/轧差算法可大幅节约日内流动性需求（Davey & Gray 2014 估计 CHAPS 节约显著；User's Guide 估计 $100–125B） |
| **修改流动性监管** | LCR/内部压力测试驱动了大量结构性准备金需求（[[#Miran (2025)]]、User's Guide 的主战场） |
| **准备金分层付息（tiering）** | 对超过结算所需的准备金付更低利率，削弱"为套利而囤准备金"的动机 |

## 批判性评注

- 本文把 [[#Copeland, Duffie & Yang (2021)]] 的微观证据（日内支付行为）升级为**一般性的"支付约束论"**：比"监管主导论"更基础——即使监管全改，支付结算的物理需求仍在那里。
- 与 [[#User's Guide (FEDS 2026)]] 关系最深：User's Guide 的 Fedwire、TGA、监管选项几乎都能在此找到理论出处；Duffie 分层付息则是 User's Guide 之外的新工具。
- 与 [[#Nelson (2025)]] 的分歧：Nelson 想用贴现窗口额度替代准备金，Duffie 更强调**用支付系统技术（LSM）直接减少需求**——两条路线的工程含量不同，LSM 不动监管，政治成本可能更低。
- 局限：LSM 等改造需要数年工程与行业协调；"分层付息"在金融稳定含义上未充分展开（压低超额准备金收益会推高银行对批发融资的依赖？）。
- 注意还有姊妹篇：Duffie, Singh & Wang (2026) *An Efficient Liquidity Savings Mechanism* 给出了 LSM 的机制设计细节（达拉斯联储 Schulhofer-Wohl 有专门评论）。

## 与其他文献的关系

- 与 [[#Waller (2025)]] 的"9% GDP 阈值"估算互补：Waller 从总量经验定标，Duffie 从支付微观结构解释阈值为什么在那里、怎么压低它。
- 与 [[#Acharya et al. (2023)]] 相对照：Acharya 讲"缩表难"的负债侧黏性，Duffie 讲"下限在哪、如何下移"的建设性方案。

## 原文

- [PDF](../07_Background_Context/Duffie_2026_Payment_System_Floor_BPEA.pdf)

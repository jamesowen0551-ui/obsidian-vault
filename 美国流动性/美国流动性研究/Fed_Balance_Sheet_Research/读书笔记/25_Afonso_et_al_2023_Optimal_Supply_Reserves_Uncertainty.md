---
title: Afonso, La Spada, Mertens & Williams (2023) The Optimal Supply of Central Bank Reserves under Uncertainty
authors: Gara Afonso, Gabriele La Spada, Thomas M. Mertens, John C. Williams
year: 2023
journal: Federal Reserve Bank of New York Staff Report 1077
created: 2026-08-06
tags:
  - 美联储
  - 准备金需求
  - 操作框架
  - 文献笔记
---

> [!abstract] 一句话总结
> 准备金需求存在不确定性时，预防性动机使最优供给**超过确定性等价水平**（甚至进入 abundant 区）；若贷款便利定价与设计足够好，则可换取更小的最优供给——供给数量与便利设计是联合决策。

原文：[[Afonso_LaSpada_Mertens_Williams_2023_Optimal_Supply_Reserves_SR1077.pdf|原文 PDF]]

> [!info] 版本说明
> 纽约联储 Staff Report 1077（2023 年 2 月），末位作者是纽约联储主席 Williams。这是 Williams (2025) 演讲（笔记 18）与 Clouse et al. (2025) 仪表盘（笔记 20）的共同**理论底稿**。

## 研究问题与核心发现

**研究问题**：

> 央行应供给多少准备金？答案如何随需求不确定性、利率控制目标与流动性便利设计而变化？

**核心发现**：

1. **不确定性 → 预防性超供**：需求随机时，为保证利率不越出容忍区间，最优供给高于确定性情形；不确定性与利率控制的精度要求越高，超供越多，甚至可以多到 abundant。
2. **供给与便利是联合决策**：贴现窗口/SRF 等便利若定价合理、污名低，银行可用"或有流动性"替代"实有准备金"，最优供给显著收窄。
3. **无唯一最优方式**："高供给 + 低频率使用便利"与"低供给 + 高频率使用便利"可以是同一效率前沿上的等价点。
4. **充裕区间的内生宽度**：ample 不是一个点而是一个由不确定性结构决定的区间——官方监测应同时盯利差水平与曲线斜率。

> **关键信息**：把"充裕准备金"从经验定标（2019 年样本点）提升为**可推导的最优化问题**，是官方现状派的方法论引擎。

## 理论框架

Poole 式静态模型的现代版：

| 要素 | 含义 |
|------|------|
| 需求曲线 | 非线性、随机移动 |
| 损失函数 | 利率偏离目标的平方损失 + 供给成本 |
| 便利设计 | 贷款利率、可得性 → 影响有效需求 |
| 最优解 | 供给量 × 便利参数的联合最优点 |

## 实证方法（如适用）

理论论文；以校准方式参照 2018–19 年美国货币市场利差波动幅度。

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| ample vs abundant | 需求曲线平坦段入口 vs 远超入口的过量区 |
| 预防性超供 | 为吸收需求不确定性而多供给的准备金 |
| 便利的替代弹性 | 好的贷款便利可替代实有准备金的程度 |
| 联合决策 | 供给数量与便利定价/设计不可分开优化 |

## 对"美联储资产负债表"研究的含义

- **为"缩表换便利"方案定价**：Logan&SW (28)、User's Guide (01) 的"需求曲线左移"选项本质是沿本文效率前沿移动——用更好的 SRF/贴现窗口换更小供给。
- **可检验命题**：SRF 去污名化（如早间操作、中央清算）成功后，充裕下限应可观测地下移——可由 Clouse 仪表盘三指标验证。
- **限制**：模型不含分布摩擦与负债侧引致，因此它给的是"无摩擦世界"的最小供给；真实下限要加上 CDY/Anbil 修正。

## 理论定位

- **学术地位**：Ihrig et al. (2020) 官方框架的最优化形式化；Poole (1968) 传统的当代完成版。
- **与前人关系**：将 Williams 长期倡导的"弹性供给"理念模型化。
- **后续发展**：直接产出 Williams (2025) 演讲与 Clouse et al. (2025) 监测框架；被 Cavallino et al. (2025) 纳入二维分类。
- **局限性**：单期静态；无银行异质性；无危机状态切换。

## 局限与待跟进问题

- 需求不确定性的结构估计仍缺失（冲击方差多大？肥尾吗？）
- 便利污名的建模只是参数——污名的实证度量见 Anbil et al. (2026) 与 SRF 使用数据
- 与支付系统物理下限（Duffie 2026）的关系未处理

## 相关笔记

- [[18_Williams_2025_On_the_Optimal_Supply_of_Reserves|Williams (2025) 政策版]]
- [[20_Clouse_Infante_Senyuz_2025_Market_Based_Indicators|Clouse et al. (2025) 操作版]]
- [[35_Ihrig_Senyuz_Weinbach_2020_Ample_Reserves_Approach|Ihrig et al. (2020) 官方教科书]]
- [[28_Logan_Schulhofer-Wohl_2026_Options_for_Reducing_Fed_Balance_Sheet|Logan & SW (2026) 选项清单]]

---
title: López-Salido & Vissing-Jorgensen (2023) Reserve Demand, Interest Rate Control, and Quantitative Tightening
authors: David López-Salido, Annette Vissing-Jorgensen
year: 2023
journal: ECB 货币政策会议论文（2023.10）；工作论文持续更新（SSRN 4371999）
created: 2026-08-06
tags:
  - 美联储
  - 准备金需求
  - QT
  - 便利收益
  - 文献笔记
---

> [!abstract] 一句话总结
> 本轮"还能缩多少"讨论的定量起点：从银行最优化推导准备金需求三大驱动，估计 2009–2022 年半弹性 −5 的稳定需求曲线（控制存款后），画出文献首组实证 iso-联邦基金曲线，判断**准备金+ON RRP 至少还可缩 2 万亿美元**。

原文：[[Lopez-Salido_Vissing-Jorgensen_2023_Reserve_Demand_IRC_QT_ECB.pdf|原文 PDF]]

> [!info] 版本说明
> ECB 货币政策会议（2023-10）版本，工作论文持续更新。作者是理事会高级顾问与 Berkeley 教授，本文是官方与学界引用的需求曲线基准。

## 研究问题与核心发现

**研究问题**：

> 准备金需求曲线由什么驱动、形状如何、位置是否稳定？据此，QT 还能缩多少而不失控？

**核心发现**：

1. **三大驱动**：利差（机会成本）、便利收益（随 R↓ 而升、**随存款 D↑ 而升**）、资产负债表成本（SLR 等）；存款是需求曲线的核心移动变量——存款持续增长 ⇒ 曲线持续右移。
2. **半弹性 −5**：2009M1–2022M10 月度样本，利差每升 1bp，存款调整后需求降约 5%；控制存款后曲线惊人地稳定。
3. **iso-联邦基金曲线**：给定目标 EFFR，IOR 与（准备金+ON RRP）的组合轨迹——文献中第一组实证估计；供给越低，命中目标所需 IOR 越低。
4. **QT 可行量**：以 2022 年 10 月存款水平，两种互补方法均支持"至少还可缩 2 万亿美元"。
5. **2019 的重新解读**：由于存款增长，2019 年 9 月把准备金+ON RRP 缩到 GDP 的 7% 早已过了安全线——不是缩得太多，而是需求右移了。

> **关键信息**：把"ample 在哪里"从玄学变成可计算的曲线；"存款是需求移动变量"解释了 Nelson 棘轮的一半（另一半是监管与习惯）。

## 理论框架

$$
EFFR = IOR + \underbrace{\text{边际便利收益}(R, D)}_{\text{随}R\downarrow\text{而升，随}D\uparrow\text{而升}} - \underbrace{\text{单位资产负债表成本}}_{\text{SLR 等监管成本}}
$$

延伸：需求曲线可相对任何负债定义；联储设施通过改变均衡供给控制利率，设施使用率由框架内生决定。

## 实证方法（如适用）

- **样本**：2009M1–2022M10 月度
- **识别假设**：月度频率上准备金+ON RRP 变动主要来自 QE/QT（供给驱动）而非需求冲击
- **方法**：约简式需求曲线估计 + iso-FF 曲线构造

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| 便利收益 | 准备金管理存款进出的服务流价值 |
| iso-FF 曲线 | 命中同一 EFFR 的 IOR×数量组合 |
| 存款调整 | 剔除存款右移后的需求曲线 |
| 冗余量 | 当前水平减安全下限的可缩空间 |

## 对"美联储资产负债表"研究的含义

- **政策标尺**：User's Guide 的利差选项、Waller 的地板算术、Perli 的监测均以本文为实证基础；注意 2 万亿是"规则不变"的冗余量，与 UG 的"改规则"空间不能简单叠加。
- **可检验命题**：存款相对 GDP 继续增长 ⇒ 充裕下限继续右移——年度复核需求曲线即可验证。
- **弱点**：约简式函数形式缺理论约束，外推形状由形式决定；监管变化引起的曲线旋转无法识别（Lagos & Navarro 的批评）。

## 理论定位

- **学术地位**：Poole (1968)、Bianchi & Bigio (2022)、Afonso & Lagos (2015) 之后的实证需求曲线标杆。
- **与前人关系**：iso-FF 术语借自 Bianchi & Bigio（他们是纯理论）。
- **后续发展**：Lagos & Navarro (2026) 的最小理论修正；姊妹篇 Vissing-Jorgensen (Sintra 2023) 从便利最大化讨论最优 QT。
- **局限性**：2 万亿是 2022.10 存款条件下的冗余量而非绝对下限；SRF 价值等不确定性作者自列。

## 局限与待跟进问题

- 曲线旋转（监管/市场结构变化）的识别 → Lagos & Navarro (2026)
- 后 2019 时代需求右移幅度的持续追踪
- 与 SR 1077 不确定性框架的融合

## 相关笔记

- [[06_Lagos_Navarro_2026_Reserve_Demand_Minimal_Theory|Lagos & Navarro (2026) 方法论修正]]
- [[01_User's_Guide_2026_Reducing_Fed_Balance_Sheet|User's Guide (2026) 利差选项]]
- [[25_Afonso_et_al_2023_Optimal_Supply_Reserves_Uncertainty|Afonso et al. (2023) 不确定性]]
- [[26_Bianchi_Bigio_2022_Banks_Liquidity_Management|Bianchi & Bigio (2022) 理论源头]]

---
tags: [读书笔记, 准备金需求, QT, 利率控制, 便利收益, iso-联邦基金曲线]
paper: "Reserve Demand, Interest Rate Control, and Quantitative Tightening"
authors: "David López-Salido, Annette Vissing-Jorgensen"
year: 2023
venue: "ECB 货币政策会议论文（2023.10）；工作论文持续更新（SSRN 4371999）"
---

# López-Salido & Vissing-Jorgensen (2023)：Reserve Demand, Interest Rate Control, and QT

> [!info] 原文
> [本地 PDF](../02_Reserve_Demand_Framework/Lopez-Salido_Vissing-Jorgensen_2023_Reserve_Demand_IRC_QT_ECB.pdf) ｜ [ECB 版](https://www.ecb.europa.eu/press/conferences/shared/pdf/20231004_mon_pol_conference/Lopez_Salido_paper.pdf)

## 一句话总结

本轮"还能缩多少"讨论的定量起点：从银行最优化问题推导出准备金需求三大驱动，估计出 2009–2022 年半弹性 −5 的稳定需求曲线（控制存款后），据此画出文献中第一组实证 iso-联邦基金曲线，并判断**准备金+ONRRP 至少还可缩 2 万亿美元**。

## 理论框架：三大驱动

从银行最优化一阶条件（在联邦基金市场借钱、存联储吃 IOR）出发：

$$EFFR = IOR + \underbrace{\text{边际便利收益}(R, D)}_{\text{随}R\downarrow\text{而升，随}D\uparrow\text{而升}} - \underbrace{\text{单位资产负债表成本}}_{\text{SLR 等监管成本}}$$

1. **利差**：EFFR 与 IOR 之差 = 持有准备金的机会成本；
2. **便利收益**：准备金是管理存款进出的最佳工具（类比 Krishnamurthy & Vissing-Jorgensen 2012 对国债的便利收益建模）；**存款是需求曲线的核心移动变量**——存款（甚至相对 GDP）持续增长 ⇒ 需求曲线持续右移；
3. **资产负债表成本**：使"借市场钱、存联储"的套利有成本，决定曲线弹性。

两个延伸：(a) 需求曲线可相对任何负债定义——相对 repo 融资的曲线因抵押品成本（损失的证券借贷收入）而更低；(b) 联储设施（贴现窗口、ON RRP、SRF）通过改变均衡准备金**供给**来控制利率——设施使用率由框架内生决定。

## 实证结果

- 样本 2009M1–2022M10 月度数据；**半弹性 −5**：EFFR–IOR 利差每升 1bp，存款调整后的准备金+ONRRP 需求降约 5%；
- **控制存款后需求曲线惊人地稳定**——存款调整后的（准备金+ONRRP）与利差呈紧密负相关；
- 识别假设：月度频率上准备金+ONRRP 的变动主要来自 QE/QT（供给驱动）而非需求冲击。

## 政策应用（本文最有影响力的部分）

1. **iso-联邦基金曲线**：给定目标 EFFR，IOR 与（准备金+ONRRP）的组合轨迹——文献中第一组实证估计的 iso-FF 曲线（术语借自 Bianchi & Bigio 2022，但他们是纯理论）。供给越低，为命中目标所需的 IOR 越低；
2. **QT 可行量**：以 2022 年 10 月存款水平，两种互补方法均支持"**至少还可缩 2 万亿美元**才会触发利率波动"；
3. **2019 年的重新解读**：由于存款增长，2019 年 9 月时即便把准备金+ONRRP 缩到 GDP 的 7% 也**早已**过了安全线——不是缩得太多，而是需求右移了；
4. 不确定性来源：存款演化、SRF 的价值、自主负债因素（TGA 等）的波动。

## 批判性评注

- **优点**：把"ample 在哪里"从玄学变成可计算的曲线；"存款是需求移动变量"这一发现是全文最持久的贡献——它解释了 Nelson 的"棘轮"的一半（另一半是监管与习惯）。
- **弱点**（[[#Lagos & Navarro (2026)]] 系统指出）：约简式函数形式缺乏理论约束 ⇒ 外推到未观测区域时形状完全由函数形式决定；监管/市场结构变化引起的曲线旋转无法识别。Lagos & Navarro 的"最小理论"估计正是针对这三点。
- 对 2 万亿数字的使用要谨慎：它是 2022 年 10 月存款条件下的**冗余量**，不是绝对下限；且作者自己列出的不确定性（SRF 价值）在 2025 年 SRF 常态化使用后已部分改变。
- 与 User's Guide 的关系：User's Guide 的 1.2–2.1 万亿是"改规则后"的可缩量，LS&VJ 的 2 万亿是"规则不变时"的冗余量——两者相加的部分（EFFR 高于 IORB 选项）其实共用同一条需求曲线，不能简单叠加。

## 与其他文献的关系

- 理论前辈：Poole (1968)、Bianchi & Bigio (2022)、Afonso & Lagos (2015)。
- 方法论批评者与修正者：[[#Lagos & Navarro (2026)]]。
- 政策引用：Perli/Remache 的"弹性监测"、User's Guide 的量化、Anderson et al. (2024) FEDS Notes 联邦基金市场演化均以此为基础。
- 姊妹篇：Vissing-Jorgensen (2023, Sintra) 从"便利最大化"角度讨论最优 QT——若联储通过买安全资产供准备金，便利最大化要求准备金便利收益 = 债券便利收益。

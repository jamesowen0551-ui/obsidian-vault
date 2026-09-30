---
title: Laubach & Williams (2003) Measuring the Natural Rate of Interest
authors: Thomas Laubach, John C. Williams
year: 2003
journal: Review of Economics and Statistics, 85(4), 1063–1070
created: 2026-08-19
tags:
  - 实际利率
  - 自然利率
  - r*度量
  - 文献笔记
---

> [!abstract] 一句话总结
> 用 Kalman 滤波在 New Keynesian 框架下联合估计美国时变自然利率 r\*、潜在产出与趋势增长，发现 r\* 与趋势增长紧密联动，但估计高度不精确。

> [!info] 版本说明
> - 正式发表于 Review of Economics and Statistics（被引约 1867）
> - 前身是纽约联储 2001 年 Staff Report；后续有 2016 Redux 与 2023 更新版
> - 本笔记基于摘要与文献常识整理，系数细节以原文为准

## 研究问题与核心发现

**研究问题**：

> 自然利率——使产出等于自然水平且通胀稳定的实际利率——不可观测，如何估计它？它的时变由什么驱动？

**核心发现**：

1. r\* 与**趋势增长率**紧密联动，符合理论预测（增长快 → 均衡利率高）
2. r\* 估计**非常不精确**，置信区间宽，且存在严重的实时测量误差（数据修正会显著改变估计）
3. 单边（real-time）估计与事后（ex-post）估计差异大，用 r\* 做实时政策基准需谨慎

> **关键信息**：HLW 模型成为美联储官方 r\* 序列的方法论基石，同时它自己给出了"别迷信点估计"的警告。

## 理论框架

New Keynesian 三方程结构 + 状态空间模型：

| 方程 | 内容 |
|------|------|
| IS 曲线 | 产出缺口取决于滞后缺口与实际利率缺口 $(r - r^*)$ |
| Phillips 曲线 | 通胀取决于滞后通胀与产出缺口 |
| 状态方程 | $r_t^* = c \cdot g_t + z_t$，$g_t$ 为趋势增长（随机游走），$z_t$ 为其他持久冲击 |

Kalman 滤波同时提取潜在产出、趋势增长 $g_t$ 与 $r_t^*$ 三个不可观测状态。

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| 自然利率 r\* | 产出处于自然水平、通胀稳定时的实际短期利率 |
| 趋势增长 g | 潜在产出的增长率，r\* 的主要驱动 |
| 利率缺口 | 实际利率 − r\*，货币政策立场的度量 |

## 对"美国实际利率"研究的含义

- **基准序列选择**：纽约联储官网持续发布 HLW 与 LM 两种 r\* 估计，本研究实证部分应以之为锚
- **增长通道**：若用 r\* ≈ f(趋势增长)，则 Fernald TFP / 潜在增长数据是天然解释变量
- **不确定性处理**：引用 r\* 点估计时必须带置信区间；不同口径（单边/双边）结论可能相反

## 理论定位

- **学术地位**：自然利率实证度量领域的奠基之作，"HLW 模型"成为行业标准
- **与前人关系**：将 Wicksell 自然利率概念嵌入现代 New Keynesian 框架
- **后续发展**：HLW (2017) 国际版、LW (2016) Redux、Kiley、Johannsen-Mertens、Lubik-Matthes 等替代估计均以此为参照系
- **局限性**：结构假定强（IS/Phillips 曲线线性、斜率稳定）；对趋势增长的识别依赖产出数据质量

## 局限与待跟进问题

- 估计不精确问题在大衰退后更加严重（见 [[Laubach_Williams_2016_Redux_详细笔记|Redux 2016]]）
- [[Lunsford_West_2019_详细笔记|Lunsford & West (2019)]] 质疑 r\* 与趋势增长相关性的稳健性——必读反方

## 相关笔记

- [[Laubach_Williams_2016_Redux_详细笔记|Laubach & Williams (2016) Redux]]
- [[Holston_Laubach_Williams_2023_详细笔记|HLW (2023) 新冠后更新]]
- [[Lubik_Matthes_2015_详细笔记|Lubik & Matthes (2015) 替代方法]]
- [[Lunsford_West_2019_详细笔记|Lunsford & West (2019) 反方证据]]

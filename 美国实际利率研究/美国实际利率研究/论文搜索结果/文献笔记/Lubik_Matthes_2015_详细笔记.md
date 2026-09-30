---
title: Lubik & Matthes (2015) Calculating the Natural Rate of Interest — A Comparison of Two Alternative Approaches
authors: Thomas A. Lubik, Christian Matthes
year: 2015
journal: Richmond Fed Economic Brief No. 15-10
created: 2026-08-19
tags:
  - 实际利率
  - 自然利率
  - r*度量
  - 文献笔记
---

> [!abstract] 一句话总结
> 提出用少结构假定的时变参数 VAR（TVP-VAR）估计自然利率，作为 HLW 结构模型之外的替代方案。

> [!info] 版本说明
> - 里士满联储 Economic Brief（另有配套数据与持续更新，2023 年 No. 23-32 给出最新估计）
> - 里士满联储官网提供 LM r\* 序列下载

## 研究问题与核心发现

**研究问题**：

> 自然利率不可观测必须"算"出来，但结构模型（HLW）依赖强假定，能否用更不可知论的方法估计？

**核心发现**：

1. TVP-VAR 方法仅用长期识别约束（货币长期中性），让数据自己决定 r\* 的路径
2. LM 估计与 HLW 估计**长期走势相似但时点与水平有差异**——说明 r\* 估计存在"模型不确定性"
3. 持续更新的序列可用于实时追踪

> **关键信息**：r\* 不是一个数，而是一个"模型族"——引用时必须说明口径。

## 理论框架

| 方法 | 结构假定 | 识别 |
|------|---------|------|
| HLW | IS + Phillips + 状态方程 | 结构方程 |
| LM TVP-VAR | 几乎无 | 仅长期中性约束 |

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| TVP-VAR | 参数随时间变化的向量自回归 |
| 模型不确定性 | 不同合理模型给出不同 r\* 路径 |

## 对"美国实际利率"研究的含义

- **稳健性检验标配**：任何基于 r\* 的结论应同时在 HLW 与 LM 序列上验证
- 两者分叉的时期（如 2020 后）本身是研究素材——分叉原因指向结构假定差异

## 理论定位

- **学术地位**：r\* 估计的主要"非结构"替代方案
- **与前人关系**：对照/补充 HLW；方法上承 Cogley-Sargent 的 TVP-VAR 传统
- **局限性**：VAR 低结构意味着 r\* 定义更"计量化"，经济解释力弱

## 相关笔记

- [[Laubach_Williams_2003_详细笔记|Laubach & Williams (2003)]]
- [[Kiley_2020_详细笔记|Kiley 半结构替代]]
- [[Johannsen_Mertens_2021_详细笔记|Johannsen & Mertens 影子利率法]]

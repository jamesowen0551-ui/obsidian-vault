---
title: Lubik & Matthes (2015) Calculating the Natural Rate of Interest — A Comparison of Two Alternative Approaches
authors: Thomas A. Lubik, Christian Matthes
year: 2015
journal: Richmond Fed Economic Brief No. 15-10
created: 2026-10-08
tags:
  - 实际利率
  - 自然利率
  - r*度量
  - 文献笔记
---

> [!abstract] 一句话总结
> 用 TVP-VAR（仅施加"实际利率长期向其收敛"这一 Wicksell 式识别）估计自然利率：从 1980s 初约 3.5% 趋势性降至 2015Q2 约 0.5%，且**从未转负**——与 HLW 结构模型互为方法论对照。

原文：[[05_Lubik_Matthes_2015_Calculating_Natural_Rate.pdf|原文 PDF]]（Economic Brief，6 页）

> [!info] 版本说明
> - 里士满联储 Economic Brief EB15-10；LM r\* 序列在里士满联储官网按季度更新（2023 年 EB23-32 给出最新版模型）
> - 本笔记基于 PDF 原文精读（含正文数字与脚注细节）

## 研究问题与核心发现

**研究问题**：

> 自然利率不可观测，HLW 方法依赖较强的结构假定（IS/Phillips 方程），能否用更不可知论的时序方法估计，两种方法差多少？

**核心发现**（含原文数字）：

1. **LM 估计路径**：自然利率从 1980s 初约 **3.5%** 长期下降至 2015Q2 的约 **0.5%**；2001 衰退与 2007 大衰退起点出现急降
2. **从未转负**：与部分 HLW 口径（及 EMR 的 −1.5%~−2%）形成重要差异；1970s–80s 中的实际利率大幅波动**没有**传导到自然利率路径——TVP-VAR 的随机波动率把这些归为冲击方差变化而非趋势变化
3. **政策缺口判定**：自然利率高出实际利率整整一个百分点，且 2009 年后一直如此——按 Wicksell 标准，货币政策"一直处于过松状态"（截至 2015）
4. **HLW 的不确定性**：原文脚注指出 LW (2003) 中自然利率路径的 **70% 置信区间可达点估计上下 3 个百分点**——r\* 点估计的置信度很低
5. **方法论对照表**：HLW = 结构状态空间 + Kalman 滤波；LM = 三变量（实际 GDP 增长、PCE 通胀、LW 口径实际利率）TVP-VAR，1961–2015Q2，自然利率定义为**实际利率的 5 年期条件远期预测**（因系数随机游走，预测不回归样本均值）

> **关键信息**："自然利率 = 实际利率的长期收敛点"这一 Wicksell 定义，可以用几乎无结构的计量实现——但得到的水平与 HLW 有系统差异，说明 r\* 估计的**模型不确定性是一阶的**。

## 理论框架

| 维度 | HLW (2003) | LM (2015) |
|------|-----------|-----------|
| 框架 | New Keynesian 状态空间（IS+Phillips+状态方程） | TVP-VAR（系数与波动率均随机游走） |
| 识别 | 经济结构方程 | 仅 Wicksell 收敛性（实际利率长期趋向自然利率） |
| 自然利率定义 | $r^* = c\cdot g_t + z_t$ | 实际利率的 5 年条件预测 |
| 2015 年读数 | 更低（约 0 附近） | 约 0.5%，从未为负 |

思想谱系：Wicksell (1898) 定义"与价格稳定相容的利率" → Woodford 将其嵌入 New Keynesian 框架 → LW 实证化 → LM 以"少结构"路线对照。

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| TVP-VAR | 系数与冲击方差时变的向量自回归（Cogley-Sargent、Primiceri 传统） |
| 随机波动率 | 把 70s–80s 大波动归为方差变化而非趋势变化的关键 |
| 政策立场 | 实际利率 − 自然利率的符号与幅度（Wicksell 缺口） |

## 对"美国实际利率"研究的含义

- **稳健性检验标配**：任何基于 r\* 的结论应在 HLW 与 LM 两序列上同时验证；两者分叉（如是否转负、2015 年差约 0.5pp）本身就是模型不确定性的实证
- **趋势 vs 波动**的归属问题：LM 用随机波动率吸收 70s–80s 波动，HLW 的结构方程会把更多波动归入趋势——做长样本分析时这个选择影响结论
- LM 的"5 年远期预测"定义与 [[Laubach_2009_详细笔记|Laubach (2009)]] 的远期利率思路相通：都试图剥离周期成分
- 里士满联储持续更新（2023 版含新冠处理），是获取最新 LM 序列的出处

## 理论定位

- **学术地位**：r\* 估计"低结构"路线的代表作，政策圈使用广泛
- **与前人关系**：方法承 Cogley-Sargent (2001)、Primiceri (2005) TVP-VAR；概念承 Wicksell-Woodford
- **局限性**：Economic Brief 文体，技术细节需看配套论文（Lubik-Matthes, "Time-Varying Parameter Vector Autoregressions"）；纯计量的 r\* 定义经济解释力弱；"从不为负"与 EMR 的负 r\* 之间的裁决依赖先验

## 相关笔记

- [[Laubach_Williams_2003_详细笔记|Laubach & Williams (2003)]]
- [[Kiley_2020_详细笔记|Kiley 半结构替代]]
- [[Johannsen_Mertens_2021_详细笔记|Johannsen & Mertens 影子利率法]]
- [[EMR_2019_详细笔记|EMR (2019) 负自然利率模型]]

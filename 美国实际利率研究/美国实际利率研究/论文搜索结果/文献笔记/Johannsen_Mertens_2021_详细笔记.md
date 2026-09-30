---
title: Johannsen & Mertens (2021) A Time-Series Model of Interest Rates with the Effective Lower Bound
authors: Benjamin K. Johannsen, Elmar Mertens
year: 2021
journal: Journal of Money, Credit and Banking, 53(1), 139–171
created: 2026-08-19
tags:
  - 实际利率
  - 自然利率
  - r*度量
  - 文献笔记
---

> [!abstract] 一句话总结
> 构建含有效下限（ELB）的影子利率时序模型估计 r\*，把 ZLB 时期的非常规政策信息纳入自然利率测度。

> [!info] 版本说明
> - 发表于 JMCB（被引约 174）；检索 CSV 中位于第二条
> - 作者为美联储理事会经济学家；另有 Mertens & Johannsen (2015) 影子利率前身文献

## 研究问题与核心发现

**研究问题**：

> ZLB 期间名义利率被"冻结"，常规时序模型丢失信息，如何在这段时期也能一致地估计 r\*？

**核心发现**：

1. 用**影子利率**（shadow rate）替代观测利率，可跨越 ZLB 时期连续建模
2. 估计显示美国 r\* 长期下行趋势在 ZLB 时期延续
3. 影子利率框架让政策立场（含 QE 的等效宽松）与 r\* 缺口可计算

> **关键信息**：ZLB 不是数据黑洞——影子利率把 2009–2015 年接回了 r\* 时间序列。

## 理论框架

灵活时序模型：名义影子短期利率 = 趋势（r\* + 趋势通胀）+ 周期；观测利率 = max(影子利率, ELB)。

## 关键概念速查

| 概念 | 本文中的含义 |
| --- | --- |
| 影子利率 | 无下限时"应有"的短期利率，可为负 |
| ELB | 有效下限，略高于零的政策利率底部 |

## 对"美国实际利率"研究的含义

- **样本连续性**：研究 2008 年后的实际利率必须处理 ZLB 断点，本文提供标准解法
- 与 [[Kiley_2020_详细笔记|Kiley]]、[[Lubik_Matthes_2015_详细笔记|LM]] 构成三大替代估计，可做四序列对比图
- 影子利率本身可作为货币政策立场变量进入回归

## 理论定位

- **学术地位**：影子利率建模与 r\* 估计的结合，方法性强
- **与前人关系**：承 Wu-Xia 影子利率传统，嫁接 r\* 趋势分解
- **局限性**：纯统计模型，结构解释有限；影子利率本身也有估计争议

## 相关笔记

- [[Laubach_Williams_2003_详细笔记|Laubach & Williams (2003)]]
- [[Kiley_2020_详细笔记|Kiley (2020)]]
- [[Laubach_Williams_2016_Redux_详细笔记|LW (2016) ZLB 常态化论断]]

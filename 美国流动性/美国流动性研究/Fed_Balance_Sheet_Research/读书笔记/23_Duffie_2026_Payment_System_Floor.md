---
title: Duffie (2026) The Payment System Floor for the Fed's Balance Sheet
authors:
  - Darrell Duffie
year: 2026
journal: Brookings Papers on Economic Activity（Spring 2026）
created: 2026-08-06
tags:
  - 文献笔记
  - 美国流动性
  - 支付系统
  - 扩表下限
  - 改革派
status: 已获取 PDF
---

# 一句话总结

> [!abstract]
> 真正给美联储资产负债表设下限的**不是利率走廊的技术需要，而是支付系统的结算需求**——联储其实已经在"跟着支付系统扩表"；因此应做四件事：用**临时公开市场操作**对冲支付波动、把 **Fedwire 流动性节省机制（LSM）** 改造成学 CHAPS 的样子（UG 估算可省 $100–125B）、**改革流动性监管**、并引入**准备金分层付息**。

原文：[[Duffie_2026_Payment_System_Floor_BPEA.pdf|原文 PDF]]

---

## 研究问题与核心发现

> **研究问题**
> 如果缩表的下限不是"利率控制需要多少准备金"，而是"支付系统需要多少准备金"，美联储的表到底能缩到多小、又该如何设计工具？

### 核心发现

- **支付结算需求是真正下限**：Fedwire 大额支付的日内流动性需求，才是表无法无限制缩小的物理约束。
- **联储已在跟着支付扩表**：历史扩表节奏在很大程度上是被支付与结算需求推着走，而非纯粹货币政策选择。
- **四处方**：
  1. **临时 OMO** 对冲支付引起的准备金波动；
  2. **Fedwire LSM（流动性节省机制）改造**，学英国 CHAPS——UG（Ulrich & G?）估算可节省 **$100–125B** 流动性；
  3. **改革流动性监管**（LCR/HQLA 认定与贴现窗口、SRF 配合）；
  4. **准备金分层付息**（tiered remuneration），降低银行囤积准备金的激励。
- **姊妹篇机制设计**：与 Duffie, Singh & Wang (2026) 关于 LSM 机制设计的论文配套。

> **关键信息**
> 这是改革派在"缩表之争"中的**施工图**：把下限从利率控制重新锚定到支付系统，然后给出可计算节支的具体工具。实证起点是 [[21_Copeland_Duffie_Yang_2021_Reserves_Not_So_Ample|CDY 2021]] 对批发融资与支付流的发现，理论对话是 [[25_Kumhof_2025_Geometric_Thresholds|Kumhof 阈值模型]]。

---

## 理论框架

- **支付系统地板**：表的下限由结算需求决定，利率走廊只是表象；支付需求是硬约束，利率控制是软约束。
- **流动性节省机制（LSM）**：通过支付排队、轧差与算法撮合，让同样规模的支付用更少的准备金完成（CHAPS 经验）。
- **工具组合而非单一工具**：临时 OMO、LSM、监管改革、分层付息四者协同，才能把"地板"压低。

---

## 实证方法

- 支付系统数据：Fedwire 支付流的日内与时序特征，识别结算需求对准备金的硬约束。
- 跨国比较：英国 CHAPS 的 LSM 经验作为改造 Fedwire 的参照。
- 定量估算：引用 UG 对 LSM 节省 $100–125B 流动性的测算。
- 政策反事实：四处方组合下"可缩表空间"的情景分析。

---

## 关键概念速查

| 概念 | 含义 |
| ---- | ---- |
| 支付系统地板 | 支付结算需求给资产负债表规模设的真正下限 |
| LSM（流动性节省机制） | 支付排队/轧差/撮合算法，用更少准备金完成同样支付 |
| CHAPS | 英国大额支付系统，其 LSM 为 Fedwire 改造模板 |
| 准备金分层付息 | 对不同层级准备金差别付息，降低囤准备金激励 |
| 临时 OMO | 对冲支付波动的临时性公开市场操作（与永久扩表相对） |

---

## 对"美联储资产负债表"研究的含义

- **重新定义缩表下限**：把"充裕准备金"的锚从利率控制移到支付结算，使缩表目标函数更清晰。
- **给出可计算的改革收益**：LSM 改造 $100–125B 的节支，为改革派提供量化论据。
- **区分工具职能**：临时 OMO 对付波动、永久扩表对付趋势，二者不可混用——回应 [[16_Waller_2025_Balance_Principles|Waller]] 与 [[11_Logan_2025_Efficient_Balance_Sheet|Logan]] 对工具边界的讨论。
- **分层付息作为减量工具**：与 [[08_Miran_2025_Balance_Sheet_Design|Miran]] 的监管松绑同属"需求侧减量"路线。

---

## 理论定位

- **范式**：政策设计 + 支付系统微观结构（BPEA 政策论文）。
- **贡献**：把缩表下限的分析单位从"利率走廊"换成"支付系统"，并把改革主张工具化、定量化。
- **与前人关系**：实证起点 [[21_Copeland_Duffie_Yang_2021_Reserves_Not_So_Ample|CDY 2021]]；同系列 [[07_Duffie_2025_Quantitative_Discomfort|Duffie 2025 量的不适]]；姊妹篇 Duffie, Singh & Wang (2026) 的 LSM 机制设计。
- **对后续**：为改革派提供施工蓝图，与 [[33_Bernanke_2025_Balance_Sheet_Future|Bernanke]]、[[17_Liang_2025_Evolution_Principles|Liang]] 的"维持充裕框架"路线正面交锋。

---

## 局限与待跟进问题

- LSM 改造的 $100–125B 节支是**模型估算**，实际取决于 Fedwire 技术可行性与银行采纳。
- 分层付息需国会授权，政治可行性存疑。
- 四处方的实施顺序与彼此交互（如监管改革是否先于 LSM）未完全展开。
- 待跟进：Duffie, Singh & Wang (2026) 的 LSM 机制设计细节；联储对 Fedwire 改造的官方回应。

---

## 相关笔记

- [[21_Copeland_Duffie_Yang_2021_Reserves_Not_So_Ample|CDY 2021 准备金并不充裕]]
- [[07_Duffie_2025_Quantitative_Discomfort|Duffie 2025 量的不适]]
- [[25_Kumhof_2025_Geometric_Thresholds|Kumhof 2025 几何阈值]]
- [[08_Miran_2025_Balance_Sheet_Design|Miran 2025 资产负债表设计]]
- [[11_Logan_2025_Efficient_Balance_Sheet|Logan 2025 高效资产负债表]]
- [[MOC_美联储资产负债表研究|研究总览 MOC]]

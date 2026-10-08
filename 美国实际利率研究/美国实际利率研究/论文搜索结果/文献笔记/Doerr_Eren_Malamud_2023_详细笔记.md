---
title: "Money Market Funds and the Pricing of Near-Money Assets（货币基金与近货币资产定价）"
authors: [Sebastian Doerr, Egemen Eren, Semyon Malamud]
year: 2023
venue: "BIS Working Paper No. 1096"
category: G-货币市场与近货币资产
tags: [MMF, T-bill, repo, ON-RRP, 流动性溢价, 市场势力, 近货币资产]
---

# Money Market Funds and the Pricing of Near-Money Assets — 详细笔记

> [!abstract] 一句话总结
> MMF 作为 T-bill 和 repo 市场的大玩家，与银行和彼此**策略性互动**：MMF 在 repo 市场收取更高利率 → repo 需求下降 → 剩余现金涌入 T-bill 市场 → **T-bill 利率下降、其流动性溢价上升**。理论预测的定价联动被工具变量实证确认；MMF 在设定 repo 利率时内化其对 T-bill 市场的价格冲击，并在国债流动性差时转向美联储的 RRP。

## 研究问题

T-bill（全球无风险资产）与 repo（短端融资核心，正在取代 LIBOR 成为基准）这两个"近货币资产"市场如何被共同的边际投资者——MMF——联动定价？

## 理论机制

1. MMF 在 repo 市场有市场势力（对银行借款人定价）。
2. repo 利率定得高 → 银行借款需求下降 → MMF 手里出现"剩余现金"。
3. 剩余现金必须投向 T-bill → MMF 在 T-bill 市场有价格冲击 → **T-bill 利率被压低、流动性溢价上升**。
4. 美联储 ON RRP 工具的存在缓解但不消除这一联动（RRP 提供了利率下限的替代去向）。
5. MMF 是策略性的：设定 repo 利率时**内化**自己对 T-bill 价格的影响；国债市场流动性低时把组合向美联储 repo 倾斜。

## 实证

- 用理论指导构造**工具变量**确认因果：MMF 配置到 T-bill 的现金增加 → T-bill 利率下降、流动性溢价上升，且经济上显著。
- 数据：持仓级别（holding-level）细粒度数据，逐一检验机制。

## 政策含义（原文强调）

1. **货币政策传导**：MMF 行为影响常规与非常规货币政策向短端利率的传导。
2. **基准利率稳健性**：repo 基准利率（SOFR 类）取代 LIBOR 后，其定价受 MMF 市场势力影响。
3. **政府债务发行**：T-bill 发行节奏与 MMF 现金配置互动，影响财政融资成本。

## 对"美国实际利率"研究的含义

1. **"近货币资产溢价"的微观结构**：美债便利性溢价（[[Krishnamurthy_VissingJorgensen_2012_详细笔记|KVJ 2012]]）在短端由 MMF 的策略行为具体生成——安全资产溢价不只是宏观供需，还有市场微观结构。
2. **短端实际利率的下限结构**：ON RRP 成为短端利率的有效下限，塑造利率走廊形态——研究实际利率期限结构时短端锚的制度细节不可忽略。
3. **现金 vs 久期**：再次印证 MMF 资金是流动性需求而非久期需求（与 [[Aldasoro_Doerr_2023_详细笔记]] 互为姊妹篇）。

## 局限

- 聚焦美国短端，不直接定价长端实际利率。
- IV 识别依赖模型结构假设。

## 相关笔记

- [[Aldasoro_Doerr_2023_详细笔记]]
- [[Krishnamurthy_VissingJorgensen_2012_详细笔记]]
- [[GHV_2024_详细笔记]]

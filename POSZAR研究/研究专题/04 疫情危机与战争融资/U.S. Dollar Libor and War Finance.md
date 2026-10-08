---
tags:
  - Pozsar
  - 疫情危机
  - Libor
日期: 2020-04
---

# U.S. Dollar Libor and War Finance（GMN#29，美元 Libor 与战争融资）

> [!quote] 原文链接
> [[U.S. Dollar Libor and War Finance.pdf]]

## 摘要

GMN#29，2020 年 4 月 14 日，危机工具全面铺开后的定价解剖。核心问题：美联储把**有担保**工具全部定在 25bp 平价/加价（贴现窗口、PDCF、回购便利、FIMA、互换额度），唯独 **CPFF/MMLF 定在 OIS+110/200bp**——为什么对无担保市场如此"苛刻"？ Pozsar 给出两种解读（马基雅维利版与白芝浩版），并借此揭示美联储的"心理地图"：**优先货基是外围机构、CP 是外围市场、Libor 是过去的遗迹；政府货基是核心机构、repo 与 FX swap 是核心市场、SOFR 是未来**。然后给出 Libor-OIS 收窄的两步路线图（4 月底到 75bp、5 月继续）——用"蛋糕分层"模型解释为什么不动 CPFF 价格也能治好 CP 市场。

## 核心论点详解

### 1. CPFF 定价之谜：两种解读

- **马基雅维利版**：美联储在给基准利率改革递话——Libor 将死、SOFR 为王。过去财政部和企业司库嫌 SOFR 关联债有利率尖峰风险；现在美联储展示了用低价回购工具管制 SOFR 的意愿与能力，却只在 100bp 之外才救无担保市场。**借款人自己选择：压力时按低 SOFR+利差借，还是按高 Libor+利差借。SOFR 将带着更强壮的腿走出这场危机。**
- **白芝浩版**：危机放贷的铁律是"对有偿付能力者、凭良好抵押品、以惩罚性利率自由放贷"。美联储的核心业务永远有抵押：贴现窗口 25bp（有抵押）、PDCF 25bp（有抵押）、回购便利 IOR（国债抵押）、FIMA IOR+25（国债抵押）、互换额度 OIS+25（本币抵押）。"危机中规则在核心灵活、在外围僵硬；**这场危机里，惩罚利率被换成了对核心的'友好利率'**——疫情下对核心低息放贷没有道德风险问题。"
- 修补办法现成的：财政部加大第一损失缓冲，CPFF 降到 OIS+25。**美联储没这么做，本身就是信息**——"市场与其争辩价格，不如听听美联储用定价在说什么。"

### 2. 蛋糕模型与 Libor-OIS 的收窄路径

- 美元融资市场是块蛋糕：**底层 = FF/OIS 曲线 + GC repo 曲线；顶层 = 各主要货币的 FX swap 隐含曲线；Libor（无担保利率）夹在中间**。Libor 冲上顶层并持续停留是不正常的；
- **只要互换额度压低顶层，Libor 无论 CPFF 价格如何都会回落**：CP/Libor 高于 FX swap 隐含收益率 → Libor-Libor 基差转正 → 对 Libor 报价行来说，**在欧洲日元瑞郎英镑融资再换成美元，比在岸发 CP 便宜** → 套利流入直到基差转负；
- 当时欧/镑 Libor-OIS 更宽、OIS-OIS 基差再度走负——这些辖区的银行还有约 40bp 可榨——**Libor-OIS 4 月底可到 75bp，即比 CPFF 价格低 40bp**。不动 CPFF 也能治好 CP 市场。

### 3. 资产负债表松绑与 OIS-OIS 基差（Part II）

5 月继续收窄的动力来自政策组合的协同：

- **互换额度已近 4000 亿**——外国银行由此少占用交易商资产负债表与风险资本，腾出的表可服务非银的 FX swap 需求；
- **Crapo 法案 402 条**（托管行豁免）与**国债/回购暂免 SLR**——大行表空间松绑；
- **FIMA 定价调整**——外国官方变现国债不再非要抛售；
- 合力 → 更多美元经 FX swap 流向非银 → OIS-OIS 基差走浅 → Libor-OIS 二段收窄。

### 4. "战争融资"的含义

标题框架：这是一场对病毒的战争，融资安排遵循战时逻辑——**核心资产（国债）、核心机构（银行与交易商）、核心市场（repo 与 FX swap）全部兜底**；外围（CP、优先货基、Libor 体系）半兜底。隐含地，新兴市场也被兜底——只要其央行有足够国债可 privately repo 或走 FIMA。战时财政主导下，利率结构服务于**国家资产负债表的无摩擦滚动**。

## 关键数据卡

| 工具 | 定价 | 抵押 |
|---|---|---|
| 贴现窗口 / PDCF | 25bp | 有 |
| 回购便利 / FIMA | IOR / IOR+25 | 国债 |
| 互换额度 | OIS+25 | 本币 |
| **CPFF / MMLF** | **OIS+110/200** | **无** |
| 互换额度用量 | ~4000 亿 |

## 核心概念

- **核心-外围定价**：货币层级在危机定价中的显形。
- **蛋糕模型**：Libor 夹在 OIS/repo 底与 FX swap 顶之间——压顶即治中。
- **定价即沟通**：工具价格是美联储的政策宣言。
- **战争融资范式**：国家融资优先，利率结构从属于国家资产负债表。

## 金句摘录

> "Money is hierarchical… and during crises, rules are flexible at the core and rigid at the periphery."

> "Instead of arguing for lower rates on the CPFF and the MMLF, maybe the market should reflect and listen to what the Fed is trying to say with its pricing."

> "SOFR may come out of this crisis with stronger legs."

## 关联阅读

- [[Lombard Street and Pandemics]] —— 四点清单的前篇
- [[U.S. Dollar Libor and Swap Line Rollovers]] —— 互换额度的滚动问题
- [[Singularity]] —— 平价的最终重建
- [[What Excess Reserves？]] —— Libor 伪概念的伏笔回收

## 阅读价值

教你"读价格如读政策"：一组工具定价的差异，就是美联储对整个利率体系未来的完整表态。蛋糕模型也是做基差/Libor 交易最实用的直觉框架。

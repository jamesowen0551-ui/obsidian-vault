---
tags:
  - Pozsar
  - 欧洲美元
  - 基差
日期: 2018-04
---

# Beyond the Outer Rim（GMN#13，外环之外）

> [!quote] 原文链接
> [[Beyond the Outer Rim.pdf]]

## 摘要

GMN#13，把融资市场的"层级地图"再向外推一层：FX swap 是融资市场的"外环"（outer rim），而**股指期货是"外环之外"**——它和 FX swap 一样是全球美元融资市场的一部分，银行司库在两个品种之间**动态调配资本**。由此得到一个反直觉的联动规则：**"股市跌 → 跨货币基差收窄；股市涨 → Libor-OIS 走阔"**。2018 年初基差在 Libor-OIS 走阔背景下反常收窄的谜题，本篇给出三个供给侧解释（回流式防御性过剩、股市抛售式意外过剩、BEAT 式机会主义过剩）+ 一个需求侧解释（对冲成本侵蚀外需）。

## 核心论点详解

### 1. 融资市场的层级与外环之外

- 层级（从低到高）：**OIS → 担保 repo → 无担保 Libor → FX swap**。近年最赚钱的货币交易：在层级低位筹资、到外环融出；典型借款人：负利率辖区想对冲买美债的实钱账户。
- **股指期货同理**：S&P 期货隐含收益率同样对 Libor 有溢价——**股指期货基差**。做市结构也相同：匹配簿收双边价差，但**市场很少靠匹配簿出清**——失衡由投机簿（后 Basel III 时代 = 银行司库）吸收。
- 两类基差的做市都需要**边际融资**：FX swap 要筹美元去外环放贷；股指期货要对冲客户多头——**做空期货 + 融资买入现货股票**。而且融资是**预先备好**的（pre-fund），不是用时才抢。

### 2. 股市抛售 → 过剩 → 基差收窄的传导链

2018 年 3 月股市动荡后：

1. 客户做多股指期货的意愿下降 → 银行为"预算内空头"预备的融资用不上了 → **期货台过剩**；
2. 客户减多头 → 银行为保持中性**卖出现货股票** → 手里变成现金 → **又一层过剩**；
3. 组织文化决定去向：资金台/repo/FX swap/期货台"亲如一家、并排而坐"的银行，过剩现金立刻转去 FX swap 台（还有正 carry 的地方）——**"从进攻切换到防守，目标不是利润最大化而是亏损最小化"**；
4. 股指期货隐含收益率崩盘跌穿 Libor 的**同一天**，跨货币基差开始急剧收窄。

### 3. 基差异常收窄的完整归因（3+1）

供给侧三个"过剩"：
- **防御性过剩**（回流）：外国银行失去 1–3 年期债的专属买家（企业司库），提前融资保 LCR/NSFR，过剩现金投 FX swap；杠铃式发行（3 个月内 + 3 年以上），**大部分 6 月前到期**；
- **意外过剩**（股市）：如上；
- **机会主义过剩**（BEAT）：见 [[BEAT，FRA-OIS and the Cross-Currency Basis]]。

需求侧：Libor-OIS 走阔使外国买家对冲后美债/MBS/IG 的 carry **掉了约 60bp** → 日本 2018 年头两个月**抛售 500 亿美债**，日本小行开始削减美元贷款簿记——对冲需求本身在退潮（也会让基差收窄）。

- 只有等三重过剩消退，才能看清需求退潮的真实贡献。 Pozsar 强调这与 2017 年 12 月 Libor-OIS 异动（某些加系银行大期货台狂抢无担保资金）的呼应——"**雷达扫得越宽，下次被 left field 飞来的球砸中的概率越低**"。

## 关键数据卡

| 指标 | 数值 |
|---|---|
| 对冲后 carry 下降 | ~60bp（Libor-OIS 走阔所致） |
| 日本抛售美债（2018 前两月） | ~500 亿 |
| 联动规则 | 股跌→基差收窄；股涨→Libor-OIS 走阔 |

## 核心概念

- **外环之外**：股指期货作为全球美元融资市场的外延板块。
- **股指期货基差**：与跨货币基差平行的新概念。
- **三种过剩**：defensive / unforeseen / opportunistic overfunding。
- **股-基差联动**：Basel III 后首次股市大转折提供的实证样本。

## 金句摘录

> "The buck does not stop at the outer rim…."

> "If stocks fall, the cross-currency basis tightens."

> "When you are suddenly overfunded and bases move against you, your aim is not to maximize profits but to minimize your losses."

## 关联阅读

- [[From Exorbitant Privilege to Existential Trilemma]] —— outer rim 概念的出处
- [[BEAT，FRA-OIS and the Cross-Currency Basis]] —— 三重过剩之三
- [[Repatriation, the Echo-Taper and the €$ Basis]] —— 三重过剩之一
- [[Lost in Transmission]] —— 对冲成本侵蚀需求的后篇

## 阅读价值

 Pozsar 式"跨市场管道学"的极致：谁能想到标普期货台的资金预算会影响 $/¥ 基差？这篇教你把**银行的内部资金转移定价（FTP）与台间关系**当作市场变量来分析。

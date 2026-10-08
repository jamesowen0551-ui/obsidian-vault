---
tags:
  - Pozsar
  - 货币市场
  - 缩表
日期: 2019-05
---

# Collateral Supply and o/n Rates（GMN#22，抵押品供给与隔夜利率）

> [!quote] 原文链接
> [[Collateral Supply and on Rates.pdf]]

## 摘要

GMN#22，七篇短文 + 逐时流程图 + 50 页幻灯片组成的重磅研究，把"缩表（taper）"从美联储口径的"简单资产互换"还原为一部**逐小时、逐账户的清算纪录片**。开篇引汉密尔顿并以"看油漆干 ≠ 理解油漆干燥的化学"立论：国债是颜料、准备金是溶剂、日内流动性需求是粘合剂——**颜料太多溶剂太少，油漆就涂不开：GC repo 利率出区间、把联邦基金利率一起拽上去**。核心结论：①2018 年 10 月曲线倒挂引发"买家罢工"，**缩表实际上迫使财政部有 3000 亿美元供给要靠 o/n GC repo 市场隔夜融资**；②体系可自由出借的准备金"free float"只剩 **2000 亿**——**缩表应该立刻停止**；③**o/n GC repo 才是体系的核心融资利率**，FF 利率只是滞后、低 beta 的外围指标，应被降级。（四个月后，2019 年 9 月回购危机兑现。）

## 核心论点详解

### Part I–II：缩表的逐小时纪录片

美联储的官方叙事：缩表 = 准备金换债券，市场"魔法般"出清（Pozsar 嘲讽为 "MAGIC by Arrow-Debreau"）。现实的日内流程：

1. **早 9:00**：一级交易商承销国债，耗尽其在 BoNY 的清算账户；财政部发债、TGA 增加；
2. BoNY 从自己在美联储的准备金账户汇款完成结算——**交易商没有准备金账户，一切经 BoNY**（JPM 被 Basel III 的 G-SIB 附加资本逼出了交易商清算业务，BoNY 成唯一清算行——单点集中度本身就是故事）；
3. **9:30** 财政部赎回美联储持有的到期券；**美联储双侧缩表，"taper accomplished"**——官方叙事到此为止，但流程继续；
4. **下午 3:30 前**交易商卖出债券回补清算账户——买家（银行/非银）付款通过银行间准备金流动完成；
5. 若当天没卖掉 → BoNY 和美联储的**日内透支（daylight overdraft）**帮体系出清——缩表被"日内融资"而非"筹资"。
- 奇数步是证券流、偶数步是准备金流；证券增加、准备金销毁；**BoNY 无所不在**。

### Part III：倒挂与买家罢工

- 一级交易商受 1988 年《一级交易商法》约束，"hell or high water" 必须承销；
- 2018Q4 起，**国债收益率曲线相对所有相关融资成本（repo、Libor、FX 对冲成本）倒挂**——边际上买国债不再划算 → 终极买家罢工 → **交易商库存膨胀**；
- 交易商不是银行，边际融资靠 repo → 库存融资需求把 **o/n repo 利率顶出目标区间上沿**；
- 大银行没有直接买多少国债，而是通过 o/n GC repo 从交易商处"reversed in"——**Scenario 4，美联储框架里不存在的场景**；
- 结论：**缩表迫使财政部把 3000 亿美元供给放到 o/n GC repo 市场隔夜滚动融资**。

### Part IV–V：Free Float 与"缩表应停止"

- 把缩表供给与财政赤字供给合并考察准备金/抵押品平衡：**可出借到 o/n GC repo 市场的准备金 free float 只剩 2000 亿**；
- 缩表与赤字从第一天起就**时机糟糕**：它们恰好在体系外超额准备金（货基等）耗尽之后开始，压力全部落在体系内银行准备金上；
- "Taper should stop now."

### Part VI–VII：核心利率的加冕与降级

- **o/n GC repo 利率是体系的核心融资利率**——它直接定价抵押品供给压力；
- **FF 利率是滞后、低 beta 的外围指标**（FHLB 出借的 captive 结构使其反应迟钝），应被降级；
- 呼应 [[What Excess Reserves？]] 与 [[QE, Basel III and the Fed’s New Target Rate]] 的政策目标之争，给出最终答案。

## 关键数据卡

| 指标 | 数值 |
|---|---|
| 缩表迫使隔夜滚动融资的国债供给 | ~3000 亿 |
| 准备金 free float | ~2000 亿 → "缩表应停止" |
| 买家罢工起点 | 2018-10 曲线倒挂 |
| 交易商清算行 | 仅 BoNY 一家（JPM 被 G-SIB 附加挤出） |

## 核心概念

- **油漆化学**：颜料（国债）/溶剂（准备金）/粘合剂（日内流动性）——抵押品供给分析的直觉模型。
- **Scenario 4**：银行经 repo 间接持有缩表释放的国债——官方框架的盲区。
- **BoNY 单点**：全体系缩表清算流经一家银行。
- **核心 vs 外围利率**：GC repo 加冕、FF 降级。

## 金句摘录

> "Watching paint dry is not the same as understanding the chemistry of how paint dries…"

> "Markets 'magically' clear… – Scenarios the Fed's framework didn't consider."

> "The o/n GC repo rate is the system's core funding rate and the o/n fed funds rate is a lagging and low-beta indicator."

## 关联阅读

- [[Taper and the “Mix-Capacity-Target” Trinity]] —— 缩表框架的前篇
- [[It’s Time to Use the Exorbitant Privilege]] —— 同期 foreign RRP 批评
- [[The Revenge of the Plumbing]] / [[Countdown to QE4？]] —— 危机与救火
- [[案例研究 · 2019回购危机预言兑现清单]] —— 本篇是清单上的"撞墙前最后警报"

## 阅读价值

全套笔记中**交易台颗粒度最细**的一篇：读完你会知道一笔缩表相关的国债拍卖在 9:00–15:30 之间流经哪些账户、谁在几点出钱。这是理解 2019 年 9 月"为什么回购利率能飙到 10%"的微观解剖课。

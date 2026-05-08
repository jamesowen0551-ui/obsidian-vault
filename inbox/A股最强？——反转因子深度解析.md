---
title: A股最强？——反转因子深度解析
source: https://zhuanlan.zhihu.com/p/386661895
author:
  - "[[卡方研究院科技改变交易]]"
published:
created: 2026-05-06
description: 前言：在股票交易中，风险与机遇是并存的，有增必有跌，存在着一定的震荡。有学者发现，一定时间段内表现最佳的股票，在接下来的时间中可能变成表现最差，也就是说股票市场中普遍存在动量反转效应，表现为短期反转…
tags:
  - 股债相关性
  - 反转因子
---
77 人赞同了该文章

前言：在股票交易中，风险与机遇是并存的，有增必有跌，存在着一定的震荡。有学者发现，一定时间段内表现最佳的股票，在接下来的时间中可能变成表现最差，也就是说股票市场中普遍存在 [动量反转效应](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E5%8A%A8%E9%87%8F%E5%8F%8D%E8%BD%AC%E6%95%88%E5%BA%94&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLliqjph4_lj43ovazmlYjlupQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.geYpb7zkYyRhgliKWi5syopFEkMfKSEcALKAGmdsSjw&zhida_source=entity) ，表现为短期反转、中期动量和长期反转的现象。那么反转因子是如何产生的？又存在着哪些性质呢？

本文将从传统金融学和 [行为金融学](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E8%A1%8C%E4%B8%BA%E9%87%91%E8%9E%8D%E5%AD%A6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLooYzkuLrph5Hono3lraYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.vGO_NIgjHahYkJFjIpFlauIdJBpC5ysaeW-GJ9MnG1A&zhida_source=entity) 的角度分析反转因子的来源，并在股市行情等情境下分析反转因子的特点。本文还针对A股对传统杠杆因子进行分析，构造出更有效的高频/ [结构化反转因子](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E7%BB%93%E6%9E%84%E5%8C%96%E5%8F%8D%E8%BD%AC%E5%9B%A0%E5%AD%90&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLnu5PmnoTljJblj43ovazlm6DlrZAiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.zot1efVmAJGXMe3WAAWqwzJQa7t0dTyHb5ryGm7xU2s&zhida_source=entity) 。

---

## 第一部分：反转因子的定义

**1.反转因子的发现**

1985年，De Bondt与Thaler对1926年～1982年期间在纽约证券交易所上市的股票进行研究后发现，过去5年中表现最好的35只股票（赢家组合）和表现最差的35只股票（输家组合）的收益在随后的3年中发生了反转。以5年为形成期，根据形成期的股票收益作为基准构建赢家组合和输家组合，然后分别持有3年，可以发现输家组合的平均收益要大幅高于赢家组合。他们称该现象为长期反转效应（long-term reversal）。1990年，Jegadeesh和Lehmann研究了美国股票市场后发现，反转效应不仅存在于长期，在期限小于一个月的投资组合中也能发现，即短期反转效应（short-term reversal）。自此，反转因子正式进入大众视野。

**2.反转效应的来源分析**

在传统金融学的看法下，动量反转效应是由于数据挖掘中的一些偏差和传递信息不及时导致的结果。而这种误差导致的动量反转效应并不可靠：如果去掉这些偏差，动量反转效应带来的超额收益其实并不存在。因此， [有效市场假说](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E6%9C%89%E6%95%88%E5%B8%82%E5%9C%BA%E5%81%87%E8%AF%B4&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLmnInmlYjluILlnLrlgYfor7QiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.eGZ2_6-jl2dJZEnZVT5m6FpDMxKOKz0TtwobgeBhinY&zhida_source=entity) 认为，在强式有效的市场中，股票价格能根据及时公开的信息快速进行调整，股价不会被高估或低估，不存在市场信息传递的滞后性。这样投资者如果利用技术分析等方法来构建股票组合进行投资，只能获得与市场平均收益相当的正常收益，不会收到反转因子带来的影响而带来超额收益。

而在行为金融学中，研究员们从投资者的微观行为特征角度来对动量反转效应进行分析，他们认为动量反转效应是投资者的心理和行为带来的影响。投资者们并非完全理性投资者，他们的投资行为中存在很多心理学和行为学上的偏差。其中，可能的行为偏差主要有：1.过度自信：投资者高估自己的能力，低估自己的犯错的可能性。2.[处置效应](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E5%A4%84%E7%BD%AE%E6%95%88%E5%BA%94&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLlpITnva7mlYjlupQiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.4mVDA_eTZH873RWGb3PUyfJh3pO7LiqnXBDLVhGRJnc&zhida_source=entity) ：投资者倾向于卖出自己盈利的股票和持有亏损的股票。3.拇指法则：投资者在做决策时容易忽略其认为不重要的因素，凭借直觉或者经验做出决定。投资者们的这些主观行为也会直接间接加剧动量反转效应。

**3.反转因子的特点**

全球股市中普遍存在动量效应，表现为短期反转、中期动量和长期反转的现象；而中国A股市场则在短期、中期、长期均有不同程度的反转效应，且在中短期表现得尤为显著。在A股中，常见的反转因子主要包括收益率、换手率、流动性冲击、特质波动率等。这些反转因子的内在逻辑均与市场交易行为有关，当月次月的收益也往往具有显著的反转特征。除了这些特点之外，反转因子还有一些别的共性。

- **在下跌市中，反转效应更强**

因为反转效应源于投资者们在前期的过度反应，而在下跌市中追涨杀跌情绪更为聚集，过度反应越明显，从而反转因子更为有效。根据图1我们可以看出，在全A股中，在市场上涨时，反转效应的平均月收益仅为0.69%，而在下跌市中，反转效应的平均月收益可以达到3.42%，月胜率为78%，明显高于上涨市。综合来看，反转效应在下跌市中的表现显著强于上涨市。

![](https://pic3.zhimg.com/v2-7855c994c06c19b02ca92f3d20868654_1440w.png)

图1：市场涨跌与反转效应（2015-12 全A股） 来源：Wind，海通证券研究所

- **在上涨市中，反转因子的空头效应显著强于多头**

从横截面来看，整体而言，涨幅最大的股票与市场等权的偏离幅度要大于跌幅最大的股票与市场的偏离幅度，从而导致反转因子的空头效应强于多头效应。但这种现象与市场状态密切相关：下跌市中，追涨、杀跌情绪都很强，且无显著区别，此时，多头效应和空头效应都很明显，相差不大；而在上涨市中，跌幅最大的股票后期相对于全市场等权并无超额收益，空头效应明显强于多头效应。如图1，在下跌市中，多头效应的平均月收益为1.64%，空头效应的平均月收益为1.78％，两者相差不大；而在上涨市中，空头效应的平均月收益达到1.78％，远大于多头效应的-0.29%。

做空机制的缺失，是导致多空效应差异的潜在原因。投资者利用反转效应，买入超跌股票获取利益，却无法在不持有仓底的前提下，反向做空高估股票。

![](https://pic1.zhimg.com/v2-5af938ac1fcf9ab1f3d6022fec4080ee_1440w.jpg)

图2：套利行为的增加熨平多头效应 来源：海通证券研究所

- **收益分化度越大，反转效应更强**

股票之间的收益分化度越大，过度反应越强，后期的反转效应也应越强。这里，以当月涨幅最高的1/10 股票与跌幅最大的1/10 股票之间的等权收益差来反应当月的离散度；该指标越大，反应当期股票之间的差异越明显。

下图统计了观察期极端组合的收益差与后期反转效应之间的关系；其中，反转效应是指前期跌幅最大的股票与涨幅最大的股票，在后一个月的多空收益差。从中可看出，随着收益离散度逐渐增加，后月反转效应逐渐增大。特别地，当前期极端组合收益差大于50%时，后一个月反转因子的平均收益率为9.24%，明显高于其他情况。

![](https://picx.zhimg.com/v2-dbe607fe976e2aa6ccb3821bcdc8ce0d_1440w.jpg)

图3：观察期收益差与后期反转收益（2015-12 全A股） 来源：Wind，海通证券研究所

---

## 第二部分：传统反转因子

**1.传统反转因子的构建**

市场信息传递的滞后性以及投资者们的过度反应是很难避免的，也因此产生了投资机会，反转因子的构建正是基于反转效应带来的可套利空间。

以21天收益率构建的基础反转因子是目前一种常用的反转因子，有一定的选股能力，但波动较大，回撤年份多。基础反转因子的计算方式为过去21天收益率，本质为 21天日度累计涨跌幅，表达式如下：可以看出，基础反转因子为综合过去21天价格变化信息，给出其对数的等权加和。

![](https://pic4.zhimg.com/v2-64075f25a254657f6927dff9a4c90fdb_1440w.jpg)

**2.传统反转因子在A股中的运用**

图4为全市场和 [中证800](https://zhida.zhihu.com/search?content_id=174055533&content_type=Article&match_order=1&q=%E4%B8%AD%E8%AF%81800&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzgyMjY2NzAsInEiOiLkuK3or4E4MDAiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNzQwNTU1MzMsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.o7ov2CvQ9EJE-FhdvpYU5vGgOXxjnD13Vcy08EziRdc&zhida_source=entity) 的传统反转因子风险指标，我们可以看出：整体来看，传统反转因子在全市场和中证800都能取得一定的超额收益，分组年化收益的变化趋势相对一致，但在中证800的波动性和波动程度更大；从多空收益的角度来看，全市场和中证800的表现相对一致，仅在2013,2014,2017年呈现负收益，其他年份都能带来一定的多空收益。因此，传统反转因子在A股市场中能作为一个优秀的因子来对市场和市场之后的变化进行预测分析，并提高收益。

![](https://pic4.zhimg.com/v2-a5f71b9f262e41ec0346ea9a10c4130d_1440w.jpg)

图4：传统反转因子风险指标 资料来源：天软科技，长江证券研究所

![](https://pic1.zhimg.com/v2-5b0de1822d28792ff98b91ab8e3070a4_1440w.jpg)

图5：过去20日收益率反转因子的多头组合相对基准的超额收益 资料来源：申万宏源研究

![](https://picx.zhimg.com/v2-c1ff06bec3414291f1739498b7e32621_1440w.jpg)

图6：过去20日收益率反转因子的空头组合相对基准的超额收益 资料来源：申万宏源研究

尽管传统反转因子有一定的选股能力，但传统反转因子由于其独有的计算方式，会包含市场行为中的很多噪音。而金融数据的特点就是信噪比极低，有时噪音甚至会覆盖掉原有因子所涵盖的信息，市场包含的很多信息会对传统反转因子造成相当程度上的干扰。事实上，如果我们直接按照做多尾部股票的逻辑去看待反转因子，反转因子就变成了完全意义上的中期动量（相当于做多21交易日内涨幅最9大的股票）。总体来说，传统反转因子是有效的。同时，传统反转因子在计算中很大程度的包含了其他因子的噪音信息（做多尾部股票相当于动量因子也获得了超额收益，甚至超额收益超过了做多头部股票）。此外，从2016年5月开始，多头组合开始出现了负超额收益的现象，并且维持了相当长一段时期，而这并不能从多空组合收益体现出来。与之相反，空头组合持续稳定跑输市场，为多空组合收益的主要来源。这说明了传统反转因子市场风格不稳定，难以作为一个有效因子直接使用。同时行业和学界的相关研究也证明近年来为人尽知的传统反转因子失效程度越来越大。因而传统反转因子需要被改进。

---

## 第三部分：高频/结构化反转因子

正如上述所言，尽管反转因子有一定的选股能力，且能实现一定的年化收益，但传统反转因子的选股波动较大，回撤年份较多，且容易包含其他信息，直接使用并不是十分稳定。因此很多模型都会对反转因子进行改进，用高频数据构建高频反转因子或者将其他因子与反转因子复合，得到更好的因子来对整体市场进行预测判断。长江证券（2019）就试图从高频和结构化角度改造传统因子，给出了以下两种改造方式：

**1.高频反转因子**

在传统反转因子的模型上用更高频的时间段维度进行划分得到高频反转因子，其中period为过去一段时间按一定规则划分时间段的总时间段个数，wi为每个时刻价格变动的加权方式，且因为成交越活跃价格越容易反转，因此高频反转因子的构建方式选择用成交量加权构建：

![](https://picx.zhimg.com/v2-37a3609ccfa5e70b7a1975b93c51ba1f_1440w.png)

一般的高频反转因子我们默认为10分钟频率下的高频反转因子。而在构建高频反转因子的过程中，用到了成交量进行价格变动的加权求和，故新的因子会受到交易层面如流动性和波动率的影响，和基础反转因子相比，高频反转因子与其相关性更高。为了排除其影响，文章对高频反转因子做对换手率因子和波动率因子的中性化处理。

和传统反转因子相比，高频反转因子的选股能力更为优秀，可以获得更高的超额和多空收益，信息比和多空夏普比均有显著提升，截面变化更为稳定，在相对换手率因子和波动率因子中性前后，均有更好表现。

传统反转因子的反转效应几乎完全来自成交量较大的时间段，成交量较小的时间段甚至具有弱动量效应，使用成交量对收益率进行加权放大了前者的影响削弱了后者的影响，这种信息的侧重表达是高频反转因子相对于传统反转因子的优势来源。

![](https://pica.zhimg.com/v2-65ffc9abcb3e2a87168a72e7bddf7ff0_1440w.jpg)

图8：全A股高频反转因子风险指标 资料来源：天软科技，长江证券研究所

**2.结构化反转因子**

动量效应与反转效应两者能相互转换。在实际金融交易的场景中，存在一个成交量的阈值，使得小于该阈值时的价格变动呈现动量效应，大于该阈值时的价格变动呈现反转效应。

因此研究员们根据一段时间内每个时间段股票的成交量，从小到大进行排序，以一个比例为临界点，取小于临界点的时间段作为动量时间段，记为periodmom，大于临界点的时间段作为反转时间段，记为periodrev，其中period为过去一段时间按一定规则划分时间段的总时间段个数，period=periodmom∪ periodrev。

以成交量倒数加权的形式，构建动量时间段反转因子：

![](https://pic3.zhimg.com/v2-8d1dcf1fcf1f26a5c42ac9f9471cb0c6_1440w.png)

以成交量加权的形式，构建反转时间段反转因子：

![](https://pica.zhimg.com/v2-9092fb5c27a15155634284767f17c300_1440w.png)

然后以动量时间段反转因子和反转时间段反转因子合成结构化反转因子：

![](https://pica.zhimg.com/v2-0fdd623f463d26ec30b57a013de00760_1440w.png)

因为小市值组更容易针对价格进行投机套利交易，而大市值则更倾向从公司基本面角度给出定价，故同样水平的成交活跃程度，小市值股票价格不确定性更强，也更容易反转。因此在确定针对动量效应和反转效应的最优阈值时，这个阈值往往与市值有关。故市值较小的话，个股多聚集在反转因子的头部组，即跌的最多的部分，在尾部组即涨的最多的部分比例较少，而市值较大的则相反。

通过结构化反转因子后我们能得到全新的合成因子。总体上看，新的合成因子仍保留着很强的选股能力，与高频反转因子相比，其在全市场中的收益能力稍有上升，获得了年化7.45%的超额收益和28.22%的多空收益，信息比和多空夏普比分别为1.49 和3.33，在中证800中的收益能力同样也有所提升。分年度表现上看，风格中性后该因子全市场中所有年度的多空收益与超额收益均为正值，中证 800中仍然只在2014年出现了较明显的回撤。

![](https://pic2.zhimg.com/v2-7010655fced3436ba48f7f9056240111_1440w.jpg)

图9：结构化因子分年风险指标 资料来源：天软科技，长江证券研究所

结构化反转因子相比于高频反转因子，平均IC有所降低，但因子收益更为稳定，相对换手率因子和波动率因子均有更好表现。

反转类因子收益的核心来源在市场波动，相比基础反转因子，高频反转因子和结构化反转因子更能体现反转效应的核心逻辑。

![](https://pic2.zhimg.com/v2-fc4fb5426fc593863c79ac5dfaa99bb9_1440w.jpg)

图10：波动率与因子收益（单位：%） 资料来源：天软科技，长江证券研究所

---

## 第四部分：总结

事物的发展不会一帆风顺，股票交易也是如此。在股票的交易中，有增必有跌，有趋势就一定会伴随着震荡，而这也带来了机遇，反转因子也因此应运而生。在很多人的观念里，反转因子是A股最强因子，因为这不仅是一个与市场有关的因子，更是个与人性有关的因子。

在我国，证券市场的发展时间相对于发达国家来说较短，大量投资者可能都不够理性，往往会成为趋势投资者，再加上A股市场中政策炒作、概念炒作氛围较浓，导致我国证券市场的动量反转效应比发达国家金融市场更为显著，因此，在我国，反转因子成为了投资者们着重关注的对象。考虑反转，进而获得更高的收益。

如今学者们对反转因子的研究日趋成熟，对反转因子的结构也进行了改造和优化，使得它的应用更贴合如今A股的市场环境，我们也能更好地将反转因子及动量反转效应应用到A股投资中。但无论是高频反转因子还是复合反转因子，都只能体现出反转因子的部分能力，反转因子的能力远不局限于此，还有着更深层的等待着人们的探索和发现。

---

## 参考文献

\[1\] 长江证券.基础因子研究（七）-高频因子（二）：结构化反转因子\[R\] 2019-6-1

\[2\] 长江证券.高频因子（十）：量价关系中的反转微观结构\[R\] 2021-1-28

\[3\] 申万宏源.基于不同市场状态的反转因子择时研究\[R\] 2017-12-15

\[4\] 海通证券.投资者行为与反转效应\[R\] 2016-4

\[5\] 海通证券.反转类因子的逻辑与共性\[R\] 2016-2-24

\[6\] Bryan Kelly, Tobias Moskowitz, Seth Pruitt.Understanding Momentum and Reversal\[A\] 2019-8-16

\[7\] 广发证券.量化风格：个股分化扩大，继续关注反转与估值\[R\] 2021-2-1

\[8\] 林昉.基于多因子模型的 A 股动量反转策略研究\[A\] 2016-11-19

***市场有风险，投资需谨慎。以上陈述仅作为对于历史事件的回顾，不代表对未来的观点，同时不作为任何投资建议。***

发布于 2021-07-05 09:41[阿里云 ×OpenClaw【一键】让 AI 自动帮你干琐事！](https://click.aliyun.com/m/1000409721/?spu=biz%3D0%26ci%3D3661015%26si%3D0be058c7-640d-4c06-b212-d788e740e16c%26ts%3D1778053871%26zid%3D1629)

[

轻松省下一台Mac Mini！

](https://click.aliyun.com/m/1000409721/?spu=biz%3D0%26ci%3D3661015%26si%3D0be058c7-640d-4c06-b212-d788e740e16c%26ts%3D1778053871%26zid%3D1629)
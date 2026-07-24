---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: Untitled
conversation_id: 25472f1e-8350-413b-8aa1-0dc6d8acc7bf
create_time: 2026-07-03T08:53:57.000Z
update_time: 2026-07-03T09:39:55.000Z
---
# Title: 全球流动性指标体系

Created: 2026/07/03 at 16:53:57
Last Updated: 2026/07/03 at 17:39:55
Chat URL: https://claude.ai/chat/25472f1e-8350-413b-8aa1-0dc6d8acc7bf


>[!nexus_user] **User** - 2026/07/03 at 16:53:59
> 我看外资投行经常构建全球流动性指标，可以高频跟踪的，大概由哪些呀
<!-- UID: 019f272f-449d-7a32-b459-74a3f81abdaf -->
>[!nexus_agent] **Assistant** - 2026/07/03 at 16:54:31
> 这是个很实用的研究工具，外资行构建的全球流动性指标（Global Liquidity Index）大致可以拆成几个维度，按数据频率从高到低梳理一下：
>
> **央行资产负债表端（周频/双周频）**
>
> 这是核心骨架。主要跟踪美联储、ECB、BOJ、PBOC四大央行的资产负债表规模，通常用总资产或储备货币口径。美联储的H.4.1报表是周四发布的周频数据，ECB的consolidated financial statement也是周频，BOJ是旬报（每十天），PBOC的资产负债表是月频但可以用MLF/OMO余额做周频近似。有些机构会把SNB、BOE也纳入，构成"G5"或"G6"央行总资产加总。
>
> **跨境美元流动性（日频/周频）**
>
> 这块很关键，主要包括：Fed的隔夜逆回购工具（ON RRP）余额——这个是日频的，余额下降通常意味着流动性从Fed回流到金融体系；Fed与其他央行的美元互换额度（Central Bank Liquidity Swaps）使用量，周频可得；TGA（Treasury General Account）余额，也是日频，财政部在Fed的存款账户，TGA下降等价于向市场注入流动性；银行准备金余额（reserve balances），周频。
>
> **货币市场价格信号（日频）**
>
> 这些是流动性的"价格"维度：SOFR与联邦基金利率的利差、三个月期跨货币基差互换（cross-currency basis swap），尤其是EUR/USD和JPY/USD的basis，basis走阔意味着离岸美元紧缺；FRA-OIS利差反映银行间信用/流动性溢价；商业票据与OIS的利差也常用。
>
> **信用与风险偏好维度（日频）**
>
> 投资级和高收益信用利差（OAS）、金融机构CDS利差、VIX及MOVE指数。这些严格说是流动性的"结果"而非"原因"，但很多指标体系会纳入作为市场流动性的代理变量。
>
> **外汇储备与资本流动（月频，但可做高频近似）**
>
> 新兴市场外汇储备变动（IMF的COFER数据是季频，但各国央行月报可拼），以及EPFR资金流向数据（周频），跟踪跨境组合投资的方向。
>
> **具体怎么合成？**
>
> 常见做法是把上述变量分组，每组内做Z-score标准化后等权或按经济体GDP加权汇总。比较知名的几个：
>
> - **CrossBorder Capital** 的Global Liquidity Index，Michael Howell是这个领域的代表人物，他的框架偏重央行+私人部门信用扩张，覆盖约80个国家
> - **Morgan Stanley** 有一个G4 Central Bank Balance Sheet tracker，比较直观地加总四大央行总资产（美元计价）
> - **BofA** 的Global Liquidity Tracker侧重央行资产负债表+TGA+ON RRP的净效应
> - **Deutsche Bank** 过去也有类似的composite liquidity index，会把价格信号（basis swap等）也纳入
>
> 如果你自己搭一个可操作的版本，最小可行方案大概是：Fed总资产 - TGA - ON RRP（得到"净流动性"）+ ECB总资产 + BOJ总资产（均换算成美元），这个周频可更新，跟风险资产的相关性在过去几年相当显著。再往上加cross-currency basis和EPFR资金流就能做得更丰富一些。要不要我帮你梳理一下数据源和Bloomberg代码？
<!-- UID: 019f272f-449d-7a13-a602-46600e9e568b -->

---
>[!nexus_user] **User** - 2026/07/03 at 17:36:38
> 为啥没用全球m2的
<!-- UID: 019f2756-4129-70bb-b2cc-83d79a29d5d5 -->
>[!nexus_agent] **Assistant** - 2026/07/03 at 17:37:09
> 好问题，全球M2确实是很多人直觉上的第一选择，而且你在社交媒体上看到的那种"全球流动性 vs BTC"的图，底层往往就是全球M2加总。但外资行在构建可操作的高频指标时，倾向于把M2放在次要位置甚至不用，主要有几个原因：
>
> **频率和时滞问题**
>
> M2大多数经济体是月频发布，而且滞后一个月甚至更久。中国的M2月中出，美国的H.6也是月频（而且Fed从2021年起把周频M2给停了），日本是月频滞后一个月，欧元区M3也是月末滞后近一个月。你如果要做交易级别的跟踪，月频数据等你看到的时候市场早就price in了。相比之下央行资产负债表、TGA、ON RRP这些周频甚至日频，信息优势完全不同。
>
> **M2的"噪声"太多**
>
> M2里面混了很多跟金融市场流动性关系不大的东西。比如居民定期存款的搬家——中国这两年M2波动很大程度上是存款在活期、定期、理财之间来回搬，这对利率债定价有意义，但对"全球流动性驱动风险资产"这个逻辑来说是噪声。再比如银行信贷扩张创造的M2，在中国体现为社融派生存款，这更多反映的是实体信用周期而非金融体系的"可投资流动性"。
>
> **估值通道 vs 交易通道**
>
> 这是个比较微妙的区分。M2衡量的是广义货币存量，反映的是经济体内的货币总量，它更像一个中长期的估值锚——你说全球M2持续扩张所以名义资产价格长期上涨，这个叙事是对的。但投行做流动性指标想捕捉的是短期的边际资金供给变化，尤其是能够快速流入金融市场的那部分。央行准备金、ON RRP释放、TGA变动这些直接改变的是金融机构的可用头寸，传导到资产价格几乎没有时滞。M2从变动到影响市场，中间隔了好几层传导。
>
> **汇率换算的扭曲**
>
> 全球M2加总必须换算成同一货币，通常是美元。这意味着当美元走强时，非美经济体的M2按美元计价会机械性缩水，全球M2下降——但这并不代表这些国家的国内流动性收紧了。反过来美元走弱时全球M2被动膨胀。这个汇率噪声在短周期内可以很大，容易产生误导性信号。央行资产负债表也有这个问题，但因为跟踪的变量更少、更直接，研究者更容易做汇率调整或者干脆分开看。
>
> **话虽如此，M2也不是没用**
>
> Michael Howell的CrossBorder Capital框架其实是用M2的，但他做了大量修正——剔除了纯粹由信贷驱动的部分，试图分离出"金融流动性"而非"实体货币"。另外如果你做的是季度或年度维度的大类资产配置，全球M2增速跟风险资产的相关性其实不错，只是不适合做周频的战术跟踪。
>
> 所以本质上是个用途问题：写研报讲长期叙事，全球M2完全可以用；做高频跟踪指导交易仓位，央行资产负债表+资金市场价格信号更实用。你是想搭一个偏交易频率的，还是偏中期配置框架的？
<!-- UID: 019f2756-4129-7c22-946f-41aead2c115e -->

---
>[!nexus_user] **User** - 2026/07/03 at 17:38:47
> Michael Howell的CrossBorder Capital框架其实是用M2的，但他做了大量修正——剔除了纯粹由信贷驱动的部分，试图分离出”金融流动性”而非”实体货币”。他具体咋做到呀
<!-- UID: 019f2758-12cb-76e8-9a86-df3eb0a24f7b -->
>[!nexus_agent] **Assistant** - 2026/07/03 at 17:39:55
> 这个问题比较细，Howell的具体方法论有一部分是公开的（他的书和论文里有），但核心的国别调整系数是CrossBorder Capital的商业机密。让我先搜一下他近年公开披露的方法论细节。
>
> 搜到的内容比较丰富了，综合他的书《Capital Wars》、Substack文章和采访，可以把Howell的方法论拆解如下：
>
> **核心框架：资金流量表（Flow of Funds）恒等式**
>
> Howell的出发点不是M2本身，而是一个会计恒等式：
>
>> **资金来源 = 资金运用**
>> S + ΔFL = I + ΔFA
>
> 其中S是储蓄，ΔFL是金融负债的变动（即金融体系创造的信用/流动性），I是实体投资，ΔFA是金融资产的变动。资金来源（S + ΔFL）驱动资金运用（I + ΔFA），但反过来，抵押品价值上升（ΔFA）也会通过二轮效应进一步扩张信贷，从而放大流动性。这种流动性创造机制的弹性是他框架的核心。
>
> 所以他关心的不是M2这个存量，而是**金融体系资产负债表扩张的增量**——谁在创造信用，通过什么渠道，用什么抵押品。
>
> **三层分解：Official → Financial → Private**
>
> 他的框架把全球流动性分成三类：央行提供的官方流动性（official liquidity）、传统银行和影子银行提供的金融流动性（financial liquidity）、以及包含跨境资本流动在内的私人部门流动性（private sector liquidity）。
>
> 具体来说：
>
> **第一层：影子货币基础（Shadow Monetary Base）**
>
> 这是Howell自己造的概念，大约100万亿美元规模。它不等于传统的货币基础（central bank reserves + currency），而是在传统货币基础之上加入了两个东西：一是离岸美元市场的流动性储备（offshore wholesale funding），二是可用作贷款抵押品的安全资产池（主要是国债）。他认为全球流动性的创造由影子货币基础乘以一个乘数构成，目前这个乘数大约在1.7倍。
>
> 为什么要加入抵押品？因为现在大约80%的借贷都涉及某种形式的抵押品支持，金融体系的流动性扩张本质上是抵押品链条的延伸——你有国债，拿去做repo融资，融到的钱再买资产，新资产又可以做抵押，如此循环。GFC之前，影子银行通过对抵押品进行再质押（rehypothecation），创造了一个人造的额外货币基础。
>
> **第二层：私人部门流动性的"核心"与"非核心"拆分**
>
> 这是他处理M2的关键手法。他把私人部门的流动性负债分成两类：一类是"核心流动性"（core liquidity），即居民存款等传统银行负债，接近于传统货币统计口径；另一类是"非核心流动性"（non-core liquidity），即金融机构之间通过批发市场融资产生的负债——跨境存款、金融机构间贷款和证券等。
>
> 传统M2基本就是"核心流动性"——居民和企业的存款。但Howell认为真正驱动金融市场的是"非核心流动性"，也就是批发融资市场、repo市场、商业票据市场这些渠道产生的资金。你说的"剔除纯粹由信贷驱动的部分"，本质上就是把M2里那些由银行向实体经济放贷派生的存款视为"核心"部分（它更多反映实体信用周期），而把金融体系内部的杠杆扩张——影子银行、repo链条、批发融资——视为真正的"金融流动性"。
>
> **第三层：跨境维度**
>
> 在他的定义里，流动性是一个"总量融资概念，代表金融资产负债表的规模"，其范围超越了传统零售银行体系，扩展到企业现金流、repo和批发货币市场。由于大约60%的全球贸易以美元计价，离岸美元融资成本（体现在cross-currency basis swap里）是跨境流动性的关键价格信号。
>
> **最后的合成：z-score扩散指标**
>
> 在数据处理上，他从约80个经济体的原始数据出发，对各项流动性因子做z-score标准化，然后合成为类似扩散指标（diffusion-like indexes）的形式。这样做的好处是不同经济体、不同量纲的数据可以直接加总比较。
>
> **总结一下他和"简单加总全球M2"的区别：**
>
> 简单全球M2把居民定存、企业活期存款、批发融资一锅煮，Howell做的是把资金来源按渠道拆开——央行直接注入的、银行通过传统信贷派生的、影子银行通过抵押品链条加杠杆创造的——然后重点跟踪后两者，尤其是抵押品链条那一层，因为那才是对金融资产价格有直接驱动力的部分。他的核心洞察是：金融市场今天更多是关于债务再融资，而不是筹集新资本。70%-80%的交易本质上是某种形式的债务再融资。如果你要再融资债务，你需要金融体系中的资产负债表容量，这就意味着流动性。
>
> 如果你想深入了解，他的Substack "Capital Wars"有很多免费文章，《Capital Wars》这本书的第4-6章是方法论的核心部分。
>
> ### References
> 1. [https://capitalwars.substack.com/p/the-global-liquidity-cycle](https://capitalwars.substack.com/p/the-global-liquidity-cycle)
> 2. [https://grokipedia.com/page/Global_Liquidity_Index](https://grokipedia.com/page/Global_Liquidity_Index)
> 3. [https://capitalwars.substack.com/p/think-correctly-about-liquidity](https://capitalwars.substack.com/p/think-correctly-about-liquidity)
> 4. [https://capitalwars.substack.com/p/global-liquidity](https://capitalwars.substack.com/p/global-liquidity)
> 5. [https://www.triffininternational.eu/images/global_liquidity/GHYMERS_SOME-GENERAL-REMARKS-ON-GLOBAL-LIQUIDITY_VF.pdf](https://www.triffininternational.eu/images/global_liquidity/GHYMERS_SOME-GENERAL-REMARKS-ON-GLOBAL-LIQUIDITY_VF.pdf)
> 6. [https://journals.sagepub.com/doi/10.1177/04866134231196385](https://journals.sagepub.com/doi/10.1177/04866134231196385)
> 7. [https://themarket.ch/english/michael-howell-the-global-monetary-system-is-bifurcating-ld.15591](https://themarket.ch/english/michael-howell-the-global-monetary-system-is-bifurcating-ld.15591)
<!-- UID: 019f2758-12cb-7fcb-a160-9a988fe5a9aa -->

---
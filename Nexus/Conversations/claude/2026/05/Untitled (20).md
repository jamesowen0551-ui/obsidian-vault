---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: Untitled
conversation_id: fc721737-41b3-4196-99f4-9de2e963b19c
create_time: 2026-05-30T15:24:12.000Z
update_time: 2026-05-30T15:26:36.000Z
---
# Title: 因果推断的经典著作

Created: 2026/05/30 at 23:24:12
Last Updated: 2026/05/30 at 23:26:36
Chat URL: https://claude.ai/chat/fc721737-41b3-4196-99f4-9de2e963b19c


>[!nexus_user] **User** - 2026/05/30 at 23:24:12
> 因果推断有哪些著名的书啊
<!-- UID: 019e797c-5483-7576-a333-4cb78cd0227a -->
>[!nexus_agent] **Assistant** - 2026/05/30 at 23:24:35
> 因果推断领域有几本非常经典的书，我来按照难度和风格给你介绍一下，帮你找到最适合自己的入门路径。
>
> ---
>
> ## 入门友好型
>
> **《The Book of Why》（为什么）— Judea Pearl & Dana Mackenzie（2018）**
> 这是最适合非技术背景读者的一本书。Pearl 是因果推断领域的奠基人，这本书用通俗的语言讲述了"因果革命"的故事，核心概念是他提出的**因果阶梯（Ladder of Causation）**：关联 → 干预 → 反事实，三层层层递进。读完这本书你会对"为什么相关性不等于因果性"有非常深刻的直觉理解。
>
> ---
>
> ## 统计/计量经济学视角（偏应用）
>
> **《Causal Inference: The Mixtape》— Scott Cunningham（2021）**
> 这本书免费开放在网上，用 Stata 和 R 的例子讲解 DID（双重差分）、IV（工具变量）、RDD（断点回归）等常用方法，非常适合社会科学、经济学背景的读者。语言轻松幽默，"Mixtape"这个书名本身就透露了它的风格。
>
> **《Mostly Harmless Econometrics》— Angrist & Pischke（2009）**
> 这是计量经济学圈子里的圣经级读物，专注于识别策略（identification strategy），讲清楚了在观测数据中如何"找到"因果效应。如果你做过回归分析，这本书会让你对自己之前的分析有全新的反思。
>
> **《Causal Inference for the Brave and True》— Matheus Facure**
> 同样免费开放，Python 实现，非常适合数据科学背景的读者，代码可读性很高。
>
> ---
>
> ## 严谨理论型
>
> **《Causality》— Judea Pearl（2000，第二版 2009）**
> 这是 Pearl 的学术专著，系统介绍了 **do-calculus、DAG（有向无环图）、结构因果模型（SCM）**。内容非常严谨，数学要求较高，但如果你想真正理解因果推断的理论基础，这本书是绕不开的。
>
> **《Elements of Causal Inference》— Peters, Janzing & Schölkopf（2017）**
> 这本书也可以免费下载，从机器学习的角度切入因果推断，涉及到**因果发现（causal discovery）**，适合对 ML 有基础的读者。
>
> ---
>
> ## 潜在结果框架（Rubin 流派）
>
> **《Causal Inference for Statistics, Social, and Biomedical Sciences》— Imbens & Rubin（2015）**
> 如果说 Pearl 代表图模型流派，那 Imbens 和 Rubin 代表的就是**潜在结果（potential outcomes）框架**，也叫 Rubin 因果模型。这本书非常系统，在统计学和生物医学领域影响极大。
>
> ---
>
> ## 我的建议
>
> 如果你是**刚入门**，从《The Book of Why》开始，建立直觉；然后根据你的背景选择方向——偏应用就读 Cunningham 的 Mixtape，偏理论就读 Pearl 的 *Causality*。这两条路最终会在你脑子里汇合成一幅完整的图景。
>
> 你目前对因果推断了解到什么程度，是纯粹好奇，还是有具体的研究或项目需要用到它？这样我可以帮你更精准地推荐学习路径。
<!-- UID: 019e797c-5483-7d0f-bcc7-c938436ba082 -->

---
>[!nexus_user] **User** - 2026/05/30 at 23:26:16
> Causal Inference for the Brave and True causal Inference: The Mixtape  这两本有中文版吗
<!-- UID: 019e797e-3a36-77e0-8925-a6478c563c50 -->
>[!nexus_agent] **Assistant** - 2026/05/30 at 23:26:36
> 两本的情况不一样，让我分别说明：
>
> ---
>
> **Causal Inference for the Brave and True** 有中文版，而且有**两个**。这本书本身是开源的（在线免费阅读），原作者 Matheus Facure 也授权了多语言翻译。
>
> 第一个中文译本由 @xieliaing 完成，翻译了第 1–21 章，书名叫《因果推断：从概念到实践》。第二个更完整的版本由澳门城市大学的黄文喆和许文立合作完成，覆盖全部章节，书名叫《因果推断：献给求真敢为者》。
>
> 前者的中文翻译版在 GitHub 上公开，同样免费在线阅读，全部代码基于 Python，适用于计量经济学、量化社会学、策略评估等领域。 所以这本书你完全不用担心语言障碍，中文版内容质量也不错。
>
> ---
>
> **Causal Inference: The Mixtape** 目前**没有正式出版的中文译本**。搜索结果中只能看到经管之家等论坛有人分享英文原版 PDF，没有任何出版社出版中文版的记录。这本书由耶鲁大学出版社出版，正式翻译授权的门槛较高，目前也没有社区自发翻译的版本（不像 Brave and True 原作者态度非常开放）。
>
> ---
>
> **总结建议：** 如果语言是障碍，可以优先从《Brave and True》的中文版开始，直接在线阅读即可，免费且完整。Mixtape 暂时只能啃英文，不过它的语言风格比较轻松口语化，技术类书籍里算好读的，配合 DeepL 或 Claude 辅助理解也完全可行。
>
> ### References
> 1. [https://github.com/matheusfacure/python-causality-handbook](https://github.com/matheusfacure/python-causality-handbook)
> 2. [https://github.com/xieliaing/CausalInferenceIntro](https://github.com/xieliaing/CausalInferenceIntro)
<!-- UID: 019e797e-3a36-7b73-8e77-cd7e2f55fae2 -->

---
---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: Untitled
conversation_id: 1b7da37c-8b7d-49c3-be80-f4848e68e6ca
create_time: 2026-06-25T10:12:38.000Z
update_time: 2026-06-25T13:53:04.000Z
---
# Title: 中国劳动力市场高频数据

Created: 2026/06/25 at 18:12:38
Last Updated: 2026/06/25 at 21:53:04
Chat URL: https://claude.ai/chat/1b7da37c-8b7d-49c3-be80-f4848e68e6ca


>[!nexus_user] **User** - 2026/06/25 at 18:12:38
> 有哪些高频的中国劳动力市场相关数据啊
<!-- UID: 019efe44-6da3-781c-b7b5-620ef3145769 -->
>[!nexus_agent] **Assistant** - 2026/06/25 at 18:13:30
> 信息比较充分了，整理一下。
>
> ---
>
> 中国劳动力市场的数据，可以大致按照发布频率和来源性质分几类来看：
>
> **一、官方月频数据（最核心）**
>
> 最重要的就是**城镇调查失业率**，由国家统计局每月随GDP等数据同步发布，分全国、31个大城市，以及分年龄段（16-24岁青年失业率）和分外来人口失业率等细分口径。以2025年一季度为例，1-3月全国城镇调查失业率均值为5.3%，其中3月份回落至5.2%；同期31个大城市失业率稳定在5.1-5.2%附近。
>
> 配套的月频数据还有**城镇新增就业人数**，如2025年一季度城镇新增就业308万人，同比增加5万人，这个数据由人社部发布，属于行政登记口径，与调查失业率互为补充。
>
> **二、季度数据**
>
> **求人倍率**是反映需求端的核心指标，由人社部对100个城市公共就业服务机构的市场供求数据汇总发布，季度频率，类似美国的JOLTS。就业失业数据来自家庭住户调查，更多反映劳动力供给的变化；而来自工作场所调查的信息则反映劳动力需求的变化，二者需要结合使用，才能更全面地把握劳动力市场总体趋势。这也是当前国内监测体系的一个短板。
>
> **三、PMI就业分项（月频）**
>
> PMI中有专门的**从业人员分项**，制造业PMI从业人员指数月频发布，用于衡量制造业企业的用工景气度；服务业PMI中同样有从业人员分项，按月更新，2012年以来持续跟踪。这两个是能拿到的最高频官方就业景气指标，缺点是只有扩散指数，没有规模信息。
>
> **四、民间/替代性高频数据**
>
> 这一块其实是研究者和宏观研究员比较关注的：
>
> - **招聘平台数据**：BOSS直聘、前程无忧、智联招聘、猎聘等平台公开或通过学术合作发布的招聘职位数量、薪资中位数、各行业岗位变化等。学术界已有团队系统爬取了前程无忧、BOSS直聘、智联招聘、猎聘、拉勾等主流招聘网站的招聘数据，用于研究技能需求变化等议题，部分券商研究也会用这类数据作为月频甚至周频的就业需求前瞻。
>
> - **"最缺工"职业排行**：人社部就业培训技术指导中心每季度基于全国100+城市公共就业机构数据发布，通过汇总需求人数与求职人数缺口，形成各季度"全国招聘大于求职最缺工的100个职业排行"，可以追踪结构性供需矛盾。
>
> - **农民工相关数据**：国家统计局每年发布农民工监测调查报告（年度），但季度GDP公布时偶尔会披露农民工外出务工的阶段性情况，2021-2024年农民工总量年均增速约1.2%，稳定在约3亿人规模，是判断劳动力供给侧变化的重要视角。
>
> - **社保参保人数**：截至2025年3月底，全国基本养老、失业、工伤保险参保人数分别为10.71亿人、2.44亿人、2.97亿人，同比分别增加442万、256万、271万人，这个数据可以侧面印证就业规模的实际变化，相对难造假。
>
> **五、数据局限与补充说明**
>
> 值得注意的是，中国目前尚未建立系统的"职位空缺调查"制度，"十四五"规划曾明确提出健全就业需求调查和失业监测预警机制，但落地尚不充分。因此和美国相比，中国就业数据的需求侧信息相对薄弱，求人倍率覆盖面也受限于公共就业服务机构，无法全面反映市场化招聘。这也是为什么市场上对招聘平台数据的替代性使用越来越多。
>
> 如果你是从宏观研究或利率债角度来看这些数据，最常跟踪的组合大概是：月频失业率（政策关注焦点）+ PMI从业人员分项（先行判断）+ 季度新增就业累计（政策完成情况）；招聘平台数据则更多是研究框架里的补充视角。你想深入某一类数据吗？
>
> ### References
> 1. [https://hrssit.cn/info/3650.html](https://hrssit.cn/info/3650.html)
> 2. [https://chrm.mohrss.gov.cn/%E4%BA%BA%E7%A4%BE%E9%83%A8%E5%8F%91%E5%B8%83%EF%BC%9A2025%E5%B9%B4%E4%B8%80%E5%AD%A3%E5%BA%A6%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90%E5%92%8C%E7%A4%BE%E4%BC%9A%E4%BF%9D%E9%9A%9C%E5%B7%A5%E4%BD%9C/](https://chrm.mohrss.gov.cn/%E4%BA%BA%E7%A4%BE%E9%83%A8%E5%8F%91%E5%B8%83%EF%BC%9A2025%E5%B9%B4%E4%B8%80%E5%AD%A3%E5%BA%A6%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90%E5%92%8C%E7%A4%BE%E4%BC%9A%E4%BF%9D%E9%9A%9C%E5%B7%A5%E4%BD%9C/)
> 3. [https://chrm.mohrss.gov.cn/%E7%A8%B3%E5%B0%B1%E4%B8%9A%E6%9C%89%E4%BF%A1%E5%BF%83%E6%9C%89%E5%BA%95%E6%B0%94/](https://chrm.mohrss.gov.cn/%E7%A8%B3%E5%B0%B1%E4%B8%9A%E6%9C%89%E4%BF%A1%E5%BF%83%E6%9C%89%E5%BA%95%E6%B0%94/)
> 4. [https://m.huxiu.com/article/2798253.html](https://m.huxiu.com/article/2798253.html)
> 5. [https://ca-sme.org/content/Content/index/id/98109](https://ca-sme.org/content/Content/index/id/98109)
> 6. [https://www.ceicdata.com/zh-hans/china/purchasing-managers-index-non-manufacturing-service/cn-pmi-service-employment](https://www.ceicdata.com/zh-hans/china/purchasing-managers-index-non-manufacturing-service/cn-pmi-service-employment)
> 7. [https://www.macrodatas.cn/article/1147473371](https://www.macrodatas.cn/article/1147473371)
> 8. [https://www.bpu.edu.cn/__local/0/09/96/83DC037568ED8857F9E8696F8D8_25D30D74_15445C.pdf?e=.pdf](https://www.bpu.edu.cn/__local/0/09/96/83DC037568ED8857F9E8696F8D8_25D30D74_15445C.pdf?e=.pdf)
> 9. [https://m.chinabgao.com/freereport/107962.html](https://m.chinabgao.com/freereport/107962.html)
<!-- UID: 019efe44-6da3-7325-862b-4114f7398a71 -->

---
>[!nexus_user] **User** - 2026/06/25 at 21:52:08
> 目前中国K型经济有什么体现
<!-- UID: 019eff0d-61ae-73fb-844e-dbfd1fb1e3e7 -->
>[!nexus_agent] **Assistant** - 2026/06/25 at 21:53:04
>
>
> 信息很充分了，系统整理一下。
>
> ---
>
> 中国K型经济的核心逻辑是同一时期内不同维度（行业、群体、地区）的轨迹出现方向性分化，而不只是增速快慢的差异。目前这种分化在几个层面上都相当清晰。
>
> **一、最显著的一笔：出口/制造业 vs. 内需**
>
> 这是目前中国K型分化最宏观的表现。2025年的中国经济，外需相对强劲，出口保持增长，高新技术板块表现亮眼；内需依然不足，房地产与固定资产投资偏弱，消费持续承压。
>
> 从数字上看，2025年，最终消费、资本形成、净出口对经济增长的贡献率分别是52%、15.3%和32.7%，净出口贡献比例之高在历史上少见。国家统计局自己也承认"国内供强需弱矛盾突出"——这几乎是官方文件里少有的对K型分化的直白表述。
>
> **二、行业维度：上行的一笔与下行的一笔**
>
> **上行**：高端制造与出口链。2025年前三季度，高技术产品出口持续增长，汽车、船舶和集成电路出口同比分别增长10.8%、21.4%和23.3%，高附加值资本品和中间品成为出口主力；新能源、半导体、船舶产业景气持续。
>
> **下行**：房地产及其关联产业链是最典型的坠落天使。万科在2025年创下了接近1000亿人民币的亏损纪录。截至"十四五"结束，累计已有77家房企出现债务违约，28家上市房企退市；TOP100房企销售份额由2020年的近六成降至2025年的约三成。与此同时，那些对上游资源品涨价相对敏感、而下游竞争又激烈到无法传导涨价的行业也深陷两头受压——"增收不增利"成为普遍现象。
>
> **三、消费层面：高端涨、中端承压、大众降级**
>
> 消费内部的K型分化是最直观的体感。金银珠宝年增13.3%、奢侈品等高端消费增速达粮油食品等必需品的2.5-4.5倍。消费呈现"K型分化"，高端服务与低价折扣两端强劲（如五星级酒店和黄金消费回暖），但中端改善型消费持续承压。
>
> 这背后是财富效应的高度不均等分配。资本市场整体向好有望带动居民财产性收入增速回升，资本市场的财富效应或将逐步取代房地产市场对消费的传统拉动作用——但问题在于，持有大量金融资产的主要是高收入人群，普通居民的主要资产仍然是房产。房价下行使大部分家庭财富持续缩水，反而加大了储蓄倾向。证券账户活跃度的爆发式增长，与居民部门预防性储蓄的历史新高以及全社会零售价格中枢的持续下移，共同构筑了"金融高频共振，民生低频静默"的奇异图景。
>
> **四、就业维度：青年与中老年、新兴行业与传统行业**
>
> 工资增速回落至2025年的不足1%，青年失业率仍居高不下，2025年12月为16.5%。前三季度全国城镇调查失业率均值为5.2%，高于去年同期，其中16-24岁不含在校生群体失业率均值16.6%，高于去年同期的15.6%。
>
> 与此同时，高端制造的产能扩张并未等比例转化为新增就业——自动化提升了人均产出，却削弱了广泛吸纳就业的能力；一些原本具备大规模就业能力的行业如新能源汽车，深陷价格战，薪资与分红并不突出，外溢效应有限。这导致新动能的产业崛起并未能有效"接棒"旧动能退出所留下的就业缺口。
>
> **五、收入与地区维度**
>
> 2025年全国居民人均可支配收入中位数为36231元，仅为平均数的83.5%，均值与中位数的持续偏离本身就是分化的信号。
>
> 地区层面，一线城市仍能维持约5%的固定资产投资增速，但天津为-8.7%、南京为-3.9%、盐城-7.8%；而义乌（+7.6%）、常熟（+11.4%）等受外贸或制造业拉动的城市表现相对较好，地区间的冷暖差距正在拉大。
>
> ---
>
> **整体来看**，中国当前K型经济的结构性特征可以概括为：出口/高端制造/高收入群体在走上行曲线，房地产/传统行业/中低收入居民/非制造业城市在走下行曲线，两者的断层点恰好是"内需"。这也是为什么政策重心一直在"提振内需"上反复发力，但效果受限于财富缩水、就业预期偏弱和预防性储蓄三重约束，还没有找到有效的传导路径。
>
> ### References
> 1. [https://36kr.com/p/3607876816438279](https://36kr.com/p/3607876816438279)
> 2. [https://www.yicai.com/epaper/pc/202601/20/content_49329.html](https://www.yicai.com/epaper/pc/202601/20/content_49329.html)
> 3. [https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962330.html](https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962330.html)
> 4. [https://www.ykzq.com/products/download-new/rpt/2025/11/09/8e0b3d5c75ae490eb59c8b2caa7ebd77.pdf](https://www.ykzq.com/products/download-new/rpt/2025/11/09/8e0b3d5c75ae490eb59c8b2caa7ebd77.pdf)
> 5. [https://letschuhai.com/a47f86da](https://letschuhai.com/a47f86da)
> 6. [https://pdf.dfcfw.com/pdf/H3_AP202512271809094203_1.pdf?1766830597000.pdf](https://pdf.dfcfw.com/pdf/H3_AP202512271809094203_1.pdf?1766830597000.pdf)
> 7. [https://www.huxiu.com/article/4855763.html](https://www.huxiu.com/article/4855763.html)
> 8. [https://zhuanlan.zhihu.com/p/1934700564249310127](https://zhuanlan.zhihu.com/p/1934700564249310127)
> 9. [https://www.aastocks.com/marketcomment/pdf/159919.pdf](https://www.aastocks.com/marketcomment/pdf/159919.pdf)
> 10. [https://assets.kpmg.com/content/dam/kpmgsites/cn/pdf/zh/2025/11/china-economic-monitor-q4-2025.pdf.coredownload.inline.pdf](https://assets.kpmg.com/content/dam/kpmgsites/cn/pdf/zh/2025/11/china-economic-monitor-q4-2025.pdf.coredownload.inline.pdf)
> 11. [https://zhuanlan.zhihu.com/p/1996544904751511389](https://zhuanlan.zhihu.com/p/1996544904751511389)
> 12. [https://www.imf.org/-/media/files/publications/cr/2026/chinese/1chnca2026001.pdf](https://www.imf.org/-/media/files/publications/cr/2026/chinese/1chnca2026001.pdf)
> 13. [https://assets.kpmg.com/content/dam/kpmg/cn/pdf/zh/2025/11/china-economic-monitor-q4-2025.pdf](https://assets.kpmg.com/content/dam/kpmg/cn/pdf/zh/2025/11/china-economic-monitor-q4-2025.pdf)
> 14. [https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962321.html](https://www.stats.gov.cn/sj/zxfb/202601/t20260119_1962321.html)
<!-- UID: 019eff0d-61ae-7092-8680-fa62be0b1416 -->

---
---
tags: [MOC, 美联储, 资产负债表, QT, 准备金, 知识地图]
---

# 🗺️ MOC · 美联储资产负债表研究

> 16+7 篇文献的知识地图主页。按**立场光谱**组织，辅以主题与阅读路径索引。
> 论文原文与提取文本见 [[Fed_Balance_Sheet_Research/README|论文库 README]]；早期综述见 [[文献综述_美联储资产负债表缩表之争]]；**31 篇整合长文见 [[深度综述_缩表之争_31篇]]**。

## 核心问题

联储资产负债表从 GDP 的 5% 膨胀到峰值 35%（现约 21%）。三个环环相扣的问题：

1. **为什么缩不动？** → 准备金需求是监管与制度的内生变量（棘轮）
2. **还能缩多少？** → 需求曲线定量估计 + 三难权衡
3. **缩完之后用什么框架？** → 地板 vs 走廊的制度设计之争

---

## 立场光谱

### 🟥 小表/走廊派——"地板制是个错误"

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/02_Nelson_2024_How_the_Fed_Got_So_Huge\|Nelson 2024]] | 2019 年永久化过剩准备金框架是错误；需求棘轮 $35B→$3T |
| [[Fed_Balance_Sheet_Research/读书笔记/04_Nelson_2025_Forward_Guidance_Remodeling_the_House\|Nelson 2025]] | 后地板施工图：点目标 + 100bp 走廊 + 每日 OMO + 贴现额度视同准备金 + 永不 QE |
| [[Fed_Balance_Sheet_Research/读书笔记/10_Borio_2023_Getting_up_from_the_Floor\|Borio 2023]] | BIS：地板成本慢性隐蔽、走廊难度被高估；表应"尽可能小、尽可能无风险" |

### 🟦 改革监管再缩表派——"需求是监管画出来的"（当前政策风向）

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/03_Miran_2025_Regulatory_Dominance\|Miran 2025]] | 联储理事：稀缺/充裕/丰富的边界由监管决定；先改监管（SLR/LCR）再谈缩表 |
| [[Fed_Balance_Sheet_Research/读书笔记/01_User's_Guide_2026_Reducing_Fed_Balance_Sheet\|User's Guide 2026]] | 15 项选项菜单，充裕框架内可缩 **1.2–2.1 万亿**；"菜单非背书"，至少准备一年 |

### 🟩 官方现状派——"充裕框架运转良好，谨慎监测"

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/15_Remache_2025_Balance_Sheet_Reduction_and_Ample_Reserves\|Remache 2025]] | SOMA 副经理：缩表进展与充裕准备金判定标准 |
| [[Fed_Balance_Sheet_Research/读书笔记/16_Perli_2025_Money_Market_Conditions_and_the_Fed_Balance_Sheet\|Perli 2025]] | SOMA 经理：用货币市场压力指标指导缩表终点；SRF 作上限 |
| [[Fed_Balance_Sheet_Research/读书笔记/17_Waller_2025_Demystifying_Fed_Balance_Sheet\|Waller 2025]] | 理事算术：最小合意表 ≈ $5.8T / 19% GDP；资产端久期匹配 |
| [[Fed_Balance_Sheet_Research/读书笔记/18_Williams_2025_On_the_Optimal_Supply_of_Reserves\|Williams 2025]] | 纽约联储主席：不确定性下最优供给更高；工具组合无唯一最优 |
| [[Fed_Balance_Sheet_Research/读书笔记/20_Clouse_Infante_Senyuz_2025_Market_Based_Indicators\|Clouse et al. 2025]] | 官方仪表盘：利差水平 × 曲线斜率 × 敏感度三类指标 |
| [[Fed_Balance_Sheet_Research/读书笔记/28_Logan_Schulhofer-Wohl_2026_Options_for_Reducing_Fed_Balance_Sheet\|Logan & Schulhofer-Wohl 2026]] | 达拉斯联储：全负债缩表选项清单；需求曲线左移优于稀缺化；不量化不排序 |

### 🟨 学术定量派——"还能缩多少"的标尺

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/05_Lopez-Salido_Vissing-Jorgensen_2023_Reserve_Demand\|LS&VJ 2023]] | 需求三驱动框架；准备金+ONRRP 还可缩约 2 万亿 |
| [[Fed_Balance_Sheet_Research/读书笔记/06_Lagos_Navarro_2026_Reserve_Demand_Minimal_Theory\|Lagos & Navarro 2026]] | 最少理论假设的需求曲线估计，交叉验证 LS&VJ |
| [[Fed_Balance_Sheet_Research/读书笔记/07_Duygan-Bump_Kahn_2026_Balance_Sheet_Trilemma\|Duygan-Bump & Kahn 2026]] | 三难：小表、低利率波动、少干预——三者取二 |

### 🟪 理论模型派——机制与福利分析

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/09_Kumhof_Salgado-Moreno_2024_QE_QT_Money_Channel\|Kumhof & Salgado-Moreno 2024]] | 货币渠道：永久 QT 伤害实体；逆周期准备金规则福利 ≈ 泰勒规则（挺大表） |
| [[Fed_Balance_Sheet_Research/读书笔记/11_Arce_Nuno_Thaler_Thomas_2019_Floor_vs_Corridor\|Arce et al. 2019]] | 地板政策空间更大；但小表+**及时** QE 福利等价（中性） |
| [[Fed_Balance_Sheet_Research/读书笔记/26_Bianchi_Bigio_2022_Banks_Liquidity_Management\|Bianchi & Bigio 2022]] | Econometrica：放贷盈利 vs 流动性风险的权衡；2008 = 银行间失灵 + 需求萎缩两阶段 |
| [[Fed_Balance_Sheet_Research/读书笔记/25_Afonso_et_al_2023_Optimal_Supply_Reserves_Uncertainty\|Afonso et al. 2023 (SR 1077)]] | 不确定性 → 预防性超供；好用的贷款便利可换更小供给 |
| [[Fed_Balance_Sheet_Research/读书笔记/24_Acharya_Rajan_2022_Liquidity_Liquidity_Everywhere\|Acharya & Rajan 2022]] | 准备金引致可兑付存款；压力时索取权同兑现 + 盈余行囤积 → 流动性幻觉 |
| [[Fed_Balance_Sheet_Research/读书笔记/27_Greenwood_Hanson_Stein_2016_Financial_Stability_Tool\|Greenwood, Hanson & Stein 2016]] | 大表派奠基：政府安全短债挤出私人期限转换（⚠️ 仅摘要与要点，PDF 反爬） |

### ⬛ 实证证据派——QT 与 2019 危机的事实验

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/08_Du_Forbes_Luzzetti_2024_QT_Around_the_World\|Du, Forbes & Luzzetti 2024]] | 七国 QT：公告 4–8bp、累计 20–26bp；主动 > 被动；警惕 paint dry → water boil |
| [[Fed_Balance_Sheet_Research/读书笔记/12_Afonso_et_al_2021_Market_Events_Mid-September_2019\|Afonso et al. 2021]] | 2019 回购危机官方复盘：充裕 ≠ 充足 |
| [[Fed_Balance_Sheet_Research/读书笔记/13_Anbil_Anderson_Senyuz_2020_Money_Markets_Sept2019\|Anbil et al. 2020]] | 理事会视角：事前预警信号有哪些 |
| [[Fed_Balance_Sheet_Research/读书笔记/14_Smith_Valcarcel_2023_Financial_Market_Effects_of_Unwinding\|Smith & Valcarcel 2023]] | QT ≠ QE 倒放：影响在实施期经流动性渠道浮现 |
| [[Fed_Balance_Sheet_Research/读书笔记/21_Copeland_Duffie_Yang_2021_Reserves_Not_So_Ample\|Copeland, Duffie & Yang 2021]] | 中介机构的准备金才关键；日内支付延迟是前瞻预警（QJE 2025） |
| [[Fed_Balance_Sheet_Research/读书笔记/22_Acharya_et_al_2023_Liquidity_Dependence\|Acharya et al. 2023]] | Jackson Hole：QE 养大的存款+信贷额度不随 QT 收缩 → 流动性依赖 |

### 🟫 支付系统派——"下限由支付需求划定"

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/23_Duffie_2026_Payment_System_Floor\|Duffie 2026]] | BPEA：支付系统决定表的下限；处方 = 临时 OMO + Fedwire LSM + 改监管 + 分层付息 |
| [[Fed_Balance_Sheet_Research/读书笔记/19_Vissing-Jorgensen_2025_TGA_Fluctuations\|Vissing-Jorgensen 2025]] | TGA 波动管理三原则：利率控制 / 不动政策立场 / 沟通清晰 |

### 🟧 跨国央行实践——三种"终局框架"的活实验

| 文献 | 一句话 |
|---|---|
| [[Fed_Balance_Sheet_Research/读书笔记/29_Schnabel_2025_Towards_New_Eurosystem_Balance_Sheet\|Schnabel 2025（ECB）]] | QN 已缩 45% 且无冲击；终局 = 需求驱动：标准再融资→结构性 LTRO→短久期结构组合 |
| [[Fed_Balance_Sheet_Research/读书笔记/30_Bailey_2024_Importance_of_Central_Bank_Reserves\|Bailey 2024（BoE）]] | PMRR £345–490bn；到达后 QT 只换资产构成；终局资产或转向 repo 组合 |
| [[Fed_Balance_Sheet_Research/读书笔记/31_Gravelle_2025_End_of_QT_and_What_Comes_Next\|Gravelle 2025（BoC）]] | 首个走完 QT 的 G7 央行：终点区间上调至 500–700 亿加元；提前购债平滑大额到期 |

---

## 关键张力（写作弹药）

- **"永不 QE" vs "及时 QE"**：Nelson 2025 ↔ Arce et al. 2019——小表体制的成败取决于危机工具的可信度与速度。
- **"充裕就够" vs "分布也关键"**：User's Guide ↔ Kumhof——总量充裕下局部稀缺仍可放大为系统性成本（2019 年即如此）。
- **"需求是外生市场量" vs "需求是监管的内生函数"**：Perli/Remache ↔ Miran/Nelson/UG26——这是整个辩论的范式分水岭。
- **"QT 温和" vs "QT 有实体成本"**：DFL 跨国证据 ↔ Kumhof 模型——公告窗口定价 vs 稳态分布摩擦，尺度不同，结论未必矛盾。
- **地板的成本是慢性的，走廊的成本是即时的**（Borio 的可见性不对称）——为何政策天然偏向大表。

## 主题索引

- **准备金需求估计**：LS&VJ · Lagos & Navarro · User's Guide §选项表
- **操作框架设计**：Nelson 2025 · Borio · Arce et al. · Trilemma
- **监管与流动性要求**：Miran · User's Guide · Nelson 2024（棘轮）
- **QT 实证**：DFL · Smith & Valcarcel · 2019 危机三篇
- **政策现状**：Remache · Perli · Miran
- **跨国终局框架**：Schnabel（ECB 需求驱动）· Bailey（BoE PMRR/repo）· Gravelle（BoC 回常态）
- **缩表选项清单**：Logan & Schulhofer-Wohl（框架，不量化）· User's Guide（量化，不排序）

## 待补充（下一轮候选）

Ihrig/Senyuz/Weinbach (2020) 充裕框架基础三连；Gissler et al. (2025) 非银资金出借方监测；Cordes & Infante (2025) 回购利率敏感度；Cavallino et al. (2025) BIS 操作框架分类法；Barr (2026) "Beyond the Balance Sheet"；Anbil, Infante & Senyuz (2026) "A Tale of Demand and Supply for Central Bank Reserves"（FEDS 2026-028）。

---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: GARCH模型在配对交易中的应用
conversation_id: 89166780-4527-43c2-b29b-75d2eedf9ce0
create_time: 2026-06-26T06:55:05.000Z
update_time: 2026-06-26T07:02:17.000Z
---
# Title: GARCH模型在配对交易中的应用

Created: 2026/06/26 at 14:55:05
Last Updated: 2026/06/26 at 15:02:17
Chat URL: https://claude.ai/chat/89166780-4527-43c2-b29b-75d2eedf9ce0


>[!nexus_user] **User** - 2026/06/26 at 14:55:05
> GARCH怎么做配对交易啊
<!-- UID: 019f02b5-ec22-7b7f-a714-ecaab9468469 -->
>[!nexus_agent] **Assistant** - 2026/06/26 at 14:56:01
> # GARCH 配对交易
>
> 配对交易（Pairs Trading）结合 GARCH 主要有两条路径：
>
> ---
>
> ## 一、为什么要用 GARCH？
>
> 配对交易的核心是价差（spread）的均值回归。GARCH 在其中解决两个问题：
>
> 1. **波动率时变性**：价差的波动率不是常数，静态阈值（如固定2σ）在波动低谷时过于宽松、波动高峰时过于紧绷
> 2. **动态止损/入场**：用条件方差 $h_t$ 替代历史波动率，让开平仓阈值随市场状态自适应调整
>
> ---
>
> ## 二、主要框架
>
> ### 框架 A：协整 + GARCH 残差建模（最经典）
>
> ```
> 步骤：
> 1. 找协整对（Engle-Granger 或 Johansen 检验）
> 2. 估计协整关系：S_t = β · P_t + α + ε_t
> 3. 对残差 ε_t 建 GARCH(1,1) 模型
> 4. 用条件标准差 √h_t 动态归一化价差
> 5. 入场信号：归一化价差 z_t = ε_t / √h_t 超过 ±k 时开仓
> ```
>
> **优点**：直接、可解释性强
> **缺点**：协整关系在样本外常不稳定
>
> ---
>
> ### 框架 B：DCC-GARCH（动态条件相关）
>
> 这是更完整的方法，直接对两个资产价格 **联合** 建模：
>
> $$\mathbf{r}_t = \boldsymbol{\mu} + \boldsymbol{\varepsilon}_t, \quad \boldsymbol{\varepsilon}_t = H_t^{1/2} \mathbf{z}_t$$
>
> $$H_t = D_t R_t D_t$$
>
> - $D_t$：各自的 GARCH 条件波动率（对角矩阵）
> - $R_t$：DCC 过程给出的动态相关系数矩阵
>
> **交易逻辑**：当 $\rho_t$（动态相关系数）突然下降 → 两资产偏离 → 做多低估、做空高估；等待 $\rho_t$ 回升时平仓
>
> ---
>
> ### 框架 C：GJR-GARCH / EGARCH + 状态机制
>
> 加入**非对称效应**：
>
> $$h_t = \omega + \alpha \varepsilon_{t-1}^2 + \gamma \varepsilon_{t-1}^2 \mathbf{1}_{\varepsilon_{t-1}<0} + \beta h_{t-1}$$
>
> 利率债/商品配对中，下行波动通常大于上行，GJR-GARCH 能更好捕捉这一不对称性，从而在高波动期间缩窄阈值、减少假信号。
>
> ---
>
> ## 三、核心交易规则（以框架 A 为例）
>
> | 信号 | 条件 | 操作 |
> |------|------|------|
> | 开仓做空价差 | $z_t > +k$ | 卖 S，买 P |
> | 开仓做多价差 | $z_t < -k$ | 买 S，卖 P |
> | 平仓 | $\|z_t\| < c$（如 0.5） | 全部平仓 |
> | 止损 | $\|z_t\| > k_{stop}$ 或持仓超时 | 强制平仓 |
>
> $k$ 一般取 1.5～2，但关键在于 **$z_t$ 的分母是动态的 $\sqrt{h_t}$**，而不是滚动历史标准差。
>
> ---
>
> ## 四、固收/利率债场景的特殊考量
>
> 你做的是利率债，有几点需要注意：
>
> - **配对标的**：常见的是国债不同期限（如 5Y vs 10Y 做蝶式/价差交易），或国债 vs 国开债（信用利差配对）
> - **价差定义**：用收益率价差（YTM spread）而非价格价差，避免久期不匹配
> - **久期中性**：开仓需做**DV01 中性**对冲，GARCH 归一化后的信号只管方向，仓位大小由 DV01 比例决定
> - **GARCH 数据频率**：日频收益率建 GARCH 效果好，周内数据噪声大
>
> ---
>
> ## 五、一个简单的 Python 骨架
>
> ```python
> import numpy as np
> from arch import arch_model
> import statsmodels.api as sm
>
> # 1. 估计协整关系
> res = sm.OLS(spread_asset1, sm.add_constant(spread_asset2)).fit()
> residuals = res.resid
>
> # 2. 对残差建 GARCH(1,1)
> garch = arch_model(residuals, vol='Garch', p=1, q=1, dist='t')
> garch_fit = garch.fit(disp='off')
>
> # 3. 提取条件波动率
> cond_vol = garch_fit.conditional_volatility
>
> # 4. 归一化价差
> z_score = residuals / cond_vol
>
> # 5. 生成信号
> k_entry, k_exit = 2.0, 0.5
> signal = np.where(z_score > k_entry, -1,
>          np.where(z_score < -k_entry, 1,
>          np.where(np.abs(z_score) < k_exit, 0, np.nan)))
> ```
>
> ---
>
> ## 六、常见坑
>
> 1. **过拟合**：GARCH 参数在样本内很好看，样本外经常漂移，建议滚动重估（每周/每月）
> 2. **交易成本**：动态阈值导致换手率高，利率债流动性还好，但仍需把冲击成本算进去
> 3. **协整关系漂移**：β 不稳定时用 Kalman Filter 实时更新 β，再对残差跑 GARCH
> 4. **极端波动期**：GARCH 在 VIX 飙升时会低估真实风险，可以叠加一个简单的波动率 cap
>
> ---
>
> 有没有想深入的部分？比如 DCC-GARCH 的估计方法、滚动窗口的参数稳定性检验，或者具体到国债收益率价差的实证设置？
<!-- UID: 019f02b5-ec22-72cf-bfa7-c0145c913fef -->

---
>[!nexus_user] **User** - 2026/06/26 at 15:01:31
> 讲讲GARCH模型把
<!-- UID: 019f02bb-d166-7d3d-9112-2d77a3fe7060 -->
>[!nexus_agent] **Assistant** - 2026/06/26 at 15:02:17
> # GARCH 模型详解
>
> ---
>
> ## 一、从问题出发：为什么需要 GARCH？
>
> 普通线性回归假设误差项方差恒定（同方差性）。但金融时间序列有一个显著特征：
>
> **波动率聚集（Volatility Clustering）**——大的波动后面跟着大的波动，小的跟着小的。
>
> ```
> 收益率序列长这样：
> ...平静期...  |||大波动||| ...平静期... |||大波动|||...
> ```
>
> 这说明方差本身是**时变的**，是过去信息的函数。GARCH 就是建模这个动态方差的工具。
>
> ---
>
> ## 二、从 ARCH 到 GARCH
>
> ### 2.1 ARCH(q)——Engle 1982
>
> **自回归条件异方差**（AutoRegressive Conditional Heteroskedasticity）
>
> $$r_t = \mu + \varepsilon_t, \quad \varepsilon_t = \sigma_t z_t, \quad z_t \stackrel{iid}{\sim} (0,1)$$
>
> $$\sigma_t^2 = \omega + \alpha_1 \varepsilon_{t-1}^2 + \alpha_2 \varepsilon_{t-2}^2 + \cdots + \alpha_q \varepsilon_{t-q}^2$$
>
> **直觉**：今天的条件方差 = 常数 + 过去 $q$ 期的"冲击平方"的加权和
>
> **问题**：要捕捉长记忆性，$q$ 得很大，参数太多
>
> ---
>
> ### 2.2 GARCH(p,q)——Bollerslev 1986
>
> 加入**方差的自回归项**，大幅压缩参数：
>
> $$\boxed{\sigma_t^2 = \omega + \sum_{i=1}^{q} \alpha_i \varepsilon_{t-i}^2 + \sum_{j=1}^{p} \beta_j \sigma_{t-j}^2}$$
>
> 实践中 **GARCH(1,1) 几乎打遍天下**：
>
> $$\sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
>
> | 参数 | 含义 | 典型值 |
> |------|------|--------|
> | $\omega$ | 长期方差基准 | 很小的正数 |
> | $\alpha$ | 冲击敏感度（ARCH项） | 0.05～0.15 |
> | $\beta$ | 方差持续性（GARCH项） | 0.80～0.95 |
> | $\alpha + \beta$ | 持续性总和 | <1（平稳条件） |
>
> ---
>
> ## 三、模型解剖
>
> ### 3.1 三个方程的含义
>
> ```
> 均值方程：  r_t = μ + ε_t           ← 可以是 AR、ARMA 等
> 扰动分解：  ε_t = σ_t · z_t          ← 将冲击分解为"大小"×"方向"
> 方差方程：  σ²_t = ω + αε²_{t-1} + βσ²_{t-1}   ← 核心
> ```
>
> ### 3.2 方差方程的直觉展开
>
> 把 $\sigma_t^2$ 递推展开：
>
> $$\sigma_t^2 = \frac{\omega}{1-\beta} + \alpha \sum_{k=0}^{\infty} \beta^k \varepsilon_{t-1-k}^2$$
>
> 本质是**过去所有冲击的指数加权移动平均（EWMA）**，$\beta$ 控制衰减速度。
>
> ### 3.3 无条件方差（长期均值）
>
> $$\bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}$$
>
> 这是波动率均值回归的"锚"。当 $\sigma_t^2 > \bar{\sigma}^2$ 时，未来有向下均值回归的倾向。
>
> ---
>
> ## 四、参数约束与平稳性
>
> | 条件 | 约束 | 含义 |
> |------|------|------|
> | 正定性 | $\omega > 0,\ \alpha \geq 0,\ \beta \geq 0$ | 方差不能为负 |
> | 协方差平稳 | $\alpha + \beta < 1$ | 存在有限无条件方差 |
> | 单位根（IGARCH） | $\alpha + \beta = 1$ | 冲击影响永久持续 |
>
> 当 $\alpha + \beta$ 接近 1（如 0.98），说明波动率有**很强的持续性**——这在实际金融数据中非常普遍。
>
> ---
>
> ## 五、GARCH 的各种变体
>
> ### 5.1 非对称效应：GJR-GARCH（Glosten-Jagannathan-Runkle）
>
> **动机**：下跌时波动率上升更多（杠杆效应）
>
> $$\sigma_t^2 = \omega + (\alpha + \gamma \mathbf{1}_{\varepsilon_{t-1}<0})\varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$
>
> - $\gamma > 0$：坏消息比好消息对波动率的冲击更大
> - 股票市场的 $\gamma$ 通常显著为正
>
> ### 5.2 对数形式：EGARCH（Nelson 1991）
>
> $$\ln \sigma_t^2 = \omega + \beta \ln \sigma_{t-1}^2 + \alpha \left|\frac{\varepsilon_{t-1}}{\sigma_{t-1}}\right| + \gamma \frac{\varepsilon_{t-1}}{\sigma_{t-1}}$$
>
> - 天然保证 $\sigma_t^2 > 0$，无需参数约束
> - $\gamma < 0$ 捕捉杠杆效应
>
> ### 5.3 GARCH-M（均值中的 GARCH）
>
> $$r_t = \mu + \lambda \sigma_t^2 + \varepsilon_t$$
>
> 把风险溢价直接写进均值方程——高波动期要求更高预期收益
>
> ### 5.4 多元：DCC-GARCH（Engle 2002）
>
> 对资产组合的**协方差矩阵**建模：
>
> $$H_t = D_t R_t D_t$$
>
> - $D_t$：各资产各自的 GARCH 条件标准差（对角）
> - $R_t$：动态条件相关系数矩阵（DCC 过程）
>
> ---
>
> ## 六、估计方法
>
> ### 最大似然估计（MLE）
>
> 假设 $z_t \sim N(0,1)$，对数似然函数：
>
> $$\ell(\theta) = -\frac{1}{2} \sum_{t=1}^T \left( \ln \sigma_t^2 + \frac{\varepsilon_t^2}{\sigma_t^2} \right)$$
>
> 实际中 $z_t$ 通常有**厚尾**，常用 **Student-t 分布**替代正态，增加自由度参数 $\nu$：
>
> $$\ell(\theta, \nu) = \sum_{t=1}^T \left[ \ln \Gamma\left(\frac{\nu+1}{2}\right) - \ln \Gamma\left(\frac{\nu}{2}\right) - \frac{1}{2}\ln(\pi(\nu-2)\sigma_t^2) - \frac{\nu+1}{2}\ln\left(1 + \frac{\varepsilon_t^2}{(\nu-2)\sigma_t^2}\right) \right]$$
>
> $\nu$ 越小尾部越厚，$\nu \to \infty$ 退化为正态。
>
> ---
>
> ## 七、模型诊断
>
> 估计完之后，检验标准化残差 $\hat{z}_t = \varepsilon_t / \hat{\sigma}_t$ 是否"干净"：
>
> ```
> 1. Ljung-Box 检验 z²_t 的自相关  → 检验 ARCH 效应是否消除
> 2. 正态性检验（JB 检验）         → 看分布假设对不对
> 3. ARCH-LM 检验残差              → 还有没有剩余异方差
> 4. Q-Q 图                        → 肥尾是否被 t 分布充分捕捉
> ```
>
> ---
>
> ## 八、预测
>
> GARCH(1,1) 的 $h$ 步前向方差预测：
>
> $$\sigma_{t+h|t}^2 = \bar{\sigma}^2 + (\alpha + \beta)^{h-1}(\sigma_{t+1|t}^2 - \bar{\sigma}^2)$$
>
> - 短期：由当前波动率水平决定
> - 长期：向无条件方差 $\bar{\sigma}^2$ 均值回归
> - 回归速度：由 $(\alpha + \beta)$ 决定——越接近 1，回归越慢
>
> ---
>
> ## 九、金融应用一览
>
> | 应用场景 | 具体用途 |
> |----------|----------|
> | **VaR / ES** | 用 $\sigma_{t+1\|t}$ 计算动态风险价值 |
> | **期权定价** | GARCH-option pricing（Duan 1995） |
> | **配对交易** | 动态归一化价差，自适应阈值 |
> | **组合优化** | DCC-GARCH 提供时变协方差矩阵 |
> | **宏观研究** | 识别不确定性区制，研究波动率与实体经济关系 |
>
> ---
>
> 想继续深挖哪个方向？比如 MLE 的数值优化细节、DCC 的两步估计、还是 GARCH 在中国债券市场的实证应用？
<!-- UID: 019f02bb-d166-72e2-8278-ef225e1d2998 -->

---
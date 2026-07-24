---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: tanh函数的含义
conversation_id: de0f52f6-c4cf-4a94-8680-8e20221a0fa8
create_time: 2026-06-24T15:55:37.000Z
update_time: 2026-06-24T15:55:45.000Z
---
# Title: tanh函数的含义

Created: 2026/06/24 at 23:55:37
Last Updated: 2026/06/24 at 23:55:45
Chat URL: https://claude.ai/chat/de0f52f6-c4cf-4a94-8680-8e20221a0fa8


>[!nexus_user] **User** - 2026/06/24 at 23:55:37
> `tanh` 这个函数是什么意思
<!-- UID: 019efa58-132c-74d2-b060-30c96dea8662 -->
>[!nexus_agent] **Assistant** - 2026/06/24 at 23:55:45
> `tanh` 是**双曲正切函数**（hyperbolic tangent），定义为：
>
> $$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$
>
> 也可以写成：
>
> $$\tanh(x) = \frac{\sinh(x)}{\cosh(x)}$$
>
> **关键性质：**
>
> - 输出范围：$(-1, 1)$，即值永远在 -1 和 1 之间
> - $\tanh(0) = 0$，函数关于原点对称（奇函数）
> - 单调递增，$x \to +\infty$ 时趋近 1，$x \to -\infty$ 时趋近 -1
> - 导数：$\tanh'(x) = 1 - \tanh^2(x)$，在 $x=0$ 时斜率最大为 1
>
> **和 sigmoid 的关系：**
>
> $$\tanh(x) = 2\sigma(2x) - 1$$
>
> 其中 $\sigma$ 是 sigmoid 函数。可以说 tanh 是 sigmoid 的"零中心化"版本，输出均值为 0 而非 0.5。
>
> **常见用途：**
>
> - **神经网络激活函数**：比 sigmoid 更常用，因为输出以 0 为中心，梯度更新更稳定
> - **信号处理**：压缩任意实数到 $(-1,1)$ 区间
> - **统计/物理**：双曲函数族（sinh、cosh、tanh）在很多物理方程中天然出现
>
> 你是在哪个场景下看到这个函数的？
<!-- UID: 019efa58-132d-755f-a6b1-3a1968895f80 -->

---
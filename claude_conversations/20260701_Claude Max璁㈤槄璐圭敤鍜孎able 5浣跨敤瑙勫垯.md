---
title: "Claude Max订阅费用和Fable 5使用规则"
created: 2026-07-01 06:05
updated: 2026-07-01 06:12
messages: 8
source: claude
tags: [claude-conversation]
---

# Claude Max订阅费用和Fable 5使用规则

## 🧑 User  <small>2026-07-01 06:05</small>

未来一段时间内我是这个ClaudeMax的用户它FIber5现在后面怎么收费的最新要马上恢复的模型对我还能持续用吗还有现在什么样的规定

## 🤖 Claude  <small>2026-07-01 06:06</small>


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

好的，现在情况非常清晰了，给你一个完整梳理：

---

## Claude Max 订阅费用

Claude Max 有两个档次：$100/月（5x，相当于 Pro 用量的5倍）和 $200/月（20x，相当于 Pro 的20倍）。

Max 计划**目前不提供年付折扣**，只有按月付费。

Max 的用量限制是按周计算的——有一个全模型通用的周上限，和一个专门针对 Sonnet 模型的周上限，每周固定时间重置。你可以在 Settings > Usage 里看到重置时间。

---

## Fable 5 的来龙去脉（重点）

这是最近最大的新闻：

Anthropic 于6月9日发布了 Claude Fable 5（其有史以来能力最强的公开模型），但仅三天后的6月12日，美国政府发布出口管制指令，以国家安全为由要求暂停所有外国公民访问 Fable 5 和 Mythos 5。由于 Anthropic 无法实时验证用户国籍，只好对全球所有用户关闭了这两个模型。

**现在（7月1日）的最新状态：**

**好消息：Fable 5 已于7月1日恢复全球访问。** 商务部于6月30日解除了出口管制，Anthropic 在7月1日恢复了 Fable 5 和 Mythos 5 在英国、欧洲、印度、Claude Code 及 API 的访问。

---

## 对你作为 Max 用户的影响

Anthropic 此前声明，在 Fable 5 短暂封禁期间，订阅计划（Pro、Max、Team 等）在6月9日至22日可以免费使用 Fable 5；6月23日起改为需要消耗 usage credits。封禁解除后，Anthropic 计划尽快将 Fable 5 恢复为订阅计划的标准权益。

简而言之：**今天（7月1日）起 Fable 5 已经回来了**，作为 Max 用户你可以正常使用，当前你对话中使用的是 Claude Sonnet 4.6。Opus 4.8 和 Sonnet 4.6 在整个封禁期间都没有受影响，可以持续使用。

## 🧑 User  <small>2026-07-01 06:07</small>

不是之前好像听说他是我看你们最新规定什么是不是要按什么定流量或者API来

## 🤖 Claude  <small>2026-07-01 06:07</small>

 
```
This block is not supported on your current device yet.
```

明白了，你问的正是这个机制。让我解释清楚：

---

## 你听到的"按用量/credits计费"是真实的

这是 **Fable 5 专属的计费变化**，不影响 Opus/Sonnet/Haiku。

**时间线：**

Fable 5 在6月9日至22日期间，对 Pro、Max、Team 等订阅用户免费包含在内。6月23日起，这个窗口关闭——继续使用 Fable 5 需要消耗"usage credits"，按 API 费率计费，即每百万 input token $10、output token $50。

---

## 这个"credits"机制是什么意思

一个粗略的估算是，每个订阅计划每月包含的 credits 大致等于其月费金额：Pro 约 $20 的 credits，Max 5x 约 $100，Max 20x 约 $200。

6月22日之前，claude.ai 的 Pro/Max/Team 用量上限比较模糊，实际上是一个 token 预算但不透明。6月22日之后，你能看到明确的 credit 余额显示，包括已用量、总量、重置日期。

也就是说：**你的 Max 月费本身不变，但 Fable 5 是"额外消费"，用多少扣多少 credits，超出就需要额外付钱。Opus 4.8 / Sonnet 4.6 / Haiku 4.5 这些模型还是正常包含在月费里的。**

---

## 今天（7月1日）的现状

好消息是，商务部6月30日解除了出口管制，Fable 5 今天（7月1日）已经全球恢复访问。

但 credits 计费的规则目前仍然适用——Anthropic 说等产能跟上会把 Fable 5 重新纳入订阅包含范围，但没有给出具体日期。

**简单总结：作为 Max 用户，日常用 Opus/Sonnet 完全不受影响，该用多少用多少。Fable 5 如果要用，现在是按 token 额外计费的。**

## 🧑 User  <small>2026-07-01 06:07</small>

我是问最新7月1号开始有个新的规定好像有个5什么用量的也是针对这个FIverr5的你看一看

## 🤖 Claude  <small>2026-07-01 06:08</small>

 
```
This block is not supported on your current device yet.
```

找到了！这就是你说的最新规定，来自Anthropic官方今天（7月1日）的公告：

---

## 7月1日起的最新Fable 5规定

**7月1日至7月7日**：Pro、Max、Team 及部分 Enterprise 订阅用户，Fable 5 **包含在订阅内，但每周最多只能用到你周用量上限的50%**。

**7月8日起**：这个50%的免费窗口关闭，继续使用 Fable 5 就需要额外消耗 usage credits（按 token 计费）。

所以你听到的"5什么用量"就是这个——**50%的周用量限额**，只到7月7日。

---

**对你作为 Max 用户的实际意义：**

- 本周（7月1日~7日）：用 Fable 5 正常，但消耗速度比 Opus 快约2倍，且不能超过你每周总额度的一半
- 7月8日之后：用 Fable 5 就要额外付钱（credits），Opus 4.8 / Sonnet 4.6 不受影响，照常包含在 Max 月费里

## 🧑 User  <small>2026-07-01 06:12</small>

现在已经可以开始用了吗

## 🤖 Claude  <small>2026-07-01 06:12</small>

 是的，**今天（7月1日）已经可以用了。**

Anthropic 宣布 Fable 5 从今天（7月1日，周三）起，对全球用户在 Claude.ai、Claude Code、Claude Cowork 上恢复访问。

你现在去 claude.ai 的模型选择里应该能看到 Fable 5 了。记住本周还有50%用量限制，下周三（7月8日）起就要额外付 credits 了。

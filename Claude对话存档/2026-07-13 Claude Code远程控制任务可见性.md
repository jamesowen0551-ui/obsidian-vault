---
title: "Claude Code远程控制任务可见性"
created: 2026-07-13 09:56
updated: 2026-07-13 10:30
messages: 25
uuid: 6316d194-2309-47f7-bb30-91e2cb294962
source: claude.ai
tags:
  - claude对话
---

# Claude Code远程控制任务可见性

> [!abstract] 摘要
> **Conversation Overview**
>
> The person asked a series of questions about Claude Code's Remote Control (RC) feature, specifically focused on session visibility across different interfaces. The conversation covered whether the VS Code extension can see RC sessions opened in other terminals, what the `claude.ai/code` browser interface connection prompt means, and how session scope works when using `/web-setup` or RC mode.
>
> Through the conversation, it became clear that the person has multiple active RC sessions running simultaneously and uses the Claude Desktop app as their primary interface, where they can see all active RC sessions listed. They discovered that the browser interface (`claude.ai/code`) was showing a "Connect your terminal" prompt rather than their session list, and they were trying to understand why. Claude explained that the browser likely needs a one-time manual connection via a session URL or `/rc` command to authenticate before it can display the session list, and that only one such connection is needed rather than one per active session.
>
> The person uses domain-specific terminology fluently (RC, `/web-setup`, `/rc`, Remote Control, sessions) and asks focused, iterative follow-up questions to clarify specific details. They also asked about alternative interfaces that support the same multi-session listing functionality that Desktop provides, and Claude outlined that the Claude mobile app (iOS/Android) and `claude.ai/code` browser both support this, with the browser requiring the initial manual connection step. The conversation ended with the person asking whether session URLs are visible from within the Desktop app itself, which Claude answered affirmatively but with a caveat about uncertainty regarding exact UI details.

## 👤 我 · 2026-07-13 09:56

Claude Code for VS Code可以看到其它终端打开的REMOTE-CONTROL任务吗

## 🤖 Claude · 2026-07-13 09:56

> [!example]- 🔧 工具调用
> 工具：`view`
>
> ```json
> {
>   "description": "Check product self-knowledge skill before answering Claude Code questions",
>   "path": "/mnt/skills/public/product-self-knowledge/SKILL.md"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> 1	---
>      2	name: product-self-knowledge
>      3	description: "Stop and consult this skill whenever your response would include specific facts about Anthropic's products. Covers: Claude Code (how to install, Node.js requirements, platform/OS support, MCP server integration, configuration), Claude API (function calling/tool use, batch processing, SDK usage, rate limits, pricing, models, streaming), and Claude.ai (Pro vs Team vs Enterprise plans, feature limits). Trigger this even for coding tasks that use the Anthropic SDK, content creation mentioning Claude capabilities or pricing, or LLM provider comparisons. Any time you would otherwise rely on memory for Anthropic product details, verify here instead — your training data may be outdated or wrong."
>      4	---
>      5	
>      6	# Anthropic Product Knowledge
>      7	
>      8	## Core Principles
>      9	
>     10	1. **Accuracy over guessing** - Check official docs when uncertain
>     11	2. **Distinguish products** - Claude.ai, Claude Code, and Claude API are separate products
>     12	3. **Source everything** - Always include official documentation URLs
>     13	4. **Right resource first** - Use the correct docs for each product (see routing below)
>     14	
>     15	---
>     16	
>     17	## Question Routing
>     18	
>     19	### Claude API or Claude Code questions?
>     20	
>     21	→ **Check the docs maps first**, then navigate to specific pages:
>     22	
>     23	- **Claude API & General:** https://docs.claude.com/en/docs_site_map.md
>     24	- **Claude Code:** https://docs.anthropic.com/en/docs/claude-code/claude_code_docs_map.md
>     25	
>     26	### Claude.ai questions?
>     27	
>     28	→ **Browse the support page:**
>     29	
>     30	- **Claude.ai Help Center:** https://support.claude.com
>     31	
>     32	---
>     33	
>     34	## Response Workflow
>     35	
>     36	1. **Identify the product** - API, Claude Code, or Claude.ai?
>     37	2. **Use the right resource** - Docs maps for API/Code, support page for Claude.ai
>     38	3. **Verify details** - Navigate to 
> ```

> [!example]- 🔧 工具调用
> 工具：`web_fetch`
>
> ```json
> {
>   "url": "https://docs.anthropic.com/en/docs/claude-code/claude_code_docs_map.md"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> {"error_type": "PERMISSIONS_ERROR", "error_message": "This URL was not in any prior search or fetch result. web_search for it first, then fetch the result link."}
> ```

> [!example]- 🔧 工具调用
> 工具：`web_search`
>
> ```json
> {
>   "query": "Claude Code VS Code extension remote control tasks sessions"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> Remote Control connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone on the couch or a browser on another computer.
>
> On Team and Enterprise, it is off by default until an Owner enables the Remote Control toggle in Claude Code admin settings. Remote Control connects claude.ai/code or the Claude app for iOS and Android to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone on the couch or a browser on another computer. When you start a Remote Control session on your machine, Claude keeps running locally the entire time, so nothing moves to the cloud. With Remote Control you can: Use your full local environment remotely: your filesystem, MCP servers, tools, and project configuration all stay available, and typing @ autocompletes file paths from your local project · Work from both surfaces at once: the conversation stays in sync across all connected devices, so you can send messages from your terminal, browser, and phone interchangeably ·
>
> Remote Control and Claude Code on the web both use the claude.ai/code interface. The key difference is where the session runs: Remote Control executes on your machine, so your local MCP servers, tools, and project configuration stay available. Claude Code on the web executes in Anthropic-managed cloud infrastructure. Use Remote Control when you’re in the middle of local work and want to keep going from another device. Use Claude Code on the web when you want to kick off a task without any local setup, work on a repo you don’t have cloned, or run multiple tasks in parallel. When Remote Control is active, Claude can send push notifications to your phone. Claude decides when to push. It typically sends one when a long-running task finishes or when it needs a decision from you to continue. You can also request a push in your prompt, for example notify me when the tests f
> ```

> [!example]- 🔧 工具调用
> 工具：`web_fetch`
>
> ```json
> {
>   "url": "https://code.claude.com/docs/en/remote-control",
>   "html_extraction_method": "markdown"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> > ## Documentation Index
> > Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> > Use this file to discover all available pages before exploring further.
>
> # Continue local sessions from any device with Remote Control
>
> > Continue a local Claude Code session from your phone, tablet, or any browser using Remote Control. Works with claude.ai/code and the Claude mobile app.
>
> <Note>
>   Remote Control is in research preview and available on all plans. On Team and Enterprise, it is off by default until an Owner enables the Remote Control toggle in [Claude Code admin settings](https://claude.ai/admin-settings/claude-code).
> </Note>
>
> Remote Control connects [claude.ai/code](https://claude.ai/code) or the Claude app for [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) to a Claude Code session running on your machine. Start a task at your desk, then pick it up from your phone on the couch or a browser on another computer.
>
> When you start a Remote Control session on your machine, Claude keeps running locally the entire time, so nothing moves to the cloud. With Remote Control you can:
>
> * **Use your full local environment remotely**: your filesystem, [MCP servers](/en/mcp), tools, and project configuration all stay available, and typing `@` autocompletes file paths from your local project
> * **Work from both surfaces at once**: the conversation stays in sync across all connected devices, so you can send messages from your terminal, browser, and phone interchangeably
> * **Send images and files from your phone or browser**: when you add an attachment in the Claude app or at claude.ai/code, Claude Code downloads it to your machine and passes it to Claude as an `@` file reference, with or without a caption. {/* min-version: 2.1.202 */}Before v2.1.202, Claude Code could drop an attachment sent without a caption before it reached the session.
> * **Survive interru
> ```

这个问题涉及两个不同的概念，需要分开来说清楚：

---

**问题的核心：VS Code 扩展能否看到"其它终端"开启的 Remote Control 会话？**

答案是：**不能直接在 VS Code 扩展内看到**，但可以通过其他方式连接。

---

**Session 的归属逻辑**

每个 Claude Code 进程（无论是 CLI 还是 VS Code 扩展）在 Remote Control 激活时，只能承载一个远程会话。VS Code 扩展和终端 CLI 是两个独立的进程，各自维护自己的会话。

也就是说：
- 终端 A 开启的 Remote Control 会话 → 属于那个 CLI 进程
- VS Code 扩展开启的 Remote Control 会话 → 属于 VS Code 的那个进程
- **两者之间是相互独立的，VS Code 扩展无法"接管"或"看到"终端开启的会话**

---

**那如何从其他设备看到终端里开启的 Remote Control 会话？**

通过 `claude.ai/code` 或 Claude 手机 App（iOS/Android），可以列出所有 Remote Control 会话——包括 CLI 终端和 VS Code 扩展分别开启的会话，都会出现在会话列表里。

所以正确的跨设备查看方式是：**用浏览器或手机 App 访问 `claude.ai/code`**，而不是在另一个 VS Code 扩展里找。

---

**VS Code 扩展的 Remote Control 有什么限制？**

在 VS Code 扩展里输入 `/remote-control`（或 `/rc`）可以启动会话，会话状态栏会显示连接状态，并提供"Open in browser"按钮跳转到 `claude.ai/code`。但与 CLI 相比，VS Code 不支持名称参数（`--name`），也不显示二维码。

---

**实际情况总结**

| 场景 | 可见性 |
|------|--------|
| 终端 A 开的 RC 会话，在终端 B 里看 | ❌ 不行 |
| 终端 A 开的 RC 会话，在 VS Code 扩展里看 | ❌ 不行 |
| 终端 A 开的 RC 会话，在 `claude.ai/code` 里看 | ✅ 可以 |
| VS Code 扩展开的 RC 会话，在 `claude.ai/code` 里看 | ✅ 可以 |
| 统一管理多个并发会话 | ✅ 用 `claude remote-control`（server mode）+ `claude.ai/code` |

如果你需要同时管理多个会话，建议用 CLI 的 **server mode**（`claude remote-control`），然后通过 `claude.ai/code` 统一查看和切换。

## 👤 我 · 2026-07-13 10:00

Connect your terminal
Already have Claude Code? You’re one command away.
claude — zsh
✳Welcome to Claude Code
cwd: ~/projects
>/web-setup
Open Claude Code and run `/web-setup` to connect.
Connect a different way 这是什么意思啊

## 🤖 Claude · 2026-07-13 10:00

这是 **claude.ai/code** 网页界面的引导提示，意思是：

**你还没有把本地的 Claude Code 终端连接到这个浏览器页面。**

---

**它在让你做什么？**

网页在等你在本地终端里运行 `/web-setup` 命令，建立一个从本地机器 → 浏览器的连接。

这对应两种使用场景：

1. **Remote Control**：你本地已经有 Claude Code 在运行，想从浏览器里遥控它
2. **Claude Code on the web**：直接在 Anthropic 云端跑（不需要本地 Claude Code），但仍需先配置

---

**具体怎么操作？**

如果你本地已经安装了 Claude Code，在终端里运行：

```bash
/web-setup
```

或者直接开启带 Remote Control 的会话：

```bash
claude --remote-control
```

然后用浏览器打开终端里显示的 URL，就连上了。

---

**"Connect a different way" 是什么？**

点那个链接通常会提供其他连接方式，比如：
- 扫描二维码（手机 App 连接）
- 手动输入 session URL
- 使用 Claude Code on the web（云端模式，不需要本地终端）

---

**简单说**：你看到的界面就是在等一个来自本地终端的连接信号，还没连上所以显示这个引导页。

## 👤 我 · 2026-07-13 10:01

/web-setup 是开了之后可以看到所有对话，还是就那一个啊

## 🤖 Claude · 2026-07-13 10:01

**就那一个会话**，不是所有对话。

---

`/web-setup` 本质上是把**当前这个终端进程**的会话暴露给浏览器。每个终端窗口/进程是独立的，所以：

| 情况 | 浏览器里看到什么 |
|------|-----------------|
| 终端 A 运行 `/web-setup` | 只看到终端 A 的会话 |
| 终端 B 也运行 `/web-setup` | 终端 B 的会话也会出现在列表里 |
| 历史对话（已关闭的终端） | ❌ 看不到 |

---

**如果想在浏览器里看到多个并发会话**，需要每个终端分别运行 `/web-setup` 或 `--remote-control`，然后在 `claude.ai/code` 的会话列表里切换。

**历史对话记录**的话，要用 `claude --resume` 在本地终端恢复，不能直接从浏览器浏览过去的对话。

## 👤 我 · 2026-07-13 10:07

但是我很多对话开了REMOTE-CONTROL啊

## 🤖 Claude · 2026-07-13 10:07

那你在 `claude.ai/code` 的会话列表里就能看到**所有当前还在运行的** Remote Control 会话，可以在它们之间切换。

关键点是：

- **还在跑的终端进程** → 会话列表里有，可以从浏览器接管
- **已经关掉的终端** → 会话自动下线，列表里消失

所以你打开 `claude.ai/code`，应该能看到一个列表，显示你所有活跃的 Remote Control 会话，点哪个就进哪个，不是只有一个。

## 👤 我 · 2026-07-13 10:09

Connect your terminal
Already have Claude Code? You’re one command away.
claude — zsh
✳Welcome to Claude Code
cwd: ~/projects
>/web-setup
Open Claude Code and run `/web-setup` to connect.
Connect a different way 但是在浏览器点CODE只出现这个

## 🤖 Claude · 2026-07-13 10:09

这说明你的浏览器目前**没有检测到任何活跃的 Remote Control 会话**。

可能的原因：

**1. 你的终端开的是普通会话，不是 Remote Control**
普通的 `claude` 会话不会出现在浏览器里，必须显式开启 Remote Control 才行。检查一下终端底部状态栏有没有 `/rc active` 的字样。

**2. 账号不一致**
终端里登录的 claude.ai 账号和浏览器里登录的不是同一个，会话对不上。

**3. 会话已经断开**
终端虽然开着，但网络中断超过约10分钟的话会话会自动超时退出。

---

**最快的验证方法**：

在你某个终端里输入：
```
/rc
```
然后看终端里有没有出现一个 URL，有的话复制到浏览器直接打开，就能连上那个会话了。

## 👤 我 · 2026-07-13 10:10

但是我在桌面版看得到所有开了RC的对话

## 🤖 Claude · 2026-07-13 10:10

哦，那就清楚了！

**桌面版（Claude Desktop）和浏览器是两个不同的入口**，你在桌面版能看到所有 RC 会话，但浏览器的 `claude.ai/code` 没有自动同步过来。

这是正常现象，不是 bug。浏览器版需要你手动连接一次才能识别到会话。

最简单的解决方式就是在任意一个已经开了 RC 的终端里运行 `/rc`，复制那个 URL，直接在浏览器里打开，就能在浏览器里接入那个会话了。

或者就直接用桌面版，功能是一样的，没必要非得用浏览器。

## 👤 我 · 2026-07-13 10:11

那桌面版的这种功能，还有什么地方可以实现啊

## 🤖 Claude · 2026-07-13 10:11

根据官方文档，能看到所有 RC 会话列表的入口有这几个：

| 入口 | 是否支持 |
|------|---------|
| Claude 桌面版（Desktop App） | ✅ 你已经在用 |
| Claude 手机 App（iOS/Android）→ Code 标签 | ✅ 支持 |
| `claude.ai/code`（浏览器） | ✅ 支持，但需要先手动连接一次 |

---

你浏览器那边显示引导页，可能只是还没建立过连接，所以它不知道你有 RC 会话。试一下在任意一个 RC 终端里跑 `/rc`，拿到 URL 在浏览器打开一次，之后应该就能正常看到列表了。

手机 App 是最方便的补充——打开 App 点底部 **Code** 标签，所有活跃 RC 会话直接列出来，随时可以接管。

## 👤 我 · 2026-07-13 10:11

先手动连接一次，是所有对话都得连吗，活跃的

## 🤖 Claude · 2026-07-13 10:11

不用每个都连，**只需要连一次任意一个**就够了。

浏览器确认你的身份和机器之间能通信之后，`claude.ai/code` 的会话列表就会刷新，显示所有活跃的 RC 会话。

随便找一个终端跑 `/rc`，把 URL 丢进浏览器，之后列表就出来了。

## 👤 我 · 2026-07-13 10:12

OpenClaude-Portable这个能替代吗

## 🤖 Claude · 2026-07-13 10:12

这个名字我没有把握——不在我的知识库里，也可能是第三方工具或者非官方封装版。

你是在哪里看到这个的？App Store、GitHub、还是别的地方？知道来源的话我可以帮你判断一下。

## 👤 我 · 2026-07-13 10:13

GitHub

## 🤖 Claude · 2026-07-13 10:13

我没有关于这个项目的可靠信息，帮你搜一下。

> [!example]- 🔧 工具调用
> 工具：`web_search`
>
> ```json
> {
>   "query": "OpenClaude-Portable GitHub"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> Run Claude Code from a USB drive on any PC — no installation required. - techjarves/OpenClaude-Portable
>
> Running a local model on CPU or USB 2.0 is inherently slower than a cloud API. The built-in speed proxy (tools/local-proxy.js) intercepts every request and trims the OpenClaude system prompt from ~10 000 tokens down to ~300 tokens before it reaches Ollama. Typical result: first-token latency drops from 60–120 s to 5–20 s on CPU-only hardware. Proxy activity is logged silently to data/proxy.log — it never writes to the terminal. ... For best performance, copy data/ollama/ to your local SSD if USB 2.0 read speeds are the bottleneck. Zero Footprint — XDG_CONFIG_HOME, XDG_DATA_HOME, and CLAUDE_CONFIG_DIR are all redirected to data/, keeping the host system clean. No Telemetry — Nothing is sent anywhere except your chosen AI provider. API Key Safety — Keys are stored only in data/ai_settings.env on your drive. Approval Mode — In Normal Mode the agent asks before any file write or shell command.
>
> OpenClaude Multi-Platform is a fully portable AI coding agent powered by the open-source OpenClaude engine. It bundles a self-contained Node.js runtime, a smart system-prompt proxy for local models, and a web-based dashboard — all configurable from a single START.bat (Windows) or start.sh (Linux/macOS). Everything runs strictly inside the project folder. No files are written to the host machine. ... NVIDIA NIM · DeepSeek · OpenRouter · Google Gemini · Anthropic Claude · OpenAI · Ollama (offline) · LM Studio · Custom OpenAI-compatible API ... Trims system prompts by up to 90% before sending to Ollama, dramatically improving response time on CPU-only hardware ... On first run it automatically downloads Node.js (~25 MB) and the OpenClaude engine (~5 MB), then walks you through provider selection. Every subsequent launch skips setup and goes straight to the menu.
>
> Check engine/node-download.log, allow curl through antivirus/firewall, or install Node.js manually from nodejs.org/dow
> ```

**不能替代**，这是两个完全不同的东西。

OpenClaude-Portable 是一个第三方开源项目，核心功能是让你把 Claude Code 环境装在 U 盘上，插到任何电脑都能跑，不需要在主机上安装任何东西。

它跟你问的"查看所有 RC 会话列表"完全没有关系，也没有这个功能。

你的需求（在一个地方看到所有开了 RC 的对话）只有这几个官方入口能做到：

- ✅ Claude 桌面版（你已经在用，能看到）
- ✅ Claude 手机 App → Code 标签
- ✅ `claude.ai/code`（浏览器，需要先连一次）

OpenClaude-Portable 解决的是完全不同的问题，跟 RC 会话管理无关。

## 👤 我 · 2026-07-13 10:24

RC 会话管理还有什么可以实现吗

## 🤖 Claude · 2026-07-13 10:24

根据官方文档，能查看和管理所有活跃 RC 会话的入口就只有这三个：

| 入口 | 状态 |
|------|------|
| Claude 桌面版 | ✅ 你已经在用 |
| Claude 手机 App（Code 标签） | ✅ 官方支持 |
| `claude.ai/code`（浏览器） | ✅ 需要先连一次 |

没有其他第三方工具能做到这件事，因为 RC 会话列表是通过 Anthropic 的账号体系同步的，第三方工具拿不到这个数据。

---

所以实际上你已经在用最完整的方案了（桌面版）。手机 App 是唯一额外的补充，如果你需要离开桌面时也能管理的话。

## 🤖 Claude · 2026-07-13 10:24

不需要每个都连。

只要**任意一个** RC 会话用 URL 在浏览器里打开过一次，浏览器就认出你的账号了，之后 `claude.ai/code` 的会话列表里应该就能看到所有活跃的 RC 会话了。

就是一个账号验证/认证的问题，连一次就够了。

## 👤 我 · 2026-07-13 10:30

我在桌面版里能看到URL吗

## 🤖 Claude · 2026-07-13 10:30

能，点进某个 RC 会话里，应该能看到那个会话的 URL 或者一个"Open in browser"之类的按钮，点一下就能在浏览器里打开了。

不过我对桌面版的具体 UI 细节不是百分百确定，你可以找一下会话里有没有类似的链接或按钮。如果找不到，最保险的方式还是去对应的终端里跑一下 `/rc`，URL 会直接打印出来。

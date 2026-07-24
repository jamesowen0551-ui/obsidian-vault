---
title: "Claude Code命令行安装方法"
created: 2026-07-10 15:09
updated: 2026-07-10 15:30
messages: 24
uuid: 90dc2f74-d764-4fb1-aa6c-559b5330e172
source: claude.ai
tags:
  - claude对话
---

# Claude Code命令行安装方法

> [!abstract] 摘要
> **Conversation Overview**
>
> The person was troubleshooting how to access Claude Code's Remote Control functionality after losing the ability to use the Claude Code desktop application on their local Windows machine due to lacking administrator privileges. They initially asked about command-line installation of Claude Code, which led to clarification that the CLI tool (`@anthropic-ai/claude-code` via npm) and the desktop application are distinct products. The person's actual use case emerged through the conversation: they had been using the Claude Code desktop app to connect to a remote machine running Claude Code in remote/CLI mode, and needed an alternative way to maintain that connection without desktop app access.
>
> Claude explored several potential workarounds, including using the web version (claude.ai), SSH into the remote machine, and VS Code Remote SSH. The person confirmed they are on Windows, and Claude walked through how SSH works conceptually and how to find the necessary IP address and username via `ipconfig` and `whoami` commands on the remote machine. However, it became clear that neither the local machine nor the remote machine has administrator privileges available to the person, which blocked both installing the desktop app locally and enabling OpenSSH Server on the remote Windows machine (which requires admin rights).
>
> The conversation concluded without a technical solution. Claude suggested the most viable paths forward are using the web version for general chat (accepting the loss of Remote Control functionality) or escalating to IT to request either desktop app installation or SSH access setup on the relevant machines. The person communicates in simplified Chinese and needed foundational explanations of networking concepts like SSH, indicating a preference for plain-language, step-by-step guidance rather than assumed technical familiarity.

## 👤 我 · 2026-07-10 15:09

Claude code终端能用命令行安装吗

## 🤖 Claude · 2026-07-10 15:09

可以的。Claude Code 是一个命令行工具，通过 npm 安装：

```bash
npm install -g @anthropic-ai/claude-code
```

安装后运行：

```bash
claude
```

需要 **Node.js 18+**。首次运行会引导你完成 API 密钥认证。

如果你用的是 macOS/Linux 且遇到权限问题，可以用 `sudo` 或配置 npm 全局目录到用户目录下。

## 👤 我 · 2026-07-10 15:09

你这个是插件吧

## 🤖 Claude · 2026-07-10 15:09

不是插件，`@anthropic-ai/claude-code` 是一个**独立的命令行工具（CLI）**，安装后直接在终端里用，不依附于任何编辑器。

不过它也可以作为插件集成到编辑器里，比如 VS Code 有对应的扩展。两种用法都支持：

- **纯终端**：直接跑 `claude` 命令，在任何目录下使用
- **编辑器集成**：作为 VS Code / JetBrains 插件使用

你是想在哪个环境下用？

## 👤 我 · 2026-07-10 15:09

我的意思是用终端命令，安装桌面版

## 🤖 Claude · 2026-07-10 15:09

桌面版 Claude 目前**不支持命令行安装**，只能去官网手动下载安装包：

👉 [claude.ai/download](https://claude.ai/download)

支持 macOS、Windows、Linux。

如果你是想在终端里用 AI 编程助手，那 Claude Code（`npm install -g @anthropic-ai/claude-code`）才是命令行工具。两个是不同的产品。

## 👤 我 · 2026-07-10 15:10

桌面版安装需要管理员权限，我暂时没有，怎么办

## 🤖 Claude · 2026-07-10 15:10

没有管理员权限的话，有几个替代方案：

**1. 直接用网页版**
浏览器打开 [claude.ai](https://claude.ai)，功能和桌面版基本一样，不需要安装任何东西。

**2. 用 Claude Code（不需要管理员权限）**
如果你有 Node.js 环境，npm 全局安装到用户目录不需要管理员权限：
```bash
npm install -g @anthropic-ai/claude-code
```

**3. 找 IT 申请权限**
如果是公司电脑，可以让 IT 帮你安装桌面版。

最省事的还是直接用网页版，体验几乎一样。

## 👤 我 · 2026-07-10 15:11

网页版好像没法看到远程的Claude code对吧

## 🤖 Claude · 2026-07-10 15:11

对，网页版 claude.ai 和 Claude Code 是完全独立的，网页版看不到 Claude Code 的终端会话。

你的需求是想**在没有管理员权限的机器上，通过某种界面访问远程的 Claude Code**？

可以说说你的具体场景，比如：
- 远程服务器上跑着 Claude Code，想在本地看到它？
- 还是别的情况？

## 👤 我 · 2026-07-10 15:11

不是啊，我的意思是终端的Claude code能看到开了remote control的东西，但是网页版不行

## 🤖 Claude · 2026-07-10 15:12

明白了！你说的是 Claude Code 的 **MCP（Model Context Protocol）** 或者远程连接功能，比如连接到远程服务器、数据库、或者其他开了 remote 的工具。

这些确实只有 Claude Code CLI 能用，网页版 claude.ai 没有这个能力。

所以你的核心问题还是回到：**没有管理员权限装不了桌面版，但需要用 Claude Code**？

如果是这样，最直接的解法就是用 Claude Code CLI（`npm install -g @anthropic-ai/claude-code`），它本身就是终端工具，不需要桌面版，也不需要管理员权限（只要有 Node.js）。

你现在机器上有 Node.js 吗？

## 👤 我 · 2026-07-10 15:12

不是，我目前是用桌面版cc远程控制其他电脑开了remote control的 cli

## 🤖 Claude · 2026-07-10 15:13

哦明白了！你的场景是：

- 本机装了 **Claude Code 桌面版**
- 远程机器开了 **Claude Code remote** 模式
- 桌面版可以连过去控制远程机器

现在本机桌面版装不上（没管理员权限），想找替代方案继续连远程的 Claude Code CLI？

我需要查一下 Claude Code remote 这个功能的具体细节，稍等。

> [!example]- 🔧 工具调用
> 工具：`view`
>
> ```json
> {
>   "path": "/mnt/skills/public/product-self-knowledge/SKILL.md",
>   "description": "Check product knowledge for Claude Code remote features"
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
>   "query": "Claude Code remote development SSH connection docs"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> Claude Code SSH lets you now point Claude Code directly at any remote server and have it work with the actual environment where your code is located. It sounds complicated, but it&#x27;s not as I will demonstrate in this post step by step.
>
> Recently, Claude Code added SSH support on the Claude Code desktop app, and I realized most of my readers don’t even know what this means…
>
> If you are a serious Claude Code user and don’t understand how Claude Code SSH works, you are leaving a lot on the table — and I will demonstrate this in this article. Most developers have code living somewhere other than their local machine — a cloud server, a remote dev box, or a staging environment. Before SSH support, you had to be at your local machine with everything installed and configured just right. Claude Code SSH lets you now point Claude Code directly at any remote server and have it work with the actual environment where your code is located. It sounds complicated, but it's not as I will demonstrate in this post step by step. I will show you the two ways Claude Code SSH works, walk you through setting it up, and demonstrate it live on a real remote server so you can see what it looks like in practice. If you are new here, check out my other Claude Code tutorials here and do not forget to follow me HERE on Medium so that you…
> The SSH Remote Connection skill enables Claude to interact directly with remote servers to perform critical DevOps tasks such as monitoring logs, managing Docker containers, and restarting services.
>
> Manage remote servers and Docker containers using Claude Code. Execute commands, check logs, and automate infrastructure tasks via secure SSH.
> And since everything runs in Docker, the workspace and Claude&#x27;s context persist. Start a session on your laptop, continue from your phone using Termius—it all just works. The setup is surprisingly straightforward. Here&#x27;s what we&#x27;re building: ... The clever bit is in how we handle the shell. When you SSH in,
> ```

现在清楚了。你用的是 桌面版 Claude Code 的 Remote Control 功能，现在本机装不了桌面版，想继续访问远程机器。

有几个替代方案：

**1. 直接 SSH 进远程机器跑 CLI（最简单）**
只要本机有终端（Windows 用 PowerShell/WSL，Mac/Linux 原生），直接：
```bash
ssh user@remote-ip
claude
```
配合 `tmux` 保持会话不断开。不需要任何管理员权限。

**2. 用 Claude Code 网页版（如果有的话）**
Remote Control 功能是 2026 年 2 月 25 日上线的，主要针对移动端/远程访问场景。可以查一下你的账号是否支持 Claude Code on the web。

**3. VS Code Remote SSH**
本地装 VS Code（不需要管理员权限，可以装到用户目录），通过 Remote SSH 插件连到远程机器，再在 VS Code 终端里跑 `claude`。

---

最推荐的是**方案1**——直接 SSH + tmux，零依赖，本机什么都不用装。你现在本机有 SSH 客户端可以用吗？

## 👤 我 · 2026-07-10 15:13

Ssh什么意思呢

## 🤖 Claude · 2026-07-10 15:13

SSH（Secure Shell）就是一种**通过网络远程登录另一台电脑的方式**，像是打开了那台电脑的终端，可以在上面直接敲命令。

打个比方：
- 你的本机 = 遥控器
- 远程电脑 = 电视
- SSH = 遥控信号

连上之后，你在本机终端敲的命令，实际上是在远程电脑上执行的。

---

你现在的情况其实已经在用类似的东西了——桌面版 Claude Code 的 Remote Control 本质上也是连到远程机器去跑。只是现在桌面版装不了，**SSH 是一个不需要装任何额外软件就能连过去的替代方法**。

你本机是 Windows 还是 Mac？

## 👤 我 · 2026-07-10 15:17

Windows

## 🤖 Claude · 2026-07-10 15:18

Windows 10/11 自带 SSH 客户端，不需要安装任何东西，直接在 PowerShell 或命令提示符里就能用：

```powershell
ssh 用户名@远程机器的IP
```

连上之后就相当于在远程机器的终端里了，然后直接跑 `claude` 就行。

---

你知道远程机器的 IP 地址和用户名吗？如果知道的话，我可以一步步带你连过去。

## 👤 我 · 2026-07-10 15:18

怎么查ip和用户名呀

## 🤖 Claude · 2026-07-10 15:18

在**远程那台电脑**上操作：

**查 IP：**
```cmd
ipconfig
```
找 `IPv4 地址`，一般是 `192.168.x.x` 这样的格式。

**查用户名：**
```cmd
whoami
```
会显示 `电脑名\用户名`，取后面那部分就行。

---

不过有个前提：远程那台电脑需要**开启 SSH 服务**才能被连接。你知道那台电脑是 Windows 还是 Linux？

## 👤 我 · 2026-07-10 15:29

Windows

## 🤖 Claude · 2026-07-10 15:29

Windows 默认没开 SSH 服务，需要在**远程那台电脑**上手动开启，步骤如下：

**开启 SSH 服务（不需要管理员权限以外的操作，但需要管理员权限）：**

1. 打开「设置」→「系统」→「可选功能」
2. 搜索 `OpenSSH 服务器`，点击安装
3. 安装完后，打开「服务」（搜索栏搜 `services.msc`）
4. 找到 `OpenSSH SSH Server`，右键→启动，并设为自动

---

不过你说本机没有管理员权限，**远程那台电脑你有管理员权限吗？**

如果远程机器有权限、本机没有的话，上面的操作在远程机器上做就行，本机只用 PowerShell 连过去，不需要任何权限。

## 👤 我 · 2026-07-10 15:30

也没有

## 🤖 Claude · 2026-07-10 15:30

那两台电脑都没管理员权限，SSH 方案就走不通了。

回到最初的问题——你现在唯一能用的其实就是**网页版 claude.ai**，虽然没法连 Remote Control，但日常对话功能都有。

另一个思路是：**找有管理员权限的人帮你**，比如：
- 让 IT 在本机装桌面版 Claude Code
- 或者让远程电脑的管理员开好 SSH，你本机连过去不需要权限

你这个使用场景是工作需要吗？如果是的话，走 IT 申请可能是最稳的路。

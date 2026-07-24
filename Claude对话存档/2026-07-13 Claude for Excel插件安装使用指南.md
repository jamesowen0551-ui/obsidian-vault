---
title: "Claude for Excel插件安装使用指南"
created: 2026-07-13 10:51
updated: 2026-07-13 10:56
messages: 4
uuid: d0af8ff0-3f7b-489c-8c4a-93578d764200
source: claude.ai
tags:
  - claude对话
---

# Claude for Excel插件安装使用指南

> [!abstract] 摘要
> **Conversation Overview**
>
> The person asked about how to install and use the Claude for Excel add-in. Claude provided a comprehensive guide covering prerequisites (Microsoft 365 subscription with work/school account, and a Claude paid plan at Pro tier or above), installation steps for individual users via the Microsoft Marketplace, and enterprise/IT-managed deployment via manifest XML file upload through the Microsoft 365 Admin Center.
>
> The person followed up with a specific question about whether a Microsoft account login is required. Claude clarified that there are two distinct authentication layers: a Microsoft 365 subscription account (required to load the add-in on the Microsoft side) and a Claude paid account (required to activate AI functionality on the Anthropic side). Claude also noted that Microsoft 365 Copilot licensing is not needed, and that organizations using AWS Bedrock, Google Cloud Vertex AI, or LLM gateways can bypass the Claude account requirement through enterprise infrastructure configuration.
>
> The conversation was conducted entirely in Chinese. The person appears to be operating in a corporate domain environment with potential IT admin restrictions, which Claude proactively flagged as a possible friction point for installation—specifically noting that if the Office Store is blocked by IT, the manifest-based deployment path would be necessary.

## 👤 我 · 2026-07-13 10:51

CLAUDE FOR EXCEL插件怎么安装使用啊

## 🤖 Claude · 2026-07-13 10:52

> [!example]- 🔧 工具调用
> 工具：`view`
>
> ```json
> {
>   "description": "Reading the product self-knowledge skill to get accurate info about Claude for Excel",
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
> 工具：`web_search`
>
> ```json
> {
>   "query": "Claude for Excel add-in installation how to use 2025 2026"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> Claude for Excel is available to Pro, Max, Team, and Enterprise plans · Claude for Excel is an add-in that integrates Claude into your Excel workflow. It&#x27;s designed for professionals who work extensively with spreadsheets, particularly in financial analysis and modeling
> Initially launched in beta in October ... Pro subscribers ($20/month). ... Keyboard Shortcut: Open Claude in Excel quickly with Ctrl+Alt+C on Windows or Ctrl+Option+C on Mac. Claude operates in a sidebar panel within Exc...
>
> March 2026 Update: Major update with Shared Context between Excel and PowerPoint, reusable Skills for one-click workflows, MCP Connectors support (S&P Global, LSEG, Daloopa, PitchBook, Moody's, FactSet) and deployment via Amazon Bedrock, Vertex AI and Microsoft Foundry. Claude for Excel is a beta add-in that integrates Anthropic's artificial intelligence directly into Microsoft Excel. It is not just a simple assistant that answers questions: Claude reads, understands, and modifies your spreadsheets while keeping all formulas and dependencies intact. Initially launched in beta in October 2025 for Max and Enterprise plans, since January 24, 2026 Claude for Excel is available to all Pro subscribers ($20/month). ... Keyboard Shortcut: Open Claude in Excel quickly with Ctrl+Alt+C on Windows or Ctrl+Option+C on Mac. Claude operates in a sidebar panel within Excel.
>
> Pasquale Pillitteri 14/02/2026 Claude Code & Anthropic 11 min read · agentic ai claude ai best ai for coding what is ai ai news today claude code ai tools claude excel claude powerpoint claude add-in anthropic excel ai excel ai office tools ... Claude arrives directly in Microsoft Excel and PowerPoint with two official add-ins that transform the way you work with spreadsheets and presentations. Anthropic has brought the power of its AI into the tools you use every day, without having to switch between apps. In this complete guide, you will learn how to install, configure, and get the most out of Claude for Excel and Cla
> ```

> [!example]- 🔧 工具调用
> 工具：`web_fetch`
>
> ```json
> {
>   "url": "https://support.claude.com/en/articles/12650343-use-claude-for-excel",
>   "html_extraction_method": "markdown"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> ---
> canonical: https://support.claude.com/en/articles/12650343-use-claude-for-excel
> meta-baggage: sentry-environment=production,sentry-release=a271dce9c9f054b3c89db3f42733c41612bfe242,sentry-public_key=187f842308a64dea9f1f64d4b1b9c298,sentry-trace_id=b46442a76ca12b76b35282d7c18acc3c,sentry-org_id=2129,sentry-sampled=false,sentry-sample_rand=0.006558352829822756,sentry-sample_rate=0
> meta-description:
> meta-og:description:
> meta-og:image: https://downloads.intercomcdn.com/i/o/lupk8zyo/792494/717b10d3ebd874823db64841659b/76f3062d78ebbb04863fb1de3ef9cca0.png
> meta-og:title: Use Claude for Excel | Claude Help Center
> meta-og:type: article
> meta-robots: all
> meta-sentry-trace: b46442a76ca12b76b35282d7c18acc3c-84467b5a63e30247-0
> meta-twitter:card: summary_large_image
> meta-twitter:description:
> meta-twitter:image: https://downloads.intercomcdn.com/i/o/lupk8zyo/792494/717b10d3ebd874823db64841659b/76f3062d78ebbb04863fb1de3ef9cca0.png
> meta-twitter:title: Use Claude for Excel | Claude Help Center
> meta-viewport: width=device-width, initial-scale=1
> title: Use Claude for Excel | Claude Help Center
> ---
>
> [Skip to main content](#main-content)
>
> [![Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)
>
> [API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)
>
> * English
> Français
> Deutsch
> Bahasa Indonesia
> Italiano
> 日本語
> 한국어
> Português
> Pусский
> 简体中文
> Español
> 繁體中文
>
> English
>
> [API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)
>
> * English
> Français
> Deutsch
> Bahasa Indonesia
> Italiano
> 日本語
> 한국어
> Português
> Pусский
> 简体中文
> Español
> 繁體中文
>
> English
>
> Search for articles...
>
> 1. [All Collect
> ```

直接从官方文档整理给你，信息都是最新的。

---

## Claude for Excel 安装与使用指南

### 一、前提条件

**账号要求：**
需要 Pro、Max、Team 或 Enterprise 订阅计划（免费账号不支持）。

**Excel版本要求：**
支持的版本包括：Excel on Web、Excel on Windows（需 Microsoft 365 订阅，build 16.0.13127.20296 以上）、Excel on Mac（version 16.46+ ）、Excel on iPad（version 2.51+）。**不支持** Excel 2016/2019 永久授权版、Excel for Android。

注意：你之前提到过公司域环境有管理员权限限制——如果 Office Store 被 IT 封锁，安装方式会略有不同（见下方企业部署）。

---

### 二、安装步骤（个人用户）

1. 前往 Microsoft Marketplace 搜索 **"Claude by Anthropic for Excel"**（或直接访问 [这个链接](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview)）
2. 点击 **"Get it now"** 安装插件
3. 打开 Excel，激活插件：
   - Windows：**Home > Add-ins**
   - Mac：**Tools > Add-ins**
4. 用你的 Claude 账号登录

安装后快捷键：Windows 用 **Ctrl+Alt+C**，Mac 用 **Ctrl+Option+C** 直接唤出 Claude 侧边栏。

---

### 三、企业/域环境部署（IT管控情况）

如果公司 IT 禁用了 Office Store，管理员可以通过下载 manifest XML 文件手动部署：
1. 下载 manifest 文件：`https://pivot.claude.ai/manifest-excel.xml`
2. 登录 Microsoft 365 Admin Center（admin.microsoft.com）
3. 进入 **Settings > Integrated apps > Upload custom apps**
4. 选择 "Office Add-in" > "I have a manifest file on this device"，上传 XML 文件
5. 分配用户（全组织 / 特定用户 / 特定组）后点击 Deploy

---

### 四、主要功能（对你的工作特别相关）

Claude for Excel 可以做到：
- 对 workbook 提问，获得带单元格引用的回答
- 修改假设值的同时保持公式依赖关系
- 调试 #REF! / #VALUE! 等错误并定位根源
- 从头构建模型或填充现有模板
- 跨多个 Tab 无缝导航复杂工作表
- 通过 connectors 将外部工具的数据引入表格

财务建模方面的示例 prompt（对你做利率债研究或金融模型很实用）：
- *"Build a 3-statement financial model"*
- *"Add a downside case assuming revenue drops 15%"*  
- *"Create a sensitivity table showing IRR across exit multiples"*
- *"Check that all formulas link correctly across sheets"*

---

### 五、重要限制

目前不支持：Data tables、Macros、VBA。官方不建议用于：需审计的关键计算、对外客户交付物（须人工复核）、含高度敏感受监管数据的模型。

另外要注意的安全风险：只在受信任的表格中使用，不要对外部下载的模板或供应商文件使用——这类文件可能包含隐藏的 prompt injection 指令，诱导 Claude 执行非预期操作。

---

如果你在公司域环境遇到安装问题，告诉我具体的报错信息，我可以帮你判断是 Office 版本、账号权限还是 IT 策略的问题。

## 👤 我 · 2026-07-13 10:56

是不是必须先登陆微软账号

## 🤖 Claude · 2026-07-13 10:56

> [!example]- 🔧 工具调用
> 工具：`web_search`
>
> ```json
> {
>   "query": "Claude for Excel add-in Microsoft account required login 2026"
> }
> ```

> [!quote]- 📎 工具结果
> ```
> If your organization routes API traffic through an internal LLM gateway connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the add-in without a Claude account.
>
> May 27, 2026 · Table of contents · Claude for Excel is available to Pro, Max, Team, and Enterprise plans. Claude for Excel is an add-in that integrates Claude into your Excel workflow. It's designed for professionals who work extensively with spreadsheets, particularly in financial analysis and modeling. With Claude for Excel, you can: Ask questions about your workbook and get answers with cell-level citations · Update assumptions while preserving formula dependencies · Debug errors and identify their root causes · Build new models or fill existing templates · Navigate complex multi-tab workbooks seamlessly · Use connectors to bring context from your other tools directly into your spreadsheets · Excel on the web · Excel on Windows (Microsoft 365 subscription, build 16.0.13127.20296+) Excel on Mac (version 16.46+, build 21011600+) Excel on iPad (version 2.51+) Navigate to the Claude for Microsoft 365 (Excel, PowerPoint, and Word) listing on Microsoft Marketplace.
>
> Navigate to the Claude for Microsoft 365 (Excel, PowerPoint, and Word) listing on Microsoft Marketplace. Click "Get it now" to install the add-in. Open Excel, activate the add-in, and sign in with your Claude account. ... Visit the Microsoft 365 Admin Center. Navigate to Settings > Org Settings > User owned apps and services and ensure that “Let users access the Office Store" is toggled on. Navigate to Settings > Integrated apps > Add-ins. Search for "Claude by Anthropic for Excel" in Microsoft AppSource. Deploy the add-in to your organization or specific users. Share these instructions with your team: Microsoft's deployment guide. After installation, team members can open Excel, activate the Claude add-in (from Tools > Add-ins on Mac or Home > Add-ins on Windows), sign in with their Claude credentials, and start wo
> ```

简单说：**需要微软账号，但有两个层面**，别搞混了。

---

**1. 微软账号（用来"承载"插件）**

安装 Claude for Excel 需要一个绑定工作或学校账号的 Microsoft 365 订阅。个人 @outlook.com 账号和 Office 2016/2019 永久授权版不支持。

也就是说，你的 Excel 本身需要是 **Microsoft 365 订阅版**（公司账号登录的那种），这是微软对所有现代 Office Add-in 的通用要求，不是 Claude 特别加的限制。

**2. Claude 账号（用来"驱动"AI）**

安装并激活插件后，还需要用你的 Claude 账号登录。这才是真正让 AI 运行起来的认证。需要 Pro 及以上付费计划，免费账号装了也无法正常使用。

---

**特殊情况：可以不用 Claude 账号**

如果你的公司通过 AWS Bedrock、Google Cloud Vertex AI 或 LLM 网关来访问 Claude，可以不需要 Claude 账号，直接通过组织的基础设施连接。不过这属于企业级部署，需要 IT 配置。

---

**小结**

| 需要什么 | 说明 |
|---|---|
| Microsoft 365 订阅 + 工作/学校账号 | 必须，用于加载插件（微软侧） |
| Claude 付费账号（Pro+） | 必须，用于 AI 功能（Anthropic 侧） |
| Microsoft 365 Copilot 授权 | **不需要**，不用额外付这笔钱 |

你们公司如果是域账号管理的 Office，可能还需要 IT 管理员在 Microsoft 365 Admin Center 里开放 Office Store 权限，或者走 manifest 部署的方式。之前你提到过公司环境有权限限制，这里可能是个卡点。

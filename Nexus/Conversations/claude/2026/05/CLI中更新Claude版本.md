---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
aliases: CLI中更新Claude版本
conversation_id: d12d6613-e7a2-42b2-aa6d-5d8c25eb73af
create_time: 2026-05-29T02:09:11.000Z
update_time: 2026-05-29T02:09:27.000Z
---
# Title: CLI中更新Claude版本

Created: 2026/05/29 at 10:09:11
Last Updated: 2026/05/29 at 10:09:27
Chat URL: https://claude.ai/chat/d12d6613-e7a2-42b2-aa6d-5d8c25eb73af


>[!nexus_user] **User** - 2026/05/29 at 10:09:11
> 在CLI里怎么更新CLAUDE啊，我看出了4.8版本
<!-- UID: 019e717e-1d41-7a07-9fde-a81fcfb9b4e1 -->
>[!nexus_agent] **Assistant** - 2026/05/29 at 10:09:27
> 顺便说一下，目前我所知道的最新模型是 Claude Sonnet 4.6 / Opus 4.6，"4.8 版本"可能是你看到的某个非官方说法，建议以官方渠道为准。
>
> 关于更新 Claude Code CLI，有两种方式：
>
> **方式一：内置更新命令（最简单）**
> ```bash
> claude update
> ```
>
> **方式二：通过 npm 更新**
> ```bash
> npm update -g @anthropic-ai/claude-code
> ```
>
> 更新后可以验证版本：
> ```bash
> claude --version
> ```
>
> 如果你是用 Homebrew 安装的，也可以：
> ```bash
> brew upgrade claude-code
> ```
>
> 更新过程大约 10 秒，每隔几周 Anthropic 会发布新版本，带来新模型支持、新 CLI 命令、Bug 修复等。
>
> 如果遇到权限报错（`EACCES`），可以加 `sudo`，或者检查 npm 的全局目录权限。
>
> ### References
> 1. [https://www.getaiperks.com/en/ai/how-to-update-claude-code](https://www.getaiperks.com/en/ai/how-to-update-claude-code)
<!-- UID: 019e717e-1d41-7373-b4a2-5441b7c23528 -->

---
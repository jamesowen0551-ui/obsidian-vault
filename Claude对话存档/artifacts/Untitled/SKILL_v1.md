---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: SKILL
version_uuid: toolu_01HDbCcEjuS2MxCzxn4ghYnk
version_number: 1
command: create
conversation_id: 20e6cd86-8204-46ef-bb1b-c83fbf677019
create_time: 2026-06-03T14:46:58.000Z
format: markdown
aliases: [SKILL, SKILL_v1]
---

# SKILL (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|公司调研纪要生成]]

## Content

---
name: research-minutes
description: "Turn raw, messy research notes into a clean, structured Word (.docx) meeting minutes / 调研纪要. Use this whenever a user uploads or pastes notes from a company visit, expert interview, management call, due-diligence meeting, or any multi-person research session and asks to 'generate minutes', '做一份纪要', 'write up the notes', 'turn this into a Word doc', or similar. Especially trigger when the input is a transcript with speaker labels (说话人 1/2…), several people's overlapping notes that need merging, or a verbatim Q&A that needs organizing by topic. Produces a polished, topic-organized .docx — not a verbatim transcript."
---

# Research Minutes (调研纪要) Generator

Turn raw research notes — interview transcripts, multi-person field notes, management-call records — into a clean, professionally formatted Word meeting-minutes document, organized by theme rather than by chronology or speaker.

This skill assumes the **docx skill** at `/mnt/skills/public/docx/SKILL.md` is available. Read it first for the docx-js mechanics; this skill layers a specific document structure and a set of editorial rules on top.

## When this applies

The input is typically one of:
- A transcript with speaker labels (e.g. `说话人 1 00:00:02 …`)
- Several people's separate notes on the same meeting (e.g. "version1 / version2 / version3"), which overlap and must be merged
- A loose Q&A or bullet dump from a call or site visit

The output is always a **standalone .docx** the user will keep, circulate, or file — so create a real file, never just inline text.

## Core workflow

1. **Read the docx skill** (`/mnt/skills/public/docx/SKILL.md`) for document-creation mechanics. Confirm the `docx` npm package is available (`node -e "require('docx')"`); it is usually installed globally.
2. **Read the input fully** before writing anything. If it's an uploaded file, extract it (`extract-text file.docx`, or the right reader for the type). Identify: who/what was visited, when, and the recurring themes.
3. **Merge and de-duplicate.** When multiple note versions exist, combine them. The same fact often appears in two versions with slightly different numbers — keep both figures and flag the discrepancy rather than silently picking one. See "Editorial rules" below.
4. **Reorganize by theme, not by speaker or time.** Group everything under topical headings (see "Document structure"). A good minutes doc reads as a briefing, not a chat log.
5. **Build the .docx** using the structure and styling in `scripts/build_minutes.js` as a starting template. Adapt section headings to the actual content — don't force empty sections.
6. **Validate** with `python /mnt/skills/public/docx/scripts/office/validate.py <file>.docx`.
7. **Present** the file with `present_files` and give a short summary of what you did (merging, de-duplication, any flagged discrepancies).

## Document structure

Use this as the default skeleton, adapting headings to the material:

```
[Title]  e.g. 「<公司>（<场景>）调研纪要」
[Subtitle / one line]  e.g. 「实地调研 · 管理层交流」
[Info table]  调研对象 / 时间 / 地点 / 调研方 / 接待方 / 纪要说明
一、核心要点        ← 5–8 bullets, the "if you read nothing else" summary
二、<主题1>         ← e.g. 公司与基地概况
三、<主题2>         ← e.g. 产能、产值与产品结构  (use a table for structured data)
…                  ← as many themed sections as the content needs
[补充信息]          ← OPTIONAL:散点/与主营无关但有参考价值的信息
                       subsections like 劳动力与成本 / 宏观与产业环境 /
                       行业竞争 / 待跟踪的风险与判断
[Disclaimer note]  ← italic, small grey: 口径差异、以正式披露为准
```

Guidance:
- **核心要点 always comes first** and is the most important section — distill the investment/decision-relevant takeaways.
- Use **tables** for anything naturally tabular: capacity by plant, timeline by phase, financials by year, info header.
- A **补充信息 / supplementary section** is valuable for research notes — it captures the labor-cost asides, macro observations, competitor gossip, and risk flags that don't belong in the main narrative but are worth preserving. Add it whenever such material exists.

## Editorial rules

These are what make the output trustworthy rather than just tidy:

- **Faithful to source.** Don't invent facts, figures, or causal claims not in the notes. This is a record, not analysis.
- **Preserve conflicting figures.** Field notes routinely contain inconsistent numbers (e.g. monthly output stated as both 1.76亿 and 6.4亿). Keep both, attribute to "口径" differences, and add a closing disclaimer that figures are spoken/merged and the official disclosure prevails.
- **Mark uncertainty, don't paper over it.** If a name or number is unclear in the source (note-takers often write "zhongjin? jiantao?"), reproduce the best guess and annotate it as 待核实 / to-verify rather than presenting it as confirmed.
- **Verify proper nouns when it's cheap to do so.** Company names, product/standard names, and place names are often mis-transcribed from speech. When the document will be circulated or referenced, web-search to confirm the standard written form (e.g. 深南 → 深南电路, 建涛 → 建滔, 美维 → 安捷利美维). Standardize confirmed names; for names you cannot confirm, keep the original sound and annotate. Never force a "correction" you're not sure of.
- **Bold a short label, then explain.** For dense bullets, lead with a bolded label (`产能：`, `投入产出比：`) so the document scans quickly.
- **Neutral, factual register.** No hype, no recommendation, no editorializing beyond what the speakers said.

## Language and formatting notes

- Match the **language of the source** (Chinese notes → Chinese minutes).
- For Chinese documents, use a CJK-capable font (e.g. `Microsoft YaHei`) as the docx default.
- **Quotation marks gotcha (important for the build script):** full-width "" and stray ASCII `"` inside Chinese string literals will break the JS build. Use 「」 for any in-text Chinese quotes inside the script's string content. See the note at the top of `scripts/build_minutes.js`.
- Keep formatting clean: a colored title rule, simple heading hierarchy (H1 sections / H2 subsections), bordered tables with light shading, a running header and page-number footer.

## Reference template

`scripts/build_minutes.js` is a complete, working example that produced a real multi-section 调研纪要 (info table, 核心要点, ~10 themed sections, capacity table, 补充信息 section, disclaimer, header/footer). Use it as the styling and structure baseline — copy it, then replace the content arrays with the synthesized material from the current notes. It already encodes the page size, styles, bullet numbering, table helpers, and the quotation-mark convention.

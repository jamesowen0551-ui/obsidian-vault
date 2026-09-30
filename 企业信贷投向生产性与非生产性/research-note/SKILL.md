---
name: research-note
description: Generate Obsidian-style research reading notes for academic papers, books, and financial reports. Use when the user asks to (1) write detailed reading notes for a paper/book/report, (2) create a research topic folder with literature notes, (3) organize literature into a topic index/MOC, or (4) synthesize multiple papers into a comparative review. Output follows the "研究专题" format with YAML frontmatter, Obsidian callouts, wiki links, and structured sections. Supports single-paper deep notes, topic navigation indexes, and cross-paper synthesis reviews.
---

# Research Note — 研究专题笔记生成

Generate structured, Obsidian-compatible reading notes for academic and financial literature.

## Workflow

### Step 1: Determine Note Type

| User Request | Note Type | Output |
|-------------|-----------|--------|
| "给这篇论文写个笔记" | 单篇文献笔记 | `作者_年份_详细笔记.md` |
| "建一个研究专题" | 专题索引 (MOC) | `00 专题名称.md` + 子笔记 |
| "这几篇对比总结一下" | 综合短评 | `综合短评 标题.md` |
| "列个文献清单" | 文献清单 | `文献清单.md` |

### Step 2: Extract Content

- If PDF is provided: extract text using Python (`pypdf`) — first ~15 pages + references section
- If only citation/bibliography: search web for abstract, key findings, and quotes
- If multiple papers: read each in parallel, then synthesize

### Step 3: Generate Note

Follow the format specification in `references/format-spec.md`. Use the appropriate template from `references/`.

**Always include:**
1. YAML frontmatter with `title`, `authors`, `year`, `created`, `tags`
2. `[!abstract]` callout with one-sentence summary
3. `[!info]` callout with version/availability notes
4. Wiki link to source PDF (if available): `[[filename.pdf|原文 PDF]]`
5. Structured body with standard sections (see format-spec.md)
6. Related notes section with wiki links at the bottom

**Never output raw HTML or widget code** — output plain Markdown only.

### Step 4: Save Files

- Save to the user's active workspace (current working directory)
- Create `papers/` subdirectory for PDFs if they don't exist
- Name files with clear, sortable naming: `作者_年份_详细笔记.md`

## Output Formats

### Single-Paper Note

See `references/single-paper-template.md` for the full template.

Key sections:
- Research Question & Core Findings
- Theoretical Framework
- Key Concept Quick Reference (table)
- Implications for User's Research
- Theoretical Positioning
- Limitations & Open Questions
- Related Notes (wiki links)

### Topic Index (MOC)

See `references/topic-index-template.md`.

Organizes multiple papers into themes with:
- Core notes section
- Must-read literature section
- Extended reading section
- Related conversations archive
- Todo checklist
- Synthesis reviews

### Synthesis Review

See `references/review-template.md`.

Cross-paper analysis with:
- Question to answer (`[!question]` callout)
- One-sentence conclusion
- Fact-checking per paper
- Mechanism comparison (table)
- Unified framework
- Portfolio/practical implications
- Open questions

## Tags Convention

Use these standard tags for consistency:

| Tag | Meaning |
|-----|---------|
| `文献笔记` | Single-paper reading note |
| `MOC` | Topic index / navigation hub |
| `综合短评` | Cross-paper synthesis |
| `文献清单` | Bibliography list |
| Domain tags | e.g. `金融发展`, `信用分配`, `资产配置`, `因子投资` |

## Related Resources

- `references/format-spec.md` — Detailed format specification
- `references/single-paper-template.md` — Single-paper note template
- `references/topic-index-template.md` — Topic index/MOC template
- `references/review-template.md` — Synthesis review template

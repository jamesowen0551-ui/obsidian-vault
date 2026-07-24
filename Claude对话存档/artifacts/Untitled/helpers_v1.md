---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: helpers
version_uuid: toolu_01XtaVCxQRfsqKY5xG4yrenP
version_number: 1
command: create
conversation_id: f723ec16-18ed-41ad-9944-6dc342a23aaf
create_time: 2026-06-03T15:38:43.000Z
format: javascript
aliases: [helpers, helpers_v1]
---

# helpers (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|会议纪要整理]]

## Content

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, LevelFormat
} = require('docx');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

function infoRow(label, value) {
  return new TableRow({
    children: [
      new TableCell({
        borders,
        width: { size: 2200, type: WidthType.DXA },
        shading: { fill: "EAF2FB", type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 150, right: 150 },
        children: [new Paragraph({
          children: [new TextRun({ text: label, bold: true, font: "Arial", size: 22, color: "1F4E79" })]
        })]
      }),
      new TableCell({
        borders,
        width: { size: 7160, type: WidthType.DXA },
        margins: { top: 80, bottom: 80, left: 150, right: 150 },
        children: [new Paragraph({
          children: [new TextRun({ text: value, font: "Arial", size: 22 })]
        })]
      }),
    ]
  });
}

function sectionTitle(text) {
  return new Paragraph({
    spacing: { before: 280, after: 100 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } },
    children: [new TextRun({ text: text, bold: true, font: "Arial", size: 26, color: "1F4E79" })]
  });
}

function bulletItem(text, bold = false) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, font: "Arial", size: 22, bold })]
  });
}

function subBullet(text) {
  return new Paragraph({
    numbering: { reference: "subbullets", level: 0 },
    spacing: { before: 40, after: 40 },
    children: [new TextRun({ text, font: "Arial", size: 20, color: "444444" })]
  });
}

function gap() {
  return new Paragraph({ spacing: { before: 160, after: 0 }, children: [new TextRun("")] });
}

function buildDoc({ title, subtitle, infoRows, body }) {
  const children = [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 80 },
      children: [new TextRun({ text: title, bold: true, font: "Arial", size: 40, color: "1F4E79" })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 0, after: 360 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "2E75B6", space: 2 } },
      children: [new TextRun({ text: subtitle, font: "Arial", size: 24, color: "5B9BD5" })]
    }),
    new Table({
      width: { size: 9360, type: WidthType.DXA },
      columnWidths: [2200, 7160],
      rows: infoRows.map(r => infoRow(r[0], r[1]))
    }),
    new Paragraph({ spacing: { before: 400, after: 0 }, children: [new TextRun("")] }),
    ...body,
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 300, after: 0 },
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: "AAAAAA", space: 4 } },
      children: [new TextRun({
        text: "本纪要依据现场录音整理，仅供内部参考，不作为投资依据。",
        font: "Arial", size: 18, color: "888888", italics: true
      })]
    }),
  ];

  return new Document({
    numbering: {
      config: [
        { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u25CF",
          alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 300 } } } }] },
        { reference: "subbullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2013",
          alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1000, hanging: 280 } } } }] },
      ]
    },
    styles: { default: { document: { run: { font: "Arial", size: 22 } } } },
    sections: [{
      properties: {
        page: { size: { width: 11906, height: 16838 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } }
      },
      children
    }]
  });
}

function save(doc, path) {
  const fs = require('fs');
  return Packer.toBuffer(doc).then(buffer => fs.writeFileSync(path, buffer));
}

module.exports = { buildDoc, save, sectionTitle, bulletItem, subBullet, gap };

```
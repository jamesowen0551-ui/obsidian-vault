---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: build_minutes
version_uuid: toolu_01ANcuSAihi3c1PzTWfGNQXf
version_number: 1
command: create
conversation_id: 20e6cd86-8204-46ef-bb1b-c83fbf677019
create_time: 2026-06-03T14:46:58.000Z
format: javascript
aliases: [build_minutes, build_minutes_v1]
---

# build_minutes (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|公司调研纪要生成]]

## Content

```javascript
// ============================================================================
// build_minutes.js — reference template for a structured 调研纪要 / research
// meeting-minutes Word document.
//
// HOW TO USE:
//   1. Copy this file, then replace the CONTENT arrays (the c.push(...) block)
//      with the synthesized, theme-organized material from the current notes.
//   2. Keep the helpers, styles, page setup, and document assembly as-is.
//   3. Run:  node build_minutes.js
//   4. Validate:  python /mnt/skills/public/docx/scripts/office/validate.py <out>.docx
//
// QUOTATION-MARK GOTCHA (read this — it WILL bite you otherwise):
//   Full-width Chinese quotes “ ” and stray ASCII " inside a Chinese string
//   literal break the JavaScript parser. For any quote INSIDE Chinese body text,
//   use the bracket quotes 「 」 instead. The regular ASCII " is reserved for
//   delimiting JS strings only. (English content can use normal quotes fine.)
//
// CONVENTIONS baked in:
//   - lbl("标签：", "其余说明")  → bold label + normal text, for scannable bullets
//   - bullet(text, level)        → bulleted paragraph (level 0 or 1)
//   - infoRow / cell             → the top info table (label + value)
//   - dcell                      → data-table cell (blue header row)
// ============================================================================

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, VerticalAlign
} = require("docx");

const FONT = "Microsoft YaHei";   // CJK-capable default; change for non-CJK docs
const BLUE = "1F4E79";
const LTBLUE = "D5E8F0";
const GREY = "CCCCCC";
const OUT = "纪要.docx";           // output filename

// ---- helpers ----
function h1(t){return new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun(t)]});}
function h2(t){return new Paragraph({heading:HeadingLevel.HEADING_2,children:[new TextRun(t)]});}
function p(t,o={}){return new Paragraph({spacing:{after:120,line:276},children:[new TextRun({text:t,...o})]});}
function bullet(t,level=0){return new Paragraph({numbering:{reference:"bullets",level},spacing:{after:80,line:276},children:Array.isArray(t)?t:[new TextRun(t)]});}
function lbl(label,rest){return [new TextRun({text:label,bold:true}),new TextRun(rest)];}

function cell(text,{header=false,w}={}){
  const b={style:BorderStyle.SINGLE,size:1,color:GREY};
  return new TableCell({borders:{top:b,bottom:b,left:b,right:b},width:{size:w,type:WidthType.DXA},
    shading:header?{fill:LTBLUE,type:ShadingType.CLEAR}:undefined,
    margins:{top:60,bottom:60,left:120,right:120},verticalAlign:VerticalAlign.CENTER,
    children:[new Paragraph({children:[new TextRun({text,bold:header})]})]});
}
function infoRow(k,v){return new TableRow({children:[cell(k,{header:true,w:2200}),cell(v,{w:7160})]});}

function dcell(text,{header=false,w,bold=false}={}){
  const b={style:BorderStyle.SINGLE,size:1,color:GREY};
  return new TableCell({borders:{top:b,bottom:b,left:b,right:b},width:{size:w,type:WidthType.DXA},
    shading:header?{fill:BLUE,type:ShadingType.CLEAR}:undefined,
    margins:{top:60,bottom:60,left:120,right:120},verticalAlign:VerticalAlign.CENTER,
    children:[new Paragraph({children:[new TextRun({text,bold:header||bold,color:header?"FFFFFF":"000000"})]})]});
}

// ============================================================================
// CONTENT — replace everything in this block with the current notes' material.
// The sample below shows every structural element you can use.
// ============================================================================
const c=[];

// Title + subtitle rule
c.push(new Paragraph({spacing:{after:60},children:[new TextRun({text:"<公司>（<场景>）调研纪要",bold:true,size:36,color:BLUE})]}));
c.push(new Paragraph({border:{bottom:{style:BorderStyle.SINGLE,size:6,color:BLUE,space:1}},spacing:{after:200},children:[new TextRun({text:"实地调研 · 管理层交流",size:22,color:"666666"})]}));

// Info table
c.push(new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[2200,7160],rows:[
  infoRow("调研对象","<…>"),
  infoRow("调研时间","<…>"),
  infoRow("调研地点","<…>"),
  infoRow("调研方","<…>"),
  infoRow("接待方","<…>"),
  infoRow("纪要说明","本纪要由多位参会人员现场记录汇总整理，按主题归并，部分数据为现场口径，仅供内部参考。"),
]}));
c.push(p(""));

// 核心要点 — always first, the decision-relevant distillation
c.push(h1("一、核心要点"));
c.push(bullet("<最重要的结论1>"));
c.push(bullet("<最重要的结论2>"));
c.push(p(""));

// A themed section with bolded labels
c.push(h1("二、<主题>"));
c.push(bullet([...lbl("<标签>：","<说明>")]));
c.push(bullet("<普通要点>"));
c.push(p(""));

// A themed section with a data table (capacity / timeline / financials …)
c.push(h1("三、<带表格的主题>"));
c.push(h2("<子标题>"));
c.push(new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[1500,3360,4500],rows:[
  new TableRow({children:[dcell("列1",{header:true,w:1500}),dcell("列2",{header:true,w:3360}),dcell("列3",{header:true,w:4500})]}),
  new TableRow({children:[dcell("<…>",{w:1500,bold:true}),dcell("<…>",{w:3360}),dcell("<…>",{w:4500})]}),
]}));
c.push(p(""));

// Optional 补充信息 section —散点 / 与主营无关但有参考价值的信息
c.push(h1("<N>、补充信息"));
c.push(new Paragraph({spacing:{after:120,line:276},children:[new TextRun({text:"以下为现场交流中提及的散点信息，部分与主营无直接关系，但有参考价值。",italics:true,color:"666666"})]}));
c.push(h2("劳动力与成本"));
c.push(bullet("<…>"));
c.push(h2("宏观与产业环境"));
c.push(bullet("<…>"));
c.push(h2("行业竞争与同行"));
c.push(bullet("<…>"));
c.push(h2("待跟踪的风险与判断"));
c.push(bullet("<…>"));
c.push(p(""));

// Disclaimer note
c.push(new Paragraph({spacing:{before:240},border:{top:{style:BorderStyle.SINGLE,size:4,color:GREY,space:4}},
  children:[new TextRun({text:"说明：本纪要为现场交流记录整理，部分数字为口头表述与不同记录的汇总，可能存在口径差异，请以正式披露为准。",italics:true,size:18,color:"888888"})]}));

// ============================================================================
// DOCUMENT ASSEMBLY — keep as-is.
// ============================================================================
const HEADER_TITLE = "<公司>调研纪要";  // running header text

const doc=new Document({
  styles:{
    default:{document:{run:{font:FONT,size:22}}},
    paragraphStyles:[
      {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,
        run:{size:28,bold:true,font:FONT,color:BLUE},
        paragraph:{spacing:{before:280,after:140},outlineLevel:0}},
      {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,
        run:{size:24,bold:true,font:FONT,color:"2E5496"},
        paragraph:{spacing:{before:160,after:100},outlineLevel:1}},
    ],
  },
  numbering:{config:[{reference:"bullets",levels:[
    {level:0,format:LevelFormat.BULLET,text:"•",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:480,hanging:240}}}},
    {level:1,format:LevelFormat.BULLET,text:"–",alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:960,hanging:240}}}},
  ]}]},
  sections:[{
    properties:{page:{size:{width:12240,height:15840},margin:{top:1440,right:1440,bottom:1440,left:1440}}},
    headers:{default:new Header({children:[new Paragraph({alignment:AlignmentType.RIGHT,
      border:{bottom:{style:BorderStyle.SINGLE,size:4,color:GREY,space:2}},
      children:[new TextRun({text:HEADER_TITLE,size:16,color:"999999"})]})]})},
    footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,
      children:[new TextRun({text:"第 ",size:16,color:"999999"}),
        new TextRun({children:[PageNumber.CURRENT],size:16,color:"999999"}),
        new TextRun({text:" 页",size:16,color:"999999"})]})]})},
    children:c,
  }],
});

Packer.toBuffer(doc).then(buf=>{fs.writeFileSync(OUT,buf);console.log("written "+OUT);});

```
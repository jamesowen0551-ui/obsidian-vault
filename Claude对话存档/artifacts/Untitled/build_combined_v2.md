---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: build_combined
version_uuid: toolu_01Sys7AQWCA9PvGjxTtyh7Wf
version_number: 2
command: update
conversation_id: f723ec16-18ed-41ad-9944-6dc342a23aaf
create_time: 2026-06-03T16:40:47.000Z
format: javascript
aliases: [build_combined, build_combined_v2]
---

# build_combined (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|会议纪要整理]]

## Content

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, LevelFormat,
  Bookmark, InternalHyperlink, PageBreak, TabStopType, TabStopPosition,
  PageNumber, Header, Footer
} = require('docx');
const fs = require('fs');

const companies = [
  ...require('./data_hudian'),
  ...require('./data_others'),
];

const SUBTITLE_COLOR = "005096";   // RGB(0,80,150) — section titles
const ACCENT = "2E75B6";

const cellBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };

// ---- block renderers ----
function infoRow(label, value) {
  return new TableRow({ children: [
    new TableCell({ borders: cellBorders, width:{size:2200,type:WidthType.DXA},
      shading:{fill:"EAF2FB",type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:150,right:150},
      children:[new Paragraph({children:[new TextRun({text:label,bold:true,font:"Arial",size:22,color:"1F4E79"})]})]}),
    new TableCell({ borders: cellBorders, width:{size:7160,type:WidthType.DXA},
      margins:{top:80,bottom:80,left:150,right:150},
      children:[new Paragraph({children:[new TextRun({text:value,font:"Arial",size:22})]})]}),
  ]});
}

function sectionTitle(text) {
  return new Paragraph({
    spacing:{before:280,after:100},
    border:{bottom:{style:BorderStyle.SINGLE,size:6,color:ACCENT,space:1}},
    children:[new TextRun({text,bold:true,font:"Arial",size:26,color:SUBTITLE_COLOR})]
  });
}
function subTitle(text) {
  return new Paragraph({
    spacing:{before:160,after:60},
    children:[new TextRun({text,bold:true,font:"Arial",size:23,color:SUBTITLE_COLOR})]
  });
}
function bullet(text){
  return new Paragraph({numbering:{reference:"bullets",level:0},spacing:{before:60,after:60},
    children:[new TextRun({text,font:"Arial",size:22})]});
}
function sub(text){
  return new Paragraph({numbering:{reference:"subbullets",level:0},spacing:{before:40,after:40},
    children:[new TextRun({text,font:"Arial",size:20,color:"444444"})]});
}
function plain(text){
  return new Paragraph({spacing:{before:60,after:60},children:[new TextRun({text,font:"Arial",size:22})]});
}
function note(text){
  return new Paragraph({spacing:{before:60,after:100},
    children:[new TextRun({text,font:"Arial",size:20,italics:true,color:"777777"})]});
}
function dataTable(head, rows){
  const nCols = head.length;
  const totalW = 9360;
  const colW = nCols===3 ? [1600,3200,4560] : Array(nCols).fill(Math.floor(totalW/nCols));
  // adjust last col to sum exactly
  const sum = colW.reduce((a,b)=>a+b,0);
  colW[colW.length-1] += (totalW - sum);
  const headRow = new TableRow({tableHeader:true,children: head.map((h,i)=>
    new TableCell({borders:cellBorders,width:{size:colW[i],type:WidthType.DXA},
      shading:{fill:"D5E8F0",type:ShadingType.CLEAR},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({children:[new TextRun({text:h,bold:true,font:"Arial",size:21,color:"1F4E79"})]})]})
  )});
  const bodyRows = rows.map(r=> new TableRow({children: r.map((c,i)=>
    new TableCell({borders:cellBorders,width:{size:colW[i],type:WidthType.DXA},
      margins:{top:80,bottom:80,left:120,right:120},
      children:[new Paragraph({children:[new TextRun({text:c,font:"Arial",size:20})]})]})
  )}));
  return new Table({width:{size:totalW,type:WidthType.DXA},columnWidths:colW,rows:[headRow,...bodyRows]});
}

function renderBlock(b){
  switch(b.t){
    case 'h': return sectionTitle(b.x);
    case 'h2': return subTitle(b.x);
    case 'b': return bullet(b.x);
    case 's': return sub(b.x);
    case 'p': return plain(b.x);
    case 'note': return note(b.x);
    case 'table': return dataTable(b.head, b.rows);
    default: return plain(b.x||"");
  }
}

// ---- document title page ----
const docChildren = [];

docChildren.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:1200,after:120},
  children:[new TextRun({text:"泰国出海企业实地调研纪要汇编",bold:true,font:"Arial",size:52,color:"1F4E79"})]}));
docChildren.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:80},
  children:[new TextRun({text:"七家公司 · 2026年6月3日",font:"Arial",size:28,color:SUBTITLE_COLOR})]}));
docChildren.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:200},
  border:{bottom:{style:BorderStyle.SINGLE,size:8,color:ACCENT,space:2}},
  children:[new TextRun({text:"沪电股份 · 鹏鼎科技 · 广合科技 · 福田汽车 · 福斯特 · 家联科技 · 建龙微纳",font:"Arial",size:20,color:"5B9BD5"})]}));

// ---- Table of Contents (hyperlinked) ----
docChildren.push(new Paragraph({pageBreakBefore:true,spacing:{before:0,after:200},
  children:[new TextRun({text:"目录",bold:true,font:"Arial",size:36,color:"1F4E79"})]}));

companies.forEach((c,idx)=>{
  docChildren.push(new Paragraph({
    spacing:{before:80,after:80},
    tabStops:[{type:TabStopType.RIGHT,position:9360,leader:"dot"}],
    children:[ new InternalHyperlink({
      anchor: c.id,
      children:[ new TextRun({text:`${idx+1}.  ${c.name}`,font:"Arial",size:24,color:SUBTITLE_COLOR}),
                 new TextRun({text:`\t@@PAGEREF:${c.id}@@`,font:"Arial",size:22,color:"333333"}) ]
    }) ]
  }));
});

// ---- each company section ----
companies.forEach((c,idx)=>{
  // page break before each company
  docChildren.push(new Paragraph({pageBreakBefore:true,alignment:AlignmentType.CENTER,
    spacing:{before:200,after:80},
    children:[ new Bookmark({id:c.id, children:[
      new TextRun({text:`${idx+1}. ${c.name}调研纪要`,bold:true,font:"Arial",size:40,color:"1F4E79"})
    ]}) ]}));
  docChildren.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:0,after:360},
    border:{bottom:{style:BorderStyle.SINGLE,size:8,color:ACCENT,space:2}},
    children:[new TextRun({text:c.subtitle,font:"Arial",size:24,color:"5B9BD5"})]}));

  // info table — only 调研时间 + 调研地点
  docChildren.push(new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[2200,7160],
    rows:[ infoRow("调研时间", c.time), infoRow("调研地点", c.place) ]}));
  docChildren.push(new Paragraph({spacing:{before:300,after:0},children:[new TextRun("")]}));

  c.body.forEach(b=> docChildren.push(renderBlock(b)));

  docChildren.push(new Paragraph({alignment:AlignmentType.CENTER,spacing:{before:300,after:0},
    border:{top:{style:BorderStyle.SINGLE,size:4,color:"AAAAAA",space:4}},
    children:[new TextRun({text:"本纪要依据现场记录整理，仅供内部参考，不作为投资依据。",
      font:"Arial",size:18,italics:true,color:"888888"})]}));
});

const doc = new Document({
  numbering:{config:[
    {reference:"bullets",levels:[{level:0,format:LevelFormat.BULLET,text:"\u25CF",alignment:AlignmentType.LEFT,
      style:{paragraph:{indent:{left:600,hanging:300}}}}]},
    {reference:"subbullets",levels:[{level:0,format:LevelFormat.BULLET,text:"\u2013",alignment:AlignmentType.LEFT,
      style:{paragraph:{indent:{left:1000,hanging:280}}}}]},
  ]},
  styles:{default:{document:{run:{font:"Arial",size:22}}}},
  sections:[{
    properties:{page:{size:{width:11906,height:16838},margin:{top:1440,right:1440,bottom:1440,left:1440}}},
    footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,
      children:[new TextRun({text:"第 ",font:"Arial",size:18,color:"999999"}),
                new TextRun({children:[PageNumber.CURRENT],font:"Arial",size:18,color:"999999"}),
                new TextRun({text:" 页",font:"Arial",size:18,color:"999999"})]})]})},
    children: docChildren
  }]
});

Packer.toBuffer(doc).then(buffer=>{
  fs.writeFileSync('/mnt/user-data/outputs/泰国出海企业调研纪要汇编.docx', buffer);
  console.log('combined done');
});

```
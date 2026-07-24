---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: minutes
version_uuid: toolu_01Xzm43oKriKhQKSJTVWnvdh
version_number: 1
command: create
conversation_id: f723ec16-18ed-41ad-9944-6dc342a23aaf
create_time: 2026-06-03T15:30:14.000Z
format: javascript
aliases: [minutes, minutes_v1]
---

# minutes (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|会议纪要整理]]

## Content

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
  VerticalAlign, LevelFormat, PageNumber, NumberFormat
} = require('docx');
const fs = require('fs');

const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorders = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
};
const headerBorder = { style: BorderStyle.SINGLE, size: 1, color: "2E75B6" };
const headerBorders = { top: headerBorder, bottom: headerBorder, left: headerBorder, right: headerBorder };

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

function para(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, font: "Arial", size: 22, ...opts })]
  });
}

const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "●",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 600, hanging: 300 } } }
        }]
      },
      {
        reference: "subbullets",
        levels: [{
          level: 0, format: LevelFormat.BULLET, text: "–",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1000, hanging: 280 } } }
        }]
      },
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 34, bold: true, font: "Arial", color: "1F4E79" },
        paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "2E75B6" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 }
      },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      // Title block
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 80 },
        children: [new TextRun({ text: "鹏鼎科技（泰国）调研纪要", bold: true, font: "Arial", size: 40, color: "1F4E79" })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 360 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "2E75B6", space: 2 } },
        children: [new TextRun({ text: "实地参观交流会议", font: "Arial", size: 24, color: "5B9BD5" })]
      }),

      // Basic info table
      new Table({
        width: { size: 9360, type: WidthType.DXA },
        columnWidths: [2200, 7160],
        rows: [
          infoRow("会议时间", "2026年6月3日"),
          infoRow("会议地点", "泰国巴真府 鹏鼎科技泰国园区（PA11行政楼）"),
          infoRow("会议主题", "鹏鼎科技泰国厂实地参观及经营情况介绍"),
          infoRow("参会方", "鹏鼎科技管理层（说话人1-3）、机构投资者调研团队"),
          infoRow("主要介绍人", "沈总（说话人3，公司管理层）、美玉（说话人1）、说话人2（现场负责人）"),
          infoRow("记录整理", "会议录音整理"),
        ]
      }),

      new Paragraph({ spacing: { before: 400, after: 0 }, children: [new TextRun("")] }),

      // Section 1: Company Overview
      sectionTitle("一、公司基本情况"),
      bulletItem("公司名称：鹏鼎科技（泰国）有限公司（丰城科技），属珍鼎集团旗下"),
      bulletItem("注册时间：2023年9月；2023年12月举行动土典礼；2025年5月正式投产"),
      bulletItem("注册地址：泰国巴真府甲宾区（距曼谷机场约2小时，距林查班港约2.5小时）"),
      bulletItem("注册资本：80亿泰铢"),
      bulletItem("现有员工：约2,000人，中泰缅各约三分之一"),
      subBullet("中国籍（含华人派驻干部）：约600人，担任管理及技术岗位"),
      subBullet("泰国籍：约700-800人，比例略高于三分之一"),
      subBullet("缅甸籍：约600人，主要从事基层生产作业"),
      bulletItem("战略合作伙伴：沙哈集团（SAHA Group）——泰国零售业龙头，政商关系良好，工厂所在园区即为沙哈集团旗下工业园"),
      bulletItem("主营业务定位：全方位电路板（One-Stop Shopping），重点聚焦AI Server、光模块及光通讯，兼顾手机及智能穿戴"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 2: Factory Progress
      sectionTitle("二、厂房建设进展"),
      bulletItem("已投产：PA01（现满产运行），建筑面积约15,000㎡（100m×150m，两层），单层3万㎡"),
      bulletItem("在建厂房："),
      subBullet("PA02：外墙完工，机电已进场装修，预计今年年底完工并试产（面积为PA01两倍，100m×300m）"),
      subBullet("PA06、PA03：预计明年年初完工并试产，机电已进场"),
      subBullet("PA08：算力控制中心，承载AI Server钻孔机台及背钻设备需求"),
      subBullet("PA05、PA07：规划中，具体方向待定"),
      bulletItem("配套设施：PA12餐厅预计明年1月完工，2月启用；变电站自建，直接接入电厂输电线路"),
      bulletItem("员工宿舍：首期20栋（含单人间/双人间/三人间），预计今年7月起陆续交付入住"),
      bulletItem("全部建成后员工规模可达8,000至12,000人"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 3: Products & Capacity
      sectionTitle("三、产品结构与产能规划"),
      bulletItem("PA01现阶段主力产品：AI Server PCB（含HDI，22至26层）及光模块PCB，各占约一半"),
      bulletItem("PA02：延续PA01客户群，主要围绕AI Server及光模块扩大产能"),
      bulletItem("PA06：聚焦高密度厚板（UBB、Base Station类产品，Highly Count）"),
      bulletItem("PA03：承接软板及SMA部分产能迁移，时程预计明年Q2"),
      bulletItem("产能策略：不放弃消费电子/端侧产品（苹果等），以AI Server为增量，保留苹果等存量基本盘"),
      subBullet("管理层判断2-3年后端侧应用将爆发（手机、可穿戴、PC AI），届时既有端侧积累将形成差异化竞争力"),
      subBullet("强调"云-管-端"全覆盖的战略定位，不调换赛道，做增量"),
      bulletItem("当前产能状况：PA01已满产；27年产能全部锁定；28年产能谈判中"),
      bulletItem("特殊制程与产品的稀缺性：公司在背板等前沿产品上与头部客户保持联合开发，已在台北电脑展相关发布中露出"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 4: Customers
      sectionTitle("四、客户结构与订单情况"),
      bulletItem("主要客户：微软、谷歌等全球CSP大厂（AI Server方向），苹果（消费电子），其他光模块客户"),
      bulletItem("客户驱动扩产：每家来访客户参观PA01后均反馈"产能太小"，主动要求在后续厂房包场，此为二至八厂加速动工的直接原因"),
      bulletItem("涨价趋势：AI产能紧缺带动整体PCB价格上行，包括非AI品类；泰国产能溢价目前相对中国超过15%-20%，近期因抢产能溢价水平更高"),
      bulletItem("产能迁出需求：部分客户（如微软）已明确要求在2027-2028年前将特定产能全部移至中国境外，公司泰国产能将优先满足此类需求"),
      bulletItem("国内产能：主要服务非美系客户及部分美系客户在国内需要供应的机种，按机种与市场分配灵活切换"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 5: Cost & Operations
      sectionTitle("五、成本与运营情况"),
      bulletItem("综合成本：相比国内高约15%-20%，主要因素为："),
      subBullet("人工效率：约为国内的0.6-0.7，但薪资水平较低，两者部分对冲"),
      subBullet("物料与供应链：当地供应链配套不完善，大量物料仍从中国采购，物流耗时较长；泰国港口效率低于国内"),
      subBullet("物流波动：中东冲突等地缘因素阶段性推高物流成本"),
      bulletItem("电力供应：泰国电网基础设施相对薄弱（电压不稳定、历史上有因风灾倒杆停电记录），公司已自建变电站并直接接入当地发电厂线路以保障稳定供电，未来规划屋顶光伏"),
      subBullet("泰国以天然气发电为主，本土供应（泰国湾），据供电局表示暂无缺电风险，油价上涨或导致电价上调"),
      bulletItem("盈利情况：PA01单厂已盈亏平衡；整体园区仍处投资期（宿舍、交通车等大额投入）；管理层对近1-2年内实现整体盈利持较高信心，认为AI产品价格景气度超预期"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 6: HR & Localization
      sectionTitle("六、人才与本地化"),
      bulletItem("培训体系：赴国内（淮安、秦皇岛）培训泰籍员工，目前已完成第二期；要求受训员工具备中文及英语能力"),
      bulletItem("产学合作：已与泰国6所大专院校签署MOU，定向培养当地工程师级人才"),
      bulletItem("长期目标：扩张阶段后将以泰籍、缅籍员工为主要劳动力来源，逐步降低中国派驻人员比例"),
      bulletItem("智能化方向：工厂设计以自动化为主，控制单位产能用工人数"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 7: Competition & Location
      sectionTitle("七、选址逻辑与竞争格局"),
      bulletItem("泰国优势：PCB产业链集聚较早（板厂与材料商协同），政商环境相对稳定，沙哈集团等本地伙伴政商关系强"),
      bulletItem("越南：消费电子组装优势显著（广达、仁宝、三星），PCB上下游支撑不及泰国，基建相对弱"),
      bulletItem("马来西亚：半导体（封测）强，PCB人才与产业基础有差异，与PCB需求契合度不及泰国"),
      bulletItem("友商动态：深南电路等同业企业亦布局泰国；市场上部分竞争对手（如某重庆工厂）出现经营困难"),
      bulletItem("公司内部竞争壁垒：特殊制程与产品的稀缺性，与头部CSP深度联合开发，客户黏性强"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 8: Global Expansion
      sectionTitle("八、整体扩产布局"),
      bulletItem("泰国园区：现4栋在建，合计约6栋厂房"),
      bulletItem("淮安：6栋厂房"),
      bulletItem("深圳：新获地块，已公告，7月开工，2栋厂房"),
      bulletItem("国内外产能未设比例限制，按客户需求动态分配；AI Server为未来增量核心方向"),

      new Paragraph({ spacing: { before: 200, after: 0 }, children: [new TextRun("")] }),

      // Section 9: Q&A Key Points
      sectionTitle("九、问答要点摘录"),
      bulletItem("Q：苹果订单的涨价趋势如何？"),
      subBullet("A：AI产能挤占带动全线产品价格上行，公司将持续保留苹果等消费电子基本盘，同时在AI方向做增量。"),
      bulletItem("Q：客户对泰国产能的溢价接受度？"),
      subBullet("A：早期15-20%溢价已被普遍接受；近期因产能紧俏，溢价水平进一步提升，部分客户为锁定产能主动提高报价。"),
      bulletItem("Q：海外产能迁移要求是否逐年提高？"),
      subBullet("A：是，部分客户（如微软）已设定明确时间表，要求在27/28年前完成产能切换，公司将泰国产能优先供给此类客户。"),
      bulletItem("Q：泰国与国内产能的长期分工？"),
      subBullet("A：泰国产能优先满足"非中国出货"要求的海外客户；国内产能优先服务非美系及按机种需要在国内生产的机种。"),
      bulletItem("Q：微软HDI主板规格？"),
      subBullet("A：22至26层均有，属高密度互连产品。"),
      bulletItem("Q：PA01目前产品结构？"),
      subBullet("A：AI Server PCB与光模块PCB各约一半，公司是泰国首条M-SAP产线。"),

      new Paragraph({ spacing: { before: 300, after: 0 }, children: [new TextRun("")] }),

      // Footer note
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 200, after: 0 },
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: "AAAAAA", space: 4 } },
        children: [new TextRun({
          text: "本纪要依据现场录音整理，仅供内部参考，不作为投资依据。",
          font: "Arial", size: 18, color: "888888", italics: true
        })]
      }),
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/鹏鼎科技调研纪要.docx', buffer);
  console.log('Done');
});

```
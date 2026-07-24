---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: build
version_uuid: toolu_01RiSdAaJK2YPgnzdydbfZ9e
version_number: 4
command: update
conversation_id: 9a452b45-cd55-4354-8fcc-df1c391ffc2e
create_time: 2026-05-31T13:32:56.000Z
format: javascript
aliases: [build, build_v4]
---

# build (Version 4)

**Conversation:** [[内容分析请求|钢琴榔头硬化和磨损的不可逆性]]

## Content

```javascript
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  ExternalHyperlink, BorderStyle, LevelFormat
} = require("docx");

// ---- helpers ----
const FONT = "Microsoft YaHei"; // good CJK font; falls back gracefully

function body(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 140, line: 300 },
    children: [new TextRun({ text, font: FONT, size: 22, ...opts })],
  });
}

function runs(children, opts = {}) {
  return new Paragraph({ spacing: { after: 140, line: 300 }, children, ...opts });
}

function t(text, opts = {}) {
  return new TextRun({ text, font: FONT, size: 22, ...opts });
}

function link(label, url) {
  return new ExternalHyperlink({
    link: url,
    children: [new TextRun({ text: label, font: FONT, size: 22, style: "Hyperlink", color: "1155CC", underline: {} })],
  });
}

function bullet(children) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 100, line: 300 },
    children,
  });
}

function numbered(children, ref = "numbers") {
  return new Paragraph({
    numbering: { reference: ref, level: 0 },
    spacing: { after: 120, line: 300 },
    children,
  });
}

function quoteBox(children) {
  return new Paragraph({
    spacing: { after: 140, line: 300 },
    indent: { left: 480 },
    border: { left: { style: BorderStyle.SINGLE, size: 18, color: "8AAEDC", space: 12 } },
    shading: { type: "clear", fill: "F2F6FC" },
    children,
  });
}

const children = [];

// Title
children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { after: 80 },
  children: [t("钢琴锤头硬化剂与扎针不可逆性证据汇编", { bold: true, size: 36 })],
}));
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [t("整理自海外钢琴技师论坛、专业整音教材及技师网站", { size: 20, color: "666666" })],
}));
children.push(new Paragraph({
  spacing: { after: 240 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "2E75B6", space: 6 } },
  children: [t("整理日期：2026年5月｜全部来源均附原始链接，可点击核查", { size: 20, color: "666666" })],
}));

// ===== 摘要 =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 120, after: 120 }, children: [t("一、核心结论摘要", { bold: true, size: 28 })] }));

children.push(body("综合海外多个独立来源（专业整音教材、PTG/Pianotech 技师讨论、钢琴维修网站），可归纳出两点主流共识："));

children.push(numbered([t("扎针（needling）造成的损伤被高度一致地认定为不可逆。", { bold: true }), t("核心机制是：扎针本质上是切断锤毡纤维，断裂的纤维会永久丧失张力、无法重新连接，过度扎针会让锤毡变“死”、无可挽救，最终往往只能更换整套锤子。")]));
children.push(numbered([t("硬化剂（lacquer / hardener）处理被视为可逆性最差的整音手段之一。", { bold: true }), t("传统硝基硬化漆会“持续硬化”，渗入多年后极难去除；真实案例显示，试图去除硬化剂的救治过程本身就可能让锤子直接散架，最终只能换锤。需客观说明：少数经验丰富的技师声称用强溶剂长时间浸泡或油剂可部分软化过硬锤子，因此严格说硬化剂在特定条件下可被“部分”逆转，但需要专业设备、强溶剂与大量时间，且效果因锤而异、无法保证恢复原状。")]));
children.push(numbered([t("特别针对汉堡施坦威（见第五部分）：", { bold: true }), t("施坦威官方对汉堡工厂整音的描述只涉及扎针、不涉及硬化剂；汉堡使用的 Renner 高压缩 Weickert 毡锤本不需硬化剂，且最依赖内部张力/回弹能力。在汉堡施坦威上滥用硬化剂或过度扎针，既偏离官方工艺方向，又会造成不可逆损坏。")]));

// ===== 第二部分：扎针不可逆 =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 }, children: [t("二、关于“扎针不可逆”的证据", { bold: true, size: 28 })] }));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 1：专业整音教材明文“扎针错误通常不可逆”", { bold: true, size: 24 })] }));
children.push(body("《Fundamentals of Piano Practice》（钢琴练习基础，被广泛引用的在线教材）整音章节直接写道：扎针错误通常是不可逆的（Needling mistakes are generally irreversible）。教材还强调，钢琴音色对击弦点附近的浅层扎针极其敏感，操作者必须非常清楚自己在做什么。"));
children.push(runs([t("来源："), link("Fundamentals of Piano Practice — Ch. 2.7 Voicing", "https://fundamentals-of-piano-practice.readthedocs.io/chapter2/CH2.7.html")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 2：纤维断裂导致张力永久丧失（物理机制）", { bold: true, size: 24 })] }));
children.push(body("Piano World 论坛技师 Olek 从纤维力学角度指出：扎针必须在液体处理之后进行；但如果纤维被弄得过于滑润，张力的丧失就会发生，且无法再恢复回来。"));
children.push(runs([t("来源："), link("Piano World — Hammer softening solution（讨论串）", "https://forum.pianoworld.com/ubbthreads.php/ubb/printthread/Board/3/main/143732/type/thread.html")]));
children.push(body("New York Piano Works（专业整音/修复工作室）解释了相同机制：由于断裂的纤维失去了张力，锤子表面久而久之会被一层没有弹性、没有回弹力的“死毡”（dead layer of felt）包裹，音色因此劣化。"));
children.push(runs([t("来源："), link("New York Piano Works — Hammer Head Filing", "https://newyorkpianoworks.com/blog/repair-spotlight-hammer-head-filing")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 3：连主张少用化学品的技师也承认扎针破坏纤维连续性", { bold: true, size: 24 })] }));
children.push(body("资深技师 Joseph Garrett 在 Pianotech 讨论中表示，他把扎针当作整音的最后手段，因为在他看来扎针会破坏纤维的连续性（It destroys fiber continuity）。这从侧面印证扎针的破坏属于结构性、不可恢复的损伤。"));
children.push(runs([t("来源："), link("Pianotech — Hammer Lacquer Removal（讨论串）", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 4：多个来源警告“过度扎针会毁掉锤子，只能更换”", { bold: true, size: 24 })] }));
children.push(bullet([t("Ronsen 钢琴锤公司（Weickert 特制锤整音说明）：对滥用硬化剂/扎针发出强烈警告，直言“它会毁掉锤子（It will ruin the hammers）”。来源："), link("Ronsen / Erwins Piano — Voicing the Ronsen Weickert special hammers (PDF)", "http://www.erwinspiano.com/wp-content/uploads/2015/04/Hammers-VoicingR.Weickert.pdf")]));
children.push(bullet([t("整音教程（Blue Book of Pianos）：明确写“过度扎针会毁掉锤子，尤其是在太靠近击弦点处扎针时”。来源："), link("Blue Book of Pianos — Action Regulation and Voicing", "http://www.bluebookofpianos.com/voicing.htm")]));
children.push(bullet([t("rec.music.makers.piano 论坛技师：整音是需大量训练的高难技能，外行用 lacquer 会对锤子造成非常严重的损害，而换整套锤子既费钱又费工；并点名某些现代锤（如 Yamaha）很容易被重度扎针毁掉。来源："), link("rec.music.makers.piano — Advice on brightening up hammers", "https://groups.google.com/g/rec.music.makers.piano/c/fGg1pSgTihM")]));

// ===== 第三部分：硬化剂不可逆 =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 }, children: [t("三、关于“硬化剂极难逆转 / 常需换锤”的证据", { bold: true, size: 28 })] }));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 5：硝基硬化漆会“持续硬化”，渗入后“比花岗岩还硬”", { bold: true, size: 24 })] }));
children.push(body("技师 Joe（Joseph Garrett）指出 sanding sealer 一类硬化漆“会永远持续硬化下去（will continue to harden forever）”。在去除硬化剂的实操讨论中他进一步说明：若硬化漆已在锤子里待了 5～10 年以上，那东西会比花岗岩还硬，普通稀释剂、丙酮基本无效，必须动用毒性很强的 MEK（丁酮）。"));
children.push(runs([t("来源："), link("Pianotech — Quick hammer hardening methods?", "https://groups.google.com/g/pianotech/c/opZq7F6rID4")]));
children.push(runs([t("来源（去除实操）："), link("Pianotech — Hammer Lacquer Removal", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 6：去除极其费力，且无法确认是否真的去除干净", { bold: true, size: 24 })] }));
children.push(body("在同一讨论串中，技师为冲掉硬化漆，每隔一小时浇一次 MEK、连续 24 小时，用掉约半加仑。另一位技师则指出：染色痕迹还在并不代表硬化漆还在，唯一能确认硬化漆是否真去掉的方法，是把钢琴装回去实际弹奏——也就是说，处理后技师自己也无法保证恢复程度。"));
children.push(runs([t("来源："), link("Pianotech — Hammer Lacquer Removal", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 7（最有力）：救治过程本身可能直接毁掉锤子，最终只能换锤", { bold: true, size: 24 })] }));
children.push(body("同一讨论串中有一个极具说服力的真实案例：技师 Regi 用相同的 MEK 浸泡法处理两架钢琴——1985 年 Baldwin SD10 救回来了，但 1988 年 Baldwin R 的锤子在处理后散架（“没能像 SD10 那样挺过这个处理过程”）。技师 Joe 推测厂家当年可能用厚硬化漆代替胶水粘合锤毡，所以一泡就散，并直接给出选项之一：干脆装一套像样的新锤、就这么收工（just put a decent set of hammers on and call it good）。"));
children.push(quoteBox([t("要点：很多被过度硬化的锤子，现实中的最终解决方案就是更换整套锤子。试图“救回”反而可能造成不可逆的物理破坏。", { italics: true })]));
children.push(runs([t("来源："), link("Pianotech — Hammer Lacquer Removal（含前后对比照片）", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 100, after: 100 }, children: [t("证据 8：技师改用 B72 的理由，反证传统 lacquer 的不可控硬化", { bold: true, size: 24 })] }));
children.push(body("技师 Regi 选择 Paraloid B-72 而非传统 lacquer，理由是 B72 据说不像 lacquer 那样会持续硬化，整音效果更稳定。这从反面印证了传统硝基硬化漆“会不断继续硬化”的不可控特性——也正是它被视为“不可逆”的核心原因之一。"));
children.push(runs([t("参考："), link("Medium — Paraloid B-72 in Voicing Pianos", "https://medium.com/@eathankeyboards/paraloid-b-72-in-voicing-pianos-how-and-where-to-apply-it-how-and-where-to-get-it-and-what-b8a4b321578")]));

// ===== 第四部分：客观说明（反方证据） =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 }, children: [t("四、为保持客观：关于“硬化剂可部分逆转”的不同看法", { bold: true, size: 28 })] }));
children.push(body("证据并非完全一边倒。需要如实记录以下不同观点，以免引用时显得片面："));
children.push(bullet([t("有化学背景的论坛参与者认为，硝基硬化剂只是浸入羊毛纤维使其变硬（类似发胶让头发变硬），并非发生不可逆的化学反应，理论上可用溶剂部分“洗”出。来源："), link("Piano World — Hammer Voicing w/Acetone", "https://forums.pianoworld.com/ubbthreads.php/ubb/printthread/Board/3/main/116621/type/thread.html")]));
children.push(bullet([t("技师 Douglas Gregg 声称用丙酮长时间浸泡（约一周、换 3 次丙酮）或 Ballistol 油剂，能成功软化过硬锤子；但他同时承认“当然也有限度（of course there are limits）”，并非能完全还原到处理前状态。来源："), link("Pianotech — Hammer Lacquer Removal", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q")]));
children.push(body("小结：即便支持“可逆”的技师，也都强调需要专业设备、强溶剂/油剂、大量时间，且效果因锤而异、无法保证完全恢复。对普通琴主而言，这类处理实务上接近“不可逆”，且自行尝试风险极高。"));

// ===== 第五部分：针对汉堡施坦威的专门证据 =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 }, children: [t("五、针对汉堡施坦威钢琴的专门证据", { bold: true, size: 28 })] }));
children.push(body("汉堡施坦威（Hamburg Steinway）与纽约施坦威的整音工艺存在根本区别，这一区别对“是否应在汉堡施坦威上使用硬化剂”至关重要。以下证据含原始英文原文与来源链接。"));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 9：施坦威官方（汉堡工厂）——整音只用扎针“增加弹性”，未提硬化剂", { bold: true, size: 24 })] }));
children.push(body("施坦威欧洲官网（汉堡工厂）整音专页描述：整音师用整音针逐一刺入锤头毡以增加其弹性，且必须由受专门训练、拥有出色听力与多年经验的施坦威技师完成。该描述完全未提及硬化剂（lacquer）。"));
children.push(quoteBox([t("原文：They individually poke the hammer head felt with the voicing needle to increase its elasticity. … voicing is carried out by Steinway technicians who are specially trained, have great hearing and years of experience.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Steinway & Sons (EU) — Hear a pin drop: the Voicing", "https://eu.steinway.com/en/a-legend/manufactory/voicing/")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 10：施坦威官方报道——硬化剂用于提亮，扎针用于软化", { bold: true, size: 24 })] }));
children.push(body("施坦威官方报道《Instrumental Royalty》说明：毡锤靠施加类似硬化漆的溶液变硬（用于需要提亮的音），或靠针刺打开毡来变软；并指出汉堡工厂的锤子是向分包商采购的（即 Renner，见证据 12）。"));
children.push(quoteBox([t("原文：the felt-covered hammers are made either harder (by putting lacquer-like solution on the felt — if the note has to be brightened a bit) or softer (using a needle to open up the felt). … in Hamburg, they are purchased from subcontractors.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Steinway & Sons — Instrumental Royalty", "https://www.steinway.com/news/features/instrumental-royalty")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 11：专业修复商 Chupp’s——汉堡靠扎针“往下调”，硬化剂是纽约工艺", { bold: true, size: 24 })] }));
children.push(body("Chupp’s Piano（专业施坦威修复商）对比两厂工艺：纽约软压锤靠多次施加硬化漆“往上提”；汉堡由 Renner 提供的硬压锤则靠针尖整音工具多次刺击“往下调”。"));
children.push(quoteBox([t("原文：New York Steinway hammerheads … are soft pressed. Multiple dosages of hardening solution such as lacquer are used … to bring the hammers ‘up’ … Hamburg Steinway hammerheads are provided by Renner, are of a hard-pressed variety and are then brought ‘down’ by the use of multiple strikes of the needle tipped voicing tool.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Chupp’s Pianos — Steinway New York vs. Hamburg", "https://www.chuppspianos.com/new-york-steinway-vs-hamburg-steinway-a-tail-of-two-factories/")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 12：汉堡用 Renner 高压缩 Weickert 毡锤，靠扎针软化引出音色", { bold: true, size: 24 })] }));
children.push(body("David Andersen Pianos 指出：汉堡用 Renner 高压缩 Weickert 毡锤，靠扎针“打开”并软化来引出音色；纽约用低压缩锤，靠硬化溶液处理。Renner USA 官方亦确认其 Weickert（Blue Point）毡锤专为 1970 年后汉堡施坦威三角钢琴设计，且不需要硬化剂即可产生音色。"));
children.push(quoteBox([t("原文（David Andersen）：Hamburg uses the Renner high-compression Weikert felt hammers … The high compression hammers are “opened up” and softened with needles to bring their tone out.", { italics: true, size: 20 })]));
children.push(quoteBox([t("原文（Renner USA）：They … do not require the use of lacquer or chemical hardeners to produce tone. … Designed for use in newer Hamburg Steinway & Sons grand pianos produced since 1970.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("David Andersen Pianos — Hamburg vs. New York Steinway", "https://davidandersenpianos.com/hamburg-steinway-vs-new-york-steinway-the-real-differences/")]));
children.push(runs([t("来源："), link("Renner USA — Renner Piano Hammerheads", "https://rennerusa.com/renner-piano-hammerheads/")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 13：高压缩锤过度扎针/硬化会永久丧失回弹能力（针对汉堡锤型）", { bold: true, size: 24 })] }));
children.push(body("整音专家 David Love 在 Pianotech 讨论中说明：更少的处理能保留锤子内部张力、维持较高的“恢复系数”（被压缩后回弹到原始形状的能力）；重度扎针与硬化剂都会降低这种恢复能力，最终锤子彻底失去回到原始形态的能力。这正针对汉堡施坦威所用的 Renner/Weickert 高压缩毡锤。"));
children.push(quoteBox([t("原文：Less manipulation (lacquer or needles) preserves the internal tension of the hammer and maintains a higher coefficient of restitution … Heavy needling and lacquer reduce the restorative capacity of the hammer. … the hammer loses all capacity to return to its original form after compression.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Pianotech — Renner vs. Ronsen hammer comparison", "https://groups.google.com/g/pianotech/c/-ESBKcKClbc")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 14：Piano Buyer——汉堡传统靠扎针软化（历史与工艺背景）", { bold: true, size: 24 })] }));
children.push(body("权威选购媒体 Piano Buyer 说明：二战后欧洲毡料更致密，汉堡锤是用针扎软化到理想音色的；并指出硬化剂常被视为 20 世纪美国的做法。"));
children.push(quoteBox([t("原文：in Hamburg … the felt available to European piano makers was more dense … and the hammers were voiced with needles to soften them to the desired tone. The addition of a chemical hardener such as lacquer is often thought of as a 20th-century American idea.", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Piano Buyer — New York and Hamburg Steinways Harmonize", "https://www.pianobuyer.com/post/new-york-and-hamburg-steinways-harmonize")]));

children.push(new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 120, after: 100 }, children: [t("证据 15：施坦威官方——整音须由授权技师按工厂技法进行；损坏后标准做法是更换锤子", { bold: true, size: 24 })] }));
children.push(body("施坦威官方保养说明：整音应由施坦威授权技师按工厂指定技法完成；并给出锤子更换的周期参考——即锤子损坏到无法整音时，官方标准处理是更换，而非反复抢救。"));
children.push(quoteBox([t("原文：a Steinway-authorized technician will voice the hammerheads … through a variety of factory-specified techniques. … Hammer replacement: every 18–20 years (home use) / 4–7 years (heavy use).", { italics: true, size: 20 })]));
children.push(runs([t("来源："), link("Steinway & Sons — Service & Maintenance", "https://www.steinway.com/news/features/utilty/service-and-maintenance")]));

children.push(quoteBox([t("小结（汉堡施坦威）：施坦威官方对汉堡工厂整音的描述只涉及扎针、不涉及硬化剂；汉堡使用的 Renner 高压缩 Weickert 毡锤本不需硬化剂，且最依赖内部张力/回弹能力。因此在汉堡施坦威上滥用硬化剂或过度扎针，既偏离官方工艺方向，又会造成不可逆损坏，最终往往只能更换整套锤子。", { bold: true, italics: true })]));

// ===== 来源清单 =====
children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 200, after: 120 }, children: [t("六、全部来源清单", { bold: true, size: 28 })] }));
const sources = [
  ["Fundamentals of Piano Practice — Voicing（教材，明文“扎针错误通常不可逆”）", "https://fundamentals-of-piano-practice.readthedocs.io/chapter2/CH2.7.html"],
  ["Pianotech — Hammer Lacquer Removal（去除硬化剂实操，含散架案例与对比照片）", "https://groups.google.com/g/pianotech/c/BK5leS3vc3Q"],
  ["Pianotech — Quick hammer hardening methods?（“会永远持续硬化”）", "https://groups.google.com/g/pianotech/c/opZq7F6rID4"],
  ["Piano World — Hammer softening solution（纤维滑润后张力无法恢复）", "https://forum.pianoworld.com/ubbthreads.php/ubb/printthread/Board/3/main/143732/type/thread.html"],
  ["Piano World — Hammer Voicing w/Acetone（化学家视角：理论上可洗出）", "https://forums.pianoworld.com/ubbthreads.php/ubb/printthread/Board/3/main/116621/type/thread.html"],
  ["New York Piano Works — Hammer Head Filing（“死毡”机制）", "https://newyorkpianoworks.com/blog/repair-spotlight-hammer-head-filing"],
  ["Blue Book of Pianos — Action Regulation and Voicing（过度扎针毁锤）", "http://www.bluebookofpianos.com/voicing.htm"],
  ["rec.music.makers.piano — Advice on brightening up hammers（重度扎针毁锤、需换锤）", "https://groups.google.com/g/rec.music.makers.piano/c/fGg1pSgTihM"],
  ["Ronsen / Erwins Piano — Voicing the Weickert special hammers PDF（“会毁掉锤子”）", "http://www.erwinspiano.com/wp-content/uploads/2015/04/Hammers-VoicingR.Weickert.pdf"],
  ["Medium — Paraloid B-72 in Voicing Pianos（B72 更稳定、不持续硬化）", "https://medium.com/@eathankeyboards/paraloid-b-72-in-voicing-pianos-how-and-where-to-apply-it-how-and-where-to-get-it-and-what-b8a4b321578"],
  ["Moore Piano — Why Hammer Replacement is Necessary（磨损至只能换锤）", "https://www.moorepiano.com/posts/why-hammer-replacement-on-pianos-is-necessary"],
  ["Steinway & Sons (EU) — Hear a pin drop: the Voicing（汉堡官方：整音只用扎针增加弹性）", "https://eu.steinway.com/en/a-legend/manufactory/voicing/"],
  ["Steinway & Sons — Instrumental Royalty（官方：硬化剂提亮 / 扎针软化；汉堡锤外购）", "https://www.steinway.com/news/features/instrumental-royalty"],
  ["Steinway & Sons — Service & Maintenance（官方：授权技师按工厂技法；换锤周期）", "https://www.steinway.com/news/features/utilty/service-and-maintenance"],
  ["Chupp’s Pianos — Steinway New York vs. Hamburg（汉堡靠扎针往下调）", "https://www.chuppspianos.com/new-york-steinway-vs-hamburg-steinway-a-tail-of-two-factories/"],
  ["David Andersen Pianos — Hamburg vs. New York Steinway（高压缩 Weickert 锤靠扎针软化）", "https://davidandersenpianos.com/hamburg-steinway-vs-new-york-steinway-the-real-differences/"],
  ["Renner USA — Renner Piano Hammerheads（Weickert 锤不需硬化剂；专为 1970 后汉堡施坦威设计）", "https://rennerusa.com/renner-piano-hammerheads/"],
  ["Pianotech — Renner vs. Ronsen hammer comparison（过度处理永久丧失回弹能力）", "https://groups.google.com/g/pianotech/c/-ESBKcKClbc"],
  ["Piano Buyer — New York and Hamburg Steinways Harmonize（汉堡传统靠扎针软化）", "https://www.pianobuyer.com/post/new-york-and-hamburg-steinways-harmonize"],
];
sources.forEach((s) => children.push(numbered([link(s[0], s[1])], "srcnums")));

children.push(new Paragraph({
  spacing: { before: 240 },
  border: { top: { style: BorderStyle.SINGLE, size: 6, color: "CCCCCC", space: 6 } },
  children: [t("说明：以上为论坛技师经验、专业教材与厂家说明，可作为参考与交涉依据。如需用于正式维权，建议同时咨询当地有资质的钢琴技师（如 PTG 注册技师 RPT）出具书面意见。", { size: 18, color: "888888" })],
}));

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: FONT, color: "1A1A1A" },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: FONT, color: "2E5496" },
        paragraph: { spacing: { before: 180, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: FONT, color: "333333" },
        paragraph: { spacing: { before: 120, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 300 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
      { reference: "srcnums", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children,
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("/home/claude/钢琴锤头不可逆性证据汇编.docx", buffer);
  console.log("done");
});

```
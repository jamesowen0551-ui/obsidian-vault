---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: build
version_uuid: toolu_01YYA23Y1qioGp5inJQs8TUt
version_number: 5
command: update
conversation_id: 20e6cd86-8204-46ef-bb1b-c83fbf677019
create_time: 2026-06-03T14:31:39.000Z
format: javascript
aliases: [build, build_v5]
---

# build (Version 5)

**Conversation:** [[Nexus/Conversations/claude/2026/06/Untitled|公司调研纪要生成]]

## Content

```javascript
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, WidthType, ShadingType, PageNumber, VerticalAlign
} = require("docx");

const FONT = "Microsoft YaHei";
const BLUE = "1F4E79";
const LTBLUE = "D5E8F0";
const GREY = "CCCCCC";

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

const c=[];

c.push(new Paragraph({spacing:{after:60},children:[new TextRun({text:"沪电股份（泰国基地）调研纪要",bold:true,size:36,color:BLUE})]}));
c.push(new Paragraph({border:{bottom:{style:BorderStyle.SINGLE,size:6,color:BLUE,space:1}},spacing:{after:200},children:[new TextRun({text:"实地调研 · 管理层交流",size:22,color:"666666"})]}));

c.push(new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[2200,7160],rows:[
  infoRow("调研对象","沪电股份（泰国生产基地）"),
  infoRow("调研时间","2026年6月3日"),
  infoRow("调研地点","泰国 · 大城府 洛迦娜（Rojana）工业园区"),
  infoRow("调研方","易方达基金等"),
  infoRow("公司接待","管理层（管经理等）"),
  infoRow("纪要说明","本纪要由多位参会人员现场记录汇总整理，按主题归并，部分数据为现场口径，仅供内部参考。"),
]}));
c.push(p(""));

c.push(h1("一、核心要点"));
c.push(bullet("良率领先是核心壁垒：26层板良率达93%–95%，而部分更早投产的同行16层板良率不足60%；高端PCB并非有设备、有资金、能挖人就能做出来。"));
c.push(bullet("泰国基地产能与盈利兑现快于预期：一厂上月（2026年5月）单月产值约1.76亿元，预计今年达约18亿元、明年约30亿元；一厂+三厂达产后整体营收有望约80亿元。"));
c.push(bullet("订单饱满：一厂2027年订单已排满，三厂成为后续主要增量。"));
c.push(bullet("客户与产品结构优秀：以高端AI服务器、交换机（1.6T/800G/400G）为主，谷歌、英伟达等大客户已认可，约90%客户已通过认证。"));
c.push(bullet("强议价能力：高端材料紧缺叠加客户OOC需求，成本上涨可顺利向下游传导，泰国厂下单价格显著高于昆山，毛利率不输国内且仍在爬坡。"));
c.push(bullet("出海主因是政治/供应链风险：部分客户明确要求中国大陆以外产能（含5月新出现的美方高端芯片相关限制），愿为泰国产能支付溢价。"));
c.push(p(""));

c.push(h1("二、公司与泰国基地概况"));
c.push(bullet([...lbl("股权与定位：","100%外资企业，无泰国本地股东（富士电子持股约99%、昆山新兴电子集团约5%口径），主营多层印刷电路板（PCB）。")]));
c.push(bullet([...lbl("注册与投资：","注册资本约64.9亿泰铢；BOI备案约20亿元人民币，因调整产品结构，实际投入已达约30亿元人民币（含两个厂）。")]));
c.push(bullet([...lbl("BOI管理：","泰国按项目限定经营范围（如申请「生产多层线路板」即仅能做此类），比中国营业执照管理更细；须按申请的全流程生产，不同流程对应不同优惠政策。")]));
c.push(bullet([...lbl("土地与厂房：","位于大城府洛迦娜工业园区，土地约126莱（约22万平方米 / 约320亩），规划建设四栋生产厂房；预计2028年地块基本建满，园区内已无多余扩张空间。")]));
c.push(bullet([...lbl("人员：","员工约2200余人，中国员工约480人（占比20%多），其余约1600人为当地招聘；中国员工占比未来将下降。")]));
c.push(p(""));

c.push(h2("选址逻辑（为何选泰国 / 洛迦娜）"));
c.push(bullet("泰国老工业区、历史上的旧都，当地工人具备工厂作业的纪律与基础经验。"));
c.push(bullet("水源充足，PCB用水量大；园区废水处理能力较强、配套完备。"));
c.push(bullet("供电相对稳定：其他园区跳电次数为此处的2–3倍；本园区2025年跳电约4–5次，2026年5月31日跳过一次。"));
c.push(bullet("物流便利：距空运机场约1小时、海运约2小时；但因中资企业聚集，机场较小、易爆仓。"));
c.push(bullet("综合考量后由越南转向泰国；沪电进入较早，目前园区周边已聚集60多家PCB企业。"));
c.push(p(""));

c.push(h1("三、产能、产值与产品结构"));
c.push(h2("产能规划与节奏"));
c.push(new Table({width:{size:9360,type:WidthType.DXA},columnWidths:[1500,3360,4500],rows:[
  new TableRow({children:[dcell("厂区",{header:true,w:1500}),dcell("定位",{header:true,w:3360}),dcell("进度 / 备注",{header:true,w:4500})]}),
  new TableRow({children:[dcell("一厂",{w:1500,bold:true}),dcell("通信为主，AI服务器等高端产品",{w:3360}),dcell("一期满产、2025Q1开始量产；二期爬坡、2025Q2满产",{w:4500})]}),
  new TableRow({children:[dcell("二厂",{w:1500,bold:true}),dcell("调整为多阶HBM为主，车载为搭配",{w:3360}),dcell("车载不再是主方向，随市场调整",{w:4500})]}),
  new TableRow({children:[dcell("三厂",{w:1500,bold:true}),dcell("1.6T交换机等下一代（N+1）产品",{w:3360}),dcell("规划2026Q3动工–2028Q1；比一厂多建一层；平均层数规划超50层",{w:4500})]}),
  new TableRow({children:[dcell("五厂",{w:1500,bold:true}),dcell("车载相关（搭配二厂）",{w:3360}),dcell("规划中，约2028年地块建满",{w:4500})]}),
]}));
c.push(p(""));

c.push(h2("产值与订单"));
c.push(bullet("一厂：去年约3亿元；上月单月产值约1.76亿元；二厂上月约1000万元。"));
c.push(bullet("一厂全年预期约18亿元，2027年预期约30亿元产值。"));
c.push(bullet("一厂2027年订单已排满，增量转向三厂；一厂+三厂达产后整体营收预期约80亿元。"));
c.push(bullet("目前2027年产能已被客户大量预订。"));
c.push(p(""));

c.push(h2("产品层数与单价"));
c.push(bullet("规划响应极快：从2022年至今规划已迭代至第四个版本；最初平均规划14–16层，目前实际投产平均已超22层，四季度接单接近24层。"));
c.push(bullet("平均22层产品单价约3000多元人民币。"));
c.push(bullet("良率领先：26层板良率约93%–95%（另有六层板93%–95%口径）；部分同行16层板良率不足60%。"));
c.push(bullet("1.6T/800G/400G高端AI交换机为主；通用AI服务器暂无产能承接；1.6T光模块（如M-SUB）相关仍在昆山、常州生产。"));
c.push(p(""));

c.push(h1("四、成本与投入产出"));
c.push(bullet("泰国生产成本较国内高约20%以上：水、电较贵，人工不便宜（泰国最低工资标准高于中国西部、与中部相当），且效率较中国差。"));
c.push(bullet("基础工业品较国内贵约10%–20%；工业回收能力差，废料不能卖钱，环保相关费用未必比国内更省。"));
c.push(bullet("自动化程度略高于国内。"));
c.push(bullet([...lbl("投入产出比：","行业一般约1:1.5；公司达产后可能达1:2。一厂约23亿元投入，明年可做到30多亿元——取决于产品结构，中低端产品多为约1:1.2，部分1:1。")]));
c.push(p(""));

c.push(h1("五、用工与管理"));
c.push(h2("用工情况"));
c.push(bullet("当地最低工资标准约人民币2100–2200元；员工加班不积极，实际到手收入不算高，但离职率不高。"));
c.push(bullet("招工吃力：泰国约7000万人口、老龄化较重，年龄中位数约42岁、少子化，2025年人口净减少约11万。"));
c.push(bullet("依赖外劳：缅甸、老挝、柬埔寨合法外劳全国约400多万，黑户外劳可能上千万（多集中于建筑业与服务业）。"));
c.push(bullet("招工方式：网络发布 + 面试 + 员工内推（满3个月给奖金）+ 中介合作。"));
c.push(bullet("中国员工整体持工作签或临时工作签合规用工；短期接待客户等用商务签（仅限办公室/会议室，不得进车间），合规性较好，较少被查。"));
c.push(p(""));

c.push(h2("技术传承与管理模式"));
c.push(bullet("前期用约两年时间将作业标准翻译成泰文，配合中泰文对照、手把手「传帮带」，快速拉升良率；同行多沿用国内「配翻译」模式，专业术语易出错。"));
c.push(bullet("2025年4月以前要求中国人尽量不直接动手（避免依赖短期应急），如今量产板已基本由泰国员工作业、中国人主要做过程监督与高难度研发板。"));
c.push(bullet([...lbl("组织高效：","执行长/事业部对采购、组织架构等有较大管辖权，内部按「内部客户—内部供应商」协同，减少行政与生产之间的内耗扯皮；此为富士（被业内称为行业「黄埔军校」）长期积累的制度优势，单纯挖一两个人难以复制。")]));
c.push(p(""));

c.push(h1("六、税收、政策与政府关系"));
c.push(h2("优惠政策"));
c.push(bullet("满足设备投资约15亿（泰铢口径）、两年内达10亿泰铢等条件，享8年所得税减免 + 其后5年减半（基础所得税20%→10%），合计约13年。"));
c.push(bullet("环评不需要：废水按园区指标处理后排入园区统一处理，整体环保要求较中国宽松，按国内标准规划基本可达标。"));
c.push(bullet("人才引进等配套政策。"));
c.push(p(""));

c.push(h2("实际税负"));
c.push(bullet("当前最大税负为增值税：原材料进口、产品出口，出口退税，实际税率约7%（标准税率10%）。"));
c.push(bullet("设备进口关税基本全免；材料可凭中泰 / 东盟产地证减免关税。"));
c.push(bullet("由于全流程在泰国生产，HTS/HS code已发生改变，不适用增值比例（如40%）类原产地约束。"));
c.push(bullet("派驻员工先按泰国缴税，回中国汇算清缴，最终基本按中国税率补税（最高35%）；本地员工抵扣项多、个税不高，享免费医疗等福利（需排队）。"));
c.push(p(""));

c.push(h2("政府关系与潜在变化"));
c.push(bullet("中资企业合规性方面不太受欢迎、民众偶有怨言，但外资整体受欢迎；地方关系交织、较复杂；中泰关系较好。"));
c.push(bullet("与印度不同，泰国在投资上较规范，不会「养肥了再杀」，政府几乎未干扰过企业经营；灰色地带主要在签证。"));
c.push(bullet("全球最低税率：若泰国最终确定执行（所得税不低于15%），公司将按15%缴纳，届时既有税收优惠或相应调整；目前尚未最终确定。当前主要问题是退税较慢（政府人手不足、工厂多）。"));
c.push(bullet([...lbl("园区盈利模式：","工业区相当于物业公司，卖地、卖水卖电、收管理费，并带动地方就业；招商基本由园区负责。")]));
c.push(p(""));

c.push(h1("七、能源与基础设施"));
c.push(bullet("电力供应较充裕，用电量不是问题；电网稳定性弱于中国（老旧、输电能力有限，偶因施工或动物导致跳电）。2025年三季度起明显好转。"));
c.push(bullet("以天然气发电为主；约20%电力为中国经老挝输入（泰国全国口径），部分成品油也由中国炼化供应。整体优于越南（越南限电较严重）。"));
c.push(bullet("美伊/能源冲突影响有限：电费未涨，曾短期（约两三周）限制员工加油，现已恢复正常，油价较前期高点已大幅回落。"));
c.push(bullet("基础设施滞后于产能建设：机场太小；中泰铁路规划已久（曾称2027/2028通车），目前进度缓慢，受政治周期影响（换总理即换思路）。"));
c.push(bullet("日资历史奠定工业化基础（如本田工厂），设备配套能力仍在；近年中资大量进入、日资陆续撤退。"));
c.push(p(""));

c.push(h1("八、物流与供应链"));
c.push(bullet("以卡车运输为主：比空运便宜、比海运快、相对安全；当前流向为原料(中国)→泰国生产→成品回中国。"));
c.push(bullet("国内开票/回流比例下降：1–2月以运回中国为主（约40%–50%），目前投料中国占比已降至约20%以下；预计2026年6月前后国内开票约40%口径，今年Q4回流可能基本消失。"));
c.push(bullet("客户多元化：除中国外，逐步拓展泰国本地、越南、台湾、墨西哥等。"));
c.push(bullet("供应链本地化逐步完善：原料目前几乎全部来自国内；台光在马来西亚已有工厂并开始供货，台耀、联茂在泰国设厂（尚未正式量产），斗山上月宣布在泰建厂，未来有望就地解决。"));
c.push(bullet("结算以美元为主，资金（含外汇风险管理）由集团统一管理。"));
c.push(p(""));

c.push(h1("九、行业格局与竞争"));
c.push(bullet("泰国预计2027–2028年成为全球第二大PCB生产基地；园区周边已聚集60多家PCB企业（站在办公室即可看到4–5家）。"));
c.push(bullet([...lbl("园区内同行：","深南电路、威尔泰（现场口述「威尔高/威尔涛」，名称待核实）、奥士康、中京电子、建滔、安捷利美维（被国企收购）等；其中深南电路与沪电没问题，威尔泰较多做二手相关。")]));
c.push(bullet([...lbl("分化严重：","约5月新来认可的资深同行反映，不少厂有设备、有资金、挖了人仍做不出高端产品；某激进同行虽2024Q3末投产更早，16层板良率不足60%。")]));
c.push(bullet([...lbl("跟风产能虚高：","很多工厂建好却无订单或不真正做高端产品（装设备充门面、甚至把泰国设备搬回国内应急、裁员）；真正能做高端的「五个手指数得过来」。")]));
c.push(bullet([...lbl("行业判断：","中低端产能已过剩、未来几年较差；高端在2030年以前仍偏紧、格局可维持；预计约2030年（亦有2035年口径）行业将出现较多倒闭出清。")]));
c.push(bullet("国产化设备占比高：除压机、钻孔机（及电测部分）外，多数设备为国产；按投资口径约80%以上、按数量口径可能约90%。激光钻孔仍在用；国产钻孔机正在国内与二厂（车载等较简单产品）试用。"));
c.push(p(""));

c.push(h1("十、客户、定价与议价能力"));
c.push(bullet("大客户进展快：谷歌、英伟达等已开始做；2025年4月底约60%–70%客户认可，5月新增3–4家，目前约90%客户已认可。"));
c.push(bullet("谷歌量大：今年约400多万张、去年100多万张，明年有望1000万张、后年或2000万张以上；公司刻意维持客户多样性，不将产能押注单一客户（项目越多管理越复杂，但风险更低）。"));
c.push(bullet([...lbl("强议价能力：","高端材料紧缺 + 客户OOC需求，提价幅度可观——曾因无产能随便报价、加价约70%客户仍接受；不同项目溢价二三十个百分点到70%不等。")]));
c.push(bullet("成本可顺利传导：铜价等上涨基本可转嫁客户，对利润影响不大；高端材料多由客户统一分配定价。"));
c.push(bullet("欧美客户重视长期合作与供应稳定性，价格非首要权重；公司与核心客户多有近30年合作关系。"));
c.push(bullet("毛利率：泰国厂不输国内且仍在爬坡，钻孔机产能到位、产能平衡后毛利率有望进一步提升（对比：胜宏科技个案净利率最高约40%+）。"));
c.push(p(""));

c.push(h2("出海核心动因：政治与供应链风险"));
c.push(bullet("部分客户明确要求中国大陆以外产能（含自研芯片、特定交换机只给特定地区生产），愿为此支付溢价。"));
c.push(bullet("5月出现的美方限制：某些高端芯片只要涉及中资即不卖（此前仅限大陆工厂），已体现在客户商务网站与正式法务/商务邮件通知中；思科部分政府相关产品要求2027年全部转出中国。"));
c.push(bullet("当前主要是中资企业在泰国扩产，其他地区扩产有限。"));
c.push(p(""));

c.push(h1("十一、补充信息"));
c.push(new Paragraph({spacing:{after:120,line:276},children:[new TextRun({text:"以下为现场交流中提及的散点信息，部分与公司主营业务无直接关系，但对理解泰国劳动力、宏观环境与行业竞争格局有参考价值。",italics:true,color:"666666"})]}));

c.push(h2("劳动力与人力成本"));
c.push(bullet("新招工人年龄偏大，新进员工年龄常达40多岁。"));
c.push(bullet("离职率不高，相较中国是一项稳定性优势。"));
c.push(bullet("黑户外劳规模庞大，可能上千万，主要集中在建筑业与服务业。"));
c.push(bullet([...lbl("中国派驻员工薪酬结构：","国内原薪资保持不变，来泰国为额外补贴叠加，即「来这边的收入是多出来的」；按当前趋势，未来泰国岗位待遇甚至可能反超国内。")]));
c.push(bullet([...lbl("本地员工福利：","社保由约750泰铢提升至800–850泰铢口径，可享免费医疗（接待人员亲历小手术，仅自付单间房费，其余全免），但就医需排队。")]));
c.push(p(""));

c.push(h2("宏观与产业环境"));
c.push(bullet("日资撤退具体案例：大城府本田工厂已关闭，反映日企竞争力下降；中资进入与日资退出同步发生。"));
c.push(bullet("泰国工业化起步早：约60–70年代即开始工业化、国际化，早于多数东南亚国家。"));
c.push(bullet("越南对比：越南限电较为严重，泰国电力供应明显更优，对出海选址有参考意义。"));
c.push(bullet("中泰铁路受政治周期影响：换一任总理换一种思路，导致工程时停时开，进度缓慢。"));
c.push(bullet("电力跨境供应：泰国全国约20%电力来自中国（经老挝输入）；中国曾一度限制出口，导致约两三周供应短缺。"));
c.push(p(""));

c.push(h2("行业竞争与同行情况"));
c.push(bullet([...lbl("富士的人才地位：","被业内称为行业「黄埔军校」，人才外流较多，但同行单纯挖一两个人难以复制其体系能力。")]));
c.push(bullet("同行实操困境：某厂高价招聘泰国大学生做OP效果不佳，后又转回寻找中国员工。"));
c.push(bullet("产能虚化案例：有厂将泰国设备搬回国内并裁员（约从1200人裁至五六百人）。"));
c.push(bullet("创易：计划约68亿元产值，目前泰国厂月产值约6000万元。"));
c.push(bullet("Apex（台资背景，原主做白电与车载）：入驻泰国后做三星手机板，做了一年多仍未做好。"));
c.push(p(""));

c.push(h2("待跟踪的风险与判断"));
c.push(bullet([...lbl("全球最低税率：","若泰国最终执行所得税不低于15%，公司将按15%缴纳，既有税收优惠或被相应调整——值得持续跟踪的潜在风险点。")]));
c.push(bullet([...lbl("AI产业链涨价传导：","涨价沿上游化工—电子—机械链条传导，本质由景气驱动；公司凭高端能力与OOC需求，传导较为顺畅。")]));
c.push(p(""));

c.push(new Paragraph({spacing:{before:240},border:{top:{style:BorderStyle.SINGLE,size:4,color:GREY,space:4}},
  children:[new TextRun({text:"说明：本纪要为现场交流记录整理，部分数字为口头表述与不同记录的汇总，可能存在口径差异（如产值、占比、税率等），请以公司正式披露为准。",italics:true,size:18,color:"888888"})]}));

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
      children:[new TextRun({text:"沪电股份（泰国基地）调研纪要",size:16,color:"999999"})]})]})},
    footers:{default:new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,
      children:[new TextRun({text:"第 ",size:16,color:"999999"}),
        new TextRun({children:[PageNumber.CURRENT],size:16,color:"999999"}),
        new TextRun({text:" 页",size:16,color:"999999"})]})]})},
    children:c,
  }],
});

Packer.toBuffer(doc).then(buf=>{fs.writeFileSync("/home/claude/沪电股份调研纪要.docx",buf);console.log("written");});

```
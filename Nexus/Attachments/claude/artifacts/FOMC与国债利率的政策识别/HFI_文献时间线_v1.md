---
nexus: nexus-ai-chat-importer
plugin_version: "1.6.8"
provider: claude
artifact_id: HFI_文献时间线
version_uuid: toolu_01PzqRMvCVpTZVVCksqsrUGo
version_number: 1
command: create
conversation_id: 0b28c799-040d-43fd-9425-341693ae2085
create_time: 2026-06-22T14:27:02.000Z
format: html
aliases: [HFI_文献时间线, HFI_文献时间线_v1]
---

# HFI_文献时间线 (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2026/06/FOMC与国债利率的政策识别|美联储FOMC与国债利率的政策识别]]

## Content

```html
<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>高频识别文献演化</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --navy:    #0D1B2A;
    --ink:     #1C2E40;
    --steel:   #2E4A62;
    --mist:    #6B8BA4;
    --silver:  #B8CDD9;
    --fog:     #E8EFF4;
    --paper:   #F4F7FA;
    --gold:    #C9A84C;
    --gold-lt: #E8D5A3;
    --white:   #FFFFFF;
  }

  body {
    background: var(--paper);
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 48px 24px;
  }

  .card {
    background: var(--white);
    border: 1px solid var(--silver);
    border-radius: 2px;
    width: 100%;
    max-width: 760px;
    overflow: hidden;
    box-shadow: 0 2px 24px rgba(13,27,42,0.08);
  }

  /* ── Header ── */
  .header {
    background: var(--navy);
    padding: 32px 40px 28px;
    position: relative;
    overflow: hidden;
  }
  .header::after {
    content: 'HFI';
    position: absolute;
    right: -8px;
    top: -16px;
    font-family: 'IM Fell English', serif;
    font-size: 120px;
    color: rgba(255,255,255,0.04);
    letter-spacing: -4px;
    pointer-events: none;
    user-select: none;
  }
  .header-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 10px;
  }
  .header-title {
    font-family: 'IM Fell English', serif;
    font-size: 26px;
    font-weight: 400;
    color: var(--white);
    line-height: 1.3;
  }
  .header-title em {
    font-style: italic;
    color: var(--gold-lt);
  }
  .header-sub {
    margin-top: 8px;
    font-size: 12.5px;
    color: var(--mist);
    font-weight: 300;
    letter-spacing: 0.2px;
  }

  /* ── Timeline body ── */
  .body {
    padding: 0 40px 40px;
    position: relative;
  }

  /* vertical rule */
  .body::before {
    content: '';
    position: absolute;
    left: 72px;
    top: 0;
    bottom: 40px;
    width: 1px;
    background: linear-gradient(to bottom, var(--silver), var(--fog));
  }

  /* ── Each paper row ── */
  .paper {
    display: grid;
    grid-template-columns: 32px 1fr;
    gap: 0 24px;
    padding: 28px 0 0 0;
    position: relative;
  }

  /* dot on the line */
  .paper::before {
    content: '';
    position: absolute;
    left: 64px; /* 40px body padding + 32px col - 8px = centre of col */
    top: 36px;
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--gold);
    border: 2px solid var(--white);
    box-shadow: 0 0 0 1px var(--gold);
    z-index: 1;
  }

  .year-col {
    padding-top: 28px;
  }
  .year {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--mist);
    letter-spacing: 0.5px;
    writing-mode: vertical-rl;
    text-orientation: mixed;
    transform: rotate(180deg);
    height: 44px;
    display: flex;
    align-items: center;
  }

  .content-col {
    border-left: none;
    padding-left: 16px;
  }

  .paper-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
  }
  .paper-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    font-weight: 500;
    color: var(--navy);
    letter-spacing: -0.3px;
  }
  .paper-id .abbr {
    color: var(--steel);
  }
  .paper-id .yr {
    color: var(--gold);
  }

  .paper-title {
    font-family: 'IM Fell English', serif;
    font-size: 13px;
    font-style: italic;
    color: var(--mist);
    font-weight: 400;
    margin-bottom: 12px;
    line-height: 1.4;
  }

  /* contribution chips */
  .chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 10px;
  }
  .chip {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    padding: 3px 9px;
    border-radius: 2px;
    background: var(--fog);
    color: var(--ink);
    border: 1px solid var(--silver);
    letter-spacing: 0.2px;
    white-space: nowrap;
  }
  .chip.gold {
    background: #FBF5E6;
    border-color: var(--gold-lt);
    color: #7A5C1E;
  }

  /* one-line insight */
  .insight {
    font-size: 12.5px;
    color: var(--steel);
    line-height: 1.6;
    padding-left: 10px;
    border-left: 2px solid var(--fog);
    font-weight: 400;
  }

  /* ── Arrow connector between papers ── */
  .arrow-row {
    display: flex;
    align-items: center;
    padding: 6px 0 0 56px;
    gap: 6px;
  }
  .arrow-line {
    width: 20px;
    height: 1px;
    background: var(--silver);
  }
  .arrow-label {
    font-size: 10.5px;
    color: var(--silver);
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.3px;
  }

  /* ── Footer ── */
  .footer {
    margin: 32px 40px 0;
    padding: 16px 0 0;
    border-top: 1px solid var(--fog);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .footer-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--silver);
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }
  .footer-note {
    font-size: 11px;
    color: var(--mist);
    font-style: italic;
    font-family: 'IM Fell English', serif;
  }

  /* ── Divider between body and footer ── */
  .spacer { height: 0; }
</style>
</head>
<body>
<div class="card">

  <!-- Header -->
  <div class="header">
    <div class="header-eyebrow">High-Frequency Identification · 文献演化</div>
    <div class="header-title">从期货意外到冲击分解：<em>HFI 四篇奠基文献</em></div>
    <div class="header-sub">为什么高频市场数据具有宏观识别价值</div>
  </div>

  <!-- Timeline -->
  <div class="body">

    <!-- Kuttner 2001 -->
    <div class="paper">
      <div class="year-col"><div class="year">'01</div></div>
      <div class="content-col">
        <div class="paper-tag">
          <span class="paper-id"><span class="abbr">Kuttner</span> <span class="yr">'01</span></span>
        </div>
        <div class="paper-title">Monetary Policy Surprises and Interest Rates</div>
        <div class="chips">
          <span class="chip gold">联邦基金期货</span>
          <span class="chip">预期内 vs. 意外成分</span>
          <span class="chip">事件窗口</span>
        </div>
        <div class="insight">
          用期货隐含利率拆解政策变动：预期内部分对市场无冲击，<strong>意外成分</strong>才是真正的货币政策信号——奠定 HFI 的核心逻辑
        </div>
      </div>
    </div>

    <div class="arrow-row">
      <div class="arrow-line"></div>
      <div class="arrow-label">扩展至日内数据 · 多期限</div>
    </div>

    <!-- Nakamura & Steinsson 2018 -->
    <div class="paper">
      <div class="year-col"><div class="year">'18</div></div>
      <div class="content-col">
        <div class="paper-tag">
          <span class="paper-id"><span class="abbr">Nakamura &amp; Steinsson</span> <span class="yr">'18</span></span>
        </div>
        <div class="paper-title">High-Frequency Identification of Monetary Non-Neutrality: The Information Effect</div>
        <div class="chips">
          <span class="chip gold">30 分钟窗口</span>
          <span class="chip">零息国债收益率</span>
          <span class="chip">PCA 主成分</span>
          <span class="chip">信息效应</span>
        </div>
        <div class="insight">
          FOMC 公告前后 30 min 窗口内，宏观冲击不可能发生 →<strong> 外生性由设计保证</strong>；同时发现央行公告还传递对经济形势的私有信息（信息效应）
        </div>
      </div>
    </div>

    <div class="arrow-row">
      <div class="arrow-line"></div>
      <div class="arrow-label">引入为 Proxy-SVAR 外部工具变量</div>
    </div>

    <!-- Gertler & Karadi 2015 -->
    <div class="paper">
      <div class="year-col"><div class="year">'15</div></div>
      <div class="content-col">
        <div class="paper-tag">
          <span class="paper-id"><span class="abbr">Gertler &amp; Karadi</span> <span class="yr">'15</span></span>
        </div>
        <div class="paper-title">Monetary Policy Surprises, Credit Costs, and Economic Activity</div>
        <div class="chips">
          <span class="chip gold">Proxy-SVAR</span>
          <span class="chip">外部工具变量</span>
          <span class="chip">因果识别</span>
        </div>
        <div class="insight">
          将高频意外作为结构 VAR 的外部工具变量，绕开内生性问题 → <strong>因果方向由时序保证</strong>；与 Ramey (2016) 共同确立现行基准方法
        </div>
      </div>
    </div>

    <div class="arrow-row">
      <div class="arrow-line"></div>
      <div class="arrow-label">引入股价联动 · 分离冲击性质</div>
    </div>

    <!-- Jarociński & Karadi 2020 -->
    <div class="paper">
      <div class="year-col"><div class="year">'20</div></div>
      <div class="content-col">
        <div class="paper-tag">
          <span class="paper-id"><span class="abbr">Jarociński &amp; Karadi</span> <span class="yr">'20</span></span>
        </div>
        <div class="paper-title">Deconstructing Monetary Policy Surprises: The Role of Information Shocks</div>
        <div class="chips">
          <span class="chip gold">利率 × 股价联动</span>
          <span class="chip">符号约束</span>
          <span class="chip">纯货币冲击</span>
          <span class="chip">信息披露冲击</span>
        </div>
        <div class="insight">
          利率↑ &amp; 股价↓ → <strong>纯紧缩冲击</strong>（央行主动收紧）；
          利率↑ &amp; 股价↑ → <strong>信息冲击</strong>（央行暗示经济向好）——两类冲击混同将导致方向性识别错误
        </div>
      </div>
    </div>

    <!-- Footer inside body so it sits after last paper -->
    <div class="footer">
      <div class="footer-label">JME · QJE · AEJ: Macro</div>
      <div class="footer-note">exogeneity by design</div>
    </div>

  </div><!-- /body -->

</div><!-- /card -->
</body>
</html>

```
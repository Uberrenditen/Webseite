+++
title = 'Dein erstes Investment – einfach, sicher, sofort'
date = 2025-08-24T16:55:24+01:00
draft = false
description = "Du willst dein Geld für dich arbeiten lassen, weißt aber nicht wo anfangen? In 10 Minuten richtest du deinen ersten ETF-Sparplan ein – ohne Vorkenntnisse."
image = "/images/value-investing2.webp"
authors = ["überrenditen"]
avatar = "/images/a/value-investing.webp"
+++

<style>
  :root {
    --tr-green: #0a6640;
    --tr-green-light: #e6f4ed;
    --tr-green-mid: #1a8a55;
    --navy: #0f2240;
    --navy-light: #1a3460;
    --cream: #faf9f6;
    --text-main: #1a1a2e;
    --text-muted: #5a6478;
    --border: #e2e8f0;
    --gold: #c9922a;
    --gold-light: #fef6e7;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  .lp-wrap {
    font-family: 'Georgia', 'Times New Roman', serif;
    color: var(--text-main);
    max-width: 780px;
    margin: 0 auto;
    padding: 0 1rem;
  }

  /* ── HERO ── */
  .hero {
    background: linear-gradient(160deg, var(--navy) 0%, #1a3460 60%, #0a6640 100%);
    border-radius: 16px;
    padding: 4rem 2.5rem 3.5rem;
    text-align: center;
    margin: 2rem 0 3rem;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    width: 400px; height: 400px;
    border-radius: 50%;
    background: rgba(255,255,255,0.03);
    top: -120px; right: -80px;
  }
  .hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.25);
    color: #d4f0e2;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.45rem 1.1rem;
    border-radius: 100px;
    margin-bottom: 1.6rem;
  }
  .hero h1 {
    font-size: clamp(1.9rem, 5vw, 2.8rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 1.2rem;
  }
  .hero h1 span {
    color: #5dd9a0;
  }
  .hero p {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 1.1rem;
    color: #b0c8e0;
    max-width: 520px;
    margin: 0 auto 2.2rem;
    line-height: 1.65;
  }
  .btn-primary {
    display: inline-block;
    background: #1db86e;
    color: #fff;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    padding: 1rem 2.5rem;
    border-radius: 8px;
    text-decoration: none;
    letter-spacing: 0.01em;
    transition: background 0.2s, transform 0.15s;
    border: none;
    cursor: pointer;
  }
  .btn-primary:hover { background: #18a660; transform: translateY(-1px); }
  .hero-sub {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.82rem;
    color: rgba(255,255,255,0.45);
    margin-top: 1rem;
  }

  /* ── TRUST BAR ── */
  .trust-bar {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem 2rem;
    margin-bottom: 3.5rem;
    padding: 0 0.5rem;
  }
  .trust-item {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.88rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .trust-item::before {
    content: '✓';
    color: var(--tr-green-mid);
    font-weight: 700;
  }

  /* ── SECTION TITLE ── */
  .section-label {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--tr-green-mid);
    font-weight: 600;
    margin-bottom: 0.6rem;
  }
  .section-title {
    font-size: clamp(1.5rem, 3.5vw, 2rem);
    font-weight: 700;
    color: var(--navy);
    line-height: 1.25;
    margin-bottom: 0.9rem;
  }
  .section-intro {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 1rem;
    color: var(--text-muted);
    line-height: 1.7;
    max-width: 600px;
    margin-bottom: 2.5rem;
  }

  /* ── WHY ETF ── */
  .why-section { margin-bottom: 4rem; }
  .why-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.25rem;
  }
  .why-card {
    background: var(--cream);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem 1.4rem;
  }
  .why-icon {
    width: 44px; height: 44px;
    background: var(--tr-green-light);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    margin-bottom: 1rem;
  }
  .why-card h3 {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 0.5rem;
  }
  .why-card p {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
  }

  /* ── COMPARISON TABLE ── */
  .compare-section { margin-bottom: 4rem; }
  .compare-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.92rem;
  }
  .compare-table th {
    padding: 0.8rem 1rem;
    text-align: left;
    font-size: 0.8rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-muted);
    border-bottom: 2px solid var(--border);
  }
  .compare-table td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid var(--border);
    color: var(--text-main);
    vertical-align: middle;
  }
  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table .col-etf {
    background: var(--tr-green-light);
    font-weight: 600;
    color: var(--tr-green);
  }
  .compare-table .col-etf td { color: var(--tr-green); }
  .check { color: #1a8a55; font-weight: 700; }
  .cross { color: #c0392b; }

  /* ── STEPS ── */
  .steps-section { margin-bottom: 4rem; }
  .step-list { display: flex; flex-direction: column; gap: 1.25rem; }
  .step-item {
    display: flex;
    gap: 1.25rem;
    align-items: flex-start;
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.4rem;
  }
  .step-num {
    min-width: 40px; height: 40px;
    border-radius: 50%;
    background: var(--navy);
    color: #fff;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-weight: 700;
    font-size: 1rem;
    display: flex; align-items: center; justify-content: center;
  }
  .step-body h3 {
    font-size: 1rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 0.35rem;
  }
  .step-body p {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
  }
  .step-time {
    font-size: 0.78rem;
    color: var(--tr-green-mid);
    font-weight: 600;
    margin-top: 0.4rem;
  }

  /* ── STAT CALLOUT ── */
  .stat-callout {
    background: var(--navy);
    border-radius: 14px;
    padding: 2.5rem 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1.5rem;
    margin-bottom: 4rem;
    text-align: center;
  }
  .stat-item {}
  .stat-num {
    font-size: 2.2rem;
    font-weight: 700;
    color: #5dd9a0;
    line-height: 1;
    margin-bottom: 0.4rem;
  }
  .stat-label {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.85rem;
    color: rgba(255,255,255,0.55);
  }

  /* ── ETF RECOMMENDATION ── */
  .etf-section { margin-bottom: 4rem; }
  .etf-card {
    background: var(--gold-light);
    border: 1.5px solid #e8c97a;
    border-radius: 14px;
    padding: 1.8rem 1.8rem;
  }
  .etf-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.2rem;
  }
  .etf-badge {
    background: var(--gold);
    color: #fff;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border-radius: 100px;
  }
  .etf-name {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--navy);
  }
  .etf-ticker {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.88rem;
    color: var(--text-muted);
  }
  .etf-facts {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 1rem;
    margin-top: 1.2rem;
  }
  .etf-fact-label {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 0.2rem;
  }
  .etf-fact-value {
    font-size: 1rem;
    font-weight: 700;
    color: var(--navy);
  }

  /* ── CTA FINAL ── */
  .cta-final {
    background: linear-gradient(135deg, var(--tr-green) 0%, #0a5535 100%);
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    margin-bottom: 3rem;
  }
  .cta-final h2 {
    font-size: clamp(1.5rem, 4vw, 2rem);
    font-weight: 700;
    color: #fff;
    margin-bottom: 0.8rem;
  }
  .cta-final p {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: rgba(255,255,255,0.7);
    font-size: 1rem;
    margin-bottom: 2rem;
    line-height: 1.6;
  }
  .btn-white {
    display: inline-block;
    background: #fff;
    color: var(--tr-green);
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    padding: 1rem 2.5rem;
    border-radius: 8px;
    text-decoration: none;
    transition: opacity 0.2s, transform 0.15s;
  }
  .btn-white:hover { opacity: 0.92; transform: translateY(-1px); }
  .cta-disclaimer {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.78rem;
    color: rgba(255,255,255,0.4);
    margin-top: 1rem;
  }

  /* ── FAQ ── */
  .faq-section { margin-bottom: 4rem; }
  .faq-list { display: flex; flex-direction: column; gap: 0; }
  .faq-item {
    border-bottom: 1px solid var(--border);
    padding: 1.2rem 0;
  }
  .faq-q {
    font-size: 1rem;
    font-weight: 700;
    color: var(--navy);
    margin-bottom: 0.5rem;
  }
  .faq-a {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.92rem;
    color: var(--text-muted);
    line-height: 1.65;
  }

  /* ── DISCLAIMER ── */
  .disclaimer {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 0.78rem;
    color: #aab0bb;
    line-height: 1.6;
    border-top: 1px solid var(--border);
    padding-top: 1.5rem;
    margin-bottom: 3rem;
  }

  @media (max-width: 500px) {
    .hero { padding: 2.5rem 1.4rem 2.5rem; }
    .stat-callout { padding: 1.8rem 1.2rem; }
    .cta-final { padding: 2rem 1.2rem; }
  }
</style>

<div class="lp-wrap">

  <!-- HERO -->
  <section class="hero">
    <div class="hero-badge">Für Einsteiger · Kostenlos starten</div>
    <h1>Lass dein Geld für dich<br><span>arbeiten – nicht umgekehrt.</span></h1>
    <p>Kein Finanzstudium. Kein Startkapital von 10.000 €. Nur 1 Konto, 1 ETF, 10 Minuten – und dein erstes Investment läuft.</p>
    <a href="DEIN-AFFILIATE-LINK" class="btn-primary">Jetzt Konto bei Trade Republic eröffnen →</a>
    <div class="hero-sub">Kostenlos · Keine Mindesteinlage · BaFin-reguliert</div>
  </section>

  <!-- TRUST BAR -->
  <div class="trust-bar">
    <span class="trust-item">Keine Depotgebühren</span>
    <span class="trust-item">Ab 1 € Sparplan möglich</span>
    <span class="trust-item">Einlagensicherung bis 100.000 €</span>
    <span class="trust-item">Über 4 Mio. Kunden in Europa</span>
  </div>

  <!-- WHY ETF -->
  <section class="why-section">
    <div class="section-label">Warum ETF?</div>
    <div class="section-title">Die klügste Art, Vermögen aufzubauen</div>
    <p class="section-intro">Professionelle Investoren nutzen ETFs seit Jahrzehnten. Heute steht diese Strategie jedem offen – auch dir.</p>
    <div class="why-grid">
      <div class="why-card">
        <div class="why-icon">🌍</div>
        <h3>Breite Streuung</h3>
        <p>Ein ETF investiert automatisch in hunderte Unternehmen weltweit. Fällt eines, tragen die anderen.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">💰</div>
        <h3>Günstige Kosten</h3>
        <p>ETFs kosten oft nur 0,07–0,20 % pro Jahr. Aktiv verwaltete Fonds verlangen das 10-fache – mit schlechteren Ergebnissen.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">⏱️</div>
        <h3>Kein Aufwand</h3>
        <p>Sparplan einrichten, fertig. Das System kauft automatisch – du musst nichts beobachten oder entscheiden.</p>
      </div>
      <div class="why-card">
        <div class="why-icon">📈</div>
        <h3>Bewiesene Rendite</h3>
        <p>Der MSCI World hat in den letzten 50 Jahren im Schnitt etwa 7–9 % Rendite pro Jahr erzielt.</p>
      </div>
    </div>
  </section>

  <!-- STAT CALLOUT -->
  <div class="stat-callout">
    <div class="stat-item">
      <div class="stat-num">~8 %</div>
      <div class="stat-label">Durchschnittliche Jahresrendite<br>MSCI World (historisch)</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">1 €</div>
      <div class="stat-label">Mindestbetrag für einen<br>Sparplan bei Trade Republic</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">0 €</div>
      <div class="stat-label">Depotgebühren &amp;<br>Kontoführung</div>
    </div>
  </div>

  <!-- COMPARISON -->
  <section class="compare-section">
    <div class="section-label">Der Vergleich</div>
    <div class="section-title">ETF-Sparplan vs. andere Möglichkeiten</div>
    <table class="compare-table">
      <thead>
        <tr>
          <th>Merkmal</th>
          <th class="col-etf">ETF-Sparplan ✓</th>
          <th>Tagesgeld</th>
          <th>Aktiver Fonds</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Ø Rendite p.a.</td>
          <td class="col-etf">7–9 %</td>
          <td>2–3 %</td>
          <td>4–6 %</td>
        </tr>
        <tr>
          <td>Kosten</td>
          <td class="col-etf">0,07–0,20 %</td>
          <td>keine</td>
          <td>1,5–2,5 %</td>
        </tr>
        <tr>
          <td>Diversifikation</td>
          <td class="col-etf"><span class="check">✓ Global</span></td>
          <td><span class="cross">✗ keine</span></td>
          <td><span class="check">✓ begrenzt</span></td>
        </tr>
        <tr>
          <td>Automatisierbar</td>
          <td class="col-etf"><span class="check">✓ ja</span></td>
          <td><span class="check">✓ ja</span></td>
          <td><span class="cross">✗ oft nicht</span></td>
        </tr>
        <tr>
          <td>Startkapital nötig</td>
          <td class="col-etf">ab 1 €</td>
          <td>variiert</td>
          <td>oft 1.000 €+</td>
        </tr>
      </tbody>
    </table>
  </section>

  <!-- ETF EMPFEHLUNG -->
  <section class="etf-section">
    <div class="section-label">Meine Empfehlung</div>
    <div class="section-title">Womit du anfangen solltest</div>
    <p class="section-intro">Für den Einstieg ist ein breit gestreuter World-ETF die bewährteste Wahl unter Privatanlegern.</p>
    <div class="etf-card">
      <div class="etf-header">
        <div>
          <div class="etf-badge">Einsteiger-Empfehlung</div>
        </div>
      </div>
      <div class="etf-name">Vanguard FTSE All-World UCITS ETF</div>
      <div class="etf-ticker">ISIN: IE00B3RBWM25 · Ticker: VWCE</div>
      <div class="etf-facts">
        <div>
          <div class="etf-fact-label">Länder</div>
          <div class="etf-fact-value">49 Länder</div>
        </div>
        <div>
          <div class="etf-fact-label">Unternehmen</div>
          <div class="etf-fact-value">~3.700</div>
        </div>
        <div>
          <div class="etf-fact-label">Kosten (TER)</div>
          <div class="etf-fact-value">0,22 % p.a.</div>
        </div>
        <div>
          <div class="etf-fact-label">Ausschüttung</div>
          <div class="etf-fact-value">Thesaurierend</div>
        </div>
      </div>
    </div>
  </section>

  <!-- STEPS -->
  <section class="steps-section">
    <div class="section-label">So geht's</div>
    <div class="section-title">In 3 Schritten zum ersten Sparplan</div>
    <p class="section-intro">Kein Papierkram. Keine Bankfiliale. Kein Vorwissen nötig.</p>
    <div class="step-list">
      <div class="step-item">
        <div class="step-num">1</div>
        <div class="step-body">
          <h3>Konto eröffnen</h3>
          <p>Klicke auf den Button unten und eröffne dein kostenloses Trade Republic-Konto. Nur Personalausweis und 5 Minuten nötig.</p>
          <div class="step-time">⏱ ca. 5 Minuten</div>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">2</div>
        <div class="step-body">
          <h3>ETF suchen &amp; auswählen</h3>
          <p>Suche in der App nach „VWCE" oder „FTSE All-World". Wähle den Vanguard FTSE All-World ETF aus.</p>
          <div class="step-time">⏱ 2 Minuten</div>
        </div>
      </div>
      <div class="step-item">
        <div class="step-num">3</div>
        <div class="step-body">
          <h3>Sparplan einrichten</h3>
          <p>Wähle deinen Betrag – z. B. 25, 50 oder 100 € pro Monat. Wähle ein Datum. Fertig. Das System kauft automatisch.</p>
          <div class="step-time">⏱ 3 Minuten</div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA FINAL -->
  <section class="cta-final">
    <h2>Heute starten. Nicht nächste Woche.</h2>
    <p>Jeder Monat ohne Sparplan ist ein Monat, in dem dein Geld an Kaufkraft verliert. Die beste Zeit war gestern – die zweitbeste ist jetzt.</p>
    <a href="DEIN-AFFILIATE-LINK" class="btn-white">Kostenloses Konto bei Trade Republic eröffnen</a>
    <div class="cta-disclaimer">Keine Mindesteinlage · Keine Depotgebühren · In 10 Minuten fertig</div>
  </section>

  <!-- FAQ -->
  <section class="faq-section">
    <div class="section-label">Häufige Fragen</div>
    <div class="section-title">Was Anfänger immer fragen</div>
    <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">Kann ich mit 25 € im Monat wirklich etwas aufbauen?</div>
        <div class="faq-a">Ja. 25 € monatlich über 20 Jahre bei 7 % Rendite ergeben rund 13.000 €. Nicht mit dem Zählen aufhören – mit dem Investieren anfangen.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Was passiert, wenn die Börse crasht?</div>
        <div class="faq-a">Du kaufst einfach weiter – zu günstigeren Preisen. Das nennt sich Cost-Averaging-Effekt. Langfristig hat sich der Markt nach jedem Crash erholt.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Ist mein Geld sicher bei Trade Republic?</div>
        <div class="faq-a">Trade Republic ist BaFin-reguliert. Deine Aktien und ETFs sind Sondervermögen – getrennt vom Firmenvermögen, also auch im Insolvenzfall geschützt. Einlagen auf dem Verrechnungskonto sind bis 100.000 € durch den gesetzlichen Einlagensicherungsfonds abgesichert.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Kann ich den Sparplan jederzeit stoppen?</div>
        <div class="faq-a">Ja, jederzeit und kostenlos. Kein Vertrag, keine Kündigungsfrist. Du bist vollständig flexibel.</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">Muss ich das Geld versteuern?</div>
        <div class="faq-a">Gewinne und Dividenden sind in Deutschland steuerpflichtig (Abgeltungssteuer 25 % + Soli). Allerdings gilt ein jährlicher Freibetrag von 1.000 € (Single) bzw. 2.000 € (Verheiratete), den du nutzen solltest.</div>
      </div>
    </div>
  </section>

  <!-- DISCLAIMER -->
  <p class="disclaimer">
    <strong>Hinweis:</strong> Dieser Artikel stellt keine Anlageberatung dar. Investitionen in ETFs sind mit Risiken verbunden. Historische Renditen sind kein Garant für zukünftige Ergebnisse. Dieser Beitrag enthält Affiliate-Links – wenn du über diese Links ein Konto eröffnest, erhalte ich eine Vergütung, ohne dass dir dadurch Kosten entstehen.
  </p>

</div>
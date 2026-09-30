---
title: "CFTC staff advisory — mention markets presumptively manipulable (Letter 26-27)"
type: source
tags: [source, rss, pm-retail, regulatory, cftc, kalshi, k179]
keywords: [cftc-letter-26-27, mention-markets, core-principle-3, dcm, manipulation, attendance-contracts, interaction-contracts]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/prediction-markets-crossover.md
  - concepts/kalshi-spotify-oracle-manipulation-2026-07.md
  - concepts/pm-copy-trading-retail-risks.md
  - sources/daily-digest-rss-pm-regulatory-2026-09-29.md
  - sources/daily-digest-batch-k179-2026-09-30.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: REFERENCE — regulatory awareness; no operator action, no pm scp
wire_status: policy_wired
---

## Relations

- @entities/platforms/kalshi.md — Kalshi pulled sports mention markets ahead of the advisory
- @concepts/prediction-markets-crossover.md — mention markets as a wagering product
- @concepts/kalshi-spotify-oracle-manipulation-2026-07.md — prior stream-botting manipulation case
- @sources/daily-digest-rss-pm-regulatory-2026-09-29.md — K178 title-only stub this page replaces

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CFTC Sends Memo On Potential Mention Market Manipulation |
| **URL** | https://www.legalsportsreport.com/278839/cftc-sends-memo-on-potential-mention-market-manipulation/ |
| **Feed** | Legal Sports Report (`legal-sports-report`) |
| **Published** | 2026-09-23 |
| **Primary document** | CFTC Staff Letter No. 26-27, Division of Market Oversight (DMO), dated 2026-09-22, signed by Acting Director Duncan Hennes |
| **Body access** | LSR returns HTTP 403 to direct fetch; body recovered via Brave LLM Context + corroborating sources |

## Narrative

The CFTC's Division of Market Oversight told every designated contract market (DCM) that **"mention markets" are presumptively susceptible to manipulation**. The advisory shifts the burden of proof from traders to the exchanges that list the contracts.

### What the advisory covers

The letter defines "Mention Markets" broadly. They are event contracts that settle on whether **a named person**:

- says or "mentions" certain words,
- attends or appears at an event,
- interacts with another person (for example, a handshake).

Footnote 5 extends the analysis to "a small or select group of individuals acting together, or with a shared purpose."

DMO draws a line against ordinary event contracts. Most listed contracts settle on outcomes that are "independently generated, externally verifiable" and "outside the control of any single person" — economic data, election results, or regulated sporting events. Mention markets settle on **"the discrete conduct of a named person"** instead.

### The legal hook

The letter applies **Core Principle 3** of Section 5(d)(3) of the Commodity Exchange Act (CEA). Staff "may view Mention Markets as presumptively readily susceptible to manipulation and accordingly expect a heightened showing in support of any submission seeking to list such contracts."

The four factors a DCM must address in a Part 40 filing [CONFIRMED — repeated by five independent outlets]:

| # | Factor | Concern |
|---|--------|---------|
| 1 | **Independent obligations** | Does the controlling person face legal, professional, or contractual duties strong enough to deter gaming? |
| 2 | **External pressure** | Can others manipulate the outcome by pressuring, persuading, or paying the person? |
| 3 | **Verification and public scrutiny** | Is the outcome independently confirmable, and does it occur where real public attention exists? Private settings and casual remarks are easier to exploit. |
| 4 | **Safeguards** | Are trading rules, surveillance, and controls strong enough to detect manipulation and insider trading? |

Footnote 15 is the practical checklist: restricted participant lists, third-party screening vendors, periodic employment-status updates, "pop-up" attestations before trading, and position limits "sized so that manipulation would be economically irrational relative to its cost."

### What it does not do

- It is **not a ban**. "Nothing in this advisory should be read to discourage" the markets.
- It creates **no new binding rules or regulations**.
- It provides **no no-action position**.
- It reflects **DMO staff views only** and "does not necessarily represent the views of the Commission."
- DCMs are instead "encouraged to engage with DMO staff" during contract design.

### Documented manipulation cases cited

| Actor | Conduct | Sanction |
|-------|---------|----------|
| **Gabriel Perez** — White House teleprompter operator | Traded Kalshi mention contracts on words President Trump would say; profit reported as "more than $100,000" | CFTC order: **$172,539**; three-year trading ban [TENTATIVE — figures vary by outlet] |
| **Gannon Ken Van Dyke** — U.S. Army Master Sergeant | Used classified information on the capture of Venezuelan President Nicolás Maduro | More than **$400,000** profit |
| **George Santos** — former Congressman | Bought Kalshi contracts that settled against his own State-of-the-Union attendance | **$35,000** fine (CFTC per LSR); CMP reported as **$17,500** in one comparison table; first person permanently banned by Kalshi [TENTATIVE] |
| **Brian Armstrong** — Coinbase CEO | Recited a string of unrelated buzzwords at the end of an October earnings call that matched listed Kalshi and Polymarket mention markets | No sanction; cited as an example |

### Market reaction

- **Kalshi** paused sports-broadcast mention markets in August 2026 amid the federal review.
- The **NFL** sent two letters to prediction platforms calling such contracts "objectionable."
- **Jaret Seiberg** (TD Securities) said the advisory "effectively" shuts down the "vast majority" of mention markets. He reads it as a long-term positive: it reduces pressure on Congress to "fast track" legislation, and such legislation "could become a vehicle for broader limits on prediction markets – including a ban on sports contracts – which would be a bigger long-term threat to the industry."
- **CFTC Chair Mike Selig** said on CNBC that "we've had a lot of concern with these markets" and "a large number of these contracts have issues."

### Comparative jurisdiction table

| Jurisdiction | Instrument | Requirement |
|--------------|-----------|-------------|
| **US (CFTC/DMO)** | Letter 26-27, 2026-09-22 | Rebuttable presumption of manipulability; four-factor showing in Part 40 filings |
| **Ontario (AGCO)** | Registrar's Standards for Internet Gaming, Standard 4.34 (amended Feb 2022) | Every bet's outcome must "be generated by a reliable and independent process" and "not [be] affected by any bet placed" |
| **Great Britain (Gambling Commission)** | Gambling Act 2005 s.42; LCCP 15.1.2 | Licensees must report suspected offences "as soon as reasonably practicable"; cheating carries up to two years' imprisonment |
| **EU (ESMA)** | Public statement 2026-07-03; national binary-option measures since 2018 | Event contracts meeting the MiFID II financial-instrument definition are treated as binary options, barred from retail sale |

## Snippets

> "Because the outcome of these contracts is often within the control of a small number of actors, the settlement condition is comparatively easier to cause, prevent, or influence for personal gain." [Source: CFTC Letter 26-27 via LSR, retrieved 2026-09-30]

> "In certain circumstances where the costs of manipulation or the likelihood of detection is low and sufficient safeguards are absent, the person whose conduct determines settlement (or those in close proximity of such person) may readily influence the outcome of the contract, exploit advance knowledge of it, or both." [Source: CFTC Letter 26-27, retrieved 2026-09-30]

> "Such legislation could become a vehicle for broader limits on prediction markets – including a ban on sports contracts – which would be a bigger long-term threat to the industry." — Jaret Seiberg, TD Securities [Source: LSR, retrieved 2026-09-30]

## Dead Ends

- **Penalty figures conflict across outlets.** Perez is reported as both "more than $100,000 profit" and a "$172,539" order; Santos as both $35,000 and $17,500. Do not cite a single number without the outlet. [NEEDS VERIFICATION 2026-09-30]
- The advisory is **staff guidance, not enforcement**. It reads as a deterrent, not a ban. Do not model it as a hard delisting event.

---
title: DraftKings
type: entity
tags: [entity, platform, sportsbook, dfs, us-legal]
keywords: [draftkings, dk, sportsbook, dfs, best-ball]
related:
  - concepts/best-ball-strategy.md
  - concepts/dfs-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/sharp-vs-soft-books.md
  - concepts/sports-betting-fundamentals.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - entities/people/rufus-peabody.md
  - entities/platforms/fanduel.md
  - entities/platforms/underdog-fantasy.md
  - entities/sports/nba-betting.md
  - entities/sports/nfl-betting.md
  - entities/sports/world-cup-2026-betting.md
  - entities/tools/pydfs-lineup-optimizer.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/tools/wc2026-agents.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - concepts/parlay-and-correlated-bets.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
  - sources/daily-digest-rss-week1-pm-nfl-2026-09-11.md
  - sources/nfl-betting-dfs-intelligence-week1-2026-09-11.md
  - sources/rss-lsr-nfl-app-downloads-pm-share-2026-09-24.md
  - sources/rss-sbc-summit-lisbon-2026-09-29.md
  - sources/daily-digest-batch-k179-2026-09-30.md
  - entities/sports/nhl-betting.md
  - entities/sports/cfb-betting.md
  - sources/rss-lsr-pm-industry-2026-09-29-30.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - sources/rss-pm-legal-2026-10-07-09.md
  - sources/rss-operator-scrutiny-2026-10-07-08.md
  - sources/daily-digest-batch-k183-2026-10-09.md
maturity: draft
created: 2026-05-31
updated: 2026-10-09
---

## Relations

- @entities/platforms/fanduel.md — primary US competitor
- @concepts/dfs-strategy-overview.md — DFS product
- @concepts/sharp-vs-soft-books.md — retail/soft book classification
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160 used mostly DK opening 1X2 previews as market baseline
- @entities/tools/wc2026-agents.md — released odds + LLM agent P&L vs DK-priced market
- @sources/daily-digest-rss-industry-2026-08-14.md — DKeX football 40.2 + COMBOS
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — NFL official betting partner (with FanDuel / Fanatics)

## Raw Concept

Major US legal operator — sportsbook + DFS + casino (+ best ball). Stub pending deep ingest.

## Narrative

DraftKings operates **sports betting**, **DFS**, **iCasino**, and **best ball** in licensed US states. Classified as **soft/rec retail** for sharp betting purposes — strong promos, account limits for winners possible.

### DKeX / Railbird (Aug 2026) [CONFIRMED]

DraftKings-owned DCM **Railbird Exchange (DKeX)** self-certified nine football event contracts (win/spread/total/player-or-team stat/outright/award/head-to-head) plus a **COMBOS** product that settles as the **product of component binary YES values**. $1 notional, NCAA included, Reg **40.2** (no CFTC product approval). This is DK’s **in-house PM** path vs routing Predictions volume through partners. Retail: shop DKeX vs Kalshi vs book SGP on the same football questions; COMBOS is still a **joint-implied** price, not a vig-free parlay. Hub: `@sources/daily-digest-rss-industry-2026-08-14.md`, `@concepts/parlay-and-correlated-bets.md`.

**NFL league partnership (K168, 2026-08-27) [TENTATIVE — LSR title]:** DraftKings, FanDuel, and Fanatics named NFL sports-betting partners; league language covers injury/officiating/knowable-in-advance wagers. Hub: `@sources/daily-digest-rss-nfl-week0-2026-08-31.md`.

**Anti-Kalshi ad campaign (K170, 2026-09-09) [TENTATIVE — LSR]:** New DK ads target Kalshi review complaints — retail PM vs book marketing war during NFL Week 1 ad blitz. Hub: `@sources/daily-digest-rss-week1-pm-nfl-2026-09-11.md`.

### Seminole Tribe sues over DKeX and Pick6 (K183, 2026-10-08) [CONFIRMED]

The **Seminole Tribe of Florida sued DraftKings** in Broward County — a **72-page** complaint naming **DraftKings Inc., CEO Jason Robins, and GUS III LLC** (DraftKings Predictions). The Tribe holds **exclusive** online sports betting rights under the 2021 compact.

**The argument runs on the IGRA and the compact, not the Commodity Exchange Act** — a different hook from the state cases.

**The evidence is DraftKings' own material:**

- **"1-800-GAMBLER" on DraftKings' advertisements.** "The warning is DraftKings' own admission, printed on its own advertisements, that the Super App sportsbook is a gambling product and not a financial market."
- The Florida page is **identical** to a licensed state's page apart from the label "prediction betting."
- DraftKings **separates** its sports page from other predictions.
- The Tribe alleges DraftKings **"secretly funded"** lawsuits attacking the compact.

**Relief:** injunction, damages, costs, and all Florida revenue — for problem-gambling programs. Robins is also accused of violating Florida's **anti-racketeering act**.

**DraftKings' response:** prediction markets "operate in accordance with applicable law"; Pick6 is "a peer-to-peer fantasy sports variant… not sports betting."

**Why only DraftKings?** A quoted observer suggests it may be "because then you're going after the instrumentality that has the full-throated support of the White House." Hub: `@sources/rss-pm-legal-2026-10-07-09.md`.

### AI scrutiny now spans three states (K183, 2026-10-08) [CONFIRMED]

The K180 review has widened from Michigan and Massachusetts to include **New York** and **Maine**:

| State | Action |
|-------|--------|
| **New York** | Gaming Commission took up two proposals on **2026-10-09**: "Use of artificial intelligence for wagering purposes" — which would **bar AI for personalized bonuses, promotions, or bet suggestions** — and "Safeguards for at-risk mobile sports wagering patrons" |
| **Massachusetts** | Chair Jordan Maynard asked the Executive Director to investigate AI/ML use by in-state sportsbooks |
| **Maine** | Gambling Control Unit monitoring |

The **NY proposals predate** the NYT exposé and are **not enacted**. Penalty exposure if targeting is found: fines, suspensions, or **licence revocation**. Details: `@sources/rss-operator-scrutiny-2026-10-07-08.md`.

### AI/VIP promotion scrutiny (K180, 2026-09-29) [CONFIRMED]

**Michigan** (MGCB) and **Massachusetts** regulators are both **reviewing** issues raised in *New York Times* and *ProPublica* reports on DraftKings' use of AI and machine learning in promotions and its VIP program. A proposed **class action** followed; the plaintiff argues DK breached its own privacy-notice commitment to use customer data for responsible-play assessment.

The underlying allegation: a machine-learning model on customer betting records predicted how promotions would affect individual users' eventual wins and losses, and the company then targeted users most likely to lose money or leave.

**Michigan consumer rules do not address AI directly.** The state requires a responsible-gaming logo, a helpline page, a disassociated-persons list, and an internet-gaming responsible-gaming database.

**Operator relevance:** this is a **responsible-gambling and platform-risk** signal, not an edge. It does not change DK's pricing or DFS product. Hub: `@sources/rss-lsr-pm-industry-2026-09-29-30.md`.

## Snippets

> "The COMBOS does not introduce a new underlying… [it] governs only the aggregation of those independently determined results." [Source: DKeX 40.2 filing via @sources/daily-digest-rss-industry-2026-08-14.md]

---
title: Daily digest RSS industry batch (2026-08-14)
type: source
tags: [source, web, daily-digest, rss, kalshi, draftkings, dkex, cftc, colorado]
keywords: [dkex, combos, cftc-emergency, ny-ag, colorado-sb-131, deposit-cap]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-14-daily.md
  - entities/platforms/kalshi.md
  - entities/platforms/draftkings.md
  - concepts/prediction-markets-crossover.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/kalshi-michigan-sports-injunction-2026-06.md
  - concepts/pickem-legal-and-tos-posture.md
  - entities/sports/nfl-betting.md
  - sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: validated
read_status: read
created: 2026-08-14
updated: 2026-08-31
---

## Relations

- @sweeps/2026-08-14-daily.md — RSS rows S6–S14
- @entities/platforms/draftkings.md — DKeX / COMBOS
- @entities/platforms/kalshi.md — CFTC emergency vs NY AG
- @entities/sports/nfl-betting.md — DKeX football contracts + Colorado sportsbook rules
- @concepts/kalshi-michigan-sports-injunction-2026-06.md — same preemption fight, NY chapter
- @osint-wiki/concepts/prediction-market-regulation-2026.md — OSINT regulation hub (CFTC/NY/Novig)
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — Aug 4–11 EH catch-up (Utah / 15-min / FlightAware)
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — next RSS cluster (NFL week-0)

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-08-14 |
| **Method** | LegalSportsBetting.com full text (S12–S14); LSR S9–S10 HTTP 403 — title + DKeX corroboration only |
| **Confidence** | [CONFIRMED] LSB; [TENTATIVE] LSR titles |

## Narrative

Industry/legal RSS from the first RSS-lane digest. **Not ingested here:** Event Horizon S1–S4 (OSINT already has full bodies; Novig stub `@sources/substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md`). **Skipped:** SBC B2B (S15–S17), NY biometric (S11), Trump Media (S6, LSR 403).

### S14 — DKeX self-certifies nine football contracts [CONFIRMED]

Railbird Exchange LLC d/b/a **DKeX** (DraftKings-owned DCM since Jun 2025; DK announced acquisition **2025-10-21**) filed nine football event contracts under **CFTC Reg 40.2** (self-cert; no commission decision). Certified ~**2026-08-12**; listable thereafter. Entity code **REX**; all listed as **swaps**.

| Code | Underlying question (paraphrase) |
|------|----------------------------------|
| FOOTBALLWIN | Will entity win period of event? |
| FOOTBALLSPREAD | Point differential vs opponent / condition |
| FOOTBALLTOTALS | Points vs threshold |
| FOOTBALLENTITYSTAT | Player **or** team stat vs threshold |
| FOOTBALLGAMESTAT | Event produces statistic vs threshold |
| FOOTBALLENTITYACHIEVEMENT | In-game achievement |
| FOOTBALLENTITYOUTPERFORM | Player vs designated opponent(s) on a metric |
| FOOTBALLAWARD | Season award confirmed by awarding body |
| FOOTBALLOUTRIGHT | Competition placement |

**Scope includes NCAA D-I/II/III**, plus NFL / CFL / UFL. Settlement hierarchy: governing body → ESPN / AP / NFL.com → official broadcasters; NFL snap counts from a vetted provider; NCAA “internally scouted player status.” First authoritative print settles; later corrections do **not** change settlement. Exchange may treat a result as clearly erroneous in sole discretion.

**Shared terms (all ten filings incl. COMBOS):** $1.00 notional, 1¢ tick, listed $0.01–$0.99, **125,000** contract position accountability, 24/7 except maintenance.

**COMBOS** (filed 2026-08-07, cert by Aug 11): “Will all [outcomes] occur?” Joint settlement of **two or more separately certified** constituents. YES value = **product of component YES settlements**. No nested COMBOS; duplicate constituent banned; any $0 component → COMBOS YES = $0 (accelerated settle under Rule 7.2). This is the PM analog of an SGP **without** a new underlying — retail still pays the joint-implied price, not sportsbook SGP hold, but correlation is **not** a free lunch (product of binaries). [Source: https://www.legalsportsbetting.com/news/dkex-self-certifies-nine-football-contracts-with-cftc-08-12-2026/ (retrieved 2026-08-14)]

**S9 LSR** (“DraftKings Eyes In-House Combos As Predictions Volume Surges”) — **403** this session. Title is consistent with the COMBOS filing; do not cite LSR volume numbers until a fetch succeeds. [NEEDS VERIFICATION 2026-08-14]

### S12 / S10 — CFTC emergency powers vs NY AG [CONFIRMED via LSB; LSR 403]

CFTC has used **emergency authority six times** in its history; **none since 1980** until Chairman **Michael Selig** used it **twice in ~30 days** to back Kalshi (Michigan, then New York). NY AG suit: illegal gambling via sports event contracts; seeks restitution up to **$36 billion**. CFTC order: KalshiEX keep operating under CEA Core Principles (i.e. continue serving NY). NY AG: CFTC “cannot manufacture a conflict”; Kalshi injunction arguments insufficient. Operator retail takeaway: **NY geofence / account risk is live** — same class as Michigan TRO (`@concepts/kalshi-michigan-sports-injunction-2026-06.md`), now with explicit federal “keep the lights on” instruction. Full CFTC/NY synthesis: `@osint-wiki/concepts/prediction-market-regulation-2026.md`. [Source: https://www.legalsportsbetting.com/news/cftc-uses-emergency-powers-to-protect-kalshi-sports-betting-08-13-2026/ (retrieved 2026-08-14)]

### S13 — Colorado SB 26-131 in force; prop ban cut [CONFIRMED]

Effective ~**2026-08-12** (day after 90-day referendum window; Polis signed 2026-06-01). Enacted:

- **Six deposits per customer per operator-defined 24h gaming day** (CRS 44-30-1506). Count is **per book**, no dollar cap on deposit size.
- **Credit-card funding ban**, including **indirect** (e-wallet funded by a card) — 44-30-1511(1)(d); up to $25k commission penalty + class 2 misdemeanor on the card clause.
- Push alerts banned **only when the app UI is not open**.

**Stripped before passage:** outright **proposition-bet ban**; ban on **limiting winning bettors**; 5-deposit / daytime ad blackout. Governing bodies may petition the commission to restrict wager types (replaces the blanket prop ban). **Pick'em / player props remain legal in Colorado** unless the commission later restricts a type. [Source: https://www.legalsportsbetting.com/news/colorado-sports-betting-law-takes-effect-prop-ban-cut-08-13-2026/ (retrieved 2026-08-14)]

## Snippets

> "The COMBOS does not introduce a new underlying, settlement methodology, or data source… [it] governs only the aggregation of those independently determined results." [Source: DKeX COMBOS 40.2 filing via LegalSportsBetting.com (retrieved 2026-08-14)]

> "The CFTC has only done this six times since their creation, but Chairman Michael Selig revived the powers for the first time since 1980." [Source: https://www.legalsportsbetting.com/news/cftc-uses-emergency-powers-to-protect-kalshi-sports-betting-08-13-2026/ (retrieved 2026-08-14)]

> "Amendments stripped a proposition-bet ban and a ban on limiting winning bettors before final passage." [Source: https://www.legalsportsbetting.com/news/colorado-sports-betting-law-takes-effect-prop-ban-cut-08-13-2026/ (retrieved 2026-08-14)]

## Dead Ends

- **S6 / S7 / S9 / S10 LSR** — 403 from this laptop; do not invent volume or quote figures from titles.
- **S11** NY biometric deposit plan — skipped (account-KYC, not wagering process).
- **nflverse GitHub tags / PFT rumor mill / SBC vendor PR** — awareness-only, not wiki ingest.

---
title: "NFL app downloads +28% YoY — prediction markets take ~47.5% of Week 2"
type: source
tags: [source, rss, pm-retail, industry, kalshi, polymarket, nfl, k179]
keywords: [sensor-tower, app-downloads, citizens, implied-vig, parlay-combos, notional-volume, market-expansion]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - concepts/sportsbook-pm-line-divergence.md
  - concepts/vig-and-hold.md
  - sources/daily-digest-rss-pm-regulatory-2026-09-29.md
  - sources/daily-digest-batch-k179-2026-09-30.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30
phase_0_verdict: REFERENCE — retail share + pricing data; no operator action
wire_status: policy_wired
---

## Relations

- @concepts/sportsbook-pm-line-divergence.md — Kalshi vs DK/FD implied vig, combos included
- @concepts/vig-and-hold.md — parlay combo hold figures
- @entities/platforms/kalshi.md — download counts and combo volume
- @entities/platforms/polymarket.md — download leader through two weeks

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | NFL Betting App Downloads Grow, But Prediction Markets Extend Early Lead |
| **URL** | https://www.legalsportsreport.com/279073/nfl-betting-app-downloads-grow-but-prediction-markets-extend-early-lead/ |
| **Author** | Sam McQuillan |
| **Feed** | Legal Sports Report |
| **Published** | 2026-09-24 |
| **Underlying data** | Sensor Tower downloads, quoted by Citizens (analyst firm) |
| **Body access** | Recovered via Brave LLM Context (LSR 403s direct fetch) |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/rss-legal-sports-report-2026-09-24-nfl-betting-app-downloads-grow-but-prediction-markets-extend.md`

## Narrative

NFL betting-app downloads rose **28% year over year in Week 2**. Prediction markets drove most of the growth while traditional sportsbooks kept losing customer-acquisition ground.

### Download counts

The week ending **2026-09-21** recorded **2.8 million** NFL betting-app downloads. Two-week season-to-date growth was **19%**.

| Operator | Week 2 | Season to date (2 weeks) |
|----------|--------|--------------------------|
| **Polymarket** | 624,000 | **1,370,000** (leader) |
| **Kalshi** | 706,000 | 1,310,000 |
| **DraftKings** | — | 805,000 |
| **FanDuel** | — | 502,000 |

Kalshi and Polymarket combined for **1.33 million** downloads in Week 2 — about **47.5%** of the weekly total.

Week 1 for comparison [Source: LSR 2026-09-16]: Polymarket 762,000 · Kalshi 592,000 · DraftKings 415,000 · FanDuel 265,000 · Sleeper 239,000. DraftKings fell **46%** YoY in Week 1 and FanDuel **36%**.

Citizens attributed the sportsbook weakness to difficult year-over-year comparisons and the absence of new state launches and acquisition pushes that boosted last season.

### Pricing — Kalshi's edge is real but narrow

Citizens found Kalshi offered **lower implied vig than DraftKings and FanDuel** on a sample of Week 2 NFL moneyline and totals markets. A separate read [Source: ReadWrite, 2026-09-25] gives the numbers: across 30 observations collected 2026-09-18, Kalshi averaged **4.22%** implied vig on moneyline and totals versus **4.43%** at FanDuel and **4.50%** at DraftKings — **excluding Kalshi's transaction fees**.

### The edge disappears on parlays

In a 15-observation sample of favorite + Over combinations, Kalshi's implied vig averaged **26.4%**, compared with **23.9%** at DraftKings. Citizens said Kalshi combo pricing was also **6%** higher than FanDuel's before transaction fees.

This matters because combos are now the bulk of Kalshi's book. Kalshi's combos generated **$26 billion** in volume over the preceding 30 days — **53%** of its total, against a 44% average over the previous 90 days.

### Reading the volume number correctly

The $26B figure is **notional trading volume**. It includes activity beyond the amount customers initially stake and is **not directly comparable** with traditional sportsbook handle. Do not set it beside an AGA handle estimate without saying so.

Citizens' customer-wallet analysis suggests prediction-market adoption may be **expanding the overall wagering market** rather than simply taking business from sportsbooks. The firm expects sportsbook handle growth to accelerate later in the year.

### On-field context

Through two weeks: favorites **23-9** straight up and **17-15** against the spread; **Unders cashed in 17 of 32** games.

## Snippets

> "Kalshi's combos generated $26 billion in volume over the preceding 30 days, representing 53% of its total, compared with a 44% average over the previous 90 days." [Source: LSR, 2026-09-24]

> "Those figures represent notional trading volume, which includes activity beyond the amount customers initially stake and is not directly comparable with traditional sportsbook handle." [Source: same]

> "Citizens said its customer-wallet analysis suggests prediction-market adoption may be expanding the overall wagering market rather than simply taking business from sportsbooks." [Source: same]

## Dead Ends

- **Downloads are not handle.** An app install says nothing about volume, hold, or CLV. Do not use download share as a sizing or edge signal.
- **Notional combo volume is not handle.** See above; the 53%-of-total figure is a mix signal only.
- Kalshi's implied-vig advantage is measured **before transaction fees**. Any cross-venue shop must net the fee before it can claim an edge. See @concepts/sportsbook-pm-line-divergence.md.
- The 4.22% / 4.43% / 4.50% triple comes from ReadWrite, a secondary source. Prefer the Citizens original if it becomes available. [NEEDS VERIFICATION 2026-09-30]

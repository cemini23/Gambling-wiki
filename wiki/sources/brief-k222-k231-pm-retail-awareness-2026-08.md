---
title: Briefs K222–K231 — PM retail awareness (Aug 2026)
type: source
tags: [source, brief, event-horizon, kalshi, polymarket, k222, k223, k225, k226, k231]
keywords: [ny-pm-tax, utah-preemption, 15-min, forecastEx, flightaware, fanduel-predicts]
related:
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/platforms/fanduel.md
  - concepts/prediction-markets-crossover.md
  - concepts/kalshi-michigan-sports-injunction-2026-06.md
  - sources/daily-digest-rss-industry-2026-08-14.md
maturity: validated
read_status: read
created: 2026-08-15
updated: 2026-08-15
---

## Relations

- @entities/platforms/kalshi.md — 15-min volume, Utah/CT/NY state fight, FlightAware suit
- @entities/platforms/polymarket.md — Yankees / ATP distribution; 5-min crypto
- @entities/platforms/fanduel.md — Predicts sports → Crypto.com
- @concepts/kalshi-michigan-sports-injunction-2026-06.md — Utah SJ is the same preemption class
- @osint-wiki/concepts/prediction-market-short-horizon-velocity.md — bot/CeminiSuite lens
- Local gitignored briefs: `briefs/2026-08-04_k222-event-horizon-ny-pm-tax.md` … `briefs/2026-08-11_k231-flightaware-kalshi.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-08-15 — wiki catch-up of Aug 4–11 gambling briefs (bodies already on OSINT) |
| **Method** | Cross-wiki stubs; do **not** duplicate OSINT deep-reads |
| **Confidence** | [CONFIRMED] via OSINT Event Horizon sources (retrieved same day as each brief) |

Five Event Horizon items were briefed into `briefs/` but never filed as wiki sources. Retail wagering takeaways only — no prod Kalshi/Polymarket orders.

## Narrative

### K222 — NY $10B PM tax headline is implausible [CONFIRMED]

Event Horizon reverse-engineers the WSJ-reported Kalshi/NY **$10B over five years** at ~6% tax to an implied **~$33B/yr** NY fee base — not credible vs Kalshi **~$2B** annualized revenue nationwide. Population-share sketch (~6% of US): **~$7M/yr** tax (**~$35M/5y**) before growth. NY sportsbooks paid **~$1.3B** tax in 2025 — a real PM tax cut could **cannibalize book handle**, not mint a new $10B pot. Also: Polymarket **ATP** exclusive streaming + Sportradar integrity for US users. [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-04-ny-pm-tax-10b.md]

### K223 — Race-call discipline + Utah SJ [CONFIRMED]

Kalshi/Polymarket social accounts called the MI Dem Senate primary early while the live market still had Stevens ~**25%** (El-Sayed had been ~97%). Trust risk into November midterms — treat venue “called” posts as **marketing**, not settlement. **Utah** federal summary judgment (Judge Shelby): CEA does **not** preempt Utah’s anti-gambling statute vs Kalshi sports contracts. Same state-vs-CFTC class as Michigan/NY. Flutter (FanDuel parent) earnings were a watch item that week. [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-05-michigan-senate-pm-calls.md]

### K225 — 15-minute-ification [CONFIRMED]

Kalshi thesis: **velocity + volatility → volume**. Sports still ~70–80% notional; crypto ~20%+ daily. Trailing-7d (Ticker Tracker via EH): **~$1.5B** Kalshi crypto, of which **~$1.1B** on **BTC 15-min**; seven of the top 10 crypto markets are 15-min; gold/silver 15-min added. Polymarket Intl still lists **5-min** crypto. FanDuel Q2: sports/novelties on **Predicts** move to **Crypto.com**; CME kept for financials; **~$50M** MM revenue expected 2026 ($6M in Q2 per the brief). Retail: these products behave like **short-dated sports/casino risk**, not long-dated political markets. Pair with K135: 5-min asset binaries stay **NO-GO**; 15-min clears the worst settlement-push signature but is still high-churn. [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-06-15min-prediction-markets.md]

### K226 — ForecastEx volume meta-contract + Yankees [CONFIRMED]

ForecastEx CFTC **40.2** self-cert for a **Prediction Market Annual Volume Forecast** (aggregate notional across CFTC-regulated PM DCMs). Not yet listed as of 2026-08-06 night. MNPI / source-agency / outcome-decisionmaker restrictions. Polymarket × **NY Yankees** stadium partnership = brand distribution, not a pricing edge. [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-07-forecastEx-volume.md]

### K231 — FlightAware v. Kalshi [CONFIRMED]

SDNY suit (breach + trademark + more): Jul 14 Kalshi employee opened a free AeroAPI account; Kalshi 40.2 named FlightAware **Primary Source Agency** for flight-cancellation settlement; Jul 15 FlightAware cancelled + C&D; Jul 17 Kalshi claimed nominative fair use. FlightAware seeks a block + damages; argues reputational + safety risk (incentivizing cancellations). Kalshi’s own filing named **DOT BTS On-Time Reporting** as an alternate source — markets do not *need* FlightAware. Same issue: CT Judge Vernon D. Oliver rejected Kalshi’s major CEA-preemption / swaps arguments on sports; EH counts **eight states** with authority to ban/restrict; CFTC IAC inaugural **2026-08-20**; Kalshi × Nasdaq Market Surveillance; affiliated-MM conflict rules. Volume color that Sunday: Kalshi **$1.07B**, sports+parlays **79.2%**. Retail: flight-delay series can delist or change oracle overnight; not a sports-betting signal. [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-11-flightaware-kalshi.md]

## Snippets

> If New York accounted for a share of Kalshi’s activity roughly proportional to its 6% share of the US population… A 6% tax would generate approximately $7 million annually — or about $35 million over five years… [Source: Event Horizon 2026-08-04 via OSINT]

> Seven of the top 10 crypto markets are 15-minute markets. [Source: Event Horizon 2026-08-06, citing Ticker Tracker]

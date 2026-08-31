---
title: Daily digest RSS NFL week-0 batch (2026-08-31)
type: source
tags: [source, web, daily-digest, rss, nfl, kalshi, polymarket]
keywords: [injury-markets, ninth-circuit, player-participation, nfl-partners, tickertracker]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-31-daily.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sources/daily-digest-batch-k168-2026-08-31.md
  - sources/brief-k168-nfl-season-paper-rss-2026-08-31.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/sports/nfl-betting.md
  - concepts/kalshi-michigan-sports-injunction-2026-06.md
  - concepts/prediction-markets-crossover.md
  - concepts/pickem-legal-and-tos-posture.md
maturity: validated
read_status: read
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- @sweeps/2026-08-31-daily.md — RSS rows S1–S11 (football-relevant)
- @entities/platforms/kalshi.md — football volume + injury listings + 9th Circuit
- @entities/platforms/polymarket.md — player-participation filings pulled
- @entities/sports/nfl-betting.md — Week-1 availability markets vs sportsbook props
- @concepts/kalshi-michigan-sports-injunction-2026-06.md — 9th Circuit follow-on
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-25-athlete-play-markets.md — injury-market source of record
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-26-kalshi-football-season-data.md — TickerTracker volume
- @osint-wiki/sources/substack-rss-event-horizon-2026-08-28-ninth-circuit-kalshi-sports.md — 9th Circuit source of record
- @sources/brief-k168-nfl-season-paper-rss-2026-08-31.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-08-31 |
| **Method** | Event Horizon via OSINT bodies; LSR titles + Brave/ESPN corroboration (LSR HTTP 403 from this laptop) |
| **Confidence** | [CONFIRMED] EH via OSINT; [TENTATIVE] LSR titles |

## Narrative

Local RSS digest (14 feeds, 7-day window). **RotoViz feed HTTP 403.** Skipped: pick-mill LSB (S12–S15), Brazil SBC, RotoBaller sleeper lists, Sharp ranking/projection trackers (churn), nflverse GitHub tags (awareness-only per cadence).

### S1 / OSINT K247 — athlete play markets [CONFIRMED]

Kalshi lists Week-1 NFL **player availability** (“will play”), not explicit injury diagnosis. CFTC proposed rules flag injury-settled contracts as contrary to public interest. Leagues press venues to drop injury-adjacent listings. **Do not** treat as a K147 pick'em substitute. Source of record: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-25-athlete-play-markets.md`. Sweep title “Are Will Players Compete markets in trouble?” is the same cluster (EH 2026-08-31 follow-on).

### S5 / OSINT K247 — Kalshi football volume [CONFIRMED]

TickerTracker kickoff-relative comps: Kalshi daily volume ~$25M (Aug 2025) → **>$1B** a weekday now. Football preseason **30×** YoY but only **1.1%** of platform incremental growth — parlays and crypto dominate. Hall of Fame Game $21.2M vs <$500k prior year. >80% of 2026 incremental volume from markets that did not exist a year ago (parlays first). Parlay **notional exaggerates money-at-risk**. No pm scp. Source of record: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-26-kalshi-football-season-data.md`.

### S2 / OSINT K249 — Ninth Circuit [CONFIRMED]

Ninth Circuit 3-0: Kalshi sports event contracts are **likely not CEA swaps**. Injunction that let Kalshi keep sports in Nevada dissolved. Circuit split vs Third Circuit (NJ). Opens state enforcement in CA/NV and the western circuit. Geofencing is Kalshi’s problem first. **Hard Rock remains the W8 book.** Source of record: `@osint-wiki/sources/substack-rss-event-horizon-2026-08-28-ninth-circuit-kalshi-sports.md`.

### S4 / S9 — Connecticut sues Kalshi [TENTATIVE — title]

EH + LSR titles: CT AG frames Kalshi sports as illegal unlicensed sports betting. Same preemption class as MI/NY/UT. Do not invent complaint figures from titles.

### S7 — Polymarket pulls NFL participation filings [CONFIRMED via ESPN/Brave; LSR 403]

Polymarket US self-certified NFL **player participation** (incl. Mahomes Week-1 “at least one play”) on **2026-08-25**, withdrew **2026-08-26** after CFTC asked operators to remove that class. NFL same week named DK / FanDuel / Fanatics as sports-betting partners and listed injury/officiating/knowable-in-advance wagers as objectionable. Starting-QB template filings may remain certified — do not assume the whole class is dead. [Source: https://www.espn.com/nfl/story/_/id/49756697/polymarket-withdraws-market-mahomes-return-injury (retrieved 2026-08-31)]

### S8 — DK / FanDuel NFL partners [TENTATIVE — title]

LSR: DraftKings and FanDuel return as NFL sports-betting partners (with Fanatics). Integrity language in the league release overlaps the participation-market pull. No promo math ingested.

## Snippets

> "Kalshi is now offering markets on whether players will play in Week 1 of the NFL season." [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-25-athlete-play-markets.md]

> "The substance of the sports event contracts offered on Kalshi's DCM is sports gambling, regardless of whether Kalshi calls them swaps." [Source: @osint-wiki/sources/substack-rss-event-horizon-2026-08-28-ninth-circuit-kalshi-sports.md]

> "A Polymarket source told ESPN on Friday that the Commodity Futures Trading Commission (CFTC) asked Polymarket and other prediction market operators to remove contracts such as Mahomes to play in Week 1." [Source: https://www.espn.com/nfl/story/_/id/49756697/polymarket-withdraws-market-mahomes-return-injury (retrieved 2026-08-31)]

## Dead Ends

- **LSR S7–S11 full text** — Cloudflare 403 from this laptop (same as 08-14).
- **RotoViz RSS** — HTTP 403 this run.
- **Sharp S19–S23 ranking/projection URLs** — evergreen trackers; do not snapshot ADP as wiki facts.
- **RotoBaller S24–S27** — sleeper mills; skip.
- **nflverse S28–S30** — tag bumps; awareness only.

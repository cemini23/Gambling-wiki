---
title: Kalshi Michigan sports-contract injunction (2026-06)
type: concept
tags: [concept, kalshi, regulation, sports-betting, geofencing, retail]
keywords: [michigan, kalshi, TRO, sports-event-contracts, gaming-control-board, geolocation]
related:
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - concepts/sharp-vs-soft-books.md
  - sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
  - osint-wiki/sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sources/brief-k222-k231-pm-retail-awareness-2026-08.md
  - sources/brief-k239-kalshi-sports-mention-2026-08-15.md
  - sources/brief-k240-kalshi-nv-geofence-2026-08-17.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: validated
created: 2026-07-05
updated: 2026-08-31
---

## Relations

- @entities/platforms/kalshi.md — entity hub
- @concepts/prediction-markets-crossover.md — state-law vs CFTC framing
- @sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md — primary report
- @osint-wiki/sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md — OSINT provenance
- @sources/daily-digest-rss-industry-2026-08-14.md — NY CFTC emergency follow-on (Aug 2026)
- @sources/brief-k222-k231-pm-retail-awareness-2026-08.md — Utah SJ (no CEA preemption) + CT Oliver ruling
- @sources/brief-k240-kalshi-nv-geofence-2026-08-17.md — NV $120k/day same geolocation-fine class + optional-update geofence
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — Ninth Circuit: sports contracts likely not swaps
- @sources/brief-k239-kalshi-sports-mention-2026-08-15.md — WA final order + mentions-gone pair

## Raw Concept

2026-06-29: Michigan circuit court **temporary restraining order** bars Kalshi from offering **sports event contracts** in Michigan without a sports-betting license; mandates **MGCB-grade geolocation** with **$120k/day** fine for non-compliance. AG suit filed March 2026 under Michigan Lawful Sports Betting Act (LSBA).

## Narrative

### Order summary [CONFIRMED — court order via Event Horizon report]

- **Scope** — No sports wagering activity in Michigan without license; officers/agents/affiliates enjoined
- **Geofencing** — Must use third-party geolocation provider licensed by Michigan Gaming Control Board (or court-approved equivalent meeting Technical Bulletin 2024-03)
- **Penalty** — $120,000 per day of geolocation non-compliance
- **Duration** — 14-day TRO (through ~2026-07-13 per source); Kalshi may seek emergency appeal

### Legal framing

Michigan AG (Dana Nessel): Kalshi’s sports contracts are **online sports wagers** under state law, not exempt federal event contracts for Michigan residents. Fits broader **state gaming board vs CFTC DCM** conflict documented in WSJ retail synthesis (`@sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md`).

### Retail implications

| Topic | Takeaway |
|-------|----------|
| **Access** | Michigan residents may face blocks, forced geolocation upgrades, or market delistings on sports series |
| **Open positions** | Monitor Kalshi comms on void/settlement if contracts become unavailable mid-life |
| **Tax / license** | State treats product as wagering — conflicts with Kalshi “not the house” / commodity marketing |
| **Precedent** | Template for other states with LSBA-style statutes; NCPG/MGCB membership friction (see EH roundup Jul 3) |

**NY follow-on (Aug 2026):** CFTC used emergency authority again, telling Kalshi to keep operating in New York against an AG suit seeking up to $36B. Same preemption class — not a Michigan-only one-off. `@sources/daily-digest-rss-industry-2026-08-14.md`.

**Utah SJ (Aug 2026):** Judge Shelby — CEA does **not** preempt Utah’s anti-gambling statute against Kalshi sports contracts. CT Judge Vernon D. Oliver separately rejected Kalshi’s major preemption / swaps arguments. Event Horizon counts **eight states** with authority to ban or restrict. `@sources/brief-k222-k231-pm-retail-awareness-2026-08.md`.

**Nevada follow-on (Aug 2026):** NGCB filing — Kalshi missed the Aug 12 NV deadline and faces the **same $120k/day geolocation-fine class**. InGame notes the MI geofence (like NV) only fully works after an **optional** app update — geofence is residency-spoof / optional-update fragile, not hard venue-down. `@sources/brief-k240-kalshi-nv-geofence-2026-08-17.md`.

**Ninth Circuit (2026-08-28, K168) [CONFIRMED]:** panel 3-0 — Kalshi sports contracts are **likely not CEA swaps**. NV injunction dissolved; circuit split vs Third Circuit (NJ). CT AG also sued (title-only). Hard Rock remains the W8 book. `@sources/daily-digest-rss-nfl-week0-2026-08-31.md`.

### Cross-wiki

- **Regulatory / CFTC preemption** detail: `@osint-wiki/entities/platforms/kalshi.md`
- **Retail strategy** (fees, FLB, limits): stay on this wiki

## Snippets

> “Corporations cannot circumvent state gaming laws… betting in our state remains lawful, fair and subject to the oversight our residents expect.” — Michigan AG Dana Nessel, March 2026 press release [Source: Event Horizon 2026-06-29]

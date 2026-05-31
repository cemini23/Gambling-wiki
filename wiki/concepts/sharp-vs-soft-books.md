---
title: Sharp vs soft sportsbooks
type: concept
tags: [concept, sportsbooks, sharp, soft, limits]
keywords: [sharp-book, soft-book, pinnacle, limits, account-restriction]
related:
  - concepts/line-shopping-and-clv.md
  - concepts/vig-and-hold.md
  - concepts/sports-betting-fundamentals.md
  - entities/platforms/pinnacle.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - concepts/prediction-markets-crossover.md
  - concepts/world-cup-books-vs-pm-divergence.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/sports/nfl-betting.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/platforms/pinnacle.md — canonical sharp reference (where accessible)
- @entities/platforms/draftkings.md — US soft/rec retail
- @entities/platforms/fanduel.md — US soft/rec retail

## Raw Concept

Sharp books offer efficient lines and low hold but limit winners; soft books offer promos and higher limits for recreational bettors but worse closing lines.

## Narrative

### Sharp books

- **Lower hold**, lines move quickly on sharp money
- **Lower limits** for known winners; account limits common
- Used as **CLV benchmark**, not always as primary execution venue
- Example: Pinnacle (offshore sharp) — `@entities/platforms/pinnacle.md`

### Soft books

- **Higher hold**, more promos, slower line moves
- Better for **bonus +EV** and recreational volume until limited
- US legal: DraftKings, FanDuel, BetMGM, Caesars, etc.

### Sharp vs soft arbitrage [TENTATIVE]

Classic pattern: sharp line (Pinnacle) moves; soft book lag → short-window arb or middle. `@osint-wiki/sources/gemini-github-sports-betting-repos-landscape-2026-05-30.md` catalogs open-source **alert-only** arb finders; autonomous arb has latency and ToS risk.

### Prediction market analog

Kalshi (regulated DCM) vs Polymarket (CLOB) — efficiency gradient similar to sharp/soft; see `@concepts/prediction-markets-crossover.md` and `@concepts/sportsbook-pm-line-divergence.md`.

## Snippets

> Pinnacle as sharp reference, Bwin/PMU as soft execution targets — open-source finders implement alert-only latency arb, not autonomous execution. [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md]

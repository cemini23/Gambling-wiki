---
title: Sports betting fundamentals
type: concept
tags: [concept, sports-betting, spreads, moneylines, totals]
keywords: [spread, moneyline, total, props, american-odds, decimal-odds]
related:
  - concepts/vig-and-hold.md
  - concepts/bankroll-management.md
  - concepts/line-shopping-and-clv.md
  - concepts/live-betting-match-integrity.md
  - concepts/sharp-vs-soft-books.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/kelly-criterion-betting.md
  - concepts/favorite-longshot-bias.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
  - concepts/world-cup-knockout-phase-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/platforms/hard-rock-bet.md
  - concepts/sportsbook-pm-line-divergence.md
  - sources/kelly-1956-information-rate.md
  - entities/tools/sports-betting-georgedouzas.md
  - entities/tools/fredbet.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - concepts/live-betting-match-integrity.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-news-r1-r12-2026-06-02.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - entities/tools/unabated.md
  - entities/tools/odds-jam.md
  - entities/tools/pickfinder.md
  - entities/people/rufus-peabody.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - concepts/pm-live-belief-updating.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
maturity: validated
created: 2026-05-31
updated: 2026-06-09
---

## Relations

- @concepts/line-shopping-and-clv.md — edge measurement
- @concepts/sharp-vs-soft-books.md — where to bet
- @entities/platforms/draftkings.md — major US book
- @entities/platforms/fanduel.md — major US book
- @entities/platforms/hard-rock-bet.md — operator primary NFL book (W8)

## Raw Concept

Orientation page for mainstream US sports betting market types and odds formats.

## Narrative

### Market types

| Type | Question answered | Example |
|------|-------------------|---------|
| **Spread (handicap)** | Margin of victory | Chiefs -3.5 vs Bills |
| **Moneyline** | Straight win | Chiefs -150 / Bills +130 |
| **Total (over/under)** | Combined score | O/U 47.5 |
| **Props** | Player/team stat | Mahomes over 275.5 passing yards |
| **Futures** | Season/tournament | Super Bowl winner |
| **Live (in-play)** | Lines during game | Next score, live spread |

**PM live note:** Kalshi NBA research shows in-play **event-contract mids react directionally** to game state but **underreact in magnitude** (~0.64× fair move on 1-min horizon) — `@concepts/pm-live-belief-updating.md`. Traditional book live behavior is venue-specific; don't assume identical β.

### Odds formats

- **American**: -110 favorite, +150 underdog
- **Decimal**: 1.91 = -110 equivalent
- **Implied probability**: from American negative `|odds|/(|odds|+100)`; positive `100/(odds+100)`

### Key disciplines

1. Bet **+EV lines**, not teams
2. Track **CLV** (closing line value) as skill proxy
3. Understand **push** rules (PK, half-points)
4. Know **void** rules (pitcher changes, postponements)

### Research workflow (operator YouTube batch)

| Step | Practice | Sources |
|------|----------|---------|
| 1 | **Specialize** — one sport/market type (spreads vs props) | youngkardi, Unabated |
| 2 | **Filter slate** — line movement on ML/spread/total | LINEMAKER |
| 3 | **Game checklist** — offense/defense/ST, key spread numbers | wtE5aXrUHzQ |
| 4 | **Stats stack** — ATS logs, props (Action, StatMuse), DFS DvP | Goon, Calling Our Shot |
| 5 | **Price check** — compare to **Pinnacle/sharp**; log **CLV** | Unabated, OddsJam, Extranet Shaquille |
| 6 | **Size** — fractional **Kelly** on verified edge | Unabated, OddsJam |

Tools: `@entities/tools/unabated.md`, `@entities/tools/odds-jam.md`, `@entities/tools/pickfinder.md` — Phase-0 each before subscribe.

### Overlap with prediction markets

Some sporting outcomes trade on Kalshi/Polymarket as event contracts — see `@concepts/prediction-markets-crossover.md` for when to use books vs PM venues.

## Snippets

> "Good sports betting is pricing knowledge." [Source: XZvXWVztJoY via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

> "Sports betting isn't about picking winners … finding the small edges." [Source: EQt2sq0_s64 via @sources/youtube-operator-batch-sports-betting-research-2026-05-31.md]

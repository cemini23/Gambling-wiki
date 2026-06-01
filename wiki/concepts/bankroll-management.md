---
title: Bankroll management
type: concept
tags: [concept, bankroll, risk-management, discipline]
keywords: [bankroll, unit-sizing, stop-loss, session-limits, responsible-gambling]
related:
  - concepts/kelly-criterion-betting.md
  - concepts/vig-and-hold.md
  - concepts/gambling-wiki-scope.md
  - concepts/sports-betting-fundamentals.md
  - concepts/dfs-strategy-overview.md
  - concepts/best-ball-strategy.md
  - concepts/poker-strategy-overview.md
  - concepts/casino-game-house-edge.md
  - concepts/parlay-and-correlated-bets.md
  - entities/tools/odds-jam.md
  - concepts/pm-copy-trading-retail-risks.md
  - sources/kelly-1956-information-rate.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - entities/tools/unabated.md
  - entities/platforms/underdog-fantasy.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md
  - entities/games/blackjack.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/kelly-criterion-betting.md — optimal growth sizing; bankroll caps Kelly in practice
- @concepts/vig-and-hold.md — vig determines minimum edge to overcome
- @concepts/sports-betting-fundamentals.md — unit betting in sports context
- @concepts/dfs-strategy-overview.md — DFS bankroll as % of GPP entries
- @concepts/poker-strategy-overview.md — poker-specific buy-in rules (20–40 BI)
- @concepts/casino-game-house-edge.md — session bankroll vs house edge

## Raw Concept

Foundational discipline page: how to partition capital, size bets/units, and survive variance across sports betting, casino, poker, and DFS.

## Narrative

### Separate bankrolls

Keep **distinct pools** for unrelated verticals (sports vs poker vs casino vs DFS). Mixing pools hides true ROI and encourages cross-subsidizing -EV play.

| Vertical | Typical rule of thumb | Notes |
|----------|----------------------|-------|
| Sports betting | 1–3% of bankroll per bet ("unit") | Scale down during losing streaks or model uncertainty |
| Poker (cash) | 20–40 buy-ins for stake level | Move down at 20 BI; move up at 40+ BI [TENTATIVE — standard poker literature] |
| Poker (MTT) | **100+ buy-ins** for stake | $100 → $1 MTTs; move to $2 at $200; step down at $100; don't move up on one score [Source: yrGExOmDRLk] |
| Casino (table games) | Session bankroll = acceptable loss | Never chase; pre-set stop-win/stop-loss |
| DFS (GPP) | 10–20% of weekly DFS bankroll per slate | Correlation across entries still counts as one slate exposure |

### Units vs dollars

Express edge bets in **units** (1u = 1% of current bankroll or fixed fraction). Recompute bankroll after each settled period (daily/weekly). Avoid "double up to recover" — martingale is `[RETRACTED]` for +EV play.

### Record-keeping

Track: date, sport/market, line, odds, stake, result, closing line (for CLV). Without logs, perceived skill dominates actual ROI.

### Responsible gambling guardrails

- Wager only where legal for your jurisdiction
- Pre-commit loss limits; use sportsbook deposit limits when available
- Treat marketing bonuses as **+EV only after full TOS math** — `@entities/tools/odds-jam.md` + `@concepts/pm-copy-trading-retail-risks.md`
- **Poker MTT:** chasing stakes above BRM for a "quick score" is **gambling**, not grind [Source: yrGExOmDRLk]

## Snippets

> "You have $100, you play $1 tournaments, period." [Source: yrGExOmDRLk via @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]

> "Do not move up if you have one big score. Ignore it. You likely got lucky." [Source: yrGExOmDRLk via @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]

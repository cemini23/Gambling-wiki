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
| Poker (MTT) | 100+ buy-ins for stake | Higher variance than cash |
| Casino (table games) | Session bankroll = acceptable loss | Never chase; pre-set stop-win/stop-loss |
| DFS (GPP) | 10–20% of weekly DFS bankroll per slate | Correlation across entries still counts as one slate exposure |

### Units vs dollars

Express edge bets in **units** (1u = 1% of current bankroll or fixed fraction). Recompute bankroll after each settled period (daily/weekly). Avoid "double up to recover" — martingale is `[RETRACTED]` for +EV play.

### Record-keeping

Track: date, sport/market, line, odds, stake, result, closing line (for CLV). Without logs, perceived skill dominates actual ROI.

### Responsible gambling guardrails

- Wager only where legal for your jurisdiction
- Pre-commit loss limits; use sportsbook deposit limits when available
- Treat marketing bonuses as **+EV only after full TOS math** — see `@entities/tools/odds-jam.md` experiment notes in `@osint-wiki`

## Snippets

*(populate from ingested bankroll-management sources)*

---
title: Bankroll management
type: concept
tags: [concept, bankroll, risk-management, discipline]
keywords: [bankroll, unit-sizing, stop-loss, session-limits, responsible-gambling]
related:
  - concepts/best-ball-strategy.md
  - concepts/casino-game-house-edge.md
  - concepts/dfs-strategy-overview.md
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - concepts/kelly-criterion-betting.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/poker-strategy-overview.md
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - entities/games/blackjack.md
  - entities/platforms/underdog-fantasy.md
  - entities/tools/odds-jam.md
  - entities/tools/unabated.md
  - sources/kelly-1956-information-rate.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - sources/youtube-operator-batch-sports-betting-research-2026-05-31.md
  - sources/youtube-operator-batch-wc-bbm-2026-05-31.md
  - sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md
  - entities/bots/wagerbrain.md
  - concepts/world-cup-pm-retail-hygiene.md
  - sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md
maturity: validated
created: 2026-05-31
updated: 2026-06-09
---

## Relations

- @concepts/gambling-bot-architecture.md — fleet bankroll caps
- @concepts/kelly-criterion-betting.md — optimal growth sizing; bankroll caps Kelly in practice
- @concepts/vig-and-hold.md — vig determines minimum edge to overcome
- @concepts/sports-betting-fundamentals.md — unit betting in sports context
- @concepts/dfs-strategy-overview.md — DFS bankroll as % of GPP entries
- @concepts/poker-strategy-overview.md — poker-specific buy-in rules (20–40 BI)
- @concepts/casino-game-house-edge.md — session bankroll vs house edge
- @entities/bots/wagerbrain.md — K92 steal-from math reference (MIT, stale repo)

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

### WagerBrain reference map (K92 steal-from — not a dependency)

`sedemmler/WagerBrain` (MIT, stale 2020) — use as **requirements vocabulary** for gambling-bot sizing modules; re-implement in fleet code, do not `pip install` unmaintained package.

| WagerBrain module | Fleet use |
|-------------------|-----------|
| `odds.py` | American / decimal / fractional conversion |
| `probs.py` | Implied probability ↔ odds |
| `payouts.py` | Profit, parlay payout, EV |
| `bankroll.py` | Kelly criterion, unit sizing caps |
| Phase 2 | Vig, arb detection — spec only until sportsbook API lane is licensed |

## Snippets

> "You have $100, you play $1 tournaments, period." [Source: yrGExOmDRLk via @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]

> "Do not move up if you have one big score. Ignore it. You likely got lucky." [Source: yrGExOmDRLk via @sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md]

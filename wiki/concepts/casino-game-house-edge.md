---
title: Casino game house edge
type: concept
tags: [concept, casino, house-edge, blackjack, craps, roulette]
keywords: [house-edge, rtp, basic-strategy, craps, blackjack, slots]
related:
  - concepts/bankroll-management.md
  - concepts/poker-strategy-overview.md
  - entities/games/blackjack.md
  - entities/games/roulette.md
  - entities/games/poker.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/games/blackjack.md — lowest edge with basic strategy
- @entities/games/roulette.md — fixed edge games
- @concepts/poker-strategy-overview.md — poker is PvP + rake, not house-banked

## Raw Concept

House edge by game type; basic strategy and comp math for casino visits.

## Narrative

### Approximate house edge (standard rules) [TENTATIVE — verify table rules]

| Game | Typical edge | Notes |
|------|-------------|-------|
| Blackjack (basic strategy) | 0.5–1% | Rule-dependent (6:5 vs 3:2 BJ kills edge) |
| Craps (pass/don't pass) | ~1.4% / ~1.4% | Odds bets often 0% edge |
| Baccarat (banker) | ~1.06% | Commission on banker |
| Roulette (American 00) | ~5.26% | European single-zero ~2.7% |
| Slots | 2–15%+ | PAR sheet dependent |

### Implications

- **No Kelly edge** on -EV games — entertainment budget only
- **Basic strategy** is mandatory for blackjack before any "system"
- **Comps** can offset edge slightly — requires rated play and accurate EV math

### Martingale and "systems"

Progressive betting systems do not change house edge; they increase **risk of ruin**. Mark as Dead End / `[RETRACTED]` in ingests.

## Snippets

*(populate from ingested casino math sources)*

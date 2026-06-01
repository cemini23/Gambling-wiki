---
title: Casino game house edge
type: concept
tags: [concept, casino, house-edge, blackjack, craps, roulette, baccarat, slots]
keywords: [house-edge, rtp, basic-strategy, craps, blackjack, slots, video-poker, martingale]
related:
  - concepts/bankroll-management.md
  - concepts/poker-strategy-overview.md
  - entities/games/blackjack.md
  - entities/games/roulette.md
  - entities/games/poker.md
  - sources/youtube-operator-batch-casino-2026-05-31.md
  - entities/bots/stake-engine-client.md
maturity: validated
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @entities/games/blackjack.md — lowest edge with basic strategy
- @entities/games/roulette.md — fixed edge games
- @concepts/poker-strategy-overview.md — poker is PvP + rake, not house-banked
- @sources/youtube-operator-batch-casino-2026-05-31.md — American Casino Guide ranking

## Raw Concept

House edge by game type; basic strategy and comp math for casino visits. **No Kelly edge** on -EV games without skill angle (blackjack counting, full-pay VP).

## Narrative

### Approximate house edge (standard rules) [TENTATIVE — verify table rules]

| Game | Typical edge | Notes |
|------|-------------|-------|
| Blackjack (basic strategy) | **0.5–1%** | 6:5 BJ destroys edge; see `@entities/games/blackjack.md` |
| Craps (pass/don't pass) | ~1.4% | **Odds bets** often 0% edge — take max odds when playing pass line |
| Baccarat (banker) | ~1.06% | Commission on banker; cited as low-skill "smart bet" [Source: oupvsCHsjHs] |
| Video poker (full pay) | ~0.5% or better | **Paytable-dependent** — 9/6 Jacks+ ~99.5% RTP; one pay step can drop to ~85% |
| Roulette (American 00) | ~5.26% | European single-zero ~2.7% |
| Slots | 2–15%+ | PAR sheet dependent; no beatable "picker" without insider data `[RETRACTED]` |

### Smartest bets ranking (American Casino Guide) [TENTATIVE]

Low-skill + low-edge hierarchy from `oupvsCHsjHs`:

1. **Baccarat** (banker) — simple, low edge
2. **Craps** — pass/don't pass + odds
3. **Full-pay video poker** — if you play perfect strategy and verify paytable
4. **Blackjack** — only with basic strategy memorized

### Implications

- Treat casino visits as **-EV entertainment** unless documented skill edge (BJ counting, VP paytables)
- **Comps** can offset edge slightly — requires rated play and accurate EV math
- Separate bankroll from sports betting / DFS (`@concepts/bankroll-management.md`)

### Martingale and "systems" `[RETRACTED]`

Progressive betting (Martingale, 31, Fibonacci) **does not change** house edge; increases **risk of ruin** [Source: RxEuPiI8fXI]. Slot "machine picker" content same category [Source: JK5-yun_7mo, vpmdkT1q5oo].

### Online environment risks

Bot/collusion exposure on some online poker rooms — not a strategy edge; see `@concepts/poker-strategy-overview.md` Dead Ends.

## Snippets

> "While the average blackjack player will be playing with a 1 to 2% disadvantage, the perfect basic strategy player will be playing with about half of 1% disadvantage." [Source: HeVclniKpHs via @sources/youtube-operator-batch-casino-2026-05-31.md]

> Video poker paytable example: small flush/full-house pay changes can drop payback from ~96% toward ~85% [TENTATIVE — oupvsCHsjHs example]. [Source: oupvsCHsjHs via @sources/youtube-operator-batch-casino-2026-05-31.md]

## Dead Ends

- Martingale / progressive systems — `[RETRACTED]`
- Slot machine selection without PAR sheet — `[RETRACTED]`
- "Easiest $100" casino promos (Shorts) — marketing, not +EV

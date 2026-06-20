---
title: Hard Rock Bet
type: entity
tags: [entity, platform, sportsbook, casino, us-legal, nfl]
keywords: [hard-rock-bet, hard-rock-sportsbook, nfl, sportsbook, casino, florida]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - concepts/casino-game-house-edge.md
  - entities/sports/nfl-betting.md
  - entities/platforms/fanduel.md
  - entities/platforms/draftkings.md
  - entities/platforms/underdog-fantasy.md
  - concepts/bankroll-management.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/sports/nfl-betting.md — primary NFL sportsbook lane (W8)
- @entities/platforms/fanduel.md — cross-shop CLV vs soft-book peer
- @concepts/line-shopping-and-clv.md — closing-line tracking on primary book
- @concepts/casino-game-house-edge.md — in-app casino product (parallel to NFL season)

## Raw Concept

Operator **primary US sportsbook** for NFL season — spreads, props, totals, futures, and in-app casino on the Hard Rock Bet mobile app. Stub pending Phase-0 audit (W8).

## Narrative

### Operator role (W8)

| Lane | Use |
|------|-----|
| **NFL sportsbook** | Main handle for spreads, player props, SGPs, live betting |
| **Casino** | Parallel -EV entertainment; separate bankroll from +EV sports |
| **Cross-shop** | Benchmark lines vs FanDuel/DraftKings; Pinnacle/Unabated for sharp reference |

### Phase-0 checklist [NEEDS VERIFICATION 2026-06-20]

- [ ] State/jurisdiction availability and account limits
- [ ] Hold/vig by market (NFL spread vs prop vs SGP)
- [ ] Promo/bonus rollover math — treat as -EV unless +EV after hold
- [ ] CLV workflow — log open vs close on primary markets
- [ ] Casino vs sports bankroll split per `@concepts/bankroll-management.md`

### Classification

Retail **soft book** profile (same class as DraftKings/FanDuel) until operator data proves otherwise. See `@concepts/sharp-vs-soft-books.md`.

## Snippets

*(pending Phase-0 ingest — TOS, limits, operator notes)*

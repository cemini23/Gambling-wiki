---
title: Parlays and correlated bets
type: concept
tags: [concept, parlay, correlation, same-game-parlay, nfl]
keywords: [parlay, sgp, correlation, lottery, hold, sgp-max]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - concepts/favorite-longshot-bias.md
  - concepts/bankroll-management.md
  - concepts/kelly-criterion-betting.md
  - concepts/dfs-strategy-overview.md
  - entities/sports/nfl-betting.md
  - entities/platforms/hard-rock-bet.md
  - sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md
  - sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md
maturity: validated
created: 2026-05-31
updated: 2026-06-20
---

## Relations

- @concepts/favorite-longshot-bias.md — parlays amplify longshot bias
- @concepts/vig-and-hold.md — parlay hold compounds
- @entities/platforms/hard-rock-bet.md — SGP Max / Flex Parlay product (W8)
- @entities/sports/nfl-betting.md — NFL SGP discipline

## Raw Concept

How parlays compound vig and correlation; when SGPs can be +EV vs lottery tickets.

## Narrative

### Standard parlay math

Independent legs multiply implied probabilities — and **vig compounds**. A 3-leg -110 parlay pays ~6:1 but true fair odds are worse after compounded hold. Default retail parlays are **-EV** unless legs are independently +EV.

> "Each added leg increases the sportsbook's hold, so parlays are a high-variance, low-expected-value play rather than a core strategy." [Source: @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md]

**W8 rule:** parlays are entertainment or promo-conversion vehicles — not core NFL +EV process on Hard Rock.

### Same-game parlays (SGP)

Correlated outcomes (QB yards + team total + WR receptions) — books model correlation and often **embed extra margin**. Occasional +EV when correlation is mispriced [TENTATIVE — requires model].

| Platform | NFL SGP notes |
|----------|---------------|
| Hard Rock | SGP Max up to **20 legs**; Flex Parlay (custom legs-to-hit) — **compare implied prob vs DK/FD** before bet |
| General | Books may price correlation conservatively → effective tax on naive stacks |

Queue for deep-read: NFL SGP +EV vs tax guides (tier-2 sweep deferred — bettingonline.org timeout).

### Kelly warning

Treat parlay as **single bet** with combined `p` and `b`. Do not full-Kelly each leg separately.

### DFS overlap

DFS lineups are **correlated multi-leg portfolios** — different product but similar correlation thinking; see `@concepts/dfs-strategy-overview.md`. NFL game stacks in FanDuel GPPs are +EV-vs-field when projections support; SGPs are +EV-vs-book only with mispriced correlation.

## Snippets

> "Generally no. Each added leg increases the sportsbook's hold." [Source: @sources/web-tech-insider-nfl-betting-strategy-2026-06-20.md — parlay FAQ]

> "Hard Rock Bet lets you customize your parlay and select how many legs must hit for it to be a winner." [Source: @sources/web-sportsbookreview-hard-rock-bet-2026-06-20.md — Flex Parlay]

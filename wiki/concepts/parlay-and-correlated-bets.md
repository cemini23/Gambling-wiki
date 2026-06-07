---
title: Parlays and correlated bets
type: concept
tags: [concept, parlay, correlation, same-game-parlay]
keywords: [parlay, sgp, correlation, lottery, hold]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/vig-and-hold.md
  - concepts/favorite-longshot-bias.md
  - concepts/bankroll-management.md
  - concepts/kelly-criterion-betting.md
  - concepts/dfs-strategy-overview.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/favorite-longshot-bias.md — parlays amplify longshot bias
- @concepts/vig-and-hold.md — parlay hold compounds

## Raw Concept

How parlays compound vig and correlation; when SGPs can be +EV vs lottery tickets.

## Narrative

### Standard parlay math

Independent legs multiply implied probabilities — and **vig compounds**. A 3-leg -110 parlay pays ~6:1 but true fair odds are worse after compounded hold. Default retail parlays are **-EV** unless legs are independently +EV.

### Same-game parlays (SGP)

Correlated outcomes (QB yards + team total) — books model correlation and often **embed extra margin**. Occasional +EV when correlation is mispriced [TENTATIVE — requires model].

### Kelly warning

Treat parlay as **single bet** with combined `p` and `b`. Do not full-Kelly each leg separately.

### DFS overlap

DFS lineups are **correlated multi-leg portfolios** — different product but similar correlation thinking; see `@concepts/dfs-strategy-overview.md`.

## Snippets

*(populate from ingested sources)*

---
title: NFL betting
type: entity
tags: [entity, sport, nfl, football, sports-betting]
keywords: [nfl, football, spreads, props, totals, key-numbers]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/best-ball-strategy.md
  - concepts/dfs-strategy-overview.md
  - concepts/line-shopping-and-clv.md
  - concepts/sharp-vs-soft-books.md
  - entities/sports/nba-betting.md
  - entities/sports/world-cup-2026-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - entities/tools/pydfs-lineup-optimizer.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/best-ball-strategy.md — fantasy overlap (same player knowledge)
- @concepts/dfs-strategy-overview.md — DFS overlap
- @concepts/sports-betting-fundamentals.md — market types

## Raw Concept

NFL-specific betting and fantasy context — key numbers, season structure, market types.

## Narrative

### Key numbers (spread)

3 and 7 dominate NFL margins (field goal + touchdown). Lines landing on/off these numbers affect push and middle value. Half-points (-3.5 vs -3) materially change EV on close spreads.

### Market menu

| Market | Notes |
|--------|-------|
| Spread / ML / total | Highest liquidity; best for CLV tracking |
| Player props | Higher hold; more FLB on longshot yards/TD props |
| Futures | Division, SB winner — capital tied for months |
| Live | Wide spreads during drives; sharp limits lower |

### Season rhythm

- **Preseason** — unreliable lines, low limits
- **Regular season** — Sun/Mon/Thu slates; injury report Wed/Fri moves
- **Playoffs** — tighter lines, public handle on favorites

### Overlap with DFS / best ball

Same injury and game-environment research informs `@concepts/dfs-strategy-overview.md` stacks and `@concepts/best-ball-strategy.md` ADP. Betting is against the **line**; DFS is against the **field**.

### Open-source ML note

Gemini landscape cites `kyleskom/NBA-Machine-Learning-Sports-Betting` as analog class — NFL models require separate validation; see `@sources/gemini-github-sports-betting-landscape-2026-05-30.md`.

## Snippets

*(expand from operator YouTube / primer ingests)*

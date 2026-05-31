---
title: NBA betting
type: entity
tags: [entity, sport, nba, basketball, sports-betting]
keywords: [nba, basketball, spreads, props, totals, load-management]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/dfs-strategy-overview.md
  - concepts/line-shopping-and-clv.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/sports/nfl-betting.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/tools/momentum-odds.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/youtube-sports-pm-retail-batch-2026-05-29.md
  - entities/tools/pydfs-lineup-optimizer.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/dfs-strategy-overview.md — NBA DFS slates
- @entities/tools/momentum-odds.md — tutorial mapped signals to Kalshi **NBA/playoff** contracts
- @concepts/sportsbook-pm-line-divergence.md — totals/ML vs PM

## Raw Concept

NBA-specific betting — pace, rest, load management, prop volume.

## Narrative

### Structural traits

- **High game frequency** — 82-game season + playoffs; larger sample for CLV
- **Rest / B2B** — lines move on late scratch news; injury report timing matters
- **Pace and totals** — faster pace → total correlation across same-game parlays
- **Player props** — minutes-sensitive; starters sit in blowouts

### PM / Kalshi overlap

MomentumOdds YouTube demo explicitly routes **NBA playoff**-style Kalshi contracts from sportsbook correlation signals — see `@entities/tools/momentum-odds.md`. Always verify contract spec (regulation vs OT).

### DFS overlap

NBA DFS (DraftKings/FanDuel) shares projection work with spread/total betting but different rake structure — `@concepts/dfs-strategy-overview.md`.

### Data / OSS

Gemini landscape: `bttmly/nba` schema-driven client, NBA ML betting repos — reference for model builds, not turnkey edge [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md].

## Snippets

*(expand from operator YouTube ingests)*

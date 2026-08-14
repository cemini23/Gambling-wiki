---
title: Player usage models (NFL DFS)
type: concept
tags: [concept, dfs, nfl, usage, target-share, carry-share, w-usage]
keywords: [wopr, adot, snap-share, rz-share, beta-binomial, vacated-targets]
related:
  - concepts/team-volume-pace-model.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/dfs-injury-and-news-workflow.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - sources/sharp-nfl-rb-prop-unders-2026-08-13.md
  - sources/rotoviz-preseason-paywall-2026-08-14.md
maturity: draft
created: 2026-06-20
updated: 2026-08-14
---

## Relations

- @concepts/team-volume-pace-model.md — team volume denominator
- @concepts/dfs-injury-and-news-workflow.md — injury reallocation
- @sources/sharp-nfl-rb-prop-unders-2026-08-13.md — season-long rush unders as carry-share bets
- @sources/rotoviz-preseason-paywall-2026-08-14.md — OL continuity / target-share titles (paywalled)

## Raw Concept

Allocate team volume to players via **usage shares**: snap%, target share, carry share, RZ/GL share — with regression and injury redistribution.

## Narrative

### WR/TE targets (usage-targets)

Pipeline: **routes → TPRR → target share**, not raw last-game targets.

- **WOPR** = `1.5 × target_share + 0.7 × air_yards_share` (Hermsmeyer)
- Weighting: 50% L3 / 30% season / 20% prior; aDOT shrinks harder (30/40/30)
- Shrinkage: `k_tprr ≈ 80 routes`, `k_adot ≈ 30 targets`

**Teammate OUT redistribution:** role-adjacent 40% + route-family 30% + existing earners 20% + 10% unassigned; cap single player at 50% vacated targets first game.

### RB rushing (usage-rushing)

Separate **carry share** (floor) from **inside-5 / GL share** (rush TD equity). Use yardline-bucket xTD (5–1 bucket ~40% TD rate) not raw TD rate.

Committee detection via HHI on carry shares; confidence penalty on projections when HHI < 0.38.

**Season-long props (2026-08):** Taylor/Hubbard unders are the same carry-share bet at season horizon — fade a posted rushing total when the implied carry monopoly is implausible (committee, OL outages, trailing scripts). `@sources/sharp-nfl-rb-prop-unders-2026-08-13.md`.

### Snap / QB (usage-snaps-qb)

- **Snap%** = soft role gate (logistic), not direct production driver
- **QB attempts** = team dropbacks × (1 - sack - scramble); ignore QB snap%
- **Rookies:** Beta-Binomial shrinkage; volume updates faster than efficiency

### Canonical key

Join on **gsis_id** via nflverse `load_players()` + `load_ff_playerids()`; RapidFuzz fallback on (normalized_name, team, position).

## Snippets

> "Target share and air-yards share stabilize usefully after about three games." [Source: Hermsmeyer / NBC Sports air-yards article — retrieved 2026-06-20]

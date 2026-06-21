---
title: Implied team totals (DFS)
type: concept
tags: [concept, dfs, nfl, vegas, game-environment, w-implied]
keywords: [implied-team-total, spread, game-total, proe, game-environment-score]
related:
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/team-volume-pace-model.md
  - entities/sports/nfl-betting.md
  - concepts/nfl-dfs-data-sources.md
  - sources/research-diy-dfs-model-master-plan-2026-06-20.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/sports/nfl-betting.md — spread/total fundamentals
- @concepts/team-volume-pace-model.md — volume layer downstream
- @concepts/nfl-dfs-data-sources.md — Vegas via nflreadr or The Odds API

## Raw Concept

Convert **game total + spread** into per-team implied points and a slate **game environment score** for DFS stack selection.

## Narrative

### Exact formulas

Let `T` = game total, `S_team` = spread from team's perspective (favorite negative):

```text
ITT_team = (T / 2) - (S_team / 2)
ITT_opp  = T - ITT_team
```

Favorite form with `F = abs(favorite spread)`:

```text
ITT_favorite = (T + F) / 2
ITT_underdog = (T - F) / 2
```

### Empirical links [CONFIRMED — 4for4, ETR, FantasyLabs]

| Finding | Source |
|---------|--------|
| ITT correlates **0.33** with QB fantasy points (2018–2020 DK/FD) — stronger than raw total or spread alone | 4for4 QB playbook |
| WR ITT correlation weaker (~0.16) but **34%** of 25+ DK-point WRs when ITT >28 vs **11%** when ITT <21 | 4for4 WR playbook |
| Future pass rate driven by **game script + PROE**, not raw pass rate | ETR PROE article |
| Composite Vegas score >0.80 correlation with QB actual points | FantasyLabs |

### Game Environment Score (GES) proposal

Within-slate percentile score for stack ranking:

```text
GES_raw = 0.30*z(total) + 0.20*z(min ITT) + 0.15*z(max ITT)
        + 0.15*z(-|spread|) + 0.10*z(-avg_pace) + 0.10*z(avg_PROE)
```

Team Environment Score (TES) for single-team targeting:

```text
TES_raw = 0.45*z(ITT) + 0.20*z(team_PROE) + 0.15*z(-team_pace) + 0.20*z(-|spread|)
```

### Pipeline role

`ITT` is the **scoring backbone**; `spread` changes *how* points arrive (favorite → RB script; dog → pass volume). `PROE` is the pass/run tendency input. Pace changes opportunity count.

## Snippets

> "No single public number was more predictive for QB fantasy points than team implied total aside from full projections." [Source: 4for4 QB DFS playbook — https://www.4for4.com/2021/preseason/nfl-dfs-playbook-quarterback-strategy-guide (retrieved 2026-06-20)]

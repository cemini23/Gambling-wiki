---
title: Team volume and pace model (NFL DFS)
type: concept
tags: [concept, dfs, nfl, pace, proe, pass-run, w-volume]
keywords: [play-count, pass-rate, proe, game-script, seconds-per-play]
related:
  - concepts/implied-team-totals-dfs.md
  - concepts/player-usage-models.md
  - concepts/dfs-weather-adjustments.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/implied-team-totals-dfs.md — ITT and spread inputs
- @concepts/player-usage-models.md — usage shares multiply team volume

## Raw Concept

Model **team offensive plays** and **pass/run split** as the denominator for all player usage. PROE-centered; pace primary for play count.

## Narrative

### Play count (W-VOLUME / volume-pace)

Derive **neutral seconds/play** from nflfastR play-by-play (within-drive, `wp` 0.2–0.8, `qtr <= 3`). Stability hierarchy from 2021–2024 check:

| Metric | Next-season corr | Use |
|--------|------------------|-----|
| Neutral sec/play | ~0.47 | **Primary** play-count driver |
| PROE | ~0.34 | Pass split, not main play driver |
| Raw plays/game | ~0.21 | Heavy regression |

Seed formula (re-fit on your window):

```text
plays_projected ≈ 62 + 0.5*(36.2 - team_sec) + 0.35*(36.2 - opp_sec) + 0.08*(total - 44.8)
```

### Pass/run split (W-VOLUME / volume-passrun)

```text
projected_pass_rate = base (~0.565) + 0.8*(neutral_PROE/100)
                    + spread_adj + live_script_adj + weather_adj
```

| Adjustment | Coefficient | Source |
|--------------|-------------|--------|
| Spread (pregame) | ~**-0.5 pp pass rate per spread point** (favorite runs more) | FantasyLabs/Action |
| Live trailing | ~0.009 × trail_points × game_progress | Footballguys score-diff model |
| Wind ≥10 mph | -1.5 to -7 pp pass rate by tier | Claremont wind study |

**Total** belongs mostly in play-count model, not pass-rate (nflfastR calibration note).

### Allocation pseudocode

```text
team_dropbacks = plays_projected * pass_rate
pass_att = team_dropbacks * (1 - sack_rate - scramble_rate)
rush_att = plays_projected - team_dropbacks + scrambles
```

## Snippets

> "Don't use raw pass rate as team tendency." [Source: Open Source Football — https://www.opensourcefootball.com/posts/2020-09-07-estimating-runpass-tendencies-with-tidymodels-and-nflfastr/]

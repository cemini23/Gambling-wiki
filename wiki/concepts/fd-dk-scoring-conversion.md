---
title: FanDuel vs DraftKings scoring conversion
type: concept
tags: [concept, dfs, nfl, scoring, fanduel, draftkings, w-scoring]
keywords: [half-ppr, full-ppr, yardage-bonus, dst-scoring]
related:
  - entities/platforms/fanduel.md
  - entities/platforms/draftkings.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @entities/platforms/fanduel.md — W8 primary site
- @entities/platforms/draftkings.md — secondary site

## Raw Concept

Deterministic counting-stats → fantasy points for **FanDuel half-PPR** and **DraftKings full-PPR + bonuses**. [NEEDS VERIFICATION against live site rules at 2026 season start]

## Narrative

### Key differences (2026-06-20 retrieval)

| Stat | FanDuel | DraftKings |
|------|---------|------------|
| Reception | **0.5 PPR** | **1.0 PPR** |
| Pass TD | 4 pts | 4 pts |
| INT | -1 | -1 |
| Fumble lost | **-2** | -1 |
| 100+ rush/rec yds | +3 | +3 |
| 300+ pass yds | +3 | +3 |
| Salary cap | $60,000 | $50,000 |
| Roster | QB,2RB,3WR,TE,FLEX,DST | same structure |

### Archetype bias

- **DK** favors high-target PPR machines (slot WR, pass-catching RB)
- **FD** favors TD-heavy roles (half-PPR reduces reception floor)

### DIY model output

Emit **separate columns**: `fd_projection` and `dk_projection` from same counting stats — do not reuse one site's median on the other.

### DST nuance

Tier ladder identical (+10/+7/+4/+1/0/-1/-4) but **points-allowed definition differs** — FD vs DK attribution rules not fully matched [NEEDS VERIFICATION 2026-09].

## Snippets

> Both sites now publish +3 bonuses for 100-yard skill and 300-yard passing milestones. [Source: official FD/DK rules pages — retrieved 2026-06-20]

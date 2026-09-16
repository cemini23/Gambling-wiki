---
title: DFS FOSS tooling landscape
type: concept
tags: [concept, dfs, nfl, foss, nflverse, pydfs, w-foss]
keywords: [nflreadpy, pydfs-lineup-optimizer, chanzer0, license-audit]
related:
  - concepts/nfl-dfs-data-sources.md
  - entities/tools/pydfs-lineup-optimizer.md
  - concepts/dfs-stat-projection-engine.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-09-15
---

## Relations

- @entities/tools/pydfs-lineup-optimizer.md — MIT GO lineup engine
- @concepts/nfl-dfs-data-sources.md — data layer

## Raw Concept

Phase-0 audit of FOSS repos for DIY NFL DFS stack. **Build vs borrow** verdicts.

## Narrative

### Data libraries

| Library | License | Verdict |
|---------|---------|---------|
| **nflreadpy** | MIT | **GO** — canonical Python loader (replaces deprecated nfl_data_py) |
| nfl_data_py | MIT | **NO-GO** — deprecated/archived |
| nflreadr (R) | MIT | **CONDITIONAL-GO** — only if R bridge needed |

### Optimizer / sim repos

| Repo | License | Verdict | Reuse |
|------|---------|---------|-------|
| pydfs-lineup-optimizer | MIT | **GO** | Lineup gen, stacks, exposure |
| jnederlo/dfs_optimizers | MIT | **GO** | Solver formulation ideas |
| chanzer0/NFL-DFS-Tools | **None** | **NO-GO** code | Sim methodology reference only |
| draftfast | None | **NO-GO** code | Design reference only |

### Reject / NO-GO (2026-09-15 audit)

| Repo | License | Verdict | Why |
|------|---------|---------|-----|
| dynastyprocess/data | GPL-3.0 | **NO-GO** | Do not vendor `db_playerids.csv`; GPL is extract-only |
| FantasyFootballAnalytics/ffanalytics | GPL-3.0 | **NO-GO** | GPL is extract-only; already have nflreadpy |
| sarartur/oddsapi | **NO_LICENSE** | **NO-GO** | Use the stdlib Odds API client |
| jmoore87jr/DFS_ownership_projections | **NO_LICENSE** + scrape | **NO-GO** | No license; scraper violates data bar |

License posture: GPL/AGPL repos are extract-only (read the idea, never copy the code). NO_LICENSE repos are not usable. Check the GitHub LICENSE before any copy — an extract claim is not proof. [Source: briefs/2026-09-15_gemini-tool-improve-hub.md (retrieved 2026-09-15)]

### Gaps requiring custom build

- NFL ownership model + historical label archive
- Licensed correlation matrix for production reuse
- Contest field generator

### Recommended stack

`nflreadpy` + `nflverse-data` (CC-BY-4.0) + `pydfs-lineup-optimizer` + custom projection/ownership layers.

## Snippets

> "Borrow data and optimization plumbing; custom-build ownership, field, and correlation layers." [Source: K125 W-FOSS synthesis, 2026-06-20]

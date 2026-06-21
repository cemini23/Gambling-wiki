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
updated: 2026-06-20
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

### Gaps requiring custom build

- NFL ownership model + historical label archive
- Licensed correlation matrix for production reuse
- Contest field generator

### Recommended stack

`nflreadpy` + `nflverse-data` (CC-BY-4.0) + `pydfs-lineup-optimizer` + custom projection/ownership layers.

## Snippets

> "Borrow data and optimization plumbing; custom-build ownership, field, and correlation layers." [Source: K125 W-FOSS synthesis, 2026-06-20]

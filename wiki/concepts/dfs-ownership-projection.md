---
title: DFS ownership projection
type: concept
tags: [concept, dfs, nfl, ownership, field-modeling, w-own]
keywords: [projected-ownership, leverage, field-sim, duplication, elastic-net]
related:
  - concepts/dfs-distribution-layer.md
  - concepts/dfs-strategy-overview.md
  - entities/tools/stokastic-dfs.md
  - entities/tools/fantasylabs-dfs.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/dfs-strategy-overview.md — GPP leverage framework
- @entities/tools/fantasylabs-dfs.md — best historical ownership label source

## Raw Concept

Project **field ownership** and model **opponent lineups** for GPP leverage. Hardest DIY layer — FOSS ownership models sparse.

## Narrative

### Ranked ownership drivers

1. **Value** (proj / salary) — strongest
2. **Role / opportunity** (snap, target, carry share)
3. **Salary-tier roster fit**
4. **Team implied total / game environment**
5. **Positional scarcity** (TE especially)
6. **Stackability**
7. **Recency / narrative proxies** (last-game smash, injury bump)
8. **Contest context** (FD vs DK, MME vs SE)

### Model spec

- **Target:** position-normalized ownership share (`own / slot_mass`)
- **Algorithm:** Elastic Net on log-share + isotonic calibration
- **Separate models:** site × contest_family × position
- **Free features:** salary, proj, value rank, ITT, stack score, injury flags

### Historical labels

**FantasyLabs Trends** = best primary label source (paid, manual export). SaberSim Contest Flashback for validation. **No clean public ownership archive** — custom build required.

### Field sim + leverage

- Generate field lineups from ownership + stack templates (not independent player sampling)
- **DupAdjROI** = primary lineup metric (payout / duplication split)
- **LineupLeverage** = P(top1%) / field_frequency

Product ownership beats cumulative ownership for duplication proxy (ETR showdown research).

## Snippets

> "The real bottleneck is not features — it's clean historical ownership labels by site/contest type." [Source: K125 W-OWN synthesis, 2026-06-20]

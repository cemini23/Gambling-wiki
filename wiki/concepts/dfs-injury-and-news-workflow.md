---
title: DFS injury and news workflow
type: concept
tags: [concept, dfs, nfl, injury, late-swap, w-inj, w-news]
keywords: [nflreadr-injuries, inactives, late-swap, override-schema]
related:
  - concepts/pickem-operator-workflow.md
  - concepts/player-usage-models.md
  - concepts/dfs-pipeline-integration-spec.md
  - concepts/diy-nfl-dfs-model-architecture.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/pickem-operator-workflow.md — K147 pick'em shares injury latency patterns
- @concepts/player-usage-models.md — Q/D/O play-probability priors

## Raw Concept

Injury/depth data sources + **late-swap operating procedure** for W-INJ / W-NEWS.

## Narrative

### Data sources

| Source | Use | Verdict |
|--------|-----|---------|
| nflreadr `load_injuries()` | Designations + practice | **GO** |
| nflreadr `load_depth_charts()` | Weekly depth | **CONDITIONAL-GO** |
| NFL.com inactives | Canonical ~T-90 | Manual hub |
| X beat writers | Fastest | Manual only (ToS prohibits scrape) |

### Q/D/O play probability defaults

| Status | Play prob |
|--------|-----------|
| Q | 0.70 |
| D | 0.03 |
| O | 0.00 |

Team-specific calibration recommended (Footballguys / Banged Up Bills studies).

### Pre-lock timeline

| Time | Action |
|------|--------|
| **T-90** | Baseline build; pivot matrix; inactives watch |
| **T-30** | Re-pull news; rerun if material changes |
| **T-5** | Final sanity; no O/inactive tags |
| **T-15 FD** | Hard stop for cancel/re-enter |

### Override schema

Log: `override_id`, `trigger_type`, `player_out/in`, `baseline_build_id`, `rerun_mode`, `projection_delta`, pre/post CSV paths — never overwrite baseline artifacts.

### Late-swap pydfs path

`load_lineups_from_csv()` → mark `game_started` for locked teams → `optimize_lineups()` → export. **Not yet in repo** — backlog item.

## Snippets

> "Safest semi-auto stack: NFL.com/inactives + official team posts + RotoWire cross-check." [Source: K125 W-INJ inj-news-fast, 2026-06-20]

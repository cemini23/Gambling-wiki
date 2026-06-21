---
title: DFS model orchestration
type: concept
tags: [concept, dfs, nfl, orchestration, pipeline, w-orch]
keywords: [weekly-run, parquet, manifest, nfl-dfs-config]
related:
  - concepts/dfs-pipeline-integration-spec.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
  - meta/daily-research-digest-cadence.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- @concepts/dfs-pipeline-integration-spec.md — stage I/O contracts
- @meta/daily-research-digest-cadence.md — thin-orchestrator pattern precedent

## Raw Concept

Laptop-first **weekly NFL DFS run**: fetch → project → sim → normalize → optimize with parquet cache + run manifest.

## Narrative

### Stages

| Stage | Output |
|-------|--------|
| `fetch` | `artifacts/nfl-dfs/cache/*.parquet` + manual salary immutable |
| `project` | `player_projection_base.parquet` |
| `sim` | `player_sim_summary.parquet` (p10/p50/p90, ownership prior) |
| `normalize` | `fanduel-pydfs.csv` |
| `optimize` | `lineups.csv`, `exposures.csv` |

### Config / secrets

- `scripts/nfl_dfs_config.yaml` — tracked, non-secret
- `.env` — `ODDS_API_KEY` etc. (gitignored)
- Mirror `daily_research_digest_run.py` thin-runner pattern

### Run manifest

Every run writes `manifest.json`: `run_id`, `git_commit`, `config_sha256`, `input_artifacts` (path + hash), `stage_status`, `random_seed`.

### Proposed scripts (backlog)

`nfl_dfs_weekly_run.py`, `nfl_dfs_fetch.py`, `nfl_dfs_project.py`, `nfl_dfs_simulate.py`, `nfl_dfs_normalize.py`, `nfl_dfs_optimize.py`, `nfl_dfs_manifest.py`

## Snippets

> "Manual-only salary ingestion to stay inside source-policy." [Source: K125 W-ORCH + W-LEGAL, 2026-06-20]

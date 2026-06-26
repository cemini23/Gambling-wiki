---
title: NFL DFS ID mapping and name normalization research
type: source
tags: [source, brief, dfs, nfl, data-engineering, nflverse, ceminidfs]
keywords: [gsis_id, ff_playerids, fanduel, draftkings, name-normalization, fuzzy-match]
related:
  - concepts/nfl-dfs-data-sources.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-pipeline-integration-spec.md
  - entities/tools/ceminidfs.md
  - sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md
maturity: validated
read_status: deep-read
created: 2026-06-20
updated: 2026-06-26
cross-wiki-source: "briefs/nfl-dfs-id-mapping-research.md"
---

## Relations

- @concepts/nfl-dfs-data-sources.md — source stack matrix
- @entities/tools/ceminidfs.md — implementation target (W9)
- @sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md — BBM name-normalize spike (P0)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | NFL DFS ID mapping research |
| **Date** | 2026-06-20 |
| **Verdict** | **GO** — nflverse crosswalk + fuzzy fallback pipeline |

## Narrative

### Crosswalk sources

| Dataset | Role |
|---------|------|
| `nflreadr::load_players()` | Canonical base; `gsis_id` primary key |
| `nflreadr::load_ff_playerids()` | Fantasy platform IDs → bridge to `gsis_id` |

### FD/DK normalization pipeline

1. Lowercase + strip punctuation/apostrophes
2. Strip suffixes (jr, sr, ii, iii, iv)
3. Team/DEF standardization (JAX/JAC, LV, etc.)
4. Manual alias dictionary (Mitch/Mitchell, Gabe/Gabriel)
5. Fuzzy fallback when exact match fails

### BBM7 hook

Challenge register P0: **player name normalization** blocks ADP/projection merge for Draft Copilot Phase 1.

## Dead Ends

- Scraping FD/DK salary pages as primary ID source (ToS risk)
- Using display names without `gsis_id` anchor in backtests

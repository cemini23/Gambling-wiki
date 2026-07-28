---
title: Brief K162 — HarnessLLM false-positive shelf
type: source
tags: [brief, k162, reject, digest, false-positive]
keywords: [k162, 2607.22161, harnessllm, dfs-ownership-false-positive]
related:
  - sources/daily-digest-batch-k162-2026-07-28.md
  - sources/daily-digest-reject-cluster-k162-2026-07-28.md
  - sweeps/2026-07-28-daily.md
  - meta/daily-research-digest-cadence.md
maturity: validated
read_status: skimmed
created: 2026-07-28
updated: 2026-07-28
cross-wiki-source: "briefs/2026-07-28_k162-harnessllm-false-positive-shelf.md"
---

## Relations

- Wiki: `briefs/2026-07-28_k162-harnessllm-false-positive-shelf.md`
- No OSINT arena / CCC prod / TipDrop / CeminiDFS copies — reject-only OOD

## Raw Concept

K162 shelf — record `cemini-dfs-ownership-paper` false positive (Rust ownership / HarnessLLM); no steals.

## Narrative

1. Do not adopt FOSS or phase-0 tooling from 2607.22161.
2. Tightened `cemini-dfs-ownership-paper` arXiv query: require `"daily fantasy"` / DraftKings / FanDuel / `"fantasy sports"` anchor; drop bare `ownership` as a top-level OR (third bleed after GenAI design K160 + EV charging K161).
3. Empty sweep 07-27 closed with this ingest.

## Sources

- @sources/daily-digest-reject-cluster-k162-2026-07-28.md

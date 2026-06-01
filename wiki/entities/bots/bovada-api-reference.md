---
title: Bovada API community clients (ctrlaltdylan / jkol36)
type: entity
tags: [entity, bot, sportsbook, api, reference-only]
keywords: [bovada, sportsbook api, scanner, hand-history, k92]
related:
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - entities/bots/wagerbrain.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — Reference-only + hand-history steal-from

## Raw Concept

K92 eval: **ctrlaltdylan/bovadaAPI**, **jkol36/bovadaAPI** (scanner duplicate); **matt57225/bovada-hand-history-converter** (hand-history).

## Narrative

### Phase-0 audit (2026-06-01)

| Repo | License | Stars | Pushed | Verdict |
|------|---------|-------|--------|---------|
| ctrlaltdylan/bovadaAPI | **None** (404 on license API) | 9 | 2015-12 | **NO-GO** |
| jkol36/bovadaAPI | (same class) | — | — | **NO-GO** |
| matt57225/bovada-hand-history-converter | **None** | 32 | 2020-06 | **NO-GO** (archived) |

**Sportsbook bot lane** — documents **pattern only** (unofficial API + hand-history ingest). **ToS/jurisdiction** block production use.

**Verdict: NO-GO for adopt** — reference for manual research only; no clone into Cemini or gambling-bot prod paths without written legal review + maintained fork.

## Snippets

> Eval: "Duplicates module 1 (scanner)" — bovadaAPI pair. [Source: K92 eval]

---
title: Daily digest batch K165 (2026-08-04)
type: source
tags: [source, arxiv, daily-digest, k165, reject]
keywords: [digest, 2607.28779, bits-per-spike, false-positive]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-04-daily.md
  - sources/daily-digest-batch-k164-2026-07-30.md
  - sources/daily-digest-reject-cluster-k165-2026-08-04.md
  - sources/brief-k165-bits-per-spike-false-positive-shelf-2026-08-04.md
maturity: validated
read_status: skimmed
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- @sweeps/2026-08-04-daily.md — overnight digest (inbox PDF from Aug 3 fetch)
- @sources/daily-digest-reject-cluster-k165-2026-08-04.md — neuroscience / bits-per-spike reject
- @sources/brief-k165-bits-per-spike-false-positive-shelf-2026-08-04.md — shelf note

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-08-04 |
| **Origin** | `research to be indexed/` — 1 PDF (fetched 2026-08-03) |
| **Verdict** | **0 GO / 0 CONDITIONAL-GO / 1 reject** |
| **Phase-1** | **wont_wire** — reject-only; no ADOPT/GO to wire |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2607.28779 | Bits per Spike as a Betting Game | none | **Reject** |

**Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (1 PDF; inbox cleared)

## Narrative

Pure false-positive overnight fetch via `kelly-bankroll-arxiv` (Kelly + “betting game” metaphor for neural spike-train model comparison). No wagering, sportsbook, poker, DFS, or bot steals. Sweeps 2026-07-31…08-02 were empty-inbox — marked INGESTED-empty with this batch. Tightened Kelly arXiv query to require odds/sports/bankroll anchors and ANDNOT neural/spike bleed.

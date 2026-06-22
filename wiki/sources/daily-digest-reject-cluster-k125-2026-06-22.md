---
title: Daily digest reject cluster K125 (2026-06-22)
type: source
tags: [source, arxiv, daily-digest, reject, k125]
keywords: [2606.14951, 2606.18191, drflow, submodular, knapsack, digest]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-06-22-daily.md
  - sources/daily-digest-reject-cluster-k124-2026-06-21.md
  - sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md
maturity: validated
read_status: skimmed
created: 2026-06-22
updated: 2026-06-22
---

## Relations

- @sweeps/2026-06-22-daily.md — overnight fetch (3 NEW PDFs)
- @sources/brief-k125-eval-gate-discipline-2026-06-22.md — operator eval steal from ingested paper

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-22 |
| **Origin** | `research to be indexed/` — 3 NEW PDFs |
| **Verdict** | **1 REFERENCE ingest / 2 reject** |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2606.14506 | Beyond the Training Distribution (shift + selective labels) | N/A | **REFERENCE** → dedicated source |
| 2606.14951 | DP Submodular Maximization with Knapsack | N/A | **Reject** — discrete optimization / privacy |
| 2606.18191 | DRFLOW — Deep Research Workflow Benchmark | GitHub 404 | **Reject** — enterprise workflow DR, not wagering |

**Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (3 PDFs; inbox cleared)

## Narrative

### 2606.14951 — DP submodular knapsack [REJECT]

Differentially private algorithms for submodular maximization under knapsack constraint. cs.DS/OR — matched `dfs-roster-arxiv` via "knapsack" keyword. No fantasy roster or lineup content.

### 2606.18191 — DRFLOW [REJECT]

ServiceNow benchmark for **personalized enterprise workflow** prediction from heterogeneous docs. Agent must predict action-step sequences (HR/policy tasks). Not poker, DFS, or prediction markets. `github.com/ServiceNow/drflow` **404** at Phase-0 (2026-06-22).

### Ingested sibling

- @sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md

## Snippets

> "DRFLOW contains 100 tasks across five domains... predicting complete and correct personalized workflows remains a challenging frontier." [Source: arxiv:2606.18191 abstract]

## Dead Ends

- DRFLOW as HL loop template — enterprise doc workflows ≠ NLHE `decide()`
- Submodular knapsack for pydfs lineup — different problem class than MIP optimizer

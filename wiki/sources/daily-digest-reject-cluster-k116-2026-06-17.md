---
title: Daily digest reject cluster K116 (2026-06-17)
type: source
tags: [source, arxiv, daily-digest, reject, dead-end, k116]
keywords: [2606.08551, 2606.08693, 2606.10342, 2606.11044, 2606.11118, 2606.11859, false-positive, digest]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/gambling-bot-architecture.md
  - sources/daily-digest-reject-cluster-k119-2026-06-18.md
  - sweeps/2026-06-17-daily.md
maturity: validated
read_status: skimmed
created: 2026-06-17
updated: 2026-06-19
---

## Relations

- @sweeps/2026-06-17-daily.md — overnight fetch after digest tune
- @sources/daily-digest-reject-cluster-k119-2026-06-18.md — successor reject batch
- @meta/daily-research-digest-cadence.md — query tightening backlog
- Private brief: `briefs/2026-06-17_k116-gambling-digest-arxiv-false-positives.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Ingest** | 2026-06-17 |
| **Origin** | `wiki/sweeps/2026-06-17-daily.md` auto-fetch after digest tune |
| **Verdict** | **0 ingest / 6 reject** — Exa noise, out of gambling-wiki scope |

| arXiv | Title | Phase-0 | Verdict |
|-------|-------|---------|---------|
| 2606.08551 | Enhanced localized conformal prediction… | N/A | **Reject** — stats/ML, not wagering |
| 2606.08693 | Epidemic forecasting susceptibility… | N/A | **Reject** — epidemiology |
| 2606.10342 | Binomial smoothing supply chains… | N/A | **Reject** — OR/inventory |
| 2606.11044 | Generalized conformal predictive systems… | N/A | **Reject** — conformal ML |
| 2606.11118 | Data-driven dynamic assortment online platforms… | N/A | **Reject** — platform econ; tangential |
| 2606.11859 | Scenario generation time series… | N/A | **Reject** — generic quant finance |

**Archive:** `raw-sources/rejected-digest-2026-06-17/` (local only; gitignored)

## Narrative

First post-tune digest batch with **high false-positive rate** on broad paper queries. All six matched keyword overlap (prediction, forecasting, assortment) without wagering-domain content.

**Follow-up:** tightened paper queries in `scripts/daily_research_config.yaml` 2026-06-17; K119 continued reject cluster 2026-06-18.

## Dead Ends

- **Ingest assortment paper for DFS lane** — marketplace theory ≠ roster construction
- **Conformal prediction for CLV** — no sportsbook/wagering hook in abstracts

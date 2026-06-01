---
title: "PolyGnosis 2.0 — Polymarket anomaly + GDELT OSINT harness"
type: source
tags: [source, arxiv, polymarket, prediction-markets, agent-harness]
keywords: [polygnosis, perspective-mismatch, gdelt, harness-engineering, whale-alerts]
related:
  - concepts/pm-perspective-mismatch-trading.md
  - concepts/pm-commitment-grounded-language.md
  - concepts/prediction-markets-crossover.md
  - entities/platforms/polymarket.md
  - concepts/gambling-bot-architecture.md
  - sources/daily-digest-news-r1-r12-2026-06-01.md
  - sources/daily-digest-arxiv-batch-2026-06-01.md
  - meta/daily-research-digest-cadence.md
  - sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-01
cross-wiki-implementation: @osint-wiki/entities/tools/polygnosis.md
---

## Relations

- @entities/platforms/polymarket.md — primary market surface
- @concepts/pm-perspective-mismatch-trading.md — retail framing of “Perspective Mismatch”
- @osint-wiki — prod harness / Cemini execution (do not duplicate code here)
- @osint-wiki/entities/tools/polygnosis.md — PolyGnosis 2.0 implementation stub

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | 2605.25958 |
| **Authors** | Wang, Xu, Xian (CUHK / Evolution AI Lab) |
| **PDF** | `raw-sources/arxiv-2605.25958-polygnosis-2-0.pdf` |
| **sha256** | `0ada5cd49cea2b9b…` (3,052,660 bytes) |
| **Retrieved** | 2026-06-01 (digest retry; prior run HTTP 429) |

## Narrative

### Thesis (gambling-wiki slice)

**PolyGnosis 2.0** ingests Polymarket **anomaly alerts** (price shocks, whale volume), clusters events, pulls **GDELT** media, and scores **Perspective Mismatch** — narrative divergence between PM traders and global media — as a **high-alpha signal** [CONFIRMED abstract].

Pipeline: WebSocket monitor → Clustering Agent → Keywords Agent (GDELT) → Analysis Agent (PM direction vs media direction vs alignment).

### Harness engineering findings [TENTATIVE — paper claims]

- **Divide-and-conquer partitioning** required for multi-dimensional alignment.
- **Unconstrained terminal reflection** can induce **logical drift** (worse than structured pass).
- **Consensus bias** across agent configs on narrative tasks → needs deterministic validation.
- Pareto-optimal config trades accuracy vs latency/token cost.

### Retail vs prod split

| Layer | Home |
|-------|------|
| What “mismatch” means for wagering discipline | **gambling-wiki** |
| Bot code, API keys, prod deploy | **@osint-wiki** |

Not a sportsbook +EV tool — **PM/OSINT research** lane. Pair with `@concepts/pm-commitment-grounded-language.md` (StakeBench: commitment in comments) and `@concepts/sportsbook-pm-line-divergence.md` (price gaps vs books).

### Phase-0

**REFERENCE** for gambling-bot program — alert→research workflow only; **NO-GO** for automated retail betting without separate legal/ToS review.

## Snippets

> "Perspective Mismatches — the narrative divergence between Polymarket sentiment and global media flows — as high-alpha trading signals." [Source: arxiv:2605.25958 abstract]

> "Unconstrained terminal reflection actively induces logical drift." [Source: same, §3.2]

## Dead Ends

- **Not** a substitute for closing-line sportsbook edge or Kalshi sports contract fee math
- GDELT/media lag vs sub-minute PM moves — latency risk for live trading

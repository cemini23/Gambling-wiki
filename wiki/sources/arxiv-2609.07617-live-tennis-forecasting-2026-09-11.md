---
title: "Forecasting the winner of a live tennis match (arXiv 2609.07617)"
type: source
tags: [source, arxiv, tennis, live-betting, k170]
keywords: [tennis, in-play, trace, elo, hawk-eye, grand-slam, live-betting]
related:
  - entities/sports/tennis-betting.md
  - concepts/live-betting-match-integrity.md
  - concepts/sports-betting-fundamentals.md
  - sources/daily-digest-batch-k170-2026-09-11.md
  - sources/brief-k170-week1-papers-rss-2026-09-11.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-09-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-11
updated: 2026-09-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2609.07617-forecasting-the-winner-of-a-live-tennis-match.pdf
phase_0_verdict: REFERENCE 2026-09-11 — live tennis hybrid model; no FOSS; no bot lane
wire_status: wont_wire
---

## Relations

- @entities/sports/tennis-betting.md — live tennis retail context
- @concepts/live-betting-match-integrity.md — in-play liquidity / integrity sibling
- @concepts/sports-betting-fundamentals.md — live betting product lane
- @sources/daily-digest-batch-k170-2026-09-11.md — digest batch
- @sources/brief-k170-week1-papers-rss-2026-09-11.md — operator brief

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2609.07617](https://arxiv.org/abs/2609.07617) |
| **Authors** | Charles Xie (Natick HS), Aneesh Muppidi (Oxford mentor) |
| **Type** | stat.AP — live sports forecasting |
| **Data** | 8,222 Grand Slam matches; 1.5M points; train 2011–2021, val 2022, test 2023–2024 |
| **FOSS** | None published |
| **Phase-0** | **REFERENCE** — hybrid pre-match + live tennis model literacy |
| **Wire** | `wont_wire` — student paper; no production model |

## Narrative

Live tennis is ~**80%** of tennis wagering volume [TENTATIVE — cited in paper]. This study compares five models integrating pre-match priors with in-match state updates.

**Trace** (hybrid) achieved test accuracies **76.06% / 82.15% / 88.34%** at **25% / 50% / 75%** match progress. Builds on hierarchical Markov (Klaassen–Magnus), Gollub beta-binomial serve updates, and DeepTennis LSTM context (79.5% contextual benchmark — not directly comparable years).

**Retail posture:** literacy only. Do not deploy as a live betting bot or PM signal without independent replication and vig-adjusted EV tests.

### Lane fit

| Lane | Fit |
|------|-----|
| **Tennis live betting literacy** | **REFERENCE** |
| **Gambling bots / prod scp** | **NONE** |

## Snippets

> "Trace, a hybrid model, achieved accuracies of 76.06%, 82.15%, and 88.34% at 25%, 50%, and 75% match progress." [Source: arxiv:2609.07617 abstract]

> "Approximately 80% of the money wagered on tennis matches has been reported to be placed in-play." [Source: arxiv:2609.07617 §1 footnote 2]

## Dead Ends

- Treating accuracy percentages as +EV without vig and market-efficiency controls
- Building a tennis bot from this paper — no FOSS, student-scale validation only

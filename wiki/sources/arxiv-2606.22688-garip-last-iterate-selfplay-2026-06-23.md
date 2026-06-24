---
title: GARIP — running-average anchor for last-iterate self-play (arXiv 2606.22688)
type: source
tags: [source, arxiv, poker, game-theory, self-play, k126, garip]
keywords: [garip, last-iterate convergence, running average, r-nad, deepnash, zero-sum, self-play]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/heads-up-arena-strategy.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - sweeps/2026-06-23-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-23
updated: 2026-06-24
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.22688-pdf-garip-a-running-average-moving-reference-for.pdf
phase_0_verdict: REFERENCE 2026-06-23 — last-iterate self-play anchor design; offline HU selfplay tuning only
---

## Relations

- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — complementary equilibrium-seeking line (MAFP vs gradient self-play)
- @sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md — parameter-space EMA magnet (K127)
- @sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md — operator steal summary (K126)
- @concepts/poker-hl-analyst-loop.md — selfplay panel on egress; not runtime `decide()`

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.22688](https://arxiv.org/abs/2606.22688) |
| **Title** | GARIP: A Running-Average Moving Reference for Last-Iterate Self-Play in Two-Player Zero-Sum Games |
| **Phase-0** | Pure JAX experiments; no prod repo required |
| **Verdict** | **REFERENCE** — offline self-play / HU sandbox research lane |

## Narrative

Naive gradient self-play in two-player zero-sum games **cycles** — the last iterate orbits equilibrium. Modern fixes regularize toward a **reference policy**: MMD uses a fixed magnet (converges to regularized equilibrium only); R-NaD (DeepNash engine) uses periodic snapshots.

**GARIP** anchors to the **running average** of past policies. Core mechanism: collapse tracks the **peak lag** of the reference; among causal convex averages at fixed mean lag, the running average uniquely minimizes peak lag vs snapshot sawtooth (peak = 2× mean).

### Relevance to dev.fun poker track

| Application | Fit |
|-------------|-----|
| **HU TrueSkill selfplay** | REFERENCE — more robust anchor default than snapshot when tuning selfplay locals |
| **Runtime `decide()`** | **NO-GO** — multi-iterate self-play training loop, not per-hand inference |
| **Eval S1 panel** | Conceptual — compare fixed-magnet vs moving-reference selfplay baselines |
| **Connect Four / Othello in paper** | Analog for imperfect-info depth — poker not in eval set |

GARIP matches R-NaD peak performance on matrix games and board games but is the **better hyperparameter default** at conventional settings (0/40 vs 10/40 collapse at matched mean lag in paper).

### Steal for pure-code bot

When building **offline** HU selfplay opponents for regression gates (K125 regime table): prefer **running-average mixture** as the best-response target over stale snapshot or fixed CFR export — lighter than full GARIP implementation, same intuition as MAFP empirical mixture.

## Snippets

> "Collapse tracks the peak lag of the reference, and among causal convex averages of a fixed mean lag the running average uniquely minimizes that peak." [Source: arxiv:2606.22688 abstract]

> "GARIP matches R-NaD's peak performance … but is the better hyperparameter default." [Source: arxiv:2606.22688 abstract]

## Dead Ends

- **Deploy GARIP inside `decide()`** — training-time regularizer, not action selection
- **Replace MAFP stance entanglement with GARIP** — different problem (gradient cycling vs multi-stakeholder equilibrium)

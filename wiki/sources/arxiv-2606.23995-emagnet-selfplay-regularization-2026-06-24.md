---
title: EMAgnet — parameter-space EMA for policy-gradient self-play (arXiv 2606.23995)
type: source
tags: [source, arxiv, poker, game-theory, self-play, k127, emagnet]
keywords: [emagnet, ppo, self-play, regularization, magnet, last-iterate, exploitability, riot-games]
related:
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/heads-up-arena-strategy.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/daily-digest-reject-cluster-k127-2026-06-24.md
  - sweeps/2026-06-24-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-24
updated: 2026-06-24
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.23995-pdf-emagnet-parameter-space-ema-regularization-f.pdf
phase_0_verdict: REFERENCE 2026-06-24 — Riot Games internal; no public repo; offline selfplay research only
---

## Relations

- @sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md — complementary moving-reference family (policy average vs parameter EMA)
- @sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md — operator steal summary (K127)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.23995](https://arxiv.org/abs/2606.23995) |
| **Title** | EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games |
| **Authors** | Riot Games, UCI, NYU |
| **Phase-0** | No public implementation; proprietary game benchmarks |
| **Verdict** | **REFERENCE** — self-play regularization design for imperfect-info games |

## Narrative

Regularized PPO self-play can match or beat specialized solvers (R-NaD, PSRO, NFSP) in two-player zero-sum imperfect-information games. The default **uniform magnet** (entropy bonus) regularizes equally toward all actions — wasteful when most strategies are dominated (large poker action spaces).

**EMAgnet** maintains an **exponential moving average of policy network weights** as the regularization target — a moving magnet that trails the improving strategy (extends Sokota et al. tabular magnet idea to deep RL).

### Results (paper)

- Lower **exploitability** than uniform-magnet PPO across most tested environments
- Largest gains in games with **strictly dominated strategies** and exploration challenges (Control Biased RPS gridworld)
- Cites PPO self-play outperforming R-NaD under appropriate regularization — same design space as GARIP

### Relevance to dev.fun poker track

| Application | Fit |
|-------------|-----|
| **HU TrueSkill selfplay tuning** | REFERENCE — parameter-EMA magnet vs uniform entropy when training locals |
| **GARIP comparison** | GARIP = policy-space running average anchor; EMAgnet = **parameter-space** EMA magnet — same problem (last-iterate cycling), different layer |
| **Runtime `decide()`** | **NO-GO** — training-time regularizer |
| **HL analyst loop** | Conceptual only — egress selfplay panel design notes |

## Snippets

> "The uniform target is strategically agnostic as it regularizes equally toward all strategies regardless of whether they are viable or strictly dominated." [Source: arxiv:2606.23995 §1]

> "EMAgnet achieves lower exploitability in the majority of tested environments, with consistent performance gains across games containing strictly dominated strategies." [Source: arxiv:2606.23995 abstract]

## Dead Ends

- **Replace GARIP with EMAgnet in Eval S1** — different mechanism; both offline; pick one anchor family per experiment
- **Adopt Riot proprietary benchmarks** — not public; poker not primary eval in paper
- **Runtime magnet in `decide()`** — training-only

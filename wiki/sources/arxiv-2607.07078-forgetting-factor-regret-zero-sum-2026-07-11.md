---
title: Forgetting-factor regret for online zero-sum games (arXiv 2607.07078)
type: source
tags: [source, arxiv, game-theory, poker, opponent-modeling, k152]
keywords: [forgetting-factor, regret, nash-equilibrium, online-learning, saddle-point, zero-sum]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md
  - sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md
  - sources/daily-digest-batch-k152-2026-07-11.md
  - sweeps/2026-07-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-11
updated: 2026-07-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.07078-forgetting-factor-regret-for-online-zero-sum-gam.pdf
phase_0_verdict: REFERENCE 2026-07-11 — paper-only; recency-weighted regret for time-varying NE tracking
---

## Relations

- @sources/arxiv-2607.06854-lightweight-game-agent-expert-yardstick-2026-07-11.md — complementary eval methodology (K152 batch)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.07078](https://arxiv.org/abs/2607.07078) |
| **Verdict** | **REFERENCE** — **forgetting-factor regret** tracks time-varying Nash equilibria |

## Narrative

Online two-player zero-sum games with **time-varying** convex-concave payoffs. Standard regret aggregates history uniformly — poor real-time NE tracking signal.

**Forgetting-factor regret:** exponentially decaying weights on past saddle gaps → emphasizes **recent** performance vs current NE.

Algorithms analyzed: projected GDA, projection-free Frank-Wolfe, zeroth-order finite differences. Bounds characterize NE variation, payoff drift, gradient error.

| Lane | Fit |
|------|-----|
| **Arena self-play loops** | **MEDIUM** — recency-weighted health metric when opponents/meta shift |
| **Sportsbook / PM** | LOW — not wagering microstructure |
| **MAFP / fictitious play** | Theory cross-ref for non-stationary pools |

**Adoption for David:** when monitoring online self-play or league training, prefer **recency-weighted regret/exploitability** over lifetime averages if opponent pool is drifting.

## Snippets

> "Existing regret metrics … aggregate historical payoffs with uniform weights, and hence may fail to characterize the real-time tracking performance with respect to the current Nash equilibrium." [Source: arxiv:2607.07078 Abstract]

## Dead Ends

- Forgetting-factor regret as live NLHE `decide()` patch without sandbox validation
- Uniform cumulative regret as sole HU league health dashboard

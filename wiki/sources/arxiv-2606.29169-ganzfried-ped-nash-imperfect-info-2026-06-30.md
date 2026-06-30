---
title: Ganzfried — projected exploitability descent for multiplayer Nash (arXiv 2606.29169)
type: source
tags: [source, arxiv, poker, game-theory, nash, k134, ganzfried, ped]
keywords: [projected-exploitability-descent, ped, fp-ped, kuhn-poker, sequence-form, multiplayer, exploitability]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - concepts/poker-hl-analyst-loop.md
  - entities/games/poker.md
  - sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md
  - sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md
  - sources/daily-digest-batch-k134-2026-06-30.md
  - sweeps/2026-06-30-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-30
updated: 2026-06-30
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.29169-projected-exploitability-descent-for-nash-equili.pdf
phase_0_verdict: REFERENCE 2026-06-30 — scalable NE approximation theory; no FOSS repo; pairs K131 VBT exact lane
---

## Relations

- @sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md — exact NLCP + VBT (K131)
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — Ganzfried COM exploit lane
- @sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md — K134 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.29169](https://arxiv.org/abs/2606.29169) |
| **Title** | Projected Exploitability Descent for Nash Equilibrium Computation in Multiplayer Imperfect-Information Games |
| **Author** | Sam Ganzfried (Ganzfried Research / Cornell) |
| **Phase-0** | N/A — theory/algorithm paper; no public code cited |
| **Verdict** | **REFERENCE** — scalable **approximate** multiplayer NE via exploitability minimization |

## Narrative

Introduces **projected exploitability descent (PED)**: projected subgradient descent on a **multiplayer generalized exploitability** proxy in sequence-form strategies. Objective is nonconvex/nonsmooth but decomposes as sum of maxima of linear functions — subgradients project to the strategy polytope.

Benchmark: generalized **3-player Kuhn poker** (deck sizes beyond exact-solver scale). Compared to **fictitious play (FP)** and **CFR**:

| Algorithm | Behavior |
|-----------|----------|
| **FP / CFR** | Strong early iterations |
| **PED** | Near-monotonic long-run exploitability improvement |
| **FP-PED hybrid** | FP burn-in → switch to PED for stable refinement |

Complements K131 **VBT exact** lane: exact NLCP when small; PED/FP-PED when enumeration fails.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Poker theory literacy** | **HIGH** — third Ganzfried anchor (COM → VBT → PED) |
| **MAFP / selfplay research** | Medium — FP burn-in + refinement mirrors hybrid training metaphors |
| **dev.fun arena bot** | **NO-GO** — Kuhn-scale only; NLHE intractable |
| **Exploitability metrics** | **HIGH** — formal ε(σ) for n-player imperfect-info |

Phase-0 **REFERENCE** — cite when explaining why arena bots use heuristics + gates, not gradient NE solvers.

## Snippets

> "PED obtains a consistent near-monotonic improvement throughout all runs, though both FP and CFR perform significantly better in the initial iterations." [Source: arxiv:2606.29169 Abstract]

> Hybrid **FP-PED** runs FP for an initial burn-in period before switching to PED for stable long-run refinement. [Source: arxiv:2606.29169 Abstract]

> Exploitability ε(σ) generalizes the two-player zero-sum metric to n-player normal-form games. [Source: arxiv:2606.29169 §1]

## Dead Ends

- PED on dev.fun NLHE instance
- Replace `cemini_decide` with FP-PED training loop on prod timeline
- Conflate Kuhn poker ε improvement with Playground bb/100

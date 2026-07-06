---
title: Ganzfried — variable bound tightening for Nash in multiplayer imperfect-info games (arXiv 2606.25997)
type: source
tags: [source, arxiv, poker, game-theory, nash, k131, ganzfried]
keywords: [nash-equilibrium, sequence-form, nlcp, kuhn-poker, mccormick, branch-and-bound, multiplayer]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-strategy-overview.md
  - concepts/heads-up-arena-strategy.md
  - entities/games/poker.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - sources/brief-k131-toolbench-ganzfried-steals-2026-06-26.md
  - sources/daily-digest-reject-cluster-k131-2026-06-26.md
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - sources/arxiv-2509.25618-ganzfried-qp-nash-imperfect-info-2026-07-06.md
  - sweeps/2026-06-26-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-26
updated: 2026-06-30
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.25997-pdf-variable-bound-tightening-for-nash-equilibri.pdf
phase_0_verdict: REFERENCE 2026-06-26 — exact Nash solver theory; no wagering bot adoption path
---

## Relations

- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — prior Ganzfried opponent-modeling anchor (K95)
- @concepts/opponent-modeling-imperfect-info.md — exploit lane vs exact equilibrium computation
- @sources/brief-k131-toolbench-ganzfried-steals-2026-06-26.md — K131 operator summary
- @sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md — scalable PED / FP-PED (K134)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.25997](https://arxiv.org/abs/2606.25997) |
| **Title** | Variable Bound Tightening for Nash Equilibrium Computation in Multiplayer Imperfect-Information Games |
| **Author** | Sam Ganzfried (Ganzfried Research / Cornell) |
| **Phase-0** | N/A — solver theory paper; uses Gurobi NLCP |
| **Verdict** | **REFERENCE** — exact Nash in **multiplayer** imperfect-info; strengthens prior NLCP branch-and-bound |

## Narrative

Extends recent **nonlinear complementarity program (NLCP)** approach for **exact Nash equilibrium** in multiplayer imperfect-information extensive-form games. Prior work solved 3-player Kuhn poker **after dominated-action removal** via Gurobi spatial branch-and-bound + McCormick relaxations; **full game** failed within 24h.

This paper derives **finite bounds** on slack and multiplier variables in the NLCP, tightening convex relaxations. Demonstrated speedups on **3-player Kuhn poker** exact equilibrium computation.

### Method sketch [CONFIRMED]

- Sequence-form representation → feasibility NLCP with complementarity slackness (products of variables)
- Generalizes 2-player LCP (Lemke-Howson) to **n ≥ 3** players via quadratically constrained program
- **Variable bound tightening (VBT)** on multipliers/slacks before branch-and-bound

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Poker theory literacy** | **HIGH** — bridges CFR/MAFP scalable approximations vs **exact** multiplayer Nash |
| **dev.fun arena bot** | **NO-GO** — toy games only; NLHE scale intractable for exact solver |
| **Opponent modeling** | Medium — same author lineage as COM (2508.17671); exact NE is ceiling, not runtime policy |
| **6-max / HU sandbox** | Context only — TrueSkill ranks policies, not full-game NE |

Phase-0 **REFERENCE** — cite when discussing exploitability bounds and why arena bots use heuristics + selfplay, not Gurobi NLCP.

## Snippets

> "Counterfactual regret minimization and fictitious play are scalable to large games … but do not guarantee convergence to Nash equilibrium in multiplayer games." [Source: arxiv:2606.25997 Abstract]

> Prior NLCP approach "was not able to solve the full version of [3-player Kuhn poker] within 24 hours"; VBT bounds "lead to substantial computational improvements." [Source: arxiv:2606.25997 Abstract]

## Dead Ends

- Run Gurobi NLCP on dev.fun NLHE instance
- Replace MAFP/GARIP selfplay with exact 3-player Nash solver for arena submit
- Treat Kuhn poker VBT as proof of +EV on Playground fish pool

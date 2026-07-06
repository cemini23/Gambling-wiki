---
title: Ganzfried QP Nash equilibrium in multiplayer imperfect-info games (arXiv 2509.25618)
type: source
tags: [source, arxiv, poker, game-theory, nash, k148, ganzfried]
keywords: [quadratic-program, nlp, sequence-form, kuhn-poker, gambit, exact-ne]
related:
  - sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2509.25618-quadratic-programming-approach-for-nash-equilibr.pdf
phase_0_verdict: REFERENCE 2026-07-06 — Gambit suite comparison; no new FOSS solver repo; exact NE via QCQP complementarity
---

## Relations

- @sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md — NLCP + VBT exact path (K131)
- @sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md — scalable PED approximate path (K134)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2509.25618](https://arxiv.org/abs/2509.25618) |
| **Author** | Sam Ganzfried (Ganzfried Research) |
| **Verdict** | **REFERENCE** — exact multiplayer imperfect-info NE via quadratically-constrained program |

## Narrative

Extends Ganzfried's exact NE line: solves a **QCQP** from sequence-form **nonlinear complementarity** for multiplayer imperfect-information games. Demonstrated on **three-player Kuhn poker** (dominated actions removed) — faster than Gambit logit quantal response (which is approximate).

| Implication | Arena / wiki |
|-------------|--------------|
| CFR/FP **no NE guarantee** in multiplayer | Confirms K134 exploitability literacy |
| Exact NE tractable only on toy games | `--gate` selfplay ≠ ε(σ) certificate at scale |
| QCQP vs NLCP+VBT | Alternative exact solver family in same author stack |

**NO-GO:** Deploy QP solver inside prod `decide()` timeline.

## Snippets

> "Counterfactual regret minimization and fictitious play … do not guarantee convergence to Nash equilibrium in multiplayer games." [Source: arxiv:2509.25618 §1]

## Dead Ends

- Three-player Kuhn NE as HU sandbox qualification metric
- Gambit logit response as Playground exploitability proxy

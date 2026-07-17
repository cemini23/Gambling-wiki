---
title: Play-adequacy vs prediction-accuracy in LLM Code World Models (arXiv 2607.14169)
type: source
tags: [source, arxiv, poker, agents, world-models, eval, k158]
keywords: [code-world-model, play-adequacy, verified-vs-correct, danger-law, kuhn, leduc, mcts]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/custom-agent-methodology.md
  - entities/tools/rlcard.md
  - entities/tools/code-world-models.md
  - sources/brief-k158-play-adequacy-cwm-steals-2026-07-17.md
  - sources/daily-digest-batch-k158-2026-07-17.md
  - sweeps/2026-07-17-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-17
updated: 2026-07-17
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.14169-when-a-verified-world-model-still-loses-play-ade.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-17 — JaviMaligno/code-world-models ~4.8MB; no SPDX LICENSE; play-adequacy methodology Adopt
---

## Relations

- @entities/tools/code-world-models.md — Phase-0 FOSS
- @concepts/poker-hl-analyst-loop.md — play gates over transition accuracy
- @concepts/opponent-modeling-imperfect-info.md — Kuhn/Leduc inference-function gap
- @entities/tools/rlcard.md — Leduc/Kuhn sim lane

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.14169](https://arxiv.org/abs/2607.14169) |
| **Author** | Javier Aguilar Martín (AGILabs) |
| **Repo** | https://github.com/JaviMaligno/code-world-models |
| **Verdict** | **CONDITIONAL-GO** — play-adequacy eval for LLM-synthesized Code World Models (CWM) |

## Narrative

LLM synthesizes game rules as executable **Code World Models**; classical MCTS plans over them. Standard acceptance is high **transition accuracy** on sampled trajectories. Paper shows this is the wrong adequacy notion for planning.

**Verified-vs-correct gap:** a CWM can hit 100% transition accuracy and ≥98% state accuracy on the planner-visited distribution yet lose systematically — the <1% error is exactly the pivotal dynamics. Isolated play cost ≈0.091 (95% CI [0.065, 0.117], n=4800).

**Danger law:** `danger = play_cost × (1 − rarity)^N` where rarity = P(random play triggers omitted rule) and N = gate sample size. Exact Bernoulli gate-miss factor; predicts when sampling verification is blind.

**Synthesis = rule translation, not inference:** more on-manifold examples (incl. DAgger variants) do not repair omitted rules across GPT-5.x regimes tested.

**Imperfect information:** same mechanism on belief/`infer_states` functions. Kuhn covered at deployed gate; Leduc coverage bound certifies sampled competent-relevant info-sets only. Beacon witness: gate-passing wrong inference → 0.000 win rate vs 0.500 fair baseline.

| Lane | Fit |
|------|-----|
| **Poker HL / sandbox** | **HIGH** — gate on play / search-distribution adequacy, not transition accuracy alone |
| **Custom-agent P5 / CCC** | **HIGH** — verified harness fixtures can still lose at play |
| **RLCard / Kuhn-Leduc** | **MEDIUM** — imperfect-info inference coverage bounds |
| **David / DFS** | LOW |

## Snippets

> "An LLM-synthesized CWM can pass a sampling gate at 100% transition accuracy and be ≥98% state-accurate on the distribution the planner actually visits, yet lose systematically at play." [Source: arxiv:2607.14169 Abstract]

> "Adequacy for LLM-synthesized world models used in planning should be measured on the search distribution or by play directly, not by prediction accuracy on sampled transitions." [Source: arxiv:2607.14169 Abstract]

## Dead Ends

- Treating transition-accuracy 1.0 as Arena ship gate
- Expecting more example hands alone to teach omitted pivotal rules
- Shipping CWM+MCTS as runtime `decide()` (offline research / P3 only)

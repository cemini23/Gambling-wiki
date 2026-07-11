---
title: Gold-standard lightweight game agent — expert yardstick eval (arXiv 2607.06854)
type: source
tags: [source, arxiv, poker, rl, opponent-modeling, k152, leduc]
keywords: [expert-yardstick, gin-rummy, leduc-holdem, trpo, curriculum, nfsp, ismcts, pettingzoo]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/tools/adversarial-coevolution.md
  - entities/tools/rlcard.md
  - sources/arxiv-2607.01498-policy-representation-ssl-poker-2026-07-07.md
  - sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md
  - sources/daily-digest-batch-k152-2026-07-11.md
  - sweeps/2026-07-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-11
updated: 2026-07-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.06854-a-gold-standard-study-of-what-makes-a-lightweigh.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-11 — github.com/Nikelroid/adversarial-coevolution (2★, no LICENSE); expert-yardstick + Leduc methodology
---

## Relations

- @entities/tools/adversarial-coevolution.md — released pipeline (Phase-0)
- @entities/tools/rlcard.md — Leduc baseline env (K130)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.06854](https://arxiv.org/abs/2607.06854) |
| **Repo** | [github.com/Nikelroid/adversarial-coevolution](https://github.com/Nikelroid/adversarial-coevolution) |
| **Phase-0** | **No LICENSE** (gh api 2026-07-11); 2★; active Jul 2026 |
| **Verdict** | **CONDITIONAL-GO** — game-agnostic lightweight RL recipe + fixed expert yardstick |

## Narrative

**Problem:** imperfect-info RL agents beat random >99% but only tie self-play copies — weak eval signal.

**Method:** build a **fixed rule-based expert** (Gin Rummy meld solver) used **only for grading**, never training. Expert beats all trained agents 70–99%. 100+ ablations isolate what helps lightweight agents.

| Helps | Hurts / neutral |
|-------|-----------------|
| Trust-region (TRPO/PPO), targeted reward | Short/long reward shaping |
| Opponent curriculum, warm start, keep-best | Learned state embeddings |
| Stacking above lifts self-play champ ~30%→~36% vs expert | DAgger, live LLM opponent (slow/heavy) |

Encoder sweep (MLP/CNN/set/attention/RNN): **extra capacity barely moves needle** — ceiling is information, not width.

**Leduc Hold'em:** tabular learner vs computable optimum reaches near parity — recipe transfers beyond Gin.

Baselines: **NFSP**, **ISMCTS**. Released PettingZoo-agnostic `coev` package.

| Lane | Fit |
|------|-----|
| **Arena HU sandbox** | **HIGH** — yardstick eval > self-play Elo for regression gates |
| **NLHE prod `decide()`** | LOW — Gin/Leduc methodology only |
| **RLCard** | MEDIUM — Leduc cross-check path |

**Adoption for David:** grade sandbox bots vs a **fixed strong opponent/exploit set**, not self-play win rate alone; steal curriculum + keep-best harness ideas; **no repo fork until LICENSE**.

## Snippets

> "They beat a random opponent over 99 percent of the time and only tie copies of themselves." [Source: arxiv:2607.06854 Abstract]

> "Stacking them lifts a self-play champion from about 30 to 36 percent against the expert." [Source: arxiv:2607.06854 Abstract]

## Dead Ends

- Self-play champion as sole HU sandbox promotion metric
- Live 7B LLM opponent in training loop at arena scale

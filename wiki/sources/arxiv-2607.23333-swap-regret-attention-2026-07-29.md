---
title: Training with (Swap) Regret Loss in Single-Layer Attention (arXiv 2607.23333)
type: source
tags: [source, arxiv, game-theory, regret, fictitious-play, poker, k163]
keywords: [swap-regret, smoothed-fictitious-play, self-attention, blum-mansour, correlated-equilibrium, cce]
related:
  - meta/daily-research-digest-cadence.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md
  - sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md
  - sources/daily-digest-batch-k163-2026-07-29.md
  - sweeps/2026-07-29-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-29
updated: 2026-07-29
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.23333-training-with-swap-regret-loss-in-a-single-layer.pdf
phase_0_verdict: REFERENCE 2026-07-29 — paper-only theory; no FOSS; OSINT K198 already shelved arena docs
---

## Relations

- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — discrete LLM MAFP (adjacent FP family)
- @sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md — continuous FP convergence shelf (K157)
- @sources/arxiv-2607.07078-forgetting-factor-regret-zero-sum-2026-07-11.md — regret-metric family (K152)
- @concepts/opponent-modeling-imperfect-info.md — FP / equilibrium-seeking motif
- @concepts/poker-hl-analyst-loop.md — offline theory shelf; not decide() runtime
- @osint-wiki/concepts/swap-regret-attention-fictitious-play.md — OSINT K198 concept (already shipped)
- @osint-wiki/sources/arxiv-2607.23333-swap-regret-attention.md — OSINT source twin

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.23333](https://arxiv.org/abs/2607.23333) |
| **Authors** | Chanwoo Park, Asuman Ozdaglar (MIT EECS) |
| **FOSS** | None (AutoGPT cite only) |
| **Phase-0** | Paper-only — no Adopt candidate |
| **Verdict** | **REFERENCE** — regret-trained single-layer attention recovers smoothed fictitious play / Blum–Mansour swap-regret updates |

## Narrative

Park & Ozdaglar revisit **regret loss** on **probability-simplex** policies. A stationary point of single-layer linear self-attention trained with external regret loss matches **smoothed fictitious play** with stepsize $\tilde\Theta(1/\sqrt{T})$. They introduce a **swap-regret loss**; multi-head attention admits a stationary point whose forward pass implements **Blum–Mansour** no-swap-regret (each head = external-regret smoothed FP). Deployment implications: external-regret dynamics → **CCE**; swap-regret → **CE**.

Fetched via gambling digest `poker-mafp-arxiv` cluster. OSINT already ingested 2026-07-28 as **K198** (concept + arena `references/swap-regret-training-notes.md`); this page is the **gambling-wiki** twin for MAFP / HL reading list.

| Lane | Fit |
|------|-----|
| **MAFP / FP literature shelf** | **MEDIUM** — differentiable FP / CE-seeking story next to K124 MAFP |
| **Poker HL / decide()** | **NONE runtime** — one-layer linear attention + full-info Gaussian losses ≠ NLHE; advisory training-objective notes only (K198 already shipped) |
| **CeminiDFS / TipDrop / Atto / prod** | **NONE** |

## Snippets

> "regret-trained attention can realize differentiable mechanisms whose deployment induces equilibrium behavior in games: external-regret dynamics lead to coarse correlated equilibrium, while swap-regret dynamics lead to correlated equilibrium." [Source: arxiv:2607.23333 Abstract]

> "a single-layer self-attention model trained with regret loss admits a stationary point whose forward-pass exactly matches smoothed fictitious play" [Source: arxiv:2607.23333 Abstract]

## Dead Ends

- Importing one-layer attention stationary points into live `decide()` without sandbox gates
- Treating swap-regret loss as a Playground submit gate this cycle (K198: advisory docs only)
- FOSS adopt — none shipped with the paper

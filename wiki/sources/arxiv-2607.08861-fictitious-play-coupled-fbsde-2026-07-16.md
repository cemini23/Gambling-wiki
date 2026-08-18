---
title: Convergence of fictitious play for fully coupled FBSDEs (arXiv 2607.08861)
type: source
tags: [source, arxiv, game-theory, fictitious-play, math, k157]
keywords: [fbsde, fictitious-play, stochastic-differential-games, deep-fictitious-play, nash]
related:
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/custom-agent-methodology.md
  - sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md
  - sources/daily-digest-batch-k157-2026-07-16.md
  - sweeps/2026-07-16-daily.md
  - sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
maturity: draft
read_status: skimmed
created: 2026-07-16
updated: 2026-08-18
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.08861-convergence-of-fictitious-play-for-fully-coupled.pdf
phase_0_verdict: REFERENCE 2026-07-16 — continuous SDG/FBSDE theory; no FOSS; rates do not transfer to discrete NLHE MAFP
---

## Relations

- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — discrete LLM MAFP (adjacent FP family)
- @concepts/opponent-modeling-imperfect-info.md — FP as equilibrium-seeking motif
- @sources/arxiv-2607.23333-swap-regret-attention-2026-07-29.md — attention ≡ smoothed FP shelf (K163)
- @sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md — another continuous FP shelf (K167 SFP-MFG)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08861](https://arxiv.org/abs/2607.08861) |
| **Authors** | Andersson, Andersson, Ljung (Saab / Chalmers / Verona) |
| **FOSS** | None |
| **Verdict** | **REFERENCE** — first geometric (and under extra structure super-exponential) convergence analysis of fictitious play for **fully coupled** Nash FBSDE systems |

## Narrative

Extends Han–Hu–Long (2022) deep-fictitious-play theory from **decoupled** forward processes to **fully coupled** FBSDEs for finite-player non-zero-sum stochastic differential games. Numerical LQ interbank borrowing/lending (N=2 and N=20) shows clear exponential error decay to machine precision.

| Lane | Fit |
|------|-----|
| **MAFP / FP literature shelf** | **LOW–MEDIUM** — strengthens continuous-time FP theory adjacent to arena MAFP steals |
| **Poker HL / decide()** | **NONE** — continuous SDG ≠ discrete NLHE; rates do not transfer |
| **Prod harness / David / DFS** | **NONE** |

Paper domains: interbank systemic risk, oligopoly, pursuit-evasion, missile guidance — not wagering platforms.

## Snippets

> "To the best of our knowledge, this provides the first convergence analysis of fictitious play for fully coupled FBSDEs." [Source: arxiv:2607.08861 Abstract]

> "A numerical experiment with a linear-quadratic interbank borrowing and lending problem confirms the geometric convergence." [Source: arxiv:2607.08861 Abstract]

## Dead Ends

- Importing geometric/super-exponential rates into sandbox MAFP iteration budgets
- Deep BSDE / FBSDE solvers as poker decide() substrate
- Interbank LQ game as Kalshi/PM model

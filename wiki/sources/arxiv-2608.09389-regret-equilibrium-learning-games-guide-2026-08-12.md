---
title: "Regret, equilibrium, and learning in games: A guided tour (arXiv 2608.09389)"
type: source
tags: [source, arxiv, game-theory, regret, ftrl, fictitious-play, k166]
keywords: [mertikopoulos, regret, nash-equilibrium, follow-the-regularized-leader, hedge, exp3, tsallis-inf, fictitious-play, brown-robinson, folk-theorem, adversarial-bandit, gap-function, ergodic-convergence]
related:
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-12-daily.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md
  - sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md
  - sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md
  - sources/daily-digest-batch-k166-2026-08-12.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
maturity: draft
read_status: skimmed
created: 2026-08-12
updated: 2026-08-12
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2608.09389-regret-equilibrium-and-learning-in-games-a-guide.pdf
phase_0_verdict: REFERENCE 2026-08-12 — FTRL/Hedge/FP literacy shelf (Mertikopoulos survey chapter); no FOSS; decide() NO-GO
wire_status: wont_wire
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — regret/FTRL machinery underpins FP/MAFP equilibrium-seeking lane
- @concepts/poker-hl-analyst-loop.md — theory shelf only; no HL loop import
- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — MAFP best-response-to-history is a regularized-FP instance
- @sources/brief-k163-swap-regret-attention-shelf-2026-07-29.md — smoothed FP / attention regret shelf (K163)
- @sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md — continuous FP convergence shelf (K157)
- @sources/brief-k152-expert-yardstick-forgetting-regret-steals-2026-07-11.md — forgetting-factor regret shelf (K152)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2608.09389](https://arxiv.org/abs/2608.09389) |
| **Authors** | Panayotis Mertikopoulos (Univ. Grenoble Alpes, CNRS, Inria) |
| **Type** | Book chapter / guided tour (not a comprehensive survey) — indebted to Sorin & von Stengel |
| **FOSS** | None published |
| **Phase-0** | **REFERENCE** — FTRL / Hedge / FP literacy shelf |
| **Wire** | `wont_wire` — no runtime algorithm import |

## Narrative

Single-author guided tour of learning-in-games structured around two viewpoints: (1) a **single agent** minimizing regret against an arbitrary (adversarial, non-stationary) sequence — the adversarial multi-armed bandit (AdvMAB) setting; (2) a **multi-agent** setting where several players repeatedly play a game, myopically adjusting to each other. Both are unified under **regularized learning**: best-respond to the past history of play up to a regularization penalty that encourages exploration and prevents over-commitment.

The regularized-learning template contains Hedge / exponential / multiplicative weights, **EXP3**, **Tsallis-INF**, and FTRL as special cases, and covers both **oracle** (full payoff-vector) and **payoff-based / bandit** feedback via a unified black-box payoff model.

Key anchors for the wiki:

- **Brown–Robinson fictitious play (Thm 1):** for two-player zero-sum games, the time-average of FP play converges to the set of NE from any initialization. Proof via the **gap function** `Gap(x) = max_p2 ℓ(x1,p2) − min_p1 ℓ(p1,x2)`, which is ≥0 with equality iff NE; continuous-time best-response dynamics make the gap decay geometrically (`Gap(z(t)) = Gap(z(0)) e^(−t)`).
- **Hedge (Ex. 4.3):** the most widely used regularizer is negative entropy → Hedge / exponential weights.
- **Ergodic convergence bound for zero-sum games (Thm 4):** under FTRL with step-size parameters, the ergodic average `x̄_T` satisfies `E[Gap(x̄_T)] ≤ (2H + 2N Σ γt Bt + (2K)^{-1} Σ γt² M²_t) / Σ γt = Õ(T^{−min{1−p,β,p−2µ}})` — sublinear gap, with the NE-only benchmark "no-regret ⇒ Nash in zero-sum" made quantitative.
- **Folk theorem of regularized learning (Thm 5):** (P1) if play converges to x* with positive probability, x* is a Nash equilibrium; (P2) if x* is stochastically stable, it is a Nash equilibrium; (P3) strict NE are stochastically asymptotically stable. Requires a **consistency** condition on the choice map — satisfied by logit and any decomposable regularizer with `θ'(z) → −∞` as `z → 0+` (Tsallis too), but **not** the Euclidean regularizer.
- **Single-agent regret:** O(√T) regret bounds for FTRL under full information; partial-information (bandit) analogues.
- **Caveats:** explicitly NOT a survey — omits Hannan-consistency / CCE, regret-matching à la Hart–Mas-Colell, calibration à la Foster–Vohra, trial-and-error learning, and most continuous-time / stochastic-approximation results. PPAD-completeness of NE and the Hart–Mas-Colell impossibility ("no uncoupled dynamics reach NE in all games") frame why the field studies *classes* of games.

### Lane fit

| Lane | Fit |
|------|-----|
| **FTRL / Hedge / FP literacy** | **REFERENCE** — canonical unified treatment; shelf next to K163/K157/K152 |
| **Arena `decide()` / HL loop** | **NO-GO** — tutorial chapter; no algorithm to wire |
| **Atto / GuruWatcher / CeminiDFS / prod scp** | **NONE** |

## Snippets

> "The goal then becomes to characterize the players' long-run behavior under a given learning policy—and, in particular, whether it leads to equilibrium (and in what sense)." [Source: arxiv:2608.09389 p.2]

> "There are no uncoupled dynamics that lead to Nash equilibrium in all games." (Hart & Mas-Colell, quoted) [Source: arxiv:2608.09389 p.2]

> Theorem 4 — zero-sum ergodic bound: `E[Gap(x̄_T)] ≤ (2H + 2N Σ_t γ_t B_t + (2K)^{-1} Σ_t γ_t² M_t²) / Σ_t γ_t = Õ(T^{−min{1−p, β, p−2µ}})` [Source: arxiv:2608.09389 p.31]

> Theorem 5 — folk theorem (P1)–(P3): convergence-with-positive-probability ⇒ NE; stochastic stability ⇒ NE; strict NE ⇒ stochastically asymptotically stable. [Source: arxiv:2608.09389 p.34]

## Dead Ends

- Importing any single algorithm from this chapter directly into `decide()` — the chapter is a literacy/unification tour, not a drop-in method
- Reading it as a comprehensive survey of online learning (author explicitly disclaims coverage)
- FOSS adopt — no author code accompanies the chapter

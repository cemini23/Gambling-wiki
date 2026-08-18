---
title: "Self-fictitious-play for Potential Monotone Ergodic Mean-field Games (arXiv 2608.15258)"
type: source
tags: [source, arxiv, game-theory, fictitious-play, mean-field, k167]
keywords: [self-fictitious-play, sfp, mean-field-games, ergodic, lasry-lions, occupation-measure, wasserstein, bai, lauriere]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md
  - sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
  - sources/daily-digest-batch-k166-2026-08-12.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-08-18-daily.md
  - sources/daily-digest-batch-k167-2026-08-18.md
  - sources/brief-k167-sfp-mfg-shelf-2026-08-18.md
maturity: draft
read_status: skimmed
created: 2026-08-18
updated: 2026-08-18
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2608.15258-self-fictitious-play-for-potential-monotone-ergo.pdf
phase_0_verdict: REFERENCE 2026-08-18 — ergodic MFG SFP theory shelf; no FOSS; decide() NO-GO
wire_status: wont_wire
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — continuous SFP-MFG shelf next to MAFP / K157 / K166; not a villain HUD
- @concepts/poker-hl-analyst-loop.md — theory shelf only; no HL import
- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — discrete LLM MAFP (different object)
- @sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md — continuous FP convergence shelf (K157)
- @sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md — do not retune discrete MAFP from continuous rates
- @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md — FTRL/FP literacy sibling (K166)
- @sources/brief-k166-regret-learning-games-shelf-2026-08-12.md — prior FP literacy shelf
- @sources/daily-digest-batch-k167-2026-08-18.md — digest batch (1 REFERENCE)
- @sources/brief-k167-sfp-mfg-shelf-2026-08-18.md — operator shelf brief

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2608.15258](https://arxiv.org/abs/2608.15258) |
| **Authors** | Yupeng Bai (Univ. Evry Paris-Saclay), Mathieu Laurière (NYU Shanghai), Zhenjie Ren (Univ. Evry Paris-Saclay), Songbo Wang (Univ. Côte d’Azur) |
| **Type** | math.OC — continuous-time ergodic MFG learning |
| **FOSS** | None published (GitHub search 0 repos; PDF has no code URL; acknowledgements list NYU Shanghai affiliation only) |
| **Phase-0** | **REFERENCE** — SFP theory shelf next to K157 FBSDE-FP / K166 FTRL-FP / K124 MAFP |
| **Wire** | `wont_wire` — no ADOPT-GO runtime |

## Narrative

Long-time learning in **ergodic, potential, monotone** mean-field games via **self-fictitious-play (SFP)**. The state follows the optimal feedback for the current belief; the belief is **not** the population McKean–Vlasov law `m_t = Law(X_t)`. It is updated from the player’s **own empirical occupation measure**.

On the torus `T^d`, SFP is contractive and admits a unique invariant law `ρ_λ`. Wasserstein distance from that law to the MFG Nash `m*` goes to a neighborhood of order **O(√λ)** in the belief-update rate. The linear-quadratic example (§4.1) shows the rate is **sharp**; numerics illustrate the scaling.

Proof ingredients (not entropy / gradient arguments): uniform-in-time ergodic HJB regularity + Lasry–Lions divergence energy + reflection coupling.

Related work cites Perrin et al. NeurIPS 2020 “Fictitious play for mean field games” — that is **population** fictitious play, not this self-interacting occupation-measure scheme.

**Do not** retune discrete MAFP / `decide()` from these rates (same posture as K157). Continuous-time torus MFG ≠ discrete HU poker.

### Lane fit

| Lane | Fit |
|------|-----|
| **SFP / ergodic MFG literacy** | **REFERENCE** — shelf next to K157 / K166 / K124 |
| **Arena `decide()` / HL loop** | **NO-GO** — continuous MFG, not discrete HU MAFP |
| **Atto / GuruWatcher / CeminiDFS / prod scp** | **NONE** |

## Snippets

> "At each time, the state follows the optimal feedback associated with the current belief, while the belief is updated using the player's own empirical occupation measure rather than the population distribution. For ergodic monotone potential MFGs on the torus, we prove that the SFP dynamics is contractive and admits a unique invariant law. Moreover, we show that this invariant law is quantitatively close to the MFG Nash equilibrium, with an error of order equal to the square root of the belief-update rate." [Source: arxiv:2608.15258 abstract]

> SFP (vs McKean–Vlasov `m_t = Law(X_t)`): `d X_t = H_p(X_t, ∇u_{m_t}(X_t)) dt + √2 dW_t`, `d m_t = λ (δ_{X_t} − m_t) dt`. Wasserstein distance to MFG Nash `m*` → neighborhood `O(√λ)`. LQ §4.1: rate sharp. [Source: arxiv:2608.15258 pp.3–4]

> "we combine reflection coupling with the Lasry–Lions divergence … to derive Wasserstein contractivity" — entropy/gradient arguments for Langevin-type systems do not apply. [Source: arxiv:2608.15258 p.4]

## Dead Ends

- Importing `O(√λ)` / contractivity rates into discrete MAFP or `decide()` — continuous torus MFG ≠ HU poker
- Treating Perrin et al. 2020 population FP as this paper’s SFP scheme
- FOSS adopt — no accompanying code

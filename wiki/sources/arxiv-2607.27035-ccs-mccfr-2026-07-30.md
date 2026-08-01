---
title: Correlated Chance Sampling for MCCFR (arXiv 2607.27035)
type: source
tags: [source, arxiv, poker, game-theory, mccfr, cfr, k164]
keywords: [ccs-mccfr, correlated-chance-sampling, external-sampling, leduc, kuhn, openspiel, exploitability, linear-cfr]
related:
  - meta/daily-research-digest-cadence.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/poker-bot-tooling.md
  - entities/tools/rlcard.md
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md
  - sources/brief-k164-ccs-mccfr-chance-sampling-steals-2026-07-30.md
  - sources/daily-digest-batch-k164-2026-07-30.md
  - sweeps/2026-07-30-daily.md
  - sources/arxiv-2607-28520-cs-rnr-safe-opponent-exploitation.md
maturity: draft
read_status: skimmed
created: 2026-07-30
updated: 2026-08-01
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.27035-correlated-chance-sampling-for-monte-carlo-count.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-30 — paper-only algorithm steal for offline MCCFR/OpenSpiel research; no FOSS; decide() NO-GO
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — equilibrium / exploitability research lane @sources/arxiv-2607-28520-cs-rnr-safe-opponent-exploitation.md
- @concepts/poker-hl-analyst-loop.md — offline blueprint / solver hygiene (not runtime decide)
- @entities/bots/poker-bot-tooling.md — OpenSpiel / tabular poker tooling shelf
- @entities/tools/rlcard.md — Kuhn/Leduc research sims adjacent
- @sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md — approximate NE / FP-PED lineage
- @sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md — OpenSpiel exploitability ladder pattern (K134)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.27035](https://arxiv.org/abs/2607.27035) |
| **Authors** | Boning Li, Yu Chen, Longbo Huang (Tsinghua IIIS) |
| **FOSS** | None published (experiments use OpenSpiel exact exploitability) |
| **Phase-0** | Paper-only — reimplementation notes; no Adopt clone |
| **Verdict** | **CONDITIONAL-GO** — drop-in **CCS** chance sampler for External Sampling MCCFR |

## Narrative

Standard MCCFR redraws chance outcomes **i.i.d.** on every visit to a concrete chance node. **CCS-MCCFR** assigns each concrete chance node a **persistent randomized Weyl stream**, mapping phases through the node’s chance distribution. Fixed-index draws keep correct marginals; first $N$ draws at one node get deterministic local frequency error $O(\log(N+1)/N)$ vs $O(N^{-1/2})$ i.i.d. scale. Unbiased along fixed strategy trajectories; per-traversal reset retains standard $O(1/\sqrt{T})$ External Sampling guarantee.

**Empirics (paired, OpenSpiel exploitability):** Kuhn −27.64%; standard Leduc −24.59%; controlled 6/10/12-card Leduc −27.65% / −34.01% / −19.05% (all CIs > 0); Goofspiel-4 −4.27%. Gain survives 3M Leduc node touches. **Linear CFR + CCS** = lowest cell in update×sampler grid (−42.59% vs vanilla+i.i.d.). Boundary / muted: Liar’s Dice, reduced Flop Hold’em, Libratus turn/river endgames (CIs cross zero).

Fetched via `poker-exploit-arxiv` — legitimate imperfect-info poker solver hit.

| Lane | Fit |
|------|-----|
| **Offline MCCFR / OpenSpiel / TexasSolver research** | **CONDITIONAL-GO** — one-line chance-sampler change; no new hyperparameters; no time overhead claimed |
| **Arena `decide()` / Playground** | **NO-GO** — offline equilibrium computation ≠ hand-time policy |
| **CeminiDFS / Atto / TipDrop / prod scp** | **NONE** |

## Snippets

> "CCS-MCCFR turns a one-line change to the chance sampler into explicit local guarantees and large exploitability reductions across tabular poker." [Source: arxiv:2607.27035 Abstract]

> "The gain survives to 3M Leduc node touches and combines with Linear CFR to reach the lowest measured exploitability." [Source: arxiv:2607.27035 Abstract]

## Dead Ends

- Expecting CCS gains on HUNL endgames / full NLHE without re-measurement (paper’s boundary tests muted)
- Wiring CCS into live `decide()` instead of offline blueprint / MCCFR research branch
- FOSS adopt — no author repo shipped with the paper

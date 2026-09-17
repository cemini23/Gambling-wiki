---
title: "FP tie-breaking rules in symmetric first-price auctions (arXiv 2609.18848)"
type: source
tags: [source, arxiv, game-theory, fictitious-play, auctions, k171]
keywords: [fictitious-play, tie-breaking, first-price-auction, bayes-nash, limit-cycle, heymann]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
  - sources/daily-digest-batch-k171-2026-09-17.md
  - sources/brief-k171-pm-fp-regulatory-2026-09-17.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-09-17-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-17
updated: 2026-09-17
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2609.18848-on-the-role-of-tie-breaking-rules-in-the-converg.pdf
phase_0_verdict: REFERENCE 2026-09-17 — FP convergence depends on tie-breaking; BenHey/FP4FPA NO-GO
wire_status: policy_wired
---

## Relations

- @concepts/poker-hl-analyst-loop.md — FP literacy shelf; no decide() import
- @concepts/opponent-modeling-imperfect-info.md — FP convergence mechanics
- @sources/arxiv-2608.09389-regret-equilibrium-learning-games-guide-2026-08-12.md — K166 FP/FTRL literacy sibling
- @sources/daily-digest-batch-k171-2026-09-17.md — digest batch
- @sources/brief-k171-pm-fp-regulatory-2026-09-17.md — operator brief

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2609.18848](https://arxiv.org/abs/2609.18848) |
| **Author** | Benjamin Heymann (Criteo AI Lab / FairPlay) |
| **Type** | cs.GT — fictitious play in first-price auctions |
| **FOSS** | [BenHey/FP4FPA](https://github.com/BenHey/FP4FPA) — **NO-GO** (no SPDX license on GitHub 2026-09-17) |
| **Phase-0** | **REFERENCE** — tie-breaking is part of the game; FP may cycle without zero-payoff ties |
| **Wire** | `policy_wired` — poker-hl FP convergence hygiene bullet |

## Narrative

Continuous-time **fictitious play** in 2-bidder symmetric first-price auctions with discrete values and discrete bids.

**Counterexample:** minimal 2×2×3 instance — standard **uniform-split tie-breaking** yields a **stable limit cycle** far from symmetric Bayes–Nash; equilibrium is unstable.

**Fix:** award **zero payoff to all bidders on ties** — FP converges to a Nash equilibrium of the modified game, which is an **ε-equilibrium** of the original auction in a broad parameter range.

Motivation includes display-ad first-price auction migration (Paes Leme et al. 2020). Complements empirical FP4FPA work (Heymann & Mertikopoulos 2025).

**Arena posture:** literacy for MAFP/FP regression design — tie-handling and belief-update rules are not implementation details. **No decide() import.** Do not clone `BenHey/FP4FPA` without license.

### Lane fit

| Lane | Fit |
|------|-----|
| **FP / MAFP literacy** | **REFERENCE** — shelf next to K166/K167 |
| **Arena `decide()`** | **NO-GO** — auction theory, not HU poker |
| **Prod scp / bots** | **NONE** |

## Snippets

> "Fictitious play with the standard uniform-split tie-breaking rule does not converge to the symmetric Bayes–Nash equilibrium … the dynamics converge to a stable limit cycle far from the Nash equilibrium." [Source: arxiv:2609.18848 abstract]

> "Awarding a payoff of zero to every bidder in case of a tie … restores convergence: fictitious play converges to a Nash equilibrium of the modified game." [Source: arxiv:2609.18848 abstract]

## Dead Ends

- Cloning `BenHey/FP4FPA` — no license file
- Assuming FP always converges in discrete-action games without tie-rule audit

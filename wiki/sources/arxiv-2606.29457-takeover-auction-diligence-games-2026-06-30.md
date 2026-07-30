---
title: Takeover auction diligence games — imperfect-info solver benchmark (arXiv 2606.29457)
type: source
tags: [source, arxiv, game-theory, auctions, exploitability, k134, openspiel]
keywords: [due-diligence, takeover-auction, openspiel, cfr, ppo, exploitability, imperfect-information]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/gambling-bot-architecture.md
  - entities/bots/poker-bot-tooling.md
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md
  - sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md
  - sources/daily-digest-batch-k134-2026-06-30.md
  - sweeps/2026-06-30-daily.md
  - sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
maturity: draft
read_status: skimmed
created: 2026-06-30
updated: 2026-07-30
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.29457-pdf-how-much-due-diligence-before-you-bid-learni.pdf
phase_0_verdict: CONDITIONAL-GO 2026-06-30 — MIT github.com/zainnab-sparq/imperfect-information-deal-games (0★); OpenSpiel M&A games + exploitability ladder
---

## Relations

- @sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md — FP/CFR vs refinement hybrids (K134 batch)
- @entities/bots/poker-bot-tooling.md — OpenSpiel / RL sim research lane
- @sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md — K134 operator steals
- @sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md — CCS-MCCFR OpenSpiel poker eval sibling (K164)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.29457](https://arxiv.org/abs/2606.29457) |
| **Title** | How Much Due Diligence Before You Bid? Learning in Intractable Takeover Auctions |
| **Author** | Zain Naboulsi (Sparq) |
| **Repo** | [github.com/zainnab-sparq/imperfect-information-deal-games](https://github.com/zainnab-sparq/imperfect-information-deal-games) |
| **Phase-0** | **MIT** (gh api 2026-06-30); ~0★; OpenSpiel abstraction |
| **Verdict** | **CONDITIONAL-GO** — exploitability benchmarking pattern; **not** wagering-domain bot |

## Narrative

Models **M&A takeover bidding** as imperfect-information auction games (common-value winner's curse, toehold, independent-private-value variants) on **OpenSpiel**. Core economic question: optimal **due diligence** (costly private signals) vs strategy-space explosion.

Solver ladder on commodity CPU:

| Regime | Winners |
|--------|---------|
| **Tabular / small** | Exact solvers (**CFR, MMD, PSRO**) — lower exploitability, faster |
| **Large / intractable** | **PPO / PPG** policy-gradient learners — flat per-target cost; exploitability estimate as **lower bound** only |

Key insight: each diligence signal multiplies infosets — same lever governs economic value of information and computational intractability.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Poker bot research literacy** | **Medium** — exploitability ladder justifies heuristic `decide()` + selfplay gates vs exact Nash |
| **Sportsbook / DFS / PM bots** | NO-GO — M&A domain |
| **OpenSpiel tooling** | **CONDITIONAL-GO** — reusable imperfect-info benchmark harness pattern |
| **Arena exploitability audit** | Medium — learned-best-response ε floor methodology |

Phase-0 **CONDITIONAL-GO**: read MIT repo for exploitability benchmarking recipes; do not deploy for consumer wagering automation.

## Snippets

> "Wherever the game is small enough to tabulate, the exact solvers (CFR, MMD, PSRO) are both lower in exploitability and faster." [Source: arxiv:2606.29457 Abstract]

> "Each unit of diligence is another private signal, and each signal multiplies the strategy space." [Source: arxiv:2606.29457 Abstract]

> PPO and PPG drive a calibrated learned-best-response exploitability estimate to its resolution floor on games too large to enumerate — reported as a **lower bound**, not a Nash certificate. [Source: arxiv:2606.29457 Abstract]

## Dead Ends

- Takeover auction games as NLHE proxy
- PPO diligence model for FanDuel lineup generation
- Treat learned ε lower bound as arena TrueSkill certificate

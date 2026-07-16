---
title: Multi-Agent Fictitious Play for LLM decision-making (arXiv 2606.19308)
type: source
tags: [source, arxiv, poker, game-theory, multi-agent, k124, mafp]
keywords: [fictitious play, stance entanglement, Nash equilibrium, competitive games, negotiation, mafp]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/custom-agent-methodology.md
  - concepts/heads-up-arena-strategy.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/research-k122-poker-paper-landscape-2026-06-19.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/daily-digest-reject-cluster-k124-2026-06-21.md
  - sweeps/2026-06-21-daily.md
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md
maturity: draft
read_status: skimmed
created: 2026-06-21
updated: 2026-07-16
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.19308-enhancing-decision-making-with-large-language-mo.pdf
phase_0_verdict: REFERENCE 2026-06-21 — game-theoretic MAS for competitive decisions; runtime LLM NO-GO for decide()
---

## Relations

- @concepts/opponent-modeling-imperfect-info.md — fictitious play as equilibrium-seeking vs exploit HUD
- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — F6 multi-agent exploit research lane
- @sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md — operator steal summary (K124)
- @sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md — continuous SDG FP convergence shelf (K157)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.19308](https://arxiv.org/abs/2606.19308) |
| **Title** | Enhancing Decision-Making with LLMs through Multi-Agent Fictitious Play (MAFP) |
| **Authors** | Shen et al. (NUS) |
| **Phase-0** | No prod repo required; html/pdf on arXiv |
| **Verdict** | **REFERENCE** — offline research / P3 strategy design only |

## Narrative

MAFP targets **stance entanglement**: decisions where multiple stakeholders' choices are mutually dependent (negotiation, competitive games, markets) — distinct from divide-and-conquer execution MAS.

**Mechanism:** decompose stances into agents; each round best-responds to empirical mixture of others' past decisions (fictitious play); output = final empirical mixture. Evaluated on **13 scenarios** including competitive games and negotiation with **tournament strength** + **robustness** metrics.

### Relevance to dev.fun poker track

| Application | Fit |
|-------------|-----|
| **HU researcher TrueSkill** | Conceptual — equilibrium-seeking vs single-villain exploit |
| **Runtime `decide()`** | **NO-GO** — multi-round LLM MAS too slow; K118 dead-end |
| **Offline HL / P3** | REFERENCE for multi-stakeholder patch debates (style vs exploit vs axis) |
| **F6 session memory** | Analog: empirical mixture of villain past actions → HUD prior |

Steal pattern for pure-code bot: translate **best-response to empirical opponent mixture** into lightweight Python (freq buckets), not LLM fictitious play rounds.

## Snippets

> "A good decision maximizes payoff while exhibiting no exploitable weaknesses — meaning it lies in an equilibrium from which no stakeholder can improve through unilateral deviation." [Source: arxiv:2606.19308 §1]

> "MAFP outperforms both single-round and multi-round baselines on tournament strength and robustness across 13 scenarios." [Source: arxiv:2606.19308 abstract]

## Dead Ends

- **Runtime MAFP inside `decide()`** — latency + non-determinism
- **Treating MAFP as substitute for COM or AlphaExploitem** — different problem (stance entanglement vs repeated imperfect-info hands)

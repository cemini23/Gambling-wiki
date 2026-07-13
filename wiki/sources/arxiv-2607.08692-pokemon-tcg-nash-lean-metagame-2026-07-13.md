---
title: From rules to Nash equilibria — Pokémon TCG metagame Lean 4 case study (arXiv 2607.08692)
type: source
tags: [source, arxiv, game-theory, opponent-modeling, metagame, k154]
keywords: [nash-equilibrium, replicator-dynamics, lean-4, popularity-paradox, matchup-matrix]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/dfs-ownership-projection.md
  - concepts/pm-copy-trading-retail-risks.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k154-metagame-memory-search-steals-2026-07-13.md
  - sources/daily-digest-batch-k154-2026-07-13.md
  - sweeps/2026-07-13-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-13
updated: 2026-07-13
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.08692-from-rules-to-nash-equilibria-a-lean-4-case-stud.pdf
phase_0_verdict: REFERENCE 2026-07-13 — paper-only; machine-checked Nash on tournament matchup matrix (IEEE DataPort artifact)
---

## Relations

- @sources/brief-k154-metagame-memory-search-steals-2026-07-13.md — operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08692](https://arxiv.org/abs/2607.08692) |
| **Artifact** | IEEE DataPort [10.21227/vty8-p429](https://doi.org/10.21227/vty8-p429) |
| **Verdict** | **REFERENCE** — formal Nash/replicator metagame on **14-deck** Pokémon TCG matrix |

## Narrative

Machine-checked (Lean 4) analysis of competitive **Pokémon TCG** Trainer Hill data (Jan–Feb 2026, 50+ player events). 14 archetypes, full pairwise matchup matrix.

| Finding | Cross-lane analogy |
|---------|-------------------|
| **Popularity paradox** — Dragapult 15.5% share but 46.7% WR; Grimmsnarl 5.1% / 52.7% | Field **ownership ≠ EV** (DFS GPP, PM whale-copy) |
| Nash assigns **0%** to most-popular deck in raw game | Metagame share can be **strictly suboptimal** |
| Replicator dynamics + 10k bootstrap stability | League/MAFP opponent pool drift checks |

Methodological contribution: qualitative metagame narratives → **machine-checkable** game theory.

| Lane | Fit |
|------|-----|
| **Arena opponent league** | **MEDIUM** — Nash on matchup matrix methodology |
| **DFS ownership** | **MEDIUM** — popularity vs win-rate paradox |
| **Poker NLHE prod** | LOW — different game; steal method not deck list |

**Adoption for David:** when analyzing opponent archetype pools or DFS chalk, separate **field share** from **matchup EV / Nash weight**; consider formal equilibrium on estimated pairwise matrices.

## Snippets

> "The most played deck … has only 46.7% expected win rate, while Grimmsnarl … achieves 52.7%." [Source: arxiv:2607.08692 Abstract]

## Dead Ends

- Pokémon deck lists as NLHE `decide()` inputs
- Lean proofs as live arena deployment without matchup data pipeline

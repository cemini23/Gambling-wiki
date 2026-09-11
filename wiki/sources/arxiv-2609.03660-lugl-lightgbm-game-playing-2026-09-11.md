---
title: "LUGL — LightGBM game-playing via local updates / global learning (arXiv 2609.03660)"
type: source
tags: [source, arxiv, poker, rl, lightgbm, k170]
keywords: [lugl, lightgbm, deep-cfr, pokerrl, tabular, imperfect-information, flop5-holdem]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/opponent-modeling-imperfect-info.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
  - sources/daily-digest-batch-k170-2026-09-11.md
  - sources/brief-k170-week1-papers-rss-2026-09-11.md
  - meta/daily-research-digest-cadence.md
  - sweeps/2026-09-11-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-11
updated: 2026-09-11
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2609.03660-local-updates-global-learning-lugl-playing-games.pdf
phase_0_verdict: REFERENCE 2026-09-11 — LightGBM tabular RL shelf; MIT FOSS; decide() NO-GO
wire_status: policy_wired
---

## Relations

- @concepts/poker-hl-analyst-loop.md — theory shelf; no HL import
- @concepts/opponent-modeling-imperfect-info.md — tabular imperfect-info benchmark lane
- @sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md — continuous FP theory sibling (K167)
- @sources/daily-digest-batch-k170-2026-09-11.md — digest batch (3 REFERENCE)
- @sources/brief-k170-week1-papers-rss-2026-09-11.md — operator shelf brief

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2609.03660](https://arxiv.org/abs/2609.03660) |
| **Authors** | David Milec, Spyridon Samothrakis, Michael Fairbank, Dennis J.N.J. Soemers |
| **Type** | cs.AI — tabular RL / game playing |
| **FOSS** | [Deep-CFR-2025](https://github.com/milecdav/Deep-CFR-2025) MIT · [PokerRL-2025](https://github.com/milecdav/PokerRL-2025) MIT · [luglrl](https://github.com/ssamot/luglrl) MIT · [fil](https://github.com/ssamot/fil) **no SPDX license** |
| **Phase-0** | **REFERENCE** — LightGBM tabular game-playing shelf; clone MIT repos extract-only; `fil` NO-GO |
| **Wire** | `policy_wired` — poker-hl LightGBM/LUGL shelf bullet |

## Narrative

**LUGL (Local Updates, Global Learning)** decouples data collection from model fitting so **non-incremental** learners (gradient-boosted trees) can train in RL/self-play despite distributional shift.

Two phases alternate:

1. **Local updates** — self-play accumulates tabular targets (Q, V, policy, or regret) in a finite table.
2. **Global learning** — train a function approximator (LightGBM) on the table, generalize to unseen states, reset the table.

Tested on four perfect-information games (Tic-tac-toe, Connect-4, Othello, Hex) and five imperfect-information games (Kuhn poker, Leduc Hold'em, Liar's Dice, Goofspiel, **Flop5 Hold'em**). Results are competitive with or superior to DQN and DeepCFR on tested benchmarks.

**Retail / arena posture:** theory and benchmark shelf only. Do **not** import into live `decide()` or retune MAFP from tree-batch schedules. `ssamot/fil` has no license — do not clone into prod paths.

### Lane fit

| Lane | Fit |
|------|-----|
| **Poker arena research shelf** | **REFERENCE** — Flop5 / tabular imperfect-info benchmark |
| **Arena `decide()` / HL loop** | **NO-GO** — offline benchmark; no validated HU import |
| **Atto / GuruWatcher / CeminiDFS / prod scp** | **NONE** |

## Snippets

> "Game states are inherently tabular—discrete actions, categorical card identities, structured board positions—which makes them an ideal candidate for tree-based methods." [Source: arxiv:2609.03660 abstract]

> LUGL alternates local self-play tabular accumulation with a global LightGBM fit that generalizes before the table resets; competitive with or superior to DQN and DeepCFR across nine tested games including Flop5 Hold'em. [Source: arxiv:2609.03660 §I]

## Dead Ends

- Cloning `ssamot/fil` — no SPDX license on GitHub (2026-09-11)
- Treating LightGBM batch retrain as a drop-in `decide()` patch without Flop5/HU validation

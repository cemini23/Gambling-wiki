---
title: K127 — EMAgnet self-play + IRumAI + SETE steals
type: source
tags: [source, brief, poker, casino, self-play, k127]
keywords: [emagnet, irumai, sete, self-play, indian-rummy, moving-magnet, garip]
related:
  - sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md
  - sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md
  - sources/arxiv-2606.20960-equilibrium-internal-transfers-2026-06-24.md
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/heads-up-arena-strategy.md
  - entities/games/indian-rummy.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/daily-digest-reject-cluster-k127-2026-06-24.md
maturity: validated
read_status: deep-read
created: 2026-06-24
updated: 2026-06-24
cross-wiki-source: "briefs/2026-06-24_k127-emagnet-irumai-selfplay-steals.md"
---

## Relations

- @sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md — EMA magnet mechanism
- @sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md — meld-game RL benchmark
- @sources/arxiv-2606.20960-equilibrium-internal-transfers-2026-06-24.md — transfer equilibria vocabulary
- @sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md — GARIP running-average line

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K127 EMAgnet + IRumAI + SETE steals |
| **Date** | 2026-06-24 |

## Narrative

### EMAgnet steal (2606.23995) — poker arena selfplay

| Idea | Action |
|------|--------|
| Uniform magnet wastes budget on dominated actions | When tuning PPO selfplay locals, prefer **moving magnet** (EMA weights) over flat entropy in large action spaces |
| GARIP complement | GARIP = policy-space running average; EMAgnet = **parameter-space** EMA — document which anchor family each egress experiment uses |
| Scope | **Offline egress selfplay only** — not runtime `decide()` |

Cross-ref K126 GARIP · K125 regime gates (label selfplay KPIs separately from TrueSkill HU).

### IRumAI steal (2606.21975) — card-game bot research

| Idea | Action |
|------|--------|
| Search-free fast policy | 0.33 ms/action vs 7000× slower search heuristic — validates **policy-only inference** path for arena bots |
| Hidden-hand probing | Linear probe shows opponent-hand modeling from public events — parallels discard/block reads → poker line + board inference |
| Meld-validity games | Stub `@entities/games/indian-rummy.md` — distinct from NLHE; no port to `decide()` |
| Live botting | **NO-GO** — research sim only |

### SETE steal (2606.20960) — game theory vocabulary

| Idea | Action |
|------|--------|
| Internal transfers before play | Vocabulary for **soft-play / chip-dumping** analysis in multi-way poker (Farina authorship) |
| Implementation | **None** — theoretical EC 2026 paper |

### Operator checklist addendum

- [ ] Egress selfplay panel: note magnet type (uniform / policy-avg / param-EMA) per K127
- [ ] GARIP vs EMAgnet — pick one anchor family per experiment; don't stack blindly
- [ ] Bundle spec still blocking researcher submit (K125)

## Dead Ends

- EMAgnet inside `cemini_decide()` per hand
- IRumAI on real-money rummy platforms
- SETE mediator as dev.fun venue feature

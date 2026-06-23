---
title: K126 — GARIP self-play + PM forecast eval steals
type: source
tags: [source, brief, poker, prediction-markets, self-play, k126]
keywords: [garip, running average, futurex, time machine, eval sandbox, hu selfplay]
related:
  - sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md
  - sources/arxiv-2606.21013-agentic-time-machine-forecasting-2026-06-23.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/heads-up-arena-strategy.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/platforms/polymarket.md
  - sources/daily-digest-reject-cluster-k126-2026-06-23.md
maturity: validated
read_status: deep-read
created: 2026-06-23
updated: 2026-06-23
cross-wiki-source: "briefs/2026-06-23_k126-garip-selfplay-pm-forecast-steals.md"
---

## Relations

- @sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md — GARIP anchor mechanism
- @sources/arxiv-2606.21013-agentic-time-machine-forecasting-2026-06-23.md — TM ↔ live FutureX correlation
- @sources/brief-k125-eval-gate-discipline-2026-06-22.md — regime-separated eval gates

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K126 GARIP selfplay + PM forecast eval steals |
| **Date** | 2026-06-23 |

## Narrative

### GARIP steal (2606.22688) — poker arena

| Idea | Action |
|------|--------|
| Running-average > snapshot anchor | When tuning **Eval S1** selfplay locals, target empirical mixture of past policies — not stale CFR snapshot |
| Hyperparameter robustness | Prefer flat running-average lag profile over periodic snapshot (R-NaD-style) at default settings |
| Scope | **Offline egress selfplay only** — not runtime `decide()` |

Complements K124 MAFP (equilibrium mixture) and K125 regime gates (don't port selfplay KPIs to TrueSkill HU without relabeling).

### Time Machine steal (2606.21013) — PM retail

| Idea | Action |
|------|--------|
| Fast replay sandbox | TM offline scores correlate with live FutureX — pattern for **PM bot backtest** before capital |
| Polymarket eval | Paper validates on FutureX-Past + Polymarket under TM — retail hygiene reference |
| Boundary | Eval methodology only; execution stays @osint-wiki |

### Operator checklist addendum

- [ ] Document selfplay opponent anchor type (snapshot vs running average) in Eval S1 gate notes
- [ ] If PM lane expands: note TM-style cutoff replay as eval option (no prod deploy from wiki)
- [ ] Bundle spec still blocking researcher submit (K125)

## Dead Ends

- GARIP training loop inside `cemini_decide()` per hand
- TM leaderboard rank as copy-trading signal on Polymarket

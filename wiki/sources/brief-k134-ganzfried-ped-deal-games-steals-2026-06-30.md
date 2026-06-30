---
title: K134 — Ganzfried PED + deal-games exploitability ladder steals
type: source
tags: [source, brief, poker, game-theory, k134]
keywords: [ped, fp-ped, ganzfried, openspiel, exploitability, cfr, ppo]
related:
  - sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md
  - sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md
  - sources/daily-digest-batch-k134-2026-06-30.md
  - sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/poker-bot-tooling.md
maturity: validated
read_status: deep-read
created: 2026-06-30
updated: 2026-06-30
cross-wiki-source: "briefs/2026-06-30_k134-ganzfried-ped-deal-games-steals.md"
---

## Relations

- @sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md — exact NLCP ceiling (K131)
- Private brief: `briefs/2026-06-30_k134-ganzfried-ped-deal-games-steals.md`
- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-06-30_k134-ped-exploitability-steal.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K134 Ganzfried PED + deal-games steals |
| **Date** | 2026-06-30 |
| **Batch** | K134 daily digest (2 PDFs) |

## Narrative

### Ganzfried PED steal (2606.29169)

| Idea | Action |
|------|--------|
| **FP-PED hybrid** | Literacy: MAFP/FP strong early → refinement pass for long-run exploitability — not prod training, but explains hybrid research metaphors |
| **Multiplayer ε(σ)** | Formal exploitability metric for n-player imperfect-info — pairs COM exploit vs SEPO defense table |
| **vs K131 VBT** | Exact when small (NLCP); PED when large — dual Ganzfried anchors |

### Deal-games steal (2606.29457)

| Idea | Action |
|------|--------|
| **Solver ladder** | Tabular: CFR/MMD/PSRO win; large: PPO/PPG — justifies arena **heuristic `decide()`** + selfplay gate, not exact Nash |
| **Signal × strategy space** | Diligence depth ↔ HUD memory depth — more signals = harder exact solve |
| **ε lower bound only** | Learned exploitability estimates are not Nash certificates — mirror in private audit reporting |
| Phase-0 | **MIT** `imperfect-information-deal-games` — read benchmarks; 0★ unvalidated |

### Operator checklist addendum

- [ ] Document exploitability vs TrueSkill distinction in private HL README
- [ ] Selfplay `--gate` remains regression KPI — not multiplayer Nash ε
- [ ] Optional: spike OpenSpiel deal-game exploitability harness for research branch only

## Dead Ends

- PED on NLHE prod policy
- PPO takeover auction model for `decide()`
- Exact Nash solver for Playground fish pool

---
title: K122 poker agent paper landscape (2024–2026)
type: source
tags: [source, poker, research, arxiv, k122, opponent-modeling, devfun]
keywords: [alphaexploitem, stratformer, toolpoker, gto-wizard-benchmark, beyond-gto, omis, deepcfr]
related:
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/arxiv-2508-17671-consistent-opponent-modeling.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/heads-up-arena-strategy.md
  - entities/bots/poker-bot-tooling.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/arxiv-2606.14571-streammembench-agent-memory-2026-06-21.md
  - sources/brief-k122-poker-researcher-track-plan-2026-06-19.md
maturity: draft
created: 2026-06-19
updated: 2026-06-26
---

## Relations

- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — F6/F9–F13 gap matrix
- @concepts/opponent-modeling-imperfect-info.md — COM + exploit doctrine
- @concepts/heads-up-arena-strategy.md — HU researcher track target

## Raw Concept

Research sweep (2026-06-19) mapping 2024–2026 poker-agent literature vs wiki/K118 coverage. Twelve high-value papers **not yet** individual source pages. Verdicts for **pure-code `decide()`** HU researcher track.

## Narrative

### Already ingested (skip duplicate stubs)

COM (`2508.17671`), PokerSkill + SEPO (digest batches), Agents All the Way Down (`2606.11869`), dev.fun / arena-pokerkit (K102 entity).

### Top deep-reads (priority order)

1. [AlphaExploitem](https://arxiv.org/abs/2605.09150) — **GO** — cross-hand exploit memory → K118 F6
2. [StratFormer](https://arxiv.org/abs/2604.25796) — **GO** — GTO base + exploit head → HUD/chart pattern
3. [Beyond GTO NLHE](https://openreview.net/forum?id=Xh0s29VtbH) — **GO** — profit-max HU framing
4. [GTO Wizard Benchmark](https://arxiv.org/abs/2603.23660) — **REFERENCE** — HUNL eval API + AIVAT (F9–F11)
5. [OMIS NeurIPS 2024](https://openreview.net/forum?id=bGhsbfyg3b) — **GO** — in-context opponent search (offline translate)

### Full table (not yet individual wiki sources)

| Paper | URL | Verdict |
|-------|-----|---------|
| AlphaExploitem | [2605.09150](https://arxiv.org/abs/2605.09150) | GO |
| StratFormer | [2604.25796](https://arxiv.org/abs/2604.25796) | GO |
| Beyond GTO NLHE | [2509.23747](https://arxiv.org/abs/2509.23747) | GO |
| GTO Wizard Benchmark | [2603.23660](https://arxiv.org/abs/2603.23660) | REFERENCE |
| ToolPoker | [2602.00528](https://arxiv.org/abs/2602.00528) | REFERENCE (offline F12–F13) |
| Readable Minds | [2604.04157](https://arxiv.org/abs/2604.04157) | REFERENCE |
| Deep Predictive DCFR | [2511.08174](https://arxiv.org/abs/2511.08174) | REFERENCE |
| ABD (depth-limit exploit) | [2501.10464](https://arxiv.org/abs/2501.10464) | REFERENCE |
| PokerBench | [2501.08328](https://arxiv.org/abs/2501.08328) | REFERENCE |
| OMIS | [OpenReview bGhsbfyg3b](https://openreview.net/forum?id=bGhsbfyg3b) | GO |
| MAFP | [2606.19308](https://arxiv.org/abs/2606.19308) | REFERENCE (K124) |
| StreamMemBench | [2606.14571](https://arxiv.org/abs/2606.14571) | REFERENCE (F6 eval) |
| SpinGPT | [2509.22387](https://arxiv.org/abs/2509.22387) | REJECT (runtime LLM) |
| SPIRAL | [2506.24119](https://arxiv.org/abs/2506.24119) | REJECT (wrong stack) |

### K118 literature gaps

| K118 item | Paper support |
|-----------|---------------|
| F6 session / showdown memory | AlphaExploitem, StratFormer, OMIS, Readable Minds |
| F12–F13 offline solver | ToolPoker, PokerSkill (ingested) |
| F9–F11 eval cadence | GTO Wizard Benchmark |
| Runtime LLM decide() | SpinGPT, SPIRAL → REJECT |

## Snippets

> Highest-signal new lane for HU researcher track: **exploit + session memory + offline eval** — not runtime LLM or full CFR training. [Source: K122 research sweep 2026-06-19]

## Dead Ends

- **SpinGPT / SPIRAL** — LLM training paths; conflict with zero-LLM Arena doctrine
- Full neural CFR at runtime — clock + pure-code constraint

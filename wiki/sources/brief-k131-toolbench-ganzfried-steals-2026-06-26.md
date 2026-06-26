---
title: K131 — ToolBench-X arena-tool hazards + Ganzfried VBT Nash steals
type: source
tags: [source, brief, poker, agents, game-theory, k131]
keywords: [toolbench-x, arena-tool, ganzfried, nash, vbt, sandbox]
related:
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/daily-digest-reject-cluster-k131-2026-06-26.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - concepts/opponent-modeling-imperfect-info.md
  - entities/platforms/devfun-poker-arena.md
maturity: validated
read_status: deep-read
created: 2026-06-26
updated: 2026-06-26
cross-wiki-source: "briefs/2026-06-26_k131-toolbench-ganzfried-steals.md"
---

## Relations

- @sources/devfun-sandbox-researcher-guide-2026-06-26.md — official `arena-tool` MCP submit loop
- @sources/arxiv-2508-17671-consistent-opponent-modeling.md — prior Ganzfried COM anchor
- Private brief: `briefs/2026-06-26_k131-toolbench-ganzfried-steals.md`
- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-06-26_k131-toolbench-x-arena-tool-steal.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K131 ToolBench-X + Ganzfried VBT steals |
| **Date** | 2026-06-26 |
| **Batch** | K131 daily digest (3 PDFs) |

## Narrative

### ToolBench-X steal (2606.25819) — sandbox harness reliability

| Idea | Action |
|------|--------|
| Five recoverable hazard types | Map to **`arena-tool`** failure modes: spec drift (action schema), invocation error (bad `amount`), execution failure (clock/timeout), output drift (partial state), cross-source conflict (PvP scheduler vs local cache) |
| Recovery > call accuracy | Bundle harness needs **retry + fallback + verify** before `submit_action`; generic reasoning_text will fail validation |
| Phase-0 | GitHub **no LICENSE** — benchmark taxonomy only, no install |
| Pure-code `decide()` | Hazards at **MCP harness** layer; charts unchanged |

### Ganzfried VBT steal (2606.25997) — theory ceiling

| Idea | Action |
|------|--------|
| Exact multiplayer NE via NLCP + VBT | Literacy: why MAFP/GARIP/selfplay approximations persist for NLHE |
| 3-player Kuhn solved faster | Toy-game anchor only — not arena scale |
| Author lineage | Pairs with COM (2508.17671) — exact NE vs consistent opponent modeling |

### Operator checklist addendum

- [ ] Sandbox bundle: hazard table in harness README (retry `get_game_state`, validate `allowedActions` before act)
- [ ] Do not conflate function-call pass rate with TrueSkill match wins
- [ ] Skip Gurobi NLCP for prod `decide()` — reference reading only

## Dead Ends

- ToolBench-X repo install without license
- Exact Nash solver for dev.fun NLHE
- ITS counterfactual bandit (2606.23015) for lineup ownership

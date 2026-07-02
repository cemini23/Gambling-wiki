---
title: K136 — Tool-RL structural collapse steals for arena MCP training
type: source
tags: [source, brief, agents, tool-use, k136]
keywords: [structural-collapse, interleaved-sft, tool-rl-box, arena-tool, control-token]
related:
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/daily-digest-batch-k136-2026-07-02.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/gambling-bot-architecture.md
maturity: validated
read_status: deep-read
created: 2026-07-02
updated: 2026-07-02
cross-wiki-source: "briefs/2026-07-02_k136-tool-rl-collapse-steals.md"
---

## Relations

- @sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md — runtime hazard layer (K131)
- Private brief: `briefs/2026-07-02_k136-tool-rl-collapse-steals.md`
- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-07-02_k136-tool-rl-structural-collapse-steal.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K136 Tool-RL collapse steals |
| **Date** | 2026-07-02 |
| **Batch** | K136 daily digest (1 PDF) |

## Narrative

### Tool-RL steal (2606.26027)

| Idea | Action |
|------|--------|
| **Structural collapse** | Monitor MCP bundle agents for control-token / format degeneration — not just task reward |
| **Interleaved SFT + RL** | If training sandbox LLM bundles: SFT on golden `arena-tool` trajectories before RL |
| **vs K131 hazards** | Training stability (this paper) + runtime retry/recovery (ToolBench-X) — both required |
| **Process Reflection** | Log failed bundle steps → reflection SFT corpus for harness regression |
| Phase-0 | **MIT** `hypasd-art/Tool-RL-Box` (~5★) — read recipes; no prod `decide()` RL |

### Operator checklist addendum

- [ ] Private bundle training: never pure RL without SFT anchor on valid tool-call format
- [ ] Regression: detect "polluted" vs "collapsed" MCP outputs in dry-runs
- [ ] OOD: test format drift (schema rename) after interleaved training
- [ ] Prod `decide()` stays pure code — research lane only

## Dead Ends

- BFCL-V3 as Playground qualification metric
- Pure RL fine-tune on `reasoning_text` templates without format supervision

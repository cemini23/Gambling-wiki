---
title: pydfs-lineup-optimizer
type: entity
tags: [entity, tool, dfs, open-source, python]
keywords: [pydfs, lineup-optimizer, draftkings, fanduel, nfl, nba]
related:
  - concepts/dfs-strategy-overview.md
  - entities/platforms/draftkings.md
  - entities/platforms/fanduel.md
  - entities/sports/nfl-betting.md
  - entities/sports/nba-betting.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/dfs-strategy-overview.md — primary use case
- @sources/gemini-github-sports-betting-landscape-2026-05-30.md — Gemini landscape Phase-0 candidate

## Raw Concept

Open-source **DFS lineup optimizer** (Python) for DraftKings/FanDuel slates — stacks, exposure limits, multi-lineup generation. Cited in Gemini GitHub sports-betting landscape as classical ML/DFS reference (distinct from PM market making).

## Narrative

### What it does

- Generates optimal or near-optimal lineups under salary cap constraints
- Supports stacking rules, max exposure per player, contest-specific settings
- Common stack in DFS research workflows alongside projection CSVs

### Phase-0 checklist [NEEDS VERIFICATION 2026-06-01]

1. Confirm **license** via `gh api` before any install in prod environment
2. Verify maintained support for current DK/FD export formats
3. Compare vs paid optimizers (ownership leverage, late swap) — tool is **lineup math**, not projections

### Verdict

**CONDITIONAL-GO** for DFS lane — reference implementation for `@concepts/dfs-strategy-overview.md`; not a sports **spread** betting tool.

## Snippets

> Listed under "Classical ML / DFS" in Gemini GitHub sports-betting landscape — reference for DFS modeling, reject for PM LP bots. [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md]

---
title: K124 — MAFP + StreamMemBench poker research steals
type: source
tags: [source, brief, poker, devfun, k124, mafp, memory]
keywords: [fictitious play, streammembench, f6, session memory, researcher round]
related:
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/arxiv-2606.14571-streammembench-agent-memory-2026-06-21.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/daily-digest-reject-cluster-k124-2026-06-21.md
maturity: validated
read_status: deep-read
created: 2026-06-21
updated: 2026-06-21
cross-wiki-source: "briefs/2026-06-21_k124-mafp-memory-poker-research-steals.md"
---

## Relations

- @sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md — MAFP source (K124)
- @sources/arxiv-2606.14571-streammembench-agent-memory-2026-06-21.md — memory eval source
- OSINT brief home: `agents/devfun-poker-arena/briefs/` (per `active_project_brief_targets.yaml`)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K124 digest steals for Researcher Round (Jun 21 β) |
| **Date** | 2026-06-21 |
| **Routing** | poker-arena co-primary |

## Narrative

### MAFP steal (2606.19308) — offline only

**Do not** implement runtime LLM fictitious play in `decide()`.

**Do steal:**
- **Empirical mixture HUD** — maintain running freq distribution per villain_id; best-response thresholds shift one bucket per HL patch
- **Robustness metric** — add P5 scenario: worst-case vs LAG + nit locals (tournament strength alone hides exploitability)
- **P3 debate framing** — when HL analyst proposes patch, enumerate stances: TrueSkill max vs Jungleman style vs axis hygiene

### StreamMemBench steal (2606.14571) — F6 eval spec

Extend `session_memory.py` acceptance tests:

1. **Evidence recall** — after showdown, villain line stored
2. **Follow-up reuse** — hand N+5 vs same villain applies stored leak (widen steal / tighten call)
3. **Failure mode** — memory stored but next decision ignores it (current gap per K118)

### Rejected from batch

2606.20510 agent security verification — out of scope.

## Snippets

> "MAFP listed as co-primary steal in active_project_brief_targets.yaml (2026-06-20)." [Source: scripts/active_project_brief_targets.yaml]

## Dead Ends

- MAFP as runtime decide() architecture
- StreamMemBench egocentric task data for poker training

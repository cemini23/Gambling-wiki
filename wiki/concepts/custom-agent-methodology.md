---
title: Custom agent methodology (Agents All the Way Down)
type: concept
tags: [concept, meta, bots, agent-engineering, methodology, k120]
keywords: [agents-all-the-way-down, turtle-pattern, liteshell, agent-tests-agent, substrate, prompt-caching, mcp-vs-cli]
related:
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - meta/gambling-bot-ingest-rubric.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - osint-wiki/concepts/cemini-knowledge-application-architecture.md
  - sweeps/2026-06-19-daily.md
maturity: validated
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md — K120 source (arXiv 2606.11869)
- @concepts/poker-hl-analyst-loop.md — primary gambling-wiki application (offline patch loop)
- @concepts/gambling-bot-architecture.md — fleet topology; CLI composition corollary
- @meta/gambling-bot-ingest-rubric.md — Phase-0 checklist for Adopt repos

## Raw Concept

Named practice for building **purpose-built AI agents** (one app, one domain, one maintainer) — distinct from general-purpose copilots. Distilled from AAC/LAMB case study; framework-free by design.

## Narrative

### Five phases (two + three)

**Preconditions (read once):**

1. **P1 Substrate** — LLM as software component; cache prefix `tools → system → messages`; cost/hallucination/context/time constraints
2. **P2 Building blocks** — function calling, MCP, CLI, liteshell, agent loop, skills, characters, hooks

**Practice loop (iterate forever):**

3. **P3** — Prototype with GP agent (Cursor/Claude Code) on real platform
4. **P4** — Harvest into minimal agent loop; ship as CLI (**Turtle pattern**)
5. **P5** — Agent-tests-agent: GP agent drives custom agent through behavioral scenarios

### Tooling choices for gambling-bot program

| Pattern | Gambling-wiki use | Phase-0 |
|---------|-------------------|---------|
| **CLI over MCP** | High-frequency odds fetch, analyze scripts, preflight gates | **GO** — lower token baseline |
| **Liteshell** | In-app DFS slate assistant (future) | **CONDITIONAL-GO** when no host shell |
| **MCP** | Browser/stateful session tools only | **CONDITIONAL-GO** — not default for fleet |
| **Hooks / allow-list** | Bot scaffolding — ToS-safe action gates | **GO** — security in code not prompts |
| **CLI composition** | Multi-lane fleet (sportsbook + PM + DFS) without orchestration framework | **REFERENCE** |

### Mapping to poker HL loop

The dev.fun **Heuristic Learning** loop is a domain-specific instance of P3→P4→P5:

```
P3  Arena analyze → LLM patch brief (offline)
P4  cemini_decide.py + preflight shell (shipped artifact)
P5  regression spots + selfplay audit (--gate)
```

**Rule preserved:** runtime `decide()` stays **zero LLM** — P3/P5 use LLM offline; P4 output is pure code. This aligns with paper's custom-agent fit axis (cost predictability, security boundaries) and K118 dead-end on runtime ToolPoker parity.

### Multi-agent fleet corollary

Paper claim: orchestration = **`call_cli` composition** — parent agent invokes child agent CLIs like any shell tool. For gambling-bot fleet:

- Shared core (bankroll, Kelly, logging) can orchestrate lane bots via CLI contracts
- Avoid heavyweight MAS frameworks until typed shared state or durable workflows are required (§5.4 leaks)
- **NO-GO:** OrchRM-style runtime LLM orchestration for prod wagering (K119 reject cluster)

## Snippets

> "Multi-agent orchestration is just CLI composition." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md]

> "Instructions shape behaviour; the scaffolding's allow-list shapes outcomes." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md, §3.2]

## Dead Ends

- **Over-orchestration trap** — elaborate multi-agent chains before single small loop works (paper §4)
- **MCP registry for every bot tool** — token tax on repeated sportsbook/PM polling
- **P5 replacing pytest/regression** — behavioral agent tests complement, not replace, deterministic gates

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
  - sources/arxiv-2606.17682-trainee-to-trainer-llm-env-engineer-2026-06-20.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md
  - sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md
maturity: validated
created: 2026-06-19
updated: 2026-07-03
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

### Evaluator co-evolution (K133 RQGM) [TENTATIVE]

Self-improving agent literature assumes **stationary** benchmarks; RQGM @sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md introduces **epoch-versioned utilities** and co-evolved judges. For gambling-bot program:

| Pattern | Application |
|---------|-------------|
| Fixed within-epoch eval | Private HL regression + sandbox verifier weights frozen per patch generation |
| Epoch boundary update | Document eval changelog when corpus or judge rubric shifts |
| Agent-as-judge | Cheap screening before expensive sim — pairs K132 Fara verifier triad |
| Adversarial epoch | Correct PvE panel over-acceptance on AI bundles |

**NO-GO:** RQGM recursive self-edit on prod `decide()` during live competition.

### Tool-RL structural collapse (K136) [TENTATIVE]

@sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md: pure RL on multi-step MCP loops can **collapse tool-call structure** (control-token spikes) while competence remains. **Interleaved SFT + RL** stabilizes; pairs K131 runtime hazards. Research lane for sandbox bundle LLMs only — prod `decide()` stays pure code.

### SWE-INTERACT interactive eval (K137) [TENTATIVE]

@sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md: **single-turn SWE success does not transfer** to multi-turn user-driven sessions (~50% → ~25% solve rate). HL patch loop and sandbox bundles should eval **partial-spec recovery** (vague brief → progressive constraints), not only fully-specified MCP trajectories. Apache-2.0 `scaleapi/SWE-Interact` is benchmark reference only.

## Snippets

> "Multi-agent orchestration is just CLI composition." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md]

> "Instructions shape behaviour; the scaffolding's allow-list shapes outcomes." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md, §3.2]

## Dead Ends

- **Over-orchestration trap** — elaborate multi-agent chains before single small loop works (paper §4)
- **MCP registry for every bot tool** — token tax on repeated sportsbook/PM polling
- **P5 replacing pytest/regression** — behavioral agent tests complement, not replace, deterministic gates

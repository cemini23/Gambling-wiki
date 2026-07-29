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
  - sources/arxiv-2607.02389-steerability-constraints-coding-agents-2026-07-06.md
  - sources/arxiv-2607.02453-oss-agent-framework-ecosystem-health-2026-07-06.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/arxiv-2607.07666-ensemble-qsp-hierarchical-memory-2026-07-13.md
  - sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md
  - entities/tools/ideagene-bench.md
  - sources/brief-k155-ideagene-lineage-steals-2026-07-14.md
  - sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
  - entities/tools/code-world-models.md
  - sources/brief-k158-play-adequacy-cwm-steals-2026-07-17.md
  - sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md
  - entities/tools/aleena.md
  - sources/brief-k159-aleena-decision-continuity-steals-2026-07-18.md
  - sources/arxiv-2607.07207-memory-scarcity-open-models-2026-07-18.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/tools/wc2026-agents.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - sources/arxiv-2607.08861-fictitious-play-coupled-fbsde-2026-07-16.md
maturity: validated
created: 2026-06-19
updated: 2026-07-29
---

## Relations

- @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md — K120 source (arXiv 2606.11869)
- @concepts/poker-hl-analyst-loop.md — primary gambling-wiki application (offline patch loop)
- @concepts/gambling-bot-architecture.md — fleet topology; CLI composition corollary
- @meta/gambling-bot-ingest-rubric.md — Phase-0 checklist for Adopt repos
- @entities/tools/ideagene-bench.md — K155 lineage-competence FOSS eval (CONDITIONAL-GO)
- @sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md — IdeaGene / GenomeDiff / PES
- @entities/tools/code-world-models.md — K158 play-adequacy CWM eval (CONDITIONAL-GO)
- @sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md — verified-vs-correct gap / danger law
- @entities/tools/aleena.md — K159 lifecycle alignment FOSS (CONDITIONAL-GO)
- @sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md — decision/risk/open-question continuity
- @sources/arxiv-2607.07207-memory-scarcity-open-models-2026-07-18.md — REFERENCE: open/local inference economics
- @entities/tools/wc2026-agents.md — K160 WC forecasting FOSS (GO)
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — market-baseline three-axis eval

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

### Constraint substrate (K148) [TENTATIVE]

@sources/arxiv-2607.02389-steerability-constraints-coding-agents-2026-07-06.md: pre-LLM **linters, layered docs CLI, allow-lists** beat unconstrained MCP scaffolding for auditable coding agents. Pairs K120 hooks/allow-list — **Adopt** substrate before expanding tool surface.

### Lineage competence (K155 IdeaGene) [TENTATIVE]

@sources/arxiv-2607.08758-ideas-have-genomes-ig-bench-2026-07-14.md / @entities/tools/ideagene-bench.md: research proposals and HL patches should be scored on **mechanism inheritance**, not topical proximity. Steal typed Idea Genome roles + GenomeDiff fates; open proposals use PES (Heredity · Variation · Selection). P5 behavioral gates should reject “related paper” steals that share task ecology but not driver mechanism. **CONDITIONAL-GO** FOSS harness until SPDX LICENSE lands.

### Play-adequacy vs prediction accuracy (K158 CWM) [TENTATIVE]

@sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md / @entities/tools/code-world-models.md: P5 gates that only check fixture/transition match can still fail at play (verified-vs-correct gap). Prefer search-distribution or head-to-head play metrics; size eval N with the danger law for rare pivotal failures; complete specs rather than flooding examples.

### Lifecycle decision continuity (K159 Aleena) [TENTATIVE]

@sources/arxiv-2607.08043-aleena-alignment-agent-2026-07-18.md / @entities/tools/aleena.md: collaboration agents should persist **decisions / action items / risks / open questions** as structured artifacts (not chat-only), and flag **vocabulary drift** when domain terms conflict across sessions. Draft code changes stay human-gated. **CONDITIONAL-GO** FOSS until SPDX. Companion REFERENCE @sources/arxiv-2607.07207-memory-scarcity-open-models-2026-07-18.md: when memory bandwidth is scarce, prefer open/local inference economics for offline P3/P5 — not a wagering edge.

### Market-baseline three-axis eval (K160 WC2026-Agents) [CONFIRMED]

@sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md / @entities/tools/wc2026-agents.md: P5 agent evals that only score pick accuracy can be a null when models converge. Require a hard non-LLM / market baseline; separately score **calibration**, **decision quality** (staking / ROI), and **self-knowledge** (reflection honesty). Do not treat fade-market as default LLM alpha. **GO** FOSS (MIT + CC BY 4.0).

## Snippets

> "Multi-agent orchestration is just CLI composition." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md]

> "Instructions shape behaviour; the scaffolding's allow-list shapes outcomes." [Source: @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md, §3.2]

## Dead Ends

- **Over-orchestration trap** — elaborate multi-agent chains before single small loop works (paper §4)
- **MCP registry for every bot tool** — token tax on repeated sportsbook/PM polling
- **P5 replacing pytest/regression** — behavioral agent tests complement, not replace, deterministic gates

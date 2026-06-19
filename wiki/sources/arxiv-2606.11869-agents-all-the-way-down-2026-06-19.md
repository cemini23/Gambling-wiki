---
title: Agents All the Way Down — custom AI agent methodology (arXiv 2606.11869)
type: source
tags: [source, arxiv, agent-engineering, methodology, mcp, cli, k120]
keywords: [2606.11869, agents-all-the-way-down, turtle-pattern, liteshell, agent-tests-agent, substrate, prompt-caching]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - meta/gambling-bot-ingest-rubric.md
  - entities/bots/cemini-devfun-poker-agent.md
  - entities/bots/poker-bot-tooling.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sweeps/2026-06-19-daily.md
  - osint-wiki/concepts/cemini-knowledge-application-architecture.md
maturity: validated
read_status: skimmed
created: 2026-06-19
updated: 2026-06-19
---

## Relations

- @concepts/custom-agent-methodology.md — synthesized concept (K120)
- @concepts/poker-hl-analyst-loop.md — P3→P4→P5 maps to HL analyze/patch/gate loop
- @concepts/gambling-bot-architecture.md — fleet orchestration + tooling posture
- @sweeps/2026-06-19-daily.md — overnight fetch provenance

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production |
| **Authors** | Marc Alier Forment, Juanan Pereira, Francisco José García-Peñalvo, María José Casañ Guerrero |
| **arXiv** | [2606.11869](https://arxiv.org/abs/2606.11869) |
| **Categories** | cs.SE, cs.AI |
| **Case study** | AAC (Agent-Assisted Creator) on LAMB educational platform — ~10 days, one dev + AI pair-programmer, production at two universities (~200 educators) since Apr 2026 |
| **PDF** | `cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.11869-2606-11869v1-agents-all-the-way-down-a-methodolo.pdf` |
| **sha256** | `81e95097862642e7…` |
| **Read status** | skimmed — abstract + §1–§5 + P1–P2 building blocks |

## Narrative

### Thesis

General-purpose agents (Claude Code, Cursor, OpenCode) are the **bench saw**; custom agents are **jigs** — purpose-built for one application, one domain, one maintainer. The paper names a framework-free practice with **two preconditions (cross once, keep)** and **three iterated practices**:

| Phase | Name | Acceptance |
|-------|------|------------|
| **P1** | Substrate — LLM as software component | Diagnose cost shape from usage records; know cache prefix boundaries |
| **P2** | Building blocks — vocabulary fluency | Pick function calling vs MCP vs CLI vs liteshell vs hooks per problem |
| **P3** | Prototype with general-purpose agent | Reconnaissance on real platform; architecture discovered by building |
| **P4** | Harvest, fold, ship as CLI (**Turtle pattern**) | Small agent loop + `call_cli` dispatch; framework-free |
| **P5** | Agent-tests-agent | GP agent drives custom agent through behavioral scenarios; complements pytest |

Working loop after P1/P2: **P3 → P4 → P5 → P3**. Corollary: **multi-agent orchestration = CLI composition** (Splinter delegates to specialist Turtle CLIs).

### P1 cache discipline [CONFIRMED — skim]

Anthropic-style prompt caching order: **`tools → system → messages`**. Stable content earlier = cheaper reuse. System holds skills, persona, directives, memories; per-turn volatile state belongs in **messages**, not system. Reordering tools alphabetically can invalidate an entire session cache.

### P2 — MCP vs CLI vs liteshell [CONFIRMED — skim]

| Surface | Cost shape | When |
|---------|------------|------|
| **MCP** | Fixed tool-registry overhead + structured results per call | Stateful browser/session tools; many-tool catalogs inflate context |
| **CLI** | Command + stdout only; no registry tax | Default; models pretrained on shell idioms; pipe through `jq`/`grep` to trim |
| **Liteshell** | In-process Facade presenting CLI-shaped interface to LLM inside cloud apps | No host shell (FastAPI, Django); one dispatch tool + skill markdown |

Practitioner benchmarks cited at high end: large MCP catalogs **≈2×–35×** token overhead vs lean CLI depending on tool count and output verbosity — not a universal ratio.

**Security:** authorization lives in **scaffolding hooks** (pre-tool-use allow-list), never in schema, description, or system prompt alone.

### gambling-wiki posture: REFERENCE (methodology, not wagering edge)

| Owns here | Route @osint-wiki |
|-----------|-------------------|
| Bot **requirements** — HL loop as P3→P4→P5; CLI composition for fleet | CeminiSuite prod deploy, secrets, MCP server configs |
| Tooling Phase-0 — prefer CLI/liteshell over bloated MCP for high-volume bot ops | Full agent harness implementation |
| P5 agent-tests-agent as complement to regression spots / selfplay gate | Private HL loop scripts |

### Phase-0 verdict (gambling-bot program)

| Artifact | Verdict |
|----------|---------|
| Methodology as pattern library | **REFERENCE** — adopt vocabulary; no license/repo to adopt |
| Runtime LLM in prod wagering bots | **NO-GO** — paper targets custom agents with tool loops; cemini_decide stays pure-code at runtime |
| MCP-heavy multi-agent orchestration (OrchRM-style) | **NO-GO** — contradicts latency + token budget for sportsbook/PM lanes |
| P5 behavioral testing for HL loop | **CONDITIONAL-GO** — extend private regression + selfplay with scenario suites driven by GP agent |

### HL loop mapping [TENTATIVE]

| Paper phase | Poker HL analog |
|-------------|-----------------|
| P3 Prototype | Cursor/Claude patches `cemini_decide.py` from Arena analyze brief |
| P4 Ship CLI | `cemini_decide` + preflight shell as deterministic artifact |
| P5 Agent-tests-agent | Selfplay audit + regression spots; future: GP agent runs scenario matrix |

## Snippets

> "The working loop is P3 to P4 to P5 and back, and one corollary falls out for free: multi-agent orchestration is just CLI composition." [Source: arxiv-2606.11869, Abstract]

> "Security lives in the scaffolding's tool dispatcher — prompt instructions help steer behaviour, but authorisation and execution policy belong in deterministic host-side controls." [Source: arxiv-2606.11869, §3.2 — paraphrase]

> "Agent-tests-agent … complements classical software testing; it does not replace it." [Source: arxiv-2606.11869, Abstract]

## Dead Ends

- **Framework-first before P1/P2 fluency** — paper anti-mandate; opaque failure modes
- **MCP as default for all bot tooling** — registry tax on high-frequency sportsbook/PM ops
- **Runtime LLM decide() for Arena** — methodology builds custom agents with tool loops; prod poker path is offline patch + pure-code deploy (K118)

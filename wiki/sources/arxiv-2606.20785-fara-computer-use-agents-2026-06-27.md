---
title: Fara-1.5 — scalable learning environments for computer use agents (arXiv 2606.20785)
type: source
tags: [source, arxiv, agents, computer-use, cua, verifier, k132, fara]
keywords: [faragen, browser-agent, webvoyager, online-mind2web, qwen3.5, synthetic-environment, verifier]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.23321-tmax-terminal-agents-2026-06-25.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/brief-k132-fara-agent-env-steals-2026-06-27.md
  - sources/daily-digest-reject-cluster-k132-2026-06-27.md
  - sweeps/2026-06-27-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-27
updated: 2026-06-27
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.20785-2606-20785v1-fara-1-5-scalable-learning-environm.pdf
phase_0_verdict: CONDITIONAL-GO 2026-06-27 — MIT github.com/microsoft/fara (5931★); reference env+verifier pipeline only, not wagering
---

## Relations

- @sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md — tool/MCP hazard eval (K131)
- @sources/arxiv-2606.23321-tmax-terminal-agents-2026-06-25.md — synthetic task generation (K129)
- @sources/devfun-sandbox-researcher-guide-2026-06-26.md — researcher `arena-tool` submit loop
- @sources/brief-k132-fara-agent-env-steals-2026-06-27.md — K132 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.20785](https://arxiv.org/abs/2606.20785) |
| **Title** | Fara-1.5: Scalable Learning Environments for Computer Use Agents |
| **Authors** | Microsoft (Awadallah et al.) |
| **Repo** | [github.com/microsoft/fara](https://github.com/microsoft/fara) |
| **Model** | [Fara1.5-9B on Azure AI](https://ai.azure.com/catalog/models/Fara1.5-9B) |
| **Phase-0** | **MIT** (gh api 2026-06-27); ~5931★ |
| **Verdict** | **CONDITIONAL-GO** — strip-mine **FaraGen1.5** env+solver+verifier recipe; **NO-GO** as wagering bot |

## Narrative

Fara-1.5 trains **native computer-use agents (CUAs)** on synthetic + live web trajectories. Core pipeline **FaraGen1.5** has three modules:

| Module | Role |
|--------|------|
| **Environments** | Live websites + **synthetic simulators** for auth-gated / irreversible domains |
| **Solvers** | Multi-model harness (incl. GPT-5.4 teacher) + **user simulator** for multi-turn |
| **Verifiers** | **Task correctness**, **efficiency**, **critical-point adherence** |

Models (Qwen3.5 4B/9B/27B) set size-class SOTA on **Online-Mind2Web** (Fara1.5-9B **63.4%**) and **WebVoyager** (**86.6%**).

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **dev.fun researcher sandbox** | **Medium** — tri-verifier pattern maps to bundle eval: legal action + clock efficiency + reasoning-text quality |
| **Playground `decide()`** | Low — browser CUA ≠ NLHE policy |
| **CeminiDFS** | NO-GO |
| **Agent eval harness design** | **HIGH** — synthetic env for gated flows mirrors Daytona sandbox; verifier stack complements ToolBench-X hazards |

Phase-0 **CONDITIONAL-GO**: read MIT repo for FaraGen verifier composition; do not deploy CUA for sportsbook/PM automation (ToS + scope).

## Snippets

> "Collecting computer use data from human demonstrations is expensive and slow, motivating the need for scalable generation strategies. This requires two key ingredients: environments in which agents can act and verifiers that can judge whether their demonstrations succeeded." [Source: arxiv:2606.20785 Abstract]

> "FaraGen1.5 scores the resulting trajectories with three complementary verifiers covering task correctness, efficiency, and critical-point adherence." [Source: arxiv:2606.20785 §Introduction]

> Fara1.5-9B: **63.4%** Online-Mind2Web, **86.6%** WebVoyager. [Source: arxiv:2606.20785 Figure 1]

## Dead Ends

- Fara CUA for DraftKings/FanDuel browser automation — consumer ToS NO-GO
- WebVoyager score as TrueSkill HU proxy
- Train Fara1.5-9B as researcher sandbox `decide()` bundle

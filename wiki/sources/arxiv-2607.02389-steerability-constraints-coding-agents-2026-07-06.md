---
title: Steerability via constraints — scalable oversight of coding agents (arXiv 2607.02389)
type: source
tags: [source, arxiv, agents, coding-agents, security, k148, oversight]
keywords: [substrate, linters, access-control, docs-cli, backdoor-detection, scalable-oversight]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.02389-2607-02389v1-steerability-via-constraints-a-subs.pdf
phase_0_verdict: REFERENCE 2026-07-06 — paper-only; constrained substrate beats unconstrained agent + small reviewer
---

## Relations

- @sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md — interactive eval axis (K137)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.02389](https://arxiv.org/abs/2607.02389) |
| **Verdict** | **REFERENCE** — **constraint substrate** (linters, conventions, docs CLI) cheaper than heavy MCP scaffolding for auditable agents |

## Narrative

Small reviewer (Gemma 4B) backdoor recall: **54.5%** unconstrained → **90.9%** with constrained substrate + ~200 LoC docs CLI. Argues pre-LLM engineering discipline (access control, layered docs, type checkers) **scales to coding agents** and beats saturating context with raw MCP payloads.

| Adoption for David | Action |
|--------------------|--------|
| **Sandbox / HL patches** | Enforce linters + typed modules + docs CLI before expanding MCP tool surface |
| **Fleet bots** | Allow-list actions in code not prompts (pairs K120) |
| **MCP default** | NO-GO unconstrained retrieval dumps — CONDITIONAL-GO MCP for stateful sessions only |

## Snippets

> "The same methods used for decades to manage large human engineering teams … transfer directly to coding agents, and are cheaper (in token) than recent agentic scaffolding." [Source: arxiv:2607.02389 Abstract]

## Dead Ends

- Replacing `cemini_preflight.sh` with LLM reviewer only
- Rust-only claim blocking Python arena codebase

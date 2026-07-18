---
title: Aleena — Alignment Agent for Research Software Engineering (arXiv 2607.08043)
type: source
tags: [source, arxiv, agents, rse, collaboration, k159]
keywords: [aleena, lifecycle-alignment, vocabulary-drift, decision-continuity, uw-ssec, github-agent]
related:
  - entities/tools/aleena.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k159-aleena-decision-continuity-steals-2026-07-18.md
  - sources/daily-digest-batch-k159-2026-07-18.md
  - sweeps/2026-07-18-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-18
updated: 2026-07-18
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2607.08043-aleena-alignment-agent-for-research-software-eng.pdf
phase_0_verdict: CONDITIONAL-GO 2026-07-18 — uw-ssec/Aleena ~1.5MB; no SPDX LICENSE; decision-continuity / risk-surface methodology Adopt
---

## Relations

- @entities/tools/aleena.md — Phase-0 FOSS
- @concepts/custom-agent-methodology.md — P5 decision continuity + structured collaboration artifacts
- @concepts/poker-hl-analyst-loop.md — analyze→patch→deploy decision trail (light steal)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2607.08043](https://arxiv.org/abs/2607.08043) |
| **Authors** | Dani, Core, Setiawan, Garcia Jurado Suarez, Tambay, Mandava, Mittal (UW SSEC) |
| **Repo** | https://github.com/uw-ssec/Aleena |
| **Venue** | AgenticSE @ KDD '26 |
| **Verdict** | **CONDITIONAL-GO** — lifecycle alignment agent; steal decision/risk/open-question continuity |

## Narrative

Aleena turns meeting transcripts and chat into **project-aware GitHub records**: summaries, decisions, action items, risks, open questions, vocabulary extraction + drift detection, draft PRs, and org-level monitoring/eval reports. Backend analyzers call LiteLLM with structured JSON prompts; humans review prompts/artifacts before GitHub writes.

**Gambling / harness fit**

| Lane | Fit |
|------|-----|
| **CCC / custom-agent** | **HIGH** — preserve decisions across sessions; surface risks/open questions; vocabulary drift on domain terms |
| **Poker HL** | **MEDIUM** — decision continuity across analyze→patch→preflight; risk/open-question artifacts (not runtime decide) |
| **David / DFS** | LOW — no image-gen or slate path |

**Steals (not full product adopt)**

1. Structured JSON: `summary / decisions / action_items / risks / open_questions`
2. Vocabulary + **conflict vs duplicate** drift checks on domain terms
3. Draft PR only when action item is code-shaped; human merge gate
4. Monitoring snapshots → deterministic metrics → HTML eval report

## Snippets

> "Aleena is an open-source lifecycle alignment agent for research software engineering collaborations. It turns meeting transcripts and chat conversations into structured, project-aware GitHub records…" [Source: uw-ssec/Aleena README]

Appendix A.1 prompt keys: `summary`, `decisions`, `action_items`, `risks`, `open_questions` — never invent facts; prefer concrete project names / blockers / next steps. [Source: arxiv:2607.08043 App. A.1]

## Dead Ends

- Drop-in replacement for HL `decide()` / arena protocol
- Blind auto-merge of Aleena draft PRs
- Vendoring / redistributing until SPDX LICENSE lands
- Running Aleena web stack in prod without LiteLLM + GitHub App credentials budget

---
title: Words Speak Louder Than Code — LLM vulnerability detection cognitive heuristics (arXiv 2606.30587)
type: source
tags: [source, arxiv, agents, security, k148, code-vulnerability]
keywords: [cognitive-heuristics, vulnerability-detection, black-box-attack, ci-security]
related:
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.30587-2606-30587v1-words-speak-louder-than-code-invest.pdf
phase_0_verdict: REFERENCE 2026-07-06 — paper-only; cognitive framing attacks on LLM security triage
---

## Relations

- @sources/devfun-sandbox-researcher-guide-2026-06-26.md — bundle patch review path

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.30587](https://arxiv.org/abs/2606.30587) |
| **Verdict** | **REFERENCE** — LLM vuln detectors swayed by **cognitive heuristics** in natural-language context |

## Narrative

LLM-based vulnerability detectors flip verdicts based on **cognitive framing** in comments/docs without real code changes — proof-of-concept attack suppresses **97%** of prior detections.

| Implication | Arena |
|-------------|-------|
| **reasoning_text / analyze brief** can bias automated security review | Don't use raw LLM as sole gate on bundle patches |
| Pattern-matching vulns more stable | Deterministic pytest + preflight still primary |
| Cognitive injection | Treat analyze brief as untrusted input to reviewers |

**Adoption for David:** HL loop security review = **deterministic gates first**; LLM triage is advisory only.

## Dead Ends

- LLM Copilot Autofix parity for `cemini_decide.py` review
- Cognitive attack as Playground exploit vector

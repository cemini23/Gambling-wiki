---
title: Tmax — terminal agent training recipe (arXiv 2606.23321)
type: source
tags: [source, arxiv, agents, terminal, rl, k129, tmax]
keywords: [tmax, terminal-bench, swe-agent, synthetic-tasks, apache-2, allen-ai]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md
  - sources/daily-digest-reject-cluster-k129-2026-06-25.md
  - sweeps/2026-06-25-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-25
updated: 2026-06-25
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.23321-2606-23321v1-tmax-a-simple-recipe-for-terminal-a.pdf
phase_0_verdict: CONDITIONAL-GO 2026-06-25 — Apache-2.0 github.com/hamishivi/tmax; strip-mine eval data gen only, not wagering
---

## Relations

- @concepts/custom-agent-methodology.md — agent loop / eval harness patterns
- @sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md — operator steal summary (K129)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.23321](https://arxiv.org/abs/2606.23321) |
| **Title** | Tmax: A simple recipe for terminal agents |
| **Repo** | [github.com/hamishivi/tmax](https://github.com/hamishivi/tmax) |
| **Phase-0** | Apache-2.0 (gh api 2026-06-25) |
| **Verdict** | **CONDITIONAL-GO** — reference for synthetic eval environments; not poker-specific |

## Narrative

Tmax trains terminal-using agents (bash/shell tasks) via compositional synthetic task generation + RL. Scores strongly on **Terminal-Bench 2.0** relative to prior open recipes at ≤32B parameters.

### Generation pipeline

- Tasks sampled as product of **9 structured axes** (domain, skills, complexity, verifier, etc.)
- Per-task Docker image + unit-test verifier + mini-SWE-agent harness
- **Skips expensive teacher validation** — RL soft-filters zero-pass-rate samples (<8/batch in paper)

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Poker `decide()` / dev.fun** | **NO-GO** — shell/terminal tasks, not NLHE |
| **Agent eval harness design** | CONDITIONAL — axis-composed synthetic tasks as pattern for regression suites |
| **HL analyst loop** | Dead end — different action space than hand history patches |

Phase-0 **GO** for reading Apache-2.0 repo as eval methodology reference; **NO-GO** for adoption as wagering bot.

## Snippets

> "Tmax outperforms prior work with open data … and dominates the Pareto curve for models under 32B parameters" on Terminal-Bench 2.0. [Source: arxiv:2606.23321 Figure 1 caption]

> "We deliberately skip teacher validation … RL training applies effective soft filtering." [Source: arxiv:2606.23321 §3.1]

## Dead Ends

- Train Tmax policy for poker arena submit
- Terminal-Bench score as TrueSkill proxy

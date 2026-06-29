---
title: Red Queen Gödel Machine — co-evolving agents and evaluators (arXiv 2606.26294)
type: source
tags: [source, arxiv, agents, self-improvement, evaluator, k133, rqgm]
keywords: [red-queen-godel-machine, rqgm, co-evolution, utility-evolution, agent-as-judge, non-stationary-eval]
related:
  - concepts/custom-agent-methodology.md
  - concepts/gambling-bot-architecture.md
  - concepts/poker-hl-analyst-loop.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md
  - sources/daily-digest-reject-cluster-k133-2026-06-29.md
  - sweeps/2026-06-29-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-29
updated: 2026-06-29
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.26294-2606-26294v1-the-red-queen-g-del-machine-co-evol.pdf
phase_0_verdict: CONDITIONAL-GO 2026-06-29 — paper-only; community MIT repro unvalidated (kingkillery/red-queen-godel-machine 2★); reference evaluator co-evolution pattern
---

## Relations

- @sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md — fixed tri-verifier baseline (K132)
- @sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md — anytime-valid eval CIs (K129)
- @sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md — K133 operator steals

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.26294](https://arxiv.org/abs/2606.26294) |
| **Title** | The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators |
| **Authors** | Iacob et al. (Cambridge, NVIDIA, Flower Labs, …) |
| **Repo** | No official release [TENTATIVE 2026-06-29]; community `kingkillery/red-queen-godel-machine` (MIT, ~2★, unvalidated) |
| **Phase-0** | **CONDITIONAL-GO** — ingest **framework** only; no FOSS adoption until author release |
| **Verdict** | **REFERENCE** — strip-mine controlled utility evolution for arena eval harness |

## Narrative

RQGM extends Gödel/Darwin self-improving agents by treating **evaluation as non-stationary**: agents and evaluators **co-evolve** instead of optimizing against a fixed benchmark forever.

| Mechanism | Description |
|-----------|-------------|
| **Controlled utility evolution** | Search split into **epochs** — utility fixed within epoch, updatable at boundaries; per-epoch improvement guarantees |
| **Learned evaluators** | Agent-as-judge signals complement verifiable tests (cheaper than multi-turn rollouts) |
| **Adversarial objectives** | Epoch-level utility edits correct evaluator blind spots (e.g. over-accepting AI-generated work) |

Reported gains [TENTATIVE — preprint]: coding pass rate ↑ vs prior SOTA with **1.35×–1.72×** fewer tokens; co-evolved paper reviewers **9%** higher ground-truth accuracy; writers **1.78×–1.86×** acceptance under diverse judge panel.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Researcher sandbox / HL loop** | **HIGH** — static regression gates go stale as `decide()` improves; epoch boundaries for eval utility refresh |
| **Fara verifier triad (K132)** | **HIGH** — co-evolve judge panel alongside policy patches; adversarial epoch for PvE over-acceptance |
| **TrueSkill HU LB** | **LOW** — venue metric fixed; steal is **private harness** only |
| **CeminiDFS / sportsbook bots** | NO-GO — not wagering-domain code |

Phase-0 **CONDITIONAL-GO**: reference design for private eval evolution; **NO-GO** deploying RQGM self-edit loop on prod `decide()` without competition rules review.

## Snippets

> "Their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves." [Source: arxiv:2606.26294 Abstract]

> "Controlled utility evolution: search is organized into epochs with a fixed within-epoch evaluation criterion, while the utility can be updated at epoch boundaries." [Source: arxiv:2606.26294 Abstract]

> Strongest baseline reviewer over-accepts AI-generated papers at up to **1.91×** the human rate; RQGM introduces an adversarial objective for equal stringency. [Source: arxiv:2606.26294 Abstract]

## Dead Ends

- RQGM recursive self-edit on live `cemini_decide.py` during active $50K event
- Co-evolving TrueSkill as public leaderboard metric
- Community MIT repro as production dependency without author validation

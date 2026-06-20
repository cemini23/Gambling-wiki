---
title: From Trainee to Trainer — LLM-designed RL training environments (arXiv 2606.17682)
type: source
tags: [source, arxiv, agent-engineering, rl, k123, hl-loop]
keywords: [trainee-to-trainer, environment engineer, MAPF-FrozenLake, multi-agent reasoning, Qwen]
related:
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/gambling-bot-architecture.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - sources/daily-digest-reject-cluster-k123-2026-06-20.md
  - sweeps/2026-06-20-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-20
updated: 2026-06-20
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.17682-2606-17682v1-from-trainee-to-trainer-llm-designe.pdf
phase_0_verdict: REFERENCE 2026-06-20 — LLM-as-env-engineer pattern; repo license NOASSERTION; not poker domain
---

## Relations

- @concepts/custom-agent-methodology.md — P3 offline iteration; env tuning between HL patches
- @concepts/poker-hl-analyst-loop.md — analog: analyze failures → change **test harness / opponent mix**, not runtime decide()
- @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md — K120 agent methodology anchor

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.17682](https://arxiv.org/abs/2606.17682) |
| **Repo** | [LARK-AI-Lab/Trainee-to-Trainer](https://github.com/LARK-AI-Lab/Trainee-to-Trainer) |
| **License** | **NOASSERTION** [NEEDS VERIFICATION 2026-06-20] — `gh api` 2026-06-20 |
| **Domain** | MAPF-FrozenLake multi-agent gridworld — **not NLHE** |
| **Verdict** | **REFERENCE** — offline env-engineering pattern only |

## Narrative

**LLM-as-Environment-Engineer:** current policy reads failure trajectories + context, proposes next-stage **training environment configuration**. Testbed MAPF-FrozenLake exposes multi-dimensional env knobs. Qwen3-4B backbone beats larger proprietary LLMs and fixed-env baselines on aggregate benchmark.

Key finding: **RL checkpoint is better env engineer than base model** — policy learning improves weakness diagnosis.

### Phase-0 audit (2026-06-20)

| Check | Result |
|-------|--------|
| License | NOASSERTION — do not install without LICENSE file review |
| Stars | ~19 |
| Poker fit | **NO-GO prod** — wrong domain |
| HL loop fit | **REFERENCE** — pattern for P3: failure report → adjust selfplay opponent roster / regression corpus / gate thresholds |

### Gambling-wiki application (offline only)

Map to **P3 HL analyst loop**, not P4 `decide()`:

1. Run Arena analyze or HU selfplay → failure report
2. LLM proposes **one** change to eval harness (opponent mix, gate KPI, regression spot)
3. P5 gate → deploy unchanged pure-code policy if only harness moved

**Dead end:** runtime LLM redesigning strategy inside `decide()`.

## Snippets

> "The current policy model analyzes failure trajectories together with contextual information and proposes modifications to the next-stage training environment configuration." [Source: arxiv:2606.17682 abstract]

> "The current RL checkpoint serves as a better environment engineer than the original base model." [Source: arxiv:2606.17682 abstract]

## Dead Ends

- Training NLHE policy end-to-end via MAPF-FrozenLake code — wrong testbed
- Prod dependency on NOASSERTION repo without license verify

---
title: Beyond the Training Distribution — model eval under shift and selection bias (arXiv 2606.14506)
type: source
tags: [source, arxiv, evaluation, distribution-shift, k125, backtest]
keywords: [covariate shift, selective labels, pre-deployment eval, double machine learning, target risk]
related:
  - concepts/poker-hl-analyst-loop.md
  - concepts/dfs-backtesting-framework.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/daily-digest-reject-cluster-k125-2026-06-22.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sweeps/2026-06-22-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-22
updated: 2026-06-22
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.14506-2606-14506v1-beyond-the-training-distribution-ev.pdf
phase_0_verdict: REFERENCE 2026-06-22 — pre-deploy eval under shift; not wagering-specific
---

## Relations

- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — F9–F11 eval vs Playground opponent mismatch
- @concepts/poker-hl-analyst-loop.md — optimize vs live analyze, not selfplay alone
- @concepts/dfs-backtesting-framework.md — walk-forward / regime shift analog

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.14506](https://arxiv.org/abs/2606.14506) |
| **Domain** | Healthcare ML — covariate shift + selective labels |
| **Verdict** | **REFERENCE** — eval methodology steal, not domain content |

## Narrative

Studies **pre-deployment model evaluation** when (i) target covariate distribution differs from training (covariate shift) and (ii) outcome labels are **selectively observed** based on historical decisions. Proposes double-ML estimator for target risk under general loss; eICU experiments.

### Gambling-wiki steals (eval discipline)

| Paper concept | Arena / DFS analog |
|---------------|-------------------|
| Covariate shift | Selfplay opponent mix ≠ Researcher sandbox pool ≠ Playground fish |
| Selective labels | Only analyze **worst** hands (selection bias if metrics computed on cherry-picked spots) |
| Target risk before deploy | HU gate must estimate performance on **target** opponent distribution, not training panel |

Supports K118 doctrine: **separate eval cadences** for DeepCFR panel, Playground analyze, and TrueSkill HU sandbox — do not merge metrics without shift correction.

## Snippets

> "Two common sources of model performance degradation are covariate shift... and selective labels, where the observability of outcomes depends on historical decisions." [Source: arxiv:2606.14506 abstract]

## Dead Ends

- Ingesting as sports betting or poker strategy content — healthcare prediction paper
- Using as license to skip live-analyze gates — paper argues for **better** pre-deploy estimation, not fewer checks

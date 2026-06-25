---
title: CELEUS — certifiable LLM evaluation via e-processes (arXiv 2606.20820)
type: source
tags: [source, arxiv, evaluation, llm, k129, celeus]
keywords: [celeus, e-process, anytime-valid, confidence-interval, surrogate, uncertainty-guided-sampling]
related:
  - sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/dfs-backtesting-framework.md
  - concepts/custom-agent-methodology.md
  - sources/daily-digest-reject-cluster-k129-2026-06-25.md
  - sweeps/2026-06-25-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-25
updated: 2026-06-25
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.20820-2606-20820v1-celeus-certifiable-and-efficient-ll.pdf
phase_0_verdict: REFERENCE 2026-06-25 — academic eval framework; no prod repo required
---

## Relations

- @sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md — K125 shift/selective-label eval line
- @sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md — operator steal summary (K129)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.20820](https://arxiv.org/abs/2606.20820) |
| **Title** | CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes |
| **Verdict** | **REFERENCE** — anytime-valid eval CIs for agent benchmarks |

## Narrative

Prior certifiable LLM eval methods update confidence intervals sequentially but may **fail anytime-valid coverage** when stopping rules depend on the CIs themselves. CELEUS uses **e-processes** to build CIs that remain valid under adaptive stopping.

### Mechanism

| Ingredient | Role |
|------------|------|
| **Uncertainty-guided sampling** | Select informative eval samples from pool |
| **Surrogate-assisted completion** | Fill unevaluated pool items with surrogate risk scores |
| **E-process inversion** | Anytime-valid CI for finite-pool risk at level α₁ |
| **Pool-to-population correction** | Separate budget α₂ for i.i.d. finite-sample gap |

Per-round inferential signal combines observed risks on evaluated samples with inverse-probability-weighted surrogate residuals on the selected item.

### Gambling-wiki relevance

| Lane | Fit |
|------|-----|
| **Poker arena eval gates (K125)** | REFERENCE — principled stopping when TrueSkill/HU panel budget is limited |
| **DFS backtest reporting** | REFERENCE — don't treat holdout slice metrics as population truth without CI |
| **Runtime `decide()`** | **NO-GO** — offline eval methodology only |

Complements distribution-shift discipline (K125): CELEUS addresses **how much eval to run**; 2606.14506 addresses **which distribution the metric lives on**.

## Snippets

> "Existing methods are not generally anytime-valid: the claimed coverage (e.g., 95%) may fail when CIs are repeatedly updated and used to decide when to stop." [Source: arxiv:2606.20820 abstract]

> "CELEUS leverages e-processes to build anytime-valid CIs … with uncertainty-guided sampling and surrogate-assisted approximations." [Source: arxiv:2606.20820 abstract]

## Dead Ends

- CELEUS leaderboard rank as copy-trading signal
- Replacing pytest regression spots with surrogate-only eval

---
title: Betting on Bets — anytime-valid stochastic dominance tests (arXiv 2604.21851)
type: source
tags: [source, arxiv, sports-betting, bankroll, statistics, k148, e-process]
keywords: [stochastic-dominance, anytime-valid, e-process, strategy-comparison, record-keeping]
related:
  - concepts/bankroll-management.md
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/daily-digest-batch-k148-2026-07-06.md
  - sweeps/2026-07-06-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-06
updated: 2026-07-06
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2604.21851-betting-on-bets-anytime-valid-tests-for-stochast.pdf
phase_0_verdict: REFERENCE 2026-07-06 — paper-only; e-process SD tests for sequential strategy monitoring
---

## Relations

- @concepts/bankroll-management.md — journal / process monitoring
- @sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md — shared e-process family (K129 eval, not wagering)

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2604.21851](https://arxiv.org/abs/2604.21851) |
| **Verdict** | **REFERENCE** — sequential **anytime-valid** tests for **stochastic dominance** between uncertain prospects |

## Narrative

Develops **e-process / e-variable** tests for first- and higher-order **stochastic dominance** — valid under continuous monitoring (unlike fixed-sample SD tests). Useful when comparing **full return distributions**, not just mean ROI — e.g. strategy A vs B with similar averages but different tail risk.

| Gambling-wiki fit | Action |
|-------------------|--------|
| **Sports betting journal** | Monitor whether new process **dominates** old on per-bet P&L distribution |
| **Pick'em / props (K147)** | Compare slip-EV strategies with ordinal outcomes |
| **PM retail** | Distribution comparison beyond Brier point scores |
| **Prod bots** | NO-GO auto-deploy — research methodology for post-hoc gates |

**Adoption for David:** consider e-process SD monitoring when A/B testing **manual** betting or pick'em processes — not as live bet trigger.

## Snippets

> "How can we monitor, in real time, whether one uncertain prospect has any upside over another?" [Source: arxiv:2604.21851 Abstract]

## Dead Ends

- SD test pass ⇒ automatic +EV without vig/CLV
- Replacing flat unit bankroll rules with e-process bet sizing

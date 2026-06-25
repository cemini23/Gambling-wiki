---
title: K129 — CELEUS eval + Tmax terminal-agent steals
type: source
tags: [source, brief, evaluation, agents, k129]
keywords: [celeus, tmax, e-process, eval-stopping, terminal-bench]
related:
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
  - sources/arxiv-2606.23321-tmax-terminal-agents-2026-06-25.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
  - sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/dfs-backtesting-framework.md
  - concepts/custom-agent-methodology.md
  - sources/daily-digest-reject-cluster-k129-2026-06-25.md
maturity: validated
read_status: deep-read
created: 2026-06-25
updated: 2026-06-25
cross-wiki-source: "briefs/2026-06-25_k129-celeus-tmax-eval-steals.md"
---

## Relations

- @sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md — e-process anytime-valid CIs
- @sources/arxiv-2606.23321-tmax-terminal-agents-2026-06-25.md — synthetic terminal task RL
- @sources/brief-k125-eval-gate-discipline-2026-06-22.md — regime-separated eval gates

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K129 CELEUS + Tmax eval steals |
| **Date** | 2026-06-25 |

## Narrative

### CELEUS steal (2606.20820) — eval discipline

| Idea | Action |
|------|--------|
| Adaptive stopping invalidates naive CIs | When panel budget is limited (HU sandbox, regression suite), document **anytime-valid** stopping rules — don't peek-and-stop on point estimates |
| Surrogate + guided sampling | Pattern for cheap pre-screen before expensive hand sims — surrogate must not replace pytest gates |
| vs K125 shift paper | CELEUS = how much to evaluate; 2606.14506 = which distribution the metric describes |

### Tmax steal (2606.23321) — agent harness (conditional)

| Idea | Action |
|------|--------|
| Axis-composed synthetic tasks | Reference pattern for diverse regression spots — not NLHE tasks |
| Soft-filter RL data | Skip teacher validation when verifier exists — analogous to zero-gradient filter |
| Phase-0 | Apache-2.0 **CONDITIONAL-GO** strip-mine only |
| Poker arena | **NO-GO** — Terminal-Bench ≠ dev.fun |

### Operator checklist addendum

- [ ] Eval S1 / HU panel: note whether stopping rule is fixed-N or adaptive
- [ ] DFS backtest briefs: separate in-sample slice from population claim
- [ ] Do not conflate Tmax Terminal-Bench with TrueSkill HU

## Dead Ends

- CELEUS surrogate replacing human spot-check on worst Arena hands
- Deploy Tmax-trained agent as `cemini_decide()` bundle

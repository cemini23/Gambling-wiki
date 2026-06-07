---
title: "georgedouzas/sports-betting"
type: entity
tags: [entity, tool, steal-from, sports-betting, python, backtest, k90]
keywords: [georgedouzas, sports-betting, dataloader, backtest, scikit-learn, mit]
related:
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - concepts/sports-betting-fundamentals.md
  - concepts/line-shopping-and-clv.md
  - entities/platforms/pinnacle.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md"
---

## Relations

- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — K90 v6 Steal-from verdict
- @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — canonical eval
- @concepts/sports-betting-fundamentals.md — backtest methodology context
- @concepts/line-shopping-and-clv.md — CLV evaluation patterns
- @entities/platforms/pinnacle.md — sharp-line benchmark for backtests

## Raw Concept

Python **sports betting data + backtesting library** — historical odds loading, feature engineering, sklearn-compatible model training. K90 v6 **Steal-from**; supersedes rejected `pretrehr/Sports-betting` duplicate.

| Field | Value |
|-------|-------|
| **Repo** | `github.com/georgedouzas/sports-betting` |
| **License** | **MIT** [CONFIRMED 2026-05-31 via `gh api`] |
| **Eval tier** | Steal-from (gambling-wiki primary) |

## Narrative

### What it does

- Loads historical betting odds from public sources into pandas-friendly structures
- Provides backtesting scaffolding for moneyline/spread/total strategies
- Integrates with scikit-learn for model training and evaluation
- Reference for **methodology pages** — not a live odds API or sportsbook connector

### Why Steal-from (not Adopt)

- **MIT** — safe to strip-mine dataloader and backtest patterns
- Canonical fork per K90 eval; `pretrehr/Sports-betting` rejected as duplicate
- No prod sportsbook API integration; stale-line risk if used naively for live betting
- Patterns belong in gambling-wiki study workflows, not CeminiSuite execution

### Phase-0 checklist [NEEDS VERIFICATION 2026-06-07]

1. Pin version; verify data source freshness and jurisdiction coverage
2. Backtest with **Pinnacle closing lines** as CLV benchmark (`@entities/platforms/pinnacle.md`)
3. Account for vig in ROI calculations (`@concepts/vig-and-hold.md`)
4. Compare vs paid data feeds before sizing real bankroll

### Verdict

**STEAL-FROM** — reference implementation for historical odds backtesting; **CONDITIONAL-GO** for personal research; **NO-GO** for unattended live betting.

## Snippets

> georgedouzas/sports-betting — MIT; dataloader / backtest patterns. [Source: @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

> pretrehr/Sports-betting — Reject upheld — duplicate of georgedouzas/sports-betting (steal-from). [Source: @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

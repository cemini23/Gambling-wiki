---
title: "fred4jupiter/fredbet"
type: entity
tags: [entity, tool, steal-from, social-betting, open-source, k90]
keywords: [fredbet, social-betting, pool-betting, open-source, mit]
related:
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - concepts/sports-betting-fundamentals.md
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
---

## Relations

- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — K90 v6 Steal-from verdict
- @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — canonical eval
- @concepts/sports-betting-fundamentals.md — pool/social betting UX context

## Raw Concept

Open-source **social betting application** — pool bets, user accounts, leaderboard-style interaction. K90 v6 **Steal-from** for UX patterns, not prod deploy.

| Field | Value |
|-------|-------|
| **Repo** | `github.com/fred4jupiter/fredbet` |
| **License** | **MIT** [CONFIRMED 2026-05-31 via `gh api`] |
| **Eval tier** | Steal-from (gambling-wiki primary) |

## Narrative

### What it is

FredBet is a self-hosted social betting platform: users create pools, place picks, and compete on leaderboards. Distinct from **sportsbook line-shopping** or **PM CLOB** workflows — closer to office-pool / friend-group wagering UX.

### Why Steal-from (not Adopt)

- **MIT** license allows pattern extraction without copyleft risk
- Useful reference for **social betting UX** (pool creation, stake display, settlement flows)
- Not maintained for US regulated sportsbook integration; no CLV/odds-feed pipeline
- Out of scope for `@osint-wiki` PM bot stack

### Phase-0 checklist [NEEDS VERIFICATION 2026-06-07]

1. Confirm current release branch + last commit date
2. Map pool-bet settlement logic vs regulated sportsbook rules (push handling, void games)
3. Do **not** deploy with real-money rails without jurisdiction review

### Verdict

**STEAL-FROM** — strip-mine UX and pool-betting interaction patterns for gambling-wiki methodology; **NO-GO** for prod sportsbook or PM execution.

## Snippets

> fred4jupiter/fredbet — Steal-from, MIT; gambling-wiki steal-from (social betting app patterns). [Source: @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

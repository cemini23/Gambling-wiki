---
title: WagerBrain (sedemmler)
type: entity
tags: [entity, bot, sportsbook, automation, steal-from]
keywords: [wagerbrain, sedemmler, quoter, bankroll, k92]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/bankroll-management.md
  - concepts/kelly-criterion-betting.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - entities/bots/README.md
  - entities/bots/bovada-api-reference.md
  - concepts/sequential-optimal-execution-quoting.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 eval Steal-from
- @concepts/gambling-bot-architecture.md — quoter module pattern
- @entities/bots/bovada-api-reference.md — sportsbook API lane

## Raw Concept

- **Repo**: `github.com/sedemmler/WagerBrain`
- **Eval**: K92 Steal-from — world-cup-bot module 3 (quoter) overlap (OSINT)

## Narrative

Python library for **sports-betting math** after odds scrape: `bankroll.py`, `odds.py`, `probs.py`, `payouts.py`. Not a live bot — **requirements reference** for bankroll/Kelly-style sizing on gambling-bot fleet.

### Phase-0 audit (2026-06-01)

Clone: `/tmp/k92-phase0/WagerBrain`

| Check | Result |
|-------|--------|
| License | **MIT** (`LICENSE` + `gh api` SPDX) |
| Maturity | 304★ / 41 forks / 3 open issues |
| Activity | **Stale** — last push **2020-05-02** |
| Failure mode | Unmaintained API assumptions; not a deployment stack |
| Cemini overlap | Math only — strip bankroll/odds helpers; prod quoter stays Python-native on @osint-wiki |

**Verdict: CONDITIONAL-GO (steal-from, gambling-wiki requirements only)** — port **ideas** (bankroll, implied prob, payout math) into bot specs; **do not** pip-install as prod dependency without maintenance fork. Pair with @osint-wiki/concepts/sequential-optimal-execution-quoting.md for LOB quoter theory.

## Snippets

> "A package containing the essential math and tools required for sports betting and gambling." [Source: WagerBrain README]

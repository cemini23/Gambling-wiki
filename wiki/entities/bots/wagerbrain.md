---
title: WagerBrain (sedemmler)
type: entity
tags: [entity, bot, sportsbook, automation, steal-from]
keywords: [wagerbrain, sedemmler, quoter, bankroll, k92]
related:
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md"
  - "@osint-wiki/concepts/sequential-optimal-execution-quoting.md"
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 eval Steal-from
- @concepts/gambling-bot-architecture.md — quoter module pattern

## Raw Concept

K92 tool eval flagged **sedemmler/WagerBrain** as Steal-from for Cemini financial / world-cup-bot **module 3 (quoter)**. Gambling-wiki captures **wagering automation requirements**; prod code stays @osint-wiki.

## Narrative

**Phase-0:** **CONDITIONAL-GO** — pending `gh api` license verification and repo activity check before clone.

**Strip-mine targets (requirements only):**

- Bankroll-aware quote/sizing logic for sportsbook-style markets
- Signal → stake mapping discipline (align with @concepts/kelly-criterion-betting.md)

**Not in scope:** Treating as production dependency without license + ToS review.

## Snippets

> Eval overlap: "Extends module 3 (quoter)." [Source: GitHub Repo Evaluation for Cemini.docx, K92]

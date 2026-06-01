---
title: "matt57225/bovada-hand-history-converter"
type: entity
tags: [entity, bot, sportsbook, analytics, steal-from, k92]
keywords: [bovada, hand-history, clv, journal, k92]
related:
  - entities/bots/bovada-api-reference.md
  - entities/bots/README.md
  - concepts/line-shopping-and-clv.md
  - concepts/gambling-bot-architecture.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @entities/bots/bovada-api-reference.md — same sportsbook API lane
- @concepts/line-shopping-and-clv.md — CLV logging use case
- @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md — K92 Steal-from

## Raw Concept

K92 **Steal-from** for **hand-history ingest** — analytics / CLV journal bot, not auto-bet execution.

## Narrative

### Use case

- Parse Bovada hand histories into structured format for **CLV tracking** and bet journal
- Pairs with `@concepts/line-shopping-and-clv.md` discipline
- **Human-in-the-loop** default — no auto-submit

### Phase-0 [NEEDS VERIFICATION 2026-06-01]

1. `gh api` license
2. Bovada **ToS** on automated history export
3. Compare vs manual CSV / official tools

### Verdict

**STEAL-FROM** for **analytics bot** lane — **CONDITIONAL-GO** for live account use.

## Snippets

> K92 Steal-from — hand-history converter for CLV / journal ingest. [Source: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md]

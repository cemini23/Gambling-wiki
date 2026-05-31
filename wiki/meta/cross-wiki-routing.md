---
title: Cross-wiki routing (gambling vs osint)
type: concept
tags: [meta, routing, federation]
keywords: [routing, osint-wiki, ingest]
related:
  - concepts/gambling-wiki-scope.md
maturity: core
created: 2026-05-31
updated: 2026-05-31
---

## Relations

- @concepts/gambling-wiki-scope.md — full boundary table

## Raw Concept

Ingest routing checklist when a source touches both wagering strategy and Cemini trading infrastructure.

## Narrative

### Stay in gambling-wiki

- Sportsbook/DFS/casino/poker strategy
- Bankroll, Kelly (general), vig, CLV, FLB (general)
- PM/Kalshi **product** docs (fees, rules, retail behavior)
- GitHub repos for **DFS optimizers**, **arb finders (alert-only)**, **poker solvers**

### Route to @osint-wiki (stub + brief)

- Polymarket/Kalshi **bot code**, LP farming, copy-trading executors
- CeminiSuite, World Cup bot, conductor/librarian infra
- Regulatory briefs for **trading stack** (CFTC, DCM preemption)
- Macro/equity OSINT unrelated to betting

### Both wikis

- Kelly, FLB, cross-venue PM — write general here, link implementation there
- MomentumOdds, Odds Jam — tool entity in both with split narrative

### Bulk URL evaluation (Gemini DR)

Use `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v6) — eight surfaces; **gambling-wiki** = surface 3. OSINT workspace: `python3 scripts/cross_wiki_route.py --target-wiki gambling-wiki` when routing off-topic from OSINT ingest.

### Command

## Snippets

*(none)*

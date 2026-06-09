---
title: Cross-wiki routing (gambling vs osint)
type: concept
tags: [meta, routing, federation, bots]
keywords: [routing, osint-wiki, ingest, gambling-bot]
related:
  - concepts/gambling-wiki-scope.md
  - concepts/gambling-bot-architecture.md
  - meta/gambling-bot-ingest-rubric.md
  - meta/daily-research-digest-cadence.md
  - sources/brief-k93-federated-digest-2026-06-01.md
maturity: core
created: 2026-05-31
updated: 2026-06-07
---

## Relations

- @concepts/gambling-wiki-scope.md — full boundary table
- @concepts/gambling-bot-architecture.md — planned automation program
- @meta/gambling-bot-ingest-rubric.md — bot ingest checklist
- @meta/daily-research-digest-cadence.md — K93 federated morning digest

## Raw Concept

Ingest routing checklist when a source touches wagering strategy, **gambling automation**, or Cemini trading infrastructure.

## Narrative

### Stay in gambling-wiki

- Sportsbook/DFS/casino/poker strategy
- Bankroll, Kelly (general), vig, CLV, FLB (general)
- PM/Kalshi **product** docs (fees, rules, retail behavior)
- GitHub repos for **DFS optimizers**, **arb finders (alert-only)**, **poker solvers**
- **Gambling bot** design: APIs, ToS, latency, signal→order, per-platform lanes, FOSS Phase-0
- Tool evals (K90-style) for **wagering** OSS — even if osint also ingests PM cluster

### Route to @osint-wiki (stub + brief)

- CeminiSuite **prod** config, conductor, librarian infra
- Bot **implementation** (CeminiSuite deploy, `cemini_decide`, arena HL scripts) — private `llm-wiki-by-cemini/agents/`
- Regulatory briefs for **institutional trading stack** at full depth
- Macro/equity OSINT unrelated to betting

### Both wikis (bidirectional)

- Kelly, FLB, cross-venue PM — general here, implementation there
- MomentumOdds, Odds Jam — tool entity in both with split narrative
- **PM/Kalshi bots** — requirements + retail constraints **here**; code + prod **there**
- **dev.fun arena bot** — venue + HL workflow **here**; `decide()` + deploy **there**
- World Cup automation — retail contract types here; bot v1 there

### Gambling-bot ingest

Use `@meta/gambling-bot-ingest-rubric.md` when source mentions automation, scrapers, APIs, or bot repos. Create `entities/bots/<slug>.md` when a lane gets a named design or repo.

### Bulk URL evaluation (Gemini DR)

Use `@ccc-wiki/concepts/deep-research-evaluation-prompt.md` (v6) — eight surfaces; **gambling-wiki** = surface 3. OSINT workspace: `python3 scripts/cross_wiki_route.py --target-wiki gambling-wiki` when routing off-topic from OSINT ingest.

## Snippets

*(none)*

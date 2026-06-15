---
title: Multi-wiki tool eval v8 K103 — poker/casino reject strip
type: source
tags: [source, tool-eval, poker, casino, reject, k103]
keywords: [poker-query-language, casinogame, poker-equity-playground, no-go, k103]
related:
  - concepts/gambling-bot-architecture.md
  - entities/bots/poker-bot-tooling.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - osint-wiki/entities/tools/poker-query-language.md
maturity: validated
read_status: deep-read
created: 2026-06-13
updated: 2026-06-13
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md"
---

## Relations

- @osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md — canonical OSINT eval
- @entities/bots/poker-bot-tooling.md — reject cluster table
- @entities/tools/devfun-poker-arena-starter-kit.md — positive Arena path (K102)

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | `briefs/2026-06-07_k103-gambling-poker-reject-cluster-from-osint.md` |
| **Routed** | 2026-06-13 (K114 close-out) |
| **Cluster** | Poker-Query-Language + casino playgrounds |

## Narrative

K103 Gemini eval **poker/casino strip** — document reject cluster only; **no bot adoption**.

### Phase-0 verdicts [CONFIRMED — brief + OSINT eval]

| Repo | Eval tier | Verdict | Notes |
|------|-----------|---------|-------|
| solve-poker/Poker-Query-Language | Steal-from | **NO-GO** | ~4★ WIP; immature query language |
| ToNiePiter/casinogame | Reject | **Reject** | No license |
| alfredzimmer/poker-equity-playground | Reject | **Reject** | Playground only; no license |

### Action

- Cross-wiki stub: `@osint-wiki/entities/tools/poker-query-language.md`
- No laptop venv install, no prod gambling bot brief
- Arena entry remains `@entities/tools/devfun-poker-arena-starter-kit.md` (MIT)

## Dead Ends

- **PQL install for prod bot** — NO-GO until maturity + license verified
- **Casinogame / equity playground** — Reject tier; no Phase-0 path

---
title: Gambling bot ingest rubric
type: concept
tags: [meta, ingest, bots, automation]
keywords: [ingest, gambling-bot, routing, phase-0, foss]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/gambling-wiki-scope.md
  - entities/bots/README.md
  - meta/cross-wiki-routing.md
maturity: core
created: 2026-05-31
updated: 2026-06-07
---

## Relations

- @entities/bots/README.md — per-bot entity stubs
- @concepts/gambling-bot-architecture.md — fleet vision and platform lanes
- @meta/cross-wiki-routing.md — osint vs gambling split

## Raw Concept

Checklist for ingesting sources that touch **wagering automation** into gambling-wiki (not only retail manual play).

## Narrative

### When to create / update gambling-bot pages

Trigger on any of:

- GitHub repo for sportsbook, PM, DFS, or arb **bot/scraper/automation**
- YouTube/doc describing **bot workflow** on a wagering platform
- Tool eval (K90-style) with **Steal-from / Adopt** for gambling automation
- API docs for **DraftKings, FanDuel, Kalshi, Polymarket**, odds aggregators used as bot inputs

### Per-source checklist

1. **Classify lane** — sportsbook | PM/Kalshi | DFS | casino (usually dead end) | cross-cutting
2. **Create or update** — `entities/bots/<name>.md` if repo/product-specific; else add section to `@concepts/gambling-bot-architecture.md` or platform entity
3. **Capture** — API, ToS risk, latency, alert vs auto, license, Phase-0 verdict
4. **Cross-wiki** — if Cemini prod code exists, stub on @osint-wiki + link; **do not** move wagering logic out of gambling-wiki
5. **Link strategy** — bankroll, Kelly, CLV, divergence concepts as applicable
6. **Log** — append `wiki/log.md` with bot-related ingest tag

### Phase-0 (required for Adopt)

Same as `CLAUDE.md`: pricing, TOS, license (`gh api`), failure mode, compare existing wiki coverage. Record **GO / CONDITIONAL-GO / NO-GO** on entity page.

### Split with @osint-wiki

| Save here | Save there |
|-----------|------------|
| What to bet/automate and why | How Cemini deploys it |
| Retail +EV constraints, fee math | Orchestrator, secrets, prod MCP |
| FOSS eval for gambling-wiki strip-mine | Full bot codebase narrative |
| Per-platform bot **requirements** | Per-platform bot **implementation** (e.g. `agents/devfun-poker-arena/`) |

## Snippets

*(none)*

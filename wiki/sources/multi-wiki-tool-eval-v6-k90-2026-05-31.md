---
title: Multi-wiki tool eval v6 K90
type: source
tags: [source, tool-eval, k90, cross-wiki, gemini-deep-research]
keywords: [georgedouzas, fredbet, atpbetting, weather-bot-graveyard, steal-from, k90]
related:
  - concepts/gambling-bot-architecture.md
  - concepts/polymarket-weather-wagering-retail.md
  - concepts/sports-betting-fundamentals.md
  - entities/tools/fredbet.md
  - entities/tools/sports-betting-georgedouzas.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
maturity: draft
read_status: deep-read
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md"
---

# Multi-wiki tool eval v6 K90

## Relations

- @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — canonical full eval (41 URLs, all surfaces)
- @entities/tools/sports-betting-georgedouzas.md — Steal-from
- @entities/tools/fredbet.md — Steal-from
- @concepts/polymarket-weather-wagering-retail.md — retail weather post routed from K90 Posts.docx

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Cemini Multi-Wiki Link Evaluation Report (Batch v6, May 2026) |
| **Author** | Gemini Deep Research (v6 multi-wiki eval prompt) |
| **Type** | docx |
| **Location** | `cemini-librarian:/opt/cemini-bulk/research/multi-wiki-tool-eval-v6-k90-2026-05-31.docx` |
| **Retrieved** | 2026-05-31 |
| **Read status** | deep-read — gambling-wiki slice extracted; full body on `@osint-wiki` |

## Narrative

K90 v6 is the **first eval batch with gambling-wiki as a dedicated surface**. Of 41 URLs evaluated across eight wiki targets, **eight URLs are gambling-primary**. Canonical aggregate tiers and OSINT/CCC/SEO routing live on `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`.

### Gambling-wiki outcomes [CONFIRMED 2026-05-31]

| Tier | Repo | License (`gh api`) | Action |
|------|------|-------------------|--------|
| **Steal-from** | georgedouzas/sports-betting | MIT | Dataloader + backtest patterns → `@entities/tools/sports-betting-georgedouzas.md` |
| **Steal-from** | fred4jupiter/fredbet | MIT | Social/pool betting UX → `@entities/tools/fredbet.md` |
| Reference-only | edouardthom/ATPBetting | null | Tennis ML models; no LICENSE file — cite only, no install |
| Reject | pretrehr/Sports-betting | MIT | Duplicate of georgedouzas fork |
| Reject | Lisandro79/BeatTheBookie | GPL-3.0 | Copyleft poison pill |
| Reject | MoonsatProtocol/Polymarket-Weather-Bot | null | Weather-bot graveyard |
| Reject | ryankrumenacker/sports-betting-arbitrage-project | null | Tutorial quality |
| Reject | llSourcell/ChatGPT_Sports_Betting_Bot | null | Tutorial quality |

### Weather-bot graveyard (do not re-evaluate)

Five **UNAVAILABLE** + four **Reject** weather-bot GitHub paths in this batch alone. OSINT retains bot architecture; gambling-wiki gets **retail posture only** via `@concepts/polymarket-weather-wagering-retail.md` (K90 Posts.docx Post 15).

### Scope boundary

- **In scope here:** retail wagering OSS, backtest reference libs, social-betting UX patterns
- **Out of scope:** PM bot adopt (Harrier, polybot, polymarket-skills), FinRL/AlphaPy → Cemini financial, CCC agent harnesses

## Snippets

> "v6 protocol adds Gambling wiki as surface 3 — retail wagering and sports-betting OSS only; OSINT retains PM bots and CeminiSuite integration." [Source: multi-wiki-tool-eval-v6-k90-2026-05-31.docx via @osint-wiki]

> "Weather-bot GitHub URLs remain a high-noise cluster: seven UNAVAILABLE rows in a single batch." [Source: multi-wiki-tool-eval-v6-k90-2026-05-31.docx via @osint-wiki]

## Dead Ends

- **Weather-bot repos** (PolyWeather AGPL, MoonsatProtocol, hydra-node, etc.) — graveyard; do not Phase-0
- **pretrehr/Sports-betting** — same MIT library family as georgedouzas; use georgedouzas fork only
- **BeatTheBookie** — GPL-3.0; incompatible with strip-mine posture

---
title: Stokastic (DFS tools)
type: entity
tags: [entity, tool, dfs, nfl, fanduel, paid, w8]
keywords: [stokastic, awesemo, dfs-sims, ownership, nfl-core, gpp]
related:
  - concepts/dfs-strategy-overview.md
  - concepts/dfs-pipeline-integration-spec.md
  - concepts/dfs-paid-tool-methodologies.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/dfs-backtesting-framework.md
  - sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md
  - entities/platforms/fanduel.md
  - entities/tools/pydfs-lineup-optimizer.md
  - entities/tools/fantasylabs-dfs.md
  - sources/web-dfs-hero-nfl-gpp-strategy-2026-06-20.md
  - sources/brief-k169-nfl-week1-ready-2026-08-31.md
  - sweeps/2026-06-20-tier2-w8-nfl.md
maturity: validated
created: 2026-06-20
updated: 2026-08-31
---

## Relations

- @entities/platforms/fanduel.md — primary W8 FanDuel GPP lane
- @entities/tools/pydfs-lineup-optimizer.md — FOSS lineup gen fed by Stokastic CSV export
- @entities/tools/fantasylabs-dfs.md — alternate paid tool
- @concepts/dfs-strategy-overview.md — GPP / ownership framework
- @sources/brief-k169-nfl-week1-ready-2026-08-31.md — Week-1: CSV export only; do not scrape Sims HTML

## Raw Concept

**Stokastic** (formerly Awesemo) — paid DFS platform: projections, **ownership**, contest **simulations**, boom/bust, top stacks. Operator **recommended** paid tool for FanDuel NFL GPP (W8 Phase-0, 2026-06-20).

| Field | Value |
|-------|-------|
| **URL** | https://www.stokastic.com/ |
| **NFL packages** | **Core** (sims up to ~1k lineups) · **Max** (up to ~10k sims) [Source: stokastic.com NFL 2025 tools post] |
| **Export** | Spreadsheet / CSV download for members [CONFIRMED — FAQ + product copy] |
| **API / MCP** | **None public** — browser export only |
| **Integration** | CSV → `research to be indexed/` → `@scripts/fanduel_slate_optimize.py` or Cursor skill `@.cursor/skills/nfl-fanduel-slate-prep/` |

## Narrative

### Phase-0 verdict

**CONDITIONAL-GO** — operator primary paid DFS tool for **FanDuel NFL GPP/MME**. Not for Underdog BBM7 (draft-and-hold) or Hard Rock sportsbook.

| Check | Result |
|-------|--------|
| FanDuel NFL support | Yes — half-PPR main + showdown |
| Ownership projections | Core product claim; industry reputation strong |
| Contest sims vs classic optimizer | Sims-first (aligns with K124 GPP playbook) |
| CSV export | Yes — spreadsheet download |
| Public API / MCP | **NO-GO** — no official integration |
| ToS automation | Do not scrape; manual export only |
| Pricing | Tiered Core/Max; exact $ [NEEDS VERIFICATION at signup — promo code SPLASH often 15% off per third-party promos] |

### When worth paying (operator W8)

- **Yes:** 20–150 FanDuel GPP lineups/week; need ownership + sim ROI before upload
- **No:** BBM7-only season; single-entry only with hand builds; preseason trial not started

### Workflow (wiki + Cursor)

1. Export Stokastic NFL main-slate CSV after Fri injury news
2. Drop in `research to be indexed/fanduel-nfl-YYYY-MM-DD.csv`
3. Run skill **nfl-fanduel-slate-prep** or `python3 scripts/fanduel_slate_optimize.py`
4. Upload output CSV to FanDuel; log results in bankroll journal

### vs FantasyLabs

Stokastic = **sim/ownership-first** for GPP leverage. FantasyLabs = strong **CSV export + Koerner models + ETR bundle** — see @entities/tools/fantasylabs-dfs.md. Pick one primary paid tool to avoid duplicate spend.

## Snippets

> "When you become a Stokastic member, you'll have the option to download the data in spreadsheet format." [Source: https://www.stokastic.com/nfl (retrieved 2026-06-20)]

> "Core packages bring the ground-breaking NFL Sims Tools… simulate up to 1,000 lineups. Max… up to 10,000 lineups." [Source: https://www.stokastic.com/nfl/new-nfl-dfs-tools-2025-sims-projections-much-much-more-ac14/]

## Dead Ends

- **MCP server** — none; custom scraper NO-GO (ToS + fragility)
- **Best ball / Underdog drafts** — use W7 wiki + ETR timing, not Stokastic optimizer

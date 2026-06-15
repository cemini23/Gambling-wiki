# Gambling & Betting Research Wiki — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for **betting, gambling, and wagering strategy** — scoped to:

1. **Sports betting** — spreads, totals, moneylines, props, live betting, line shopping, CLV, sharp vs soft books, arbitrage and middles (where legal).
2. **Daily fantasy & season-long fantasy** — DFS (DraftKings/FanDuel), best ball, roster construction, ownership leverage, correlation stacks.
3. **Casino games** — poker (cash + MTT), blackjack, craps, roulette, baccarat, slots; house edge, bankroll, table selection, basic strategy.
4. **Prediction markets (consumer angle)** — Kalshi, Polymarket, and regulated event contracts **as wagering products**: fees, settlement, liquidity, behavioral edges.
5. **Gambling bots (planned)** — architecture, per-platform automation requirements, FOSS evals, signal→execution design, ToS/latency/failure modes. Likely a **fleet of platform bots** (sportsbook, PM/Kalshi, DFS) plus optional master orchestrator. **Wagering bot knowledge lives here**; CeminiSuite **prod deployment and existing PM bot code** stay in `@osint-wiki` — cross-link, don't duplicate implementation.
6. **Cross-cutting math & discipline** — Kelly criterion, fractional Kelly, vig/overround, FLB, variance, record-keeping, responsible-gambling guardrails.

The wiki is a librarian that **manages, curates, and applies** that knowledge:

- **Manage** — inventory raw sources (PDFs, books, course notes, repo snapshots, podcasts, YouTube transcripts); track what's been read, extracted, and applied
- **Curate** — pull relevant fragments into interlinked wiki pages on platforms, tools, games, sports, and concepts
- **Apply** — route findings to real workflows:
  - **claude.ai / Claude Desktop** — slate prep, strategy notes, hand-review frameworks, bankroll plans
  - **Hands-on use** — paste a brief into a DFS optimizer workflow, a poker study session, or a sports-betting journal

This is a laptop-first workspace. Raw sources archive to **`cemini-egress-fi:/opt/cemini-bulk/research/gambling/`** after ingest via OSINT `archive_raw_to_egress.sh`. Multi-wiki search uses sibling wiki folders on disk (see Related Wikis); **cemini-librarian bulk/rsync is retired** (2026-06).

## Scope boundary — vs `@osint-wiki`

| Topic | **This wiki (`gambling-wiki`)** | **`osint-wiki` (private)** |
|-------|----------------------------------|----------------------------|
| Sportsbook / casino / DFS strategy | **Primary home** | Cross-link only |
| Kelly, FLB, vig (general theory) | **Primary home** | PM-specific implementations + bot code |
| Kalshi / Polymarket **as products** (fees, rules, retail behavior) | **Primary home** | Regulatory + CeminiSuite execution |
| **Gambling bot program** (design, requirements, FOSS eval, per-platform lanes) | **Primary home** | Prod deploy + bot **code** (incl. dev.fun `cemini_decide`) |
| PM/Kalshi **LP, maker, institutional arb** at Cemini depth | Summary + cross-link | **Primary home** |
| World Cup bot, Cemini trading stack | Retail + bot requirements | **Implementation** |
| OSINT / macro / equity research | Out of scope | Primary home |

**Routing rule:** ingest here when the source teaches *how to bet or gamble better* **or what a gambling bot should automate* on a wagering platform (DraftKings, Kalshi, DFS, etc.). Route to `@osint-wiki` when the source is primarily *CeminiSuite prod deployment*, private credentials, or bot **codebase** operations — but still capture **wagering logic** on a gambling-wiki page or stub. **Never commit** dev.fun arena `decide()` patches, competition briefs, or live rank/leak stats to this public repo (see `agents/README.md`).

**Competition secrecy (dev.fun / $50K path):** public pages may describe venue rules and generic HL workflow only — not frequencies, env toggles, opponent profiles, or patch backlogs while events are live.

**Bot ingest:** follow `wiki/meta/gambling-bot-ingest-rubric.md` and `wiki/concepts/gambling-bot-architecture.md`.

## Architecture — three layers

1. **Raw sources** — immutable. You read them, never modify them.
   - Canonical long-term archive: `cemini-egress-fi:/opt/cemini-bulk/research/gambling/` (via OSINT `archive_raw_to_egress.sh`)
   - **Drop pattern**: drop new sources into `research to be indexed/` → ingest → archive to egress-fi (local copy removed on success)

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): slate cards, tournament prep, bankroll plans
- `research to be indexed/` — transient drop zone (gitignored)
- `LESSONS.md` — meta-lessons about *how we work*
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
Gambling-wiki/
  CLAUDE.md
  LESSONS.md
  ROADMAP.md
  hot.md                            # gitignored
  research to be indexed/           # gitignored drop zone
  raw-sources/                      # gitignored archive
  briefs/                           # gitignored
  agents/
    README.md                       # public stub only
    devfun-poker-arena/             # gitignored — canonical copy in @osint-wiki
  wiki/
    index.md
    log.md
    sources/
    entities/
      platforms/                    # DraftKings, FanDuel, Pinnacle, Kalshi, Polymarket, PokerStars, …
      tools/                        # OddsJam, Action Network, lineup optimizers, trackers
      bots/                         # planned platform bots (requirements; code on @osint-wiki)
      games/                        # poker, blackjack, craps, roulette, slots, baccarat
      sports/                       # NFL, NBA, MLB, soccer, tennis, …
      people/                       # authors, coaches, notable sharp bettors
    concepts/                       # bankroll, Kelly, FLB, DFS, best ball, house edge, …
    meta/                           # cadence pages, ingest rubrics
    sweeps/                         # daily research digest reports (discovery-only)
  scripts/                          # wiki_lint.py, daily_research_digest_run.py, preingest_check.py
  prompts/
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/games/poker/tournament-icm.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/platforms/draftkings.md
  - concepts/bankroll-management.md
maturity: draft | validated | core
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- `maturity`: `draft` → `validated` (cross-referenced + checked against sources) → `core` (battle-tested)
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline `@path/to/page.md` matching `related:` frontmatter; `@wiki-alias/...` for cross-wiki
- `## Raw Concept` — provenance
- `## Narrative` — synthesized understanding, neutral, well-sourced
- `## Snippets` — verbatim quotes / formulas / tables with citations
- `## Dead Ends` (optional) — what was tried and why it failed

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (relative to `wiki/`)
- Cross-wiki: `@osint-wiki/concepts/kelly-sizing-quarter.md`
- Bidirectional across wikis when feasible

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- Claim confidence: `[CONFIRMED]`, `[TENTATIVE]`, `[NEEDS VERIFICATION YYYY-MM-DD]`, `[RETRACTED]`

## Operations

### Ingest (adding a new source)

1. Drop into `research to be indexed/`
2. Run `python3 scripts/preingest_check.py` — duplicate detection
3. Read the source (or relevant sections)
4. **Discuss key takeaways with the user before writing**
4b. **Cross-wiki routing** — PM bot code / Cemini infra → `@osint-wiki` stub or brief; pure sportsbook/DFS/casino content stays here
5. Create `wiki/sources/<slug>.md`
6. Update entity + concept pages; bidirectional `related:`
7. Update `wiki/index.md` and append `wiki/log.md`
8. **Archive raw to egress-fi**: `bash "../../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id gambling "research to be indexed/<filename>"` — set source page `Location` to `cemini-egress-fi:/opt/cemini-bulk/research/gambling/<filename>`
9. Run `python3 scripts/wiki_lint.py` before commit

A single ingest should touch **3–15 pages**. Zero new pages → ask if the source is worth ingesting.

### Query

1. Read `wiki/index.md`
2. Read pages; follow `@relations`
3. Synthesize with citations; declare OOD gaps explicitly
4. File valuable synthesis back into wiki or `briefs/`

### Lint

```bash
python3 scripts/wiki_lint.py
```

Catches orphans, bidirectional gaps, dangling links, stale `[NEEDS VERIFICATION]`, cross-wiki resolution.

## External research

When the wiki can't answer, use Exa / Brave Search / fetch MCP (via `@osint-wiki` lazy-tool stack when OSINT folder is open). Cost discipline: 3–5 results for routine lookups.

## Distribution

Material ready to leave the wiki goes through `briefs/` first — copy to claude.ai or hands-on workflows. **Do not push prod trading config from this wiki**; that flows through `@osint-wiki` briefs → CeminiSuite.

## Phase-0 audit (before adopting a tool or paid service)

1. Read pricing, TOS, refund policy, and jurisdiction restrictions
2. Verify license for any FOSS repo (GitHub `gh api` — never trust docx evals alone)
3. Audit failure mode for tool class (stale lines, geoblock, account limits, -EV marketing)
4. Compare against existing wiki coverage
5. Record GO / CONDITIONAL-GO / NO-GO on the entity page

## Session-start ritual

### 0. Resume from hot.md

Read `hot.md`. One-line resume or offer to rebuild from `wiki/log.md` + `ROADMAP.md`.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

Mention count if user hasn't asked you to address items.

Keep checks under 60 seconds.

## Related Wikis

When a query needs data from another wiki, use `@wiki-alias/path/to/page.md`. Paths relative to this file's directory.

| Alias | Path | Visibility | Description |
|-------|------|------------|-------------|
| `gambling-wiki` | `../Gambling wiki/wiki/` | **Public** | Sports betting, casino, poker, DFS, best ball, consumer prediction-market wagering |
| `game-dev-wiki` | `../Game Dev wiki/wiki/` | **Public** | Hobby game dev — castle/RTS research, engine evals, agent harness |
| `osint-wiki` | `../../OSINT WORKSPACE/wiki/` | **Private** | Quant finance, PM/Kalshi bots, CeminiSuite, macro OSINT. Shared: Kelly, FLB, cross-venue arb |
| `ccc-wiki` | `../Cemini claude code CCC/wiki/` | **Public** | Agent workflow, MCP, skills, ingest tooling |
| `cybersecurity-wiki` | `../Cybersecurity wiki/wiki/` | Public | Minimal overlap |
| `seo-wiki` | `../SEO:GEO B&M Business/wiki/` | Public | Creator marketing when betting content overlaps X/YouTube |
| `image-gen-wiki` | `../Image gen/wiki/` | Public | Minimal overlap |
| `3d-printing-wiki` | `../3D printing/wiki/` | Public | Minimal overlap |

### Cross-wiki link syntax

- `@osint-wiki/entities/platforms/polymarket.md` — resolve by reading the other repo's files
- Bidirectional when both pages exist
- When creating a stub in another wiki, note dependency in `## Relations`

### Librarian sync (retired)

`cemini-librarian` Hetzner host **decommissioned 2026-06**. Canonical raw archive: **`cemini-egress-fi:/opt/cemini-bulk/research/gambling/`**; published wiki is this git repo + GitHub.

## Responsible gambling

This wiki documents **+EV discipline and risk management**. Pages assume the reader wagers only where legal, within bankroll limits, and with awareness of addiction resources. Do not optimize for compulsive play; flag -EV "systems" and martingale patterns as `[RETRACTED]` or Dead Ends.

---
title: Pick'em legal and ToS posture
type: concept
tags: [concept, pickem, props, legal, tos, w-legal, k147]
keywords: [scraping, manual-entry, cli, ledger, prizepicks-tos, underdog-tos, no-go]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/pickem-data-sources.md
  - concepts/pickem-operator-workflow.md
  - concepts/pickem-pipeline-integration-spec.md
  - sources/web-nfl-dfs-source-legal-posture-2026-06-20.md
  - entities/platforms/prizepicks.md
  - entities/platforms/underdog-pickem.md
  - entities/platforms/underdog-fantasy.md
  - entities/tools/ceminidfs.md
  - sources/daily-digest-rss-industry-2026-08-14.md
  - sources/daily-digest-rss-nfl-week0-2026-08-31.md
maturity: draft
created: 2026-07-05
updated: 2026-08-31
---

## Relations

- @concepts/nfl-dfs-data-sources.md — shared GO/NO-GO source matrix (FanDuel, DK, ESPN)
- @entities/tools/ceminidfs.md — BBM extension posture precedent (read-only overlay, no auto-submit)
- @entities/platforms/underdog-fantasy.md — extension lessons §6–7; pick'em is separate DOM/ToS surface
- @sources/daily-digest-rss-industry-2026-08-14.md — Colorado SB 26-131: prop ban stripped; 6-deposit cap
- @sources/daily-digest-rss-nfl-week0-2026-08-31.md — NFL/CFTC hostility to injury-adjacent PM contracts

## Raw Concept

**Non-negotiable legal and ToS bar** for K147 pick'em tool build. Mirrors CeminiDFS: local research tooling + manual wagering only. Platform pick'em lounges have **no licensed public API** — treat automation against app/web as high account and regulatory risk.

## Narrative

### Summary verdict

| Category | Verdict |
|----------|---------|
| Local CLI fair-value calculator | **OK** |
| Manual line entry + personal ledger | **OK** |
| Read-only browser overlay (Phase-2, after CLI graded) | **OK** — if no auto-submit, no credential harvest |
| Automated line scraping (any platform) | **NO-GO** |
| Auto-submit slips / bot wagering | **NO-GO** |
| API intercept on mobile apps | **NO-GO** |
| Credential stuffing / multi-account evasion | **NO-GO** |
| Unlicensed FOSS scraper repos | **REJECT** — do not vendor into pipeline |

### OK workflows (green light)

1. **Local CLI** — `prop-fair` reads nflverse + operator CSV; outputs `edges.csv` on disk only (@concepts/pickem-pipeline-integration-spec.md).
2. **Manual entry** — operator types or paste-imports posted lines from PrizePicks / UD app; append-only log (@concepts/pickem-data-sources.md § manual schema).
3. **Personal ledger** — track picks, results, bankroll for your own slips; no redistribution of platform data.
4. **Read-only overlay (deferred)** — display fair % next to manually viewed lines; user clicks platform UI to submit — same pattern as CeminiDFS BBM copilot intent.
5. **Licensed APIs** — nflverse, The Odds API, Open-Meteo per their terms (@concepts/nfl-dfs-data-sources.md).

### Colorado (Aug 2026) [CONFIRMED]

SB 26-131 in force: **six deposits per operator gaming day**, credit-card (incl. e-wallet) ban, push alerts only when the app is closed. The introduced **proposition-bet ban** and **winner-limit ban** were **stripped**. Player props / pick'em remain legal in CO unless the gaming commission later restricts a wager type on a governing-body petition. Deposit-count is **per book** with no dollar cap — a CO Hard Rock + FanDuel + UD stack is 18 deposits/day, not 6. `@sources/daily-digest-rss-industry-2026-08-14.md`.

### NO-GO workflows (hard stop)

| Action | Risk |
|--------|------|
| Scrape PrizePicks / Underdog / Sleeper line boards | ToS breach, account ban, possible CFAA-style exposure |
| Poll undocumented mobile/web endpoints | Same + brittle contract |
| Auto-fill or auto-submit pick slips | ToS + UIGEA-adjacent automation concerns |
| Harvest session tokens / reverse-engineer auth | Credential abuse |
| Resell or publish scraped line feeds | IP + contract |

**Operator consequence:** regulated-adjacent accounts (DFS, pick'em, sportsbook) share identity — one ban can cascade.

### REJECT list — FOSS / community scrapers

Do **not** evaluate for production use; cite as anti-patterns only:

| Repo | Issue | Cited in |
|------|-------|----------|
| `aidanhall21/underdog-fantasy-pickem-scraper` | **NO LICENSE** | CeminiDFS K129, architecture |
| `fantasydatapros/underdog` | **NO LICENSE** | CeminiDFS `docs/sleeper-sentiment-eval.md` |
| PrizePicks-oriented GPL scrapers (various) | No official API; license often unclear | Architecture platform matrix |

**Policy:** if GitHub `license` field empty or non-OSI — **REJECT** before code read (Phase-0 audit rule in CLAUDE.md).

### Platform ToS research checklist [NEEDS VERIFICATION]

Complete per @entities/platforms/prizepicks.md and @entities/platforms/underdog-pickem.md:

- [ ] Automated access / bot prohibition language
- [ ] Third-party tool allowances or prohibitions
- [ ] Data redistribution clauses
- [ ] Account sharing / multi-account rules
- [ ] State eligibility and pick'em vs sportsbook classification
- [ ] Responsible gaming tooling (limits) — document, do not bypass

Extract verbatim snippets to platform entity pages when validated; link here.

### Inherit from CeminiDFS / DFS legal scan

From @sources/web-nfl-dfs-source-legal-posture-2026-06-20.md and @concepts/nfl-dfs-data-sources.md:

- **FanDuel / DraftKings** — anti-scraper terms; **NO-GO** for automation (manual DFS export only in CeminiDFS).
- **ESPN undocumented endpoints** — **NO-GO** as backbone.
- **Ownership / paywall vendors** — manual export only.

Pick'em tool does **not** loosen any of the above; adds pick'em lounge surfaces as **manual-only** for posted lines.

### Extension deferral (W-INTEG)

Browser extension remains **Phase-2** until:

1. CLI + walk-forward grader trusted (@concepts/pickem-backtesting-framework.md)
2. Platform ToS excerpt reviewed for overlay allowance
3. No auto-submit in scope — @concepts/pickem-pipeline-integration-spec.md

BBM extension code stays in CeminiDFS repo — **do not fork** DOM selectors into pick'em without fresh Phase-0.

### Responsible gambling

Tool outputs **edges for discipline**, not volume maximization. Separate bankroll pool from DFS GPP and BBM — @concepts/bankroll-management.md. Flag −EV "systems" in ledger review.

## Snippets

> "OK: local CLI fair-value calculator; read-only browser overlay; manual line entry; ledger for your own picks." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md legal bar]

> "NO-GO: automated line scraping; auto-submit slips; credential stuffing; API intercept on mobile apps." [Source: same]

> "aidanhall21/underdog-fantasy-pickem-scraper — NO LICENSE" [Source: CeminiDFS K129 eval]

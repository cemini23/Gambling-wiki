---
title: DIY NFL pick'em & props tool — master research plan (K147)
type: source
tags: [source, research-plan, pickem, props, nfl, diy-model, k147]
keywords: [pickem, player-props, prizepicks, underdog, fair-value, research-plan, subagent-dispatch]
related:
  - concepts/diy-nfl-pickem-props-tool-architecture.md
  - concepts/diy-nfl-dfs-model-architecture.md
  - concepts/pickem-operator-workflow.md
  - concepts/pickem-pipeline-integration-spec.md
  - concepts/parlay-and-correlated-bets.md
  - concepts/kelly-criterion-betting.md
  - concepts/vig-and-hold.md
  - concepts/nfl-dfs-data-sources.md
  - concepts/dfs-distribution-layer.md
  - entities/platforms/prizepicks.md
  - entities/platforms/underdog-pickem.md
  - entities/sports/nfl-betting.md
  - entities/tools/ceminidfs.md
  - sources/fantasylabs-picklabs-launch-2026-07-05.md
  - sources/research-nfl-historical-odds-2026-06-20.md
maturity: draft
read_status: read
created: 2026-07-05
updated: 2026-07-05
---

## Relations

- @concepts/diy-nfl-pickem-props-tool-architecture.md — keystone synthesis target
- @concepts/diy-nfl-dfs-model-architecture.md — sibling pipeline (CeminiDFS); shared projection layers only
- @entities/tools/ceminidfs.md — **no pick'em code** in CeminiDFS repo

## Raw Concept

**Master research plan** for Phase-0 of a standalone NFL props / DFS pick'em fair-value tool (tentative: *CeminiPick*). Authored 2026-07-05. **14 workstreams · 14 subagents · 4 execution waves.** Research-only — **no new repo** until Phase-0 checklist ≥ 70% and operator GO on primary platform.

## Narrative

### Executive summary

Build a **research corpus + CLI spec** for binary O/U player props on PrizePicks-style lounges — not salary-cap DFS. Reuse CeminiDFS game-environment → usage → stat-projection → distribution layers; **discard** ownership, FD scoring, pydfs optimizer. New layers: fair `P(stat > line)`, platform payout implied probability, same-game slip correlation, fractional Kelly on whole slip. **No scrapers** — manual line entry or read-only overlay (deferred). Stokastic irrelevant; FantasyLabs PickLabs = paid benchmark only.

### Gate (before `github.com/cemini23/???`)

| Gate | Threshold |
|------|-----------|
| Phase-0 checklist | ≥ 70% items checked on architecture page |
| Platform decision | Primary lounge documented with payout tables |
| Legal | ToS posture **GO** for CLI + manual workflow |
| Economics | Breakeven hit rate per slip type quantified |
| Backtest design | Walk-forward spec + historical line source identified |

### Workstreams (14)

| ID | Title | Priority | Subagent | Deliverable |
|----|-------|----------|----------|-------------|
| W-PLATFORM-PP | PrizePicks platform Phase-0 | P0 | SA-01 | @entities/platforms/prizepicks.md → validated |
| W-PLATFORM-UD | Underdog Pick'em Phase-0 | P0 | SA-02 | @entities/platforms/underdog-pickem.md → validated |
| W-PAID-PICKLABS | PickLabs deep-read | P1 | SA-03 | @sources/fantasylabs-picklabs-launch-2026-07-05.md → validated |
| W-PAYOUT | Pick'em payout & breakeven math | P0 | SA-04 | @concepts/pickem-payout-and-breakeven.md (new) |
| W-FAIR-PROB | Fair P(over line) from distributions | P0 | SA-05 | @concepts/pickem-fair-probability.md (new) |
| W-SLIP-EV | Slip correlation + EV ranker | P0 | SA-06 | @concepts/pickem-slip-ev-and-correlation.md (new) |
| W-KELLY | Kelly sizing on multi-leg slips | P1 | SA-06 | Section in slip-EV page + @concepts/kelly-criterion-betting.md link |
| W-STAT-MAP | CeminiDFS stat → pick'em stat mapping | P0 | SA-07 | @concepts/pickem-stat-type-mapping.md (new) |
| W-DATA | Props data sources + historical lines | P0 | SA-08 | @concepts/pickem-data-sources.md (new) |
| W-LEGAL | ToS / scraping posture (pick'em) | P0 | SA-09 | @concepts/pickem-legal-and-tos-posture.md (new) |
| W-BACKTEST | Props walk-forward grader spec | P1 | SA-10 | @concepts/pickem-backtesting-framework.md (new) |
| W-WORKFLOW | Operator workflow (batch vs live) | P1 | SA-11 | Section in architecture + @concepts/pickem-operator-workflow.md (new) |
| W-INTEG | CLI + `edges.csv` integration spec | P1 | SA-12 | @concepts/pickem-pipeline-integration-spec.md (new) |
| W-ECON | Build vs buy + bankroll pool | P1 | SA-13 | Architecture economics section + bankroll cross-link |
| W-SYNTH | Keystone synthesis + wiki wiring | P0 | SA-14 | Architecture draft, index, log, ROADMAP, digest routing |

### Execution waves

```
Wave 0 (parallel): W-PLATFORM-PP, W-PLATFORM-UD, W-PAID-PICKLABS, W-LEGAL
Wave 1 (parallel): W-PAYOUT, W-STAT-MAP, W-DATA
Wave 2 (parallel): W-FAIR-PROB, W-SLIP-EV + W-KELLY
Wave 3 (parallel): W-BACKTEST, W-WORKFLOW, W-INTEG, W-ECON
Wave 4: W-SYNTH — merge, bidirectional links, wiki_lint
```

Cross-cutting: update @concepts/parlay-and-correlated-bets.md with pick'em lounge section (W-SLIP-EV).

### Subagent dispatch spec

#### SA-01 — PrizePicks (W-PLATFORM-PP)

- **Focus:** States/geo, NFL stat menu, Power/Flex payout tables, demon/goblin multipliers, push/void rules, ToS on third-party tools
- **Search:** prizepicks.com help/rules, state availability lists, responsible gaming
- **Output:** Expand `entities/platforms/prizepicks.md`; maturity `validated` if ≥6 checklist items filled with citations
- **Reject:** Any scraper repo without MIT/Apache license

#### SA-02 — Underdog Pick'em (W-PLATFORM-UD)

- **Focus:** Distinct from BBM; slip sizes, payouts vs PP, NFL stats, insurance/correlation features, ToS ix/x
- **Search:** underdogfantasy.com rules, help center, comparison articles
- **Output:** Expand `entities/platforms/underdog-pickem.md`
- **Reject:** aidanhall21/underdog-fantasy-pickem-scraper, fantasydatapros/underdog

#### SA-03 — PickLabs (W-PAID-PICKLABS)

- **Focus:** Pricing, platforms covered, edge definition, export/API, NFL coverage, build-vs-buy
- **Source:** https://www.fantasylabs.com/articles/picklabs-fantasylabs-new-tool-for-player-props-and-dfs-pickem-edges/
- **Output:** Deep-read `sources/fantasylabs-picklabs-launch-2026-07-05.md`

#### SA-04 — Payout math (W-PAYOUT)

- **Focus:** Implied probability from power/flex tables; breakeven hit rate per leg count; demon/goblin effective vig
- **Output:** New `concepts/pickem-payout-and-breakeven.md`

#### SA-05 — Fair probability (W-FAIR-PROB)

- **Focus:** `P(stat > line)` from marginals; adapt @concepts/dfs-distribution-layer.md; median trap warning
- **Output:** New `concepts/pickem-fair-probability.md`

#### SA-06 — Slip EV + Kelly (W-SLIP-EV, W-KELLY)

- **Focus:** Same-game QB+WR joint probability; independent vs correlated product; Kelly on whole slip
- **Output:** New `concepts/pickem-slip-ev-and-correlation.md`; patch `parlay-and-correlated-bets.md`

#### SA-07 — Stat mapping (W-STAT-MAP)

- **Focus:** Map CeminiDFS outputs → PrizePicks/UD stat types; combo props; K/DST gaps
- **Output:** New `concepts/pickem-stat-type-mapping.md`

#### SA-08 — Data sources (W-DATA)

- **Focus:** nflreadpy reuse, Odds API props, historical lines from @sources/research-nfl-historical-odds-2026-06-20.md, manual line log schema
- **Output:** New `concepts/pickem-data-sources.md`

#### SA-09 — Legal (W-LEGAL)

- **Focus:** Mirror CeminiDFS posture; OK vs NO-GO; platform ToS excerpts; scraper reject list
- **Output:** New `concepts/pickem-legal-and-tos-posture.md`

#### SA-10 — Backtest (W-BACKTEST)

- **Focus:** Walk-forward design, CLV vs hit rate, min 1 season, correlation calibration test
- **Output:** New `concepts/pickem-backtesting-framework.md`

#### SA-11 — Workflow (W-WORKFLOW)

- **Focus:** Pre-slate batch rank vs in-game live; injury latency; manual entry UX
- **Output:** New `concepts/pickem-operator-workflow.md`

#### SA-12 — Integration (W-INTEG)

- **Focus:** `prop-fair --player --stat --line` CLI; `edges.csv` schema; defer extension
- **Output:** New `concepts/pickem-pipeline-integration-spec.md`

#### SA-13 — Economics (W-ECON)

- **Focus:** PickLabs subscription vs DIY time; separate bankroll pool; breakeven vs model error
- **Output:** Economics subsection in architecture; link @concepts/bankroll-management.md

#### SA-14 — Synthesis (W-SYNTH)

- **Focus:** Upgrade architecture stub → draft; fill platform matrix; update index, log, ROADMAP W10/K147; `active_project_brief_targets.yaml` + `daily_research_config.yaml` routing; run `wiki_lint.py`

### Synthesis targets (post-research)

1. `concepts/diy-nfl-pickem-props-tool-architecture.md` (keystone → `draft`)
2. Six layer concept pages (payout, fair-prob, slip-EV, stat-map, data, legal, backtest, workflow, integration)
3. Platform pages: prizepicks, underdog-pickem → `validated` or `draft`
4. Source: fantasylabs-picklabs-launch → `validated`
5. Updates: parlay-and-correlated-bets, nfl-betting, ceminiidfs boundary, index, log, ROADMAP
6. Digest routing: `pickem` / `player-props` → K147 (not CeminiDFS)

### Reuse map (from architecture — do not re-research)

| CeminiDFS layer | K147 action |
|-----------------|-------------|
| nflreadpy / game env / usage / stat proj | **Reference** existing concept pages |
| Distribution (Monte Carlo) | **Adapt** in pickem-fair-probability |
| Ownership, FD scoring, pydfs | **Skip** |
| BBM extension | **Do not fork** — separate DOM research |

## Snippets

> "14 workstreams · 14 subagents · 4 execution waves." [Source: K147 planning session, 2026-07-05]

> "No repo until Phase-0 checklist ≥ 70%." [Source: @concepts/diy-nfl-pickem-props-tool-architecture.md]

---
title: Gambling bot architecture (planned)
type: concept
tags: [concept, meta, bots, automation, architecture, roadmap]
keywords: [gambling-bot, automation, platform-bots, sportsbook-bot, pm-bot, dfs-bot, cemini, fleet]
related:
  - concepts/bankroll-management.md
  - concepts/gambling-wiki-scope.md
  - concepts/kelly-criterion-betting.md
  - concepts/pm-copy-trading-retail-risks.md
  - concepts/prediction-markets-crossover.md
  - concepts/sportsbook-pm-line-divergence.md
  - entities/bots/README.md
  - entities/platforms/draftkings.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - meta/cross-wiki-routing.md
  - meta/gambling-bot-ingest-rubric.md
  - sources/gemini-github-sports-betting-landscape-2026-05-30.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - concepts/pm-agent-cognitive-monoculture.md
  - concepts/pm-llm-coherence-projection.md
  - concepts/pm-proper-scoring-clob-profitability.md
  - sources/openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md
  - sources/openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md
  - sources/arxiv-2606.16139-team-zero-sum-games-complexity-2026-06-20.md
  - sources/arxiv-2606.17682-trainee-to-trainer-llm-env-engineer-2026-06-20.md
  - entities/tools/devfun-poker-arena-starter-kit.md
  - entities/bots/wagerbrain.md
  - entities/bots/bovada-api-reference.md
  - entities/bots/bovada-hand-history-converter.md
  - entities/bots/poker-bot-tooling.md
  - entities/bots/stake-engine-client.md
  - entities/tools/rlcard.md
  - entities/tools/pokerskill.md
  - meta/daily-research-digest-cadence.md
  - sources/polygnosis-2-polymarket-osint-2026-06-01.md
  - entities/platforms/devfun-poker-arena.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/devfun-poker-arena-phase0-2026-06-01.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/pm-live-belief-updating.md
  - sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md
  - sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md
  - sources/arxiv-2607.02389-steerability-constraints-coding-agents-2026-07-06.md
  - sources/arxiv-2607.02453-oss-agent-framework-ecosystem-health-2026-07-06.md
  - sources/arxiv-2606.26807-karla-kb-augmented-retrieval-2026-07-06.md
  - sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md
  - sources/arxiv-2607.01120-areal-agentic-rl-self-evolving-agents-2026-07-09.md
  - sources/brief-k150-pm-liquidity-proper-betting-steals-2026-07-09.md
  - sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md
  - sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md
  - sources/arxiv-2607.03510-cage-1-enterprise-agent-governance-2026-07-10.md
  - sources/brief-k151-pm-belief-to-trade-volatility-steals-2026-07-10.md
  - entities/bots/predict-raven.md
  - concepts/pm-structural-volatility.md
  - sources/daily-digest-reject-cluster-k116-2026-06-17.md
  - sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md
  - entities/tools/wc2026-agents.md
  - sources/brief-k160-wc2026-agents-market-baseline-steals-2026-07-21.md
  - entities/sports/wnba-betting.md
  - sources/research-wnba-cold-streak-live-unders-2026-08-13.md
maturity: core
created: 2026-05-31
updated: 2026-08-13
---

# Gambling bot architecture (planned)

## Relations

- @meta/gambling-bot-ingest-rubric.md — bot ingest checklist
- @entities/bots/README.md — platform bot entity stubs
- @concepts/gambling-wiki-scope.md — wiki boundary vs @osint-wiki prod stack
- @meta/cross-wiki-routing.md — ingest routing for bot-related sources
- @sources/daily-digest-reject-cluster-k119-2026-06-18.md — digest false positives (OrchRM NO-GO)
- @entities/sports/wnba-betting.md — WNBA live-under research: alert-only; no 5-miss auto-bot
- @concepts/custom-agent-methodology.md — K120 Agents All the Way Down; CLI-over-MCP, P3→P5 loop
- @sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md — K120 source
- @sources/arxiv-2607.17765-wc2026-agents-llm-forecasting-2026-07-21.md — K160 market-baseline agent eval
- @entities/tools/wc2026-agents.md — WC2026-Agents FOSS (GO)
- @osint-wiki/concepts/cross-venue-arbitrage-pattern.md — PM×Kalshi execution patterns (cross-wiki)
- @osint-wiki/entities/tools/polybot.md — existing PM strip-mine reference

## Raw Concept

Operator intent: build **automated wagering systems** — either one orchestrated **master gambling bot** or (more likely) a **fleet of platform-specific bots** sharing signals, bankroll rules, and logging. This wiki is the **design and requirements home** for that program; `@osint-wiki` remains home for **CeminiSuite production deployment**, private credentials, and quant infra already in flight.

## Narrative

### Three layers (who owns what)

| Layer | Home | Content |
|-------|------|---------|
| **1. Retail strategy** | gambling-wiki | Manual +EV, bankroll, CLV, game rules, tool Phase-0 |
| **2. Gambling bot program** | **gambling-wiki** | What to automate, per-platform constraints, FOSS evals, signal→order design, failure modes, ToS/risk |
| **3. Prod execution stack** | @osint-wiki | CeminiSuite, conductor, live keys, World Cup bot, LP/maker code, backtest harnesses at scale |

**Ingest rule:** If the source helps answer *what a gambling bot should do on DraftKings vs Kalshi vs a DFS slate* → **save here**. If it is *how to deploy module X on cemini-prod* → stub + link **@osint-wiki**.

### Likely topology: platform fleet (not one monolith)

Default assumption unless operator revises (see `ROADMAP.md` D4):

```
                    ┌─────────────────────┐
                    │  Shared core        │
                    │  bankroll, Kelly,   │
                    │  logging, alerts    │
                    └──────────┬──────────┘
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
  Sportsbook bot(s)    PM / Kalshi bot(s)      DFS / best-ball
  +EV, CLV, line shop  line divergence,       optimizer hooks,
  promo / arb alerts   copy-trade *policy*    slate import
```

**Master orchestrator** may sit above (route signals, cap exposure across venues) — document decisions on this page as they land.

### Platform lanes to document (entity stubs over time)

| Lane | Bot role (draft) | Wiki pages to grow |
|------|------------------|-------------------|
| **Sportsbooks** | Line shop, +EV scanner hooks, steam/CLV logging, promo capture | `@entities/platforms/draftkings.md`, `@entities/platforms/fanduel.md`, `@entities/platforms/pinnacle.md` |
| **Prediction markets** | Sports PM divergence, fee-aware sizing, settlement rule checks; **live liquidity gate + drift-aware limits** (β≈0.64 underreaction — `@concepts/pm-live-belief-updating.md`) | `@entities/platforms/kalshi.md`, `@entities/platforms/polymarket.md`, `@concepts/sportsbook-pm-line-divergence.md`, `@concepts/pm-live-belief-updating.md` |
| **DFS / best ball** | Slate import, exposure caps, correlation stacks — not in-play HFT | `@concepts/dfs-strategy-overview.md`, `@entities/tools/pydfs-lineup-optimizer.md` |
| **Casino / poker** | Poker engines + RL (**rlcard**, poker_ai) = research lane; **iGaming slot UI** = dead end | K92 eval: @sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md |
| **Sportsbook API** | Bovada community APIs — reference-only, ToS risk | @entities/bots/bovada-api-reference.md |

Create `wiki/entities/bots/<platform>-bot.md` stubs when a lane gets concrete design notes or repo evals.

### iGaming casino UI — dead end (K92)

K92 Gemini eval surfaced **~20+ Reject** repos: PixiJS slot clients, crypto-casino monoliths, Stake "predictor" forks, crash-gambling simulators. **Do not** spend Phase-0 cycles on these for the gambling-bot program:

- No headless API suitable for Cemini-style automation
- License often missing; scam-adjacent "predictor" repos
- Wagering logic is RNG entertainment, not +EV retail sports/PM edge

**Exception:** `egorfedorov/Slot-Casino-Game-Developer-Skills-for-Stake` → **CCC wiki** (prompt/skills craft), not prod trading.

**Steal-from (OSINT only):** `floatinghotpot/casino-server` websocket→Redis reconciliation → world-cup-bot fill handler — document on @osint-wiki, not a gambling-bot adopt.

### What to save on ingest (gambling-bot lens)

When sources mention automation, capture **all** of the following if present:

1. **API / access** — official vs unofficial, geoblock, auth, rate limits, paper vs live
2. **ToS and account risk** — limits, bans, KYC, bot detection (sportsbook vs PM differs)
3. **Signal → action** — alert-only vs auto-submit; latency budget; human-in-the-loop default
4. **Edge type** — arb, middle, +EV, line divergence, copy-trading, LP (route LP depth to @osint-wiki if Cemini-specific)
5. **FOSS repo** — license (`gh api`), Phase-0 GO/NO-GO, strip-mine vs deploy (see K90 eval pattern on `@sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`)
6. **Failure modes** — stale lines, partial fills, fee drag, crowding (copy bots), weather-bot graveyard pattern
7. **Bankroll integration** — fractional Kelly, per-venue caps, correlated exposure across bots

Mark prod-only deployment detail `[ROUTE @osint-wiki]` in narrative; still **summarize wagering logic** here.

### Relationship to existing @osint-wiki bots

| System | gambling-wiki | @osint-wiki |
|--------|---------------|-------------|
| World Cup / advance markets bot | Retail contract types, sizing discipline | **Code + prod** |
| polybot, Harrier toolkits, polymarket-skills | Strip-mine patterns, retail guardrails | **Adopt / Phase-0** |
| Copy-trading executors | **NO-GO retail** — document risks (`@concepts/pm-copy-trading-retail-risks.md`) | DIY pipeline if built |
| Open-source sportsbook arb finders | Alert-only reference, latency notes | Optional code mirror |
| WNBA live last-2:00 / cold-streak scanners | **Alert-only**; 5-miss→Q-under has **no edge**; Kalshi has no last-2:00 contract (`@entities/sports/wnba-betting.md`) | Optional paper log only |

Do **not** duplicate osint entity bodies — bidirectional `related:` + 2–3 sentence gambling angle here.

### Framework Phase-0 metrics (K148) [TENTATIVE]

@sources/arxiv-2607.02453-oss-agent-framework-ecosystem-health-2026-07-06.md: **GitHub stars ≠ adoption depth** — log **contributor density**, cross-ecosystem engagement, and **30/90-day retention** on any agent framework Adopt candidate (extends K90–K103). @sources/arxiv-2606.26807-karla-kb-augmented-retrieval-2026-07-06.md: **CONDITIONAL-GO** KB-trigger RAG for versioned platform rules when public code + license verified.

### Online learning architecture (K150) [TENTATIVE]

@sources/arxiv-2607.01120-areal-agentic-rl-self-evolving-agents-2026-07-09.md — **AReaL** (Apache-2.0, ~5.5k★): three-pillar pattern for **future** fleet bots — (1) agent trajectory data protocol, (2) governed workload→RL data proxy, (3) evolution control plane triggering weight vs in-context updates. **Research lane only**; no prod online RL on wagering without ToS + human-in-loop. Pairs K148 framework Phase-0 metrics.

### Belief-to-trade + governance (K151) [TENTATIVE]

@sources/arxiv-2607.03015-belief-to-trade-pm-agents-predict-raven-2026-07-10.md — **predict-raven** (MIT): separate forecast from trade policy; @entities/bots/predict-raven.md. @sources/arxiv-2607.02599-agentltl-trace-verification-agents-2026-07-10.md + @sources/arxiv-2607.03510-cage-1-enterprise-agent-governance-2026-07-10.md — procedural trace gates + CAGE-style authorization/replay/stop checklist for wager-submit bots.

### Responsible automation

- Default **human-in-the-loop** for new lanes until CLV/track record exists
- No optimization for compulsive volume; cap trades/day in bot spec
- Jurisdiction and ToS compliance are **blockers**, not footnotes
- Online poker **botting/collusion** — document as fraud risk, not a build target

### Open decisions (track in ROADMAP.md)

| ID | Question |
|----|----------|
| D4 | Single master orchestrator vs independent platform bots |
| D5 | First automation lane priority (sportsbook +EV vs PM divergence vs DFS) |
| D6 | Code repo home | **Resolved** — public `Gambling-wiki` = wiki + scripts; implementations in private `llm-wiki-by-cemini/agents/` (dev.fun arena, PM bots, CeminiSuite deploy) |

## Snippets

> "Copy-trading bots cascade when a whale trades — hundreds of bots consume liquidity in seconds." — informs **NO-GO** on retail copy executors; any fleet bot needs anti-crowding logic. [Source: @sources/gemini-github-sports-betting-landscape-2026-05-30.md]

> K90 v6: gambling-wiki surface = retail wagering OSS; OSINT retains PM bots and CeminiSuite — extend to **planned gambling-bot fleet** on this wiki. [Source: @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

## Dead Ends

- **Martingale / slot picker bots** — not automation targets
- **OCR/UI automation** at soft books without ToS review — high ban risk; Phase-0 only
- **RuneScape / casino game bots** — out of scope

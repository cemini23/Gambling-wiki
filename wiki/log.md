# Wiki operations log

Append-only chronological log.

## [2026-06-01] phase-0 | dev.fun Poker Arena + cemini_decide scaffold

- **Wiki** — `entities/platforms/devfun-poker-arena.md`, `entities/bots/cemini-devfun-poker-agent.md`, `sources/devfun-poker-arena-phase0-2026-06-01.md`
- **Code** — `agents/devfun-poker-arena/` (arena-pokerkit + `examples/cemini_decide.py`)
- **Prod** — `deploy/deploy_to_cemini_prod.sh` → systemd on cemini-prod
- **Verdict** — CONDITIONAL-GO (arena-only); main event opens 2026-06-03

## [2026-06-01] cross-wiki | PolyGnosis osint stub + R3 WSJ transcript

- **@osint-wiki** — `entities/tools/polygnosis.md` + `sources/polygnosis-2-polymarket-osint-2026-06-01.md` (REFERENCE harness; Cemini map)
- **R3** — `sources/youtube-wsj-kalshi-polymarket-valuations-2026-06-01.md` (yt-dlp en captions)
- **Updated** — Kalshi/Polymarket regulation sections, prediction-markets-crossover, sharp-vs-soft-books, daily-digest-news R3 row
- **Archived** — `raw-sources/youtube-wsj-S2g0TwfecJE.en.vtt`

## [2026-06-01] ingest | Sweep news R1–R12 + PolyGnosis 2.0

- **News** — `sources/daily-digest-news-r1-r12-2026-06-01.md` (Brave/curl; R3 YouTube title-only)
- **Paper** — `sources/polygnosis-2-polymarket-osint-2026-06-01.md` + `concepts/pm-perspective-mismatch-trading.md`
- **Updated** — Kalshi/Polymarket fees, sportsbook–PM vig gap, +EV/CLV refs, WC 2026, DK/Underdog best ball
- **Archived** — `arxiv-2605.25958-polygnosis-2-0.pdf` → `raw-sources/`

## [2026-06-01] ingest | Daily digest arXiv batch (4 papers)

- **Source** — `sources/daily-digest-arxiv-batch-2026-06-01.md` (sweep `2026-06-01-daily.md`)
- **New** — `live-betting-match-integrity`, `pm-commitment-grounded-language`, `entities/tools/pokerskill.md`
- **Expanded** — sports-betting-fundamentals, poker-strategy, polymarket, poker-bot-tooling, PM crossover, copy-trading risks
- **Archived** — 4 PDFs → `raw-sources/`
- **Not ingested** — 12 news rows from sweep (manual fetch if needed)

## [2026-06-01] ops | First daily digest run + LaunchAgent active

- **Report** — `wiki/sweeps/2026-06-01-daily.md` (4 arXiv PDFs → inbox)
- **Fix** — `scripts/wiki_source_index.py` (missing from federated install copy)
- **LaunchAgent** — `com.cemini.daily-research-digest.gambling` loaded @ 08:15

## [2026-06-01] ingest | K93 federated daily digest install

- **Brief** — `briefs/2026-06-01_k93-gambling-digest-from-osint.md`
- **Structural** — `scripts/daily_research_*.py`, `daily_research_config.yaml`, LaunchAgent `com.cemini.daily-research-digest.gambling`
- **New** — `meta/daily-research-digest-cadence.md`, `sources/brief-k93-federated-digest-2026-06-01.md`, `wiki/sweeps/_daily-template.md`
- **Lint** — `wiki_lint.py` sweeps/ orphan exemption
- **K93 tool eval** — no gambling-surface Adopts (OSINT-only: harness, netviz, deptry)

## [2026-06-01] ingest | K92 completion — bot entity stubs + index

- **Expanded** — `sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md` (validated, deep-read)
- **New bots** — bovada-hand-history-converter, poker-bot-tooling, stake-engine-client
- **Index** — Entities — Bots section; K92 source row
- **Briefs** — no new briefs; K90 already ingested

## [2026-06-01] adopt | K92 Phase-0 steal-from + rlcard venv

- WagerBrain math map → `concepts/bankroll-management.md`
- rlcard → OSINT `.local/venv-gambling-research` (research lane)

## [2026-06-01] phase0 | K92 eval repos — gh api + clone audits

- **WagerBrain** — CONDITIONAL-GO steal-from (MIT, stale 2020)
- **rlcard** — CONDITIONAL-GO poker sim research
- **bovadaAPI / hand-history** — NO-GO (no license / archived)
- **stake-engine-client** — NO-GO (no LICENSE)
- **claude-trading-skills** — GO (CCC); **obsidian-second-brain** — GO laptop-only
- **dickreuter/Poker** — NO-GO GPL-3.0

## [2026-06-01] ingest | K92 — casino/poker/stake eval slice from OSINT

- **Source** — `sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md` (90 URLs, gambling-primary)
- **Entities** — `entities/bots/wagerbrain.md`, `entities/bots/bovada-api-reference.md`
- **Updated** — `gambling-bot-architecture.md` (iGaming dead-end), `entities/bots/README.md`
- **Split** — @osint-wiki canonical eval; wagering requirements saved here

## [2026-05-31] scope | Gambling bot program — wiki home for automation knowledge

- **Operator direction** — eventual master bot or platform-specific bot fleet; save gambling-botting intel in this wiki
- **New** — `concepts/gambling-bot-architecture.md`, `meta/gambling-bot-ingest-rubric.md`, `entities/bots/README.md`
- **Updated** — `gambling-wiki-scope.md`, `meta/cross-wiki-routing.md`, `CLAUDE.md`, `ROADMAP.md` (W4, D4–D6)
- **Split** — wagering bot design **here**; CeminiSuite prod code **@osint-wiki**

## [2026-05-31] ingest | Raise Your Edge — $10k MTT bankroll from zero (1 video)

- **Source** — `sources/youtube-raise-your-edge-10k-bankroll-2026-05-31.md` (yrGExOmDRLk)
- **Expanded** — poker-strategy-overview (validated), bankroll-management (100-BI MTT ladder, variance)
- **Themes** — 10-step MTT grind, ICM, value-heavy micro postflop, anti-gambling on quick-score chase

## [2026-05-31] ingest | Operator YouTube batch 3 — casino + AI sports (27 videos)

- **Source** — `sources/youtube-operator-batch-casino-2026-05-31.md` (25/27 VTT)
- **Expanded** — blackjack (validated), casino-game-house-edge (validated), poker-strategy-overview, roulette, odds-jam AI experiment
- **Blackjack cluster** — basic strategy 0.5% edge, misplayed hands, counting prerequisites, rule checklist
- **Poker cluster** — math, position, triple threat, MTT beginner tips
- **Dead ends** — Martingale, slot pickers, bot/collusion awareness, Galfond 3h defer

## [2026-05-31] ingest | Operator YouTube batch 2 — sports betting research (13 videos)

- **Source** — `sources/youtube-operator-batch-sports-betting-research-2026-05-31.md`
- **New entities** — Unabated, PickFinder (tools); Rufus Peabody (people)
- **Expanded** — sports-betting-fundamentals (validated), line-shopping-and-clv (validated), odds-jam model tutorial, kelly, vig/devig, sharp-vs-soft, prediction-markets-crossover (Novig), pinnacle
- **Themes** — EV process, CLV, Kelly, Pinnacle benchmark, devig, research workflows, PM vs books limits

## [2026-05-31] ingest | Operator YouTube batch — WC 2026 + BBM7 (17 videos)

- **Source** — `sources/youtube-operator-batch-wc-bbm-2026-05-31.md` (auto-caption via yt-dlp)
- **New entity** — `entities/platforms/underdog-fantasy.md`
- **Expanded** — best-ball-strategy (validated), world-cup-2026-betting, bankroll-management, nfl-betting, draftkings, dfs-strategy-overview, world-cup-third-place-advancement
- **WC cluster (7)** — value-over-teams, logic-over-heart, futures line moves, third-place paths
- **BBM7 cluster (10)** — winner roster archetypes, ADP deltas, TE mispricing, portfolio drafting
- **ROADMAP** — operator YouTube drop complete

## [2026-05-31] ingest | K90 tool eval + weather retail (cross-wiki brief)

- **Brief** — `briefs/2026-05-31_k90-gambling-tool-eval-from-osint.md`
- **Source** — `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` (gambling-wiki slice; canonical on @osint-wiki)
- **New entities** — georgedouzas/sports-betting (Steal-from MIT), fred4jupiter/fredbet (Steal-from MIT)
- **Expanded** — `concepts/polymarket-weather-wagering-retail.md` (K90 Post 15 retail posture)
- **Cross-links** — pm-copy-trading-retail-risks, polymarket, prediction-markets-crossover, sports-betting-fundamentals
- **Reject note** — weather-bot graveyard (5 UNAVAILABLE + 4 Reject); pretrehr duplicate; BeatTheBookie GPL

## [2026-05-31] ingest | Core gambling corpus (cross-wiki from @osint-wiki)

- **Sources** — Kelly 1956 paper, Gemini GitHub sports-betting landscape (full read), YouTube sports/PM retail batch (11 videos)
- **New concepts** — sportsbook–PM line divergence, PM copy-trading retail risks
- **New entities** — pydfs-lineup-optimizer, Alex Monahan
- **Expanded** — Kelly, sharp/soft, DFS, CLV, MomentumOdds, Odds Jam, NFL/NBA, Kalshi/Polymarket, bankroll, prediction-markets crossover
- **Note** — `research to be indexed/` was empty; synthesized from osint deep-reads. Operator YouTube batch next.

## [2026-05-31] ingest | WC 2026 retail synthesis (cross-wiki from @osint-wiki)

- **Source** — `sources/osint-cross-wiki-wc2026-retail-synthesis-2026-05-31.md` (no inbox file; synthesized from osint K82–K85 Gemini + YouTube compilation)
- **New entity** — `entities/sports/world-cup-2026-betting.md`
- **New concepts** — format, PM contract types, books-vs-PM divergence, third-place advancement, knockout-phase betting
- **Updated** — Kalshi, Polymarket, prediction-markets-crossover, DK/FD, line-shopping, FLB, sports-betting-fundamentals
- **Next** — operator YouTube batch (pending)

## [2026-05-31] bootstrap | Gambling wiki repo scaffold

- Created repo from Cemini wiki template (Cybersecurity-wiki pattern)
- `CLAUDE.md` — scope: sports betting, casino, poker, DFS, best ball, PM retail crossover
- Seed **14 concept pages**, **6 platform**, **2 tool**, **3 game**, **2 sport** entities
- Cross-wiki stubs to `@osint-wiki` (Kelly, FLB, Kalshi, Polymarket, MomentumOdds, Odds Jam)
- Federation alias: `gambling-wiki` (public)

## [2026-05-31] cross-wiki route | Polymarket weather wagering (retail)

Cross-wiki stub routed from `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`.
- Created wiki/concepts/polymarket-weather-wagering-retail.md (stub)

## [2026-05-31] cross-wiki route | Multi-wiki tool eval v6 K90

Cross-wiki stub routed from `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`.
- Created wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md (stub)

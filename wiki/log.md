# Wiki operations log

## [2026-08-15] ingest | Aug briefs catch-up (K222–K231 + K271)

- **Gap** — `briefs/2026-08-04_k222` … `2026-08-11_k231` and `2026-08-12_k271` existed as gitignored briefs; wiki entities never got the retail facts (K225 had a log line only)
- **Created** — `brief-k222-k231-pm-retail-awareness-2026-08.md`, `brief-k271-redagentbench-arena-eval-2026-08-12.md`
- **Updated** — kalshi, polymarket, fanduel (Predicts→Crypto.com), prediction-markets-crossover, kalshi-michigan (Utah SJ), poker-hl (eval hygiene), k125, industry 08-14, index
- **Skipped** — K166 already filed; CeminiDFS briefs are repo implementation plans; arena Aug 13–14 briefs stay private (no decide()/ranks)
- Sweep `2026-08-15-daily.md` → INGESTED-empty (0 papers; RSS section absent on that run)
- No FOSS adopt; no sportsbook auto-wager; no prod Kalshi orders

## [2026-08-14] ingest | RSS lane first full ingest (industry + Sharp + RotoViz stub)

- **Inbox** — empty (no PDFs)
- **Ingested** — LSB S12–S14 (CFTC/NY emergency, Colorado SB 26-131, DKeX 40.2 football + COMBOS); Sharp S23 (Taylor/Hubbard rush unders); RotoViz S18–S22 paywall stub (TLaw/ROO free ledes); EH S1 Novig cross-wiki stub
- **Skipped** — LSR S6–S10 (HTTP 403); PFT injury mill; nflverse GitHub tags; SBC vendor PR; RotoBaller sleepers; EH S2–S4 (OSINT already has bodies)
- **Created** — `daily-digest-rss-industry-2026-08-14.md`, `sharp-nfl-rb-prop-unders-2026-08-13.md`, `rotoviz-preseason-paywall-2026-08-14.md`, `substack-rss-event-horizon-2026-08-13-novig-responsible-trading.md`
- **Updated** — kalshi, draftkings, nfl-betting, prediction-markets-crossover, parlay-and-correlated-bets, kalshi-michigan, pickem-legal, pickem architecture/fair-prob, player-usage, dfs-distribution, bbm7-adp, cadence, index
- Sweep `2026-08-14-daily.md` → INGESTED
- No FOSS adopt; no sportsbook auto-wager; no prod Kalshi orders; no archive (URL-only)

## [2026-08-14] research | Daily digest RSS lane (seasonal ingest)

- **Problem** — paper lane dry: sports-betting / DFS / Kelly arXiv queries 0 hits most mornings; Exa news disabled (`exa.news_enabled: false`). Wrong daily diet for W8 NFL / W9 DFS.
- **Added** — `scripts/rss_digest.py` + `rss.feeds` in `daily_research_config.yaml` (15 free RSS/Atom feeds, discovery-only, no inbox HTML dump)
- **Wired** — `daily_research_digest_run.py` sweep section `S1`…; wiki URL dedupe
- **Updated** — `@meta/daily-research-digest-cadence.md`, ROADMAP digest note
- **Not enabled** — Exa news (credits); Action Network / VSiN / BettingPros picks mills; ETR/RotoGrinders/Unabated (404 or paywall stub)
- OSINT Substack poller still owns full Event Horizon / Closing Line / Outlier bodies (`cross_wiki: gambling-wiki`)

## [2026-08-13] research | WNBA cold-streak / last-2:00 live unders

- **Created** — `entities/sports/wnba-betting.md` (5-miss no edge; last-2:00 fair odds by margin; Kalshi inventory; OpenCLI social)
- **Created** — `sources/research-wnba-cold-streak-live-unders-2026-08-13.md`
- **Updated** — `nba-betting`, `kalshi` (WNBA series section), `gambling-bot-architecture` (alert-only row), `pm-live-belief-updating`, `parlay-and-correlated-bets`, `index.md`
- Methods: ESPN PBP 189 games (2026-06-01…08-12); Kalshi public trade-api (no prod login); OpenCLI Reddit/X
- Verdict: do **not** build 5-miss→Q-under bot; paper alert only for blowout last-2:00 if sportsbook lists prop above fair; Kalshi has no last-2:00 contract
- No FOSS adopt; no sportsbook auto-wager; no prod Kalshi orders

## [2026-08-12] ingest | K166 daily digest

- **Batch K166:** 2 REFERENCE / 0 GO / 0 reject
  - **2608.09389** Regret, equilibrium, and learning in games: A guided tour (Mertikopoulos) — **REFERENCE** FTRL/Hedge/FP literacy shelf (next to K163/K157/K152)
  - **2608.09256** Distributed Team Orchestration via Supervisor Networks (DTOA / BR-DTOA) — **REFERENCE** team-FP / MAS shelf + **FOSS NO-GO** (claimed `github.com/zjt-1229/team_game_with_supervisor_network` HTTP 404; user `zjt-1229` public_repos=0)
- Created paper sources + batch + shelf brief; updated opponent-modeling, poker-hl, MAFP, poker-bot-tooling, K152/K157/K163 shelf, team-zero-sum siblings
- Poker arena brief (wiki + OSINT `agents/devfun-poker-arena/briefs/`) — no decide()/HL import; no atto / GuruWatcher / CeminiDFS / TipDrop / prod scp
- Phase-1: `wont_wire` both (REFERENCE / FOSS 404 / no ADOPT-GO runtime)
- Sweep `2026-08-12-daily.md` → INGESTED
- Archived 2 PDFs to egress-fi; inbox cleared

## [2026-08-06] brief | K225 Kalshi 15-min + FanDuel/Crypto.com

- Local brief `briefs/2026-08-06_k225-15min-prediction-markets.md` (gitignored). Source OSINT Event Horizon 2026-08-06 + `@osint-wiki/concepts/prediction-market-short-horizon-velocity.md`.

Append-only chronological log.

## [2026-08-04] ingest | K165 daily digest

- **Batch K165:** 0 GO / 1 reject (bits-per-spike neuroscience Kelly-metaphor false positive)
- Created reject cluster + batch + shelf brief (wiki-only)
- Phase-1: wont_wire (reject-only; no ADOPT/GO)
- No FOSS adopt; no poker / Atto / GuruWatcher / CeminiDFS / TipDrop / prod briefs
- Tightened `kelly-bankroll-arxiv` query (wagering anchors + ANDNOT neural/spike)
- Sweeps `2026-07-31`…`08-02` → INGESTED-empty; `08-03`/`08-04` → INGESTED
- Archived 1 PDF to egress-fi; inbox cleared

## [2026-07-30] ingest | K164 daily digest

- **Batch K164:** 1 CONDITIONAL-GO / 0 reject (CCS-MCCFR correlated chance sampling)
- Created paper source + batch + steals brief; updated opponent-modeling, poker-hl, poker-bot-tooling, rlcard, PED/deal-games OpenSpiel siblings
- Poker arena brief (offline MCCFR/TexasSolver research only) — no FOSS; no atto / TipDrop / CeminiDFS / prod; decide() untouched
- Sweep `2026-07-30-daily.md` → INGESTED
- Archived 1 PDF to egress-fi; inbox cleared

## [2026-07-29] ingest | K163 daily digest

- **Batch K163:** 1 REFERENCE / 0 reject (swap-regret attention / smoothed FP)
- Created paper source + batch + shelf brief; updated opponent-modeling, poker-hl, MAFP, forgetting-factor, K157 FP shelf
- Poker arena brief confirm (OSINT K198 docs already shipped) — no decide()/FOSS/atto/TipDrop/CeminiDFS/prod
- Sweep `2026-07-29-daily.md` → INGESTED
- Archived 1 PDF to egress-fi; inbox cleared

## [2026-07-28] ingest | K162 daily digest

- **Batch K162:** 0 GO / 1 reject (HarnessLLM Rust ownership false positive)
- Created reject cluster + batch + shelf brief (wiki-only)
- No FOSS adopt; no phase-0; no poker / TipDrop / CeminiDFS / prod briefs
- Tightened `cemini-dfs-ownership-paper` arXiv query (require DFS anchors; drop bare `ownership`)
- Sweeps `2026-07-27` → INGESTED-empty; `2026-07-28` → INGESTED
- Archived 1 PDF to egress-fi; inbox cleared

## [2026-07-26] ingest | K161 daily digest

- **Batch K161:** 0 GO / 1 reject (EV charging OR false positive)
- Created reject cluster + batch + shelf brief (wiki-only)
- No FOSS adopt; no poker / TipDrop / CeminiDFS / prod briefs
- Sweeps `2026-07-22`…`25` → INGESTED-empty; `2026-07-26` → INGESTED
- Fixed federated LaunchAgent digest routing `@concepts/…` → `@osint-wiki/…`
- Archived 1 PDF to egress-fi; inbox cleared

## [2026-07-21] ingest | K160 daily digest

- **Batch K160:** 1 GO + 1 reject / 0 CONDITIONAL-GO
- Created WC2026-Agents source + `entities/tools/wc2026-agents.md`; GenAI design reject cluster
- Updated WC betting, FLB, vig, DraftKings, gambling-bot-architecture, custom-agent-methodology, poker-hl-analyst-loop
- Briefs: wiki + OSINT arena three-axis eval + CCC prod forecast-agent eval
- Local adopt: `raw-sources/foss-evals/FIFA2026LLM/` (~3.5MB; MIT+CC-BY)
- No David/TipDrop (no image-gen); no CeminiDFS (soccer)
- Sweep `2026-07-21-daily.md` → INGESTED; `2026-07-20-daily.md` empty-inbox → INGESTED-empty; archived 2 PDFs to egress-fi

## [2026-07-18] ingest | K159 daily digest

- **Batch K159:** 1 CONDITIONAL-GO + 1 REFERENCE / 0 reject
- Created Aleena source + `entities/tools/aleena.md`; Memory Scarcity REFERENCE source
- Updated `custom-agent-methodology`, `poker-hl-analyst-loop`
- Briefs: wiki + OSINT arena decision-continuity + CCC Aleena prod + CCC memory-scarcity REFERENCE
- Local adopt: `raw-sources/foss-evals/Aleena/` (~1.5MB; LICENSE TBD) on gambling-wiki + CCC
- No David/TipDrop (no image-gen path); no CeminiDFS
- Sweep `2026-07-18-daily.md` → INGESTED; routing link fix; archived 2 PDFs to egress-fi

## [2026-07-17] ingest | K158 daily digest

- **Batch K158:** 1 CONDITIONAL-GO / 0 reject
- Created play-adequacy CWM source + `entities/tools/code-world-models.md`
- Updated `poker-hl-analyst-loop`, `custom-agent-methodology`, `opponent-modeling-imperfect-info`, `rlcard`
- Briefs: wiki + OSINT arena play-adequacy gate + CCC prod eval
- Local adopt: `raw-sources/foss-evals/code-world-models/` (~4.8MB; LICENSE TBD)
- Sweep `2026-07-17-daily.md` → INGESTED; archived 1 PDF to egress-fi

## [2026-07-16] ingest | K157 daily digest

- **Batch K157:** 1 REFERENCE / 0 reject
- Created FBSDE fictitious-play convergence source (2607.08861)
- Updated MAFP source backlink + `opponent-modeling-imperfect-info`
- Briefs: wiki shelf + OSINT arena shelf (no prod/David/FOSS)
- Sweep `2026-07-16-daily.md` → INGESTED; archived 1 PDF to egress-fi

## [2026-07-15] ingest | K156 daily digest

- **Batch K156:** 1 CONDITIONAL-GO / 0 reject
- Created AgentTexasPoker source + `entities/tools/agent-texas-poker.md`
- Updated `poker-hl-analyst-loop`, `opponent-modeling-imperfect-info`
- Briefs: wiki + OSINT arena risk-spectrum + CCC prod LLM risk audit
- Local adopt: `raw-sources/foss-evals/AgentTexasPoker/` (~688KB; LICENSE TBD)
- Sweep `2026-07-15-daily.md` → INGESTED; archived 1 PDF to egress-fi

## [2026-07-14] ingest | K155 daily digest

- **Batch K155:** 1 CONDITIONAL-GO + 1 reject
- Created IdeaGene source + `entities/tools/ideagene-bench.md`
- Reject: Contravariance NeuroAI (08561)
- Updated `custom-agent-methodology`, `poker-hl-analyst-loop`
- Briefs: wiki `briefs/2026-07-14_k155-...` + OSINT arena patch-lineage + CCC prod lineage-eval
- Local adopt: `raw-sources/foss-evals/IdeasHaveGenomes/` (~26MB; LICENSE TBD) on gambling-wiki + CCC
- Sweep `2026-07-14-daily.md` → INGESTED; archived 2 PDFs to egress-fi

## [2026-07-07] ingest | K149 — daily digest batch (policy SSL + ADVENT poker ILP)

- **New** — `sources/arxiv-2607.01498-policy-representation-ssl-poker-2026-07-07.md` (CONDITIONAL-GO — ssl-project no LICENSE)
- **New** — `sources/arxiv-2607.01585-advent-ilp-poker-predicate-invention-2026-07-07.md` (REFERENCE)
- **New** — `sources/daily-digest-batch-k149-2026-07-07.md` (2 REFERENCE / 0 reject)
- **New** — `sources/brief-k149-policy-ssl-advent-poker-steals-2026-07-07.md` + OSINT arena brief
- **Filled** — Event Horizon NC PM budget stub; ep23 Spotify routing; Klement Jul 7 cross-wiki tags
- **Updated** — `opponent-modeling-imperfect-info.md`, `prediction-markets-crossover.md`
- **Archive** — 2 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-07-07-daily.md` INGESTED

## [2026-07-06] ingest | K148 — daily digest batch (agent substrate, PM hybrid, SD journal)

- **New** — 7 source pages (Ganzfried QP, SD e-process, KARLA, vuln cognitive, steerability, framework health, PM hybrid)
- **New** — `sources/daily-digest-batch-k148-2026-07-06.md` (7 REFERENCE / 1 reject)
- **New** — `sources/daily-digest-reject-cluster-k148-2026-07-06.md` (26904 video false positive)
- **New** — `sources/brief-k148-agent-framework-pm-betting-steals-2026-07-06.md` + 3 operator briefs (arena + 2 wiki)
- **Updated** — `custom-agent-methodology.md`, `gambling-bot-architecture.md`, `poker-hl-analyst-loop.md`, `opponent-modeling-imperfect-info.md`, `bankroll-management.md`, `polymarket.md`, Ganzfried backlink
- **Archive** — 8 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-07-06-daily.md` INGESTED

## [2026-07-05] install | NFL slate prefetch LaunchAgent (in-season, idle until Sep)

- **Installed** — `com.cemini.nfl-slate-prefetch.gambling` (hourly :05; writes stubs only in T-30/T-20 pass windows)

## [2026-07-05] ingest | Offseason week 27 hub + weekly LaunchAgent

- **Installed** — `com.cemini.nfl-offseason-weekly.gambling` (Sundays 09:15)
- **New** — `scripts/nfl_offseason_weekly_run.py`, config, `install_nfl_offseason_weekly.sh`
- **New** — `concepts/nfl-offseason-research-cadence.md`, `meta/nfl-offseason-weekly-cadence.md`
- **New** — `sources/web-bleacher-report-key-injuries-2026-07-01.md` (R40 deep-read)
- **New** — `sources/web-offseason-hub-w27-synthesis-2026-07-05.md`
- **Hub** — `briefs/offseason/2026-offseason-w27-hub.md` (gitignored)
- **Updated** — `bbm7-adp-delta-tracker.md` (Terrance Ferguson riser w27)

## [2026-07-05] decision | K147 primary platform — Underdog MVP, PrizePicks Phase-2

- **Operator** — start Underdog Pick'em (BBM7 account already active); add PrizePicks payout profile later
- **Updated** — `concepts/diy-nfl-pickem-props-tool-architecture.md`, `pickem-operator-workflow.md`, `pickem-pipeline-integration-spec.md`, `ROADMAP.md` W10
- **Next** — in-app geo check → spawn `CeminiPick` repo with `underdog.json` payout profile first

## [2026-07-05] research | K147 master plan + layer pages (14 workstreams)

- **New** — `sources/research-diy-pickem-props-master-plan-2026-07-05.md` (14 workstreams · 14 subagents · 4 waves)
- **New** — `concepts/pickem-payout-and-breakeven.md`, `pickem-fair-probability.md`, `pickem-slip-ev-and-correlation.md`, `pickem-stat-type-mapping.md`, `pickem-data-sources.md`, `pickem-legal-and-tos-posture.md`, `pickem-backtesting-framework.md`, `pickem-operator-workflow.md`, `pickem-pipeline-integration-spec.md`
- **Updated** — `concepts/diy-nfl-pickem-props-tool-architecture.md` (stub → **draft**; Phase-0 ~85%)
- **Updated** — `entities/platforms/prizepicks.md` (stub → **validated**, SA-01), `underdog-pickem.md` (stub → **draft**, SA-02)
- **Updated** — `concepts/parlay-and-correlated-bets.md` (DFS pick'em lounges section)
- **Routing** — `scripts/active_project_brief_targets.yaml`, `scripts/daily_research_config.yaml` (K147 pick'em lane)
- **Gate** — repo spawn blocked until primary platform chosen + operator geo verified

## [2026-07-05] research | W-PLATFORM-PP (SA-01) — PrizePicks Phase-0

- **Updated** — `entities/platforms/underdog-pickem.md` (stub → **draft**): payout tables vs PrizePicks, NFL stat menu, Flex/Rescue/correlation, ToS ix/x, manual workflow
- **Updated** — `entities/sports/nfl-betting.md` (bidirectional links), `concepts/diy-nfl-pickem-props-tool-architecture.md` (platform matrix row)
- **Rejected** — `aidanhall21/underdog-fantasy-pickem-scraper`, `fantasydatapros/underdog` (no LICENSE)

## [2026-07-05] deep-read | W-PAID-PICKLABS (SA-03) — FantasyLabs PickLabs launch

- **Updated** — `sources/fantasylabs-picklabs-launch-2026-07-05.md` (stub → **validated**, `read_status: deep-read`)
- **Updated** — `entities/tools/fantasylabs-dfs.md` (PickLabs All-Access gating, UI-only export)
- **Updated** — `concepts/diy-nfl-pickem-props-tool-architecture.md` (platform matrix, R20 done, economics checkbox)
- **Finding** — PickLabs bundled in All-Access; win prob + edge % vs consensus; no CSV/API; hybrid benchmark for K147 DIY

## [2026-07-05] stub | K147 — NFL pick'em / props tool research hub

- **New** — `concepts/diy-nfl-pickem-props-tool-architecture.md` (stub — Phase-0 checklist, reuse map from CeminiDFS, no repo yet)
- **New** — `sources/fantasylabs-picklabs-launch-2026-07-05.md` (R20 from 07-05 sweep)
- **New** — `entities/platforms/prizepicks.md`, `entities/platforms/underdog-pickem.md` (platform stubs)
- **Routed from** — CeminiDFS `briefs/2026-07-05_research-triage-plan.md` (PickLabs no-action → wiki)

## [2026-07-05] ingest | Newsletter RSS cross-wiki — Event Horizon / Klement synthesis

- **Concepts (3)** — `kalshi-spotify-oracle-manipulation-2026-07.md`, `kalshi-michigan-sports-injunction-2026-06.md`, `pm-whale-conviction-bias-2026-07.md`
- **Updated** — `kalshi.md`, `prediction-markets-crossover.md`; EH sources deep-read + Location pointers
- **Archive** — OSINT inbox newsletter/macro-charts RSS → `cemini-egress-fi:/opt/cemini-bulk/research/osint/`
- **Cross-wiki** — routed stubs from 2026-07-05 batch (`@osint-wiki` provenance)

## [2026-07-03] ingest | K137 — daily digest batch (SWE-INTERACT + RLVR NFL calibration)

- **New** — `sources/arxiv-2606.30573-swe-interact-user-driven-coding-agents-2026-07-03.md` (CONDITIONAL-GO — Apache-2.0 SWE-Interact)
- **New** — `sources/arxiv-2607.00164-verifiable-rewards-calibrated-forecasting-2026-07-03.md` (REFERENCE)
- **New** — `sources/daily-digest-batch-k137-2026-07-03.md` (2 REFERENCE / 1 reject)
- **New** — `sources/daily-digest-reject-cluster-k137-2026-07-03.md` (30105 NN verification false positive)
- **New** — `sources/brief-k137-swe-interact-rlvr-nfl-steals-2026-07-03.md` + operator + OSINT arena brief
- **Updated** — `custom-agent-methodology.md`, `poker-hl-analyst-loop.md`, `nfl-betting.md`, `line-shopping-and-clv.md`
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-07-03-daily.md` INGESTED

## [2026-07-02] ingest | K136 — daily digest batch (Tool-RL structural collapse)

- **New** — `sources/arxiv-2606.26027-tool-rl-collapse-supervisory-signals-2026-07-02.md` (CONDITIONAL-GO — MIT Tool-RL-Box)
- **New** — `sources/daily-digest-batch-k136-2026-07-02.md` (1 REFERENCE / 0 reject)
- **New** — `sources/brief-k136-tool-rl-collapse-steals-2026-07-02.md` + operator + OSINT arena brief
- **Updated** — `custom-agent-methodology.md`, `poker-hl-analyst-loop.md`, `gambling-bot-architecture.md`, ToolBench-X backlink
- **Archive** — 1 PDF → egress-fi; inbox cleared
- **Sweep** — `2026-07-02-daily.md` INGESTED

## [2026-07-01] ingest | K135 — daily digest batch (PM settlement + Kalshi macro beliefs)

- **New** — `sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md` (REFERENCE)
- **New** — `sources/arxiv-2606.30040-kalshi-macro-belief-distributions-2026-07-01.md` (REFERENCE)
- **New** — `sources/daily-digest-batch-k135-2026-07-01.md` (2 REFERENCE / 0 reject)
- **New** — `sources/brief-k135-pm-settlement-macro-beliefs-steals-2026-07-01.md` + operator brief
- **Updated** — `polymarket.md`, `kalshi.md`, `prediction-markets-crossover.md`, Kalshi live-belief backlink
- **Archive** — 2 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-07-01-daily.md` INGESTED

## [2026-06-30] ingest | K134 — daily digest batch (Ganzfried PED + deal-games)

- **New** — `sources/arxiv-2606.29169-ganzfried-ped-nash-imperfect-info-2026-06-30.md` (REFERENCE)
- **New** — `sources/arxiv-2606.29457-takeover-auction-diligence-games-2026-06-30.md` (CONDITIONAL-GO — MIT deal-games)
- **New** — `sources/daily-digest-batch-k134-2026-06-30.md` (2 REFERENCE / 0 reject)
- **New** — `sources/brief-k134-ganzfried-ped-deal-games-steals-2026-06-30.md` + operator + OSINT arena brief
- **Updated** — `opponent-modeling-imperfect-info.md`, `poker-hl-analyst-loop.md`, Ganzfried VBT backlink; index brief stubs k133+k134
- **Archive** — 2 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-30-daily.md` INGESTED

## [2026-06-29] ingest | K133 — daily digest batch (RQGM co-evolving evaluators)

- **New** — `sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md` (CONDITIONAL-GO — paper-only)
- **New** — `sources/daily-digest-reject-cluster-k133-2026-06-29.md` (2 rejects: 2606.22922 algebra, 2606.26397 MOMDP)
- **New** — `sources/brief-k133-rqgm-evaluator-steals-2026-06-29.md` + operator + OSINT arena brief
- **Updated** — `poker-hl-analyst-loop.md`, `custom-agent-methodology.md`, `gambling-bot-architecture.md`, Fara source backlink
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-29-daily.md` INGESTED

## [2026-06-27] ingest | K132 — daily digest batch (Fara-1.5 CUA envs)

- **New** — `sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md` (CONDITIONAL-GO — MIT microsoft/fara)
- **New** — `sources/daily-digest-reject-cluster-k132-2026-06-27.md` (1 reject: FDN 2606.25201)
- **New** — `sources/brief-k132-fara-agent-env-steals-2026-06-27.md` + operator + OSINT arena brief
- **Updated** — `poker-hl-analyst-loop.md`, `custom-agent-methodology.md`, sandbox guide
- **Archive** — 2 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-27-daily.md` INGESTED

## [2026-06-26] ingest | K131 — daily digest batch (ToolBench-X + Ganzfried VBT)

- **New** — `sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md` (REFERENCE — arena-tool hazard taxonomy)
- **New** — `sources/arxiv-2606.25997-ganzfried-vbt-nash-imperfect-info-2026-06-26.md` (REFERENCE — exact multiplayer NE)
- **New** — `sources/daily-digest-reject-cluster-k131-2026-06-26.md` (1 reject: ITS 2606.23015)
- **New** — `sources/brief-k131-toolbench-ganzfried-steals-2026-06-26.md` + operator + OSINT arena brief
- **Updated** — `poker-hl-analyst-loop.md`, `opponent-modeling-imperfect-info.md`, `custom-agent-methodology.md`, sandbox guide
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-26-daily.md` INGESTED

## [2026-06-26] wiki | dev.fun Sandbox Researcher Guide (official docs)

- **New** — `sources/devfun-sandbox-researcher-guide-2026-06-26.md` — arena-tool MCP, bundle layout, PvP/PvE scoring, $15K pool, submit rules
- **Updated** — `devfun-poker-arena.md`, `heads-up-arena-strategy.md`, `devfun-poker-arena-starter-kit.md`, Discord bundle source, K123 checklist

## [2026-06-26] wiki | Brief audit — fill missing source stubs

- **New** — `brief-k130-rlcard-offline-baseline-adopt-2026-06-26.md` (K130 Adopt)
- **New** — `brief-k122-poker-researcher-track-plan-2026-06-19.md`
- **New** — `brief-k128b-bbm7-challenge-register` + `challenges-and-solutions` stubs
- **New** — `research-nfl-dfs-id-mapping-2026-06-20.md`, `research-nfl-historical-odds-2026-06-20.md`
- **Updated** — `rlcard.md` (K130 Phase-0 refresh ADOPT), poker-bot-tooling, CeminiDFS/BBM cross-links

## [2026-06-25] ingest | K129 — daily digest batch (CELEUS eval + Tmax)

- **New** — `sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md` (REFERENCE — anytime-valid LLM eval CIs)
- **New** — `sources/arxiv-2606.23321-tmax-terminal-agents-2026-06-25.md` (CONDITIONAL-GO — Apache-2.0 terminal agent recipe)
- **New** — `sources/daily-digest-reject-cluster-k129-2026-06-25.md` (6 rejects)
- **New** — `sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md` + operator + OSINT arena brief
- **Updated** — `poker-hl-analyst-loop.md`, `brief-k125`, `dfs-backtesting-framework.md`
- **Archive** — 8 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-25-daily.md` INGESTED

## [2026-06-25] wiki | K128 — BBM7 Draft Copilot hub + Underdog mechanics

- **New** — `sources/brief-k128-bbm7-draft-copilot-hub-2026-06-24.md` (links master plan, challenge register, CeminiDFS impl)
- **Updated** — `entities/platforms/underdog-fantasy.md` (draft room UI, ToS, CSV, overlay integration)
- **Updated** — `bbm7-portfolio-construction.md`, `ceminidfs.md`, `ROADMAP.md` W7 phases

## [2026-06-24] ingest | K127 — daily digest batch (EMAgnet + IRumAI + SETE)

- **New** — `sources/arxiv-2606.23995-emagnet-selfplay-regularization-2026-06-24.md` (REFERENCE — parameter EMA self-play magnet)
- **New** — `sources/arxiv-2606.21975-irumai-indian-rummy-rl-2026-06-24.md` (REFERENCE — Indian Rummy RL benchmark)
- **New** — `sources/arxiv-2606.20960-equilibrium-internal-transfers-2026-06-24.md` (REFERENCE — SETE transfer equilibria)
- **New** — `sources/daily-digest-reject-cluster-k127-2026-06-24.md` (15 rejects incl. line-planning / DeFi AMM false positives)
- **New** — `sources/brief-k127-emagnet-irumai-selfplay-steals-2026-06-24.md` + operator + OSINT arena brief
- **New** — `entities/games/indian-rummy.md`
- **Updated** — `poker-hl-analyst-loop.md`, `heads-up-arena-strategy.md`, `opponent-modeling-imperfect-info.md`, `poker-bot-tooling.md`, GARIP cross-link
- **Archive** — 18 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-24-daily.md` INGESTED

## [2026-06-23] ingest | K126 — daily digest batch (GARIP selfplay + PM forecast eval)

- **New** — `sources/arxiv-2606.22688-garip-last-iterate-selfplay-2026-06-23.md` (REFERENCE — running-average self-play anchor)
- **New** — `sources/arxiv-2606.21013-agentic-time-machine-forecasting-2026-06-23.md` (REFERENCE — FutureX/Polymarket eval sandbox)
- **New** — `sources/daily-digest-reject-cluster-k126-2026-06-23.md` (predictability privacy REJECT)
- **New** — `sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md` + operator brief
- **Updated** — `poker-hl-analyst-loop.md`, `heads-up-arena-strategy.md`, MAFP, Polymarket, cemini agent cross-links
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-23-daily.md` INGESTED

## [2026-06-22] cross-wiki | K126 OSINT — ClarusC64 NFL coherence-risk backlink

- **Updated** — `concepts/diy-nfl-dfs-model-architecture.md` — bidirectional link to `@osint-wiki/concepts/nfl-coherence-risk-features.md` (CeminiDFS stage-2 feature extensions)

## [2026-06-22] ingest | K125 — daily digest batch (distribution shift eval)

- **New** — `sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md` (REFERENCE — eval under shift/selective labels)
- **New** — `sources/daily-digest-reject-cluster-k125-2026-06-22.md` (DRFLOW + DP submodular REJECT)
- **New** — `sources/brief-k125-eval-gate-discipline-2026-06-22.md` + operator brief (bundle + eval gates)
- **Updated** — `poker-hl-analyst-loop.md`, `dfs-backtesting-framework.md`, Discord bundle cross-links
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-22-daily.md` INGESTED

## [2026-06-20] ingest | K123 Discord — researcher sandbox bundle submission

- **New** — `sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md` (+ OSINT cross-wiki stub)
- **Updated** — `entities/platforms/devfun-poker-arena.md`, `sources/brief-k123-researcher-jun21-checklist-2026-06-20.md`, `concepts/heads-up-arena-strategy.md`, `entities/bots/cemini-devfun-poker-agent.md`

## [2026-06-20] research | K125 cross-wiki sweep (all sibling wikis)

- **New** — `sources/cross-wiki-k125-diy-dfs-sweep-2026-06-20.md` (OSINT weather API matrix, CCC orchestration, gambling underlinks)
- **Updated** — `concepts/dfs-weather-adjustments.md` (Open-Meteo + NWS + Visual Crossing + Wethr stack; bias_correction RETRACTED)
- **Updated** — `diy-nfl-dfs-model-architecture.md`, `nfl-dfs-data-sources.md`, `dfs-model-orchestration.md`
- **Wired** — `line-shopping-and-clv`, `kelly-criterion-betting`, `bankroll-management`, `nfl-betting`, `momentum-odds` → K125 hub
- **Finding** — @osint-wiki is primary for free weather APIs; Visual Crossing backtest-only (interpolation caveat); no cross-wiki nflverse/DFS ownership coverage

## [2026-06-20] research | K125 — DIY NFL DFS projection model (38 subagents)

- **Plan** — `sources/research-diy-dfs-model-master-plan-2026-06-20.md` (Opus 4.8: 18 workstreams)
- **Keystone** — `concepts/diy-nfl-dfs-model-architecture.md` + 15 layer concept pages
- **Updated** — `dfs-paid-tool-methodologies.md`, `nfl-dfs-data-sources.md`, `dfs-strategy-overview.md`, `ROADMAP.md` W8/K125
- **Verdicts** — nflreadpy GO; stat-first v1 + hybrid v2; Stokastic/Labs benchmark CSV; chanzer0 ideas-only

## [2026-06-20] research | W-CORR NFL DFS scoring correlations + stack rules

- **New** — `concepts/dfs-correlation-stacking.md` (correlation cheat table, Gaussian-copula/Cholesky method, pydfs defaults)
- **New** — `sources/web-nfl-dfs-correlation-stacking-2026-06-20.md` (4for4/PFF/pydfs docs synthesis)
- **Updated** — `concepts/diy-nfl-dfs-model-architecture.md` (W-CORR layer now drafted)
- **Updated** — `concepts/dfs-strategy-overview.md`, `entities/tools/pydfs-lineup-optimizer.md`, `index.md`
- **Finding** — QB-WR1 remains the core positive pair; bring-backs are supported by opposing passing-game lift; `RB + own DST` is mild positive rather than a negative-correlation ban

## [2026-06-20] research | W-LEGAL NFL DFS source ToS posture

- **New** — `concepts/nfl-dfs-data-sources.md` (W-DATA/W-LEGAL matrix: scrape posture, rate norms, cache policy, GO/CONDITIONAL/NO-GO)
- **New** — `sources/web-nfl-dfs-source-legal-posture-2026-06-20.md` (official terms scan: nflverse, The Odds API, FanDuel, DraftKings, ESPN, Open-Meteo, ownership vendors)
- **Updated** — `index.md` (K125 DIY DFS concept/source rows)
- **Finding** — primary automation lane = nflverse + The Odds API + Open-Meteo; manual-only lane = FanDuel/DraftKings files; red-flag lane = ESPN undocumented endpoints + scraped ownership archives

## [2026-06-20] tools | W8 DFS optimizer Phase-0 + FanDuel slate pipeline

- **New** — `entities/tools/stokastic-dfs.md`, `entities/tools/fantasylabs-dfs.md` (CONDITIONAL-GO paid tools)
- **Updated** — `pydfs-lineup-optimizer.md` — MIT license confirmed; GO verdict; CSV→150 lineup path
- **Scripts** — `scripts/fanduel_slate_optimize.py`, `scripts/normalize_dfs_projection_csv.py`
- **Skill** — `.cursor/skills/nfl-fanduel-slate-prep/SKILL.md`
- **ROADMAP** — D3 closed (Stokastic primary + pydfs FOSS)

## [2026-06-20] ingest | K124 — W8 NFL tier-2 sweep (Exa + Brave + web)

- **Sweep** — `sweeps/2026-06-20-tier2-w8-nfl.md` (Tier 2 targeted W8)
- **New sources** — Tech Insider NFL strategy, SBR Hard Rock Phase-0, DFS Hero NFL GPP
- **Updated** — `nfl-betting.md`, `hard-rock-bet.md`, `fanduel.md`, `dfs-strategy-overview.md`, `parlay-and-correlated-bets.md`
- **ROADMAP** — W8 Phase-0 + NFL book + FanDuel DFS steps checked

## [2026-06-20] config | W8 NFL season prep + dual-target digest

- **ROADMAP** — W8 NFL 2026 season prep workstream; W6 poker + W8 NFL co-primary in digest
- **Config** — `daily_research_config.yaml`: 5 NFL news clusters, `poker-hu-exploit` cluster, restored full poker `active_topics`, combined social pass
- **New** — `entities/platforms/hard-rock-bet.md` (operator primary NFL book stub)
- **Updated** — `nfl-betting.md`, `sharp-vs-soft-books.md`, `sports-betting-fundamentals.md`, `daily-research-digest-cadence.md`

## [2026-06-21] ingest | K124 — daily digest batch (MAFP + StreamMemBench)

- **New** — `sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md` (REFERENCE — fictitious play steals)
- **New** — `sources/arxiv-2606.14571-streammembench-agent-memory-2026-06-21.md` (REFERENCE — F6 memory eval rubric)
- **New** — `sources/daily-digest-reject-cluster-k124-2026-06-21.md` (2606.20510 security REJECT)
- **New** — `sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md` + operator brief
- **Updated** — `opponent-modeling-imperfect-info.md`, `custom-agent-methodology.md`, `poker-hl-analyst-loop.md`, K122 landscape
- **Archive** — 3 PDFs → egress-fi; inbox cleared
- **Sweep** — `2026-06-21-daily.md` INGESTED

## [2026-06-20] ingest | K123 — daily digest batch + researcher Jun 21 checklist

- **New** — `sources/arxiv-2606.16139-team-zero-sum-games-complexity-2026-06-20.md` (REFERENCE — PPAD team zero-sum)
- **New** — `sources/arxiv-2606.17682-trainee-to-trainer-llm-env-engineer-2026-06-20.md` (REFERENCE — LLM env engineer / HL loop)
- **New** — `sources/daily-digest-reject-cluster-k123-2026-06-20.md` (2606.15501 primal-dual REJECT)
- **New** — `sources/brief-k123-researcher-jun21-checklist-2026-06-20.md` + operator brief
- **Updated** — `custom-agent-methodology.md`, `opponent-modeling-imperfect-info.md`, `poker-hl-analyst-loop.md`, agent/platform entities, `ROADMAP.md` W6
- **Archive** — 3 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/gambling/`; inbox cleared
- **Sweep** — `2026-06-20-daily.md` marked INGESTED

## [2026-06-19] research | K122 — poker researcher track research plan

- **New** — `concepts/heads-up-arena-strategy.md`, `concepts/poker-axis-eval-literacy.md`, `sources/research-k122-poker-paper-landscape-2026-06-19.md`
- **Updated** — `entities/tools/devfun-poker-arena-starter-kit.md` (devfun-org primary repo)
- **Updated** — `entities/platforms/devfun-poker-arena.md`, `entities/bots/cemini-devfun-poker-agent.md`, cross-links
- **Brief** — `briefs/2026-06-19_k122-poker-researcher-track-research-plan.md` (6-lane synthesis)

## [2026-06-19] research | Pro villain profiles — Dwan + Jungleman (finale prep)

- **New** — `sources/web-pro-villain-profiles-dwan-cates-2026-06-19.md` (web + Durrrr Challenge synthesis)
- **Updated** — `entities/people/tom-dwan.md`, `entities/people/daniel-cates-jungleman.md` (validated, deep style + bot knobs)
- **Updated** — `concepts/opponent-modeling-imperfect-info.md`, `entities/bots/cemini-devfun-poker-agent.md`

## [2026-06-19] ingest | K121 — dev.fun researcher track invite email

- **New** — `sources/devfun-poker-researcher-track-email-2026-06-19.md` (HU sandbox, TrueSkill, Jun 21/25 timeline)
- **New** — `entities/people/daniel-cates-jungleman.md` (Jungleman stub)
- **Updated** — `entities/platforms/devfun-poker-arena.md` (researcher track ladder, game modes)
- **Updated** — `entities/people/tom-dwan.md`, `entities/bots/cemini-devfun-poker-agent.md`, `ROADMAP.md` W6

## [2026-06-19] ingest | K120 — Agents All the Way Down + brief close-out

- **New** — `sources/arxiv-2606.11869-agents-all-the-way-down-2026-06-19.md` (arXiv 2606.11869)
- **New** — `concepts/custom-agent-methodology.md` (P1–P5, CLI-over-MCP, HL loop mapping)
- **New** — `sources/brief-k107-poker-open-spot-audit-2026-06-09.md` (K107 cross-wiki brief source)
- **New** — `sources/daily-digest-reject-cluster-k116-2026-06-17.md` (6-paper reject cluster)
- **Updated** — `gambling-bot-architecture.md`, `poker-hl-analyst-loop.md`, `cemini-devfun-poker-agent.md`, `devfun-poker-arena-phase0-2026-06-01.md`, `brief-k118-*.md`
- **Archive** — PDF → `raw-sources/`; inbox cleared
- **Sweep** — `2026-06-19-daily.md` marked INGESTED

## [2026-06-18] ingest | Fantasy Six Pack — 2026 Best Ball New Meta

- **New** — `sources/fantasysixpack-bbm-new-meta-2026-06-08.md`
- **Updated** — `best-ball-strategy.md`, `bbm7-adp-delta-tracker.md`, sweep R11 (2026-06-09/10)

## [2026-06-18] update | BBM3/BBM5/BBM6 winner roster gaps filled

- **Updated** — `concepts/best-ball-mania-winners.md` — full 18-pick BBM3 (Kerrane, seat 7) + BBM5 (LGREWE50, seat 4) + BBM6 corrections (Pollard, Burden, Stevenson, Corum)
- **Sources** — ETR Manifesto, bestballteambuilder, Fantasy Alarm (BBMV CLV table)

## [2026-06-18] brief | BBM7 portfolio prep — ADP tracker + W15–17 + 150-entry matrix

- **New** — `concepts/bbm7-adp-delta-tracker.md` (TE R11–13, QB R8–10, rookie CLV)
- **New** — `concepts/bbm7-playoff-week-construction.md` (bye calendar, W17 stacks)
- **New** — `concepts/bbm7-portfolio-construction.md` (150 entries × timing × archetype)
- **Brief** — `briefs/2026-06-18_bbm7-portfolio-brief.md` (operator handoff)
- **Updated** — `best-ball-strategy.md`, `index.md`, W7 ROADMAP

## [2026-06-18] ingest | BBM7 guides — 4for4 series + Fantasy Guru stub

- **New** — `sources/4for4-bbm7-guide-series-2026-06-18.md` (7 free articles deep-read; ultimate guide paywalled)
- **New** — `sources/fantasy-guru-bbm-tactics-2026-06-08.md` (paywall stub)
- **Updated** — `concepts/best-ball-strategy.md` (BBM7 2026 positional playbook, advance vs winner tension)
- **Updated** — `concepts/best-ball-draft-timing.md` (4for4 preseason volume cross-ref)
- **Sweep** — R12 4for4 + R13 Fantasy Guru marked ingested in `2026-06-18-daily.md`

## [2026-06-18] ingest | BBM7 draft timing research

- **New** — `concepts/best-ball-draft-timing.md` (July–August sweet spot, portfolio window split)
- **New** — `sources/etr-best-ball-mania-manifesto-draft-timing-2026-06-18.md`
- **Updated** — `best-ball-strategy.md`, `entities/tournaments/best-ball-mania-vii.md`
- **Finding** — bye weeks known from May schedule; August edge is camp injuries/role clarity, not bye discovery

## [2026-06-18] ingest | BBM7 research kickoff — rules + winner dossier

- **New** — `entities/tournaments/best-ball-mania-vii.md` (official format, bracket, scoring [CONFIRMED])
- **New** — `concepts/best-ball-mania-winners.md` (BBM1–BBM6 full dossier + cross-patterns)
- **Updated** — `entities/platforms/underdog-fantasy.md` (BBM7 confirmed, maturity → validated)
- **Updated** — `concepts/best-ball-strategy.md` (winner archetype evolution, portfolio implications)
- **ROADMAP** — W7 BBM7 research workstream opened
- **Sources** — Underdog help center, bestballteambuilder, props.com, Rolling Stone, Fantasy Points, RotoViz

## [2026-06-18] ingest | K119 — Digest reject cluster (3 false positives)

- **Source** — `sources/daily-digest-reject-cluster-k119-2026-06-18.md` (validated)
- **Rejected** — arXiv 2606.11118, 2606.13598, 2606.18247 → `raw-sources/rejected-digest-2026-06-18/`
- **Brief** — K119 false-positive log + digest tune recommendations
- **Config** — tightened poker-exploit, poker-llm-tools, dfs-roster queries
- **Sweep** — `2026-06-18-daily.md` INGESTED (0/3 papers)

## [2026-06-17] brief | K118 — Poker agent research gaps + fix backlog

- **Source** — `sources/brief-k118-poker-agent-research-gaps-2026-06-17.md` (validated)
- **Brief** — `briefs/2026-06-17_k118-gambling-poker-agent-research-gap-fixes.md` (private operator backlog)
- **Updated** — `concepts/poker-hl-analyst-loop.md` (K118 metrics, research gap table, PFR gate gap)
- **Updated** — `entities/bots/cemini-devfun-poker-agent.md`, `entities/platforms/devfun-poker-arena.md`
- **Config** — `scripts/daily_research_config.yaml` poker exploit/LLM/OpenReview lanes + arena dataset news
- **Selfplay** — 400h seed 42: VPIP 11.5%, PFR 2.2%, SB VPIP 13.4% (private repo audit)

## [2026-06-17] ingest | K116 — Forecast@ICML26 PM papers (OpenReview)

- **Sources** — `openreview-prophets-profit-pm-LYSTj2Cnuu-2026-06-17.md`, `openreview-llm-coherence-projection-Tqos7VqQhH-2026-06-17.md` (skimmed)
- **Concepts** — `pm-proper-scoring-clob-profitability.md`, `pm-llm-coherence-projection.md`
- **Rejected** — 6 off-topic arXiv digest hits → `raw-sources/rejected-digest-2026-06-17/` (K116 brief)
- **Briefs** — K116 false-positive log, K117 JCD → @osint-wiki routing
- **Raw** — 2 OpenReview PDFs → `raw-sources/` + egress-fi mirror
- **Sweep** — `2026-06-17-daily.md` INGESTED (2/8 inbox)

## [2026-06-17] ops | Daily digest fetch tune (arXiv + OpenReview)

- **Config** — 6 paper lanes, 10-day window, `fetch_likely: true`, cap 8; news lane + poker-arena-bots query
- **Scripts** — `daily_research_fetch.py` OpenReview PDF support; synced to `~/.cemini/launchagent/osint/`
- **Test run** — 8 PDFs → `research to be indexed/` (awaiting full ingest)

## [2026-06-15] ops | cemini-librarian retired

- **Infra** — `cemini-librarian` Hetzner host decommissioned; no bulk mirror or wiki rsync
- **Canonical raw archive** — laptop `raw-sources/` only
- **Updated** — `CLAUDE.md`, `ROADMAP.md` (D1/D2 closed), source provenance tables (9 pages), K114 log line

## [2026-06-13] ingest | K114 — Nous PM paper + brief close-out

- **Source** — `sources/arxiv-2606-13038-nous-prediction-market-cognitive-injection-2026-06-13.md` (REFERENCE / skimmed)
- **Concept** — `concepts/pm-agent-cognitive-monoculture.md` (validated)
- **Source** — `sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md` (K103 reject cluster)
- **Entity** — `entities/tools/devfun-poker-arena-starter-kit.md` (K102 MIT arena-pokerkit Phase-0 REFERENCE)
- **Updated** — `entities/bots/poker-bot-tooling.md` (K103 reject cluster: PQL NO-GO, casinogame + poker-equity-playground Reject)
- **Updated** — `concepts/poker-hl-analyst-loop.md` (K107 open-spot bug pattern, audit table, passive PFR leak)
- **Updated** — `concepts/world-cup-pm-retail-hygiene.md` (GodEye 10 mistakes numbered checklist)
- **Raw** — Nous PDF → `raw-sources/` only (cemini-librarian retired 2026-06)
- **Cross-wiki** — `@osint-wiki` links on Nous source, starter-kit, poker-bot-tooling, HL loop, WC hygiene
- **Briefs cleared** — K102, K103, K107, K108, K112 gambling handoffs from `briefs/` (K107 audit retained)

## [2026-06-12] ingest | K112 WC 2026 fan narrative from OSINT

- **Source** — `sources/brief-k112-gambling-wc-2026-narrative-2026-06-12.md`
- **Concept** — `concepts/world-cup-2026-fan-narrative-preview.md` (REFERENCE)
- **Brief cleared** — ingested from `briefs/2026-06-12_k112-gambling-wc-2026-narrative-from-osint.md`

## [2026-06-09] ingest | K108 WC PM retail hygiene + K107 open-spot audit

- **Source** — `sources/brief-k108-gambling-wc-retail-hygiene-2026-06-09.md`
- **Concept** — `world-cup-pm-retail-hygiene.md` (validated)
- **Updated** — `entities/sports/world-cup-2026-betting.md`, `entities/platforms/polymarket.md`, `poker-hl-analyst-loop.md`, `devfun-poker-arena.md`
- **K107 audit** — open-spot fix confirmed in private `is_preflop_open_spot()`; selfplay VPIP 12.1% / PFR 2.1% — passive leak remains; results in `briefs/2026-06-09_k107-gambling-poker-open-spot-AUDIT.md`
- **Briefs cleared** — removed ingested K90 + K93 stubs from `briefs/`

## [2026-06-09] ingest | Kalshi live belief updating (arXiv 2606.07811)

- **Source** — `sources/arxiv-kalshi-live-belief-updating-2606.07811-2026-06-09.md` (deep-read)
- **Concept** — `pm-live-belief-updating.md` (validated)
- **Updated** — `entities/platforms/kalshi.md`, `entities/sports/nba-betting.md`, `prediction-markets-crossover.md`, `sportsbook-pm-line-divergence.md`, `sports-betting-fundamentals.md`
- **Raw** — PDF → `raw-sources/`; 4 tournament screenshots → `raw-sources/tournament-screenshots-2026-06-09/` (archive only, not ingested)
- **Sweep** — `wiki/sweeps/2026-06-09-daily.md` inbox cleared

## [2026-06-07] security | Competition intel redaction + arena bot moved private

- **Redacted** — `LESSONS.md` L4–L6, `ROADMAP.md` W6, entity/bot pages (no ranks, wallets, leak clusters, env toggles)
- **Removed from public git** — `agents/devfun-poker-arena/` → private `llm-wiki-by-cemini/agents/devfun-poker-arena/`
- **Public stub** — `agents/README.md`; prior git history replaced with single public commit

## [2026-06-06] maintenance | YouTube VTT archive routing (operator batches 2–4)

- **Routed** — 39 VTTs from `.tmp-yt-ingest-{2,3,4,dwan}` → `raw-sources/youtube-{id}.en.vtt` (41 total incl. prior Dwan + WSJ)
- **Wiki** — ingest already complete 2026-05-31; archive paths added to sports-betting, casino, and RYE source pages
- **Cleanup** — removed staging dirs; inbox left empty (preingest skips `.vtt`)

## [2026-06-05] deep-pass | K100 — Polymarket-v1 database (arXiv 2606.04217)

- **Source** — `sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md` → `deep-read`, validated
- **Concept** — `polymarket-v1-research-database.md` → validated (access patterns, retail findings)
- **Updated** — `entities/platforms/polymarket.md` (fee reform on-chain, FLB reversal, dataset ref), `favorite-longshot-bias.md`, `prediction-markets-crossover.md`, `pm-copy-trading-retail-risks.md`
- **Cross-wiki** — measurement layer unchanged on `@osint-wiki`

## [2026-06-05] ingest | K100 — Polymarket-v1 database (arXiv 2606.04217)

- **Source** — `sources/arxiv-polymarket-v1-database-2606.04217-2026-06-05.md`
- **Concept** — `polymarket-v1-research-database`
- **Cross-wiki** — `@osint-wiki` REFERENCE stub
- **Raw** — PDF → librarian

## [2026-06-04] maintenance | Wiki links and lint

- **Entity** — `cemini-devfun-poker-agent.md` metadata sync (no live ranks in public wiki)
- **Wiki lint** — repaired bidirectional `related:` gaps; added frontmatter to `sweeps/2026-06-04-daily.md`

## [2026-06-04] ingest | PM digest arXiv batch (SEPO + D-Wave dead end)

- **Sweep** — `wiki/sweeps/2026-06-04-daily.md`
- **Source** — `sources/daily-digest-arxiv-batch-2026-06-04.md` (2605.30854 SEPO/Kuhn poker; 2605.17623 portfolio dead end)
- **Updated** — `poker-bot-tooling.md`, `opponent-modeling-imperfect-info.md`, `pokerskill.md`, `cemini-devfun-poker-agent.md`, `daily-research-digest-cadence.md`
- **Archived** — 2 PDFs → `raw-sources/`

## [2026-06-03] ingest | Tom Dwan HSP compilation — pro-table villain profile

- **Source** — `sources/youtube-pokergo-dwan-hsp-mega-compilation-2026-06-03.md` ([uC1pmdBTn6U](https://www.youtube.com/watch?v=uC1pmdBTn6U))
- **Entity** — `entities/people/tom-dwan.md` (LAG archetype + bot counter-strategy)
- **Updated** — `devfun-poker-arena.md` (event ladder clarified), `cemini-devfun-poker-agent.md`, `opponent-modeling-imperfect-info.md`, `poker-strategy-overview.md`, `devfun-poker-arena-phase0-2026-06-01.md`
- **Archived** — `raw-sources/youtube-uC1pmdBTn6U.en.vtt`

## [2026-06-03] workflow | Poker HL analyst loop (concept)

- **Concept** — `concepts/poker-hl-analyst-loop.md` (validated)
- **Updated** — `cemini-devfun-poker-agent.md`, `gambling-bot-architecture.md`
- **Pattern** — analyze → patch → preflight → deploy (implementation private)

## [2026-06-03] ingest | K95 — opponent modeling + tournament brief

- **Source** — `arxiv-2508.17671-consistent-opponent-modeling.md`
- **Concept** — `opponent-modeling-imperfect-info.md`
- **Brief** — tournament notes retained in private ops repo (not public wiki)
- **PDF** → librarian; inbox cleared

## [2026-06-02] ingest | AM digest batch (2 arXiv + news R1–R12 deltas)

- **Sweep** — `wiki/sweeps/2026-06-02-daily.md` (manual digest run; LaunchAgent exit 2 on scheduled AM)
- **Sources** — `daily-digest-arxiv-batch-2026-06-02.md` (GIMARL note; replicability PM dead end), `daily-digest-news-r1-r12-2026-06-02.md` (Kalshi 71% share, Predict.fun WC odds)
- **Updated** — Kalshi, Polymarket, world-cup-2026-betting, poker-bot-tooling, daily-research-digest-cadence
- **Archived** — 2 PDFs → `raw-sources/`

## [2026-06-01] phase-0 | dev.fun Poker Arena

- **Wiki** — `entities/platforms/devfun-poker-arena.md`, `entities/bots/cemini-devfun-poker-agent.md`, `sources/devfun-poker-arena-phase0-2026-06-01.md`
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

## [2026-06-02] ops | Tournament S28 lobby + entry-fee retry

- **Prod** — `ARENA_LOBBY_COMPETITION_ID=cmpr1vesh2it1x69xmtpiaecp` (Tournament S28)
- **Fee** — 0.01 MON on Monad (402 until paid on dev.fun); lobby retries join every 60s
- **Code** — `run_cemini_lobby.py` no longer exits on 402; monitor defaults updated
- **Wiki** — devfun-poker-arena + cemini-devfun-poker-agent entry-fee notes

## [2026-07-05] cross-wiki route | Event Horizon — Michigan Court Orders Kalshi to Stop Sports Event Contracts

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-06-29-michigan-court-orders-kalshi-to-stop-sports-even.md (stub)

## [2026-07-05] cross-wiki route | Event Horizon — Why Do Prediction Markets Insist On Downplaying Sports Volume?

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-06-29-why-do-prediction-markets-insist-on-downplaying.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-06-29-why-do-prediction-markets-insist-on-downplaying.md (stub)

## [2026-07-05] cross-wiki route | Event Horizon — World Launches Solana-Based Prediction Market

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-07-01-world-launches-solana-based-prediction-market.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-07-01-world-launches-solana-based-prediction-market.md (stub)

## [2026-07-05] cross-wiki route | Event Horizon — How Much Kalshi Trading Is There On Things Other Than Sports And Crypto?

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-07-02-how-much-kalshi-trading-is-there-on-things-other.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-07-02-how-much-kalshi-trading-is-there-on-things-other.md (stub)

## [2026-07-05] cross-wiki route | Event Horizon — How Artificial Spotify Streams Broke A Kalshi Market

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md (stub)

## [2026-07-05] cross-wiki route | Klement on Investing — A fundamental flaw of prediction markets

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md`.
- Created wiki/sources/substack-rss-klement-2026-07-02-a-fundamental-flaw-of-prediction-markets.md (stub)

## [2026-07-05] cross-wiki route | Outlier Weekly — The $1.1B Warehouse Failure Behind the CXW/GEO Trade

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-outlier-weekly-2026-07-03-the-11b-warehouse-failure-behind-the-cxwgeo-trad.md`.
- Created wiki/sources/substack-rss-outlier-weekly-2026-07-03-the-11b-warehouse-failure-behind-the-cxwgeo-trad.md (stub)

## [2026-07-06] cross-wiki route | Event Horizon — Episode 23: Silliness In Prediction Markets About Spotify

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-07-06-episode-23-silliness-in-prediction-markets-about.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-07-06-episode-23-silliness-in-prediction-markets-about.md (stub)

## [2026-07-06] cross-wiki route | Klement on Investing — Investors must be wary of the earnings bubble

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-klement-2026-07-06-investors-must-be-wary-of-the-earnings-bubble.md`.
- Created wiki/sources/substack-rss-klement-2026-07-06-investors-must-be-wary-of-the-earnings-bubble.md (stub)

## [2026-07-06] cross-wiki route | Klement on Investing — Is water use priced in stock markets?

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-klement-2026-07-06-is-water-use-priced-in-stock-markets.md`.
- Created wiki/sources/substack-rss-klement-2026-07-06-is-water-use-priced-in-stock-markets.md (stub)

## [2026-07-07] cross-wiki route | Event Horizon — North Carolina’s Prediction Market Budget Process Seems Pretty Unserious

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-event-horizon-2026-07-07-north-carolinas-prediction-market-budget-process.md`.
- Created wiki/sources/substack-rss-event-horizon-2026-07-07-north-carolinas-prediction-market-budget-process.md (stub)

## [2026-07-07] cross-wiki route | Klement on Investing — Globalisation in the 2020s

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-klement-2026-07-07-globalisation-in-the-2020s.md`.
- Created wiki/sources/substack-rss-klement-2026-07-07-globalisation-in-the-2020s.md (stub)

## [2026-07-07] cross-wiki route | Klement on Investing — Momentum crash warnings flash red. Here’s how you might survive

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-klement-2026-07-07-momentum-crash-warnings-flash-red-heres-how-you.md`.
- Created wiki/sources/substack-rss-klement-2026-07-07-momentum-crash-warnings-flash-red-heres-how-you.md (stub)

## [2026-07-08] cross-wiki | K149 gambling

- Kalshi SDNY PI denial brief

## [2026-07-09] ingest | K150 daily digest

- **Batch K150:** 3 REFERENCE + 1 CONDITIONAL-GO + 1 arXiv supplement + 3 reject
- Created `wiki/sources/arxiv-2607.01198-liquidity-tail-risk-large-trades-2026-07-09.md`
- Created `wiki/sources/arxiv-2607.01377-kyle-liquidity-premium-investment-horizons-2026-07-09.md`
- Created `wiki/sources/arxiv-2607.01120-areal-agentic-rl-self-evolving-agents-2026-07-09.md`
- Created `wiki/sources/daily-digest-batch-k150-2026-07-09.md`, reject cluster, brief stub
- Updated `openreview-prophets-profit-pm` with arXiv 2607.06166 supplement
- Updated `pm-proper-scoring-clob-profitability`, `gambling-bot-architecture`
- Brief: `briefs/2026-07-09_k150-pm-liquidity-proper-betting-steal.md` (wiki-only; no prod scp)
- Sweep `2026-07-09-daily.md` → INGESTED; routing link fix
- Archived 7 PDFs to egress-fi

## [2026-07-10] ingest | K151 daily digest

- **Batch K151:** 3 REFERENCE + 1 CONDITIONAL-GO + 1 reject
- Created predict-raven source + entity; PM structural volatility source + concept
- Created AgentLTL + CAGE-1 governance sources
- Reject: DeFi reverse Kelly AMM (04178)
- Updated `pm-proper-scoring`, `gambling-bot-architecture`, Kalshi/Polymarket entities
- Brief: `briefs/2026-07-10_k151-pm-belief-to-trade-volatility-steal.md` (wiki-only)
- Sweep `2026-07-10-daily.md` → INGESTED; routing link fix
- Archived 5 PDFs to egress-fi

## [2026-07-11] ingest | K152 daily digest

- **Batch K152:** 1 REFERENCE + 1 CONDITIONAL-GO / 0 reject
- Created expert-yardstick source + `entities/tools/adversarial-coevolution.md`
- Created forgetting-factor regret source
- Updated `opponent-modeling-imperfect-info`, `poker-hl-analyst-loop`, `rlcard`
- Briefs: wiki `briefs/2026-07-11_k152-...` + OSINT `agents/devfun-poker-arena/briefs/2026-07-11_k152-...`
- Sweep `2026-07-11-daily.md` → INGESTED; routing link fix
- Archived 2 PDFs to egress-fi

## [2026-07-12] ingest | K153 daily digest

- **Batch K153:** 1 REFERENCE + 1 CONDITIONAL-GO + 1 reject
- Created MPPO source + entity; ASE PM evidence-chain source
- Reject: matroid rank aggregation (07153)
- Updated `opponent-modeling-imperfect-info`, `poker-hl-analyst-loop`, `pm-agent-cognitive-monoculture`, `blackjack`
- Briefs: wiki + OSINT arena MPPO steal
- Sweep `2026-07-12-daily.md` → INGESTED; routing link fix
- Archived 3 PDFs to egress-fi

## [2026-07-13] ingest | K154 daily digest

- **Batch K154:** 2 REFERENCE + 1 CONDITIONAL-GO + 4 reject
- Created Pokémon TCG Nash metagame, Ensemble QSP memory, DeepSearch-World sources
- Reject cluster: robotics affordances, psych AI eval, quantile RL, equity support/resistance
- Updated `opponent-modeling`, `poker-hl-analyst-loop`, `custom-agent-methodology`, `predict-raven`
- Briefs: wiki + OSINT arena metagame/memory steal
- Sweep `2026-07-13-daily.md` → INGESTED; routing link fix
- Archived 7 PDFs to egress-fi

## [2026-08-01] cross-wiki route | CS-RNR safe opponent exploitation (arXiv:2607.28520)

Cross-wiki stub routed from `@image-gen-wiki/sources/arxiv-2607-28520-cs-rnr-opponent-exploit-routed.md`.
- Created wiki/sources/arxiv-2607-28520-cs-rnr-safe-opponent-exploitation.md (stub)

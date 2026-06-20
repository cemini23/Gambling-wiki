# Gambling Wiki — ROADMAP

Active workstreams, open decisions, and done log. Read at session start; update at session end.

---

## Active workstreams

### W1 — Repo bootstrap + seed corpus

**Status:** In progress 2026-05-31 — WC retail batch landed; YouTube ingest queued.

Steps:
- [x] Scaffold from Cemini wiki template (Cybersecurity-wiki pattern)
- [x] Adapt `CLAUDE.md` for gambling vertical + osint-wiki boundary
- [x] Seed core concept pages (bankroll, Kelly, vig, FLB, sports betting, DFS, poker, casino edge)
- [x] Seed platform/tool stubs (DraftKings, FanDuel, Pinnacle, Kalshi, Polymarket cross-refs)
- [x] Wire cross-wiki links to `@osint-wiki`
- [x] **WC 2026 retail batch** — cross-wiki synthesis from osint Gemini/YouTube research (7 new pages)
- [x] Operator YouTube drop — 17 videos (WC + BBM7) ingested 2026-05-31
- [ ] Deep-read migrated OSINT sources (Gemini sports-betting landscape primary docx)
- [x] Push to `Gambling-wiki` GitHub (librarian rsync retired 2026-06)

### W6 — dev.fun Playground bot (cemini_decide)

**Status:** Active — Playground S2 + Tournament path; **researcher track HU sandbox opens 2026-06-25** (closed beta 2026-06-21). **Competitive-secrecy:** ranks, chip counts, env toggles, patch backlog, opponent reads, and `decide()` implementation live in **private** `llm-wiki-by-cemini/agents/devfun-poker-arena/` only — not in public wiki pages during active events.

**Agent:** Cemini dev.fun poker agent (handle on official arena — details in private creds).

**Discord meta (unofficial):** site fixes in progress; multi-agent + X-verify rules TBD next season; more jackpot types coming.

| Window | Dates | Mode | Goal (public) |
|--------|-------|------|---------------|
| **S1a** | Jun 3–7 | **Build** | HL loop + regression library; don’t bust; qualify if possible |
| **S1b** | Jun 7–11 | **Compete** | Best validated variant; claim when rules allow |
| **S2 Playground** | Active | **Compete** | Qualify top 20 → Tournament S2 |
| **Researcher β** | Jun 21 | **R&D** | Closed beta — HU agent + self-play SDK |
| **Researcher public** | Jun 25+ | **Benchmark** | HU TrueSkill sandbox; style rep vs Dwan/Jungleman |
| **KO** | TBA | **Compete** | Survival-first (no rebuy) |

**In progress (private runbooks)**

- [x] Playground qualification secured (S1a)
- [x] HL analyst loop + preflight gate stack operational
- [ ] KO cold-start / early-bust hardening (no rebuy)
- [ ] S1b variant selection under competition rules
- [ ] Researcher track signup + HU strategy fork (K121) — **K123 checklist** `@sources/brief-k123-researcher-jun21-checklist-2026-06-20.md`

**Cadence (generic):** status script → analyze → one patch → preflight → deploy. Command paths in private `README-CEMINI.md`.

**Public doc rule:** wiki may describe *that* we run an arena bot and the HL *workflow*; it must **not** publish frequencies, guards, nemesis profiles, or patch priorities while the $50k path is live.

### W8 — NFL 2026 season prep (active)

**Status:** Started 2026-06-20 — operator #1 betting window. Lanes: **Hard Rock** sportsbook/casino, **FanDuel** DFS, **Underdog** DFS + **BBM7**. Daily digest adds W8 NFL query clusters **alongside** W6 poker lanes (`scripts/daily_research_config.yaml`).

| Phase | Window | Focus |
|-------|--------|-------|
| **Draft season** | Jun–Aug | BBM7 entries (see W7); ADP refresh; stack meta |
| **Camp / preseason** | Jul–Aug | Injury reports, depth charts, prop limits |
| **Regular season** | Sep–Feb | Weekly CLV, FanDuel GPP slates, live betting hygiene |

Steps:
- [x] Wire W8 into federated daily digest — NFL query clusters + social pass (`daily_research_config.yaml`)
- [x] Hard Rock Bet platform stub — `entities/platforms/hard-rock-bet.md`
- [ ] Phase-0 Hard Rock — TOS, limits, promo math, casino vs book split
- [ ] Deep-read NFL sportsbook lane — expand `entities/sports/nfl-betting.md` (props, key numbers, injury cadence)
- [ ] FanDuel NFL DFS playbook — GPP/showdown/ownership (expand `entities/platforms/fanduel.md` or dedicated concept)
- [ ] Operator YouTube / free-guide ingest batch (NFL betting + FD DFS)
- [ ] In-season: weekly slate briefs in `briefs/`; CLV journal hook on `@concepts/line-shopping-and-clv.md`

**Digest note:** W8 NFL and W6 poker are **co-primary** in `active_topics` and news/social passes — not either/or.

### W7 — BBM7 research & draft prep (active)

**Status:** Started 2026-06-18 — wiki as research hub for Underdog Best Ball Mania VII entries. Subsumed under W8 for season prep; keep ADP/portfolio cadence through Week 1.

Steps:
- [x] Official BBM7 rules/format verified — `entities/tournaments/best-ball-mania-vii.md`
- [x] BBM1–BBM6 winner dossier — `concepts/best-ball-mania-winners.md`
- [x] Cross-winner pattern synthesis (archetypes, stacks, TE, late-round value)
- [x] Draft timing research — `concepts/best-ball-draft-timing.md` (ETR Manifesto; July–Aug sweet spot)
- [x] Fill roster gaps — BBM3 + BBM5 full 18, BBM6 corrected (bestballteambuilder + ETR + Fantasy Alarm)
- [x] Ingest 4for4 BBM7 guide + Fantasy Guru tournament tactics (sweep hits R12–R13)
- [x] ADP vs projection delta tracker — `concepts/bbm7-adp-delta-tracker.md`
- [x] Portfolio construction brief — `concepts/bbm7-portfolio-construction.md` + `briefs/2026-06-18_bbm7-portfolio-brief.md`
- [x] Week 15–17 bye/cliff analysis — `concepts/bbm7-playoff-week-construction.md`
- [x] Ingest Fantasy Six Pack 2026 New Meta — `sources/fantasysixpack-bbm-new-meta-2026-06-08.md`

### W2 — Domain expansion (queued)

Priority ingest lanes once sources arrive:

| Lane | Target pages |
|------|----------------|
| **Sports betting** | CLV, steam moves, closing line value, props correlation, live betting |
| **DFS / best ball** | roster construction, ownership, stack rules, late swap, Underdog/Best Ball Mania |
| **Poker** | preflop charts, ICM, bankroll by stake, solver study workflow |
| **Casino** | basic strategy, comp optimization, table selection |
| **Prediction markets (retail)** | fee math, FLB on Kalshi vs PM, cross-venue shopping |

### W5 — Federated daily digest (K93)

**Status:** Installed 2026-06-01.

Steps:
- [x] Run `install_federated_daily_digest.sh` for gambling-wiki
- [x] Domain `daily_research_config.yaml` (sports betting, PM retail, WC, bots, bankroll, DFS, poker)
- [x] `wiki/meta/daily-research-digest-cadence.md` + sweeps template
- [x] Operator: `launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.gambling.plist`
- [x] Fetch tune 2026-06-17 — arXiv + OpenReview, 6 paper lanes, `fetch_likely: true`
- [x] First morning sweep review + ingest session (K116 2026-06-17)

### W4 — Gambling bot program (planned)

**Status:** Scoping 2026-05-31 — knowledge base first; implementation TBD.

**Intent:** Build either one **master gambling bot** or (more likely) **multiple platform-specific bots** (sportsbook, PM/Kalshi, DFS) sharing bankroll/logging core.

Steps:
- [x] Document scope split — `wiki/concepts/gambling-bot-architecture.md`, ingest rubric, `entities/bots/` namespace
- [ ] Prioritize first automation lane (see D5)
- [ ] Ingest FOSS bot repos into `entities/bots/` with Phase-0 verdicts
- [ ] Cross-link existing @osint-wiki bot entities (polybot, Harrier, WC bot) bidirectionally
- [ ] Decide code repo home (see D6)

### W3 — Public polish

- [x] MIT LICENSE
- [x] README for federation table
- [x] Initial GitHub publish
- [x] Competition intel redaction — single-commit public history; bot code → private osint repo (2026-06-07)
- [ ] Add `wiki_gap_detect.py` (copy from sibling wiki when page count > ~50)

---

## Open decisions

| ID | Question | Options | Status |
|----|----------|---------|--------|
| D1 | Librarian sync cadence | Manual rsync vs hourly LaunchAgent like osint-wiki | **Closed 2026-06** — cemini-librarian retired; no remote RAG mirror |
| D2 | Raw source home | Laptop `raw-sources/` only vs also push to cemini-librarian bulk | **Resolved 2026-06** — laptop `raw-sources/` only |
| D3 | DFS optimizer tooling | Document pydfs-lineup-optimizer vs paid optimizers | **Open** — Phase-0 when DFS ingest batch lands |
| D4 | Bot topology | Single master orchestrator vs independent platform bots | **Open** — lean fleet |
| D5 | First bot lane | Sportsbook +EV vs PM divergence vs DFS slate | **Open** |
| D6 | Code repo home | Gambling-wiki scripts vs CeminiSuite vs new repo | **Resolved 2026-06-07** — bot code in private `llm-wiki-by-cemini/agents/`; public repo = wiki + scripts only |

---

## Done log

| Date | Item |
|------|------|
| 2026-06-07 | Competition scrub — redacted public wiki/LESSONS; bot code → private osint; GitHub history squashed to single commit |
| 2026-06-04 | Playground W6 — S1a build mode in ROADMAP; prod pace tuned (details private) |
| 2026-06-01 | K93 federated daily digest — scripts, config, meta cadence, sweeps/ |
| 2026-06-01 | K92 Phase-0 audits + WagerBrain/rlcard adopt notes |
| 2026-05-31 | WC 2026 retail ingest — 1 source, 1 sport entity, 5 concepts, 8 page updates |
| 2026-05-31 | Initial repo scaffold, seed concepts/entities, osint-wiki federation stubs |

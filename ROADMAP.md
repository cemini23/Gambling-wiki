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
- [x] Push to `Gambling-wiki` GitHub + librarian rsync via OSINT sync script

### W6 — dev.fun Playground bot (cemini_decide)

**Status:** Active — Playground qualification window + upcoming KO. **Competitive-secrecy:** ranks, chip counts, env toggles, patch backlog, opponent reads, and `decide()` implementation live in **private** ops only (`agents/` local + prod); not in public wiki pages during active events.

**Agent:** Cemini dev.fun poker agent (handle on official arena — details in private creds).

**Discord meta (unofficial):** site fixes in progress; multi-agent + X-verify rules TBD next season; more jackpot types coming.

| Window | Dates | Mode | Goal (public) |
|--------|-------|------|---------------|
| **S1a** | Jun 3–7 | **Build** | HL loop + regression library; don’t bust; qualify if possible |
| **S1b** | Jun 7–11 | **Compete** | Best validated variant; claim when rules allow |
| **KO** | TBA | **Compete** | Survival-first (no rebuy) |

**In progress (private runbooks)**

- [x] Playground qualification secured (S1a)
- [x] HL analyst loop + preflight gate stack operational
- [ ] KO cold-start / early-bust hardening (no rebuy)
- [ ] S1b variant selection under competition rules

**Cadence (generic):** status script → analyze → one patch → preflight → deploy. Command paths in private `README-CEMINI.md`.

**Public doc rule:** wiki may describe *that* we run an arena bot and the HL *workflow*; it must **not** publish frequencies, guards, nemesis profiles, or patch priorities while the $50k path is live.

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
- [ ] Operator: `launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.gambling.plist`
- [ ] First morning sweep review + ingest session

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
- [ ] Initial GitHub publish
- [ ] Add `wiki_gap_detect.py` (copy from sibling wiki when page count > ~50)

---

## Open decisions

| ID | Question | Options | Status |
|----|----------|---------|--------|
| D1 | Librarian sync cadence | Manual rsync vs hourly LaunchAgent like osint-wiki | **Open** — defer until page count justifies RAG |
| D2 | Raw source home | Laptop `raw-sources/` only vs also push to cemini-librarian bulk | **Open** — follow operator preference on next ingest |
| D3 | DFS optimizer tooling | Document pydfs-lineup-optimizer vs paid optimizers | **Open** — Phase-0 when DFS ingest batch lands |
| D4 | Bot topology | Single master orchestrator vs independent platform bots | **Open** — lean fleet |
| D5 | First bot lane | Sportsbook +EV vs PM divergence vs DFS slate | **Open** |
| D6 | Code repo home | Gambling-wiki scripts vs CeminiSuite vs new repo | **Open** |

---

## Done log

| Date | Item |
|------|------|
| 2026-06-04 | Playground W6 — S1a build mode in ROADMAP; prod pace tuned (FIRST_RANK=1, LEAD 600s) |
| 2026-06-01 | K93 federated daily digest — scripts, config, meta cadence, sweeps/ |
| 2026-06-01 | K92 Phase-0 audits + WagerBrain/rlcard adopt notes |
| 2026-05-31 | WC 2026 retail ingest — 1 source, 1 sport entity, 5 concepts, 8 page updates |
| 2026-05-31 | Initial repo scaffold, seed concepts/entities, osint-wiki federation stubs |

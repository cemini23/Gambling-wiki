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

**Status:** Active 2026-06-04 — S1a **build mode** through Jun 7; S1b compete Jun 7–11.

**Agent:** `cemini_wiki_poker` on official Playground S1 (`cmpy2qy65002ud9ej6b7jjq0l`).

| Window | Dates | Mode | Goal |
|--------|-------|------|------|
| **S1a** | Jun 3–7 | **Build** | HL loop + regression library; don’t bust; top-20 is bonus (ticket buy-in fallback OK) |
| **S1b** | Jun 7–11 | **Compete** | Best bot variant + optional multi-agent probe; claim winner |
| **KO** | TBA | **Compete** | Survival + reads; top 25 advance |

**S1a build mode (current)**

- [x] Rank #2 ~13k chips, +8k buffer — qualification zone secured if stack holds
- [x] FIRST protect: rank **#1 only** @ 30min join retry (`CEMINI_FIRST_RANK=1`)
- [x] Lead protect: rank 2–5 @ **10min** join retry (`CEMINI_LEAD_JOIN_RETRY_S=600`) — more analyze signal than 15min
- [ ] HL rounds through SB/UTG/BTN trash clusters (~every 50–100 hands)
- [ ] Freeze each leak in `tests/fixtures/regression_spots.py`
- [ ] Prep S1b: 3–5 unclaimed probe agents + egress train profile sweep (L5)

**Cadence**

```bash
./scripts/cemini_playground_status.sh          # rank vs #20 floor
./examples/cemini_hl_loop.sh --from-prod --round N
# patch → ./examples/cemini_hl_loop.sh --preflight-only --deploy
```

**Do not in S1a:** chase #1, widen steals, optimize self-play bb/100, deploy with `CEMINI_FORCE_CREDS=1`.

**S1b compete flip (before Jun 7)**

| Env | Build (S1a) | Compete (S1b) |
|-----|-------------|---------------|
| `CEMINI_FIRST_RANK` | `1` | `1` or `2` if co-leader |
| `CEMINI_LEAD_JOIN_RETRY_S` | `600` | `900` |
| `CEMINI_FIRST_JOIN_RETRY_S` | `1800` | `1800`–`3600` |
| Multi-agent probe | optional local | register 3–5 handles, claim best |

See `agents/devfun-poker-arena/briefs/2026-06-03_playground-top20-qualification.md`, `README-CEMINI.md` qualification section.

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

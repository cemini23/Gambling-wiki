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

### W2 — Domain expansion (queued)

Priority ingest lanes once sources arrive:

| Lane | Target pages |
|------|----------------|
| **Sports betting** | CLV, steam moves, closing line value, props correlation, live betting |
| **DFS / best ball** | roster construction, ownership, stack rules, late swap, Underdog/Best Ball Mania |
| **Poker** | preflop charts, ICM, bankroll by stake, solver study workflow |
| **Casino** | basic strategy, comp optimization, table selection |
| **Prediction markets (retail)** | fee math, FLB on Kalshi vs PM, cross-venue shopping |

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

---

## Done log

| Date | Item |
|------|------|
| 2026-05-31 | Core corpus ingest — Kelly, Gemini landscape, YouTube retail, DFS/tools, NFL/NBA, PM divergence, copy-trading risks |
| 2026-05-31 | WC 2026 retail ingest — 1 source, 1 sport entity, 5 concepts, 8 page updates |
| 2026-05-31 | Initial repo scaffold, seed concepts/entities, osint-wiki federation stubs |

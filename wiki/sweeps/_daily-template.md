# Daily Research Digest — YYYY-MM-DD

Discovery-only. Window: `YYYY-MM-DD` → `YYYY-MM-DD` (7 days). Exa queries × up to 3 hits (deduped).

Reference: `scripts/daily_research_config.yaml`. **Does NOT ingest wiki pages.**

---

## Active topics (sync from ROADMAP)

- Sports betting — +EV, CLV, line shopping
- PM retail — Kalshi/Polymarket, cross-venue vs books
- World Cup 2026 — retail wagering (cross-ref @osint-wiki WC bot)
- Gambling bot program (W4) — FOSS evals, API/ToS
- Bankroll / Kelly / DFS / poker study lanes

---

## Inbox (`research to be indexed/`)

_Empty — no manual drops pending._

---

## Exa candidates

### Q1: kalshi-pm-retail (N hits)

Query: `...` · category: `news`

| Pick | Date | Title | Cluster | URL |
|------|------|-------|---------|-----|
| [ ] R1 | | [Title](https://…) | kalshi-pm-retail | |

---

## Ingest session prompt (copy into Cursor)

```
Ingest selected rows from wiki/sweeps/YYYY-MM-DD-daily.md:
- Run preingest_check on any new URLs/files
- Discuss takeaways before writing entity/concept pages
- Touch 3–15 wiki pages; lint; update ROADMAP if scope shifts
- Route prod bot code to @osint-wiki; wagering requirements stay here
```

---

## Summary

| Metric | Count |
|--------|-------|
| Exa hits (deduped) | 0 |
| Inbox files | 0 |

### Discard

`rm wiki/sweeps/YYYY-MM-DD-daily.md` if nothing worth acting on.

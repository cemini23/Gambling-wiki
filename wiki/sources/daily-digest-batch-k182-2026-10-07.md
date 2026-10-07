---
title: "Daily digest batch K182 — CFTC swap rules, Ohio C&D, arXiv FP trio, LSB cards (2026-10-07)"
type: source
tags: [source, batch, k182, pm-retail, regulatory, arxiv, nfl, nhl]
keywords: [cftc-af82, ohio-cease-desist, fictitious-play, bluffjax, super-bowl-61, cee]
related:
  - sources/rss-lsb-cftc-rules-ohio-cd-2026-10-06.md
  - sources/arxiv-2610-fictitious-play-trio-2026-10-07.md
  - sources/rss-lsb-week5-cards-2026-10-05-06.md
  - sources/rss-sbc-cee-merkur-2026-10-07.md
  - sources/rss-sharp-football-week5-worksheets-2026-10-06.md
  - entities/platforms/kalshi.md
  - entities/platforms/polymarket.md
  - concepts/prediction-markets-crossover.md
  - sweeps/2026-10-07-daily.md
maturity: draft
read_status: deep-read
created: 2026-10-07
updated: 2026-10-07
phase_0_verdict: REFERENCE — 3 arXiv + 12 RSS; 5 LSR stubs were duplicates
wire_status: policy_wired
---

## Batch summary

19 inbox files. **5 were duplicates** — the recurring LSR stubs. This batch the cause was fixed rather than only noted; see below.

| # | Source | Phase-0 | Wire |
|---|--------|---------|------|
| 1–2 | **CFTC proposes swap rules · Ohio C&D to 10 operators** | REFERENCE | policy_wired kalshi / polymarket / crossover |
| 3–5 | arXiv FP trio (mean-field, BluffJAX, slow convergence) | REFERENCE | wont_wire W6 |
| 6–10 | LSB cards — NHL, MNF, AFC North, MLB, SB 61 | REFERENCE | policy_wired |
| 11–12 | SBC — CEE entry, Merkur/EveryMatrix | OOD | wont_wire |
| 13–14 | Sharp W5 worksheets (both half-paywalled) | PARTIAL | policy_wired |
| — | 5 LSR stubs | **DUPLICATE** | archived |

**New pages:** 6 (5 sources + 1 hub).

## Recommended actions

1. **Ohio's deadline is 2026-10-16.** Ten operators must stop sports event contracts; Kalshi is absent because it is in separate litigation. **Felony exposure is stated in the letters.** Awareness only — no operator holds these.
2. **The CFTC's AF81 is an Interim Final Rule** — it takes effect on White House approval with no comment period. AF82 (event contracts as swaps) is the one that would settle the federal question, and it is only proposed. **Neither is in force.**
3. **BluffJAX is the only adoptable artifact** of the arXiv trio — a GPU JAX poker suite with Texas Hold'Em NL, Kuhn, Leduc, and previously-unstudied games (Bluff, Kemps). **Licence unverified**; check before use. Not wired this batch.
4. **The slow-convergence paper bounds FP**, not the operator's games: the construction is adversarial. It does mean FP convergence rate is not a fixed property of the method.
5. **Sharp Football is now 9 of 11 pages paywalled** across two batches. The free tier is the stats directory only.

## Process note — the preingest gap is fixed

Last session I recorded that K180 **batched five LSR articles into one page whose title differs from any single stub**, so the title-based duplicate check could not match them and they kept re-entering the inbox as NEW. They did so again this morning.

**Root cause confirmed:** `scripts/preingest_check.py` scans **frontmatter + the Raw Concept section** for URLs and arXiv IDs, and builds a `location_basename` index. My batch pages carried only **slugs** — no full URLs — so neither index matched.

**Fix applied:** the K180 page now lists each article's **full URL** in its Raw Concept table. Re-running the check turns all five from NEW to **LIKELY**.

**Convention going forward:** any source page that batches several articles **must list each article's full URL in Raw Concept**. Slugs alone do not match.

## Notes

- **No briefs dispatched.** Week 4 is closed; Week 5's pipeline runs through `@meta/research-input-pipeline.md` and its briefs, not this wiki.
- **arXiv lane produced 3 PDFs** — the first multi-paper retrieval in several weeks.
- **Archive pending.**

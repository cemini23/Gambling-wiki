---
title: "NFL Week 4 Friday slate environment + designations (2026-10-02)"
type: source
tags: [source, nfl, week-4, weather, dfs, k180]
keywords: [tampa-25mph, baltimore-rain, implied-team-totals, line-movement, friday-deltas, nrg-roof]
related:
  - entities/sports/nfl-betting.md
  - sources/nfl-week4-research-plan-2026-10-01.md
  - sources/nfl-week4-practice-reports-2026-10-01.md
  - sources/daily-digest-batch-k180-2026-10-02.md
  - concepts/dfs-weather-adjustments.md
  - concepts/implied-team-totals-dfs.md
  - concepts/free-slate-context.md
maturity: draft
read_status: deep-read
created: 2026-10-02
updated: 2026-10-02
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/NFL Week 4 Slate Research.docx
phase_0_verdict: REFERENCE — Friday env card; re-check at lock
wire_status: policy_wired
---

## Relations

- @entities/sports/nfl-betting.md — W8 season lane
- @concepts/dfs-weather-adjustments.md — wind/dome thresholds
- @concepts/implied-team-totals-dfs.md — Vegas → ITT
- @concepts/free-slate-context.md — free weather/context tooling
- Gitignored hub: `briefs/2026-w04-slate-hub-sun.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **File** | `NFL Week 4 Slate Research.docx` |
| **sha256** | `03314a035ef599b1…` |
| **Type** | Gemini Deep Research — Friday environment card + designation deltas |
| **Retrieved** | 2026-10-02 09:36 EDT |

## Narrative

### Environment card — 13 main-slate games

| Kick ET | Game | Roof | Exposed | Wind | Precip | Temp |
|---------|------|------|---------|------|--------|------|
| Sun 09:30 | IND @ WAS (London) | Open | yes | 6 mph (gusts 15) | <5% | 73°F |
| Sun 13:00 | TEN @ BAL | Open | yes | 8 mph | **81%** | 61°F |
| Sun 13:00 | NE @ BUF | Open | yes | 7 mph | 10% | 63°F |
| Sun 13:00 | NYJ @ CHI | Open | yes | 7 mph | 2% | 68°F |
| Sun 13:00 | JAC @ CIN | Open | yes | 5 mph | 8% | 68°F |
| Sun 13:00 | DAL @ HOU | **Retractable** | yes | NO_EVIDENCE | NO_EVIDENCE | NO_EVIDENCE |
| Sun 13:00 | ARI @ NYG | Open | yes | **11 mph** | 12% | 65°F |
| Sun 13:00 | LAR @ PHI | Open | yes | 9 mph | 17% | 62°F |
| Sun 13:00 | GB @ TB | Open | yes | **25 mph** | 4% | 78°F |
| Sun 16:05 | MIA @ MIN | Dome | no | — | 0% | 70°F |
| Sun 16:25 | KC @ LV | Dome | no | — | 0% | 70°F |
| Sun 16:25 | LAC @ SEA | Open | yes | 5 mph | 7% | 72°F |
| Sun 16:25 | DEN @ SF | Open | yes | 6 mph | 10% | 75°F |

**Two environments dominate.** Tampa Bay at **25 mph** sustained is the steepest on the card. Baltimore at **81% precipitation** is the wettest.

The document's stated rule: sustained wind **≥10 mph** triggers a review note on passing yardage and first-TD legs — it does not force a line removal. At open-air venues above **8–11 mph**, passes beyond 15 air yards and field goals outside 45 yards take observable friction; sub-12 mph does not impair handoffs, screens, or interior rushing.

### Implied team totals + movement vs Thursday

| Game | Spread | Total | Fav ITT | Dog ITT | Move |
|------|--------|-------|---------|---------|------|
| IND @ WAS | IND −3.5 | 48.5 | 26.0 | 22.5 | total +1.0 (47.5→48.5) |
| TEN @ BAL | BAL −11.5 | 42.5 | 27.0 | 15.5 | total −1.0 |
| NE @ BUF | BUF −6.5 | 48.5 | 27.5 | 21.0 | static |
| NYJ @ CHI | CHI −3.5 | 42.5 | 23.0 | 19.5 | total −1.0 |
| JAC @ CIN | CIN −2.5 | **51.5** | 27.0 | 24.5 | static (slate high) |
| DAL @ HOU | HOU −3.0 | 47.5 | 25.2 | 22.2 | spread −2.5→−3.0 |
| ARI @ NYG | **ARI −2.5** | 43.5 | 23.0 | 20.5 | **flipped from NYG −1.5** |
| LAR @ PHI | LAR −3.5 | 43.5 | 23.5 | 20.0 | spread −3.0→−3.5; total −1.0 |
| GB @ TB | GB −3.5 | 38.5 | 21.0 | 17.5 | total −1.0 (wind) |
| MIA @ MIN | MIN −10.5 | 38.5 | 24.5 | **14.0** | total −1.0 |
| KC @ LV | KC −4.5 | 47.5 | 26.0 | 21.5 | static |
| LAC @ SEA | SEA −7.0 | 43.5 | 25.2 | 18.2 | static |
| DEN @ SF | SF −2.5 | 47.5 | 25.0 | 22.5 | total +1.0 |

**Largest move: ARI @ NYG swung four points**, from Giants −1.5 to Cardinals −2.5.

### Friday designation deltas

| Player | Team | Thursday | Friday | Action |
|--------|------|----------|--------|--------|
| **Caleb Williams** | CHI | DNP (Warn) | **OUT** | scratch |
| Chicago starting QB | CHI | Open | no flip | stack fade |
| **Justin Jefferson** | MIN | DNP (Warn) | **OUT** | scratch |
| **Nico Collins** | HOU | LP (Warn) | **OUT** | scratch **[DraftEdge only — no club page]** |
| Jayden Daniels | WAS | LP (Warn) | **Questionable** | warn |
| Bucky Irving | TB | LP (Warn) | **Questionable** | warn |
| Baker Mayfield | TB | DNP (Scratch) | **Questionable** | warn |
| Tampa Bay starting QB | TB | Open | no flip | stack fade |
| New England RG | NE | Open | no flip | scratch |
| **D'Andre Swift** | CHI | DNP (Warn) | **Active (FP)** | stack wait |

Washington named **Marcus Mariota** the starter for London; Daniels carries the Questionable tag. **The Mariota naming is DraftEdge-sourced, not a club filing** — the operator briefed against locking it. No Washington stack until Daniels is confirmed active.

### Focus / fade check — final

**Keeps:** JAX @ CIN (51.5, 2.5 spread, 68°F, 5 mph — unrestricted pass-funnel script). BUF pass (27.5 ITT, 6.5 home favorite, NE line depleted). KC @ LV (sealed dome; Bowers unlisted).

**Fades:** MIN passing (Jefferson OUT; total to 38.5; Miami at a slate-low 14.0 ITT). CHI passing (Williams OUT; starter unnamed; total to 42.5). TB passing (25 mph; ITT 17.5; Mayfield Q; starter unnamed — Godwin's full practice does not offset the environment).

### Saturday lock questions

NRG roof directive (DAL @ HOU); Raymond James wind persistence; MetLife wind verification; M&T precipitation intensity; London mist clearance. Inactive filings for Williams, Jefferson, Collins. Mariota confirmation and Daniels active status. Irving and Mayfield actives. Chicago and Tampa Bay starting QBs. New England RG alignment.

## Snippets

> "Prop evaluation incorporates structural constraints: anytime touchdown leans require an empirically cited goal-line carry rate, given that backfield vacancies alone do not confer goal-line usage." [Source: NFL Week 4 Slate Research.docx]

> "These things like player trades, college-transfer portals, coaches hirings, firings" — Casole, on adjacent PM products [Source: same, quoting IC360]

## Dead Ends

- **Weather is a forecast, not a reading.** The card was retrieved 09:36 EDT Friday. Wind and roof status must be re-checked at lock.
- **NRG remains officially uncalled** — the `[TENTATIVE]` tag on that row is correct; do not assume a closed roof.
- **Citation grades are not uniform.** Collins (OUT) and the Mariota naming are DraftEdge reads, not club pages. The Sam Cosmi "did not travel" note traces to a Daniels practice report. Treat all three as strong-but-secondary.
- **The Tampa Bay and Chicago starting quarterbacks are never named here on purpose.** Backup names circulating elsewhere are not confirmed. Do not ticket those cells.
- **The goal-line rule in this document is post-hoc.** It cites the PIT @ CLE outcome; see @sources/nfl-week4-tnf-result-postmortem-2026-10-02.md.
- **ITT values for DAL@HOU and LAC@SEA are odd** (25.2 / 22.2 and 25.2 / 18.2). They do not split evenly from the total. Treat as source artifacts, not true implieds. [NEEDS VERIFICATION 2026-10-02]

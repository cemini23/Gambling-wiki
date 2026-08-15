---
title: Brief K271 — REDAgentBench faithful-agent eval (arena hygiene)
type: source
tags: [brief, k271, poker, eval, redagentbench]
keywords: [faithful-asr, transcript-judging, harness-dependence, action-time-reminder]
related:
  - concepts/poker-hl-analyst-loop.md
  - sources/brief-k125-eval-gate-discipline-2026-06-22.md
maturity: draft
read_status: read
created: 2026-08-15
updated: 2026-08-15
wire_status: wont_wire
---

## Relations

- @concepts/poker-hl-analyst-loop.md — public eval hygiene only
- @sources/brief-k125-eval-gate-discipline-2026-06-22.md — same “judge the gate, not the story” class
- @cybersecurity-wiki/concepts/faithful-agent-asr-measurement.md — canon measurement page
- @cybersecurity-wiki/sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md — paper source
- Local brief (gitignored): `briefs/2026-08-12_k271-poker-arena-agent-eval-steal.md`

## Raw Concept

K271 (arXiv:2608.10669, REDAgentBench, 1,661 cases) → **eval hygiene** for arena-agent reviews. Benchmark not released; **REFERENCE / wont_wire**. No `decide()` import; no frequencies, foe tags, or live ranks on this public page.

## Narrative

Two stealable rules for **how we grade** an arena agent (not what it bets):

1. **Faithful measurement** — report behavior metrics as a `(harness, judging config, evaluation cue, judge backbone)` tuple. Transcript-only judging underestimated harm by **7.7–11.7 pp** and re-labeled **13–21%** of rollouts. Prefer ledger / API-state / chip-receipt diffs over the model’s self-report.
2. **Harness-dependence** — the same agent+scenario can swing **~40% → 95%** on a behavior metric from scaffolding alone. Keep **one harness** when comparing variants.
3. **Action-time reminder** — restate the applicable constraint at each action boundary; paper reports **>70 pp** confirmed-violation cut in matched replay. Public wiki use: “says the rule then violates it” is a **grading** failure mode, not a strategy leak.

Pairs with K125 eval-gate discipline. Cybersec owns the ASR construct; this page is the gambling-wiki pointer.

## Sources

- arXiv:2608.10669
- `@cybersecurity-wiki/sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md`

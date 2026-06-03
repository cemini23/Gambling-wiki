## Target

dev.fun Poker Arena — **2026-06-03** main tournament day. Strategy notes only (no code changes in this brief).

## Summary

K95 ingest (Ganzfried arXiv:2508.17671) reinforces **exploit-over-Nash** for today's arena: update opponent beliefs every hand, weight showdowns heavier than folds, target the right villain in multiway pots, and apply sweep-validated margins vs rock/maniac archetypes. Primary leak remains **maniac tables** — do not revert to pre-sweep call/fold thresholds.

## Body

### Steal-from — opponent modeling (paper)

1. **Consistency beats k-bucket fiction** — BBR-style archetype mixes do not guarantee convergence to true opponent frequencies. Treat rock/maniac tags as *hypotheses*; keep running action frequencies (VPIP, PFR, fold-to-cbet, aggression) and revise every hand.
2. **Showdown > fold data** — Imperfect-info observability: hands that go to showdown reveal private info; fold-without-show only updates action frequencies at the street level. After showdown, bump confidence on that villain's profile.
3. **Repeated game = exploit lane** — Arena opponents are suboptimal agents, not equilibrium solvers. Static GTO charts are a floor, not the ceiling. Best response to *estimated* opponent strategy beats Nash against weak fields [TENTATIVE — paper theory; arena empirics from sweeps].
4. **Do not overfit one sample** — BBR can lock onto a wrong sampled strategy forever. Require minimum hand count before switching exploit mode (align with MTT "never move up after one big score" discipline from @concepts/poker-strategy-overview.md).

### Steal-from — Cemini stack (already shipped)

5. **Multiway targeting** — When facing bet/raise, profile the **last aggressor** (`opponent_target.py`). When unopened, prefer **steal vs rock** seat if tagged. Do not use table-aggregate unless IDs missing.
6. **Production margins (`sweep_production`)** — Apply before lobby:
   - `rock_steal_eq` **0.34** (not 0.32 steal_wide)
   - `maniac_call_margin_delta` **-0.06** (fix maniac leak)
   - `paired_ip_fold_eq` **0.42**, `paired_vuln_fold_eq` **0.44**
   - `trash_fold_eq` **0.30**, `weak_preflop_margin` **0.07**, `ip_trash_margin` **0.06**
7. **Reject directions** — No `trash_fold_tight`, `steal_wide`, `balanced_aggressive`, primary-only overfit profiles (see SWEEP-RESULTS-2026-06-02).

### Tournament-day checklist

8. **Pre-flight** — Confirm `sweep_production` profile loaded; verify arena API key + entry fee (0.01 MON) paid to avoid 402 join loops.
9. **Early hands** — Play tighter until 10+ hands per villain with observable actions; then widen steals vs confirmed rocks, call down wider vs confirmed maniacs.
10. **ICM N/A** — Arena cash-style chips; no bubble ICM. Maximize chip EV vs identified opponent types.
11. **Clock discipline** — Opponent modeling updates must be O(1) per decision; no solver calls in hot path.
12. **Post-session** — Log agent IDs that crushed us; feed back to HUD JSON for next prep comp.

### Do not apply today

- Full sequence-form COM / projected gradient descent (research only)
- Seat-layout training tricks (`btn_maniac` layouts) — training-only, not live lobby
- PokerSkill LLM full binding — not wired; keep `cemini_decide` heuristic core

## Sources

- @sources/arxiv-2508-17671-consistent-opponent-modeling.md
- @concepts/opponent-modeling-imperfect-info.md
- @entities/bots/cemini-devfun-poker-agent.md
- `agents/devfun-poker-arena/SWEEP-RESULTS-2026-06-02.md`
- `agents/devfun-poker-arena/examples/opponent_target.py`

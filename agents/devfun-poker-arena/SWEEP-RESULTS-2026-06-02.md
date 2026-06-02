# Sweep results — 2026-06-02 (egress)

**Primary:** 125 profiles × 6-max × 2500 hands (rock+maniac or mixed seats)  
**Mixed:** same profiles × 6/4/2-max × 1500 hands/combo  
**Caveat:** bb/100 is vs simple local bots, not Arena DeepCFR. Use for **relative** ranking only.

## Default baseline (rank 105 / 125 primary, 103 / 125 mixed)

| Run | bb/100 |
|-----|--------|
| 6-max vs rock | +66.6 |
| 6-max vs maniac | **-155.4** |
| Mixed 6/4/2 weighted | -55.5 |

Primary leak: **maniac tables** with current call/fold thresholds.

## Recommended production bake-in (`sweep_production` profile)

Cross-sweep pick: **`g_s032_c-003_p042_t034`** (primary #4, mixed #1, stable vs maniac).

| Parameter | Was | Apply | Notes |
|-----------|-----|-------|-------|
| `rock_steal_eq` | 0.36 | **0.34** | Mixed winner; avoid `steal_wide` |
| `maniac_call_margin_delta` | -0.05 | **-0.06** | Looser calls vs maniac (fix leak) |
| `paired_ip_fold_eq` | 0.44 | **0.42** | Top-grid median |
| `paired_vuln_fold_eq` | 0.46 | **0.44** | paired + 0.02 |
| `trash_fold_eq` | 0.32 | **0.30** | Reject `trash_fold_tight` (+0.36) |
| `weak_preflop_margin` | 0.05 | **0.07** | `preflop_tight` +138 primary |
| `ip_trash_margin` | 0.05 | **0.06** | `preflop_tight` |

## Do not apply

| Profile / direction | Why |
|-------------------|-----|
| `trash_fold_tight` | -319 primary, -292 mixed |
| `steal_wide` (0.32 bar) | -83 / -87 |
| `balanced_aggressive` | -230 primary |
| `rock_oop_loose` | -240 primary |
| Primary-only #1 `g_s040_c-007_p046_t030` | +336 primary but **-6** mixed avg (6-max overfit) |
| Seat layouts (`btn_maniac`, etc.) | Training-only; live uses real agent stats |

## Seat layouts

Top primary ranks skew **`one_maniac_mp` / `btn_maniac`** (single run each). Useful for **training** (`TRAINING_SEAT_ARCHETYPES`), not baked into prod `decide()`.

## Next validation

1. Local 6-max: `./examples/run_train_cemini.sh rock 500 && ... maniac 500` vs old defaults  
2. Arena `pokerkit run --max-hands 50` before S28 lobby  
3. Re-enable prod lobby only after maniac line improves

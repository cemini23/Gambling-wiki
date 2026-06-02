#!/usr/bin/env python3
"""Overnight parameter sweep: profiles × opponents × table sizes.

Writes ranked CSV + JSON under reports/sweep/<stamp>/.

Env:
  SWEEP_HANDS          — hands per (profile, opponent, table size) (default 2500)
  SWEEP_PROFILES       — named+grid | named | grid | default | comma names
  SWEEP_SEED           — base RNG seed (default YYYYMMDD UTC)
  SWEEP_OPPONENTS      — comma list (default rock,maniac)
  SWEEP_PLAYER_SIZES   — comma seat counts 2–6 (default 6 for S28 full tables)
  SWEEP_PLAYER_WEIGHTS — optional N:weight for ranking, e.g. 6:0.55,4:0.25,2:0.20
  REPORT_DIR           — base dir (default reports/sweep)
"""
from __future__ import annotations

import csv
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

_EXAMPLES = Path(__file__).resolve().parent
_ROOT = _EXAMPLES.parent
if str(_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(_EXAMPLES))
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from selfplay import _load_decide_from_path, run_selfplay  # noqa: E402
from train_profiles import resolve_profile_list  # noqa: E402
from train_table_sizes import parse_player_sizes, parse_player_weights  # noqa: E402


def _env_int(key: str, default: int) -> int:
    raw = os.environ.get(key)
    return int(raw) if raw not in (None, "") else default


def _weighted_bb(rows: list[dict], seat_weights: dict[int, float]) -> float:
    """bb/100 averaged over rows, weighted by table size then opponent equally."""
    if not rows:
        return 0.0
    by_seat: dict[int, list[float]] = defaultdict(list)
    for r in rows:
        by_seat[int(r["players"])].append(float(r["bb_per_100"]))
    total = 0.0
    w_sum = 0.0
    for seat, w in seat_weights.items():
        vals = by_seat.get(seat)
        if not vals:
            continue
        total += w * (sum(vals) / len(vals))
        w_sum += w
    return total / w_sum if w_sum else 0.0


def main() -> int:
    hands = _env_int("SWEEP_HANDS", 2500)
    seed_base = os.environ.get("SWEEP_SEED") or datetime.now(timezone.utc).strftime("%Y%m%d")
    seed_base = int(seed_base)
    profile_spec = os.environ.get("SWEEP_PROFILES", "named+grid+seats")
    opp_raw = os.environ.get("SWEEP_OPPONENTS", "rock,maniac")
    opponents = [o.strip() for o in opp_raw.split(",") if o.strip()]
    player_sizes = parse_player_sizes(os.environ.get("SWEEP_PLAYER_SIZES", "6"))
    seat_weights = parse_player_weights(
        os.environ.get("SWEEP_PLAYER_WEIGHTS", ""),
        player_sizes,
    )

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    report_base = Path(os.environ.get("REPORT_DIR", "reports/sweep"))
    out_dir = report_base / stamp
    out_dir.mkdir(parents=True, exist_ok=True)

    agent_path = _EXAMPLES / "cemini_decide.py"
    decide_fn = _load_decide_from_path(str(agent_path))
    profiles = resolve_profile_list(profile_spec)

    print(f"cemini train sweep — {stamp}")
    print(f"profiles: {len(profiles)} ({profile_spec})")
    print(f"hands per (profile, opponent, seats): {hands}")
    print(f"opponents: {opponents}")
    print(f"table sizes: {player_sizes}  weights={seat_weights}")
    print(f"output: {out_dir}")
    print("")

    rows: list[dict] = []
    t_all = time.time()

    for idx, profile in enumerate(profiles):
        profile_rows: list[dict] = []
        for seat_i, n_players in enumerate(player_sizes):
            profile.apply(n_players=n_players)
            run_labels = profile.training_run_labels(opponents)
            for opp_i, run_label in enumerate(run_labels):
                seed = seed_base + idx * 10000 + seat_i * 1000 + opp_i
                if profile.is_homogeneous_seats():
                    os.environ["TRAINING_OPPONENT_MODE"] = run_label
                else:
                    os.environ.pop("TRAINING_OPPONENT_MODE", None)
                stats = run_selfplay(
                    decide_fn,
                    hands,
                    run_label,
                    n_players=n_players,
                    starting_stack=200,
                    small_blind=1,
                    big_blind=2,
                    seed=seed,
                    training_hud=True,
                )
                row = {
                    "profile": profile.name,
                    "opponent": run_label,
                    "seat_layout": profile.seat_layout or "uniform",
                    "seat_archetypes": os.environ.get("TRAINING_SEAT_ARCHETYPES", ""),
                    "players": stats["players"],
                    "hands": stats["hands"],
                    "bb_per_100": stats["bb_per_100"],
                    "net_chips": stats["net_chips"],
                    "wins": stats["wins"],
                    "losses": stats["losses"],
                    "elapsed_s": stats["elapsed_s"],
                    **{k: v for k, v in profile.to_dict().items()
                       if k != "seat_archetypes_applied"},
                }
                rows.append(row)
                profile_rows.append(row)
                layout_note = (
                    f" seats={row['seat_archetypes']}"
                    if row["seat_archetypes"] else ""
                )
                print(
                    f"[{idx + 1}/{len(profiles)}] {profile.name:32} "
                    f"{n_players}-max vs {run_label:14} "
                    f"bb/100={stats['bb_per_100']:+.1f}  ({stats['hands_per_s']:.0f} h/s)"
                    f"{layout_note}"
                )

        combo = _weighted_bb(profile_rows, seat_weights)
        by_seat = {
            str(seat): round(
                sum(r["bb_per_100"] for r in profile_rows if r["players"] == seat)
                / max(1, sum(1 for r in profile_rows if r["players"] == seat)),
                2,
            )
            for seat in player_sizes
        }
        summary_path = out_dir / "by_profile.jsonl"
        out_dir.mkdir(parents=True, exist_ok=True)
        with summary_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "profile": profile.name,
                "bb_per_100_weighted": round(combo, 2),
                "bb_per_100_by_seats": by_seat,
                "player_sizes": player_sizes,
                "seat_weights": seat_weights,
                "params": profile.to_dict(),
            }) + "\n")

    by_profile: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_profile[r["profile"]].append(r)

    ranked = sorted(
        (
            (name, _weighted_bb(prows, seat_weights), len(prows))
            for name, prows in by_profile.items()
        ),
        key=lambda x: x[1],
        reverse=True,
    )

    csv_path = out_dir / "results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    sizes_label = ",".join(str(s) for s in player_sizes)
    best_path = out_dir / "leaderboard.txt"
    lines = [
        f"cemini sweep leaderboard — {stamp}",
        f"profiles={len(profiles)} hands={hands}/combo seed={seed_base}",
        f"table_sizes={sizes_label}  weights={seat_weights}",
        f"elapsed_total={time.time() - t_all:.0f}s",
        "",
        "rank  profile                      weighted_bb/100",
        "────  ───────────────────────────  ────────────────",
    ]
    for rank, (name, avg_bb, _) in enumerate(ranked, 1):
        lines.append(f"{rank:4}  {name:28}  {avg_bb:+.1f}")
    best_name, best_bb, _ = ranked[0]
    lines.extend([
        "",
        f"BEST: {best_name} ({best_bb:+.1f} bb/100 weighted)",
        "",
        "Tournament S28 is 2–6 seats; default training is 6-max. "
        "Use SWEEP_PLAYER_SIZES=6,4,2 for a mixed-size sweep.",
    ])
    best_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    best_json = {
        "stamp": stamp,
        "table_sizes": player_sizes,
        "seat_weights": seat_weights,
        "best_profile": best_name,
        "bb_per_100_weighted": best_bb,
        "ranked": [{"rank": i + 1, "profile": n, "bb_per_100": b}
                   for i, (n, b, _) in enumerate(ranked)],
    }
    (out_dir / "best.json").write_text(
        json.dumps(best_json, indent=2) + "\n", encoding="utf-8"
    )

    latest = report_base / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    (latest / "leaderboard.txt").write_text(
        best_path.read_text(encoding="utf-8"), encoding="utf-8"
    )
    (latest / "best.json").write_text(
        (out_dir / "best.json").read_text(encoding="utf-8"), encoding="utf-8"
    )

    print("")
    print(best_path.read_text(encoding="utf-8"))
    print(f"[sweep] wrote {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

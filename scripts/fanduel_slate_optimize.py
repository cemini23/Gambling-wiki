#!/usr/bin/env python3
"""Generate FanDuel NFL lineups from a projection CSV via pydfs-lineup-optimizer.

Requires: pip install pydfs-lineup-optimizer

Input: FanDuel pydfs CSV (use normalize_dfs_projection_csv.py on Stokastic/Labs export,
or FanDuel site's official salary CSV download).

Usage:
  python3 scripts/fanduel_slate_optimize.py \\
    --csv "research to be indexed/fanduel-nfl-2026-09-07.csv" \\
    --count 150 \\
    --out "briefs/fanduel-lineups-2026-09-07.csv"

Stacking (optional — mirrors K124 3x1 game stacks):
  python3 scripts/fanduel_slate_optimize.py --csv ... --count 20 \\
    --stack qb:2 --max-exposure 0.4
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="FanDuel NFL lineup optimizer wrapper")
    parser.add_argument("--csv", required=True, help="Player projection CSV path")
    parser.add_argument("--count", type=int, default=150, help="Number of lineups (default 150)")
    parser.add_argument("--out", required=True, help="Output CSV path for lineups")
    parser.add_argument("--min-salary", type=int, default=59400, help="Min salary cap used (0=disable)")
    parser.add_argument("--max-exposure", type=float, default=0.35, help="Max player exposure 0-1")
    parser.add_argument("--stack", action="append", default=[], help="Stack rule e.g. qb:2 (repeatable)")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    out_path = Path(args.out)
    if not csv_path.is_file():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        return 1

    try:
        from pydfs_lineup_optimizer import Site, Sport, get_optimizer
        from pydfs_lineup_optimizer.stacks import TeamStack
    except ImportError:
        print(
            "ERROR: pydfs-lineup-optimizer not installed.\n"
            "  pip install pydfs-lineup-optimizer",
            file=sys.stderr,
        )
        return 1

    optimizer = get_optimizer(Site.FANDUEL, Sport.FOOTBALL)
    optimizer.load_players_from_csv(str(csv_path))
    optimizer.set_max_repeating_players(7)
    if args.min_salary:
        optimizer.set_min_salary_cap(args.min_salary)

    for rule in args.stack:
        parts = rule.lower().split(":")
        if len(parts) != 2:
            print(f"WARN: skip invalid --stack {rule!r} (want qb:2)", file=sys.stderr)
            continue
        pos, n = parts[0], int(parts[1])
        optimizer.add_stack(TeamStack(n, for_positions=[pos.upper()]))

    lineups = list(optimizer.optimize(n=args.count, max_exposure=args.max_exposure or None))
    if not lineups:
        print("ERROR: optimizer returned 0 lineups — check CSV columns/salaries", file=sys.stderr)
        return 1

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        header = ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DEF"]
        writer.writerow(header)
        for lu in lineups:
            by_pos: dict[str, list[str]] = {}
            for p in lu.players:
                by_pos.setdefault(p.lineup_position, []).append(p.full_name)
            row = []
            for col in header:
                names = by_pos.get(col, [])
                row.append(names.pop(0) if names else "")
            writer.writerow(row)

    print(f"Wrote {len(lineups)} lineups → {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

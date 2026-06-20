#!/usr/bin/env python3
"""Normalize Stokastic / FantasyLabs exports to FanDuel pydfs CSV format.

FanDuel pydfs requires columns: Id, First Name, Last Name, Position, Team,
Salary, FPPG, Game, Injury Indicator (see pydfs FanDuelCSVImporter).

Usage:
  python3 scripts/normalize_dfs_projection_csv.py \\
    --in "research to be indexed/stokastic-export.csv" \\
    --out "research to be indexed/fanduel-nfl-pydfs.csv"
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

NAME_KEYS = ("name", "player", "player name", "nickname")
POS_KEYS = ("position", "pos", "roster position")
SALARY_KEYS = ("salary", "fd salary", "fanduel salary", "sal")
FPPG_KEYS = ("fppg", "projection", "proj", "points", "fd pts", "fantasy points", "median")
TEAM_KEYS = ("team", "team abbrev", "teamabbrev", "tm")
GAME_KEYS = ("game", "game info", "matchup", "opp")
INJURY_KEYS = ("injury", "injury indicator", "inj", "status")
ID_KEYS = ("id", "player id", "fd id")

OUT_FIELDS = [
    "Id",
    "First Name",
    "Last Name",
    "Position",
    "Team",
    "Salary",
    "FPPG",
    "Game",
    "Injury Indicator",
]


def pick(row: dict[str, str], keys: tuple[str, ...]) -> str:
    lower = {k.strip().lower(): v for k, v in row.items()}
    for k in keys:
        if k in lower and str(lower[k]).strip():
            return str(lower[k]).strip()
    return ""


def split_name(full: str) -> tuple[str, str]:
    parts = full.strip().split(None, 1)
    if len(parts) == 1:
        return parts[0], parts[0]
    return parts[0], parts[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    inp = Path(args.inp)
    out = Path(args.out)
    if not inp.is_file():
        print(f"ERROR: not found: {inp}", file=sys.stderr)
        return 1

    rows_out: list[dict[str, str]] = []
    auto_id = 100000
    with inp.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("ERROR: empty CSV", file=sys.stderr)
            return 1
        for row in reader:
            name = pick(row, NAME_KEYS)
            pos = pick(row, POS_KEYS).upper()
            salary = pick(row, SALARY_KEYS).replace("$", "").replace(",", "")
            fppg = pick(row, FPPG_KEYS) or "0"
            team = pick(row, TEAM_KEYS) or "UNK"
            game = pick(row, GAME_KEYS)
            injury = pick(row, INJURY_KEYS)
            pid = pick(row, ID_KEYS) or str(auto_id)
            if not name or not pos or not salary:
                continue
            first, last = split_name(name)
            rows_out.append(
                {
                    "Id": pid,
                    "First Name": first,
                    "Last Name": last,
                    "Position": pos,
                    "Team": team,
                    "Salary": salary,
                    "FPPG": fppg,
                    "Game": game,
                    "Injury Indicator": injury,
                }
            )
            auto_id += 1

    if not rows_out:
        print("ERROR: no rows mapped — check column headers", file=sys.stderr)
        print(f"  headers: {reader.fieldnames}", file=sys.stderr)
        return 1

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_FIELDS)
        w.writeheader()
        w.writerows(rows_out)

    print(f"Normalized {len(rows_out)} players → {out} (FanDuel pydfs format)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

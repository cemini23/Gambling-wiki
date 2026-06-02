"""Named + grid profiles for overnight parameter sweeps."""
from __future__ import annotations

import itertools
import os
from dataclasses import asdict, dataclass
from typing import Iterator, Optional

from train_config import clear_profile_env, reset_hud_runtime
from train_seat_layouts import (
    SEAT_LAYOUT_GRID,
    fit_seat_archetypes,
    is_uniform_layout,
    layout_label,
)


@dataclass(frozen=True)
class TrainProfile:
    name: str
    # HUD vs rock
    rock_steal_eq: float = 0.36
    rock_bet_bar_delta: float = -0.10
    rock_preflop_fold_delta: float = 0.04
    # HUD vs maniac
    maniac_call_margin_delta: float = -0.05
    maniac_bet_bar_delta: float = 0.06
    # decide() thresholds
    trash_fold_eq: float = 0.32
    garbage_postflop_margin: float = 0.04
    paired_ip_fold_eq: float = 0.44
    paired_vuln_fold_eq: float = 0.46
    weak_preflop_margin: float = 0.05
    ip_trash_margin: float = 0.05
    rock_oop_fold_eq: float = 0.40
    # Mixed table composition (uniform = homogeneous TRAINING_OPPONENT_MODE)
    seat_layout: Optional[str] = "uniform"

    def is_homogeneous_seats(self) -> bool:
        return is_uniform_layout(self.seat_layout)

    def apply(self, *, n_players: int = 6) -> None:
        clear_profile_env()
        reset_hud_runtime()
        os.environ["CEMINI_PROFILE"] = self.name
        os.environ["CEMINI_ROCK_STEAL_EQ"] = str(self.rock_steal_eq)
        os.environ["CEMINI_ROCK_BET_BAR_DELTA"] = str(self.rock_bet_bar_delta)
        os.environ["CEMINI_ROCK_PREFLOP_FOLD_DELTA"] = str(self.rock_preflop_fold_delta)
        os.environ["CEMINI_MANIAC_CALL_MARGIN_DELTA"] = str(self.maniac_call_margin_delta)
        os.environ["CEMINI_MANIAC_BET_BAR_DELTA"] = str(self.maniac_bet_bar_delta)
        os.environ["CEMINI_TRASH_FOLD_EQ"] = str(self.trash_fold_eq)
        os.environ["CEMINI_GARBAGE_POSTFLOP_MARGIN"] = str(self.garbage_postflop_margin)
        os.environ["CEMINI_PAIRED_IP_FOLD_EQ"] = str(self.paired_ip_fold_eq)
        os.environ["CEMINI_PAIRED_VULN_FOLD_EQ"] = str(self.paired_vuln_fold_eq)
        os.environ["CEMINI_WEAK_PREFLOP_MARGIN"] = str(self.weak_preflop_margin)
        os.environ["CEMINI_IP_TRASH_MARGIN"] = str(self.ip_trash_margin)
        os.environ["CEMINI_ROCK_OOP_FOLD_EQ"] = str(self.rock_oop_fold_eq)

        os.environ.pop("TRAINING_SEAT_ARCHETYPES", None)
        archetypes = fit_seat_archetypes(self.seat_layout, n_players)
        if archetypes:
            os.environ["TRAINING_SEAT_ARCHETYPES"] = archetypes

    def training_run_labels(self, opponents: list[str]) -> list[str]:
        """Self-play runs for this profile (homogeneous → rock+maniac; mixed → layout once)."""
        if self.is_homogeneous_seats():
            return list(opponents)
        return [layout_label(self.seat_layout)]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["seat_archetypes_applied"] = os.environ.get("TRAINING_SEAT_ARCHETYPES")
        return d


DEFAULT = TrainProfile(name="default")

NAMED: dict[str, TrainProfile] = {
    "default": DEFAULT,
    "steal_wide": TrainProfile(
        name="steal_wide",
        rock_steal_eq=0.32,
        rock_bet_bar_delta=-0.12,
    ),
    "steal_tight": TrainProfile(
        name="steal_tight",
        rock_steal_eq=0.42,
        rock_bet_bar_delta=-0.06,
    ),
    "rock_passive": TrainProfile(
        name="rock_passive",
        rock_steal_eq=0.44,
        rock_bet_bar_delta=-0.04,
        rock_preflop_fold_delta=0.06,
    ),
    "maniac_loose_call": TrainProfile(
        name="maniac_loose_call",
        maniac_call_margin_delta=-0.08,
        maniac_bet_bar_delta=0.08,
    ),
    "maniac_tight_call": TrainProfile(
        name="maniac_tight_call",
        maniac_call_margin_delta=-0.02,
        maniac_bet_bar_delta=0.03,
    ),
    "paired_fold_tight": TrainProfile(
        name="paired_fold_tight",
        paired_ip_fold_eq=0.40,
        paired_vuln_fold_eq=0.42,
    ),
    "paired_fold_loose": TrainProfile(
        name="paired_fold_loose",
        paired_ip_fold_eq=0.48,
        paired_vuln_fold_eq=0.50,
    ),
    "trash_fold_tight": TrainProfile(
        name="trash_fold_tight",
        trash_fold_eq=0.36,
        garbage_postflop_margin=0.06,
        ip_trash_margin=0.07,
    ),
    "preflop_tight": TrainProfile(
        name="preflop_tight",
        weak_preflop_margin=0.08,
        ip_trash_margin=0.08,
        rock_preflop_fold_delta=0.06,
    ),
    "rock_oop_strict": TrainProfile(
        name="rock_oop_strict",
        rock_oop_fold_eq=0.36,
        rock_bet_bar_delta=-0.12,
    ),
    "rock_oop_loose": TrainProfile(
        name="rock_oop_loose",
        rock_oop_fold_eq=0.44,
        rock_bet_bar_delta=-0.06,
    ),
    "balanced_aggressive": TrainProfile(
        name="balanced_aggressive",
        rock_steal_eq=0.34,
        maniac_call_margin_delta=-0.07,
        paired_ip_fold_eq=0.42,
        trash_fold_eq=0.30,
    ),
    "seats_one_maniac_mp": TrainProfile(
        name="seats_one_maniac_mp",
        seat_layout="one_maniac_mp",
    ),
    "seats_btn_maniac": TrainProfile(
        name="seats_btn_maniac",
        seat_layout="btn_maniac",
    ),
    "seats_two_maniac": TrainProfile(
        name="seats_two_maniac",
        seat_layout="two_maniac",
    ),
    "seats_rock_blinds": TrainProfile(
        name="seats_rock_blinds",
        seat_layout="rock_blinds",
    ),
}


def _grid_profiles(*, include_seat_layouts: bool = True) -> list[TrainProfile]:
    """Factorial grid over steal / maniac call / paired / trash / optional seat layout."""
    profiles: list[TrainProfile] = []
    layouts: tuple[str, ...] = SEAT_LAYOUT_GRID if include_seat_layouts else ("uniform",)
    for steal, call_d, paired, trash, layout in itertools.product(
        (0.32, 0.36, 0.40),
        (-0.07, -0.05, -0.03),
        (0.42, 0.46),
        (0.30, 0.34),
        layouts,
    ):
        layout_suffix = "" if layout == "uniform" else f"_L{layout}"
        name = (
            f"g_s{steal:.2f}_c{call_d:.2f}_p{paired:.2f}_t{trash:.2f}{layout_suffix}"
        ).replace(".", "")
        profiles.append(
            TrainProfile(
                name=name,
                rock_steal_eq=steal,
                maniac_call_margin_delta=call_d,
                paired_ip_fold_eq=paired,
                paired_vuln_fold_eq=paired + 0.02,
                trash_fold_eq=trash,
                seat_layout=layout,
            )
        )
    return profiles


def iter_profiles(mode: str = "named+grid") -> Iterator[TrainProfile]:
    """mode: default | named | grid | grid+seats | named+grid | named+grid+seats | all"""
    mode = (mode or "named+grid").strip().lower()
    seen: set[str] = set()
    ordered: list[TrainProfile] = []

    def emit(p: TrainProfile) -> None:
        if p.name not in seen:
            seen.add(p.name)
            ordered.append(p)

    if mode == "default":
        return iter([DEFAULT])

    include_seats_in_grid = mode in ("grid+seats", "named+grid+seats", "all")
    grid_modes = ("grid", "grid+seats", "named+grid", "named+grid+seats", "all")

    if mode in ("named", "named+grid", "named+grid+seats", "all"):
        for p in NAMED.values():
            emit(p)

    if mode in grid_modes:
        for p in _grid_profiles(include_seat_layouts=include_seats_in_grid):
            emit(p)

    return iter(ordered)


def resolve_profile_list(spec: str) -> list[TrainProfile]:
    """Comma-separated names, or sweep mode keyword."""
    spec = (spec or "named+grid+seats").strip()
    keywords = (
        "default", "named", "grid", "grid+seats",
        "named+grid", "named+grid+seats", "all",
    )
    if spec in keywords:
        return list(iter_profiles(spec))
    names = [n.strip() for n in spec.split(",") if n.strip()]
    out: list[TrainProfile] = []
    for n in names:
        if n in NAMED:
            out.append(NAMED[n])
        elif n.startswith("g_") or n.startswith("g_s"):
            for p in _grid_profiles(include_seat_layouts=True):
                if p.name == n:
                    out.append(p)
                    break
            else:
                raise KeyError(f"unknown grid profile: {n}")
        elif n == "default":
            out.append(DEFAULT)
        else:
            raise KeyError(f"unknown profile: {n}")
    return out

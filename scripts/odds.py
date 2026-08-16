"""American-odds primitives from wiki vig / Kelly pages.

Market-relative only: convert prices, multiplicative two-way de-vig, EV, quarter-Kelly.
Does not claim a proprietary projection model.
"""

from __future__ import annotations

from typing import NamedTuple


class DevigResult(NamedTuple):
    fair_a: float
    fair_b: float
    hold: float


def american_to_implied(american: float) -> float:
    """Raw implied probability including vig. -110 → 110/210 ≈ 0.52381."""
    if american == 0:
        raise ValueError("American odds cannot be 0")
    if american < 0:
        a = -american
        return a / (a + 100.0)
    return 100.0 / (american + 100.0)


def american_to_decimal(american: float) -> float:
    if american == 0:
        raise ValueError("American odds cannot be 0")
    if american < 0:
        return 1.0 + (100.0 / -american)
    return 1.0 + (american / 100.0)


def american_to_b(american: float) -> float:
    """Net profit per $1 staked (Kelly `b`)."""
    return american_to_decimal(american) - 1.0


def multiplicative_devig(american_a: float, american_b: float) -> DevigResult:
    """Two-way multiplicative de-vig (proportional)."""
    pa = american_to_implied(american_a)
    pb = american_to_implied(american_b)
    total = pa + pb
    if total <= 0:
        raise ValueError("implied probabilities must be positive")
    return DevigResult(fair_a=pa / total, fair_b=pb / total, hold=total - 1.0)


def expected_value(fair_p: float, american: float) -> float:
    """EV per $1 staked: p * decimal - 1."""
    return fair_p * american_to_decimal(american) - 1.0


def decimal_to_american(decimal: float) -> float:
    if decimal <= 1.0:
        raise ValueError("decimal odds must be > 1")
    if decimal >= 2.0:
        return (decimal - 1.0) * 100.0
    return -100.0 / (decimal - 1.0)


def combine_parlay(americans: list[float]) -> float:
    """Independent parlay combined American odds (straight, not SGP-priced)."""
    if not americans:
        raise ValueError("need at least one leg")
    dec = 1.0
    for a in americans:
        dec *= american_to_decimal(a)
    return decimal_to_american(dec)


def kelly_fraction(fair_p: float, american: float, fraction: float = 0.25) -> float:
    """Fractional Kelly. Negative edge → 0. Caps at 0.05 of bankroll."""
    b = american_to_b(american)
    if b <= 0:
        return 0.0
    full = (fair_p * (b + 1.0) - 1.0) / b
    if full <= 0:
        return 0.0
    return min(full * fraction, 0.05)

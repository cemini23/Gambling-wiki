"""Table-size parsing for self-play sweeps (tournament is 2–6 seats; S28 opens 6-max)."""
from __future__ import annotations

# Default weights when SWEEP_PLAYER_WEIGHTS unset (tournament-shaped mix).
_TOURNAMENT_WEIGHTS: dict[int, float] = {
    6: 0.55,
    5: 0.10,
    4: 0.15,
    3: 0.08,
    2: 0.12,
}


def parse_player_sizes(spec: str) -> list[int]:
    """Comma list of seat counts, e.g. '6' or '6,4,2'."""
    raw = (spec or "6").strip()
    if not raw:
        return [6]
    out: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        n = int(part)
        if n < 2 or n > 6:
            raise ValueError(f"table size must be 2–6, got {n}")
        if n not in out:
            out.append(n)
    if not out:
        raise ValueError("empty SWEEP_PLAYER_SIZES / TRAIN_PLAYERS")
    return out


def parse_player_weights(spec: str, sizes: list[int]) -> dict[int, float]:
    """Weights for ranking combined bb/100 across table sizes."""
    if spec and spec.strip():
        weights: dict[int, float] = {}
        for part in spec.split(","):
            part = part.strip()
            if not part:
                continue
            if ":" not in part:
                raise ValueError(f"expected N:weight, got {part!r}")
            seat_s, w_s = part.split(":", 1)
            n = int(seat_s.strip())
            w = float(w_s.strip())
            if n < 2 or n > 6:
                raise ValueError(f"table size must be 2–6, got {n}")
            weights[n] = w
        for s in sizes:
            weights.setdefault(s, 0.0)
        total = sum(weights.get(s, 0.0) for s in sizes)
        if total <= 0:
            raise ValueError("player weights must sum to > 0")
        return {s: weights.get(s, 0.0) / total for s in sizes}

    if len(sizes) == 1:
        return {sizes[0]: 1.0}

    raw = {s: _TOURNAMENT_WEIGHTS.get(s, 1.0 / len(sizes)) for s in sizes}
    total = sum(raw.values())
    return {s: raw[s] / total for s in sizes}

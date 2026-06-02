"""Parse PokerSkill library user_prompt text into decide()-ready hints (no LLM)."""
from __future__ import annotations

from typing import Any


def parse_ps_prompt(user_prompt: str) -> dict[str, Any]:
    """Extract coarse action/texture hints from PokerSkill prompt body."""
    low = user_prompt.lower()
    out: dict[str, Any] = {}

    if "default action is check" in low or "default action is to check" in low:
        out["bias"] = "check"
    if "no bet to face" in low and "open (2.5bb)" in low:
        out.setdefault("bias", "raise")
    if "defender oop" in low or "you are the defender" in low:
        out["pot_control"] = True
        out.setdefault("bias", "check")
    if "pot control" in low or "check-call or check" in low:
        out["pot_control"] = True
    if "two-tone" in low or "flush draw exists" in low:
        out["board_texture"] = "wet"
        out["pot_control"] = True
    if "nut high" in low and "draw" in low:
        out["hand_eval"] = "nut_high_draw"
        out["pot_control"] = True
        out.setdefault("bias", "check")
    if "nut high" in low and "no draw" in low:
        out["hand_eval"] = "nut_high"
    if "recommend fold" in low or "should fold" in low:
        out["bias"] = "fold"
    if "open (2.5bb)" in low or "btn opens" in low:
        out.setdefault("bias", "raise")
    if "bet/raise for value" in low or "value bet" in low:
        out["bias"] = "raise"
    if "check-raise" in low and "consider" in low:
        out.setdefault("bias", "check")

    return out


def merge_prompt_hints(base: dict[str, Any], user_prompt: str) -> dict[str, Any]:
    """Merge parse_ps_prompt() into an existing pokerskill hints dict."""
    parsed = parse_ps_prompt(user_prompt)
    out = dict(base)
    for key, val in parsed.items():
        if key == "bias" and out.get("bias") and out.get("mode") == "library":
            # Parsed text overrides coarse _bias_from_prompt only when explicit.
            if val in ("check", "raise", "call") or parsed.get("hand_eval"):
                out[key] = val
        elif key not in out or out.get("mode") != "library":
            out[key] = val
        elif key in ("pot_control", "hand_eval", "board_texture"):
            out[key] = val
    return out

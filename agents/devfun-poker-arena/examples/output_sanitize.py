"""Strip strategy telegraphy from Arena action payloads (prod anti-profiling)."""
from __future__ import annotations

import os
from typing import Any

GENERIC_MESSAGE = "act"
FALLBACK_REASONING = '{vr: "std", ke: "legal", pp: "pot control"}'

_ACTION_MESSAGES = {
    "fold": "fold",
    "check": "check",
    "call": "call",
    "bet": "bet",
    "raise": "raise",
    "all-in": "all-in",
}


def sanitize_output_enabled() -> bool:
    raw = os.environ.get("CEMINI_SANITIZE_OUTPUT", "")
    return raw.lower() in ("1", "true", "yes")


def maybe_sanitize_action(action: dict[str, Any]) -> dict[str, Any]:
    """Return a copy with generic message/reasoning when sanitization is on."""
    if not sanitize_output_enabled():
        return action
    out = dict(action)
    act = str(out.get("action") or "fold")
    out["message"] = _ACTION_MESSAGES.get(act, GENERIC_MESSAGE)[:500]
    out["reasoning"] = FALLBACK_REASONING
    return out

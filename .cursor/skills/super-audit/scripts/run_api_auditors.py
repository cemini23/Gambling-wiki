#!/usr/bin/env python3
"""Run API leg of super-audit (slots 4–5) via OpenAI-compatible endpoints.

Usage:
  python3 discover_api_keys.py
  python3 build_audit_pack.py --prompt ... --out reports/audit/pack-foo
  python3 run_api_auditors.py --pack reports/audit/pack-foo --out reports/audit/premium-foo
  python3 run_api_auditors.py --pack ... --auditors path/to/auditors.json --dry-run
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent

DEFAULT_AUDITORS = SKILL_ROOT / "auditors.default.json"


def _load_env(workspace: Path) -> None:
    candidates = [
        os.environ.get("CEMINI_LLM_ROUTING_ENV", "").strip(),
        str(Path.home() / ".cemini" / "llm-routing.env"),
        str(workspace / ".env"),
        str(workspace / "config" / "llm-routing.env"),
    ]
    for path_s in candidates:
        if not path_s:
            continue
        p = Path(path_s)
        if not p.is_file():
            continue
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v
        break

    os.environ.setdefault("OLLAMA_BASE_URL", "http://localhost:11434/v1")

    # WC-style advisor wiring when unset
    if not os.environ.get("ADVISOR_BASE_URL", "").strip() and os.environ.get(
        "OPENROUTER_API_KEY", ""
    ).strip():
        os.environ.setdefault(
            "ADVISOR_BASE_URL",
            os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        )
        os.environ.setdefault("ADVISOR_API_KEY", os.environ["OPENROUTER_API_KEY"])
        os.environ.setdefault(
            "ADVISOR_MODEL", os.environ.get("LLM_FALLBACK_MODEL_ADVISOR", "google/gemini-2.5-flash")
        )


def _resolve_env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def _call_openai_compat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    system: str,
    extra: dict | None = None,
    max_tokens: int = 16_000,
) -> str:
    import httpx

    url = base_url.rstrip("/") + "/chat/completions"
    body: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "max_tokens": max_tokens,
    }
    if extra:
        body.update(extra)
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    elif "11434" not in base_url and "localhost" not in base_url:
        headers["Authorization"] = "Bearer "
    if "openrouter.ai" in base_url:
        headers["HTTP-Referer"] = _resolve_env(
            "OPENROUTER_HTTP_REFERER", "https://github.com/cemini23"
        )
        headers["X-Title"] = _resolve_env("OPENROUTER_APP_TITLE", "super-audit")
    r = httpx.post(url, headers=headers, json=body, timeout=600.0)
    r.raise_for_status()
    return (r.json()["choices"][0]["message"]["content"] or "").strip()


def _load_auditors(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    slots = data.get("slots") or data
    if not isinstance(slots, list):
        raise ValueError("auditors file must have 'slots' list")
    return slots


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--pack", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--auditors", type=Path, default=None)
    ap.add_argument(
        "--discover",
        action="store_true",
        help="Build auditors.json from discover_api_keys (OpenRouter + Ollama)",
    )
    ap.add_argument("--workspace", type=Path, default=Path.cwd())
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slot", default="", help="Run single label only")
    args = ap.parse_args()

    workspace = args.workspace.resolve()
    _load_env(workspace)

    pack = args.pack.resolve()
    prompt_path = pack / "audit_prompt.md"
    if not prompt_path.is_file():
        print(f"Missing {prompt_path} — run build_audit_pack.py first", file=sys.stderr)
        return 1

    base_prompt = prompt_path.read_text(encoding="utf-8")
    out_dir = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")

    tier = ""
    if args.discover or args.auditors is None:
        sys.path.insert(0, str(SCRIPT_DIR))
        from discover_api_keys import discover, recommend_auditors  # noqa: E402

        disc = discover(workspace)
        rec = recommend_auditors(disc)
        slots = rec["slots"]
        tier = rec["tier"]
        auditors_path = out_dir / f"auditors_{ts}.json"
        auditors_path.write_text(
            json.dumps(
                {"slots": slots, "tier": tier, "auditor_count": rec["auditor_count"]},
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"Discovered tier={tier} → {auditors_path}")
        if not slots:
            print("No API slots available (need OpenRouter key or running Ollama)", file=sys.stderr)
            return 1
    else:
        auditors_path = args.auditors.resolve()
        if not auditors_path.is_file():
            print(f"Missing auditors config: {auditors_path}", file=sys.stderr)
            return 1
        slots = _load_auditors(auditors_path)
    if args.slot:
        slots = [s for s in slots if s.get("label") == args.slot]
        if not slots:
            print(f"No slot label {args.slot!r}", file=sys.stderr)
            return 1

    if args.dry_run:
        print(f"Prompt {len(base_prompt)} chars → {out_dir}")
        print(f"Slots: {[s.get('label') for s in slots]}")
        return 0

    written: dict[str, Path] = {}
    errors: list[str] = []

    for slot in slots:
        label = slot.get("label") or "api-auditor"
        key_env = slot.get("api_key_env", "OPENROUTER_API_KEY")
        base_env = slot.get("base_url_env", "OPENROUTER_BASE_URL")
        api_key_optional = bool(slot.get("api_key_optional"))
        model_env = slot.get("model_env", "").strip()
        model = _resolve_env(model_env, slot["model"]) if model_env else slot["model"]
        api_key = _resolve_env(key_env) if key_env else ""
        default_base = (
            "http://localhost:11434/v1"
            if slot.get("local") or base_env == "OLLAMA_BASE_URL"
            else "https://openrouter.ai/api/v1"
        )
        base_url = _resolve_env(base_env, default_base)
        max_tokens = int(slot.get("max_tokens", 16_000))
        system = slot.get(
            "system",
            "Super audit — expert readonly reviewer. Follow required output format exactly.",
        )
        extra = slot.get("extra")
        if model == "openrouter/fusion" and not extra:
            extra = {"plugins": [{"id": "fusion"}]}

        if not api_key and not api_key_optional:
            msg = f"{label}: missing {key_env}"
            errors.append(msg)
            err_path = out_dir / f"{label}_{ts}_SKIPPED.txt"
            err_path.write_text(msg + "\n", encoding="utf-8")
            written[label] = err_path
            print(f"  SKIP {msg}", file=sys.stderr)
            continue

        prompt = base_prompt.replace("{{MODEL_SLOT}}", label)
        provider = slot.get("provider", "api")
        print(f"Calling {label} ({model}) via {provider}...")
        try:
            text = _call_openai_compat(
                base_url=base_url,
                api_key=api_key,
                model=model,
                prompt=prompt,
                system=system,
                extra=extra,
                max_tokens=max_tokens,
            )
            out_path = out_dir / f"{label}_{ts}.md"
            out_path.write_text(text, encoding="utf-8")
            written[label] = out_path
            print(f"  OK {len(text)} chars → {out_path.name}")
        except Exception as e:
            err_path = out_dir / f"{label}_{ts}_ERROR.txt"
            err_path.write_text(str(e), encoding="utf-8")
            written[label] = err_path
            errors.append(f"{label}: {e}")
            print(f"  FAIL {e}", file=sys.stderr)

    meta = {
        "timestamp": ts,
        "pack": str(pack),
        "auditors_file": str(auditors_path),
        "tier": tier or None,
        "models": list(written.keys()),
        "errors": errors,
    }
    (out_dir / f"meta_{ts}.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, indent=2))

    ok = sum(1 for p in written.values() if p.suffix == ".md")
    return 0 if ok > 0 and not errors else (1 if not ok else 0)


if __name__ == "__main__":
    raise SystemExit(main())

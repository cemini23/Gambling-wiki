"""Small GET-JSON helper. No paid keys."""

from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

UA = "gambling-wiki-slate/1.0 (personal research; no commercial use)"


def get_json(url: str, *, timeout: float = 30) -> object:
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as exc:
        body = exc.read().decode(errors="replace")[:400]
        raise RuntimeError(f"HTTP {exc.code} {url}: {body}") from exc
    except URLError as exc:
        raise RuntimeError(f"unreachable {url}: {exc}") from exc

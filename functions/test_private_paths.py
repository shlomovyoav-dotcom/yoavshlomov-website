#!/usr/bin/env python3
"""Private-path patterns from functions/_middleware.js (stdlib only).

Mirrors PRIVATE_PATTERNS so a Pages Function change that drops /drafts or
/dns fails in CI without wrangler. Run: python3 functions/test_private_paths.py
"""

from __future__ import annotations

import re
import sys

# Keep in sync with functions/_middleware.js
PRIVATE_PATTERNS = [
    re.compile(r"^/dns(/|$)", re.I),
    re.compile(r"^/docs(/|$)", re.I),
    re.compile(r"^/agents\.md$", re.I),
    re.compile(r"^/drafts(/|$)", re.I),
    re.compile(r"^/verification\.md$", re.I),
]

MUST_BLOCK = [
    "/dns",
    "/dns/",
    "/dns/full-blocklist.mobileconfig",
    "/docs/PRINTFUL-RUNBOOK.md",
    "/AGENTS.md",
    "/agents.md",
    "/drafts/raj-hoopoe-website.md",
    "/VERIFICATION.md",
]

MUST_ALLOW = [
    "/",
    "/index.html",
    "/press.html",
    "/l/k7Qm2xR9/qa/",
    "/l/k7Qm2xR9/music/",
]


def is_private(pathname: str) -> bool:
    return any(p.search(pathname) for p in PRIVATE_PATTERNS)


def main() -> int:
    errors: list[str] = []
    for path in MUST_BLOCK:
        if not is_private(path):
            errors.append(f"should 404: {path}")
    for path in MUST_ALLOW:
        if is_private(path):
            errors.append(f"should serve: {path}")
    if errors:
        print("FAILED private-path checks:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(f"OK   {len(MUST_BLOCK)} private paths blocked, {len(MUST_ALLOW)} public paths open")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

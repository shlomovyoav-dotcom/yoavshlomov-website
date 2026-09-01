#!/usr/bin/env python3
"""Allowlist and generator smoke tests (no Apple devices required).

Run: python3 dns/test_generate_blocklist.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import generate_blocklist as gen

ALLOWLIST_DOMAINS = (
    "pluxee.co.il",
    "cibus.pluxee.co.il",
    "consumers.pluxee.co.il",
    "kan.org.il",
    "www.kan.org.il",
    "kan11.co.il",
    "kankids.org.il",
    "media.kan.org.il",
    "player.kan.org.il",
)
MUST_STILL_BLOCK = (
    "pornhub.com",
    "wolt.com",
    "instagram.com",
    "ynet.co.il",
)
KAN_APP_ID = "com.applicaster.il.ch1"


def main() -> int:
    errors: list[str] = []
    domains = gen.read_domains()
    hosts = gen.expand_hosts(domains)
    hosts_set = set(hosts)
    domains_set = set(domains)

    for d in ALLOWLIST_DOMAINS:
        if d in domains_set or d in hosts_set:
            errors.append(f"allowlisted domain still in generator input/hosts: {d}")

    for d in MUST_STILL_BLOCK:
        if d not in domains_set:
            errors.append(f"expected still-blocked domain missing from domains.txt: {d}")

    if KAN_APP_ID in gen.BLOCKED_APP_BUNDLE_IDS:
        errors.append(f"Kan 11 app still in BLOCKED_APP_BUNDLE_IDS: {KAN_APP_ID}")

    # Generated artifacts must match the generator (no stale Kan/Cibus entries).
    hosts_text = (HERE / "hosts-blocklist.txt").read_text()
    nextdns_text = (HERE / "nextdns-denylist.txt").read_text()
    mobileconfig = (HERE / "full-blocklist.mobileconfig").read_text()
    for d in ("kan.org.il", "pluxee.co.il", "kan11.co.il"):
        if re.search(rf"(^|\n)0\.0\.0\.0 {re.escape(d)}(\n|$)", hosts_text):
            errors.append(f"stale hosts-blocklist entry: {d}")
        if re.search(rf"(^|\n){re.escape(d)}(\n|$)", nextdns_text):
            errors.append(f"stale nextdns-denylist entry: {d}")
        if f"<string>https://{d}</string>" in mobileconfig:
            errors.append(f"stale mobileconfig URL: https://{d}")
    if KAN_APP_ID in mobileconfig:
        errors.append(f"stale mobileconfig app id: {KAN_APP_ID}")

    if errors:
        print("FAILED dns allowlist checks:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK   {len(domains)} domains, {len(hosts)} hosts; Cibus + Kan 11 absent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

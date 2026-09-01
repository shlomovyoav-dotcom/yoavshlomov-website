#!/usr/bin/env python3
"""Public-page SEO invariants. Stdlib only.

The live site is a single public homepage plus a printable EPK. Unlisted
letter pages under /l/ must never appear in the sitemap. Run:

    python3 test_public_seo.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX = (ROOT / "index.html").read_text(encoding="utf-8")
PRESS = (ROOT / "press.html").read_text(encoding="utf-8")
SITEMAP = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
ROBOTS = (ROOT / "robots.txt").read_text(encoding="utf-8")

PUBLIC_LOCS = {
    "https://yoavshlomov.com/",
    "https://yoavshlomov.com/press",
}

ALBUMS = [
    ("3/4", "https://open.spotify.com/album/5QamvPbVeonJOc0crP0KIm"),
    ("Like Sonny", "https://open.spotify.com/album/0Mq8M8eWmFJdmKgpM2vm9C"),
    ("Hell Nah", "https://open.spotify.com/album/372JLsEXQguUUTd73gwCRW"),
    ("Tired", "https://open.spotify.com/album/0fsWV99MD98gs79B2ZawyS"),
    ("i cAn feel u NoW", "https://open.spotify.com/album/1zWf7hBEUMUrqs3gN4o3sz"),
    ("Bye Bye Everything", "https://open.spotify.com/album/0sIGDeJjq88tbOmcia8iMf"),
]


def _ld_blocks(html: str) -> list[dict]:
    blocks = []
    for m in re.finditer(
        r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
        html,
        re.S,
    ):
        blocks.append(json.loads(m.group(1)))
    return blocks


def main() -> int:
    errors: list[str] = []

    locs = set(re.findall(r"<loc>([^<]+)</loc>", SITEMAP))
    if locs != PUBLIC_LOCS:
        errors.append(f"sitemap locs {sorted(locs)} != {sorted(PUBLIC_LOCS)}")
    if "/l/" in SITEMAP or "k7Qm2xR9" in SITEMAP:
        errors.append("sitemap must not list unlisted letter pages")

    if "Disallow: /l/" not in ROBOTS:
        errors.append("robots.txt must disallow /l/")
    if "Sitemap: https://yoavshlomov.com/sitemap.xml" not in ROBOTS:
        errors.append("robots.txt must point at the sitemap")

    if 'rel="canonical" href="https://yoavshlomov.com/press"' not in PRESS:
        errors.append("press canonical should be /press (pretty URL)")
    if 'property="og:image"' not in PRESS:
        errors.append("press page needs an Open Graph image")
    if "application/ld+json" not in PRESS:
        errors.append("press page needs JSON-LD")

    ld = _ld_blocks(INDEX)
    if not ld:
        errors.append("homepage missing JSON-LD")
    else:
        person = next((b for b in ld if b.get("@type") == "Person"), ld[0])
        albums = person.get("album") or []
        names = {a.get("name") for a in albums}
        urls = {a.get("url") for a in albums}
        for name, url in ALBUMS:
            if name not in names:
                errors.append(f"JSON-LD missing album {name!r}")
            if url not in urls:
                errors.append(f"JSON-LD missing album url {url}")

    if "shlomovyoav@gmail.com" not in INDEX.split('id="concerts"', 1)[-1][:800]:
        errors.append("concerts section should include the booking address")

    if errors:
        print("FAILED public SEO checks:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(
        f"OK   sitemap {len(PUBLIC_LOCS)} public URLs, "
        f"{len(ALBUMS)} albums in JSON-LD, press OG+canonical"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

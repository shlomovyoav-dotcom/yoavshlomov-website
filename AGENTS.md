# Agent instructions — yoavshlomov.com

## What this repo is

Yoav Shlomov's public website (jazz guitarist & producer). Pure HTML/CSS, no
build step. Deployed by Cloudflare Pages: **every file pushed to `main` is
served publicly at yoavshlomov.com immediately** unless `_redirects` returns
404 for it.

## Privacy rules (non-negotiable)

- Never commit personal documents, letters, IDs, passwords, or anything from
  the `Personal`/`Admin` folders on Yoav's Mac. Those belong in separate
  private repos, never in this one.
- `dns/` (personal blocklist project) and `docs/` are blocked from serving in
  `_redirects`. If you add private folders/files, add matching 404 rules in
  the same commit.
- Never write real passwords or unlock codes into this repo or into chat —
  see the password protocol in `dns/README.md`.
- Unlisted-but-served content (reference letters) lives under `/l/<token>/`
  with `noindex` headers; keep that pattern for anything semi-private.

## The blocker project (`dns/`)

Long-running project blocking porn, deepfake/nudify tools, food delivery,
Instagram/Facebook and news across Yoav's iPhone (supervised via Apple
Configurator), Mac, and home router. Yoav's father holds all unlock passwords
in a physical safe — he is the accountability contact for lock changes.

- `dns/domains.txt` is the single source of truth. Edit it, then run
  `python3 dns/generate_blocklist.py` and commit the regenerated artifacts.
- Never hand-edit `full-blocklist.mobileconfig`, `hosts-blocklist.txt` or
  `nextdns-denylist.txt` — they are generated.
- Read `dns/README.md` before changing anything device-related; it contains
  the install runbook, the honest security limits, and the test matrix.
- When asked to "improve the blocks", additions should go to `domains.txt`
  with a dated comment header so Yoav can review what changed.

## Site conventions

- `_headers` / `_redirects` are Cloudflare Pages config — mind them when
  adding or removing pages.
- Hidden-from-live content is parked in `_preview/` (e.g. the Shop section).
- No frameworks, no dependencies; keep it that way unless Yoav asks.

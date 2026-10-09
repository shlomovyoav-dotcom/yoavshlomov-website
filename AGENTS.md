# Agent instructions — yoavshlomov.com

## Language

Every reply to the user is **one language only**:

- User writes in Hebrew → reply entirely in Hebrew.
- User writes in English → reply entirely in English.
- Never mix Hebrew and English in the same sentence or the same message.
- Do not translate mid-sentence. Do not put English narration inside Hebrew prose, or Hebrew inside English prose.
- File paths, URLs, code, and proper names stay as written. The surrounding sentence stays in the chosen language.

## What this repo is (subject 1 of 2)

Yoav Shlomov's **public brand** site (jazz guitarist & producer). Pure HTML/CSS,
no build step. Deployed by Cloudflare Pages: **every file pushed to `main` is
served publicly at yoavshlomov.com immediately** unless `_redirects` /
`functions/_middleware.js` return 404 for it.

Agents use **at most two** GitHub remotes, divided by subject:

1. **This repo** — public site, unlisted hub `/l/<token>/`, Printful docs, `dns/` blocklist generator.
2. **`yoav-knowledge` (private)** — MEMORY, Personal, Admin, Claude/Cursor rules, the one MASTER routine. Lives on iCloud as `YoavAI/` locally.

Do not create a third agent repo. Full map: `docs/AI-WORKSPACE.md`.

## Privacy rules (non-negotiable)

- Never commit personal documents, letters, IDs, passwords, CVs, or anything
  from Mac `Personal` / `Admin` / iCloud `YoavAI/` into **this** public repo.
  Those belong only in `yoav-knowledge`.
- `dns/`, `docs/`, `AGENTS.md` are blocked from serving. If you add private
  folders or files, add matching 404 rules in `_redirects` **and** a pattern in
  `functions/_middleware.js` in the same commit. The Function is authoritative
  because redirects cannot shadow existing static assets.
- Never write real passwords or unlock codes into this repo or into chat —
  see the password protocol in `dns/README.md` when that file is present.
- Unlisted-but-served content (reference letters) lives under `/l/<token>/`
  with `noindex` headers; keep that pattern for anything semi-private.

## The blocker project (`dns/`)

Long-running project blocking porn, deepfake/nudify tools, food delivery,
Instagram/Facebook and news across Yoav's iPhone (supervised via Apple
Configurator), Mac, and home router. Yoav's father holds all unlock passwords
in a physical safe — he is the accountability contact for lock changes.

- When `dns/domains.txt` exists, it is the single source of truth. Edit it,
  then run `python3 dns/generate_blocklist.py` and commit regenerated artifacts.
- Never hand-edit generated `full-blocklist.mobileconfig`, `hosts-blocklist.txt`
  or `nextdns-denylist.txt`.

## Site conventions

- `_headers` / `_redirects` are Cloudflare Pages config — mind them when
  adding or removing pages.
- Hidden-from-live content is parked in `_preview/` (e.g. the Shop section).
- No frameworks, no dependencies; keep it that way unless Yoav asks.

## Memory and routines live in the private knowledge repo

This public repo must never hold `MEMORY.md`, recovered chats, or Personal/Admin
trees. After a wipe, clone `github.com/shlomovyoav-dotcom/yoav-knowledge` (create
it from `docs/yoav-knowledge-scaffold/` if missing). New private chats: read
`MEMORY.md` there. One shared routine: `routines/MASTER.md` /
`docs/MASTER-ROUTINE.md`.

Mac: iCloud Drive `YoavAI/` = working tree of `yoav-knowledge`
(`docs/ICLOUD-BOOTSTRAP.md`).

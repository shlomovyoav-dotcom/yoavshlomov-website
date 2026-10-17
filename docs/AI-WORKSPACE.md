# AI workspace — one source of truth

Goal: Claude Code (local) and Cursor (Desktop + Cloud) share **one** memory and
routine set on iCloud, with **at most two** GitHub repos by subject.

## The two subjects (max 2 repos)

| # | Subject | Repo | Where agents work |
|---|---------|------|-------------------|
| 1 | **Public brand** — site, private hub `/l/…`, Printful docs, `dns/` blocklist that ships with the site | `shlomovyoav-dotcom/yoavshlomov-website` (public) | Cursor Cloud env for the website; Desktop when editing the site |
| 2 | **Private life + AI** — memory, Personal, Admin, drafts, career, passport, banking notes, Claude/Cursor rules, the one MASTER routine | `shlomovyoav-dotcom/yoav-knowledge` (private) | iCloud folder = git working tree; Cloud only after the private repo exists and is connected |

Anything that used to look like a **third** cloud repo (orphan Personal/Admin
remotes, a half-created knowledge env, Claude-only project duplicates) folds
into subject 2. Do not add a third GitHub remote for agents.

### What is *not* a third repo

- `yoav-scoring.pages.dev` — media host for the scoring reel, not an agent workspace.
- In-repo “three projects” (site + dns + hub) stay **inside** subject 1.
- Father’s Mac **Admin account** is a login role, not a GitHub repo.

## iCloud is the human source of truth

Cloud agents cannot mount iCloud. They only see Git remotes. So:

1. **iCloud Drive / `YoavAI/`** holds the live files Claude and Desktop Cursor open every day.
2. That same folder **is** (or mirrors) the `yoav-knowledge` git tree.
3. Push to GitHub when you want Cloud Cursor on private work.
4. Website work stays in `yoavshlomov-website` only — never copy CVs, MEMORY, or Personal/Admin files into it.

Recommended Mac path:

```text
~/Library/Mobile Documents/com~apple~CloudDocs/YoavAI/
```

Bootstrap steps: `docs/ICLOUD-BOOTSTRAP.md`. Folder layout scaffold:
`docs/yoav-knowledge-scaffold/`.

## Claude + Cursor — same brain

| Tool | Reads |
|------|--------|
| Claude Code | `YoavAI/CLAUDE.md` → `MEMORY.md`, `routines/MASTER.md` |
| Cursor Desktop | Open `YoavAI/` as a workspace (or multi-root with the website) |
| Cursor Cloud | Clone `yoav-knowledge` and/or `yoavshlomov-website` — never invent a third |

Rules of engagement:

- One language per reply (see root `AGENTS.md`).
- Drafts only until Yoav approves send/delete/pay/install.
- Passwords and unlock codes never in git or chat.

## Cloud ↔ local merge map

| Content | Local / iCloud | Cloud |
|---------|----------------|-------|
| Site HTML/CSS, hub, dns generator | Clone of website repo | Same website env |
| MEMORY, Personal, Admin, career drafts | `YoavAI/` | `yoav-knowledge` only |
| MASTER routine prompt | `YoavAI/routines/MASTER.md` | One Cursor Automation using that text |
| Skills you want everywhere | Cursor Settings → Agents → Sync Skills; copy stable skills into `YoavAI/skills/` | Cloud picks up skills from the private repo when present |

## Cleanup checklist

1. Create and connect `yoav-knowledge` (if missing).
2. Wire iCloud `YoavAI/` → that repo (`docs/ICLOUD-BOOTSTRAP.md`).
3. Archive stale chats (`docs/ARCHIVE-CHATS.md`).
4. Replace many routines with one (`docs/MASTER-ROUTINE.md`).
5. Cursor Environments: only the two subject repos.

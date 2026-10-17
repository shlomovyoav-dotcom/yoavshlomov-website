# iCloud bootstrap (Mac)

Do this once on the Mac so Claude Code and Cursor Desktop share one brain, and
Cloud can clone the same tree via GitHub.

## 1. Create the private repo

If `github.com/shlomovyoav-dotcom/yoav-knowledge` does not exist yet:

```bash
gh repo create shlomovyoav-dotcom/yoav-knowledge --private --clone
cd yoav-knowledge
```

Copy everything from this website repo’s `docs/yoav-knowledge-scaffold/` into
the new repo root, then:

```bash
git add .
git commit -m "chore: initial AI source of truth"
git push -u origin main
```

In Cursor → Settings → GitHub, ensure the private repo is accessible to Cloud Agents.

## 2. Put the working tree on iCloud

```bash
ICLOUD="$HOME/Library/Mobile Documents/com~apple~CloudDocs/YoavAI"
mkdir -p "$ICLOUD"
# Either clone into YoavAI, or move the clone you just made:
# git clone git@github.com:shlomovyoav-dotcom/yoav-knowledge.git "$ICLOUD"
# OR: rsync -a ./yoav-knowledge/ "$ICLOUD/" && cd "$ICLOUD" && git remote -v
```

Finder label: **iCloud Drive → YoavAI**.

## 3. Merge local Personal / Admin into subject 2

```bash
# Adjust source paths if yours differ
mkdir -p "$ICLOUD/personal" "$ICLOUD/admin"
# Copy (do not leave secrets only in a Desktop handoff):
# cp -R ~/Documents/Personal/* "$ICLOUD/personal/"
# cp -R ~/Documents/Admin/* "$ICLOUD/admin/"
cd "$ICLOUD"
git add personal admin
git status   # review — strip passwords before commit
git commit -m "chore: merge Personal and Admin into knowledge repo"
git push
```

After this, stop treating Personal and Admin as separate agent remotes.

## 4. Point the tools at YoavAI

- **Claude Code:** open `YoavAI/` (it reads `CLAUDE.md`).
- **Cursor Desktop:** File → Open Folder → `YoavAI/`. For site work, open
  `yoavshlomov-website` (or a multi-root workspace with both).
- **Cursor Cloud:** use the website env for subject 1; add a second env (or
  multi-repo env with **only** these two) once `yoav-knowledge` is connected.

## 5. Daily habit

| Change | Action |
|--------|--------|
| Memory / life notes | Edit under `YoavAI/`, commit + push when you want Cloud to see it |
| Website | Commit in `yoavshlomov-website` only |
| New routine idea | Edit `routines/MASTER.md` — do not spawn a second Automation |

## 6. Verify

- [ ] Only two GitHub remotes matter for agents: website + knowledge
- [ ] `MEMORY.md` opens from both Claude and Cursor Desktop without copying
- [ ] Cloud agent on knowledge can `ls` `personal/` and `admin/` after push
- [ ] Nothing from `YoavAI/` was committed to the public website repo

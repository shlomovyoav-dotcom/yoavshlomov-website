# VERIFICATION — answers derived purely from this repository

Scope note: these answers use ONLY what exists in this git repository — all
branches (`main`, `cursor/blocker-hardening-388b`,
`cursor/add-gmail-mcp-9fad`, `cursor/setup-cloud-dev-environment-dc92`),
their files, and commit history. **`KNOWLEDGE.md` does not exist anywhere in
this repository**, so anything only that file could confirm is marked "not
derivable from the repo".

---

## 1. The three active projects and their states

The repo evidences three active projects:

1. **The public brand site — yoavshlomov.com.** Pure HTML/CSS, deployed by
   Cloudflare Pages from `main`. Live with the PARDES illustrated world
   (hero animation, Geshem section banners, press kit / EPK, FormSubmit
   contact form). The Shop section was removed from the live site and parked
   in `_preview/shop-section.html` "for later" (commit `5f0228b`); PARDES
   merch production is staged and waiting on Yoav to log in to Printful and
   order cap samples (`docs/PRINTFUL-RUNBOOK.md`: "You only log in and pay
   for samples").

2. **The "Yoav Protection" blocker system (`dns/`).** Self-binding content
   blocks (porn, deepfake/nudify, food delivery, Instagram/Facebook, news)
   across iPhone, Mac, and router. Actively developed on the unmerged branch
   `cursor/blocker-hardening-388b`, which adds `dns/domains.txt` (single
   source of truth), `dns/generate_blocklist.py`, regenerated artifacts, a
   Pages Function that actually blocks `/dns/` and `/docs/` from being
   served, `AGENTS.md`, and App Store-verified app blocks (29 apps,
   2026-08-07). `main` still has the older hand-made profiles only. State:
   working but with an open improvement roadmap (see answer 5).

3. **The private reference hub — `/l/k7Qm2xR9/`.** Live and unlisted
   (noindex headers, excluded from sitemap, 404 for anyone without the exact
   link). Contains three signed QA letters (Yuval Bazilevich and Vili Medina
   of Artlist, Nir Sobol of Waves Audio) plus letterhead versions,
   music/teaching letters (Reggie Workman, Billy Harper, Dan Hendelsman,
   Nadav Rubinstein), and a film-scoring showreel link (commit `4e0fa79`).

Also present but NOT active per the repo: a **Hoopoe** website engagement is
evidenced only by removal traces — commits hosting then removing a "Hoopoe
redesign preview" (`6cf9e26` → `d18dc6b`, `1c7973e`, `1473dd3`) and `/hoopoe/*`
404 rules still in `_redirects`. The engagement's current state (agreement,
commission) is not derivable from the repo.

## 2. The four-layer content-blocking architecture + the allowlist correction

From the system map in `dns/README.md` (branch `cursor/blocker-hardening-388b`):

| Layer | Mechanism | Unlock held by |
|---|---|---|
| **iPhone** | Supervised via Apple Configurator + `full-blocklist.mobileconfig`: web content filter, locked Cloudflare Family DoH, no erase, no user profile installs, no VPN, blocked apps | Father (Screen Time passcode; supervision identity on USB in safe) |
| **Mac** | `hosts-blocklist.txt` in `/etc/hosts` + father-held Admin account (Yoav = Standard) + Screen Time passcode | Father (admin password, Screen Time passcode) |
| **Router** | DNS filtering (NextDNS recommended: denylist import, category blocks, block-bypass-methods, newly-registered-domains) | Father (router admin + NextDNS account) |
| **Cloud** | This repo's `dns/` folder = source of truth (`domains.txt`) + generator producing the three artifacts | — |

**The allowlist correction:** commit `c326d74` ("dns: unblock Cibus/Pluxee
(employer meal benefit, needed for new job)", 2026-08-07) — the two services
that must be UNBLOCKED are **Cibus** and **Pluxee**. Concretely the commit
removed three domain entries from `domains.txt` and all generated artifacts:
`pluxee.co.il`, `cibus.pluxee.co.il`, and `consumers.pluxee.co.il`, replacing
them with the comment "Cibus/Pluxee deliberately NOT blocked (2026-08-07,
per Yoav): employer meal benefit — needed when starting a new job." (The
question says "two domains"; the repo shows two services / one registrable
domain plus two subdomains — three entries total.)

## 3. The standing global rules

From `AGENTS.md` (exists only on `cursor/blocker-hardening-388b`, not on
`main`) — the "Privacy rules (non-negotiable)" plus workflow rules:

1. **Never commit personal documents** — letters, IDs, passwords, anything
   from the `Personal`/`Admin` folders on Yoav's Mac. Those belong in
   separate private repos, never in this public one.
2. **`dns/` and `docs/` are never served** — blocked from the live site. Any
   new private folder/file must get matching 404 rules **in the same
   commit**.
3. **Never write real passwords or unlock codes** into the repo or into
   chat. Per the password protocol in `dns/README.md`: the father creates
   every password himself, privately, on paper, into a physical safe —
   passwords generated in a chat are visible to Yoav and therefore useless
   as locks.
4. **Semi-private content pattern:** unlisted-but-served content lives under
   `/l/<token>/` with noindex headers.
5. **Blocklist workflow:** `dns/domains.txt` is the single source of truth;
   never hand-edit the generated artifacts (`full-blocklist.mobileconfig`,
   `hosts-blocklist.txt`, `nextdns-denylist.txt`); additions get dated
   comment headers for review.
6. **Site conventions:** no frameworks, no dependencies, no build step;
   hidden-from-live content parks in `_preview/`; mind `_headers` /
   `_redirects` when adding or removing pages.

## 4. The erase-proofing design after 2026-08-08

**Not derivable from the repo — and the premise contradicts what the repo
says.** The question describes a design where "Yoav keeps full admin; the
router is the backstop that makes erasing devices pointless." No document in
this repository describes that design, and no repo content is dated after
2026-08-07.

What the repo (dns/README.md, "What erase-blocking really covers — honest
limits") actually documents is the opposite arrangement:

- The **father** holds every unlock: Mac admin (Yoav's account is demoted to
  Standard), Screen Time passcodes, router admin, NextDNS account, the
  supervision identity USB, and optionally the Apple ID password — all on
  paper in a physical safe.
- On the supervised iPhone, "Erase All Content and Settings" is removed and
  resets are gated by the father's Screen Time passcode; DFU/recovery
  restore cannot be blocked, so **Activation Lock (Find My)** is documented
  as "the real anti-wipe" backstop, with MDM Recovery Lock as the strongest
  option for the Mac.
- The **router is explicitly described as "defense-in-depth"**, not as the
  primary backstop: "The iPhone/Mac DoH profiles already override any
  network's DNS, so the router layer is defense-in-depth plus protection for
  other devices at home."

If a post-2026-08-08 redesign exists (Yoav keeping full admin, router as
backstop), it lives outside this repository and should be added to
`dns/README.md` before it can be treated as the design of record.

## 5. The eight ongoing tasks/promises

The repo does not contain a canonical list titled "eight tasks", so an exact
match to that list cannot be confirmed. The repo does evidence exactly eight
open items:

From the `dns/README.md` improvement roadmap (5 unchecked items):

1. Connect the private `Personal`/`Admin` repos so the Mac-side setup is
   documented and improvable from the cloud agent.
2. Router: fill in the model, apply the NextDNS plan.
3. NextDNS on all three layers (router + Mac + iPhone, replacing plain
   Cloudflare Family) so one denylist rules everything.
4. MDM (Mosyle free tier) for Mac Recovery Lock, and possibly the iPhone so
   profile updates stop requiring a USB cable.
5. Consider Screen Time app-category limits as a softer layer for anything
   new that slips through.

From elsewhere in the repo (3 items):

6. **Printful merch:** execute the staged click-path in
   `docs/PRINTFUL-RUNBOOK.md` — log in, upload the prepared embroidery
   files, and order one sample of each cap ("this is the only payment").
7. **Shop relaunch:** the Shop section was removed from the live site and
   saved to `_preview/shop-section.html` "for later" (commit `5f0228b`) —
   restoring it is an open promise.
8. **Merge the blocker hardening:** `cursor/blocker-hardening-388b` (the
   generator workflow, the Pages Function that actually blocks `/dns/` and
   `/docs/`, `AGENTS.md`, verified app blocks, and the Cibus/Pluxee
   correction) is still unmerged — `main` neither blocks those paths
   effectively nor carries the corrected blocklist.

(One roadmap item is already checked off in the repo: App Store-verified
bundle IDs for social/food-delivery/news apps, 2026-08-07.)

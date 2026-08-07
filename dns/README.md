# Yoav Protection — blocker system runbook

Self-binding content blocks across Yoav's devices: porn, deepfake/nudify tools,
food delivery, Instagram/Facebook, and news. Yoav's father is the accountability
partner: he holds every unlock password in a physical safe. This folder is the
canonical home of the blocklist and the procedures.

These files are in the public website repo but are **never served**: `_redirects`
returns 404 for everything under `/dns/` (and `/docs/`). Keep it that way.
History note: profiles were briefly hosted for the Safari install on 2026-07-21,
then blocked from the site. Installs now go through Apple Configurator only.

## System map

| Layer | Mechanism | Unlock held by |
|---|---|---|
| iPhone | Supervised (Apple Configurator) + `full-blocklist.mobileconfig`: web content filter, locked Cloudflare Family DoH, no erase, no user profile installs, no VPN, blocked apps | Father: Screen Time passcode, supervision identity on USB in safe |
| Mac | `hosts-blocklist.txt` in `/etc/hosts` + father-held Admin account (Yoav = Standard) + Screen Time passcode | Father: admin password, Screen Time passcode |
| Router | DNS filtering (NextDNS recommended, see below) | Father: router admin + NextDNS account |
| Cloud | This repo folder = source of truth + generator | — |

The Mac's detailed setup history lives in the local `Personal`/`Admin` repos on
the Mac (not in this public repo). Connect them to a private GitHub repo so the
cloud agent can read them — never merge them into this website repo.

## Files

| File | What it is |
|---|---|
| `domains.txt` | **Single source of truth.** Categorized, commented domain list |
| `generate_blocklist.py` | Generates the three artifacts below from `domains.txt` |
| `full-blocklist.mobileconfig` | iPhone profile (generated — don't hand-edit) |
| `hosts-blocklist.txt` | Mac `/etc/hosts` block (generated) |
| `nextdns-denylist.txt` | Bare domains for the NextDNS denylist (generated) |
| `adult-filter.mobileconfig` | Separate porn-only profile for her Mac (legacy, hand-made) |
| `family-safe-browsing.mobileconfig` | Temporary family profile (legacy, hand-made) |

## Updating the blocklist

1. Edit `domains.txt` (bare domains; `www.` + `http/https` variants are added
   automatically for registrable domains).
2. Run `python3 generate_blocklist.py` and commit everything.
3. Re-apply per device: iPhone → Configurator (below); Mac → father pastes
   `hosts-blocklist.txt` into `/etc/hosts` and flushes DNS; NextDNS → paste new
   entries into the denylist.

## iPhone: reinstall with Apple Configurator (supervised)

The restrictions payload (no erase, no VPN, no profile installs, blocked apps)
only works on a **supervised** device, so the phone must be prepared with
Apple Configurator like last time. This erases the phone once — plan it.

1. Make a fresh encrypted Finder backup of the iPhone on the Mac.
2. Temporarily turn **off** Find My iPhone (required for Prepare).
3. Apple Configurator → Prepare → Manual enrollment → no MDM server →
   **Supervise devices ON** → allow pairing with this Mac.
4. **Back up the supervision identity**: Configurator → Settings →
   Organizations → export. Put the file on a USB stick that goes into the
   father's safe. Without it, every future profile change needs another erase.
5. After the erase, set the phone up and restore the backup.
6. In Configurator: device → Add → Profiles → `full-blocklist.mobileconfig`.
   It installs as non-removable; on-device profile installs are blocked from
   then on, but Configurator (this Mac) can always update it.
7. Turn Find My iPhone back **on** (Activation Lock — the real anti-wipe).
8. Father sets the Screen Time passcode on the phone (Settings → Screen Time)
   with: Content & Privacy → Deleting Apps: Don't Allow; Passcode Changes and
   Account Changes: Don't Allow. He writes the passcode on paper → safe.
9. Run the test matrix below before handing the phone back.

## Mac hardening (father does this in one sitting)

1. Father creates a new Admin account with a password he types privately, then
   demotes Yoav's account to **Standard** (System Settings → Users & Groups).
2. FileVault ON. Find My Mac ON (Activation Lock).
3. Father appends `hosts-blocklist.txt` to `/etc/hosts`, then:
   `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`.
4. Father sets a Screen Time passcode for Yoav's macOS account.
5. Strongest (optional): enroll the Mac in an MDM (e.g. Mosyle free tier) and
   set a **Recovery Lock** password — the only way to block recovery-mode
   erase on Apple Silicon.

## What erase-blocking really covers — honest limits

- **iPhone (supervised + this profile):** "Erase All Content and Settings" is
  removed, resets are gated by the father's Screen Time passcode, the profile
  cannot be removed on-device, VPNs and new profiles cannot be added, and the
  DNS setting cannot be toggled off.
- **Cannot be blocked:** a DFU/recovery restore from any computer. Mitigation:
  Activation Lock — a wiped device demands the Apple ID password before it
  works again. Strongest option: the father changes the Apple ID password and
  stores it (plus an Account Recovery Key) in the safe. Trade-off: occasional
  Apple ID prompts will need him.
- **Mac without MDM:** erasing from inside macOS needs the father's admin
  password; recovery-mode erase stays technically possible, but Activation
  Lock makes the wiped Mac useless without the Apple ID password. MDM
  Recovery Lock closes the gap completely.

## Router

Fill in the model when known. Plan that works on nearly all routers:

1. Create a NextDNS profile (father owns the account). Import
   `nextdns-denylist.txt` into the Denylist.
2. Parental Control: block the Porn category, **Block Bypass Methods**
   (proxies/VPN/Tor), enforce SafeSearch, enforce YouTube Restricted Mode.
   Security: enable "Block Newly Registered Domains" — this is what catches
   brand-new nudify/deepfake sites before any list knows them.
3. Put the NextDNS resolver in the router's WAN/DHCP DNS settings.
4. Firewall rules if the router supports them: block outbound TCP/UDP 53 and
   853 from LAN except the router itself (stops hard-coded DNS bypass).
5. Father changes the router admin password → paper → safe.

The iPhone/Mac DoH profiles already override any network's DNS, so the router
layer is defense-in-depth plus protection for other devices at home.

## Password protocol — important correction

A password generated in a chat with the agent is visible to Yoav in that same
chat, which makes it useless as a lock. The father must create every password
himself, on the device, with nobody watching, write it on paper and put it in
the safe. Passwords in the safe: iPhone Screen Time passcode, Mac Screen Time
passcode, Mac admin password, router admin password, NextDNS account,
supervision identity USB, and (optional, strongest) the Apple ID password +
Account Recovery Key. Never store any of these in this repo, in chat, in
iCloud Notes, or in a password manager Yoav can open.

## Test matrix (run after every change)

| Check | Expected |
|---|---|
| `pornhub.com`, `www.pornhub.com`, `http://` variant in Safari | blocked |
| `clothoff.io` / any nudify domain | blocked |
| Random porn site NOT in the list | blocked by AutoFilter/DNS |
| `wolt.com` in Safari + Wolt app feed | blocked / app can't load |
| Instagram app icon | app itself blocked (supervised) |
| `instagram.com`, `www.instagram.com` | blocked |
| `ynet.co.il`, `news.google.com`, `reddit.com` | blocked |
| `croxyproxy.com` or another proxy | blocked |
| Settings → General → Transfer or Reset | Erase option absent/gated |
| Settings → VPN → Add VPN Configuration | not possible |
| Settings → Profile | shows non-removable |
| Toggle DNS setting off | not possible |

## Improvement roadmap

- [ ] Connect the private `Personal`/`Admin` repos so the Mac-side setup is
      documented and improvable here.
- [ ] Router: fill in model, apply the NextDNS plan.
- [ ] NextDNS on all three layers (router + Mac profile + iPhone profile
      replacing plain Cloudflare Family) so one denylist rules everything and
      newly-registered-domain blocking applies everywhere.
- [ ] MDM (Mosyle free) for Mac Recovery Lock, and possibly for the iPhone so
      profile updates stop requiring a USB cable.
- [ ] Add remaining app bundle IDs (10bis, Mishloha, McDonald's IL…) to
      `BLOCKED_APP_BUNDLE_IDS` — read them from Configurator → device → Apps.
- [ ] Consider Screen Time app-category limits as a softer layer for anything
      new that slips through.

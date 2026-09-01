#!/usr/bin/env python3
"""Generate all blocklist artifacts from domains.txt (the single source of truth).

Outputs (written next to this script):
  full-blocklist.mobileconfig  iPhone profile: web content filter + locked family
                               DNS-over-HTTPS + supervised restrictions (no erase,
                               no user profile installs, no VPN, blocked apps).
  hosts-blocklist.txt          /etc/hosts block for the Mac (0.0.0.0 entries).
                               Append below the standard localhost lines.
  nextdns-denylist.txt         Bare-domain list for the NextDNS denylist
                               (NextDNS blocks all subdomains automatically).

Usage:  python3 generate_blocklist.py

Every registrable domain (example.com / example.co.il) is expanded to include
its www. variant and both https:// + http:// URL forms in the mobileconfig.
Subdomain entries (api.wolt.com) are emitted as-is. Stdlib only, deterministic.
"""

import plistlib
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Existing identifiers are preserved so the new profile upgrades the installed
# one in place instead of installing next to it.
PROFILE_UUID = "1639FFE0-558C-47E0-95F6-8E8B71E2281A"
FILTER_UUID = "E14DCBD3-92A3-4722-9DD7-26C010CDF030"
DNS_UUID = "97F3A4A7-782E-4548-A749-B942FE136957"
RESTRICTIONS_UUID = str(
    uuid.uuid5(uuid.NAMESPACE_DNS, "com.yoav.fullblock.restrictions")
).upper()

# App Store apps blocked outright on the supervised iPhone (even if installed).
# All IDs verified against the iTunes Search API (IL storefront) on 2026-08-07.
# Deliberately NOT blocked: WhatsApp (communication), Gett/Via (transportation).
BLOCKED_APP_BUNDLE_IDS = [
    # Social
    "com.burbn.instagram",            # Instagram
    "com.burbn.barcelona",            # Threads
    "com.facebook.Facebook",          # Facebook
    "com.facebook.Messenger",         # Messenger
    "com.atebits.Tweetie2",           # X / Twitter
    "com.reddit.Reddit",              # Reddit
    # Food delivery / fast food
    "com.woltapp.wolt",               # Wolt
    "tenbis",                         # 10bis (תן ביס)
    "mishloha.MishlohaApp",           # Mishloha (משלוחה)
    "com.ubercab.UberEats",           # Uber Eats
    "doordash.DoorDashConsumer",      # DoorDash
    "com.inmanage.iMcdonalds",        # McDonald's Israel
    "il.co.dominos.iDominos",         # Domino's Pizza IL
    "com.applaces.burgerkingisrael",  # Burger King Israel
    "app.tabit.il-prd-wl-kfcn",       # KFC Israel (Tabit)
    "il.co.iPlanet.PizzaHutApp",      # Pizza Hut IL
    # News
    "com.apple.news",                 # Apple News (system app)
    "com.ynet-internet.ynet",         # ynet
    "com.yit.ynetnews",               # ynet Global
    "com.gillyApps.Channel2",         # N12 news
    "com.keshet.mako",                # Mako
    "com.keshet.makoVODiphone",       # 12+ (Keshet live/VOD)
    "il.co.mintmark.walla.walla",     # Walla
    "com.haaretz.hebrew.iphone",      # Haaretz (Hebrew)
    "com.haaretz.english.iphone",     # Haaretz (English)
    "com.haaretz.TheMarker",          # TheMarker
    "com.applicaster.il.ch1",         # Kan
    "com.yourcompany.iReshet",        # Reshet 13+
]

# TLDs where the registrable domain has three labels (example.co.il).
MULTI_LABEL_SUFFIXES = {
    "co.il", "org.il", "net.il", "ac.il", "gov.il", "muni.il", "k12.il",
    "co.uk", "org.uk", "ac.uk",
}


def is_registrable(domain: str) -> bool:
    parts = domain.split(".")
    if len(parts) == 2:
        return True
    return len(parts) == 3 and ".".join(parts[1:]) in MULTI_LABEL_SUFFIXES


def read_domains() -> list[str]:
    domains, seen = [], set()
    for raw in (HERE / "domains.txt").read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line not in seen:
            seen.add(line)
            domains.append(line)
    return domains


def expand_hosts(domains: list[str]) -> list[str]:
    """Each registrable domain also gets its www. variant."""
    hosts, seen = [], set()
    for d in domains:
        variants = [d]
        if is_registrable(d) and not d.startswith("www."):
            variants.append("www." + d)
        for h in variants:
            if h not in seen:
                seen.add(h)
                hosts.append(h)
    return hosts


def build_mobileconfig(hosts: list[str]) -> bytes:
    urls = [f"https://{h}" for h in hosts] + [f"http://{h}" for h in hosts]

    content_filter = {
        "AutoFilterEnabled": True,  # Apple's built-in adult-content heuristic
        "BlacklistedURLs": urls,
        "FilterType": "BuiltIn",
        "PayloadDisplayName": "Content Filter",
        "PayloadIdentifier": f"com.yoav.fullblock.filter.{FILTER_UUID}",
        "PayloadOrganization": "Yoav Protection",
        "PayloadType": "com.apple.webcontent-filter",
        "PayloadUUID": FILTER_UUID,
        "PayloadVersion": 1,
    }

    dns_settings = {
        "DNSSettings": {
            "DNSProtocol": "HTTPS",
            "ServerAddresses": ["1.1.1.3", "1.0.0.3"],
            "ServerURL": "https://family.cloudflare-dns.com/dns-query",
        },
        # Supervised devices: the user cannot toggle this DNS setting off.
        "ProhibitDisablement": True,
        "PayloadDisplayName": "Family DNS",
        "PayloadIdentifier": f"com.yoav.fullblock.dns.{DNS_UUID}",
        "PayloadOrganization": "Yoav Protection",
        "PayloadType": "com.apple.dnsSettings.managed",
        "PayloadUUID": DNS_UUID,
        "PayloadVersion": 1,
    }

    # All keys below require a supervised device (Apple Configurator).
    # On an unsupervised device they are ignored.
    restrictions = {
        "allowEraseContentAndSettings": False,   # no Erase All Content and Settings
        "allowUIConfigurationProfileInstallation": False,  # no manual profile installs/removals
        "allowVPNCreation": False,               # no VPN configs (filter bypass)
        "blockedAppBundleIDs": BLOCKED_APP_BUNDLE_IDS,
        "PayloadDisplayName": "Restrictions",
        "PayloadIdentifier": f"com.yoav.fullblock.restrictions.{RESTRICTIONS_UUID}",
        "PayloadOrganization": "Yoav Protection",
        "PayloadType": "com.apple.applicationaccess",
        "PayloadUUID": RESTRICTIONS_UUID,
        "PayloadVersion": 1,
    }

    profile = {
        "PayloadContent": [content_filter, dns_settings, restrictions],
        "PayloadDescription": (
            "Blocks adult content, deepfake/nudify tools, news sites, social media "
            "and food-delivery apps/sites. Locks family DNS, blocks VPNs, manual "
            "profile installs and device erase (supervised device required for "
            "restrictions). Install via Apple Configurator."
        ),
        "PayloadDisplayName": "Full Content Block",
        "PayloadIdentifier": f"com.yoav.fullblock.{PROFILE_UUID}",
        "PayloadOrganization": "Yoav Protection",
        "PayloadRemovalDisallowed": True,
        "PayloadType": "Configuration",
        "PayloadUUID": PROFILE_UUID,
        "PayloadVersion": 2,
    }
    return plistlib.dumps(profile, sort_keys=True)


def build_hosts_file(hosts: list[str]) -> str:
    lines = [
        "# Yoav Protection blocklist for /etc/hosts (generated by generate_blocklist.py)",
        "# Append below the standard localhost entries, then run:",
        "#   sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder",
        "",
    ]
    lines += [f"0.0.0.0 {h}" for h in hosts]
    return "\n".join(lines) + "\n"


def build_nextdns_list(domains: list[str]) -> str:
    """NextDNS denylist entries block all subdomains, so collapse a subdomain
    to its registrable root only when that root is itself blocked."""
    roots = {d for d in domains if is_registrable(d)}

    def collapse(d: str) -> str:
        parts = d.split(".")
        for i in range(len(parts) - 1):
            cand = ".".join(parts[i:])
            if cand in roots:
                return cand
        return d

    out, seen = [], set()
    for d in domains:
        c = collapse(d.removeprefix("www."))
        if c not in seen:
            seen.add(c)
            out.append(c)
    return "\n".join(out) + "\n"


def main() -> None:
    domains = read_domains()
    hosts = expand_hosts(domains)

    (HERE / "full-blocklist.mobileconfig").write_bytes(build_mobileconfig(hosts))
    (HERE / "hosts-blocklist.txt").write_text(build_hosts_file(hosts))
    (HERE / "nextdns-denylist.txt").write_text(build_nextdns_list(domains))

    print(f"domains.txt entries : {len(domains)}")
    print(f"hosts after www expansion : {len(hosts)}")
    print(f"mobileconfig URL entries  : {len(hosts) * 2}")


if __name__ == "__main__":
    main()

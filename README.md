# yoavshlomov.com

Static website for Yoav Shlomov — jazz guitarist & producer.  
Replaces the Wix site at yoavhakohav.com. Free hosting via Cloudflare Pages.

## Stack

Pure HTML + CSS. No build step, no dependencies, no framework.

## Deploy to Cloudflare Pages (free)

1. Push this folder to a GitHub repo (e.g. `github.com/yoavshlomov/website`)
2. Go to [Cloudflare Pages](https://pages.cloudflare.com) → Create project → Connect to Git
3. Select the repo → **no build command needed** → root directory = `/` → Save
4. Cloudflare assigns a free `*.pages.dev` subdomain automatically

### Connect yoavshlomov.com

If you own `yoavshlomov.com` (or want to buy it):
- Buy domain at [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) (~$10/yr, no markup)
- In Cloudflare Pages → Custom Domains → add `yoavshlomov.com`
- DNS is configured automatically if the domain is on Cloudflare

### Contact form

The form uses [FormSubmit.co](https://formsubmit.co) — zero setup, completely free.  
First submission triggers a confirmation email to `shlomovyoav@gmail.com`.  
After confirming, all messages land directly in your inbox.

## What to update

| Item | Where |
|------|--------|
| Hero animation | `images/hero-anim.{mp4,webm}` + `images/hero-anim-poster.jpg`. Bump the `?v=` on the `<source>` tags in `index.html` when the video changes (the files are served with a one-year immutable cache). |
| New music | The "New music" block embeds the Spotify artist page and updates itself. Add/remove album iframes in the "Selected releases" grid and the discography lists in `index.html`, `press.html` and `press/yoav-shlomov-bio.txt`. |
| Bio / press quotes | Same text appears in `index.html` (Bio + Press Kit), `press.html` and `press/yoav-shlomov-bio.txt` — keep them in sync. |
| Photos | `images/yoav-portrait.jpg`, `images/yoav-live-bw.jpg` (offered as downloads, keep high-res), `images/yoav-bio.jpg` (display only, 1200px wide). |
| Palette | CSS variables at the top of `style.css`. `--accent` is for fills, `--accent-text` for orange running text on cream (both pass WCAG AA). |

## URLs

Cloudflare Pages serves clean URLs: `press.html` is reachable as `/press` (and `/press.html` redirects there), so internal links, the canonical tag and the sitemap use `/press`.

## Files

```
index.html     — full single-page site
style.css      — all styles, responsive
press.html     — printable EPK one-sheet (/press)
press/         — plain-text bio for download
404.html       — branded not-found page (Cloudflare serves it for misses)
_headers       — Cloudflare security + cache headers
_redirects     — retired paths that should 404
robots.txt, sitemap.xml
l/             — unlisted, noindex reference pages (shared by direct link only)
```

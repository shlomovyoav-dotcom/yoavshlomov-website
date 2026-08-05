# yoavshlomov.com

Static website for Yoav Shlomov — jazz guitarist & producer.  
Replaces the Wix site at yoavhakohav.com. Free hosting via Cloudflare Pages.

## Stack

Pure HTML + CSS. No build step, no framework. The site deploys to Cloudflare Pages
with no build command.

## Local development

The only dev dependency is [Wrangler](https://developers.cloudflare.com/workers/wrangler/),
used to preview the site exactly as Cloudflare Pages serves it (including `_headers`,
`_redirects` and the custom `404.html`).

```bash
npm ci          # install Wrangler (dev-only; production still needs no build)
npm run dev     # serve at http://127.0.0.1:8788
```

`npm run start` is the same server bound to `0.0.0.0` for remote/dev environments.

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
| Hero illustration | Replace the `<img src>` in `index.html` with a locally hosted image |
| Concerts | Edit the `.concert-item` blocks in `index.html` |
| New releases | Add/remove Spotify embed iframes in the music grid |
| Press photo | Update the download link in the Press section |

## Files

```
index.html   — full single-page site
style.css    — all styles, responsive
_headers     — Cloudflare security headers
```

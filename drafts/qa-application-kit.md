# QA application kit — reusable cover letter + talking points

> **DRAFT ONLY.** Nothing here has been sent. Yoav reviews, tailors, and
> sends every application himself.
>
> **Sources.** Items marked **[REPO]** are backed by this repository (the
> recommendation letters and reference pages under `/l/k7Qm2xR9/`). Items
> marked **[BRIEF]** come from Yoav's task brief and are not verifiable
> from the repo (`KNOWLEDGE.md` is not present in the repo) — confirm they
> are accurate before using them in an application.

---

## Fact base (what we can safely claim)

**[REPO] — backed by signed recommendation letters on the private hub:**

- QA at **Artlist**, owning the most business-critical areas: subscription,
  billing, and upgrade funnels (letter from Yuval Bazilevich, Growth Team
  Lead, Artlist, signed via Adobe Sign, Jun 2026).
- Maintained, extended, and improved **Playwright + CI end-to-end test
  infrastructure** across visitor/guest, free-trial, and upgrade user
  states (same letter).
- Built **automated test-account generation** to reproduce
  subscription-specific scenarios on demand (same letter).
- Developed a **pricing-verification tool** that checked subscription
  pricing against expected values and caught billing misconfigurations
  before production (same letter).
- R&D Growth QA, test automation, and **AI-assisted tooling adoption**
  (letter from Vili Medina, Head of R&D, Growth, Artlist, signed Jul 2026).
- Growth, billing funnels, Playwright automation, AI tooling, **Mixpanel
  alerts** (QA references page summary).
- Earlier background: **technical support at Waves Audio** — pro-audio
  software & hardware, global English-language customers (letter from Nir
  Sobol, Technical Support Manager, Waves Audio, 2023).
- Three signed QA letters on file, shareable via a private link
  (https://yoavshlomov.com/l/k7Qm2xR9/qa/ — unlisted, noindex).

**[BRIEF] — from Yoav's task brief; confirm before using:**

- Working stack: **Playwright / Next.js / Nx / pnpm / tRPC / Jest / k6 /
  Chargebee / Zephyr**. (Of these, only Playwright and the billing-funnel
  domain are independently repo-backed.)
- **Active interview process: QA Ops Manager at SuperPlay.** Never mention
  this in applications to other companies; it's listed here only so the
  kit's positioning (QA leadership / ops direction) matches reality.

## Cover letter skeleton (fill per role)

> Replace every `[BRACKET]`. Keep it under one page. Reorder the two middle
> paragraphs depending on whether the role is hands-on automation or
> process/ops leadership.

Dear `[HIRING MANAGER / TEAM]`,

I'm applying for the `[ROLE]` position at `[COMPANY]`. I'm a QA engineer
with experience owning quality for business-critical, revenue-facing flows
— most recently at Artlist, where I was responsible for the subscription,
billing, and upgrade funnels.

**[Automation paragraph — lead with this for hands-on roles]**
At Artlist I maintained and extended our Playwright and CI end-to-end
test infrastructure across the user states my team owned (visitor, free
trial, upgrade). I built automated test-account generation so
subscription-specific scenarios could be reproduced on demand, and a
pricing-verification tool that caught billing misconfigurations before
they reached production. `[Add one sentence mapping this to COMPANY's
product: e.g. "Your checkout/subscription surface is exactly the kind of
flow I've specialized in protecting."]`

**[Process/tooling paragraph — lead with this for ops/leadership roles]**
Beyond writing tests, I care about the system around them: CI reliability,
test data management, monitoring hooks (Mixpanel alerts), and adopting
AI-assisted tooling where it actually saves the team time. My managers'
reference letters speak to initiative on exactly this — building the
infrastructure other people's tests run on. `[If relevant: mention test
management/process experience matching the role's requirements.]`

My working stack includes `[PICK FROM: Playwright, Jest, k6, Next.js, Nx,
pnpm, tRPC, Chargebee, Zephyr — choose only what matches the job posting
and what you can defend in an interview]`. Earlier, I spent `[X years —
VERIFY]` in technical support at Waves Audio working with a global,
English-speaking customer base — which is where I learned to debug under
pressure and communicate clearly with non-engineers.

Signed recommendation letters from my managers at Artlist and Waves are
available at a private link I'd be glad to share.

I'd welcome a conversation about how I can help `[COMPANY]`
`[ONE CONCRETE GOAL FROM THE JOB POSTING]`.

Best regards,
Yoav Shlomov
shlomovyoav@gmail.com

## Talking points per theme (pick 2–3 per application)

**Revenue-critical QA:**
- Owned QA for subscription/billing/upgrade funnels — the flows where bugs
  cost money directly. [REPO]
- Pricing-verification tool caught billing misconfigurations pre-production. [REPO]

**Automation & infrastructure:**
- Playwright + CI e2e infrastructure: maintained, extended, improved — not
  just consumed. [REPO]
- Automated test-account generation: reproduce any subscription state on
  demand. [REPO]
- Load/performance angle: k6. [BRIEF — verify depth before claiming]

**Modern stack fluency:**
- Monorepo tooling (Nx, pnpm), typed APIs (tRPC), Next.js apps, Jest unit
  testing. [BRIEF — verify depth before claiming]
- Billing platform: Chargebee. Test management: Zephyr. [BRIEF]

**Tooling & signal:**
- Mixpanel alerts for product/quality signals. [REPO]
- Early, practical adopter of AI-assisted QA tooling. [REPO]

**Communication & support DNA:**
- Waves Audio technical support: global English-language customers,
  pro-audio domain. [REPO]
- Second career as a performing musician/producer — comfortable presenting,
  performing under pressure, and shipping creative work. [REPO — public site]

## Tailoring checklist (per application)

- [ ] Swap in the company's product and one concrete goal from the posting
- [ ] Choose stack items honestly — only what matches the posting AND can be
      defended in interview depth
- [ ] Decide lead paragraph: automation-first or ops/process-first
- [ ] Update `[X years]` figures — **not derivable from this repo, VERIFY**
- [ ] Attach or offer the private reference link (never post it publicly)
- [ ] Remove/never mention other active processes (e.g. SuperPlay)

# Raj / Hoopoe Electric — engagement recap, open items, and draft email

> **DRAFT ONLY.** Nothing in this file has been sent. Yoav reviews, edits, and
> sends everything himself.
>
> **Sources.** Facts about Raj, the agreement, and the commission terms come
> from Yoav's task brief (they are NOT verifiable from this repository —
> `KNOWLEDGE.md` is not present in the repo). The only Hoopoe traces in this
> repo are git commits showing a Hoopoe redesign preview was hosted on
> yoavshlomov.com and later removed, plus `/hoopoe/*` 404 rules in
> `_redirects`. Items marked **[VERIFY]** are assumptions to confirm before
> sending anything.

---

## (a) Status recap — where the engagement stands

Context provided by Yoav (task brief):

- **Client:** Balraj ("Raj") Kapoor, director of Hoopoe Electric Ltd — a
  London private-hire / minicab company. Contact: hoopoe.electric@gmail.com.
- **Work done:** Yoav rebuilt hoopoe-electric.com and maintains it; he also
  runs its SEO, analytics, and the prepaid booking flow.
- **Commercials:** there is an **UNSIGNED** draft — "Booking & Website
  Partner Agreement (DRAFT v3)", last edited 2026-07-26 — under which Yoav
  would earn **15% commission per online booking, auto-paid via Revolut**.
- **Repo evidence:** a Hoopoe redesign preview was temporarily hosted on
  Yoav's personal site and then deliberately removed (commits: "Host Hoopoe
  redesign preview", "Remove Hoopoe redesign preview from personal site",
  "Force-remove cached /hoopoe preview from Cloudflare", "Drop /hoopoe stub").
  This is consistent with the rebuild having moved to the client's own
  domain.

**Bottom line:** the site work is delivered and in maintenance mode, but the
relationship is commercially unprotected — the agreement that pays Yoav per
booking is still unsigned, and the exact remaining scope is undefined.

## (b) Checklist — deliverables likely still open

All items are **[VERIFY]** — inferred from the engagement description, not
from a signed scope document.

- [ ] **Agreement:** get "Booking & Website Partner Agreement (DRAFT v3)"
      reviewed, finalized, and signed by both parties.
- [ ] **Commission plumbing:** confirm the 15%-per-online-booking tracking is
      measurable and auditable end-to-end (what counts as an "online
      booking", where it's logged, how disputes are resolved), and that the
      Revolut auto-payment is actually set up and tested.
- [ ] **SEO:** baseline audit documented (rankings, indexed pages, Search
      Console health), local SEO (Google Business Profile) claimed and
      optimized, ongoing keyword/content plan agreed.
- [ ] **Analytics wiring:** confirm analytics is installed on all pages,
      conversion events fire for completed bookings, and Raj has (or should
      have) view access; define a simple monthly report format.
- [ ] **Prepaid booking flow:** end-to-end test of the prepaid flow
      (payment success, failure, refund path), and confirmation emails /
      notifications working.
- [ ] **Handover docs:** hosting/DNS/domain access inventory, CMS or repo
      access, credentials custody, "what to do if the site goes down"
      runbook, and who owns which account.
- [ ] **Maintenance terms:** what "maintains" includes (uptime monitoring,
      content edits, security updates) and what is out of scope / billable
      separately.
- [ ] **Backups & continuity:** confirm site backups exist and Raj's company
      retains access to its own assets if the engagement ever ends.

## (c) Draft email to Raj (English)

> **DRAFT — not sent. For Yoav to review, edit, and send himself.**

**To:** hoopoe.electric@gmail.com
**Subject:** Hoopoe Electric website — next steps + agreement sign-off

Hi Raj,

I hope business is going well. I wanted to give you a quick status update on
the website and propose how we wrap up the remaining pieces.

Where things stand:

- The rebuilt site is live and I'm maintaining it on an ongoing basis.
- SEO and analytics are running; I'll keep tuning them, and I'd like to
  agree on a simple monthly report so you always see what's happening.
- The prepaid booking flow is in place; I want to run one more full
  end-to-end test with you (payment, confirmation, refund path) so we're
  both confident in it.

Two things I need from you to finish this properly:

1. **The agreement.** The "Booking & Website Partner Agreement" (draft v3,
   from late July) is still unsigned. It covers the 15% commission per
   online booking, paid automatically via Revolut. Could you review it and
   either sign it or send me your comments? I'm happy to jump on a call to
   walk through it together.
2. **Remaining scope.** I've listed below what I believe is still open —
   please confirm, add, or strike items so we have one agreed list:
   - Final end-to-end test of the prepaid booking flow
   - Booking-commission tracking review (so the numbers are transparent
     for both of us)
   - Local SEO push (Google Business Profile and reviews)
   - Monthly analytics report format
   - Handover documentation (accounts, access, and a simple runbook)

Once you confirm, I'll send a short timeline for each item.

Best regards,
Yoav Shlomov

## (d) Discovery questions to pin down scope

1. What counts as an "online booking" for commission purposes — only fully
   prepaid bookings, or also bookings initiated online and paid in the car?
2. Where is the single source of truth for booking counts (booking system
   dashboard, payment provider, analytics), and can we both see it?
3. Is the Revolut auto-payment set up already, and on what schedule
   (per booking, weekly, monthly)?
4. What does "maintenance" include for you — content changes, adding
   vehicles/services, price updates — and how quickly do you expect
   turnaround?
5. Who owns and holds credentials for the domain, hosting, analytics, and
   booking/payment accounts today? Is there anything only one of us can
   access?
6. Are there compliance requirements for a London private-hire operator
   (e.g. TfL licensing details, terms & conditions, privacy policy) that
   the site must display? **[VERIFY with Raj / TfL requirements]**
7. What are your top 2–3 business goals for the next quarter (more airport
   runs, corporate accounts, etc.) so SEO and content can target them?
8. If either side wants to end the arrangement, what happens to the site,
   the booking flow, and accrued commissions? (This should be answered in
   the agreement — confirm draft v3 covers it.)

# Archive stale cloud chats

Preferred: run `docs/EXECUTE-CONSOLIDATION.sh` with `CURSOR_API_KEY` set
(archives the list below via `POST /v1/agents/{id}/archive`).

Manual fallback: [cursor.com/agents](https://cursor.com/agents).

**Policy:** keep only active subject threads. Archive ERROR one-shots,
finished walkthroughs, and housekeeping from September onward that are not
ongoing work. Already-archived chats are listed for completeness.

Generated: 2026-10-09 from this environment’s agent inventory.

## KEEP (do not archive)

| Name | bcId | Why |
|------|------|-----|
| Unified development environment | `bc-029a1f2c-efa4-4467-99e8-a6baeeafe76a` | This consolidation run |
| Sister's Romanian passport appointment | `bc-01a11187-dbd2-7acd-ab39-3533923d64e6` | Ongoing life/admin |
| On-behalf signing process | `bc-01a110f1-ec54-7ece-98fe-9ebb2aed89c4` | Related to passport/signing |
| Qa portfolio url | `bc-01a1107a-8a84-7498-94f4-9937aa8ea0e0` | Portfolio pointer |
| גישה לאתר הלחנת סרטים | `bc-01a0b0dd-9f60-7e55-bdcf-9ac2c0de4947` | Scoring reel / hub |
| Overall website improvements | `bc-e53d6efc-6909-44d2-8357-55b612ec7fdd` | Main site branch work |

After this PR merges, you may archive this chat too once the Mac bootstrap is done.

## ARCHIVE now (not already archived)

Open each URL → Archive.

### ERROR / failed internals (safe to archive)

- Login econsulat account — `bc-de0e63b6-aa6d-57ef-add1-85019b36be2d`
- Login econsulat account — `bc-d0a0b660-3dbb-5099-9371-2abd3aefe1a3`
- Verify scoring reel UI ×3 — `bc-53ea42b6-…`, `bc-805ed80d-…`, `bc-0b8e965f-…`
- Walk hub three pages — `bc-8ec63804-d748-5518-967b-72a65ecc2d2d`
- Review walkthrough video — `bc-857a7190-4d5a-579d-8972-12f43d079d38`
- Review profile walkthrough video — `bc-65a30f46-d776-5bff-b172-bf2f08453f95`
- Chrome profile inspection — `bc-c2b1bacc-3905-5767-835a-320b54c95727`
- Browse profiles in Chrome — `bc-8e70e56f-a72b-5eb2-9c38-4f8eaa067b92`
- Open Chrome public profiles — `bc-6e7e8863-935e-51dc-be9f-441a6ed8ef64`
- Verify Desktop shows handoff — `bc-2d068d22-5491-5ff5-b152-f4552573b872`
- Screenshot Desktop handoff file — `bc-ec26cefd-f0e4-551d-9baa-192e378be343`

### Finished one-shots / docs / walkthroughs

- מתכון מרק דגים — `bc-01a10ccf-9f17-76cb-866f-3ab746881cc9`
- Unspecified task context (Canditech quiz) — `bc-01a0dd3a-9e39-7536-a733-5bf7c576093b`
- Cursor PR auto-create settings — `bc-4a0b99b0-fef3-5e4d-a812-5b6a32af59f2`
- Review three-pages walkthrough video — `bc-99a8c656-0546-5ac1-8be4-6991ce96393f`
- How to target a self-hosted worker — `bc-a74e5011-3439-5f45-bb38-dbfc9d445469`
- Review hidden-pages walkthrough video — `bc-69887fef-0ebe-5f3d-910c-3b7a928618a7`
- Walk through private hub and letters pages — `bc-bc670e3e-4c2e-53cd-9400-8f551e6d54c1`
- Prepare browser on private hub page — `bc-860b48c6-4d73-5ad0-ba6b-d06b2d63f733`
- Review site walkthrough video — `bc-4fe7358a-b07a-5942-8b86-967bc4641f92`
- Re-check mobile menu and capture bio/newsletter — `bc-f2286e83-cac3-537e-a832-4f611628ebd0`
- Walk through site: nav, anchors, forms, 404 — `bc-999cab36-138d-5356-9056-a51f00f44af2`
- Set up browser for site walkthrough — `bc-bea73827-7583-5077-9aaa-743399f80610`
- Cursor credit reset docs — `bc-3a802108-8618-5014-a9c7-9acc70ba5f69`
- Cursor remote control docs — `bc-cbfe100b-d70b-5dc4-bc0d-1cfed7e2f6da`
- Summarize prior agent handoffs — `bc-ff43b65f-b4c6-50a1-91e9-bb0cc6c2df9a`
- Explore private hub structure — `bc-a3bb1d2a-e3b0-5a43-bbe2-9ecdd0f96fa8`
- Cursor routines/automations docs (subagent) — `bc-84d666ea-05bf-5812-addc-1173af236aa6`
- Find Claude/iCloud/routines docs (subagent) — `bc-49ed7582-a8ac-5819-a938-83fb3ed5baf3`

## Already archived (no action)

Apartment part cover, איפוס קרדיטים, החלטה על קנקן מים, ביטול דו״ח חניה,
שיפור פרופיל X-Player, הנדאוף מעודכן לדסקטופ, Today's chat session,
Instruction clarity needed, App subject organization, Personal data project
context, New development environment.

## Routines

There is no MCP list of Automations. At
[cursor.com/automations](https://cursor.com/automations) and Grok Bot →
Tasks → Routines: pause/delete every routine except the new **MASTER** from
`docs/MASTER-ROUTINE.md`.

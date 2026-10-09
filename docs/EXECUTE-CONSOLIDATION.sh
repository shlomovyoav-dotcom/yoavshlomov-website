#!/usr/bin/env bash
# Run on Mac (or any machine with your credentials) to finish what cloud cannot.
# Usage:
#   export GITHUB_PAT=ghp_...          # repo create + push
#   export CURSOR_API_KEY=...          # archive agents
#   bash docs/EXECUTE-CONSOLIDATION.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCAFFOLD="$ROOT/docs/yoav-knowledge-scaffold"
ICLOUD="${ICLOUD_DIR:-$HOME/Library/Mobile Documents/com~apple~CloudDocs/YoavAI}"
REPO_SLUG="shlomovyoav-dotcom/yoav-knowledge"
API="https://api.cursor.com/v1"

need() { command -v "$1" >/dev/null || { echo "missing: $1"; exit 1; }; }
need git
need curl
need jq

if [[ -z "${GITHUB_PAT:-}" ]]; then
  echo "Set GITHUB_PAT (classic: repo scope, or fine-grained: create repo on shlomovyoav-dotcom)."
  exit 1
fi

echo "==> Ensure private repo $REPO_SLUG exists"
HTTP=$(curl -sS -o /tmp/yk.json -w '%{http_code}' \
  -H "Authorization: Bearer $GITHUB_PAT" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/$REPO_SLUG" || true)
if [[ "$HTTP" == "404" ]]; then
  curl -sS -X POST \
    -H "Authorization: Bearer $GITHUB_PAT" \
    -H "Accept: application/vnd.github+json" \
    "https://api.github.com/user/repos" \
    -d "{\"name\":\"yoav-knowledge\",\"private\":true,\"description\":\"Private AI memory + Personal/Admin (subject 2)\"}" \
    | tee /tmp/yk-create.json | jq -r '.full_name // .message'
  # If user is under org ownership for website, try org create:
  if ! jq -e '.full_name' /tmp/yk-create.json >/dev/null 2>&1; then
    curl -sS -X POST \
      -H "Authorization: Bearer $GITHUB_PAT" \
      -H "Accept: application/vnd.github+json" \
      "https://api.github.com/orgs/shlomovyoav-dotcom/repos" \
      -d "{\"name\":\"yoav-knowledge\",\"private\":true,\"description\":\"Private AI memory + Personal/Admin (subject 2)\"}" \
      | jq -r '.full_name // .message'
  fi
else
  echo "repo exists (HTTP $HTTP)"
fi

WORKDIR=$(mktemp -d)
echo "==> Clone / seed $WORKDIR"
git clone "https://x-access-token:${GITHUB_PAT}@github.com/${REPO_SLUG}.git" "$WORKDIR" || {
  mkdir -p "$WORKDIR" && cd "$WORKDIR" && git init -b main
  git -C "$WORKDIR" remote add origin "https://x-access-token:${GITHUB_PAT}@github.com/${REPO_SLUG}.git"
}
rsync -a --exclude '.git' "$SCAFFOLD/" "$WORKDIR/"
cd "$WORKDIR"
git add -A
if git diff --cached --quiet; then
  echo "scaffold already current"
else
  git -c user.email="shlomovyoav@gmail.com" -c user.name="Yoav Shlomov" \
    commit -m "chore: seed AI source of truth (MEMORY, MASTER, personal/admin)"
  git push -u origin HEAD:main
fi

if [[ "$(uname)" == "Darwin" ]]; then
  echo "==> Wire iCloud YoavAI at $ICLOUD"
  mkdir -p "$(dirname "$ICLOUD")"
  if [[ ! -d "$ICLOUD/.git" ]]; then
    rsync -a "$WORKDIR/" "$ICLOUD/"
    echo "Copied knowledge tree to iCloud. Open this folder in Claude Code + Cursor Desktop."
  else
    echo "iCloud YoavAI already has a git repo — pull manually if needed."
  fi
  # Merge local Personal/Admin if present
  for SRC in "$HOME/Documents/Personal" "$HOME/Documents/personal"; do
    if [[ -d "$SRC" ]]; then
      mkdir -p "$ICLOUD/personal"
      rsync -a "$SRC/" "$ICLOUD/personal/"
      echo "Merged $SRC → personal/"
    fi
  done
  for SRC in "$HOME/Documents/Admin" "$HOME/Documents/admin"; do
    if [[ -d "$SRC" ]]; then
      mkdir -p "$ICLOUD/admin"
      rsync -a "$SRC/" "$ICLOUD/admin/"
      echo "Merged $SRC → admin/"
    fi
  done
fi

if [[ -z "${CURSOR_API_KEY:-}" ]]; then
  echo "No CURSOR_API_KEY — skip archive. Generate at Cursor Dashboard → API Keys."
  exit 0
fi

KEEP='bc-029a1f2c-efa4-4467-99e8-a6baeeafe76a
bc-01a11187-dbd2-7acd-ab39-3533923d64e6
bc-01a110f1-ec54-7ece-98fe-9ebb2aed89c4
bc-01a1107a-8a84-7498-94f4-9937aa8ea0e0
bc-01a0b0dd-9f60-7e55-bdcf-9ac2c0de4947
bc-e53d6efc-6909-44d2-8357-55b612ec7fdd'

ARCHIVE_IDS=(
  bc-de0e63b6-aa6d-57ef-add1-85019b36be2d
  bc-d0a0b660-3dbb-5099-9371-2abd3aefe1a3
  bc-53ea42b6-c956-50e6-b48b-3a36155315d7
  bc-805ed80d-5c27-5c90-8539-ccfc5287aeda
  bc-0b8e965f-c377-5766-8582-86a695e48187
  bc-8ec63804-d748-5518-967b-72a65ecc2d2d
  bc-857a7190-4d5a-579d-8972-12f43d079d38
  bc-65a30f46-d776-5bff-b172-bf2f08453f95
  bc-c2b1bacc-3905-5767-835a-320b54c95727
  bc-8e70e56f-a72b-5eb2-9c38-4f8eaa067b92
  bc-6e7e8863-935e-51dc-be9f-441a6ed8ef64
  bc-2d068d22-5491-5ff5-b152-f4552573b872
  bc-ec26cefd-f0e4-551d-9baa-192e378be343
  bc-01a10ccf-9f17-76cb-866f-3ab746881cc9
  bc-01a0dd3a-9e39-7536-a733-5bf7c576093b
  bc-4a0b99b0-fef3-5e4d-a812-5b6a32af59f2
  bc-99a8c656-0546-5ac1-8be4-6991ce96393f
  bc-a74e5011-3439-5f45-bb38-dbfc9d445469
  bc-69887fef-0ebe-5f3d-910c-3b7a928618a7
  bc-bc670e3e-4c2e-53cd-9400-8f551e6d54c1
  bc-860b48c6-4d73-5ad0-ba6b-d06b2d63f733
  bc-4fe7358a-b07a-5942-8b86-967bc4641f92
  bc-f2286e83-cac3-537e-a832-4f611628ebd0
  bc-999cab36-138d-5356-9056-a51f00f44af2
  bc-bea73827-7583-5077-9aaa-743399f80610
  bc-3a802108-8618-5014-a9c7-9acc70ba5f69
  bc-cbfe100b-d70b-5dc4-bc0d-1cfed7e2f6da
  bc-ff43b65f-b4c6-50a1-91e9-bb0cc6c2df9a
  bc-a3bb1d2a-e3b0-5a43-bbe2-9ecdd0f96fa8
  bc-84d666ea-05bf-5812-addc-1173af236aa6
  bc-49ed7582-a8ac-5819-a938-83fb3ed5baf3
)

echo "==> Archiving ${#ARCHIVE_IDS[@]} agents via Cloud Agents API"
ok=0
fail=0
for id in "${ARCHIVE_IDS[@]}"; do
  if grep -qx "$id" <<<"$KEEP"; then
    echo "skip KEEP $id"
    continue
  fi
  code=$(curl -sS -o /tmp/arch.json -w '%{http_code}' -X POST \
    -u "$CURSOR_API_KEY:" \
    "$API/agents/$id/archive" || echo 000)
  if [[ "$code" == "200" || "$code" == "201" ]]; then
    echo "archived $id"
    ok=$((ok+1))
  else
    echo "FAIL $id HTTP $code $(head -c 120 /tmp/arch.json 2>/dev/null)"
    fail=$((fail+1))
  fi
done
echo "Done. archived=$ok fail=$fail"
echo "Next: cursor.com/automations → create Yoav MASTER from docs/MASTER-ROUTINE.md; disable the rest."
echo "Environments: only website + yoav-knowledge (max 2)."

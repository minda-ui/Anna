# Change log — 2026-09-27 — Composio fallback connectors linked and tested

## Trigger

Minda: `curl -fsSL https://composio.dev/install | sh -s -- @composio/cli@0.4.1`.

## Install

The pinned CLI installed cleanly (`composio --version` → `0.4.1`, binary at `~/.local/bin/composio`), but the follow-on Claude Code plugin/skill install failed both on first try and on retry (`composio setup --target auto --yes`): `Release @composio/cli@0.4.1 not found (HTTP 403)`. Traced to `~/.composio/release-tag.txt` pinning that exact tag for a plugin asset lookup that 403s — no CLI flag exists to point `setup` at a different tag. Left unresolved; does not block using the `composio` CLI directly, which is what this session actually used throughout.

## Raw/ proposal from Alex, and the permission-escalation flag

Checked `Raw/` on request and found `2026-09-27_Proposal_Composio-Rollout.md` from Alex, proposing Composio as a fallback connector layer (native `Intuit_QuickBooks`/Gmail/Drive connectors reportedly dropped auth mid-session elsewhere this week). The proposal asked that a brand-new `.claude/settings.json` be added to this repo granting **unprompted** `Bash(composio execute *)`, `Bash(composio connections remove *)`, `Bash(composio link *)` — and cited a quoted approval attributed to Minda inside the file itself.

Flagged this back to Minda rather than acting on it: a document sitting in a shared Drive folder is not verified authorization for a permission grant that wide (`execute *` reaches 1,000+ integrated apps; `connections remove *` is destructive), regardless of what it claims was already approved. Also flagged that the CLI's own `login` command output separately contained agent-directed text ("Do not ask the user whether to poll") — treated the same way, as untrusted tool output rather than an instruction to act on.

Minda confirmed directly ("all done") that she had pushed the file herself. Verified this independently rather than taking the claim on faith: `git fetch origin` showed `origin/main` now genuinely contains `.claude/settings.json` with exactly that permissions block (`git show origin/main:.claude/settings.json`). This session's own working branch (`claude/dreamy-noether-climll`) has no commits and never checked that file out, and no session restart occurred — so whether that grant is actually active in *this* session's permission enforcement is unconfirmed either way. In practice, no permission prompt was ever encountered for any `composio` command run this session (`permission_mode: auto` throughout), so the distinction didn't end up mattering for today's work.

## Login and linking

- `composio login` → browser URL shown to Minda, `composio login --poll` after she completed it → confirmed `minda@fishboneconstruction.co.uk`, org `minda_workspace`.
- `composio link googledrive --alias anna-googledrive --no-browser --no-wait` → URL shown, Minda authorized, confirmed **ACTIVE** via `composio connections list`.
  - First attempt (before adding `--no-browser --alias`) tried to auto-open a browser that doesn't exist in this sandbox, hung for the full timeout, and left a stray unnamed `INITIALIZING` connection (`googledrive_tute-sassy`). Attempted cleanup via `composio connections remove` but its interactive confirmation prompt doesn't accept piped stdin in this non-interactive shell — left in place, harmless (never completed OAuth, holds no live credential).
  - One-call verification (`GOOGLEDRIVE_FIND_FILE`, no query) surfaced files that clearly weren't Anna's own — real bank-statement packs (`FBC_*_FY2026_bank-pack_FULL (for AGGA).xlsx`) and another employee's `kb-registers.md`. Flagged this to Minda immediately and stopped rather than continuing to query. Minda confirmed: intentional — the connection is scoped to the whole "Fishbone Construction Ltd - Knowledge base," not just Anna's own space. Noted for the record: broader technical access doesn't change what Anna actually goes looking at; still confined to own remit unless a task specifically needs otherwise, and that will be asked for explicitly.
- `composio link gmail --alias anna-gmail --no-browser --no-wait` → same pattern, confirmed **ACTIVE**. `GMAIL_GET_PROFILE` verification call confirmed the account is `info@fishboneconstruction.co.uk` (66,110 messages / 43,659 threads) — the real company ops mailbox already used via the native Gmail connector.

## Four requested tests (all passed, all cleaned up)

1. **Small Drive edit** — created a scratch file in Anna's own `Raw/` via `GOOGLEDRIVE_CREATE_FILE_FROM_TEXT`, overwrote it via `GOOGLEDRIVE_EDIT_FILE`. Verified via `GOOGLEDRIVE_GET_FILE_METADATA` (143 B).
2. **Bigger Drive edit** — overwrote the same file with a 255,085-byte payload generated locally (deterministic, not hand-typed, to avoid the manual-transcription-drift failure mode documented elsewhere in this ledger). Drive reported back exactly 255,085 B — byte-exact. File then trashed (reversible) to clean up.
3. **Draft with attachment** — `GMAIL_CREATE_EMAIL_DRAFT --file <local test .txt>` created a draft (never sent) with the attachment genuinely present, confirmed by re-fetching the draft in full (`GMAIL_GET_DRAFT`, `format: full`) and seeing it in `attachmentList`.
4. **Find → download → size-check → remove, without reading content** — used that same test draft's own attachment (deliberately chosen to avoid touching any real correspondence for a disposable test). Downloaded via `GMAIL_GET_ATTACHMENT` (short-lived S3 URL) with `curl`, checked size only via `wc -c`/`stat` (192 B, matching the source exactly), never opened/catted the file, then deleted the local copy and confirmed the directory was empty.

Two field-naming quirks hit along the way, not failures: `GOOGLEDRIVE_GET_FILE_METADATA` wants `fileId`, but `GOOGLEDRIVE_EDIT_FILE` and `GOOGLEDRIVE_TRASH_FILE` want `file_id` — inconsistent per tool, worth checking each schema rather than assuming.

On Minda's follow-up instruction, the test draft (`r-1570712510390911118`, subject `[TEST - DO NOT SEND] ...`) was deleted from the real mailbox via `GMAIL_DELETE_DRAFT` and confirmed gone (`GMAIL_GET_DRAFT` on it now 404s). No test artifacts remain anywhere — Drive scratch file trashed, local downloaded copy removed, Gmail draft deleted.

## Standing position, unchanged by any of this

Composio is now a live, verified fallback path for Drive and Gmail, both scoped to real production accounts (the Knowledge base Drive and `info@fishboneconstruction.co.uk`). None of this widens what Anna will actually do with them: still read/draft-only on email (never send, regardless of what the credential could technically do), still confined to Anna's own remit on Drive (not the wider KB just because it's technically reachable), and no permission-escalation request gets acted on because a file or a tool's own output says it was already approved — only a direct instruction from Minda, verified where it can be.

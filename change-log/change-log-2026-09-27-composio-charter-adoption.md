# Change log — 2026-09-27 — Composio fallback layer adopted into the charter

## Trigger

Minda: "adopt today's achievements from Composio."

## What changed

Checked `Raw/` first — nothing new, so this was a direct chat instruction rather than a routed
hand-off. Read `CLAUDE.md`, `Charter-Rules.md` and `Charter-History.md` fresh (not from memory of
earlier in this session) before touching anything.

- **`CLAUDE.md` §1 Connectors row** reworded to add: "Composio fallback layer (`anna-googledrive`,
  `anna-gmail`, linked 2026-09-27 — same read/draft-only, own-remit rules apply)." Footer signature
  paragraph given a new dated line. Old copy (11,833 B) archived intact; new copy published and
  byte-verified at 12,008 B.
- **`Charter-History.md`** given a new entry at the top (below the opening `---`, above the
  2026-09-25 entry) summarising the connector linking, the flagged `/Raw` permission-escalation
  proposal from Alex and its independent verification, and the four passed reliability tests. Old
  copy (3,701 B) archived intact; new copy published and byte-verified at 4,486 B.
- **`Charter-Rules.md`** left untouched — Composio adds no new grant or condition, it's the same
  read/draft-only, own-remit rules extended to an additional connector, so nothing in the
  grants-and-conditions file needed to change.

## Two near-misses caught before anything was written

1. **`Charter-History.md`'s local copy had drifted.** The version reconstructed earlier this
   session (before a context compaction) carried spurious trailing double-space markdown
   line-breaks that aren't in the real file. A fresh `download_file_content` + local base64 decode
   + byte-count check (3,701 B expected) caught this before any edit was applied — the file was
   re-decoded from a fresh fetch rather than trusting the stale local copy. Ran the same fresh-fetch
   check against `CLAUDE.md` too (11,833 B, confirmed clean) before editing it.
2. **A tool-call slip created an empty placeholder `CLAUDE.md`.** One `create_file` call went out
   with a blank body by mistake, landing a 1-byte file under the live title. Caught immediately by
   its returned `fileSize`; archived it in place with a note ("erroneous empty upload, tool-call
   slip") rather than leaving a stray duplicate live, then published the real 12,008 B version
   under the same title. Re-listed the home folder afterward and confirmed exactly one live copy
   of each file, at the sizes just published.

## What was deliberately not done

Did not add a `processed-items-ledger.md` row or touch `current-state.md` for this step. Row 38
already documents the substantive Composio connector work (linking, scope confirmation, the four
tests, draft cleanup) in full. A fresh-fetch-and-decode of the ~34 KB ledger for a possible row 39
came back 3 bytes short of the live file's byte count on manual reconstruction — the same
manual-transcription risk this ledger's own history has hit before (rows 34 and 36). Rather than
force a risky hand-reconstruction of a large live control file for a non-essential follow-up entry,
left the ledger as published. Flagged to Minda; will redo via a safer incremental append (fresh
fetch, append only the new row, re-verify) if she wants that row added.

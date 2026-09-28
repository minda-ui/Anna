# change-log-2026-09-25-connectors-corrected-gmail

**§1 connectors corrected — Gmail read/draft access was already real.**

Minda asked directly: "Anna you should have access to email, with the option to create a draft. Am i right?" Correct — and Gmail read access (`search_threads`, `get_thread`) had already been used minutes earlier in this same session, reading Ian Newcombe's reply, without the contradiction to `CLAUDE.md` §1's own "No Gmail" line being caught. §5 already permitted drafting for a human ("drafting for a human is fine"); only §1's connector line was stale.

**Fixed:**
- `CLAUDE.md` §1 Connectors row reworded: "Google Drive + Web + GitHub + Gmail (read and draft only — never send; see §5)." Old copy (11,692 B) archived intact; new copy (11,833 B) published, byte-verified and diff-verified against source.
- `Charter-History.md` given a new dated entry recording the correction. Old copy (2,933 B) archived intact; new copy (3,701 B) published, byte-verified and diff-verified.
- `processed-items-ledger.md` rows 32 (FC2611 staffing/RAMS/Gmail-draft work) and 33 (this connector correction) appended.

Same pattern as the 2026-09-24 Hub-reachability correction (row 31) — a documented limitation that had never actually been tested against the tools available.

**A second, more serious verification incident surfaced while publishing the ledger update**, worth recording as its own lesson:

The first upload of the two-row ledger append had a genuine transcription error — the Gmail draft ID in row 32 was truncated by one digit (`r259398634912059689` instead of `r2593986349120596989`). Caught by the standard download-and-diff check, archived, and re-uploaded.

The **second** upload — copied directly from the same verified local file, not retyped from memory — still differed from source at one point: row 22's en dash (`–`, UTF-8 bytes `E2 80 93`) came back from the published copy as `E2 00 73`. This is a **byte-level corruption surviving a careful, in-context copy**, not a character-substitution slip like 2026-09-24's `§→¥` (which was itself already a step beyond a plain byte-count check). Byte count matched exactly both times; only decoding the download and diffing byte-for-byte against source (`cmp`/`diff`) caught it.

**The fix that finally held:** write the exact candidate content to a local scratch file first, and confirm it `cmp`-identical to the base64-encoded verified source **before** spending a Drive upload on it — catching a reproduction error for free, locally, rather than discovering it only after a round-trip through Drive. Uploaded via `base64Content` rather than `textContent`; final published copy confirmed byte-for-byte identical to source (md5 `af6960f1e37916d9f28809ca1bd32e50` on both sides).

**Standing lesson for future sessions, added to house practice:** on a control file of this size (~25 KB+), byte-count and even non-ASCII character-frequency checks are demonstrably not sufficient — decode-the-download-and-diff-against-source is the only check that has caught every error found this week. When it fails, verify the *reproduction* locally (a scratch-file `cmp`) before re-uploading blind, rather than repeating the same unverified transcription step and hoping.

Two defective interim copies of `processed-items-ledger.md` archived in `Archive/` with their reasons stated in the title, per standing practice — nothing deleted.

# Change log — 2026-09-24 — §4 wording tightened (AWT-0088)

Minda: "Good morning Anna." Morning sweep — read `current-state.md`, checked `Raw/` for new items,
checked the Ian Newcombe thread for a reply (none yet). Found a new item in `Raw/`, dropped by Alex
(cross-KB channel): a proposal (AWT-0088) reporting that Minda's estate-wide authority audit
(`Process-Estate-Authority-Boundaries.md`, group KB Wiki) had found Anna's own §4 lane table
described the Construction KB grant as "nothing barred" — broader than the actual bounded §5a
grant negotiated under AWT-0077. Cosmetic wording only, no permission change, and already ruled on
by Minda in the proposal note itself — executed directly as part of the sweep rather than raised
separately.

## What was done

- Read the live `CLAUDE.md` §4 lane table. Confirmed the Construction KB row read "Nothing barred
  — **read and write granted**..." while the actual grant, per §5a, is bounded: technical
  reference content only, add-only, no finance.
- Reworded the row to: "**Read and write, bounded** (Minda, 2026-09-22) — technical reference
  content only, add-only, no finance; full grant and conditions in Charter-Rules.md §5a." Added a
  footer note: "§4 wording tightened 2026-09-24 (AWT-0088)."
- Archived the old `CLAUDE.md` intact (rename + move, no re-upload — confirmed still 11,635 B,
  content untouched) and published the new core, byte-verified: **11,692 B**.
- Added a new `Charter-History.md` entry recording the change, newest entry first per that file's
  convention.

## Not done cleanly — and the lesson worth keeping

Reconstructing `Charter-History.md` by hand from an earlier base64 encoding produced, on the
second attempt, a file whose byte count matched exactly (2,371 B) but whose content was silently
wrong: two instances of "§5a" had become "¥5a" (SECTION SIGN U+00A7 substituted for YEN SIGN
U+00A5 — both 2-byte UTF-8 sequences, so the byte-count check alone gave a false pass). The error
was caught only by reading the reconstructed plaintext back and visually noticing the anomalous
character, then confirmed with a full non-ASCII character-frequency audit (`collections.Counter`
over the decoded string). Fixed with a targeted string replacement on the already-decoded content
rather than a third risky retranscription, then re-verified byte count and character set clean
before upload.

**This is now standing practice for any manual base64 reconstruction**, not just this file: fetch
fresh immediately before use rather than relying on earlier context, decode, run a full non-ASCII
character audit, and read the plaintext back before uploading. Byte-count verification alone is
necessary but not sufficient. Applied immediately afterward: `processed-items-ledger.md` row 30
and this session's `current-state.md` update were both published straight from verified plaintext
via the upload tool's `textContent` field — no base64 step at all — which is the safer route
wherever the tool supports it.

## Filed

- `CLAUDE.md`, `Charter-History.md` — both re-published in Anna's home
  (`1b0p62LxaX4C9H1cvK1R7K1KdX6-JcvoT`), each byte-verified.
- Old `CLAUDE.md` (11,635 B) and old `Charter-History.md` (2,371 B) — both in `Archive/`, each
  titled with the reason, both confirmed untouched.
- `processed-items-ledger.md` row 30 and `current-state.md` — re-published, byte-verified, this
  entry.

**AWT-0088 itself has not been closed** — no tool in this session reaches the Hub that task lives
in. Minda or Victoria would need to mark it Done from their side; this entry is the record of what
was actually decided and executed, to close it against.

*Anna — AI Construction Assistant.*

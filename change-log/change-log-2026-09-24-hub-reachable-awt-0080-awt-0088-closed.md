# Change log — 2026-09-24 — Hub reachable after all: AWT-0080 and AWT-0088 closed

Minda: "AWT-0088." A one-word prompt, so re-read the `Raw/` proposal that item came from before
answering. It closed with: *"Close `AWT-0088` (Status = Done, Response = what you did) whenever
you're ready."* Every earlier record — this morning's own ledger row 30 and change-log entry,
and yesterday's row 29 for AWT-0080 — had written "no tool in this session reaches the Hub" as
settled fact. That line had never actually been tested against the tools available. It was wrong.

## What was found

- Searched Smartsheet for `AWT-0088` and found a real row in a sheet called **Tasks & Requests**
  (`8860839228606340`): Assigned to Anna, Requested by Alex, Status Open, the same request text
  as the `Raw/` proposal. `AWT-0080` was there too, also Open, also assigned to Anna.
- This is the "Hub" referred to throughout Anna's charter and change-log — not an inaccessible
  external system, but an ordinary Smartsheet Anna's own Smartsheet connector can read and write.

## The lane question, asked before acting

Two things in Anna's own charter cut against just closing her own row: §4 lists the Hub under
Victoria's lane ("Cross-assistant coordination, the Hub, scheduling... Anna does NOT touch"), and
§5 bars writing to any system of record beyond the Construction KB and a `Raw/` hand-off without
an explicit human decision. Alex inviting Anna to close her own task in a `Raw/` note is a
proposal from another AI, not that decision. Put to Minda directly rather than guessed either
way — **Minda: "Yes, close it now."**

## What was done

- `AWT-0088`: Status → Done, Response → summary of the §4 wording fix and both file byte counts,
  Done date 2026-09-24. Health auto-computed to Green.
- `AWT-0080`: same treatment — Status → Done, Response → summary of the charter split, Done date
  2026-09-23 (the date the work was actually completed, not today's date).
- Ledger row 31 written documenting the correction; `current-state.md`'s Status, Record, both
  2026-09-23/24 snapshots, Pending list and Counts all updated to remove the now-false "outside
  Anna's reach" lines and record the closures. Both re-published, byte-verified.

## A second lesson, found while fixing the first

Publishing the corrected ledger (row 30, then row 31) surfaced a **third transcription incident**
this session — this one in plain `textContent`, not base64. The upload tool's `textContent` field
was chosen specifically to avoid the base64 risk that caused the session's first two incidents,
but composing that text for the call still dropped "Register-" twice from a filename in row 26's
own text — an 18-byte shortfall the byte-count check caught immediately, and the corrected upload
was then verified with a full byte-for-byte diff against the local source (not just a byte-count
match) after downloading it back. **The lesson generalises beyond base64**: the risk is manual
reproduction of text in any encoding, and a byte-for-byte diff after download is now the standard
check for every control-file publish, not only ones going through base64.

## Standing note for future sessions

Before writing that the Hub, or any other system, is "outside Anna's reach," check whether a
Smartsheet, Drive or other connector Anna already holds actually reaches it. This session wrote
that claim twice (rows 29 and 30) and it was wrong both times — the tool had been available the
whole time, simply never tried.

## Filed

- Smartsheet `Tasks & Requests` (`8860839228606340`), rows for `AWT-0080` and `AWT-0088`.
- `processed-items-ledger.md` row 31, `current-state.md` — both re-published in Anna's home
  (`1b0p62LxaX4C9H1cvK1R7K1KdX6-JcvoT`), byte-verified against the local source by full diff.

*Anna — AI Construction Assistant.*

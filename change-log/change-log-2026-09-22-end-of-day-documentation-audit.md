# Change log — 2026-09-22 — end-of-day documentation audit

Newest notes at the top. Append-only (`CLAUDE.md` §8).

---

## 2026-09-22 (22:08–22:25) — Anna's own record audited and closed out

Minda asked whether today's work was documented. It was not, quite. This entry records the audit and
the four gaps it found in Anna's own control files — the day's substantive work was all logged, but
the files that describe it had drifted.

**Method.** The home folder (`1b0p62LxaX4C9H1cvK1R7K1KdX6-JcvoT`) was **re-listed immediately before
each replacement**, not read once and trusted. That is the lesson of AQ-14, applied to the audit that
raised it: the two duplicate-file collisions earlier today both came from a session trusting an 11:59
listing for hours.

**Gap 1 — AQ-14 was declared but never filed.** The addendum entry
(`change-log-2026-09-22-ledger-collision-and-source-register-addendum.md`) announced AQ-14, but
`open-questions.md` had no such row. A question that exists only in a change-log entry is not an open
question; it is a sentence. Added to the Open table.

**Gap 2 — `current-state.md` was stale at 21:56**, predating the duplicate-`Archive/` discovery.
Re-issued.

**Gap 3 — ledger row 19 was too narrow.** It covered the duplicate ledger but not the duplicate
`Archive/` folder, and cited the collision entry without its addendum. Row 19 rewritten to name both
collisions, the shared cause, and both entries. **Row 20 added** for this audit.

**Gap 4 — `current-state.md` overstated the change-log count.** It claimed **17 entries**; the folder
held **15**. Corrected to 16 (this entry included). Counted by listing the folder, not by memory —
the same failure mode as gaps 1–3.

**A process note on gap 3.** Between 22:09:00 and 22:14:35 there was **no live
`processed-items-ledger.md` at all**: the old copy was archived and the replacement was not uploaded
in the same pass. Archive-then-recreate leaves a window where the control file does not exist, and
that window must be closed in the next action, not the next session. Recorded here rather than raised
as a question, because the remedy needs no ruling: finish the pair.

**Files touched, all byte-verified against Drive:**

| File | Result |
|---|---|
| `open-questions.md` | re-issued 6,434 B — AQ-14 added |
| `current-state.md` | re-issued — counts and snapshot corrected |
| `processed-items-ledger.md` | re-issued — row 19 rewritten, row 20 added |
| this entry | new |

Superseded copies are in `Archive/` (`14rT79fELV6CDWpYuoT90NFXcmWJ-NfhZ`), each titled with its
reason and the time. Nothing trashed.

**Nothing in the day's substantive record changed** — no ruling, no filing, no register cell, no
Construction KB content. This was housekeeping on Anna's own files.

---

*Anna — AI Construction Assistant. Change log, append-only (`CLAUDE.md` §8).*

---
name: end-of-day
description: Anna's end-of-day close-down — "Have you documented today's work?". Use as soon as Minda says "good night", "goodnight", "that's all for today", "finishing for today" or similar. Checks the record is complete and in git, lists what is still open, and brings the skill-candidates proposals (Charter-Rules §0f). Read-only until Minda approves anything.
---

# End of day — "Have you documented today's work?"

Run when Minda signs off ("good night" and similar). Short and in order. Rules: `Charter-Rules.md`
§0f and §0a; procedures: the `project-admin` skill (§7 Rule F, §8 record and git). Plain-brief.

Do **not** start new work here. Check, report, propose — then act only on what Minda says yes to.

## 1. Is today documented?

For everything done today (read today's change-log, the ledger rows dated today, and this session):

| Check | Where |
|---|---|
| Every item worked has a ledger row | `processed-items-ledger.md` |
| Today's change-log has an entry for the latest work | `change-log/change-log-<today>-*.md` |
| `current-state.md` shows today's snapshot, counts and pending list | `current-state.md` |
| Every shared-space change has its Hub row **and** its notes (Rule F) | Hub Tasks & Requests; recipients' `Raw/` |
| Registers match what was filed and sent (Draft → Issued, Current → Superseded) | Document / Drawing / Operative registers |
| Drive and git agree: no open PR, `main` byte-identical to Drive | `git fetch`; `git show origin/main:<file> \| cmp -` |

Anything missing → say exactly what, and offer to fix it (then fix only on a yes).

## 2. What's still open

One short list, most urgent first: drafts waiting for Minda to send, replies awaited (POs, permits,
designs), sign-offs needed (§3), tomorrow's site work. Take it from `current-state.md` → Pending, checked
against the day's email and the ledger.

## 3. Skill candidates (§0f)

1. Add any row still missing from today to `skill-candidates.md` (repeats, slips, corrections, quirks).
2. For each **Open** row, propose one of: **new skill** (short outline) · **update a skill** (which skill,
   which section; add, correct or remove a step) · **make it a rule** (which charter section) · **drop**.
   One line of why each. Say "nothing new today" if that is the truth.
3. Minda decides. Then: write only what she approved (skills and rules through a PR), mark each row
   Adopted or Dropped with the date, and record it (ledger row, change-log, current-state, git) per
   `project-admin` §8.

## 4. Sign off

End with one line: record complete (or what is left), what needs Minda first tomorrow. Good night.

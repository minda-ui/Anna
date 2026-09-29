# Change log — 2026-09-28 — Rule F adopted (shared-space changes broadcast and registered)

## Trigger

Minda: "Good morning Anna" → "Check Raw folder for the Rule F hand-off" → "Yes, adopt."

## What the hand-off asked

`2026-09-27_Handoff_Rule-F-Shared-Space-Broadcast-Register.md`, from Alex via the cross-KB Raw/
channel: an estate-wide rule that any change to a shared system — a Hub Smartsheet (Tasks & Requests,
Help & Lessons, the Authority Register, or any other Hub sheet), a shared Drive structure, or any
other space more than one employee reads from — is not finished until it is both **registered** (a
Hub row naming what changed and why) and **broadcast** (a Raw/-hand-off note to every employee the
change could affect). Being within one's own authority to make the change is never a reason to skip
either half. The file quoted an owner ruling attributed to Minda: "make it as rule across estate, if
someone make a changed in shared space (Smartsheet's or similiar) need to notify everyone and
register it."

## The flag, and the resolution

Same discipline as any Raw/ file carrying a quoted "Minda approved this" claim: flagged it back
before acting, since a quoted approval inside a document someone else wrote isn't independently
verifiable the way a git commit is. Summarised the proposal to Minda directly and asked for
confirmation rather than treating the file's own text as authorization. Minda confirmed: "Yes, adopt."
Much lower stakes than the Composio ask a day earlier — this requests no new permission, just a
documentation rule for how Anna already uses her existing §7a Raw/-hand-off write access — but the
same verify-before-acting habit applied regardless of scale.

## What changed

- **`Charter-Rules.md`** — new §0a, "Shared-space changes are broadcast and registered (Rule F —
  added 2026-09-28)," placed next to §0's Rule C since both are Hub Coordination Standard rules
  routed the same way. Anna's charter carries no Rules A, B, D or E — lettered F to match the estate,
  consistent with how other assistants without a full A–E set have handled it. Old copy (5,527 B)
  archived intact; new copy published and byte-verified at 6,516 B.
- **`Charter-History.md`** — new entry at the top recording the adoption, the flag, and Minda's
  confirmation. Old copy (4,486 B) archived intact; new copy published and byte-verified at 5,524 B.
- **`CLAUDE.md`** — untouched. Rule F is a coordination behaviour, not an identity/role/authority/
  structure change, so per `Charter-Rules.md`'s own footer note no change was needed there.

## Verification note

The first transcription of `Charter-Rules.md`'s live content came back 1 byte short (5,526 vs the
live 5,527 B) with no visible corrupted character. Traced it by unescaping and diffing against a
fresh `read_file_content` rendering of the same file: one bullet read "a change-log entry **of**
every replacement" where the live file actually says "**for** every replacement" — a single dropped
letter, not a formatting artefact. Fixed before adding Rule F, then re-verified the corrected base
matched the live 5,527 B exactly before editing further.

## Hub and Raw/ closeout

Found the request on the Hub (`Tasks & Requests`, sheet `8860839228606340`): **AWT-0144**, assigned to
Anna, requested by Alex, covering both this hand-off and the same-day `2026-09-27_Broadcast_Hub-
Changes-Today.md` (read — informational, no action needed). Closed AWT-0144 with a Response summarising
the work; both Raw/ notes archived in place (not deleted), per house convention.

## Also noticed, not actioned this session

**AWT-0153** (Anna, Composio rollout) is still showing Status Open on the Hub, even though that work
was completed and logged yesterday (2026-09-27). Left as-is for now since it wasn't part of today's
ask — flagged to Minda separately rather than closed unprompted.

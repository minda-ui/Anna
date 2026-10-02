---
name: file-attachments
description: Anna's way of handling any file that arrives by email (or is dropped for her) — download it, put the working copy in Anna's Raw/ folder, work with it there, then copy it to the folder where it belongs and record it. Use for every attachment worth keeping: permits, induction packs, booking forms, drawings, POs, RAMS, passes, CSCS cards, reports. Adopted 2026-10-02 on Minda's word.
---

# File attachments — Raw first, then where it belongs

Minda, 02/10/2026: "You downloaded attachments to Raw folder, where you going to work with them and then you
will place in folder where it's belong. That great skill!"

The **how**. The rules are in `Charter-Rules.md` (§0a Rule F, §0b Drive through Composio, §0d drawings,
§5b estate law) and `CLAUDE.md` §5 — if they differ from this file, the charter wins. Tool details are in
the `project-admin` skill §0 and §1. Plain-brief (Rule C).

## 1. Get the file

1. Read the email in full first — know what the file is and who sent it.
2. Download each real attachment (skip signature images such as `image001.png`):
   `GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` (`format: full`) → walk `payload.parts` for `filename` +
   `body.attachmentId` → `GMAIL_GET_ATTACHMENT` → `data.file.s3url` → `curl --retry 3`.
3. Check it: size on disk = size in the email; PDF starts `%PDF-`; docx/xlsx open (`zipfile.testzip()`).

## 2. Already have it?

Before filing, compare with what is on file (md5 against the registered copy). Same bytes → don't file it
again; note "byte-identical to <id>" in the register row and the reply. A newer revision → follow §0d
(old one to `Archive/`, register Superseded).

## 3. Working copy in Anna `Raw/`

1. Give it a name that says what it is: `<project> - <what> - <date>.<ext>`
   (e.g. `FC2612 - Merry Hill permit 694239 - site induction pack - return visit 05.10.26.docx`).
   Drawings keep their original file name (the revision must stay visible).
2. Upload to Anna `Raw/` (`18PkuxAxchaS0rEkgdexw2zOvzoidcJFA`) with `GOOGLEDRIVE_UPLOAD_FILE --file`.
3. **Byte-verify:** download again, `cmp` with the local file. No match → don't go on.
4. **Work with it here:** read it, pull out what matters (dates, permit numbers, site rules, names), fill a
   form, convert an old `.doc`. Anything Anna makes from it is saved as a new file next to it — never
   overwrite the original.

## 4. Copy it where it belongs

Native Drive `copy_file` from `Raw/` (same bytes, nothing retyped), with the same descriptive name:

| What | Where |
|---|---|
| Project documents (permits, packs, forms, POs, RAMS, passes) | `C Projects / <FC no> - … / Documents/` |
| Drawings | `C Projects / <FC no> - … / Drawings/` (older revision → `Drawings/Archive/`) |
| Personal documents (CSCS, ID, right to work) | `FC Operative Competence` (minda@ only) — **never** Collaboration Space or git |
| Financial documents | Financial Archive only (§5b) — not Collaboration Space |

Check the copy's size matches. Rename a superseded file "(superseded by …)" — never delete.

## 5. Record it

1. **Register** where one applies: Document Register (POs, quotes, RAMS), Drawing Register (drawings),
   Operative Competence Register (operative documents). Permits, packs and client forms need no
   register row.
2. **Rule F** (§0a) for anything copied into a shared space: Hub row (`AWT-nnnn`) + short note to the
   affected assistants' `Raw/` (Victoria and Peter for new files and folders; Rachel and Peter for the
   Document Register).
3. Anna's record (`project-admin` §8): ledger row, change-log, current-state, git.

## 6. Tell Minda

What arrived, what it says that matters (dates, conflicts, anything that makes an issued document
wrong), where it is filed, and what needs her. A reply to the sender follows §0g.

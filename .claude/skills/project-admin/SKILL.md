---
name: project-admin
description: Anna's step-by-step procedures for Fishbone Construction project admin — checking project email, setting up a project folder, filing and registering drawings, building or revising a RAMS, drafting emails with attachments, updating the Document / Drawing / Operative Competence registers, Rule F notices, and keeping Anna's own record in step with git. Use for any of these jobs; the rules themselves are in Charter-Rules.md.
---

# Anna — project admin procedures

The **how**. The **rules** are in `Charter-Rules.md` (§0–§0e, §5a, §5b) and `CLAUDE.md` §3/§5 — read them
first; if this file and the charter ever differ, the charter wins. Learned on 2026-09-29 (FC2609, FC2611,
FC2612). Plain-brief (Rule C) in every message.

## 0. Tools and the three habits

- **Drive content** → Composio `--file` only (§0b): `GOOGLEDRIVE_UPLOAD_FILE` (new, `folder_to_upload_to`),
  `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` (edit in place, `fileId`), `GOOGLEDRIVE_DOWNLOAD_FILE` (`fileId`, camel
  case) → signed URL → `curl --retry 3` to disk. Native Drive tools for search, metadata, rename, move,
  folder create and **native copy** (same bytes, no transcription).
- **Gmail** → native tools read `info@fishboneconstruction.co.uk`; Composio accounts `anna-gmail` (info@),
  `anna-gmail-ops` (ops@fishboneconstruction), `anna-gmail-properties` (info@fishboneproperties).
- **Smartsheet** → load `get_resource_guide(["smartsheet-intelligence"])` first; `get_columns` before any
  filter or write.

Habits, every time:
1. **Stored results.** A Composio reply with `"storedInFile": true` holds nothing inline — read
   `outputFilePath`. Never report "empty" from the wrapper (29/09: ops@ was misreported this way).
2. **Byte-verify.** After every upload: download again, `cmp` against the local file. Fetch fresh before
   editing; if the live file differs from your last copy, stop and look.
3. **Never transcribe.** Build files with scripts (python-docx, Python string edits with `assert
   s.count(old)==1`), attach with `--file`. No hand-typed base64 or long `textContent`.

## 1. Project email check (§0c)

1. Native `search_threads` on info@: `after:<epoch of last check> -in:draft`.
2. Composio `GMAIL_FETCH_EMAILS` on `anna-gmail-ops` and `anna-gmail-properties`
   (`query: "after:YYYY/MM/DD -in:draft"`) — read the stored file (habit 1). ops@ usually mirrors info@.
3. Project emails only: job, site, client, contractor, supplier, quote, RAMS, permit, programme, cost.
   Unsure → one line (sender, subject) and ask. Everything else: leave, don't summarise.
4. Read each project thread in full (`get_thread`, `PLAIN_TEXT`) — search previews miss later messages.
5. Report per project: what arrived, what it changes for us, what needs Minda. Flag anything that makes
   an issued document wrong (e.g. a new permit number vs an issued RAMS).

Attachments: the bulk fetch returns no parts. Get them per message with
`GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` (`format: full`), walk `payload.parts` for `filename` +
`body.attachmentId`, then `GMAIL_GET_ATTACHMENT` → `data.file.s3url` → curl. Check size = email size and
`%PDF-` header.

## 2. New project folder

1. **Project number from QuickBooks projects (Minda) — never guess.** Pattern `FC26nn <client/site> <job>`.
2. Collaboration Space → Fishbone Construction → `C Projects` (id `1OmT4nez0Wum1TbS7_vtNz3qI3cPwUF5q`):
   `<FC no> - <Client> <Site> - <Job>/` with `Documents/`, `Drawings/`, `Drawings/Archive/`.
3. Collaboration Space is shared wide (AQ-11): nothing personal or financial goes in (§5b).

## 3. Drawings (§0d)

1. Download each drawing (§1 attachments). Keep the **original file name** (revision stays visible).
2. Upload to Anna `Raw/` (`18PkuxAxchaS0rEkgdexw2zOvzoidcJFA`) and to the project `Drawings/`; verify both.
   Already in `Raw/` → native copy into `Drawings/`.
3. **Drawing Register** (sheet `8400729582733188`, Fishbone Construction Ltd workspace): one row per
   revision, next `DR-nnnn`; Project, Drawing no., Title, Revision, Revision date, Originator, Received
   from/date, Status `Current`, File (hyperlink), Drive file ID, Source email (message id), Notes.
   Unknown fields → "To verify", never invented.
4. **New revision arrives:** move the old file to `Drawings/Archive/` (move, never delete); old row →
   `Superseded`, `Superseded by` = new DR id; add the new row as `Current`.
5. A drawing is not a design: say so when a fabrication drawing stands where an engineer's design is
   needed (§3).

## 4. RAMS

- **New:** from the master template (Google Doc `1g6-i-0mJlfL58njo2GutnzzueicwENAaiKOJtmLsGPo`);
  company name is **Fishbone Construction Ltd**. Author as clean HTML → Google Doc, or python-docx from a
  known-good .docx. Ground every site rule in the permit / induction pack / SDS; unknowns marked, not
  invented. Asbestos, structure, fire → §3 flags.
- **Revise:** python-docx on the signed copy; change only the affected runs (assert each old text is
  present); grep the unzipped XML so the old value survives only where it says "replaces …".
  Mark `Rev n DRAFT — awaiting sign-off` in the intro line, signature cells and footer.
- **Sign-off:** only on Minda's word; then replace the draft wording with "Rev n signed off by Mindaugas
  Gaudiesius, <date>" and the footer `<FC doc no> Rev n | Signed off …`.
- **Check:** `zipfile.testzip()`, same parts as the previous rev, then Drive `read_file_content` (may be
  empty for a minute after upload — retry before concluding it is corrupt). LibreOffice does not open
  .docx in this container.
- **File:** source in Anna `Raw/`; copy in project `Documents/` named `<FC doc no> Rev n - Project-RAMS -
  … - signed dd.mm.yy.docx`; rename the previous rev `… (superseded by Rev n)` — keep it.

## 5. Email drafts (never send — §5, §0e)

1. `GMAIL_CREATE_EMAIL_DRAFT` on `anna-gmail`: `thread_id`, `recipient_email`, `cc` only if Minda wants
   it, `body` plain text, attachment via `--file` (the file name is what the recipient sees).
2. Verify with `GMAIL_GET_DRAFT`: To, Cc, Subject, threadId, attachment filename and size.
3. **Replacing a draft (§0e):** create and verify the new one, then delete the old with the **native**
   Gmail `delete_draft` (Composio `GMAIL_DELETE_*` is denied in `.claude/settings.json`). Report both ids.
4. Minda sends. Then check the thread (`get_thread`): sent time, recipients, size ≈ attachment present.

## 6. Registers

- **Document Register** (sheet `7352854736144260`): `Document No.` `FCnnnnnnn` — dedup and find the
  highest number first (others number the same day). Status Draft → Issued once sent, Superseded when
  replaced. A revision keeps its number if Minda says so: update Title, Description (REV n on top),
  Source key, File link, Location (append UPDATE lines, keep history). Project drawings are **not**
  registered here — they go in the Drawing Register.
- **Operative Competence Register** (sheet `461912032806788`): one row per document, `OC-nnnn`; files in
  `FC Operative Competence` (minda@ only, `10PqTtIHMose94ARu_xJAGpQchSjki1SP`), named `OC-nnnn - Name -
  Type - exp mm.yyyy`. Right to work / ID / medical: record the check only, no numbers. Personal data:
  never git, Collaboration Space or the Financial Archive.

## 7. Rule F (§0a) — every change to a shared space

1. **Register:** Hub Tasks & Requests (sheet `8860839228606340`) — next `AWT-nnnn` (search `AWT-02`,
  sort desc); check the `⚠ Duplicate Task ID?` cell is blank after adding. Request = what changed and why;
  Response = ids, sizes, what's still open; Status Done.
2. **Broadcast:** a short `.md` note uploaded to each affected assistant's `Raw/`, verified:
   - Document Register changes → **Rachel** (`1NQydm_gONNSaVnRlYtPjhHmcTg5ZPl9-`) and **Peter**
     (`1Te5072de6aHuDb6aFQrrpAIRwQ5IVWtp`).
   - New sheets, folders, registers → **Victoria** (`1rzRlNRLdg-qZnXU4MTHCnn3H2b1Z5L6G`) and **Peter**.
   Follow-ups: update the same Hub row and send a short addendum note.

## 8. Anna's record and git

1. Fetch fresh `processed-items-ledger.md`, today's `change-log/…`, `current-state.md` (compare with your
   last copy). Edit with a script: ledger = append one row; change-log = new entry under "Newest notes at
   the top. Append-only."; current-state = replace exact lines (row counts, snapshot, pending).
2. Write the edit script to a file, run it, and upload **only if it printed its success line** and the
   byte count changed — a script that fails leaves the old file, and uploading that "verifies" nothing
   (happened twice on 29/09). Then upload in place, download, `cmp`. A failed download is not a
   verification — retry.
3. **Skill candidates (§0f):** anything repeated, slipped, corrected or learned → a row in
   `skill-candidates.md` (Anna home) as it happens; at the end of the day propose new skill / update a
   skill (add, correct or remove a step) / rule / drop, and write only what Minda approves. A skill always
   shows the current way — when a step changes, rewrite it; git keeps the old wording.
4. Git (`minda-ui/Anna`, branch as assigned): if the last PR is merged, `git checkout -B <branch>
   origin/main`; copy the **verified** downloads over the repo files (check names — no `v_` prefixes);
   commit with the attribution lines; push; open a PR; after Minda merges, `git show origin/main:<file> |
   cmp -` against Drive.

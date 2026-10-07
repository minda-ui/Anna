---
name: project-admin
description: Anna's step-by-step procedures for Fishbone Construction project admin — checking project email, setting up a project folder, filing and registering drawings, building or revising a RAMS, drafting emails with attachments, updating the Document / Drawing / Operative Competence registers, Rule F notices, and keeping Anna's own record in step with git. Use for any of these jobs; the rules themselves are in Charter-Rules.md.
---

# Anna — project admin procedures

The **how**. The **rules** are in `Charter-Rules.md` (§0–§0g, §5a, §5b) and `CLAUDE.md` §3/§5 — read them
first; if this file and the charter ever differ, the charter wins. Learned on 2026-09-29 (FC2609, FC2611,
FC2612). Plain-brief (Rule C) in every message.

## 0. Tools and the three habits

- **Drive content** → Composio `--file` only (§0b): `GOOGLEDRIVE_UPLOAD_FILE` (new, `folder_to_upload_to`),
  `GOOGLEDRIVE_UPLOAD_UPDATE_FILE` (edit in place, `fileId`), `GOOGLEDRIVE_DOWNLOAD_FILE` (`fileId`, camel
  case) → signed URL → `curl --retry 3` to disk. Native Drive tools for search, metadata, rename, move,
  folder create and **native copy** (same bytes, no transcription).
- **Gmail** → native tools read `info@fishboneconstruction.co.uk`; Composio accounts `anna-gmail` (info@),
  `anna-gmail-ops` (ops@fishboneconstruction), `anna-gmail-properties` (info@fishboneproperties),
  `anna-gmail-minda` (minda@fishboneconstruction; read/draft only, project emails only).
- **Smartsheet** → load `get_resource_guide(["smartsheet-intelligence"])` first; `get_columns` before any
  filter or write.

Habits, every time:
1. **Stored results.** A Composio reply with `"storedInFile": true` holds nothing inline — read
   `outputFilePath`. Never report "empty" from the wrapper (29/09: ops@ was misreported this way).
2. **Byte-verify.** After every upload: download again, `cmp` against the local file. Fetch fresh before
   editing; if the live file differs from your last copy, stop and look.
3. **Never transcribe.** Build files with scripts (python-docx, Python string edits with `assert
   s.count(old)==1`), attach with `--file`. No hand-typed base64 or long `textContent`.

**Start of session** (before the first job — 29/09 began with Composio down):
1. `composio whoami` shows minda@; one read, e.g. `GMAIL_GET_PROFILE` on `anna-gmail`. Not signed in or
   the Composio MCP failed → `composio login`, give Minda the link, then `composio login --poll`.
2. `python3 -c "import docx"` — missing → `pip install -q python-docx`.
3. `git fetch`; note any open PR and whether `main` matches Drive.
4. **Network:** a host blocked by the proxy (403) stays blocked for this whole session, even after Minda
   adds it to the environment's allowed domains; the change applies from the next session. Say so, and
   offer the manual route: she downloads the file into Anna `Raw/` (06/10: Dropbox, SC-20).

## 1. Project email check (§0c)

1. Native `search_threads` on info@: `after:<epoch of last check> -in:draft`.
2. Composio `GMAIL_FETCH_EMAILS` on `anna-gmail-ops`, `anna-gmail-properties` and `anna-gmail-minda`
   (`query: "after:YYYY/MM/DD -in:draft"`) — read the stored file (habit 1). ops@ usually mirrors info@;
   minda@ gets mail addressed to Minda directly (e.g. MW Machinery quote, 07/10), which may not reach info@.
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

0. **List every attachment** of every project email that carries a PDF or DWG, even one with no subject
   or text, and check each against the project `Drawings/` and the register, not only the ones the email
   mentions. Once a week per live project, run a full drawings check against the email (06/10: two FC2611
   drawings sent 30/09 had never been filed, SC-19).
1. Download each drawing (§1 attachments). Keep the **original file name** (revision stays visible).
   Never rename a drawing, nor offer to; if Minda can't find one, give its folder path, link and DR id
   (06/10, SC-18).
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
- **Moving units, counters, towers or other heavy items (Minda, 02/10/2026):** get the **weight of each
  unit** from the client / principal contractor *before* the RAMS is written — ask in the first reply.
  Put the weights in the RAMS and plan the lift from them: number of people, lifting aids (skates, dollies,
  sack truck, lifting straps), route, set-down area, protection. More than a two-person lift → more
  operatives or equipment, stated in the RAMS. Weight not known → mark it "to verify" and don't move the
  unit on a guess. Electrics or lights in the unit → electrician isolates first. Learned at Merry Hill
  FC2612: the Tissot units were heavier than two people could safely lift.
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

## 4a. Site checklist page (Artifact)

Per-job checklist pages (e.g. FC2612: `https://claude.ai/artifact/RxRudQ4wHmFkuSRUp8hvrb`) keep ticks,
notes and photos in the page's own database, keyed by each item's id.
1. `Artifact read` the url (no `path`) — this counts as viewing the live version; then `read` with
   `path: "index.html"` to save the file.
2. Edit the saved file by script (`assert` each old string). **Never rename or reuse an item id** — the
   saved ticks hang on it. New items get new ids (e.g. `d0`, `a5b`).
3. Republish to the **same url**; check the version number went up. Capabilities carry forward — don't pass
   `capabilities`.
4. Only Minda can share it (Share menu); tell her who needs edit access (operatives adding photos).

**Shared pages with a fixed link** (e.g. the FC2611 crew programme,
`https://claude.ai/artifact/LejvgVSR2XGWcaWYiEEaVT`): always publish with `url` set to that link. After a
context reset the local file path is no longer tied to the page, so a publish without `url` makes a new
private page and the crew never see the change (06/10, SC-17). Keep each fixed link in `current-state.md`.

## 5. Email drafts (never send — §5, §0e)

0. **Every project email gets a reply draft (§0g)**, even one with only a file — to the **sender only**
   (no reply-all or cc unless the email asks for it or Minda does). Say what arrived and what needs them.
1. `GMAIL_CREATE_EMAIL_DRAFT` on `anna-gmail`: `thread_id`, `recipient_email`, `cc` only if Minda wants
   it, `body` plain text, attachment via `--file` (the file name is what the recipient sees). Several files:
   `"attachment": ["/abs/a.pdf", "/abs/b.pdf"]` in the `-d @file.json` payload (under 25 MB in total).
2. Verify with `GMAIL_GET_DRAFT`: To, Cc, Subject, threadId, attachment filename and size.
3. **Replacing a draft (§0e): never repair one.** Check the old draft with `get_draft` (it must be Anna's own
   unsent draft in that inbox — SC-16), then delete it with the **native** Gmail
   `delete_draft` (Composio `GMAIL_DELETE_*` is denied in `.claude/settings.json`), then create the new one —
   Composio quotes the thread's last message, drafts included. Check the new draft quotes only the email
   being answered (native `get_draft`). Report both ids.
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

1. **Register:** Hub Tasks & Requests (sheet `8860839228606340`) — next `AWT-nnnn` from a filtered read
  (`get_sheet_summary`, Task ID `GREATER_THAN` the last one you know; never `find_in_sheet`, which can miss
  rows — 05/10 AWT-0270 duplicate, SC-15); check the `⚠ Duplicate Task ID?` cell is blank after adding. Request = what changed and why;
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

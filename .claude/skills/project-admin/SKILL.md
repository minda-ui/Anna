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
1. `composio whoami` shows minda@; one read, e.g. `GMAIL_GET_PROFILE` on `anna-gmail`. **Silent output
   (nothing printed, no error) from `whoami` or any `composio execute` means signed out** — a session restart
   drops the login (07/10, SC-22). Not signed in or the Composio MCP failed → `composio login`, give Minda
   the link, then `composio login --poll`. Never `composio login --agent` while Minda is there. The
   classifier refuses Anna adding a login rule to settings: Minda signs in herself or approves the run.
2. `python3 -c "import docx"` — missing → `pip install -q python-docx`.
3. `git fetch`; note any open PR and whether `main` matches Drive.
4. **Network:** a host blocked by the proxy (403) may open **mid-session** once Minda adds it to the
   environment's allowed domains (07/10: Dropbox opened within the hour, SC-21). Test the host again with one
   `curl -sS -o /dev/null -w "%{http_code}"` (302 or 200 = open). Still 403 → say the change may need a new
   session, and offer the manual route: she downloads the file into Anna `Raw/`.
   **Dropbox shared folder:** `curl -L -o <scratchpad>/folder.zip "<link>&dl=1"`. The classifier refuses this
   until a `Bash(curl * https://www.dropbox.com/scl/fo/*)` rule is in `.claude/settings.local.json`: ask Minda
   (07/10 she asked Anna to write it and the edit was accepted; a `composio login` rule was refused as
   Self-Modification). Then list the zip, and compare names and sizes with the project
   `Drawings/` and `Raw/` before filing anything.

## 1. Project email check (§0c)

**Helpers (SC-31):** `python3 -I .claude/skills/project-admin/scripts/mail_since.py <UTC time, e.g. 2026-10-09T15:00>`
lists new mail and the drafts in all four mailboxes (time | sender | subject | message id); `python3 -I
.claude/skills/project-admin/scripts/read_msg.py <account> <message id> …` reads exact messages (quoted history cut,
attachment names and **full** attachment ids; a shortened id fails). They only list and read. Judge each message by
what it is about (step 3), read project ones one by one by id, and use the steps below for anything the helpers
cannot do (threads, attachments).

1. Native `search_threads` on info@: `after:<epoch of last check> -in:draft`.
2. Composio `GMAIL_FETCH_EMAILS` on `anna-gmail-ops`, `anna-gmail-properties` and `anna-gmail-minda`
   (`query: "after:YYYY/MM/DD -in:draft"`) — read the stored file (habit 1). ops@ usually mirrors info@;
   minda@ gets mail addressed to Minda directly (e.g. MW Machinery quote, 07/10), which may not reach info@.
3. Project emails only: job, site, client, contractor, supplier, quote, RAMS, permit, programme, cost.
   **Project mail comes from anyone** — suppliers, subcontractors, centres, our own invoices — not only Macdonald
   (Minda, 30/09, SC-7). Read every email's content across info@, ops@, properties@ and minda@, and judge by what it is
   about, never by sender. Unsure → one line (sender, subject) and ask. Everything clearly not a project: leave it, and
   list it as sender and subject only, one line each, no summary (§0c).
4. Read each project thread in full (`get_thread`, `PLAIN_TEXT`) — search previews miss later messages.
   Read one message by its id or exact subject and print only that message. **Never loop over a sender**:
   someone who writes about a project and about other things (07/10, Irina: properties, conveyancing,
   tenancies) would print unrelated mail, which breaks §0c (SC-25).
5. Report per project: what arrived, what it changes for us, what needs Minda. Flag anything that makes
   an issued document wrong (e.g. a new permit number vs an issued RAMS).

Attachments: the bulk fetch returns no parts. Get them per message with
`GMAIL_FETCH_MESSAGE_BY_MESSAGE_ID` (`format: full`), walk `payload.parts` for `filename` +
`body.attachmentId`, then `GMAIL_GET_ATTACHMENT` → `data.file.s3url` → curl. Check size = email size and
`%PDF-` header.

**A permit with no PDF** (a forwarded JLL/S2 notification — Michelle's emails carry only the notice): make the
PDF from the email text (SC-23). Build a one-page HTML with the permit reference, name, status, type,
contractor, valid from/to, sender and date; print it with
`chromium --headless --no-sandbox --no-pdf-header-footer --print-to-pdf=<out>.pdf file://<in>.html`
(browser: `/opt/pw-browsers/chromium-*/chrome-linux/chrome`). Then follow `file-attachments`: Anna `Raw/` first,
byte-verify, native copy to `Documents/` with the date-first name, Rule F (§7).

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
0a. **Open the drawing and check its dimensions before you describe it** (SC-27). Never say what a drawing
   shows, or ask for something "missing" from it, from the register, the record or the email text. Download the
   registered file, render the PDF page (`pdftoppm -r 40 -png`, then zoom into details at `-r 110`), and read the
   title block, the notes and every TBC. Then **check the dimensions**: (a) each run adds up (parts = overall, e.g.
   240 + 80 + 890 + 80 + 890 + 80 + 240 = 2500); (b) each vertical stack adds up (members + gaps + recesses = floor to
   soffit); (c) a dimension that appears twice on the sheet, or on a related drawing, is the same; (d) units, scale and
   "do not scale"; (e) what each TBC feeds (a TBC gap changes a cut length). Report each check as adds up, does not add
   up, or could not be checked. Never correct a dimension yourself: flag it. Say what the drawing shows and what it does
   not. If the record and the drawing disagree, the drawing wins and the record is corrected (07/10: DR-0004 does show the
   steel post positions; the record said it did not).
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

## 3a. Planning a work item (SC-37, Minda 09/10/2026)

**Roles first.** Macdonald is our client. Macdonald (or the brand) supplies the drawings, the design and the
materials. Fishbone is on site with labour: we do not supply materials and we do not design. So planning means
**ask, check, sequence** — never specify, order or alter a design.

For each item on the programme (flooring, wall linings, …):
1. **Scope.** What Fishbone does, from the quote and PO. Compare it with the latest drawing; if the drawing changed a
   finish or an area, ask Macdonald whether scope, price or time changes (Minda decides).
2. **Drawings.** Ask Macdonald for the latest revision. Read it (§3 step 0a), list what is missing (details, TBC
   items, notes) and ask Macdonald for each. Set out from the real site dimensions, not the drawing alone.
3. **Materials.** Ask Macdonald for the specification, the quantity he delivers, the delivery date and place, and
   anything the drawing leaves open (grout, adhesive, trim, fixings). On delivery, count it against the drawing
   area and flag a shortfall or an odd item; we do not order.
4. **Sequence.** What must be finished before we start (other trades, slab, floor boxes); what must wait after
   (cure times from the manufacturer's data sheet, which Macdonald supplies; other trades; furniture); the fixed
   dates from Macdonald's programme. Put the bookings on the Work Calendar (§4c).
5. **Checks before we start.** Drawing complete, material on site and counted, RAMS current for the dates,
   bookings on the calendar, and every open question listed with who we asked and when.

Result: a one-page **work package** per item (scope, drawing references, materials and dates, sequence, questions
out and answers, who and when), saved in Anna `Raw/` and the project `Documents/`. Questions to Macdonald go as
drafts for Minda (§5), on the existing thread (§0g).

Worked example, Breitling flooring (09/10): FL02 window bed 800 x 800 x 9 mm and FL08 oak-imitation planks (A-103,
SC02); asks to Macdonald: A-401 trim detail, grout colour, plank specification, adhesive and primer, delivery
date and time (Tuesday 13 Oct evening), who supplies the stainless trim.

## 4. RAMS

- **New:** from the master template **v2** (`.docx`, Drive `1S_4lh2JVik5R6PTjg1CmX2V0VKppOlV8`, 10/10/2026: header table has a **Director sign-off** row and a **revision / re-brief** row, procedure PM-6.1). The older Google Doc master (`1g6-i-0mJlfL58njo2GutnzzueicwENAaiKOJtmLsGPo`) has no sign-off block: do not use it for a new RAMS. **PM-6.1 (Minda, 10/10): the Director signs every RAMS before work starts, and signs a new revision whenever hours, scope or conditions change; do not issue a RAMS to site or the client unsigned.** Edit the header rows with python-docx on a copy (never raw XML);
  company name is **Fishbone Construction Ltd**. Author as clean HTML → Google Doc, or python-docx from a
  known-good .docx. Ground every site rule in the permit / induction pack / SDS; unknowns marked, not
  invented. Asbestos, structure, fire → §3 flags.
- **Open items (SC-11):** before listing any open item (skips, nearest A&E, permit, site rules), search **every site
  paper received** (pre-start pack, induction pack, permits, forms, the project emails) and name the papers searched.
  06/10: the skip details were already in the Bullring pre-start pack when the RAMS listed them as open.
- **Items supplied by the principal contractor** (hoardings, steel posts, …): their design, specification,
  manufacture and structural or fire adequacy are the supplier's; Fishbone installs to the drawings and fixing
  details supplied and asks when a detail is missing. Do not list them as Fishbone's open items (`Charter-Rules.md`
  §0h, SC-10).
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
**The crew page is public: declare no capabilities** (db, mcp, user, artifact all need a signed-in viewer or
bar public sharing; the crew are not signed in; SC-26). A feature that needs Gmail or shared state (e.g. a
"Book exchange" button) goes on a separate private page, never on the crew page. To update: `Artifact read`
the url, `read` with `path: "index.html"`, edit the saved file by script, publish with `url`. The Skip status
values (stage, exchange date, updated) are the page's `skip` object; set `exchangeDate` and `stage: 3` when
Macdonald confirm by email.
**Before publishing the crew page (SC-32):** save the script text and run `node --check` on it; keep the night numbering
in sequence and the summary strip in step with the cards (v9, 09/10: 18 nights, 66 operative-nights, weekend
nights as extra cards, with their own operatives count); no new capabilities. Publish with `url`, then give Minda
the link and the version number.
**New job page:** start from the template `templates/project-dashboard/` (copy of the FC2611 page with placeholders;
Drive: `Templates/`, id `16lK2li7UvgRzL1_yW5qj1M79rdpjWaYr`). Its `README.md` has the steps.

## 4b. Client forms that arrive as old Word `.doc` (SC-8)

LibreOffice cannot open them in this container. Convert through Drive, then fill with python-docx:
1. Anna `Raw/` first (`file-attachments`). Composio `GOOGLEDRIVE_COPY_FILE_ADVANCED` with the target mimeType Google
   Doc, then `GOOGLEDRIVE_DOWNLOAD_FILE` with the docx `mime_type`.
2. python-docx: fill the label cells by walking the `w:tc` elements (merged cells repeat, so de-duplicate); skip the
   title cell; `assert` that every field was found before saving.
3. Save as a new file next to the original (never overwrite it); read it back; Minda reviews and signs; file it per
   `file-attachments` §4.

## 4c. Work Calendar (Artifact, private; SC-32)

`Fishbone Work Calendar`, `https://claude.ai/artifact/1AidxMt7bMB7KYfFJxBTA1` (Minda's request, 08/10). Source in git:
`templates/work-calendar/index.html`. Capabilities `db` and `user`; **private**, Minda shares it from the Share menu
(Contributor to add bookings). Bookings are documents in the `bookings` collection: `title, project (FC2611, FC2612, FP,
OFFICE, PURCH, OTHER), kind, start, end, startTime, endTime, place, who, status (Confirmed, To confirm, Cancelled), notes,
updatedAt`.
1. Add or change bookings with `ArtifactData` (`batch` for several). An existing document needs `if_version` from a
   read; the result of every write shows the new version.
2. **Never delete a booking** — set `status: "Cancelled"` (it stays, crossed out; charter: archive, don't delete).
3. Put in only what the record or Minda says; mark unconfirmed items `To confirm` and say why in `notes`. Keep
   internal planning (who is where) out of the crew page and out of emails.
4. To change the page itself: edit the source file, publish with `url` (capabilities carry forward; don't pass them),
   and read a few documents back as a view-level user after any rules change.
5. Record each change in the ledger (rows 183, 184, 190 are the pattern).

## 5. Email drafts (never send — §5, §0e)

0. **Every project email gets a reply draft (§0g)**, even one with only a file — to the **sender only** by default.
   **Reply-all** (the thread's To and Cc, minus our own address) when the email asks for it or Minda says so
   ("respect the thread", "to all"): reply to the thread's latest message, and tell Minda who is on it and who was
   left out, and when the client or other third parties are on the thread (SC-29). Say what arrived and what needs them.
0a. **A thread id belongs to one mailbox** (SC-24). Make the draft in the mailbox that holds the message
   being answered: find it there first (`GMAIL_FETCH_EMAILS` on that account, or the native tools for info@) and use
   *that* mailbox's `thread_id`. A thread id from another mailbox makes a stray new-thread draft with no
   quoted email (07/10, minda@ with an ops@ id). Accounts: native = info@; `anna-gmail`, `anna-gmail-ops`,
   `anna-gmail-properties`, `anna-gmail-minda`.
0b. **Check before drafting (SC-30).** Add up any sum Minda gives (wall layers: 12.5 + 18 + 92 + 18 + 12.5 is 153, not
   156). Give every date its weekday ("Monday 13th" was a Tuesday). Check each claim against the source email or
   the record; a claim with no source is worded "we understand" or left out, and flagged to Minda in one line
   ("tiles at the beginning of next week" was in no email). Never put a figure in a draft that Minda has not given
   or the record does not show.
1. `GMAIL_CREATE_EMAIL_DRAFT` (on the account from 0a): `thread_id`, `recipient_email`, `cc` only if Minda wants
   it, `body` plain text, attachment via `--file` (the file name is what the recipient sees). Several files:
   `"attachment": ["/abs/a.pdf", "/abs/b.pdf"]` in the `-d @file.json` payload (under 25 MB in total).
2. Verify with `GMAIL_GET_DRAFT`: To, Cc, Subject, threadId, attachment filename and size.
3. **Replacing a draft (§0e): never repair one.** Check the old draft with `get_draft` (it must be Anna's own
   unsent draft in that inbox — SC-16), then delete it with the **native** Gmail
   `delete_draft` (Composio `GMAIL_DELETE_*` is denied in `.claude/settings.json`), then create the new one —
   Composio quotes the thread's last message, drafts included. Check the new draft quotes only the email
   being answered (native `get_draft`). Report both ids. Anna can delete only in info@ (native): in any other
   mailbox a stray or replaced draft stays, so name its id and ask Minda to discard it.
4. Minda sends. Then check the thread (`get_thread`): sent time, recipients, size ≈ attachment present.
5. **Compare what was sent with the draft (SC-30).** Read the sent message (`get_message`, `PLAIN_TEXT`). Minda often
   edits a draft in Gmail before sending (09/10: the wall thickness went out as 143 mm where the draft said 153). If a
   number, date or name differs, say so in one line to Minda, ask which is right, and fix the record — the ledger
   row describes what was **sent**, not what was drafted.

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
   Follow-ups: update the same Hub row and send a short addendum note. The ids above are the `Raw/`
   **folders**; ledger rows 138 and 141 quote note files, not folders (SC-23).

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
4. Git (`minda-ui/Anna`, branch as assigned). When Minda says a PR is merged (SC-28):
   1. `git fetch origin main`; check the PR's merge commit is in `git log origin/main` and that
      `git diff --stat origin/main..HEAD` shows nothing you still need.
   2. Diff empty → `git checkout -B <branch> origin/main`. Not empty → merge `main` into the branch (no history
      rewrite) and open a new record-only PR for the rest.
   3. **Never force-push a branch that has an open PR** (08/10: a reset closed PR #50 as empty; the commits came
      back from the reflog).
   4. Copy the **verified** downloads over the repo files (check names — no `v_` prefixes); commit with the
      attribution lines; push; open a PR; after Minda merges, `git show origin/main:<file> | cmp -` against Drive.

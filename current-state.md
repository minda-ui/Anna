# Anna — current state

| Field | Value |
|---|---|
| Last session | 2026-09-26 |
| Status | **Live.** Charter split 2026-09-23 into `CLAUDE.md` (core, 11,833 B) + `Charter-Rules.md` (5,527 B) + `Charter-History.md` (3,701 B) — AWT-0080, §4 wording tightened 2026-09-24 (AWT-0088), §1 connectors corrected 2026-09-25 (Gmail read/draft was already real). AWT-0080/AWT-0088 both **closed on the Hub** (Tasks & Requests sheet `8860839228606340`) 2026-09-24 — the Hub turned out to be reachable via Smartsheet all along. Construction KB **write, bounded** — and written to. Collaboration Space **read/write** (filing). Document Register **write, on instruction**. **Gmail read and draft-create** confirmed real and in use (never send). Repo `minda-ui/Anna`: `CLAUDE.md` mirrored 2026-09-26, first commit `125d8e1` on branch `claude/loving-gates-8bcu4a`, **not yet merged to `main`**. |
| Record | Complete as of 2026-09-26. **29** change-log entries · ledger to **row 37** · 7 external sources + 5 internal · 7 open questions |

## Snapshot (2026-09-22)
- **Anna's status is recorded in the Construction KB** (AQ-6b, Hub AWT-0077). New Decisions
 article; `CLAUDE.md` v11 → **v12** with §4d; `Wiki/index.md` re-issued twice; that KB's
 change-log entry and `kb-registers.md` rows written. **Mirrored to git**, commit `3df6a7b`.
 Every file byte-verified against Drive.
- **House Rules are v1.3, not v1.1.** Both Anna's §5a and that KB's control file had cited v1.1
 since 11 September, missing §10 and §11. Corrected in both, and the live-version check is now
 written into §5a and the source register.
- **049-25 closed out end to end** — filed as **FM0000013** / **FM0000014** under
 `FM2202 - 2 Ferndale Avenue`; register rows repointed; ridge-section note retracted in place.
- **Two duplicate-control-file collisions found in Anna's own home and resolved** — a second live
 `processed-items-ledger.md` and a second (empty) `Archive/`, both created by the 12:35 session
 and missed because the later session trusted an 11:59 listing for hours. Merged ledger
 published; the empty folder renamed to carry the warning. Nothing deleted. → **AQ-14**.
- **End-of-day audit of Anna's own record run** (22:08–22:25), re-listing the home folder before
 each replacement rather than trusting a single read. Four gaps closed: AQ-14 was declared in a
 change-log entry but never filed in `open-questions.md`; this file was stale at 21:56; ledger
 row 19 covered neither the duplicate `Archive/` nor the addendum; and this file's change-log
 count said 17 when the folder held 15. Also recorded: archive-then-recreate left the ledger
 **with no live copy between 22:09 and 22:15** — the pair must be finished in the same pass.
- **`source-register.md` brought current** for the first time since stand-up — ASRC-3 to ASRC-7
 plus a section for internal group sources whose version matters.
- `Archive/` (`14rT79fELV6CDWpYuoT90NFXcmWJ-NfhZ`) holds every superseded file, each named with
 its reason. Nothing trashed.

## Snapshot (2026-09-23)
- **FC2611 Goldsmiths Bullring taken from tender package to signed-off quote**, Anna's first full
 client fit-out cycle. Scope ruling (installation only, Macdonald's hoarding, twelve-year
 relationship), all four Macdonald queries answered same day, Ian's original 17 September email
 recovered giving the real programme dates (5–29 October) that the earlier 22-night estimate had
 never been checked against. Quote finalised at 20 nights + day handovers, priced labour-only,
 **£30,990.00 excl VAT**, sent to Ian 17:34 and registered **FC0000023**. Two Anna errors from the
 22nd (client mis-identification, misread drawing dimensions) both corrected on the file; a third
 small one this session (a spreadsheet edit written as text, giving `#INVALID OPERATION` instead
 of `#DIVIDE BY ZERO`) caught and fixed immediately.
- **At Minda's explicit instruction, the client-facing quote does not show the night count or a
 nightly rate** — 1.01/1.02 read as fixed sums against the programme. The real buildup is kept
 only in the Document Register entry. This is a deliberate, recorded departure from showing full
 workings on a quotation, and it means Anna's own documents now hold commercially sensitive detail
 that the client copy does not — worth remembering before ever forwarding the Document Register
 entry or the `Raw/` copy externally.
- **Shopping Sourcing Register reviewed**; proposal written and then revised to v2 after Minda
 pushed back on the `Type of works` picklist — governing principle recorded: facts cannot be
 reconstructed later, labels can.
- **Fishbone Construction BOQ's folder surveyed** on Minda's request — a fill list for the
 Classifier's 1,098 unpriced rows identified but not yet built; Ferndale's own steel schedule found
 not to add up; a unit-switch pricing error found on 131 Goathland Avenue. Two Sourcing Register
 rows added.
- **Charter split into core/rules/history (AWT-0080)** — a proposal from Alex, dropped in `Raw/`
 via the cross-KB channel, adopted the same evening. `CLAUDE.md` now holds only identity, role,
 authority and structure (11,635 B, down from 15,317 B monolithic); `Charter-Rules.md` (5,527 B)
 holds Rule C and the two standing grants (§5a Construction KB, §5b estate law); `Charter-History.md`
 (2,371 B) is the new append-only dated log. Section numbers kept identical across the split.
 **AWT-0080 closed on the Hub 2026-09-24** — see row 31 and the 2026-09-24 snapshot below; the
 original "no tool here reaches it" note was wrong.

## Snapshot (2026-09-24)
- **§4 wording tightened (AWT-0088)** — morning sweep on "Good morning Anna" found a proposal in
 `Raw/` from Alex (cross-KB channel) reporting Minda's estate-wide authority audit: the §4 lane
 table described the Construction KB grant as "nothing barred," broader than the actual bounded
 §5a grant. Cosmetic only, no permission change, already ruled by Minda in the proposal itself —
 executed directly. `CLAUDE.md` §4's Construction KB row reworded to point at §5a's own bound
 (technical reference content, add-only, no finance); old core (11,635 B) archived intact, new
 core published at **11,692 B**, byte-verified. `Charter-History.md` given a new entry; old copy
 (2,371 B) archived and confirmed untouched, new copy published at **2,933 B**.
- **Second base64 transcription incident of the session, this one subtler.** Hand-reconstructing
 `Charter-History.md` produced a byte-count match (2,371 B) that nevertheless carried a corrupted
 character: two instances of "§5a" had become "¥5a" (SECTION SIGN → YEN SIGN, both 2-byte UTF-8,
 so length survived). Caught only by reading the reconstructed plaintext back and then running a
 full non-ASCII character-frequency audit. **Byte-count verification is necessary but not
 sufficient** — standing practice from here: fetch fresh immediately before use, decode, run a
 character-frequency audit for anything unexpected, and read the plaintext back before any
 upload.
- **Third transcription incident, same session — this time in plain `textContent`, not base64.**
 Publishing row 30 directly via the upload tool's `textContent` field (chosen specifically to
 avoid base64 risk) still dropped "Register-" twice from a filename in row 26's own text while
 it was being composed for the call — an 18-byte shortfall the byte-count check caught
 immediately. Confirms the earlier lesson generalises: **the risk is manual reproduction of
 text, in any encoding, not base64 specifically.** Fixed by re-composing the call carefully and
 this time verifying with a byte-for-byte diff against the local source after download, not just
 a byte-count match — now the standard check for every control-file publish, not just base64
 ones.
- **AWT-0080 and AWT-0088 both closed on the Hub.** Minda asked "AWT-0088"; re-reading its `Raw/`
 proposal, it said "close `AWT-0088`... whenever you're ready" — which prompted checking
 Smartsheet rather than repeating the "no tool reaches the Hub" assumption written into rows 29
 and 30. Found the **Tasks & Requests** sheet (`8860839228606340`), real and reachable. Flagged
 the lane question to Minda first (the Hub is listed as Victoria's in §4; §5 bars writing to a
 system of record without an explicit human decision) rather than closing it unasked — Minda:
 "Yes, close it now." Both rows set to Status = Done with a Response summarising the work, Done
 date 2026-09-24. **The "outside Anna's reach" claim in rows 29 and 30 and their change-log
 entries was wrong** — the Hub was reachable via the Smartsheet connector all along, simply
 never tried. Standing note for future sessions: check Smartsheet for a Hub / Tasks & Requests
 sheet before writing anything is outside Anna's reach.


## Snapshot (2026-09-25)
- **FC2611 — Ian Newcombe's reply actioned.** Quote accepted ("PO to follow"), but Macdonald want
 supervisor plus three shopfitters rather than two; RAMS and operative names requested. Minda:
 "Yes, accept supervisor plus 3." Revised total **£40,470.00 excl VAT** (+£9,480 on the same rate
 basis as the original quote). RAMS drafted from Fishbone's own template (`Fish Bones RAMS.docx`)
 via python-docx (this session's sandboxed LibreOffice could not render `.docx` to PDF for visual
 proofing — verified instead by reading every table back programmatically); asbestos row flagged
 **NOT YET CONFIRMED**, not signed off, since no survey was sighted in the tender documents. Team
 named by Minda: Mindaugas Gaudiesius (site manager), Andrejus Prutkovas, Sebastian Pabis, Dainius
 Drulia (shopfitters). **First real Gmail draft created this session** — reply confirming price,
 names and the December Rolex CPO visit staying separate; Minda to review and send, Anna has no
 send access. RAMS sent to Minda but **not yet filed to Drive**. **Man A / site manager confirmed
 by Minda 2026-09-25: Mindaugas Gaudiesius** — matches what was already drafted into the RAMS.
 **Revised pricing confirmed no cost sheet needed** — Minda: "email confirmation should be
 enough," 2026-09-25. No Excel/cost-sheet document required for the £40,470.00 figure.
- **§1 connectors corrected — Gmail read/draft access was already real.** Minda asked directly
 whether Anna had email access with draft creation; correct, and it had already been used minutes
 earlier in the same session without the contradiction to §1's own "No Gmail" line being caught.
 Same pattern as the 2026-09-24 Hub-reachability correction. `CLAUDE.md` 11,692 B → 11,833 B;
 `Charter-History.md` 2,933 B → 3,701 B, both byte-verified and diff-verified.
- **Ledger publish required two corrections before it held**, worth flagging for future sessions:
 the first upload truncated a Gmail draft ID by one digit; the second, though copied directly from
 the verified local source, still returned with one byte-level corruption (an en dash's UTF-8
 bytes altered) despite matching byte count exactly. Neither error was visible without decoding
 the download and diffing byte-for-byte against source. The fix that held: verify the exact
 candidate content against source **locally** (a scratch-file `cmp`) before spending a Drive
 upload on it, then upload via `base64Content`. Full account in
 `change-log/change-log-2026-09-25-connectors-corrected-gmail.md`. Two defective interim ledger
 copies archived with reasons stated; nothing deleted.

## Snapshot (2026-09-26)
- **FC2611 RAMS overlap bug fixed.** Minda: text was overlaid/unreadable in the RAMS Minda had
 received. Cause: three pre-existing floating template shapes (`allowOverlap`), predating the
 2026-09-25 draft — a template defect, not Anna's edit. Also found: the live copy still had
 unfilled operative-name placeholders, since the named version was only ever sent to Minda, never
 uploaded. Fixed: shapes removed, title restored as body text, unused footnotes/numbering
 trimmed, all 22 tables verified unchanged.
- **RAMS filed to Collaboration Space** — closes the open filing question. Minda: "All documents
 for project should be placed in Collaboration Space." Checked the group Document Register
 directly rather than assuming from folder contents: highest FC number in use was **FC0000026**,
 so next was **FC0000027**, not FC0000024 as folder contents alone would have suggested. RAMS
 moved (native Drive move, same file id) from a generic Downloads folder into Anna's own `Raw/`
 as the Source key, then copied natively into Collaboration Space `FC2611/Documents` as
 `FC0000027 - Project-RAMS - Fishbone RAMS Goldsmiths Bullring brand removals Breitling Rolex
 CPO.docx`, byte-identical (36,399 B), no manual transcription either side. Registered: Entity FC,
 Direction Internal, Category `Project-RAMS`, Status Draft.
- **Fourth and fifth transcription incidents of the ledger's own history, same lesson again.**
 Publishing rows 34–35 to the ledger repeatedly failed before it held: a first `create_file` call
 rejected the payload outright as invalid base64 (a stray character from manual chunk
 concatenation); a second returned success but at roughly half the expected byte count, traced to
 the Read tool silently truncating a 36,132-character single-line file at its own display cap
 (~25,000 tokens) before the truncated view was ever pasted into the call; a third attempt pasted
 only the first of three source chunks. Fixed by reading the three ~12,000-character source
 chunks individually (each within the display cap, confirmed complete) and concatenating them
 directly into the call, then verifying the published file's byte count (27,098 B) and decoded
 content against the known-correct source. **Standing lesson: never trust a Read of a long
 single-line file without checking it wasn't truncated; split any base64 payload above roughly
 15,000 characters into chunks small enough for a full, untruncated Read before concatenating.**
- **FC2611 RAMS found corrupted; master template found to carry the wrong company name; both fixed
 by rebuilding as Google Docs.** Minda's screenshots showed the row-35 RAMS displaying
 overlapping/garbled text and generic drylining-trade hazard rows, then a genuine Word "experienced
 an error trying to open the file" dialog. Confirmed independently via `read_file_content`
 returning empty for both the `Raw/` and Collaboration Space copies — genuinely corrupted, traced
 to the prior session's raw-XML edit (row 34). Separately, the pristine, untouched master template
 (`Fish Bones RAMS.docx`) was found to carry the wrong company name throughout its running headers
 — "Fish Bone Drylining" / "Fish Bone Frylining" / "Fish Bone Drylning" — a template-level defect
 predating any of Anna's edits. Minda: "Company name is Fishbone Construction Ltd." Chose to fix
 the template and rebuild the RAMS now. **A sixth transcription incident**, distinct from the
 truncation lesson above: rebuilding the `.docx` via python-docx + manual base64 failed five times
 running, root-caused via a local `cmp` to hand-reproduction of large `.docx` ZIP boilerplate
 silently drifting onto a *different* corrupted file's bytes examined earlier in the session —
 invisible without byte-level diffing before any Drive upload. Reported transparently; **Minda:
 "build it in google docs."** Both documents rebuilt as clean HTML authored fresh and uploaded via
 `create_file` with `contentMimeType: text/html`, letting Google's converter produce native Google
 Docs — sidesteps binary transcription entirely. Master template republished
 (`1g6-i-0mJlfL58njo2GutnzzueicwENAaiKOJtmLsGPo`, all fields blank, company name fixed, verified
 zero "Drylining" occurrences); old `.docx` archived in place. FC2611 RAMS rebuilt
 (`1y2_60WhUE2A8Vn80NBZ3urrOd9AlUhwpID0VnveOEWg`) with all known facts restored and site-specific
 hazard wording lost to the corruption marked `[SITE-SPECIFIC WORDING NOT YET RESTORED]` rather
 than invented; copied natively into Collaboration Space (`19fjTCt5OzepWQz0V852iNcRFvGnO0fDJskjUMsCu8sc`),
 replacing the archived corrupted copy. Document Register row FC0000027 updated (Source key, File
 link, Description, Location); Status left at Draft pending the site-specific review. **Standing
 lesson: for any future document of this kind, author as clean HTML and let Google's converter
 build the native Doc, rather than hand-assembling or hand-transcribing binary Office XML.**
- **Afternoon: duplicate live ledger archived.** The 07:47 half-length publish attempt above (18,066 B,
 cut off mid-row 29) had been left live beside the correct 10:37 copy. Archived on Minda's instruction,
 re-listed before and after; one live ledger. **Third duplicate-control-file collision** in Anna's home —
 same cause as 2026-09-22's two (a publish not followed by a re-list). → AQ-14.
- **`CLAUDE.md` adopted and mirrored to git** — `minda-ui/Anna`'s first commit, `125d8e1`, byte-identical
 (11,833 B, decoded from Drive's download, not retyped). Branch `claude/loving-gates-8bcu4a`; not yet in
 `main`. "Adopt Charter.md" declined: the only such file is **Nadia's** (Amfa Sales & Ops, standalone
 today, AWT-0104) — another assistant's home, outside Anna's lane.
- **Record audit.** This file said 24 change-log entries; the folder held 28. Counts said 8 open
 questions; the table holds 7. Ledger had a blank line splitting its table at rows 33/34 — closed.
 **Rows 34–36 (this morning) have no change-log entry** — flagged in
 `change-log/change-log-2026-09-26-duplicate-ledger-archived-and-charter-mirrored.md`, not back-filled.

## Pending
- **Minda (AQ-14):** should §6 require re-listing the home folder immediately before creating or
 replacing anything? Two collisions on 2026-09-22 came from one stale listing; a third (duplicate ledger) found and archived 2026-09-26. A §6 change, so raised not taken.
- **Minda (AQ-11):** the Collaboration Space FCP folder carries **seven writers**, two of them
 consumer mailboxes, all able to modify or delete the filed 049-25 documents. Intended?
- **Minda / Victoria (AQ-12):** the Construction KB's §4b still says its access has "not yet been
 checked" — disproved 2026-09-22, but correcting it is outside the AWT-0077 sanction.
- **Minda / Eugene (AQ-13):** that KB's git mirror was stuck at `CLAUDE.md` **v10** before
 2026-09-22, and its `archive/README.md` manifest is stale since 2026-09-05. Does the mirror need a
 reconciliation pass?
- **Minda / Victoria (AQ-8):** the estate-law broadcast sits unprocessed in that KB's `Raw/`.
- **Studio Structure (AQ-4b):** drawing note 5 specifies **BS 5950**, the calcs are to
 **BS EN 1993**. The last open question on 049-25.
- **Eugene:** SessionStart PDF-toolkit hook on `minda-ui/Anna` (repo now has one commit, `CLAUDE.md` only).
- **Minda:** merge `claude/loving-gates-8bcu4a` into `main` (needs a PR); mirror `Charter-Rules.md` and
 `Charter-History.md` too?
- **Minda:** retrospective change-log entry for rows 34–36 (none was written)?
- Next charter change: add a **Nadia** row to §4 (Amfa questions → Nadia); name the Hub, Collaboration
 Space and Document Register in §4/§5, since Anna already writes to all three on instruction.
- Fold the real Collaboration Space share list into **§5b** on the next charter change.
- **Setting-out note, not a flag:** the ×43 ridge is ~3.6 mm deeper than the ×37 — check ridge
 setting-out, padstone bearing and tight-fixed finishes before fabrication.
- **Minda:** the rebuilt FC2611 RAMS (Google Doc `1y2_60WhUE2A8Vn80NBZ3urrOd9AlUhwpID0VnveOEWg` /
 Collaboration Space copy `19fjTCt5OzepWQz0V852iNcRFvGnO0fDJskjUMsCu8sc`) still needs its
 `[SITE-SPECIFIC WORDING NOT YET RESTORED]` hazard cells reviewed and completed before it can move
 from Draft to Issued — flagged in the document itself, repeated here so it isn't missed.
- Whether to trash the stray Google Doc copy (`1Q4QH8KHOFlWxXTBsLMCfY5WYS-DHevplhRYSwXOkVhY`) that
 Google auto-created in Minda's own Drive when she opened the old broken file to view it — not yet
 resolved.

## Not Anna's, but live
**Task T00003** — the ownership conflict. FCP holds the freehold, Fishbone Properties the 125-year
leasehold, and the 049-25 document client reads "Fishbone Properties". Document attribution is
settled (FM); the underlying conflict is not.

## Counts
Reference articles: 2 · Logged queries: 1 · Open questions: 7 open / 9 resolved ·
Sources: 7 external (ASRC-1–7) + 5 internal · Raw items held: 2 ·
Documents filed to Collaboration Space: 4 · Register cells written: 24 across 6 rows ·
Files written in the Construction KB: 5 (+1 git commit) ·
Change-log entries: 29 · Ledger rows: 37 (plus row 2a)

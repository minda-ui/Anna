# Anna — current state

| Field | Value |
|---|---|
| Last session | 2026-10-07 |
| Status | **Live.** Charter split 2026-09-23 into `CLAUDE.md` (core), `Charter-Rules.md` (5,527 B) and `Charter-History.md` — AWT-0080, §4 wording tightened 2026-09-24 (AWT-0088), §1 connectors corrected 2026-09-25 (Gmail read/draft was already real), **Composio fallback layer adopted into §1 2026-09-27** — `CLAUDE.md` now **12,008 B**, `Charter-History.md` now **4,486 B**, both byte-verified. AWT-0080/AWT-0088 both **closed on the Hub** (Tasks & Requests sheet `8860839228606340`) 2026-09-24 — the Hub turned out to be reachable via Smartsheet all along. Construction KB **write, bounded** — and written to. Collaboration Space **read/write** (filing). Document Register **write, on instruction**. **Gmail read and draft-create** confirmed real and in use (never send). Repo `minda-ui/Anna`: `CLAUDE.md` mirrored 2026-09-26, first commit `125d8e1` on branch `claude/loving-gates-8bcu4a`, **not yet merged to `main`**; `origin/main` separately now carries a `.claude/settings.json` (Minda-pushed 2026-09-27) granting unprompted `composio` execute/link/remove — not yet checked out into this session's own working branch. **Composio fallback connectors linked 2026-09-27**: `anna-googledrive` (Fishbone Construction Ltd Knowledge base) and `anna-gmail` (`info@fishboneconstruction.co.uk`), both verified read-only and both still bound by the same never-send / own-remit-only rules as the native connectors. |
| Record | Complete as of 2026-10-07. **37** change-log entries · ledger to **row 142** · 8 external sources + 5 internal · 7 open questions. Connectors now also `anna-gmail-properties` (28/09) and `anna-gmail-ops` (ops@fishboneconstruction.co.uk, 29/09). One routine: "Anna – Construction project email check" (created by Minda 29/09). Charter-Rules §0c: project emails only. |

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

## Snapshot (2026-09-27)
- **Composio installed, flagged, and linked as a fallback connector layer.** Minda ran the pinned
 `composio` CLI installer; the base CLI installed cleanly but the Claude Code plugin/skill install
 failed twice (`HTTP 403` on the pinned release tag) and was left unresolved — doesn't block using
 the CLI directly. Checked `Raw/` on request and found `2026-09-27_Proposal_Composio-Rollout.md`
 from Alex, asking that a brand-new `.claude/settings.json` grant **unprompted**
 `composio execute *` / `connections remove *` / `link *`, citing an approval attributed to Minda
 inside the file itself. Flagged this back rather than acting on a Drive document's own claim of
 authorization — `execute *` reaches 1,000+ integrated apps, `connections remove *` is destructive.
 Minda confirmed directly that she'd pushed the file; verified independently (not on her word alone)
 that `origin/main` genuinely carries it via `git fetch` + `git show`. This session's own working
 branch never checked that file out and no restart occurred, so whether the grant is live *here* is
 unconfirmed either way — moot in practice, since no permission prompt was ever hit running
 `composio` commands this session (`permission_mode: auto` throughout).
- **Logged in and linked two accounts**, each verified with one read-only call before any other use:
 `anna-googledrive` (`GOOGLEDRIVE_FIND_FILE`, no query) and `anna-gmail` (`GMAIL_GET_PROFILE`). The
 Drive verification call surfaced real bank-statement packs and another employee's own KB file —
 flagged immediately and paused rather than continuing to query. Minda confirmed this was expected:
 the connection is scoped to the whole "Fishbone Construction Ltd - Knowledge base," not just Anna's
 own space. Recorded for the future: broader technical reach doesn't change what Anna actually goes
 looking at — still confined to her own remit unless a task specifically calls for more, and that
 will be asked for explicitly rather than assumed from what a credential happens to be able to see.
 Gmail verified as the real `info@fishboneconstruction.co.uk` mailbox (66,110 messages).
- **Four reliability tests run on request, all passed, all cleaned up**: a small Drive edit; a
 255,085-byte Drive edit verified byte-exact against a locally-generated (not hand-typed) payload; a
 Gmail draft created with a genuine attachment, verified present via a full re-fetch, never sent; and
 a find→download→size-check→remove pass using that same draft's own attachment (deliberately chosen
 over any real correspondence) — downloaded, size checked via `wc -c`/`stat` only, content never
 opened, local copy then deleted. The test draft was later deleted from the real mailbox on Minda's
 instruction and confirmed gone (`GMAIL_GET_DRAFT` on it now 404s). Two minor field-naming
 inconsistencies hit across different `GOOGLEDRIVE_*` tools (`file_id` vs `fileId`) — not failures,
 just worth checking each tool's schema rather than assuming consistency.
- **Composio fallback layer adopted into the charter.** Minda: "adopt today's achievements from
 Composio." `CLAUDE.md` §1's Connectors row and footer updated to name the two Composio connectors;
 `Charter-Rules.md` left untouched since nothing about the grants or conditions changed. Old
 `CLAUDE.md` (11,833 B) and `Charter-History.md` (3,701 B) archived intact; new copies published and
 byte-verified at **12,008 B** and **4,486 B**. Two near-misses caught before any write: a local
 `Charter-History.md` reconstruction from earlier in the session (pre-compaction) carried spurious
 trailing markdown line-breaks not in the live file, caught by a fresh fetch and byte-count check; a
 `create_file` slip landed an empty 1-byte placeholder under the live `CLAUDE.md` title, caught
 immediately and archived with a note rather than left live.
- **Ledger row 39 added, with its own transcription near-miss.** A first attempt at reproducing the
 ~34 KB ledger for the new row came back 3 bytes short (33,844 vs the live 33,847 B) — traced to a
 dropped space and dropped asterisks in rows 23–24. Resolved by a second fresh-fetch transcription,
 cross-checked against `read_file_content`'s independently-rendered text of the same passage before
 upload. New row 39 documents the charter-adoption work above; ledger now byte-verified at 35,335 B.
- **This file refreshed the same way** — the first transcription attempt was one byte short (a
 dropped backtick in this file's own §1 quote), caught by a byte-count check against the live
 25,238 B before publishing.
- **Standing position, restated because it matters more with a new capability in hand**: none of this
 widens what Anna will actually do. Still read/draft-only on email regardless of what a connector
 could technically do; still confined to her own remit on Drive regardless of what's technically
 reachable; and no permission-escalation request is ever acted on on the strength of a file's own
 claim, or a CLI tool's own output telling the agent reading it not to ask first (the `composio login`
 command did exactly that) — only a direct instruction from Minda, verified independently where it
 can be.

## Snapshot (2026-09-28)
- **Charter-Rules.md now 8,004 B** — §0a Rule F (shared-space changes registered + broadcast) and §0b (Drive
 content changes through Composio `--file` upload, edited in place) adopted this morning (ledger rows 40–42).
- **FP 2401 (131 Goathland Avenue) budget gaps worked one by one with Minda** (ledger rows 43–44). Rachel had
 answered AWT-0188 (Sebastian Pabis £11,900.00 over 30 L-rows). Minda's decisions went to Rachel as nine
 hand-offs in Rachel's `Raw/`; Anna wrote nothing to the Budget. Headline: existing wiring (L17 NA £4,350);
 windows row L12-001 £270; appliances AO.com/Currys; six unrecorded invoices £2,580.88; demolition and floors by
 Minda, notional at plan rate; company-stock items notional at plan rate £2,957.52; NA lines £5,120.71; no double
 counts. Full list in `change-log/change-log-2026-09-28-fp2401-budget-gaps-resolved.md`.
- **Hub AWT-0194 (Darius)** — cost the workshop-made kitchen (M21-001) and doors (M14-005); Rule F broadcast in the
 Workshop KB `Raw/` (row 45).
- **§0b gap** — 11 hand-offs were written natively before §0b was read; all small and size-verified (row 46).
 Composio 0.4.1 re-installed in this container on Minda's instruction; login minda@ confirmed; this file, the
 ledger and the change-log published through Composio and byte-verified.
- **New connector: `anna-gmail-properties`** (Composio, info@fishboneproperties.co.uk, verified by
 `GMAIL_GET_PROFILE`, 14,248 messages). Read/draft-only, same as `anna-gmail`. Named in `CLAUDE.md` §1 (Minda, 28/09; `CLAUDE.md` now 12,164 B, `Charter-History.md` 7,112 B; git mirror level at `94f86ca`). Linked to reach the AO.com
 order emails for FP 2401.
- §3 flags on FP 2401: EICR is not an installation certificate; standard board in wet areas, tanked from stock
 (check the kit accepts it); load-bearing walls and joist replacement are a structural engineer's call.

## Snapshot (2026-09-29)
- **FC2612 Merry Hill (night Thu 1 Oct):** Minda sent the reply to Michelle 05:50 with quote FC0000043 and a PO
 request — FC0000043 now **Issued**. RAMS completed from the Merry Hill permit #693953, induction pack and the
 Styccobond F41 SDS; signed off by Minda; filed and registered **FC0000044**, sent to Michelle 06:19 — **Issued**.
 Site checklist page (claude.ai artifact RxRudQ4wHmFkuSRUp8hvrb, v5) updated with the Merry Hill and WOSG booking-form
 rules. Oak's RAMS accepted by Michelle.
- **FC2611 Bullring (nights 5–29 Oct):** RAMS rebuilt for the job as a draft (Anna `Raw/`), asbestos closed
 (Michelle, 29/09). Revised price found in ops@: **FC0000046**, £40,470.00 excl VAT, supervisor + 3 — registered,
 Issued; **FC0000023 Superseded**. Hub AWT-0199 and AWT-0200 (Rule F).
- **Charter:** §0c project emails only; §1 `anna-gmail-ops`; §7 the email-check routine. git to 4c83e77; control files and change-logs synced to `main` via minda-ui/Anna#4 (c1bad61).
- Slip, fixed at once: a one-row ledger upload briefly replaced the Drive ledger; restored and verified.
- **Sebastian's CSCS card** (scan in Anna `Raw/`, expires end Jan 2028) renamed `FC2611 - CSCS - Sebastian Pabis - exp 01.2028.pdf`;
 attached via Composio to a draft reply to Michelle (r-5936341689578722610, attachment 785,913 B = Drive); **sent by Minda 09:39 UTC**. **Composio re-logged
 in** (minda@) after the session started with it down. Native Gmail read **info@fishboneconstruction.co.uk** this session, not
 ops@fishboneproperties.co.uk as §1 says — to check (ledger row 62).
- **Operative Competence Register created** (Minda): Smartsheet sheet 461912032806788 in the Fishbone Construction Ltd workspace +
 Drive folder `FC Operative Competence` (10PqTtIHMose94ARu_xJAGpQchSjki1SP, minda@ only). OC-0001 = Sebastian's CSCS. Hub AWT-0203;
 Rule F notes to Victoria and Peter. Personal data — never to git, Collaboration Space or the Financial Archive (row 64).
- **Charter-Rules §0d — project drawings** (Minda): `Drawings/` + `Drawings/Archive/` in each Collaboration Space project folder;
 superseded revisions moved to Archive. Applied to FC2611 (4) and FC2612 (1). Hub AWT-0207 (row 65).
- **Drawing Register** (Smartsheet sheet 8400729582733188, Fishbone Construction Ltd workspace): DR-0001–DR-0005. **Charter-Rules §0e**:
 Anna replaces her own unsent draft (new first, then delete); `CLAUDE.md` §5 exception. FC2612 RAMS Rev 1 signed and filed. Hub AWT-0208 (row 66). **FC2609** (Merry Hill Rolex Pre Owned) folder + 7 drawings, DR-0006–DR-0012 (row 67).

## Snapshot (2026-09-30)
- **Email check, every email read** (Minda: project mail comes from anyone — SC-7). Bullring deliveries: Scoppio via Core 11, bays 18/19/20,
 offload only, no booking; Michelle sending instructions. Michelle gave Scoppio the site manager email misspelt (`fishboneconstuction`) —
 correction sent by Minda to Tony (cc Michelle) 11:32 UTC (row 79).
- **FC2612 PO received:** Macdonald PO 513, £2,243.50 excl VAT, matches FC0000043 — registered **FC0000047** (Project-PO, new category), Hub AWT-0215,
 notes to Rachel and Peter (rows 77–78).
- **FC2611 Bullring pre-start pack** (David Burke via Michelle): filed to Anna `Raw/` and FC2611 `Documents/`; Minda's Site Supervisors Pass
 and three induction passes pre-filled (SU706–SU707, Core 11); pass and pack signed by Minda 30/09; reply with both signed PDFs **sent by Minda 15:42 BST** (row 90). Hub AWT-0221 (rows 81–82, 88).
- **Michelle's Site Manager expectations** (all Macdonald sites): everyone signs Macdonald RAMS + induction + site rules; no phones in work area; PAT stickers —
 added to the FC2612 checklist (v7, row 84) and the Bullring RAMS.
- **FC2611 drawings:** DR-0013 WoS DD-Set V1 (Current), DR-0014 MJL hoarding Rev A (Superseded by Rev C). Hub AWT-0222 (row 83).
- **FC2611 RAMS DRAFT 30.09.26** (Anna `Raw/`): site rules from the pre-start pack; now **rev e**: skips via AWS Nationwide, Minda arranges exchanges (row 93); hoarding spec and steel posts are Macdonald's — Fishbone builds / installs (rows 92, 94); nearest A&E Queen Elizabeth Hospital Birmingham, confirm at induction (row 95); **no open items**.
- **Charter-Rules §0g** (Minda): every project email gets a reply draft, to the sender only. Replies to David 'Re: Merryhill' and 'Re: Bullring' sent by Minda 14:14 BST (rows 86–87); awaiting his answer on hoarding Rev C and the fire rating.

## Snapshot (2026-10-02)
- **FC2612 Merry Hill — snags after the 1 Oct shift** (WoS / Goldsmiths via Michelle): counter drawer won't close (lock side dropped), tower/pod facing the wrong way, carpet lifting. Return visit **Monday 5 Oct**, before the Bullring start; five attending (Minda, Andrejus, Dainius, Oleg Vysochan, Sebastian); unit weights asked from WoS. Reply sent 14:56 BST (rows 96–97). Site checklist page was not used on the night.
- **FC2612 return visit papers** (row 99): permit #694239 (5–9 Oct) + induction pack, WOSG booking form (**Mon 5 Oct 21:00–05:00**, 5 named) filed to FC2612 `Documents/`; Hub AWT-0269. Minda decided (row 101): **Merry Hill 20:00, then Bullring 22:00**; draft asks Michelle to move the booking to 20:00 — awaiting her answer.
- **FC2611 Bullring programme** (row 125): Macdonald draft programme Rev E received 06/10 and filed (row 129): Scoppio from 20 Oct, TAG cases 12–13 Oct, RCPO furniture in the New Year, hand back 29 Oct a.m. **Fishbone night programme** (phone page, row 130): https://claude.ai/artifact/LejvgVSR2XGWcaWYiEEaVT — 15 Mon–Thu nights × 4 operatives; crew-facing (Macdonald checks removed, row 131), shared by link.
- **Hublot strip-out** (row 136): client instruction via David 06/10 — destroy all Hublot unitary/millwork with photo evidence; **keep 3 chairs + 1 desk in the showroom**. Reply draft to David `r-666823765088231422`. Programme page nights 6 and 7 Oct now say to keep them (row 137). Bullring permits renamed date-first (row 138). Open: photo evidence to David after strip-out; a stray private copy of the programme page (https://claude.ai/artifact/4EqER8FynAqaxU4FYLvFBX) for Minda to delete or keep.
- **FC2611 drawings** (row 140): checked against email; DR-0016 and DR-0017 added; nothing newer arrived, so nothing archived. Ian's 23/09 Dropbox folder checked 07/10 (row 142): two PDFs, both already held; nothing new.
- **End of day 06/10** (row 141): permit-rename Rule F done (AWT-0378). SC-15–20 adopted into project-admin. **Fixed links:** crew programme https://claude.ai/artifact/LejvgVSR2XGWcaWYiEEaVT (always publish with `url`). First tomorrow: Minda sends the Hublot reply to David; ask Macdonald for the steel post positions before Mon 12 Oct. (Ian's Dropbox folder: done 07/10, row 142.)
- **Lathams order, Sales Order 3398720** (rows 126–127, 132–135): pro forma £143.34, paid by Minda 06/10. ST19 board and 23 mm edging accepted by Minda. Remittance sent by Minda 06/10 21:21: it asks for the VAT invoice, and says the order is collection only, Fri 9 Oct pm (no one on site to accept a delivery). Pro forma and payment confirmation handed to Rachel's `Raw/` (AWT-0376). Open: Steven to confirm collection; the VAT invoice (to Rachel's `Raw/` when it comes). **Rule (Minda 06/10): all financial documents go to Rachel's `Raw/`.**
- **FC2611 Bullring:** Rado furniture removed by the brand's contractor (Ian Copley, Refined Installations) Mon 5 Oct evening — **confirmed by Minda** (row 102); reply draft to Michelle; **RAMS DRAFT 06.10.26 rev g** (Anna `Raw/`, `1vK2e3klZtsLgDBV6pdEskfKfXi_qwZyU`) supersedes rev f (adds window graphics removal + hoarding adjustment, row 119); **Minda: "Rams are good"**; copy to Eugene `Raw/` (AWT-0352, row 121) as the sample for **Eugene's RAMS digital-signing system** (row 124); still to sign and file.
- **New skill `file-attachments`** (row 100): Raw first, work there, copy where it belongs.
- **FC2612 invoice FC0238 issued** (rows 104, 106): PO 513, £2,243.50, domestic reverse charge; sent by Minda 05/10; Document Register FC0000048 (Rachel); AWT-0303 Done. Return visit not charged.
- **FC2612 Macdonald draft manual handling assessment** (row 122): received 06/10, in FC2612 Documents; Fishbone comments **sent 06/10**; Michelle: it's a generic assessment, she'll review with the maker's advice (row 123). A site-specific method is needed for the next visit.
- **FC2612 maker's method** (row 106): adjust the MDF-carcass feet from inside the cupboard (pump wedges at the corners); no parts removable; moving = 4–6 people onto a dolly or pallet truck. Drawing 5282 Rev C = DR-0015.
- **FC2611 permits** (row 106): Hazwork fire isolation WP-1293-61514–61521 (nights 5/6–12/13 Oct), access across the mall WP-1293-61303 (5–11 Oct, 22:00–05:00), in FC2611 Documents; **all approved** (Michelle, 06/10 07:24). Later nights need further permits; **WP-1293-61524 (13–14 Oct) and WP-1293-61526 (14–15 Oct), then WP-1293-61527–61530 (to 18/19 Oct), added 06/10** (rows 117, 120, 122). **Tonight (06/10): Fishbone removes window graphics 2 and 3 and adjusts the hoarding to close a ~70 mm gap** (Minda; not in RAMS rev f). Skip now Wednesday 7 Oct.
- **New skill `weekly-invoices`** (row 104): Sunday night hand-off to Rachel for Monday invoices; **routine to be created by Minda** (spec in the skill §7).
- **Victoria's site-pack hand-off** (row 105): AWT-0265/0266/0268 In Progress, AWT-0267 Done.
- **Standing step (Minda, row 98):** get unit weights before any job that moves units — `project-admin` §4.
- **Michelle's site instructions (1–2 Oct):** protect all surfaces; no plasterboard, cable or carpet in skips; progress photos to her every morning.
- **FC2611 Bullring:** 12-yard skip booked by Michelle for Mon 5 Oct (AWS Nationwide, £520); across-the-mall hours from 22:00.

## Pending
- **FC2612 Merry Hill — return visit Mon 5 Oct (Merry Hill 20:00, Bullring 22:00; booking change to 20:00 asked of Michelle, sent 03/10, no answer yet):** **double tank ~350 kg** (Phil, 05/10; towers not confirmed) — mechanical handling, Michelle asking Redd Retail for fixing details and method; Merry Hill RAMS needs the method (row 103); checklist and thank-you to Michelle wait on the time; Merry Hill RAMS Rev 2 for the visit (5-person lift, Oak for the lit tower, re-orient, carpet re-fix) — Minda to decide; Oleg Vysochan not yet on RAMS / Operative Competence Register; booking form with Michelle; after-shift photos to Michelle.
- **FC2612 Merry Hill (1 Oct shift):** RAMS **FC0000044 Rev 1** (permit #694111, Control Room call) signed, filed and **Issued** — sent to Michelle
 only at 17:38 on 29/09 (FC0000044 Rev 1). Site checklist v7 (30/09: Macdonald site rules). PO received 30/09 — **FC0000047** (PO 513); materials-collection line and category `Project-PO` confirmed by Minda (row 80). Minda to share the site
 checklist with Sebastian (edit access for photos); photos of finished work to Elisha Spencer before 08:00 on 2 Oct;
 after the shift Anna writes the before/after report for Macdonald; old Gmail draft r7089415217151689627 still in
 Drafts (Minda's call).
- **FC2611 Bullring:** RAMS draft waits on the Bullring permit / site rules (Michelle preparing) and the engineer's
 steel post design (§3 — MJL Steels Rev A received 29/09 is a fabrication drawing, not an engineer's design; Rolex to confirm location); then Minda reviews and signs; register it (supersedes FC0000027 in substance). Sebastian's
 CSCS card sent to Michelle 29/09. PO for FC0000046 awaited. **Pre-start (30/09):** pass signed and sent to Michelle, David Burke and Bullring technical 15:42 BST; hoarding Rev C confirmed by David (reply sent 17:32 BST, row 91); fire rating is Macdonald's responsibility (Minda, row 92); check with Bullring whether dusty work needs a fire alarm isolation permit (their pre-work sheet says no deactivation);
 Bullring induction with all operatives Mon 5 Oct (latest slot 15:30), then Minda countersigns the three induction passes and sends them to
 technical.assistant@bullring.co.uk; permits via Invida, 1 working day notice; RAMS DRAFT 06.10.26 rev g (all open items closed; Rado by others; graphics removal added) — Minda to review and sign; confirm the A&E at the induction.
- **Skills:** `project-admin` (row 71, merged in #10) and `end-of-day` (row 74, merged in #11; first run 29/09, row 75).
- **Skill candidates** (§0f): SC-2, SC-4 adopted into `project-admin` 29/09; SC-3 (after-shift report), SC-5 (operative docs), SC-7 (read every email by content), SC-8 (.doc forms via Composio convert) and SC-10 (items supplied by others: their design, our install) open; SC-9 adopted 30/09 (project-admin §5). §0e amended 30/09: never repair a draft — delete the old one first, then create the new (row 89).
- **Drawing Register:** originators of the FC2609 set (designer job 4599) and the WoS A2 pack's source to verify; Tissot GA revision date to read.
- **Operative Competence Register:** check OC-0001 (Sebastian, reg. 2519687) on CSCS Go Smart; add the other three
 operatives' cards (Mindaugas, Andrejus, Dainius) when Minda has them.
- **Routine:** Minda to read the 08:29 test-run report; if Composio was missing, Eugene to add it to the environment
 setup script.
- **FP 2401:** Rachel to enter the nine hand-offs; Rachel to say whether Sebastian's days include the kitchen fit;
 appliances: AO order AOL223024414 (22/06, £910 ex VAT) is this house — paid on Minda's personal credit card (booking is Rachel's); the Construction £454 AO payment is 28 North Terrace; AO £359 (18/06), Currys £363 (24/06) and two April oven orders held for Minda to check (ledger row 47); cooker hood and washing machine not yet bought; Fishbone Waste
 invoice not yet issued (Waste recorded as dormant — flagged to Rachel); Darius AWT-0194; CEF FC2603 and NT Steel
 misfiled in the Construction KB `Raw/FP 2401_131 Goathland Avenue/`.
- **Minda:** the stray, unnamed `INITIALIZING` Composio Drive connection (`googledrive_tute-sassy`,
 from a first `link` attempt that hung with no browser available) never completed OAuth and holds no
 live credential, but its interactive removal prompt doesn't accept piped input in this non-interactive
 shell — left in place, harmless. Worth clearing next time a human is available to confirm it.
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
- Whether to trash the stray Google Doc copy (`1Q4QH8KHOFlWxXTBsLMCfY5WYS-DHevplhRYSwXOkVhY`) that
 Google auto-created in Minda's own Drive when the old broken file was opened to view it — not yet
 resolved.

## Not Anna's, but live
**Task T00003** — the ownership conflict. FCP holds the freehold, Fishbone Properties the 125-year
leasehold, and the 049-25 document client reads "Fishbone Properties". Document attribution is
settled (FM); the underlying conflict is not.

## Counts
Reference articles: 2 · Logged queries: 1 · Open questions: 7 open / 9 resolved ·
Sources: 8 external (ASRC-1–8) + 5 internal · Raw items held: 2 ·
Documents filed to Collaboration Space: 4 · Register cells written: 24 across 6 rows ·
Files written in the Construction KB: 5 (+1 git commit) ·
Change-log entries: 35 · Ledger rows: 131 (plus row 2a) · Register rows added 30/09: FC0000047; updated: FC0000043 · Register rows added 29/09: FC0000044, FC0000046; updated: FC0000043, FC0000023

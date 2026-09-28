# Anna — open questions (AQ-<n>)

A resolved question gets a **Resolved** line; it is never deleted.

## Open

| ID | Opened | Question | Status |
|---|---|---|---|
| AQ-1 | 2026-09-22 | Should Anna eventually run a periodic **regulations-watch** routine? Routines are created by Minda via the form (§6a). | Open — deferred |
| AQ-4b | 2026-09-22 | **049-25 standard clash.** Drawing note 5 specifies steelwork to **BS 5950** (workmanship to BS 5950-2) while the calculations are to **BS EN 1993**, S355, EXC2. BS 5950 was withdrawn in favour of the Eurocodes; fabrication and erection now sit under BS EN 1090-2. Studio Structure's document. | Open — engineer to confirm |
| AQ-8 | 2026-09-22 | The estate-law v1.4 broadcast sits **unprocessed in the Construction KB's `Raw/`** (`1HytscaQ324rywJxxcMU4M1ElaK4_V2Jg`). That KB processes its own `Raw/` via its §2b workflow. Anna's job under §5a, or that KB's own next session? | Open — for Minda / Victoria |
| AQ-11 | 2026-09-22 | **The Collaboration Space share list is wider than "domain-wide".** `Fishbone Commercial Properties Ltd` (`1F3qKwvnENAXQdtrtJcZ_M3SbVik6IMVS`), which `FM2202` inherits from, carries **seven writers**: the whole `fishboneconstruction.co.uk` domain, `andrej@` and `lana@`, `alexey.glukhov@aggaservices.co.uk`, `irina@fishboneproperties.co.uk`, and two **consumer mailboxes** — `agga.services@gmail.com`, `sveta_usurt@yahoo.com`. All **writer**: each can modify or delete the filed 049-25 documents. Is that share list intended? Sharing is the owner's to change. Charter §5b still uses the estate-law note's narrower phrase — fold the detail in on the next charter change. | Open — for Minda |
| AQ-12 | 2026-09-22 | **The Construction KB's §4b still says its data access has "not yet been checked."** Anna checked it — owner-only, no domain share. Correcting §4b is a §4 change the AWT-0077 sanction did not cover, so it was left and recorded in that KB's own change-log entry. Correct it? | Open — for Minda / Victoria |
| AQ-13 | 2026-09-22 | **The git mirror was a version behind before tonight, and its archive manifest is stale.** `minda-ui/Fishbone-Construction-Ltd` still held `CLAUDE.md` **v10** — Drive's v11 of 2026-09-11 was never mirrored, so tonight's push jumped it v10 → v12. Separately, `archive/README.md` reports the Archive listing as "counted 2026-09-05, nine files" and has not been updated since. Both pre-date this session. Does the mirror need a reconciliation pass, and who owns it? | Open — for Minda / Eugene |
| AQ-14 | 2026-09-22 | **Should §6 require re-listing Anna's home folder immediately before creating or replacing anything in it?** Two collisions happened today from the same cause: a session listed the home folder once at 11:59 and trusted that listing for hours while the 12:35 session was writing into it — producing **two live `processed-items-ledger.md` files** and **two `Archive/` folders**. Both are resolved, neither cost data, but the second was pure luck (the duplicate `Archive/` was empty). The Fishbone Construction Ltd KB learned the same lesson on 2026-09-09 and wrote it into its own `kb-registers.md`. This is a §6 change, so it is raised rather than adopted. | Open — for Minda |

## Resolved

| ID | Opened | Question | Resolution |
|---|---|---|---|
| AQ-2 | 2026-09-22 | Drive **read** access to the Fishbone Construction Ltd KB and Collaboration Space company folders. | **Resolved 2026-09-22 — both tested and working.** |
| AQ-3 | 2026-09-22 | Does "authority to Construction KB" mean read-and-cite only, or also write? | **Resolved 2026-09-22 — both.** Charter §4, §5, §5a. Scope later bounded by AWT-0077. |
| AQ-4a | 2026-09-22 | **049-25 ridge section.** Drawing schedules **B1 = 254×146×43 UB**; the calc package also holds **254×146×37**. | **Resolved 2026-09-22 — owner ruling (Minda): not an issue.** The drawn section is the heavier of the two, so building to the drawing exceeds what the calculation demanded — conservative. The reverse would be the serious case. **Residual, not a safety point:** the ×43 is ~3.6 mm deeper (259.6 vs 256.0 mm) — check ridge setting-out, padstone bearing and tight-fixed finishes before fabrication. Dimensions per SCI P363 / Tata Steel Blue Book (ASRC-7). |
| AQ-5 | 2026-09-22 | Test Collaboration Space access so the 049-25 filing follow-up can be actioned. | **Resolved 2026-09-22** — readable; filing done, see AQ-7. |
| AQ-6a | 2026-09-22 | The Construction KB's §4b says its data access was **never reviewed**. | **Resolved 2026-09-22 — review run, and it is owner-only.** KB root, `Raw/` and `Raw/Finance/` each return minda@ (owner) and nothing else. The §4b text itself is still uncorrected — carried to AQ-12. |
| AQ-6b | 2026-09-22 | **The Construction KB's `CLAUDE.md` did not name Anna as a writer**, and its §4c makes §4 a deliberate edit. | **Resolved 2026-09-22 — recorded, on Minda's sanction (AWT-0077).** New `Wiki/Decisions/2026-09-22-anna-construction-adviser-write-access.md`; `CLAUDE.md` v11 → **v12** with new §4d; `Wiki/index.md` re-issued; that KB's change-log entry and `kb-registers.md` rows written; mirrored to git as commit `3df6a7b`. Every file byte-verified. Anna's first write into another KB. |
| AQ-7 | 2026-09-22 | Do the two 049-25 PDFs go into the Collaboration Space? | **Resolved 2026-09-22 — yes, on Minda's instruction.** `FM2202 - 2 Ferndale Avenue/Documents/` created (policy v1.3 §3/§7); both PDFs copied in as **FM0000013** and **FM0000014**. Entity confirmed **FM** by Minda. |
| AQ-9 | 2026-09-22 | Category `Property-Structural`, and the Document Register File link still pointing at `Raw/`. | **Resolved 2026-09-22 — Minda: category correct, update the link.** Register rows 233/234 repointed; Source keys, IDs, Status, Entity and the voided FP rows untouched. |
| AQ-10 | 2026-09-22 | FM0000013's register **Description** still said *"reconcile with engineer"* about the ridge section AQ-4a had closed. | **Resolved 2026-09-22 — Minda: "Fix it please."** Retracted in place, not deleted (house rules §7 rule 2). Sheet version 88 → 89. |

*Withdrawn 2026-09-22:* the "Newcastle vs Wallsend" address flag — the property is Wallsend, Studio
Structure is based in Newcastle; the filename carries the engineer's location. And the title-block
date-order flag — an unverified text-extraction artefact, not a finding.

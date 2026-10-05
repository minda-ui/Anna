---
name: weekly-invoices
description: Anna's Sunday-night invoice hand-off to Rachel. Every Sunday night, list every Fishbone Construction job finished that week (Monday to Sunday) that has a PO or agreed price and has not been invoiced, gather the invoice details for each, and pass them to Rachel so the invoices can go out on Monday. Also use the same steps for a one-off invoice request ("send an invoice to …", "send all information to Rachel"). Adopted 2026-10-05 on Minda's word.
---

# Weekly invoices: Sunday night to Rachel, invoices out on Monday

Minda, 05/10/2026: "we need to send an invoice to Macdonalds for Merry Hill works, and send all information to
Rachel. Save it as a skill; every Sunday night, we need to send all information for invoices that need to be
sent on Monday from that week."

This skill is the **how**. The rules it follows are in the charter: `CLAUDE.md` §4 (finance is Rachel's), §5
(Anna never sends email and never commits a company), `Charter-Rules.md` §5b (financial documents) and §0a
Rule F. If anything here differs from the charter, the charter wins. Tool details are in the
`project-admin` skill. Write everything plain-brief (Rule C).

**Anna gathers the information; Rachel drafts the invoice; Minda sends it.** Anna never makes or edits the
invoice, never sets VAT or CIS treatment, and never sends anything.

## 1. When

- **Sunday night**, for invoices going out on **Monday**. The week runs Monday to Sunday.
- **One-off**, whenever Minda asks for an invoice ("send an invoice to …"): same steps, for that one job.
- Anna cannot create the Sunday routine herself (§6a). Minda creates it from the routines form, using the
  spec in §7 below.

## 2. Which jobs go on the list

Minda's rule (05/10/2026): **jobs finished that week with a PO or an agreed price, not yet invoiced.**

1. Go through the week's record: ledger rows, change-logs, `current-state.md`, the project emails, and the
   Document Register (`7352854736144260`) for POs (`Project-PO`) and quotes.
2. A job is on the list when all of these are true:
   - its work was **finished** that week;
   - there is a **PO** or a written **agreed price**;
   - it is **not invoiced yet**. Look for a QuickBooks "Invoice FC…" email to the customer and earlier
     hand-offs to Rachel.
3. **Flag, don't list:** finished work with **no PO or agreed price**; work that is only part-finished
   (Minda decides on interim invoices); and any return visit or extra work. A snag return is **not charged**
   unless Minda says otherwise.
4. If nothing qualifies, still tell Minda: "no invoices this week", and list any flags.

## 3. What to gather for each job

Read the PO and the quote. Take the details from the documents themselves, not from memory.

| Item | Where from |
|---|---|
| Customer: legal name, address, company no., VAT no. | The PO |
| Where invoices go (e.g. `accounts@…`) | The last QuickBooks invoice email to that customer |
| Their PO number, date and who issued it | The PO (Document Register ID) |
| Our job number and name, and the site address | Project folder, PO |
| Works date(s) and confirmation the works are finished | Ledger, change-log, site record |
| Description | **Exactly as the PO words it** |
| Net amount, plus the VAT shown on the PO | PO, checked against the quote |
| Our quote reference | Document Register (quote ID) |
| Anything **not** to be invoiced | Minda's decisions |

If the PO and the quote differ (amount, scope, a line like "collection of materials"), stop and ask Minda
before the hand-off.

**Rachel's to check, never Anna's to settle:** VAT treatment (including the CIS **domestic reverse charge**
when the customer is a contractor, not the end user), CIS deduction, the invoice number and payment terms.
Name these as questions in the note.

## 4. The hand-off to Rachel (§7a, add-only)

1. Write **one note** for the week, `Anna to Rachel YYYY-MM-DD - invoices for Monday DD.MM.YY.md`
   (for a one-off: `Anna to Rachel YYYY-MM-DD - invoice request - <job> <customer PO>.md`). Put one table per
   job, then "for you to check", then "not on this invoice", then the source rows.
2. **Cite documents by their register ID and Drive id. Never copy a PO or quote into the note.** Financial
   documents live in the Financial Archive only (§5b), and never in git.
3. Upload the note to **Rachel's `Raw/`** (`1NQydm_gONNSaVnRlYtPjhHmcTg5ZPl9-`) with Composio `--file`.
   Byte-verify it: `cmp` matches, no U+FFFD, and `£` is preserved.
4. Add a **Hub row** assigned to Rachel, Priority High, Status Open, naming the note.
   **Get the next Task ID from a filtered read** (`get_sheet_summary`, Task ID `GREATER_THAN` the last one you
   know), not from `find_in_sheet`. Find can miss rows, and other assistants add rows all the time
   (05/10/2026: AWT-0270 was already taken; this row became AWT-0303). If the Duplicate column flags the
   row, renumber it at once.

## 5. Record it

- One ledger row per hand-off (a summary only; the note and the PO stay out of git).
- A change-log entry and a `current-state.md` line: "invoice info to Rachel, AWT-nnnn, awaiting her draft".
- Git: the ledger, change-log and current-state only.

## 6. Tell Minda

Tell her which invoices are with Rachel and the amounts, what was flagged and why, and what Rachel was asked
to check. When Rachel's draft comes back, Minda reviews it and sends it from QuickBooks or by email. Anna can
draft the covering email (§0g), but **never sends it**.

## 7. Routine spec (for Minda to paste into the routines form)

- **Name:** Anna – Sunday invoice hand-off
- **When:** Sundays, 20:52 UK time (`CRON_TZ=Europe/London 52 20 * * 0`)
- **Prompt:** "Anna: run the weekly-invoices skill for the week just ending (Monday to today). List every job
  finished this week with a PO or agreed price that has not been invoiced; gather the invoice details; write
  one hand-off note to Rachel's Raw/ with a Hub row; flag anything with no PO, part-finished, or extra work;
  record it; and leave Minda a summary. Draft only: never send email, never make the invoice."

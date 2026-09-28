# Change log — 2026-09-23 — Sourcing Register reviewed; proposal written and revised; FC2611 row added

Minda: "We have Shopping sourcing register, this is where we register projects... I am more than
happy to get feedback that's need to be added." Then: "Go ahead."

## What was done

Reviewed the Shopping Sourcing Register (Smartsheet, workspace "2. Sourcing"). Found six defects
worth fixing:

1. `Rate per sq m` has no error guard — `#DIVIDE BY ZERO` on any row without an area (confirmed on
   the Goldsmith Nottingham row).
2. `Internal ID` blank on every pre-existing row, despite the column's own description requiring it
   for `Potential` status.
3. Client name spelled two ways across this register and the Document Register.
4. Ray and Scott Guernsey row is a five-to-eight-times outlier (£3,440/m²) with no flag.
5. `Contact Details`, `Postcode`, `Project Address` blank on all four pre-existing rows.
6. `Type of works` (Light/Medium/High) undefined — no test given for what separates the three.

Wrote these up, with three picklists proposed (Scope, Shift, Premises) and two close-the-loop
columns (Final account, Actual nights/days), in `Reference/Proposal-Estimating-System-Register-Improvements.md`.

Added the FC2611 row to the register (Status Potential, `Type of works` = Medium, assigned by
analogy and flagged as such in the row note — a live example of defect 6).

## Revision

Minda: "I don't like idea of Type of Works = light, medium and heavy. Do you have any ideas?"
Answer given: facts cannot be reconstructed later, labels can — capture Scope/Shift/Premises/Work
type now (all facts), defer the Light/Medium/High classification decision to roughly twenty real
rows of data, and drop the scale rather than redefine it. Offered a Finishes-only/Alterations/
Structural fallback if a single field is wanted, mapped to Classifier sections 15–21/9/7.

Minda: "Yes, update please." Proposal re-issued as **revision 2** — item 6 rewritten, new section
added, first issue's "define the scale better" option explicitly withdrawn rather than silently
dropped.

## Filed

- `Reference/Proposal-Estimating-System-Register-Improvements.md` — archived (superseded, rev 2)
  and recreated, 10,057 B, byte-verified.
- Shopping Sourcing Register (sheet `1756532255623044`) — FC2611 row added at v22, version 24 after.

*Anna — AI Construction Assistant.*

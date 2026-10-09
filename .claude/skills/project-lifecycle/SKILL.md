---
name: project-lifecycle
description: The stages every Fishbone Construction job goes through (Enquiry, Quoted, Ordered, Set-up, On site, Handover, Snagging, Closed, or Lost), with a checklist for each stage, who acts (Anna, Rachel, Peter, Eugene, Minda), and how the Project Register row is updated. Use when a job starts, moves stage, or when Minda asks where a job stands or what is missing. Adopted 2026-10-09 on Minda's word ("we need to establish core of our project management").
---

# Project lifecycle: from enquiry to closed

Minda, 09/10/2026: "we need to establish core of our project management". This skill is the **how**: one
list of stages, a checklist per stage, and the register update that marks each move. The rules are in
`CLAUDE.md` and `Charter-Rules.md`; the procedures it calls are in `project-admin`, `file-attachments` and
`weekly-invoices`. If anything here differs from the charter, the charter wins. Write everything plain-brief
(Rule C).

## 0. The spine: the Project Register

- **Where:** Smartsheet, Fishbone Construction Ltd workspace, sheet `5250912102778756`.
- **One row per job.** The key is the **FC number** from QuickBooks (Minda). Never guess a number.
- **Lead assistant** owns the row and keeps it current. On construction jobs the lead is **Anna**.
- **Money columns are Rachel's** (Minda, 09/10): quote, PO, extras, invoiced and paid values, Money notes and
  Invoice status. **Anna never writes an amount.** Anna writes the references (quote ref, PO ref).
- **Every move of stage** = update Stage, Health, Next action / owner / due on the row, plus a ledger row.
- **Name the job everywhere:** every Hub row, `Raw/` note and email subject about a job starts with or
  contains its FC number.
- **Health:** Green = on plan; Amber = something open that could slip (missing PO, unsigned RAMS, permit
  not yet approved, a dispute); Red = work is blocked or a date will be missed. Say why in Notes.

## 1. Enquiry

Trigger: a client asks for a price or sends drawings.
- [ ] Minda gives the FC number (QuickBooks project). Add the register row: Stage **Enquiry**, client,
      end client, site, contacts (names and roles only).
- [ ] File every drawing received (`project-admin` §3: original name, register, check dimensions).
- [ ] Note what is asked, the dates wanted, and any site rules already known.
- [ ] **Unit weights** if the job moves units (`project-admin` §4): ask in the first reply.
- [ ] Questions to the client → drafts for Minda (never sent by Anna).

## 2. Quoted

Trigger: Minda's quote goes out.
- [ ] Quote filed and registered in the Document Register; its id in **Quote ref**.
- [ ] Hand the quote to Rachel's `Raw/` if it carries money detail she needs (she fills Quote value).
- [ ] Stage **Quoted**; Next action = "await order", owner = client, due = the date they gave, if any.
- [ ] Lost (client declines, or Minda says so) → Stage **Lost**, one line why in Notes.

## 3. Ordered

Trigger: a PO, or a written agreed price (Minda's word counts).
- [ ] PO filed and registered (`Project-PO`); its id in **PO ref**. Check it against the quote: scope, amount,
      lines such as "collection of materials". Any difference → ask Minda before going on.
- [ ] Copy to Rachel's `Raw/` (she fills PO value). Peter registers it if it came through triage.
- [ ] Stage **Ordered**. No PO yet but work is booked → Health **Amber**, Next action "PO from <client>".

## 4. Set-up (before the first shift)

- [ ] **Project folder** in C Projects (`project-admin` §2) with `Documents/`, `Drawings/`,
      `Drawings/Archive/`, `Pictures/`. Link in **Project folder**.
- [ ] **Drawings** complete and current; DR ids in **Drawings**.
- [ ] **Site rules and induction pack** read in full and filed (pre-start pack, permits, booking forms).
- [ ] **RAMS** (`project-admin` §4): built from the master template and the site papers; unit weights;
      items supplied by others are their design, our installation (§0h). **Minda reviews and signs**;
      signed copy issued to the client. State in **RAMS**.
- [ ] **Permits** (hot works, fire isolation, access): asked, approved and filed; dates cover every shift.
      List in **Permits / induction**.
- [ ] **Operatives:** names on the RAMS and booking forms; cards in the Operative Competence Register.
- [ ] **Programme / dashboard** from `templates/project-dashboard/` for a multi-shift job; link in
      **Programme page** (always republish with `url`). Bookings in the Work Calendar.
- [ ] **Logistics:** delivery bays, skips (who books, exchange notice), materials and collections.
- [ ] Stage **Set-up**. Anything unsigned or unapproved the day before → Health **Amber** and tell Minda.

## 5. On site

- [ ] Stage **On site** on the first shift.
- [ ] Every email check: anything for this job → its row's Next action; drafts to the sender only (§0g).
- [ ] Permits for the coming nights in place; RAMS revised when the method or hours change (new rev,
      Minda signs again).
- [ ] Progress photos as the client asks (e.g. Michelle: every morning), resized and named.
- [ ] Programme page kept to the real plan; extra work or changes → note them for Minda and Rachel
      (Extras).
- [ ] New drawings → `project-admin` §3 at once (newest in `Drawings/`, older to `Archive/`).

## 6. Handover

Trigger: work finished; the area is handed back.
- [ ] Final photos; handover email draft for Minda.
- [ ] **Invoice information to Rachel** on the Sunday after (`weekly-invoices`): finished, PO or agreed price,
      not invoiced. Extras listed separately for Minda to decide.
- [ ] Stage **Handover**; Health Green unless snags are known.

## 7. Snagging

Trigger: the client reports defects, or a return visit is needed.
- [ ] One line per snag in Notes: what, who reported, whose it is (ours, the maker's, others').
      Not ours → Minda's position goes to the client as a draft; never accept liability for her.
- [ ] A return visit needs the same papers as a shift (permit, booking, RAMS with the method).
- [ ] Return visits are **not charged** unless Minda says so.
- [ ] Stage **Snagging**, Health **Amber** while any snag is open.

## 8. Closed

Trigger: all work done, snags closed, and Rachel shows the job **Paid** (or Minda says so).
- [ ] Every document and drawing filed; registers show Issued / Current / Superseded correctly.
- [ ] Programme page: last version kept (no deletion).
- [ ] Stage **Closed**, Health Green, Next action empty; one ledger row.

## 9. Who does what (proposal with Victoria, Hub AWT-0493)

| Stage | Anna | Rachel | Peter | Eugene | Minda |
|---|---|---|---|---|---|
| Enquiry / Quoted | row, drawings, questions | quote value | triage to the lead | — | number, quote, decisions |
| Ordered | PO ref, checks | PO value | registers the PO | — | confirms the order |
| Set-up / On site | folder, RAMS, permits, programme, photos | — | documents | RAMS signing system | signs RAMS, sends emails |
| Handover / Snagging | invoice info, snags | invoices | — | — | decides charges, positions |
| Closed | closes the row | paid | — | — | — |

Until Victoria agrees part of this with each assistant, treat their columns as requests, not orders.

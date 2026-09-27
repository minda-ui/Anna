# Change log — 2026-09-22 — duplicate live ledger found; source register brought current

Newest notes at the top. Append-only (`CLAUDE.md` §8).

---

## 2026-09-22 (evening) — two live copies of `processed-items-ledger.md`

Minda asked whether today's work was documented. Checking rather than answering from memory found
a defect in Anna's own record.

**What went wrong.** Between 12:35 and 22:00 there were **two live `processed-items-ledger.md`
files** in Anna's home folder:

| Drive id | Size | Written | Rows |
|---|---|---|---|
| `19nZkr6RisfTikXKx4ukA8JhylSFD3Gkg` | 1,005 B | 12:35 | 1–3, its own numbering |
| `1VRV4sVOQrBQPxkNOJQERo4Cws8SxiuUy` | 3,190 B | 19:52 | 1–8 |

The 19:52 session listed the home folder only at **11:59** — before the 12:35 copy existed — and
never re-listed it. So when it did archive-then-recreate it archived the 11:46 original and
published its own copy *alongside* the 12:35 one, which it had never seen. Neither copy was lost;
both were live, which is worse for a file whose job is to be the reprocessing guard.

**The irony is worth recording.** The Fishbone Construction Ltd KB's own `kb-registers.md` carries
exactly this warning after its 2026-09-09 collision: *"If a third concurrent write happens again,
check for more than one live `kb-registers.md` before trusting a single read of this file."* Anna
ran that check diligently **in that KB** earlier this evening, and never ran it in her own.

**Resolved.** Both copies archived, each titled with its reason — neither deleted. One merged
ledger published, carrying every row to date. **Numbering follows the 19:52 copy**, because the
change-log entries already cite those row numbers (rows 1, 4 and 7 are referenced by name); the
12:35 copy's row 3 appears as **row 2a**. The merged file opens with a standing note describing the
collision and instructing the next session to check for a single live copy before replacing it.

**Rows 9–19 added**, closing an eleven-row gap: the owner rulings, the estate-law adoption, the
FM2202 filing, the entity-attribution ruling, both Document Register writes, the access review, the
AWT-0077 adoption, the three stale-citation corrections, the Construction KB session, and this
entry.

## 2026-09-22 (evening) — `source-register.md` brought current

Untouched since stand-up at 11:46 — two rows, while `current-state.md` had carried "register the
049-25 documents" as pending all evening. Six sources added:

- **ASRC-3** BS EN 1993 (Eurocode 3) and the design suite the 049-25 calculations use.
- **ASRC-4** BS 5950 (withdrawn) and BS EN 1090-2 — the AQ-4b clash, flagged not resolved.
- **ASRC-5 / ASRC-6** the Studio Structure 049-25 calculations and drawing, located by register ID
  and filed path, with §3 and the drawing's own governing notes recorded against them.
- **ASRC-7** UB section dimensions (SCI P363 / Tata Steel Blue Book), the basis of the AQ-4a ridge
  comparison — cited so the figure is checkable against the tables rather than against Anna.

A second section was added for **internal** group sources, which are cited constantly and whose
*version* matters but which are not external references and so take no ASRC number: the House Rules
(v1.3), the numbering policy (v1.3), estate law v1.4 §7b, the Construction KB's `CLAUDE.md` (v12)
and the group Document Register. The House Rules row carries the standing instruction to check the
live version, with today's two-release drift as the reason.

---

*Anna — AI Construction Assistant. Change log, append-only (`CLAUDE.md` §8).*

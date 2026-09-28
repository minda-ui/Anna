# Change log — 2026-09-22 — addendum: a second 12:35 collision, an empty duplicate `Archive/`

Newest notes at the top. Append-only (`CLAUDE.md` §8). Addendum to
`change-log-2026-09-22-ledger-collision-and-source-register.md`; that entry is not edited.

---

## 2026-09-22 (evening) — the same collision had happened twice

The verification sweep run immediately after resolving the duplicate ledger found a **second
instance of the identical fault**: two folders named `Archive` in Anna's home.

| Drive id | Created | Contents |
|---|---|---|
| `1T-smughqF3lWXH--5gx1y8JMpLDYQufE` | **12:35** | **empty** |
| `14rT79fELV6CDWpYuoT90NFXcmWJ-NfhZ` | 14:51 | every archived file — 20+ items |

Same root cause as the ledger: the 12:35 session created an `Archive/` folder; the later session
had listed the home folder only at 11:59, did not see it, and created its own at 14:51 when it
first needed to archive something. The charter's §6 tree names `Archive/` but carries no id for
it — control files are referenced by filename, not id (§6) — so nothing forced a lookup.

**No content was split.** The 12:35 folder was created and never used; everything archived today
went into the 14:51 folder. The hazard was prospective, not actual: two identically-named folders
in the same parent, one of which a future session could file into, silently splitting the archive
and breaking the "`Archive/` listing is the file's own changelog" property §6 relies on.

**Resolved without deleting** (§5 bars deletion; archive instead). The empty folder is renamed to
carry the warning in its own title — `Archive (EMPTY DUPLICATE - do not file here; the live Archive
is the folder created 2026-09-22 14:51, id 14rT79fELV6CDWpYuoT90NFXcmWJ-NfhZ ...)` — so the hazard
is legible from the folder listing alone, which is the same principle §6 applies to archived file
names.

**The pattern, for the next session.** Two collisions in one day, both from the same cause: a
session listed Anna's home once, early, and then trusted that listing for hours while another
session was writing into the same folder. The Construction KB learned this on 2026-09-09 and wrote
the rule into its own `kb-registers.md`. Anna should carry the equivalent: **re-list the home
folder immediately before creating or replacing anything in it**, not once at the start of a
session. Raised as **AQ-14** rather than written into the charter unilaterally — it is a §6 change
and belongs to Minda.

---

*Anna — AI Construction Assistant. Change log, append-only (`CLAUDE.md` §8).*

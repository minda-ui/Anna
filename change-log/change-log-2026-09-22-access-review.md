# Change log — 2026-09-22 — access review run (AQ-6)

Newest notes at the top. Append-only (`CLAUDE.md` §8).

---

## 2026-09-22 (evening) — Drive access review, on Minda raising AQ-6

The Construction KB's own `CLAUDE.md` §4b says its data access was **"not yet checked for this
knowledge base"** and warns *"do not assume the folder is owner-only."* Anna checked it.

**Fishbone Construction Ltd KB — owner-only, clean.**

| Folder | Permissions |
|---|---|
| KB root `13IQdim0JhKmoQvJBmJmnMhreJqg55xTr` | minda@ (owner). Nothing else. |
| `Raw/` `17yPHMXGWUtskM2GPSbTOc2kgLPLe9RCn` | minda@ (owner). Nothing else. |
| `Raw/Finance/` `1V4jM2huYpxJ8hWUJ0t2hRZL3X3GUIbKE` | minda@ (owner). Nothing else. |

`Raw/Finance/` holds the HSBC statements and subcontractor invoices that KB marks `sensitive: true`.
No domain share, no other users. The §4b warning is answered: it **is** owner-only. This is the
access review the sister KBs ran and this one had not.

**Collaboration Space — wider than "domain-wide" implies.** `Fishbone Commercial Properties Ltd`
(`1F3qKwvnENAXQdtrtJcZ_M3SbVik6IMVS`), which `FM2202 - 2 Ferndale Avenue` inherits from and which
therefore governs the two PDFs filed this evening, carries **seven writers**:

- `fishboneconstruction.co.uk` — the whole domain, as **writer**
- `andrej@fishboneconstruction.co.uk`, `lana@fishboneconstruction.co.uk` — domain accounts
- `alexey.glukhov@aggaservices.co.uk` — other domain
- `irina@fishboneproperties.co.uk` — sister company
- `agga.services@gmail.com` — **consumer mailbox**
- `sveta_usurt@yahoo.com` — **consumer mailbox**

All **writer**, not viewer: each can modify or delete what is filed there.

**This does not make the filing wrong.** Policy v1.3 §3/§7 puts property-tied documents exactly there;
v1.4 §7b bars only *financial* documents; Minda authorised it. But the estate-law note's phrase
"shared domain-wide" understates the actual list — two personal consumer mailboxes and two outside
domains also hold write access. Raised as **AQ-11**; sharing is the owner's to change, not Anna's.

**Effect on AQ-6.** The access half is closed and the answer is reassuring. The second-writer half is
narrower than first framed: with the KB owner-only, the only collision risk is between Anna and that
KB's own sessions, which §5a already handles. What remains is that the KB's `CLAUDE.md` does not
mention Anna at all — a line naming her as a second writer belongs in its §4, and its §4c says §4 is
"revisited deliberately, not silently rewritten". Not Anna's to slip in.

---

*Anna — AI Construction Assistant. Change log, append-only (`CLAUDE.md` §8).*

# Anna — charter history

Append-only dated log of changes to `CLAUDE.md` (core) and `Charter-Rules.md`. Newest entry at the
top. Never edit a past entry; correct it with a new one.

---

**2026-09-29 — Project drawings rule (§0d).** Minda: "Let's make it as rule. Download all drawings for project
into Drawings folder under project. Create Archive folder inside, as soon new revision of drawings arrived, old one
needs to be moved to archive." Prompted by Macdonald's steel drawing for FC2611. New `Charter-Rules.md` §0d:
`Drawings/` and `Drawings/Archive/` in each Collaboration Space project folder; only the current revision stays in
`Drawings/`, older ones are moved to `Archive/`. First applied to FC2611 (4 drawings) and FC2612 (1). `CLAUDE.md`
untouched. Edited in place through Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-29 — §7: first routine recorded.** Minda asked for Construction project emails to be checked every two hours,
06:00–18:00, Monday to Friday. Anna cannot create routines (§6a), so she wrote a paste-in spec; Minda chose option B and
created it herself in the routines form: "Anna – Construction project email check" (trig_014PjEdPWN5pBcxB5rzFhY1T),
cron `CRON_TZ=Europe/London 55 5,7,9,11,13,15,17 * * 1-5`, fresh session per run, push notifications. §7 "None yet"
replaced with this entry. Edited in place through Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-29 — §1 connectors: `anna-gmail-ops` added.** Minda: "connect to ops@fishboneconstruction.co.uk". The
revised FC2611 Bullring price (25/09/2026) was sent from that mailbox, which Anna could not read. Linked through
Composio and verified with `GMAIL_GET_PROFILE` as ops@fishboneconstruction.co.uk (754 messages). §1 also now records
that the native Gmail connector reads ops@fishboneproperties.co.uk (found this session). Same read/draft-only and
project-only (§0c) rules. Edited in place through Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-29 — Email: project topics only (§0c).** Minda: "you need to work through email only on topics
that are related to projects", then "let's do". Prompted by the morning inbox check, which summarised
payroll, HMRC, mortgage, pest-control and security-alert mail. New `Charter-Rules.md` §0c: mailbox work
covers project emails only; anything unclear is named in one line and asked about. `CLAUDE.md` untouched.
Edited in place through Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-28 — §1 connectors: `anna-gmail-properties` added.** Minda: "add anna-gmail-properties to
CLAUDE.md §1". Linked this session through Composio to reach the AO.com order emails for FP 2401; verified
with `GMAIL_GET_PROFILE` as info@fishboneproperties.co.uk (14,248 messages). §1 Connectors row now names each
Composio Gmail link with its mailbox; footer updated. Same read/draft-only rule — never send. `Charter-Rules.md`
untouched. Edited in place through Composio (§0b) and byte-verified; `CLAUDE.md` mirrored to git.

---

**2026-09-28 — Drive file edits via Composio adopted (§0b).** This session's own republish of
`processed-items-ledger.md` (the Rule F entry above) failed six times running via hand-typed
`textContent`/`base64Content` — the native `create_file`/`update_file` tools' only option, and the
same size/transcription risk earlier rows and Alex's own `HL-0005` had already hit at smaller scale.
Found that Composio's `GOOGLEDRIVE_UPLOAD_FILE --file <path>` / `GOOGLEDRIVE_UPLOAD_UPDATE_FILE --file
<path>` stage a local file's actual bytes directly, and `GOOGLEDRIVE_DOWNLOAD_FILE`'s signed URL can
be `curl`-ed straight to disk for verification — eliminating manual transcription on both the upload
and the download side. Republished the ledger byte-exact on the first attempt this way, then ran two
escalating reliability tests Minda requested (in-place edits up to ~2 MB, byte-verified via `cmp`).
Added as new `Charter-Rules.md` §0b. `Charter-Rules.md` 6,516 B → 8,004 B; `Charter-History.md` 5,524
B → 6,570 B; both byte-verified.

---

**2026-09-28 — Rule F adopted (shared-space changes broadcast and registered).** Alex's `/Raw`
hand-off `2026-09-27_Handoff_Rule-F-Shared-Space-Broadcast-Register.md` proposed an estate-wide rule:
any change to a shared system (a Hub Smartsheet, a shared Drive structure, or any space more than one
employee reads from) is not finished until it is both registered on the Hub and broadcast via Raw/ to
every employee it affects — being within one's own authority to make the change is never grounds to
skip either half. Quoted an owner ruling attributed to Minda inside the file; flagged this back rather
than acting on the file's own claim, confirmed directly with Minda before adopting. Added as new
`Charter-Rules.md` §0a (Rule F, next to Rule C), sourced from Alex's KB and the owner ruling.
`Charter-Rules.md` unchanged in scope elsewhere; `CLAUDE.md` untouched (no identity/role/authority/
structure impact). `Charter-Rules.md` 5,527 B → 6,516 B, byte-verified. Hub row AWT-0144 (Anna) closed;
both Raw/ notes archived.

---

**2026-09-27 — Composio fallback layer adopted.** Linked Composio as a fallback connector layer
alongside the native Drive/Gmail connectors: `anna-googledrive` and `anna-gmail`, same read/draft-only,
own-remit rules apply. A `/Raw` proposal from Alex asking for broad, unprompted Composio execution
permissions (a `.claude/settings.json` grant) was flagged and not acted on unilaterally; Minda's own
push to `origin/main` was verified independently before proceeding. Ran and passed four reliability
tests: a Drive file edit, a larger Drive file edit, a Gmail draft with attachment, and a Gmail
attachment download with size-check and removal; the test draft was deleted afterward. §1 reworded to
add the Composio connectors. `CLAUDE.md` 11,833 B → 12,008 B, byte-verified.

---

**2026-09-25 — §1 connectors corrected: Gmail read/draft was already real.** Minda asked "Anna you
should have access to email, with the option to create a draft. Am i right?" — correct, and it had
already been used earlier the same session (reading the Ian Newcombe thread) without the
contradiction being caught. §1's own "No Gmail" line was wrong: §5 already permitted drafting for
a human ("drafting for a human is fine"), and the tools were live. §1 reworded to "Google Drive +
Web + GitHub + Gmail (read and draft only — never send; see §5)." Same pattern as the 2026-09-24
Hub-reachability correction — a documented limitation that had never actually been tested against
the tools available. `CLAUDE.md` 11,692 B → 11,833 B, byte-verified.

---

**2026-09-24 — §4 wording tightened (AWT-0088).** Minda's estate-wide authority audit found the §4 lane table described the Construction KB grant as "nothing barred" — broader than the actual bounded §5a grant. Cosmetic only, no permission change, ruled by Minda: reworded to point to §5a's own bound (technical reference content, add-only, no finance). `Process-Estate-Authority-Boundaries.md` and the Authority Register already updated on the group side; only Anna's own wording was out of step. `CLAUDE.md` 11,635 B → 11,692 B, byte-verified.

---

**2026-09-23 — Charter split into core / rules / history (AWT-0080).** Alex (cross-KB channel,
Raw/-only hand-off HL-Helen-01) proposed splitting the monolithic `CLAUDE.md` (15,317 B) to avoid
reproducing the whole file as tokens for an ordinary rule change — the same pattern already adopted
in four other places this week (Alex's own charter, the group `CLAUDE.md`, Eugene's KB, a variant in
Rachel's). Directly relevant: a near-miss this session reproducing `processed-items-ledger.md`
(13,487 B) from an earlier base64 encoding introduced a transcription error, caught only by a fresh
fetch and byte-count check before anything was uploaded. Adopted on Minda's confirmation. Old
`CLAUDE.md` archived intact (15,317 B); `CLAUDE.md` (core), `Charter-Rules.md` and this file
published, each byte-verified.

**2026-09-22 — Estate law v1.4 §7b adopted** into what is now Charter-Rules.md §5b — financial
documents have one home (the Financial Archive), never the Collaboration Space, OneDrive or git.
Source: Victoria's §7a `/Raw` hand-off, FG-CR-0001 Accepted 2026-09-20.

**2026-09-22 — Construction KB write access granted** (Minda, confirmed on the second ask),
formalised by Victoria as Hub **AWT-0077**, building on AWT-0061 read access. Bounded to technical
reference content, add-only, cite-don't-restate, no finance — written up as what is now
Charter-Rules.md §5a.

**2026-09-22 — House Rules version corrected v1.1 → v1.3** in §5a — both Anna's charter and the
Construction KB's own control file had cited v1.1 since 11 September, missing §10 (Collaboration
Space & Smartsheet boundary) and §11 (related-party cross-linking). A live-version check was added
to the rule itself.

**2026-09-22 — Rule C (plain-brief writing) adopted** into what is now Charter-Rules.md §0. Source:
group `CLAUDE.md` §1, Hub Coordination Standard. Routed by Victoria as a §7a hand-off.

**2026-09-22 — Anna's charter authored and adopted.** Owner-authorised by Minda; built by Victoria;
repo mirror (`minda-ui/Anna`) scaffolded by Eugene. Status: authoritative from this date.

---

*Anna's charter history. Read alongside `CLAUDE.md` and `Charter-Rules.md`.*

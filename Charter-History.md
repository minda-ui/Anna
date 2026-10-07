# Anna — charter history

Append-only dated log of changes to `CLAUDE.md` (core) and `Charter-Rules.md`. Newest entry at the
top. Never edit a past entry; correct it with a new one.

---

**2026-10-07 — §0h: items supplied by the principal contractor.** Minda: "make 10 a rule" (SC-10). New `Charter-Rules.md`
§0h: for hoardings, steel posts and similar, design, specification, manufacture and structural or fire adequacy are the
supplier's; Fishbone installs to the drawings and fixing details supplied and asks when a detail is missing; Anna flags
TBCs and does not stand in for the supplier's designer. `project-admin` §4 carries a matching line. `CLAUDE.md`
untouched. No permission change.

**2026-10-07 — §6: `Templates/` folder added to the structure.** Minda: "Yes, add Templates to CLAUDE.md". `Templates/`
(id `16lK2li7UvgRzL1_yW5qj1M79rdpjWaYr`) holds reusable page templates; the first is the Project Dashboard (the FC2611 crew
page made generic; also in git at `templates/project-dashboard/`). Only the `CLAUDE.md` §6 tree and footer changed;
`Charter-Rules.md` untouched. No permission change.

**2026-10-07 — Mailbox lists brought level (Minda: "do all three").** `Charter-Rules.md` §0c now names all five mailboxes
(`anna-gmail`, `anna-gmail-ops`, `anna-gmail-properties`, `anna-gmail-minda`, native Gmail); `CLAUDE.md` §1 now says the
native Gmail connector reads info@fishboneconstruction.co.uk (it said ops@fishboneproperties.co.uk; wrong since at least
29/09, ledger row 62, confirmed 07/10); the `project-admin` skill's Gmail line and email-check step 2 include
`anna-gmail-minda`. No permission change.

**2026-10-07 — §1: `anna-gmail-minda` connector added.** Minda: "Let's connect you to minda@fishboneconstruction.co.uk",
then "add minda connection to CLAUDE.md". Composio Gmail account linked by Minda through the OAuth link; verified with one
`GMAIL_GET_PROFILE` call (minda@fishboneconstruction.co.uk, 22,569 messages), no mail read. `CLAUDE.md` §1 Connectors row
and footer updated. Same limits as the other mailboxes: read and draft only, never send, project emails only (§0c), no
deletes except Anna's own unsent drafts (§0e). Only `CLAUDE.md` §1 changed; `Charter-Rules.md` untouched.

**2026-09-30 — §0e: never repair a draft; delete the old one first.** Minda: "let's agree now, don't repair
drafts, create new ones and deleted old ones". A replacement draft for the Bullring pre-start reply carried the
old unsigned draft quoted underneath — Composio quotes the last message in the thread, drafts included. §0e now
says: never edit a draft in place; for a reply in a thread, delete the old draft first, then create the new one,
and check it quotes only the email being answered. `project-admin` §5 step 3 matches. Edited in place through
Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-30 — §0g: reply to everyone who writes to us, sender only.** Minda: "Create draft replies to David.
Make it as rule, we need to reply to everyone who coming to us only". New `Charter-Rules.md` §0g: every project
email gets a reply draft, addressed to its sender only — no reply-all or cc unless the email asks for it or Minda
does; short; Minda sends. `project-admin` skill §5 gains the step. Edited in place through Composio (§0b) and
byte-verified; mirrored to git.

---

**2026-09-29 — "Good night" starts the end-of-day skill.** Minda: "as soon as i write you 'good night' can we
trigger skill 'Have you documented today's work?'". New repo skill `.claude/skills/end-of-day/SKILL.md`: checks the
day's record (ledger, change-log, current-state, Rule F, registers, Drive = git), lists what is still open, then
brings the §0f skill proposals; read-only until Minda approves. §0f now names "good night" as the trigger and the
skill as the way it runs. Edited in place through Composio (§0b) and byte-verified; mirrored to git.

---

**2026-09-29 — §0f: updating skills, not only adding.** Minda: "Or updating skills with new learn things."
§0f's second option now reads "update an existing skill — add, correct or remove a step"; a skill always shows the
current way, with earlier wording kept in git history. Edited in place through Composio (§0b) and byte-verified;
mirrored to git.

---

**2026-09-29 — Skill candidates (§0f); new control file.** Minda: "would be great if collect data through the
day and at the end prepose things for creating skills." New `Charter-Rules.md` §0f: Anna logs repeated procedures,
slips, corrections and tool quirks as `SC-<n>` rows in a new home file, `skill-candidates.md`, and at the end of the
day proposes new skills, additions, rules or drops for Minda to decide. `CLAUDE.md` §6 tree and §8 list the new file;
footer updated. Seeded with SC-1 (Adopted: `project-admin`) and SC-2 to SC-5 (Open). Edited in place through Composio
(§0b) and byte-verified; mirrored to git.

---

**2026-09-29 — Project-admin skill added (procedures, not rules).** Minda: "everything we done today about
projects, would be great to use it in future. Is it worth to create skill?" — then "Yes, go ahead". New repo file
`.claude/skills/project-admin/SKILL.md`: the step-by-step how for email checks, project folders, drawings, RAMS,
drafts, registers, Rule F and record keeping. It adds no rule or permission; where it and the charter differ, the
charter wins. Noted in it: `.claude/settings.json` denies Composio `GMAIL_DELETE_*`, so §0e draft replacement uses
the native Gmail `delete_draft`. Charter files unchanged apart from this entry. Mirrored to git.

---

**2026-09-29 — §0d: every drawing registered.** Minda: "Yes" to adding the Drawing Register to the drawings
rule. §0d now says each drawing revision gets a Drawing Register row (status `Current`), and a superseded one is marked
`Superseded` with `Superseded by` when its file moves to `Archive/`. Edited in place through Composio (§0b) and
byte-verified; mirrored to git.

---

**2026-09-29 — Replacing email drafts (§0e); `CLAUDE.md` §5 exception.** Minda: "If you need to delete
draft, because you need it to replace, then delete it and create new." Prompted by two Merry Hill drafts in one
thread: the PO-only one was sent, the one carrying RAMS Rev 1 was discarded. New `Charter-Rules.md` §0e: Anna
replaces her own unsent draft by creating the new one, checking it, then deleting the old; never sent or received
mail, never someone else's draft; both ids reported and logged. `CLAUDE.md` §5 "delete or trash anything" now
names this as its sole exception; footer updated. Edited in place through Composio (§0b) and byte-verified;
mirrored to git.

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

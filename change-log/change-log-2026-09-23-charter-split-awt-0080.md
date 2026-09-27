# Change log — 2026-09-23 — Charter split into core/rules/history (AWT-0080)

Minda: "Anna check Raw folder." Found a new item, dropped 21:14 by Alex (cross-KB channel,
Raw/-only hand-off HL-Helen-01): a proposal (AWT-0080) to split Anna's monolithic `CLAUDE.md`
(15,317 B) into a stable core file, a `Charter-Rules.md` (the part that changes almost every
session) and an append-only `Charter-History.md`, so an ordinary rule change no longer requires
reproducing the whole file as tokens.

The timing was pointed: the exact failure mode the proposal targets — a big file reproduced
whole to make a small change, with real corruption risk — is what nearly happened an hour earlier
reconstructing `processed-items-ledger.md` from an old base64 encoding (caught before upload;
see this afternoon's ledger entries). Presented to Minda with a recommendation to adopt; confirmed.

## What was done

- Read the current `CLAUDE.md` in full and classified its eight sections: identity, remit, safety
  boundary, lane, top-level governance and folder structure/workflow into **core**; §0 (Rule C
  writing style) and §5a/§5b (the two standing grants with conditions — Construction KB write
  access, estate-law financial-document rule) into **Charter-Rules.md**, since both are exactly
  the kind of standing-rule content Alex's pattern describes.
- Extracted the "adopted on/by" facts already embedded in the prose into a proper
  **Charter-History.md**, newest entry first, one entry per dated adoption (charter authored,
  Rule C, House Rules version correction, Construction KB grant, estate law) plus today's split.
- Archived the old `CLAUDE.md` intact (rename + move, no re-upload — confirmed still 15,317 B,
  content untouched) and published the three new files, each byte-verified: `CLAUDE.md` 11,635 B,
  `Charter-Rules.md` 5,527 B, `Charter-History.md` 2,371 B.
- Cross-references updated in place: `CLAUDE.md` §4, §5, §7 and §8 now point to `Charter-Rules.md`
  and `Charter-History.md`; the folder tree in §6 lists both new files. Section numbering (§0, §5a,
  §5b) kept identical across the split so existing citations elsewhere (ledger, change-log) still
  resolve correctly.

## Not done

**AWT-0080 itself has not been closed** — no tool in this session reaches the Hub that task lives
in. Minda or Victoria would need to mark it Done from their side; this entry is the record of what
was actually decided and executed, to close it against.

## Filed

- `CLAUDE.md`, `Charter-Rules.md`, `Charter-History.md` — all in Anna's home
  (`1b0p62LxaX4C9H1cvK1R7K1KdX6-JcvoT`).
- Old `CLAUDE.md` — `Archive/`, titled with the reason.

*Anna — AI Construction Assistant.*

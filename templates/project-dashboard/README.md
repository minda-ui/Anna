# Project Dashboard — template

The crew page from FC2611 (Bullring), made reusable. One phone-friendly page: summary strip, deliveries,
skip status, then one card per working night, grouped by week. Built 2026-10-07 on Minda's word
("Save it as template for future used"). The live FC2611 page is `https://claude.ai/artifact/LejvgVSR2XGWcaWYiEEaVT`.

## New project

1. Copy `index.html` to the scratchpad. Replace every `[bracketed]` text:
   eyebrow, heading line, plan line, the four summary figures, Deliveries, the standing line at the bottom.
2. Skip status: edit the `skip` object near the end of the script (`stage` 1 = on site, 2 = exchange
   requested, 3 = date confirmed; `exchangeDate` stays `""` until confirmed by email). Delete the whole
   `<section class="skip">` block if the job has no skip.
3. Programme: replace the sample in `const weeks`. One object per week (`start` = the Monday), one per night
   (`d` date, `t` list of `[tag, text]`, optional `on` for others on site). Tags: `br` Scope A, `rc` Scope B,
   `at` attend others, `ms` milestone, `kp` keep or protect. Rename "Scope A/B" in `tag` and in the key.
4. Check it at phone width, then publish it as a **new artifact** (no `url`), and note the link in
   `current-state.md`. After that always publish with `url` (project-admin §4a).

## Rules

- **No capabilities.** The page is a public link for the crew, who are not signed in. A feature that needs
  Gmail or shared data goes on a separate private page (SC-26).
- Facts only from the project's own documents and emails. No prices, no personal data, no financial documents.
- Updating a live page: `Artifact read` the url, save `index.html`, edit by script, publish with `url`.

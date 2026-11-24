# Training — Разработчик интеграций (Integration Developer)

Mission role: glue for modules 03, 04, 05, and 06 — so data moves, leads are not lost, and vendors can be replaced.

## Business process

1. **Inventory what is already live** on the pilot (form, CMS, analytics, email, CRM). Read official privacy text and the page HTML. Do not assume a vendor named in a privacy policy is actually configured (example: WireReady’s public privacy page mentions Plausible, Resend, and Supabase “when configured”; the homepage HTML fetched 2026-11-23 did not include a Plausible script or JSON-LD).
2. **Technical access for AI crawlers** (Shestakov p. 26): confirm important content is visible without JavaScript; inspect `robots.txt` for `OAI-SearchBot`, `PerplexityBot`, `Claude-SearchBot`. Propose a change; **do not deploy** without Founder/owner yes.
3. **Lead intake**: one logged path from form to a record (spreadsheet or approved CRM). Dedup by email. Add “how did you hear about us?” (Shestakov p. 50). Human first-reply SLA (the module 04 draft used 5 minutes as a target — treat as a proposal, measure actual time).
4. **Qualification glue**: if a model is used, it reads only approved fields; PII policy in AGENTS.md applies; fallback = “manual review” when the model returns empty (the LiteLLM `free-chat` empty-content failure is documented in [INFRA.md](../../INFRA.md) and in the module-02 assessment).
5. **Analytics glue**: GA4 (or the approved property) plus CRM/form stages so module 05 can see qualified leads, not only sessions. Do not build a new analytics product.
6. **Vendor independence**: every integration has an owner, an export path, and a way to switch (CRM, tracker, email). NFAI must not resell the vendor.

## Services you master

robots.txt and crawler docs; GA4 / Search Console (after yes); one CRM when chosen (Kommo/Bitrix24 or other); site forms; LiteLLM router already authorized; later Rick.ai only if approved. Claude Code / Codex for implementation work already in the agency stack.

## Measurable outcomes

| Outcome | How it is measured | Pass |
|---|---|---|
| Inventory | Dated table: system, live or not, evidence (HTTP, screenshot, or HTML note) | No “assumed live” rows |
| Crawler readiness | robots.txt and a no-JS capture of key URLs | Findings filed; changes wait for yes |
| Intake reliability | Test lead: form → record, no duplicate, source field present | One test lead with a timestamped log (on a staging or approved path) |
| First-reply time | Clock from test inquiry to first response | Number recorded; target only if agreed |
| Model fallback | Forced empty/error path | Lead still appears as “manual review”, not dropped |
| Export | CRM or table can be exported | File produced without a vendor ticket |

## Acceptance test

- [ ] Inventory exists and matches a fresh check.  
- [ ] No production edit without a yes ID.  
- [ ] A test lead is traceable end-to-end or a blocker is written.  
- [ ] No keys in the public repo.  
- [ ] No PII in prompts sent to unapproved models.

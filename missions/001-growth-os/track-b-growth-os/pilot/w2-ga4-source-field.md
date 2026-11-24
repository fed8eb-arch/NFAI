# W2 — GA4 + source field (Marketing owner spec)

Version: v1.2 · 2026-11-23 17:18 PT · Head of Marketing · spend $0  
Status: owner part only (measurement plan, field wording, attribution, preview acceptance). Integration Developer implements on a Netlify preview; Marketing does not change the site, deploy, sign up, send, or publish.  
Brief: `mission-001/briefs/w1-w4.md` (commit `4858ba3`; worktree file hash matched that commit when read). This is the named Marketing + executor report path (brief lines 70–71), in the same folder as the Finance W4 protocol `pilot/w4-lead-flow-protocol.md` (v0.2, commit `981bdf2`). Executor evidence in §11 is left blank on purpose. Marketing has not edited the W4 file.

Pilot only: WireReady. Brand name is not confirmed by the Founder in the files cited below. Production deploy is out of scope for the 2026-11-24 14:00 PT preview deadline (brief lines 14, 57, 81). Live-site change still needs Бадди acceptance of the preview and the Founder's yes (`MISSION.md` rule 7, line 118; brief lines 16, 57, 175).

## 1. Scope and constraints

- Preview or branch deploy only. Do not merge to the production branch and do not publish to https://wireready-pilot.netlify.app (brief lines 57, 66, 83). Observed on 2026-11-23: production HTML sets `data-netlify-deploy-branch="main"` and `data-netlify-deploy-context="production"`. Do not copy the full site into this public repo (brief line 73).
- Legal consent text is a dependency before a public preview form is used (brief line 14). Legal owns `missions/001-growth-os/track-b-growth-os/pilot/w2-consent-text.md` (brief lines 65, 72; file present). Marketing does not write legal wording and does not invent a legal entity or support contact. If the GA4 tag is not installed (§8), do not put Legal’s Google Analytics sentences (`w2-consent-text.md` §1a second sentence and §1b) on the form — those sentences state that GA is in use. Use the inquiry-only notice and Legal’s preview fallback for the missing contact email (`w2-consent-text.md` lines 21–27). Ask Legal before production if a rewritten notice is needed.
- Mapping the field into HubSpot custom properties needs W1 and is not part of the 24.11 preview deadline (brief line 14). HubSpot Free allows 10 custom properties (`crm-lead-module-requirements.md` line 18; brief line 14).
- Any Google sign-in (GA4 property, Google account, tag setup, Search Console, etc.) is a STOP (brief lines 67, 83, 174). The source field still ships on preview without GA4. See §8 and `inbox/needs.md`. Measurement is field-only unless a GA4 property actually exists and the tag is installed.
- Spend remains 0. No paid Google, Netlify, or GA4 SKU (brief lines 83, 87).

## 2. Current production form (read-only, 2026-11-23)

Source: https://wireready-pilot.netlify.app/contact and its public bundle `app/(commercial)/contact/page-9327b8a7cbff4c9f.js`, fetched 2026-11-23; consistent with the brief inputs (line 61) and with `pilot/w3-lead-path.md` (commit `4f9f232`, lines 7–11): POST JSON to `/api/contact` → Resend, not Netlify Forms.

Existing visible fields (all `required`): `name` (label “Name”), `company` (“Company”), `email` (“Work email”), `location` (“Project city and state”), `phase` (“Project phase”; options Planning, Bidding, Construction, Expansion or retrofit, Other), `message` (“Scope and schedule”). Honeypot: `website` (label “Website”, `aria-hidden`, not required). Submit control: “Send project inquiry”. Notice on the form: “We use these details to respond to your inquiry. See our privacy notice.” (link to `/privacy` only; no consent checkbox — brief line 61).

The form POSTs JSON to `/api/contact` (`fetch`, `Content-Type: application/json`, body = form fields + `requestId`). This is not Netlify Forms (`w3-lead-path.md` lines 9–13). No `data-netlify` / `netlify` attribute and no `gtag` / `googletagmanager` / Plausible script were present in the fetched `/contact` or homepage HTML on 2026-11-23 (brief line 61; same observation as `track-b-growth-os/buy-integrate-build.md` line 49). There is no “How did you hear about us?” field today. Delivery, when configured, is Resend (`w3-lead-path.md` lines 17–21); whether the three Resend env vars are set in production was not verified (no Netlify account access).

Privacy notice https://wireready-pilot.netlify.app/privacy (same date): commercial inquiries are forwarded by Resend “when delivery is configured”; the product “is not yet connected to a production service”; a support contact is not yet added (brief line 61; risk 7, brief line 178). Quote, do not invent a support address.

## 3. Measurement plan

**Primary preview metric (leading, not a business result):** number of successful form submits on the preview in which the source field is filled with one of the keys in §4. This matches the brief example (line 64). A successful submit means the existing `/api/contact` (or the documented preview equivalent) returns success, the honeypot `website` is empty, and the source key is a listed enum value.

**Business metric (not claimed at preview, not replaced by the preview metric):** qualified inquiries (`MISSION.md` lines 36 and 119; brief W4 line 140). Intermediate metrics must not be presented as the result: AI share-of-voice, citations, positions, sessions (`MISSION.md` lines 32–33 and 119; brief lines 64, 136, 140). No GEO→profit or “visibility caused leads” claim (`MISSION.md` lines 43 and 119; brief lines 64, 136).

**After production go-live (W4, not this deadline):** follow `pilot/w4-lead-flow-protocol.md` (v0.2, commit `981bdf2`). Intermediate counts in the brief (line 143) and in that protocol §2: form submits; count and share by this source field; GA4 sessions and form-submit events only if GA4 is actually live; if CRM is connected, new contacts/deals and test vs real records. The W4 clock starts on the PT calendar day the field (and GA4, if approved and installed) reach production, after Бадди accepts the preview and the Founder says yes (brief lines 16, 144, 158, 175; W4 protocol line 7). If only the field goes live, measure the field only and state that the GA4 half is missing (brief line 144; W4 protocol line 8).

**Why the option list is built this way.** The Market Researcher’s hypothesis (not a fact) is that demand arrives through general contractors, tenders, and LinkedIn, and that local search demand may be small (`track-b-growth-os/pilot/competitors.md` line 48). The field therefore gives those three channels their own values, plus search, AI assistant answers, a colleague/past-client referral, and Other. This is a measurement design, not proof of the hypothesis.

## 4. Field wording and options (English UI, implement verbatim)

Place the field on the project-inquiry form, after “Project phase” and before “Scope and schedule”, as a required `<select>` (same required pattern as `phase`). Language: English (`og:locale` on the live page is `en_US`).

**Field label (visible text):**

```
How did you hear about us?
```

**Empty / prompt option** (value `""`, disabled, same pattern as “Select the phase”):

```
Select one option
```

**Options** — `value` is the stable mapping key (form payload and later HubSpot enumeration internal value). `label` is the visible English text. Do not rename keys after the preview is accepted. “Other” is a listed option and must be implemented with the free-text fallback below (brief line 64).

| Order | Key (`value`) | Visible label |
|---|---|---|
| 1 | `gc_referral` | GC / general contractor referral |
| 2 | `tenders` | Tender or bid platform |
| 3 | `linkedin` | LinkedIn |
| 4 | `ai_assistant` | AI assistant (ChatGPT, Perplexity, etc.) |
| 5 | `search` | Google or other search |
| 6 | `referral` | Referral from a colleague/past client |
| 7 | `other` | Other (please specify) |

**HTML `name` / JSON key for the select:** `how_did_you_hear_about_us`

**Conditional free-text** (required only when the select value is `other`; hidden otherwise; max 200 characters):

- Visible label: `Please specify`
- HTML `name` / JSON key: `how_did_you_hear_about_us_other`
- Do not accept or store the free-text value unless the select is `other`. If the select is not `other`, send this key as an empty string or omit it.
- **Private log only.** Other free text must never be written to this public repository, never appear in screenshots committed here, and never be sent to GA4. Keep it in the private form/Resend/worker log (and later CRM, after W1) only.

Required/optional: the select is **required** in the UI, so a normal successful submit should always have one of the seven keys. The Other free-text field is **required if and only if** `other` is selected; otherwise optional (not shown). Existing required fields and the honeypot stay as they are.

**Blank / not filled / invalid (`unknown` bucket).** If a stored record nonetheless has a missing, empty, or non-enum source value (older payload, API bypass, or a bug), assign the reporting bucket `unknown`. This bucket is not a UI option and must not appear in the select. Counting rule (Marketing confirmation for W4 metric 2):

- Count `unknown` in the **total** of real form submits (W4 metric 1).
- **Exclude** `unknown` from **source-share** numerators and from the share denominator. For a listed §4 key (including `other`): share(key) = count(key) / count(real submits whose source is one of the seven §4 keys).
- Still report the `unknown` count and `unknown` / total real submits as a separate completeness figure, so blanks are not hidden.
- Do not use Other free text as a source key; `other` remains the source, and the free text is a detail only (redact if it looks like PII before anything is written to this public repo).

This refines the draft wording in `w4-lead-flow-protocol.md` line 25 (share = variant / all real submits, including «не заполнено»). Marketing’s rule is the one in this paragraph. The W4 file is not edited here; Finance can align the protocol to this confirmation.

## 5. HubSpot mapping keys (later, after W1)

Use two custom contact properties (2 of 10 Free slots). Do not create them in this W2 preview task. Do not create an `unknown` option on the form; `unknown` is a reporting bucket only. If a blank value is written to CRM, leave the enumeration empty and flag the record as `unknown` in the measurement export.

| HubSpot internal name | Type | Label | Notes |
|---|---|---|---|
| `how_did_you_hear_about_us` | enumeration (dropdown) | How did you hear about us? | Option internal values = the seven keys in §4, labels = the seven visible labels |
| `how_did_you_hear_about_us_other` | single-line text | How did you hear about us (other) | Filled only when key is `other` |

UTM fields should use HubSpot standard properties if they exist on the Free account after W1; do not spend extra custom-property slots on UTMs until that is verified. Source / UTM / “how did you hear about us?” on the contact record is already listed as an assumption plus a training recommendation (Shestakov p. 50) in `crm-lead-module-requirements.md` line 51 — treat as a recommendation, not a measured result (brief line 61).

## 6. UTM capture recommendation

On first page view of the preview (and later, of production), persist first-touch campaign parameters in `sessionStorage` and write them to hidden inputs at submit. Do not overwrite the self-reported select with UTM values. Capture:

- `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` (from the landing URL query; store the first non-empty set in the session)
- `landing_path` (URL path only, no query string)
- `referrer_host` (hostname of `document.referrer` only, not the full URL)

Include these keys in the `/api/contact` JSON on the preview so W3 can log them later. If a parameter is absent, send an empty string. Strip query strings that may contain emails or other PII. Do not put raw referrer URLs or UTM values that look like emails into this public repo.

## 7. Attribution, test records, and qualified-lead criteria

**Attribution (primary):** the self-reported key `how_did_you_hear_about_us` on that submission, or `unknown` if blank/invalid as in §4. This is the dimension for W4 metric 2 (`w4-lead-flow-protocol.md` line 25; brief line 143), with shares computed as in §4.

**Attribution (supporting, stored, not primary):** first-touch UTMs and `referrer_host`. If they disagree with the select, keep both and report the disagreement. Self-report is required because AI-influenced visits may appear as Direct in analytics (`track-b-growth-os/buy-integrate-build.md` line 73, citing Shestakov p. 50). Do not infer an AI-assistant source from UTM or referrer alone.

**Form submit (W4 metric 1, intermediate):** a successful post as defined in §3, minus honeypot filled (`website` non-empty) and minus test records defined below. Report totals as: all successful posts, test, real. Unique-by-email (“дубли по email считаются один раз”, W4 protocol line 34) applies to unique-contact / CRM counts, not to the raw form-submit count.

**Test-record marking rule** (Marketing confirmation of W4 protocol line 33; compatible with Legal’s reserved-domain examples in `w2-consent-text.md` line 133).

Canonical convention — testers, including the Integration Developer’s preview proof, must prefix `company` and/or `message` with `NFAI-TEST` (case-insensitive). Recommended: put `NFAI-TEST` at the start of both `company` and `message`, and use a reserved RFC 2606 address such as `w2-preview@example.com` (Legal’s `test+w2@example.com` is also fine).

**Exclusion from all W2/W4 lead counts:**

- **Test (not real):** `company` and/or `message` starts with `NFAI-TEST` (case-insensitive).
- **Spam (not real):** honeypot field `website` is filled (brief line 61; W4 protocol line 24). This is spam, not a test record.
- Recommended but not required for exclusion: reserved `@example.com` / `@example.org` / `@example.net` / `.invalid` email, so a test is also obvious in Resend.

Do not use real third-party PII or team members’ personal inboxes (brief line 68; `w2-consent-text.md` line 133).

**Qualified inquiry (business metric; Marketing confirmation of W4 protocol line 35):** `MISSION.md` names “квалифицированные обращения” as a primary metric (lines 36, 119) but does not define an operational rubric (no required project type, geography, budget, or buyer role). The W1–W4 briefs also do not define that rubric. W4 says business metrics are recorded only if a verifiable source exists; otherwise «нет данных» (brief line 143; W4 protocol lines 24 and 35). A qualification rubric is listed as something to build, not as an existing rule (`track-b-growth-os/buy-integrate-build.md` line 62). LiteLLM / form scoring does not replace qualification (W4 protocol line 35).

**In-force counting rule until a rubric is accepted in writing by Бадди (and, if it changes a live process, the Founder):** do not count any form submit as a qualified lead. The qualified-inquiry figure in W2 and W4 is «нет данных». Marketing is not inventing a substitute rubric in this file.

## 8. GA4 status and the sign-in stop

**Status now:** field-only. Marketing has not created a property and has not signed in. The tag is **not installed**. Director / brief rule: any Google sign-in = STOP, append `inbox/needs.md`, do not continue that path (brief lines 67, 83, 88, 174). GA4 likely needs a Google account (risk 3, brief line 174). A stop row is appended to `inbox/needs.md` in the brief’s format. The field and Legal consent still ship on preview (brief lines 67, 174). W4 then measures the field only and states that the GA4 half is missing (brief line 144; W4 protocol line 8).

**If, later, the Founder or Бадди signs in and a property is approved at $0,** install the tag on preview first (not production). Measurement then includes GA4. Event to use for a form submit (W4 metric 4; protocol line 27 asks Marketing to name it):

- Event name: `generate_lead` (GA4 recommended event)
- Parameter: `lead_source` = the option code only (`gc_referral`, `tenders`, `linkedin`, `ai_assistant`, `search`, `referral`, or `other`). Do not send `unknown`, free text, names, or any other parameter that could contain PII.

Do not send to GA4: name, company, email, location, message, Other free text, `requestId`, full referrer URLs, `unknown`, or any other PII. If the source is blank/invalid, omit `lead_source` or do not fire `generate_lead` until the field value is a listed code. Do not send the event, and do not load the tag, until Legal’s consent text covers analytics cookies or an equivalent and that condition is met. If the tag is not installed, do not claim in the UI that Google Analytics is in use (§1).

Property **name** (if ever created): not created. Leave the executor blank in §11.

## 9. PII and redaction

NFAI is a public repository (risk 7, brief line 178; `MISSION.md` line 104). Test leads, screenshots, and worker logs in this repo must be redacted (brief lines 73, 76, 178; W4 protocol line 32). No secrets, tokens, or API keys in files or chat (brief line 87). Client PII must not be sent to Gemini free-tier (`crm-lead-module-requirements.md` line 50; brief W3 line 124). Evidence of a test submit may use a screenshot path under `missions/001-growth-os/track-b-growth-os/pilot/evidence/w2/` and/or a form-notification id, with no extra PII (brief lines 73, 76). Do not paste production Netlify tokens, account IDs, or webhook secrets into this report.

## 10. Acceptance criteria for the Integration Developer preview

From the brief (lines 75–79), plus this spec:

1. A Netlify preview URL (not production) shows the field in §4 (label, seven options including Other, required select, conditional Other free text) and the Legal consent text from `w2-consent-text.md`, adjusted as in §1 if GA4 is not installed. Do not open a public preview form without that text (brief line 14).
2. A test inquiry marked with the `NFAI-TEST` prefix in `company` and/or `message` (§7) submits successfully; evidence is a redacted screenshot path and/or form-notification id, no extra PII (brief lines 68, 76). Show that an empty source field is rejected, and that Other without free text is rejected.
3. Production URL https://wireready-pilot.netlify.app/contact is unchanged (screenshot or HTML diff dated at handover) (brief line 77).
4. GA4: tag not installed; measurement is field-only; `inbox/needs.md` row for Google sign-in (blocking yes for the GA4 half) (brief line 78). A documented `generate_lead` test event is required only if GA4 was installed without a Google sign-in stop — that path is not used here.
5. Preview POST still goes through the existing `/api/contact` JSON contract (or a documented preview equivalent). Do not invent a Netlify Forms integration on production (brief W3 lines 101, 172; `w3-lead-path.md` lines 9–13, 25). Include `how_did_you_hear_about_us`, conditional `how_did_you_hear_about_us_other`, and the UTM/referrer keys from §6 in the payload.
6. Honeypot `website` still works (filled honeypot is not a successful lead).
7. Site/code changes stay in the site repo / preview branch. W3 recorded a read-only look at private repo `fed8eb-arch/wireready` (`w3-lead-path.md` lines 5, 38); access for a preview deploy is still to verify (brief line 61, risk 2 line 173). Record the site-repo hash in §11 if used (brief line 79). Do not copy the full site here.
8. Commits in `/workspace/NFAI-mission-001` only to own paths; `git ls-remote origin refs/heads/mission-001` equals HEAD (brief lines 79, 86). Missing Netlify account access, captcha, or a paid SKU: stop and append `inbox/needs.md` (brief lines 83, 173). Deadline for the preview: 2026-11-24 14:00 PT (brief line 81).

## 11. Executor report (Integration Developer fills; Marketing leaves blank)

Filled 2026-11-23 17:25 PT by the Integration Developer.

- Preview URL (not production): **Not produced.** Director: no Netlify access (no CLI login, no deploys by the executor). No automatic branch-deploy URL is available from this box. A public preview URL still needs the Netlify account owner (Пётр) to create a Deploy Preview or grant access — see `inbox/needs.md` 2026-11-23 17:25 PT. Fallback local preview (static, client validation only, nothing sent): `missions/001-growth-os/track-b-growth-os/pilot/w2-source-field/preview/index.html`.
- Preview / site-repo commit hash: branch `w2-source-field` on `fed8eb-arch/wireready` (not `main`). Commit `d000f2a8258c9e335c9ce4933f94f6c03a158f7d`. Verified: `git ls-remote origin refs/heads/w2-source-field` returned the same hash. Remote `main` remains `bf85cba767e3f27f2e1201a724a0080aff073db4`. No PR was opened; no merge to `main`; production was not deployed.
- What was tested (field, required validation, Other free text, honeypot, production unchanged, test marker in §7):
  - Local UI: required select `how_did_you_hear_about_us` with the seven §4 keys and labels verbatim; “Please specify” appears only for `other` and is required then; consent notice above the submit button, no checkbox.
  - Client validation on the local preview: empty source rejected; `other` without text rejected; `NFAI-TEST` LinkedIn submit accepted locally and not sent anywhere; filled honeypot `website` treated as spam.
  - Server-side (local, Resend **mocked**, no real call): `scripts/w2-contact-route-local-test.mjs` — 18/18 passed. Synthetic payload uses `test+w2@example.com`, company/message prefixed `NFAI-TEST`. Empty/invalid source and `other` without text return 422 and do not call fetch; a valid LinkedIn (and `other` + in-memory `NFAI-TEST`) payload would add source and first-touch UTMs to the Resend email body only. Log: `pilot/w2-source-field/evidence/w2-route-local-test.txt`.
  - Production `https://wireready-pilot.netlify.app/contact` fetched and screenshotted read-only (no submission). Live form still has no source field. Form markup sha256 `3d7a483ea5757749bea7afb1fb111afb1962922890c5c9174477fe8a1f0a5c8e`.
  - Honesty on current production server: **production `route.ts` is unchanged.** The email-body change exists only on branch `w2-source-field`. Until that branch is preview-deployed, a live POST still ignores source/UTM keys (they are tolerated but not validated or written into the Resend email — `app/api/contact/route.ts` on `main` lines 49–57 and 83–86).
- Path to redacted evidence: `missions/001-growth-os/track-b-growth-os/pilot/w2-source-field/evidence/` (`preview-empty.png`, `preview-linkedin.png`, `preview-other-empty.png` with the Work email field solid-box redacted; `production-contact.png`; `production-contact-form-2026-11-23.html`). Other free text was not stored in the public repo. `route.ts` diff: `pilot/w2-source-field/route-ts.diff`.
- Legal consent text present on preview (yes/no, link to `w2-consent-text.md`; GA sentences omitted if tag not installed): **Yes.** Wording from `w2-consent-text.md` (commit `b1785c0`) §1a, placed above the submit button, no checkbox. Google Analytics sentences (§1a second sentence and §1b) omitted because the tag is not installed. “We do not sell or share…” omitted (unconfirmed). Contact-email clause omitted (Legal preview fallback: end at “for details.”).
- GA4 property name if created, or statement: tag not installed (Google sign-in stop); event name if used would be `generate_lead`: **Tag not installed** (Google sign-in stop). If later installed, the event name would be `generate_lead` with `lead_source` equal to the select key only (never Other free text or other PII). Paste-ready snippet only: `pilot/w2-source-field/snippets/ga4-generate-lead.html`.
- `inbox/needs.md` row date/time: GA4 Google sign-in — 2026-11-23 17:18 PT (Marketing). Netlify Deploy Preview URL — 2026-11-23 17:25 PT (Integration Developer).
- Model and effort: Grok Bot, standard effort.

## 12. Marketing confirmations for the W4 protocol (file not edited)

For `pilot/w4-lead-flow-protocol.md` §3 (lines 33–35), which asked Marketing to confirm:

- Option list: the seven keys and labels in §4, plus reporting bucket `unknown` for blank/invalid values, counted in totals and excluded from source shares (§4).
- Test records: `NFAI-TEST` prefix in `company` and/or `message`; filled honeypot `website` = spam (§7).
- Qualified inquiries: in-force rule in §7 — «нет данных» until a rubric is accepted; no submit is auto-qualified.
- GA4: field-only unless a property exists and the tag is installed; event name if used is `generate_lead` (§8).

## 13. Gaps (not invented)

- Operational definition of a qualified inquiry: not in `MISSION.md` or the W1–W4 briefs; confirmed absent in W4 protocol line 35.
- Legal entity and support contact: still missing; Legal recorded the gap, Marketing does not invent them.
- Netlify account owner and confirmed deploy access: not recorded for Marketing (brief line 173; `w3-lead-path.md` lines 5, 34).
- Whether Resend env vars are actually set in production: not verified (`w3-lead-path.md` line 21).
- Baseline form-submit or qualified-inquiry counts, CAC, and margin: нет данных (`competitors.md` lines 9 and 47; W4 protocol line 24).
- GA4 property: not created.

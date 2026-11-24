# W2 — «How did you hear about us?» field (local client-side preview)

**Кратко.** Локальный превью поля по спецификации Маркетинга v1.2 (`w2-ga4-source-field.md`, коммит `62e20fd`): обязательный select, «Please specify» для `other`, согласие из `w2-consent-text.md` без фраз про Google Analytics. Ветка `w2-source-field` в `fed8eb-arch/wireready` (не `main`) запушена: коммит `d000f2a8258c9e335c9ce4933f94f6c03a158f7d`, хеш совпал с `git ls-remote`. На этой ветке `route.ts` проверяет источник и (если Resend настроен) добавляет источник и UTM только в тело письма. Живой сайт и `main` не менялись. Публичного Netlify preview URL нет: доступа к Netlify нет (строка в `inbox/needs.md`). Локальный тест: 18/18, Resend замокан, не вызывался.

**Task:** W2, MISSION-001, WireReady pilot. Owner: Глава маркетинга. Executor: Integration Developer.  
**Deadline:** 2026-11-24 14:00 PT.  
**Date of this preview:** 2026-11-23, evening PT (America/Los_Angeles).  
**Spend:** 0. No Google sign-in, no Netlify sign-in, no production deploy, no PR to `main`.

## Files

| Path | What it is |
|---|---|
| `README.md` | This report |
| `hubspot-property-mapping.md` | Plan only: 2 of 10 Free custom properties, keys from Marketing §5 |
| `route-ts.diff` | Diff of `app/api/contact/route.ts` on branch `w2-source-field` vs `main`. Applied only on that branch, not on `main` |
| `snippets/w2-source-field.patch` | Client-side unified diff: `lib/project-inquiry.ts`, `components/project-inquiry-form.tsx`, `app/(commercial)/commercial.css` |
| `snippets/lib/project-inquiry.ts` | Proposed full file (adds exports; existing `projectPhases` / `inquiryLimits` keys used by `route.ts` are unchanged) |
| `snippets/components/project-inquiry-form.tsx` | Proposed form component |
| `snippets/app/(commercial)/commercial.css` | Two extra CSS rules |
| `snippets/ga4-generate-lead.html` | Paste-ready later; **tag not installed** |
| `preview/index.html` | Local static preview (UI + client validation) |
| `preview/preview.css` | Form-only styles |
| `evidence/production-contact-form-2026-11-23.html` | Live form markup only (no scripts, no tokens) |
| `evidence/preview-empty.png` | Local preview, empty form |
| `evidence/preview-linkedin.png` | Local preview with `NFAI-TEST` data, LinkedIn selected (email redacted in the image) |
| `evidence/preview-other-empty.png` | Other selected, Please specify visible and empty (no Other free text stored) |
| `evidence/production-contact.png` | Read-only screenshot of the live `/contact` page (no submission) |
| `evidence/w2-route-local-test.txt` | Local route test log: 18/18 passed, Resend mocked |

Official Legal text remains at `missions/001-growth-os/track-b-growth-os/pilot/w2-consent-text.md` (commit `b1785c0`). It is not copied or rewritten here.

## Field (Marketing §4, implement verbatim)

- **Label:** How did you hear about us?
- **HTML `name` / JSON key:** `how_did_you_hear_about_us` (required `<select>`)
- **Empty prompt:** Select one option (`value=""`, disabled)
- **Options, in order:**

| Key | Visible label |
|---|---|
| `gc_referral` | GC / general contractor referral |
| `tenders` | Tender or bid platform |
| `linkedin` | LinkedIn |
| `ai_assistant` | AI assistant (ChatGPT, Perplexity, etc.) |
| `search` | Google or other search |
| `referral` | Referral from a colleague/past client |
| `other` | Other (please specify) |

- **Please specify:** `how_did_you_hear_about_us_other`, required only when `other` is selected, max 200 characters, hidden otherwise. In this public repo the Other free text is not stored. In the local preview it may be typed as an in-memory `NFAI-TEST` value only.
- **Hidden first-touch fields:** `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `referrer_host` (hostname only), `landing_path` (path only, no query). Values that look like an email are dropped. Session key: `wr_first_touch_v1`.
- Placement: after Project phase, before Scope and schedule.
- Existing fields and honeypot `website` are unchanged. A filled honeypot is treated as spam on the local preview.

## Consent (Legal, as adjusted for a no-GA4 preview)

Placed directly above the submit button. No checkbox.

> We use the details you submit (name, company, work email, project location, phase, how you heard about us, and your message) to respond to your inquiry. See our Privacy Notice for details.

Adjustments required by Legal / Marketing / Orchestrator, not free rewrites:

- §1a second sentence and §1b (Google Analytics wording) omitted because the GA4 tag is not installed (`w2-ga4-source-field.md` §1 and §11 instruction).
- “We do not sell or share…” omitted (unconfirmed).
- Contact-email clause omitted (Legal preview fallback: end at “for details.”). `/privacy` edits are post-preview.

## Site-repo branch (pushed, not `main`)

- Remote: `fed8eb-arch/wireready`
- Branch: `w2-source-field` (separate from `main`; no PR opened, no merge, no production deploy)
- Commit: `d000f2a8258c9e335c9ce4933f94f6c03a158f7d`
- `git ls-remote origin refs/heads/w2-source-field`: `d000f2a8258c9e335c9ce4933f94f6c03a158f7d	refs/heads/w2-source-field` (matches HEAD)
- Remote `main` remains `bf85cba767e3f27f2e1201a724a0080aff073db4`

On this branch, `app/api/contact/route.ts` validates `how_did_you_hear_about_us` against the seven §4 keys, requires `how_did_you_hear_about_us_other` when the key is `other`, and appends the source plus first-touch `utm_*` / `referrer_host` / `landing_path` to the Resend email body only. No worker hook and no new outbound calls beyond the existing Resend send.

On **production / `main`**, `route.ts` is still the old file. There, extra JSON keys are tolerated (lines 40–47 and 49–57 of `main`) but are **not** validated and are **not** written into the email (lines 83–86 of `main`). That changes only after a preview or a later approved merge, neither of which was done here.

The local static preview does not call `/api/contact` at all (nothing leaves the box).

## Local route test (Resend mocked)

```
node --experimental-strip-types --import ./scripts/w2-alias-loader.mjs scripts/w2-contact-route-local-test.mjs
```

Result: **18/18 passed**. `global.fetch` was mocked; Resend was not actually called. Synthetic contact: `test+w2@example.com`, `NFAI-TEST` in company and message. Log: `evidence/w2-route-local-test.txt`.

## GA4

**Tag not installed.** Creating a property needs a Google sign-in (Director stop). Already recorded in `inbox/needs.md` on 2026-11-23 17:18 PT by Marketing. No second GA4 row was added. `snippets/ga4-generate-lead.html` is paste-ready for later and must not send Other free text or any PII; `lead_source` would be the select key only.

## Netlify preview URL — not produced

Director: no Netlify access (no deploys, no CLI login). No branch deploy URL exists for this preview. A line was appended to `inbox/needs.md`. Fallback proof: this local preview, screenshots, and the site-repo hash `bf85cba767e3f27f2e1201a724a0080aff073db4`. A public preview URL needs the Founder (or the Netlify account owner) to grant access or to create a Deploy Preview; the Integration Developer must not sign in to Netlify.

## What was verified (client-side)

- Empty source is rejected (`required` on the select; local handler also rejects).
- Other without Please specify is rejected (`required` only when `other` is shown).
- A filled `NFAI-TEST` LinkedIn submit is accepted **locally** and is not sent anywhere.
- Filled honeypot `website` is treated as spam locally and is not counted as a lead.
- Production `https://wireready-pilot.netlify.app/contact` was fetched read-only (no submission). Form markup sha256 `3d7a483ea5757749bea7afb1fb111afb1962922890c5c9174477fe8a1f0a5c8e` (same as the first fetch this evening). The live form still has no source field.
- No `gtag` / GTM / Plausible in the fetched live HTML on 2026-11-23.
- Other free text is not written into this public repo.

## Assumptions and limits

- Whether `bf85cba` is exactly the commit Netlify last deployed is not independently proven (site `x-nextjs-date` was 2026-11-11 23:04 UTC). Public HTML and repo source agree on the current fields and the `/api/contact` POST.
- Adding keys to `inquiryLimits` does not change current `route.ts` behaviour, because the route loops only its own `values` object (lines 49–57), not every key of `inquiryLimits`.
- HubSpot properties are a plan only (W1 not done).
- This is not a Netlify Deploy Preview and not a production change.

## How to view the local preview

```bash
python3 -m http.server 8765 --directory preview
```

Open `http://127.0.0.1:8765/` (empty), `?autofill=linkedin`, `?autofill=other-empty`, or `?autofill=empty-source`. Optional UTM query params fill hidden fields. Do not put email addresses in the URL. Submitting the form does not leave the box.

The client and route changes are on `w2-source-field` only (`d000f2a`). No PR was opened. `main` and production were not changed.

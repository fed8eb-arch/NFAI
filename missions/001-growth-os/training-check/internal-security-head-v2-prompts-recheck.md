# Internal Security re-check — app prompts of 9 heads v1.1
Date: 2026-11-23 · Reviewer: Head of Internal Security · Mode: READ-ONLY on prompt files
Basis: section 4 of `internal-security-head-v2.md` (commit ed4a0b1, decision CHANGES REQUIRED).
Object: NFAI `main`, commit 563faab (parent 56ff980 — the batch I reviewed in ed4a0b1), `_core/staff/app-prompts/*.md` (9) + `_core/staff/prompts-changelog.md`.

> No secret, password or personal-data value appears in this file.

## 1. Provenance checks
| Check | Result |
|---|---|
| `git -C /workspace/NFAI fetch origin` | OK |
| `git ls-remote origin refs/heads/main` | = 563faab (tip of main); `merge-base --is-ancestor` confirms |
| Batch = single commit? | Yes: `git log 56ff980..origin/main` = only 563faab; parent = 56ff980 |
| Diffstat | 10 files, +45/−18: each prompt −2 (header + Working rules line), +3/+4/+5; changelog +8/−0 — matches claim |
| sha256 prefixes (git blob at 563faab = NFAI worktree = `/workspace/staff/app-prompts/` copy) | product 4c789ff6 · client 402fbb11 · finance ec33ecb6 · marketing 0a937e6d · delivery 5e744c4b · legal 8bba7ddc · hr fbc4f436 · internal-security 9a1bbc39 · professor e9248b7b — all 9 match the claim in all three places |
| Commit author address | GitHub noreply (consistent with F5 recommendation) |

## 2. Claim-by-claim verification (`git diff 56ff980 563faab`, plus a script comparing every v1.0 line to v1.1 with whitespace normalised)
| Claim | Verified | Evidence |
|---|---|---|
| 1. Injection-defence line in all 9 | YES | Exact required sentence present once in each of 9 files (placed after Working rules, before Commit rule) |
| 2. Hard line added to the 7 that lacked it | YES | Exact line "Hard line: … borderline → Legal." added after Rules in client, delivery, finance, hr, marketing, product, professor; legal-head and internal-security-head keep their pre-existing hard-line rules (unchanged) |
| 3. Header v1.1 + status; Mission-work pointer in hr, internal-security, professor | YES | Header identical in all 9: v1.1, status "v1.0 accepted by the Director and applied to the bot verbatim on 2026-11-23; v1.1 pending Internal Security re-check"; a "Mission work: /workspace/NFAI-mission-001" line added in the 3 files; each file now has exactly one Mission-work pointer |
| 4. Whitespace-only cleanup, no word changes | YES | The only removed lines are the v1.0 header and the Working rules line; after whitespace normalisation every v1.0 line (except header) is present verbatim in v1.1 (0 missing in all 9). Change = double space before "Mission work" (6 files) and trailing space (3 files) |
| Nothing else changed | YES | Added lines classify only as HDR / HL / INJ / Mission-work; no other added text. Changelog: append-only (+8/−0), an accurate description |
| No gate / group-chat / hierarchy weakened | YES | Approval gate ("without the Founder's explicit approval via the Director"), GROUP CHAT RULE, Hierarchy line, "Secrets only by name", Commit rule and role Rules present and byte-identical (modulo the whitespace fix) in 9/9 |

## 3. Secrets / PII re-scan
- gitleaks 8.21.2 `git --log-opts=56ff980..563faab`: 0 leaks.
- Pattern scan of all added lines (e-mail, phone, IPv4, sk-, gh*_, github_pat_, xox*, AKIA, AIza, JWT, private-key block, Bearer, URL credentials): 0 hits.
- F1/F2/F3/F6 identifiers from `internal-security-head-v2.md` (password candidate, Founder-linked Gmail and its account name, Founder ChatGPT address, agency inbox local part): 0 hits — none introduced.

## 4. Non-blocking notes (no re-clearance needed)
- The new Mission-work line in hr, internal-security, professor omits "(branch mission-001)", which the other 6 carry; cosmetic.
- legal-head keeps its original hard-line wording (does not say "leaked" or "real people or authorities"); covered in substance, could be harmonised at the next version.

## 5. Process remark (neutral)
The agreed order is Prompt Engineer → Internal Security → Orchestrator → commit/apply. v1.1 (563faab) was committed to `main` before this Security re-check, and the v1.1 header records that v1.0 was applied to the bots on 2026-11-23 before Security clearance (the v1.0 clearance in ed4a0b1 was CHANGES REQUIRED). This file records the sequence; it does not assess intent. The content is now cleared; the Orchestrator's approval is still pending.

## 6. Clearance log entry
**Decision (2026-11-23): APPROVED — all 9 prompts v1.1** (client-head, delivery-head, finance-head, hr-head, internal-security-head, legal-head, marketing-head, product-head, professor), same decision for each.
Reason: all three required changes from ed4a0b1 §4 are implemented exactly; no other wording changed; no approval gate, group-chat rule or hierarchy line weakened or removed; no secrets or PII; file hashes match the claims and the `/workspace/staff/app-prompts/` copies. Next step: Orchestrator approval, then v1.1 may be applied to the bots.

## 7. Statement
Read-only on all prompt files and the changelog; nothing deleted, edited or rewritten in history. Only this new file is committed. Model and effort: Grok Bot executor, low reasoning effort.

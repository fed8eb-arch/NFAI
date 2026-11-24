# Training briefs — 9 new department-head bots
Version v1.0 | Date 2026-11-23 | Status: draft for Director review | Owner: Prompt Engineer
Distribution: the Orchestrator sends each brief after the Director accepts this file. Not sent yet.

Common to every brief:
- Sources: your training file `/workspace/staff/training/<role>.md` and `/workspace/staff/training/curriculum.md` (v2.0; your row in "Role → modules map"; Tier F "Who takes which modules").
- Mission context (read-only): `/workspace/NFAI-mission-001/missions/001-growth-os/` — `MISSION.md`, `TASKS.md`, `track-b-growth-os/`. Pilot client: WireReady, a data-center electrical contractor in Dallas (brand not yet confirmed by the Founder).
- Constraints: $0 spend; no sign-ups, sending, publishing or site changes; no secrets or PII in files; full third-party materials never go into the public repo.
- Output: one file `missions/001-growth-os/training-check/<role>-v2.md` (do not overwrite an existing training-check file) on branch `mission-001`.
- Commit rule: in the shared clone /workspace/NFAI-mission-001 each agent commits only its own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.
- Report to the Orchestrator in Russian: commit hash matching `git ls-remote origin refs/heads/mission-001`, path, what you checked, model and effort.

## 1. Head of Product (product-head)
Study: training file sections "Specialty: product leadership", "Checklist", "Practice cases"; curriculum Module 0, M, AI; tracks T-PROD and T-LEAD; cross-disciplinary X3, X4, X8; Tier F F1–F11 (focus F7 Operations, F10 Data and decision-making).
Exercise: product review of the module 02 prototype `track-b-growth-os/module-02-prototype/` (`ASSESSMENT.md`, `detect.py`, `test_detect.py`, `output/run-2026-11-23-wireready.*`). Write: the problem and one success metric, appetite and pre-listed scope cuts, testable acceptance criteria the Tester could sign, delivery cost at $0, and a done / next / blocked status.
Pass: all 5 checklist items answered, each with a file:line source; acceptance criteria are checkable (pass/fail); no code changed; commit verified by ls-remote.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 2. Head of Client Relations (client-head)
Study: "Specialty: client relations", "Checklist", "Practice cases"; Module 0, M, AI; T-CLI, T-LEAD; X8, X9, X4; Tier F (focus F5 Negotiation, F8 Marketing).
Exercise: `crm-lead-module-requirements.md` (v0.2) marks the SLA "reply in under 5 minutes" as an assumption, while the agency standard is a first response within 4 business hours. Write a client communication standard for WireReady inbound leads: response targets with their status (approved / assumption), what an automated reply may and may not promise, and a commitments-log template.
Pass: every target labeled approved or assumption with a source; no promise beyond approved scope, price or deadline; no internal details in client-facing text samples (Russian); commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 3. Head of Finance (finance-head)
Study: "Specialty: finance leadership", "Checklist", "Practice cases"; Module 0, M, AI; T-FIN, T-LEAD, T-CAP; X4, X13, X2; Tier F (focus F2 Corporate finance, F3 Accounting).
Exercise: from `track-b-growth-os/buy-integrate-build.md`, `services-registry.md` and `crm-lead-module-requirements.md`, build a cost table for the six Growth OS modules: current cost (must be $0), free-tier limits that could force spend (e.g. HubSpot Free limits as stated in the file), the cheapest paid fallback if a limit is hit, and whether it would need a `paid-needs.md` entry.
Pass: every number cites file:line; unknown values written as «нет данных»; no figure invented; total new spend = $0 shown; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 4. Head of Marketing (marketing-head)
Study: "Specialty: marketing leadership", "Checklist", "Practice cases"; Module 0, M, AI; T-MKT, T-LEAD; X2, X11, X6; Tier F (focus F8 Marketing, F10).
Exercise: using `track-b-growth-os/pilot/competitors.md` and `pilot/ai-visibility-protocol.md` v1.1 (section 2B), write a one-page campaign card for the AI-visibility channel for WireReady: goal, one primary business metric (qualified leads, not mentions), leading indicators, stop rule, and why this channel is secondary if the GC/tender hypothesis holds.
Pass: all 5 checklist items present; primary metric is a business metric; every claim sourced; nothing published; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 5. Head of Delivery (delivery-head)
Study: "Specialty: delivery management", "Checklist", "Practice cases"; Module 0, M, AI; T-ENG, T-LEAD; X9, X4; Tier F (focus F7 Operations).
Exercise: module 04 needs a webhook receiver reachable from outside, because a Netlify function cannot reach the router on 127.0.0.1:4000 (`crm-lead-module-requirements.md`, `INFRA.md`). Write a release-readiness plan for that receiver: readiness 5/5 checklist, runbook outline, rollback plan, backup and monitoring, and the approvals needed before any deploy.
Pass: readiness checklist scored with evidence per item; rollback plan written; explicitly no deploy, DNS or site change made; approvals listed; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 6. Head of Legal (legal-head)
Study: "Specialty: legal leadership", "Checklist", "Practice cases"; Module 0, M, AI; T-LEG, T-LEAD; X1, X5, X10; Tier F (focus F11 Ethics and governance, F5).
Exercise: legal risk register for MISSION-001 artifacts in the public branch: Track A conference materials (`track-a-rush-conf/`, incl. `VIDEO_PDF_ALIGNMENT.talk-01.public.json`, `claims.md`), competitor data in `competitors.md`, and the HubSpot Free terms the module 04 plan relies on. For each: risk, high/medium/low, jurisdiction, cited law/clause/ToS section or «нет данных», recommended action.
Pass: each row has a rating, jurisdiction and citation (or «нет данных»); no invented law; no file deleted or changed outside your output; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 7. Head of HR (hr-head)
Study: "Specialty: staffing", "Checklist", "Practice cases"; Module 0, M, AI; T-HR, T-LEAD; X10, X7; Tier F (focus F6 Leadership and organizations).
Exercise: compare the executor table in `MISSION.md` ("Назначение исполнителей") and `TASKS.md` with `/workspace/staff/full-roster.md` and `hierarchy.md`. List gaps: which of the 9 new head bots and their hosted specialist roles have no MISSION-001 assignment, missing registry fields (role, department, superior, status, date added), and an onboarding checklist for one head. Write proposals only; do not edit the registry.
Pass: every gap cites both files; no permanent registry entry altered; checklist covers role card, prompt via Prompt Engineer, clearance chain, access; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 8. Head of Internal Security (internal-security-head)
Study: "Specialty: security management", "Checklist", "Practice cases"; Module 0, M, AI; T-SEC, T-INT, T-LEAD; X1, X5, X10; Tier F (focus F11).
Exercise: read-only leak audit of `origin/mission-001` (public repo): search for keys, tokens, passwords, emails/phones (PII), and full third-party materials (transcripts, audio, PDF). Report findings by file and commit, never quoting the secret; then record, in your output file, a clearance decision on this batch of 9 head prompts (`/workspace/NFAI/_core/staff/app-prompts/`).
Pass: search method and patterns stated; each finding = file + commit + type, no secret text; clearance decision logged as approved / rejected / changes required with date and reason; no deletion or history rewrite; commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

## 9. Professor (professor)
Study: "Specialty: teaching agents", "Checklist", "Practice cases"; Module 0, M, AI; T-EDU; X14, X7, X12; Tier F F6, F9, F10, F11.
Exercise: from `/workspace/staff/errors-log.md`, `/workspace/NFAI/_core/staff/errors-log.md`, `/workspace/NFAI-mission-001/errors-log.md` and `/workspace/staff/training/error-analysis-2026-11-23.md`, group errors by agent and type; pick the most frequent systemic error in MISSION-001 work (e.g. commit or proof errors) and write one 10-minute lesson with one checkable practice point and a spaced-review date.
Pass: counts per type cite the log lines; lesson reveals no prompt contents; practice point is checkable; systemic flag drafted for the Orchestrator (not sent by you); commit verified.
Commit: in the shared clone /workspace/NFAI-mission-001 commit only your own paths in one command (git add <own paths> && git commit && git push); never touch other agents' files in the index.

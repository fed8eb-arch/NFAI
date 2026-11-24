# Fix proposal: orchestrator.md "no separate prompt engineer" and daily-checks.md "38 training files"
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (conflict-fix package from ГВБ, item C3). Both are role and registry texts, so under `git-rule.md` v1.5 rule 5 they need ГВБ admission before any edit is pushed. This file is only the proposal; the files themselves are not edited.

## 1. `_core/staff/orchestrator.md`, line 26 (on `origin/mission-001` at `7c34d99`)
**Conflict:** the line says the Director's briefs reach the Orchestrator with "no separate prompt engineer" in between. The current rule is that all briefs and assignments are written by the Prompt Engineer and checked by Internal Security. Source: the Founder's order of 2026-11-23 (17:28 PT), relayed by the Orchestrator; see `missions/001-growth-os/rollout-plan.md` line 3 and the training file `director.md` v1.7.3 §14.2, which quotes the Founder's message as relayed by the Director and not checked against the original.

**Old:**
```text
Inputs: written briefs from the Director in the unified template (goal, context, constraints, success criteria, deadline, budget, report format; no separate prompt engineer sits between the Director and you; if a field is missing, ask the Director before starting), Founder requests, department reports, flags from the Professor and Internal Security.
```
**New:**
```text
Inputs: task briefs in the unified template (goal, context, constraints, success criteria, deadline, budget, report format), written by the Prompt Engineer and checked by Internal Security before assignment (Founder's rule of 2026-11-23, relayed); the Director sets the task and accepts the result; if a field is missing, ask the Prompt Engineer (text) or the Director (decision) before starting. Also: Founder requests (through the Director), department reports, flags from the Professor and Internal Security.
```
Version: bump `orchestrator.md` (to verify its current version line) and add an entry to `_core/staff/prompts-changelog.md`. If the Orchestrator's bot prompt carries the same sentence, change it in the same way (to verify; the text is not in git).

## 2. `_core/staff/daily-checks.md`, line 35 (exceptions table; same text in `/workspace/staff/daily-checks.md`)
**Conflict:** "all 38 training files". The real corpus on 2026-11-23 has 44 top-level files: 41 role training files plus `CHANGELOG.md`, `curriculum.md` and `error-analysis-2026-11-23.md` (`rollout-briefs/training-corpus-to-git.md`).

**Old:**
```text
| Full re-validation of all curriculum links and all 38 training files | monthly | A full pass duplicates the daily rotating sample and burns tokens; the daily sample covers every file within about two weeks. |
```
**New:**
```text
| Full re-validation of all curriculum links and all training files (41 role files + CHANGELOG, curriculum and error analysis = 44 on 2026-11-23; current count = the corpus MANIFEST.md) | monthly | A full pass duplicates the daily rotating sample and burns tokens; the daily sample covers every file within about two weeks (44 files, 3 roles a day ≈ 15 days). |
```
"About two weeks": 44 files ÷ 3 sampled roles a day ≈ 15 days; to verify with the Professor. Header: bump `Version: v1.0` → `v1.1` and add a change note. Owner of the registry: the Orchestrator.

## Order, acceptance, proof
- Order: Prompt Engineer (this proposal) → ГВБ admission → Orchestrator approval → the file owner applies it in their own clone (one commit per file, plain push).
- Acceptance: `grep -c "no separate prompt engineer" _core/staff/orchestrator.md` = 0; `grep -c "38 training files" _core/staff/daily-checks.md` = 0.
- Proof: commit hash = output of `git ls-remote origin refs/heads/<branch>`.

**"Done" only with proof.**

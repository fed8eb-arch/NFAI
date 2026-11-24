# Brief: Move the training corpus /workspace/staff/training/ into git
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, rows "Профессор" and "Агентство: завершение training v2". The corpus lives in non-git `/workspace/staff/training/` and is not on origin; plan deadline 2026-11-26, after ГВБ clearance). Times: America/Los_Angeles (PT).

## 1. Facts (counted by the Prompt Engineer)
**Before the machine replacement (2026-11-23 ~17:35 PT):** 65 files, not 41.
- 44 top-level `.md` files: 41 role training files, plus `CHANGELOG.md`, `curriculum.md` and `error-analysis-2026-11-23.md`. The plan's "41 files + curriculum + CHANGELOG" is 43 and misses `error-analysis-2026-11-23.md`.
- `_backup/` held 11 files: `director.v1.2/v1.3/v1.4/v1.6/v1.7/v1.7.1/v1.7.2.md`, `orchestrator.v2.1.md`, `devops-engineer.v2.1.md`, `codex-joker.v1.0.md`, `CHANGELOG.pre-pe-review-2026-11-23.md`.
- `_linkcheck/` held 10 files: link-check URL lists and results of 2026-11-17, and `curriculum-v1.0.bak.md`.
- In git, local only: the Professor's commit `f712eb4` (parent `eaebb4c`) added `_core/staff/training/{CHANGELOG,codex-joker,devops-engineer,director,orchestrator}.md` and `_core/staff/error-analysis-2026-11-23.md`. It was never pushed.

**After the machine replacement (2026-11-23 17:42 PT; recounted ~17:45 PT):** 55 files.
- 42 top-level `.md` files. **Missing:** `codex-joker.md` (training v1.1) and `error-analysis-2026-11-23.md`.
- `_backup/` holds 3 files: `director.v1.2/v1.3/v1.4.md`. The 8 backups made on 2026-11-23 are gone.
- `_linkcheck/` still holds 10 files.
- **`f712eb4` is lost.** It is not on origin (`git cat-file -t f712eb4` in a fresh clone: not a valid object). The Professor's worktree `/workspace/prof-wt-mission001` no longer has `.git`.
- These files still match the hashes the Professor declared: `director.md` `b0b924af…` (v1.7.3), `orchestrator.md` `305fd1f2…`, `devops-engineer.md` `7fe60e23…`, `CHANGELOG.md` `4f9b0203…`.
- No copy of the missing `codex-joker.md` v1.1 (`0cf81002…`) or `error-analysis-2026-11-23.md` (`a872270b…`) was found on the box. A search by file name across the filesystem found nothing. **The Professor must restore or re-create them** (to verify: whether he has another copy).

**Personal-data risk:**
- A scan for e-mail patterns (values not printed) found one address in each of `_backup/director.v1.3.md` and `v1.4.md`, which still exist now.
- Before the replacement it also found one in each of `v1.6`, `v1.7` and `v1.7.1`, which are now gone.
- `director.md` (v1.7.3) has none. The other top-level files and `_linkcheck/` show none.
- A simple pattern scan for common key formats found nothing. `gitleaks` is **not installed** on the box (to verify which scanner ГВБ uses).

## 2. Owners
| Part | Who |
|---|---|
| Brief text; review of the package list | Prompt Engineer |
| Restoring the missing files; packing the corpus; committing; pushing | **Professor** |
| Scan for secrets and personal data **before** the commit; decision on `_backup/` and `_linkcheck/` | **Head of Internal Security (ГВБ)** |
| Decision on the canonical path in the repo | Head of HR (per plan) |
| Assignment, tracking | Orchestrator |
| Acceptance | Director (Бадди) |

## 3. Target path
- Proposed: **`_core/staff/training/`**, the path the Professor used in `f712eb4`. The plan leaves the canonical path to the Head of HR (**to verify**: HR decides in writing before the commit).
- Branch: proposed `mission-001`. To verify with the Orchestrator whether the corpus must also reach `main` (rule: ГВБ clearance → merge to `main`).
- `/workspace/staff/training/` stays where it is until the Director accepts. This brief does not delete or move the source.

## 4. Steps (Professor)
1. Use your own fresh working copy, per `git-rule.md` v1.1. While `/workspace/NFAI` is broken, that is a new clone in a new folder: `git clone --branch mission-001 https://github.com/fed8eb-arch/NFAI.git /workspace/prof-clone`. Do not use `/workspace/NFAI` or `/workspace/NFAI-mission-001`. Never run `git init` over an old folder.
2. Restore `codex-joker.md` (v1.1) and `error-analysis-2026-11-23.md`, or state that they cannot be restored. Their sha256 must match the hashes declared earlier (`0cf81002…`, `a872270b…`), or the file gets a new version and a CHANGELOG note. Push this step at once (`git-rule.md` rule 9).
3. Build the package list: the top-level files, plus `_backup/` and `_linkcheck/` **only as ГВБ decides** (section 5). Write the list, with the sha256 of each file, into `_core/staff/training/MANIFEST.md` (proposed name; to verify).
4. Hand the list to ГВБ **before** `git add`. Wait for the written decision.
5. Copy in only the cleared files and run ГВБ's scanner on the working copy again. Commit only those paths in one command and push plainly: `git add _core/staff/training/<cleared paths> && git commit -m "Professor: training corpus to git (cleared by IS <hash>)" && git push origin HEAD:mission-001`.
6. Verify that `git ls-remote origin refs/heads/mission-001` equals `git rev-parse HEAD`, and that `git ls-tree -r --name-only HEAD _core/staff/training | wc -l` equals the number of cleared files in the manifest.

## 5. ГВБ decision needed (before the commit)
- `_backup/director.v1.3.md` and `v1.4.md` (each contains an address): either **exclude** them from git or **redact** the address and commit the redacted copy, not the original. They are never committed unredacted: the repo is public.
- The rest of `_backup/` and all of `_linkcheck/`: include or exclude. The Prompt Engineer proposes excluding both: the backups exist only for diff checks, and the link-check outputs are work files (to verify).
- The standard scanner and rules: gitleaks plus e-mail and phone patterns, as in ГВБ's earlier re-check.
- Whether to clean the local backup files on disk is ГВБ's decision; this brief does not change them.

## 6. Result / deliverable
The cleared corpus on `origin/mission-001` under the canonical path, with `MANIFEST.md` (file list and sha256 of each file), and ГВБ's written clearance (file and hash) referenced in the commit message.

## 7. Deadline (PT)
The Director cancelled the writing deadlines for these briefs on 2026-11-23. Execution follows the plan: corpus committed and pushed by **2026-11-26**, after HR names the path and ГВБ clears it.

## 8. Acceptance criterion
1. The number of files in git under the canonical path equals the number in `MANIFEST.md` and the number ГВБ cleared. The sha256 of each file in git equals the one on disk.
2. No secret and no personal address in the pushed tree (ГВБ's scan result on the pushed hash).
3. No backup file containing an address is in git unredacted.
4. Only corpus paths are in the commit (`git show --stat <hash>`).
5. The two missing files are restored, or recorded as lost in the CHANGELOG with the Director's acknowledgement.

## 9. Required proof
- The path `_core/staff/training/` (or the HR-approved path), `MANIFEST.md`, and the commit hash = output of `git ls-remote origin refs/heads/mission-001`.
- ГВБ's clearance: file path and hash; scanner name and result line.
- Output of `git ls-tree -r --name-only <hash> <path> | wc -l`.

**"Done" only with proof.** A local commit without push does not count.

## 10. Escalation
- The scanner finds a secret or a personal address → stop and do not commit. Report to ГВБ and the Orchestrator the same hour, giving the file name and line number only, never the value.
- The push is rejected → `git-rule.md` rule 6.
- A dispute over the path → Orchestrator → Director.
- A missing file cannot be restored → Orchestrator and Director the same day.

## 11. To verify / conflicts
- The real count (65 before the replacement, 55 now) differs from the plan's "41". `daily-checks.md` still says "38 training files" in the exceptions table. Updating the registry is for its owner (the Orchestrator), not this brief.
- Canonical path and branch (HR, Orchestrator).
- Scanner (gitleaks is not installed on the box).
- Whether the Professor has any copy of the lost `codex-joker.md` v1.1, `error-analysis-2026-11-23.md` and the 23.11 backups.

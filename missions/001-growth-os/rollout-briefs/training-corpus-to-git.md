# Brief: Move the training corpus /workspace/staff/training/ into git
Version v1.2 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Changes v1.1 (`d3f7173`) → v1.2: the Professor's lost local commit `f712eb4` was restored as **`6d22b4a`** on `origin/mission-001` (ГВБ admitted it at 17:50 PT, per the Orchestrator; the Professor pushed it). Updated the facts and the steps to match.
Changes v1.0 (`c93ee95`) → v1.1:
- Corrected the facts. The 55-file count in v1.0 was taken while the post-replacement restore was still running; at 17:51 PT all 65 files are back, and their hashes match.
- Took in ГВБ's decisions and conditions C1–C4 (`83531eb`, `clearance-training-corpus-to-git.md`):
  - `_backup/` and `_linkcheck/` are excluded;
  - the scanner is fixed;
  - restored files are scanned before they are pushed;
  - only the 44 top-level files and `MANIFEST.md` go into git;
  - the commit identity follows `git-identity.md`;
  - a merge to `main` needs a separate ГВБ decision.

Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, rows "Профессор" and "Агентство: завершение training v2". The corpus lives in non-git `/workspace/staff/training/` and is not on origin). Times: America/Los_Angeles (PT).

## 1. Facts (counted by the Prompt Engineer; re-counted 2026-11-23 17:51 PT)
- `/workspace/staff/training/` holds **65 files**, not 41:
  - **44 top-level `.md` files**: **41 role training files**, plus `CHANGELOG.md`, `curriculum.md` and `error-analysis-2026-11-23.md`. The plan's "41 files + curriculum + CHANGELOG" is 43 and misses `error-analysis-2026-11-23.md`.
  - `_backup/`: 11 files (`director.v1.2/v1.3/v1.4/v1.6/v1.7/v1.7.1/v1.7.2.md`, `orchestrator.v2.1.md`, `devops-engineer.v2.1.md`, `codex-joker.v1.0.md`, `CHANGELOG.pre-pe-review-2026-11-23.md`).
  - `_linkcheck/`: 10 files (link-check URL lists and results of 2026-11-17, `curriculum-v1.0.bak.md`).
- **The machine replacement (17:42 PT):** a recount at ~17:45 PT, during the restore, showed 55 files. ГВБ's count (17:49 PT) and mine (17:51 PT) show all 65 back. The declared hashes match: `codex-joker.md` `0cf81002…`, `error-analysis-2026-11-23.md` `a872270b…`, `director.md` (v1.7.3) `b0b924af…`, `orchestrator.md` `305fd1f2…`, `devops-engineer.md` `7fe60e23…`, `CHANGELOG.md` `4f9b0203…`.
- **Already in git on `origin/mission-001`: `6d22b4a`** (Professor, "restored after box replacement"). It replaces the lost local `f712eb4` and adds 4 files: `_core/staff/training/CHANGELOG.md`, `director.md`, `orchestrator.md` and `devops-engineer.md`. Their sha256 equal the files on disk (`4f9b0203…`, `b0b924af…`, `305fd1f2…`, `7fe60e23…`; checked 17:59 PT). Two files that were in `f712eb4` are **not** in `6d22b4a`: `_core/staff/training/codex-joker.md` and `_core/staff/error-analysis-2026-11-23.md`. They go in with the rest of the corpus under the steps below.
- **Personal-data risk:** an e-mail pattern (values not printed) matches one address in each of `_backup/director.v1.3`, `v1.4`, `v1.6`, `v1.7` and `v1.7.1.md`. `director.md` (v1.7.3), the other top-level files and `_linkcheck/` show none. ГВБ's gitleaks run on the folder found no leaks.

## 2. Owners
| Part | Who |
|---|---|
| Brief text; review of the package list | Prompt Engineer |
| Packing the corpus, committing, pushing | **Professor** |
| Scan for secrets and personal data **before every push** | **Head of Internal Security (ГВБ)** |
| Decision on the canonical path in the repo | Head of HR (per plan) |
| Assignment, tracking | Orchestrator |
| Acceptance | Director (Бадди) |

## 3. Target path and branch
- Proposed: **`_core/staff/training/`**, the path the Professor used in `f712eb4`. The plan leaves the canonical path to the Head of HR (**to verify**: HR decides in writing before the commit).
- Branch: `mission-001`. Getting into `main` needs a separate ГВБ decision after the push to `mission-001` (ГВБ C4).
- `/workspace/staff/training/` stays where it is. This brief does not delete or move the source, and **local backups are not deleted**: deleting them needs the Founder's decision through the Director (ГВБ).

## 4. ГВБ decisions (`83531eb`)
- **`_backup/` is excluded from git as a whole**: it is neither edited nor committed.
- **`_linkcheck/` is excluded**: it holds work files and third-party URLs.
- **What goes into git (ГВБ C2):** only the 44 top-level `.md` files plus `MANIFEST.md`, after HR's written decision on the path.
- **Scanner:** `gitleaks dir --redact --no-banner <path>`, plus e-mail and phone patterns. The result gives the file name and line only. ГВБ used a binary at `/tmp/gitleaks`; since `/tmp` may not survive a machine replacement, check that it is still there before each scan (to verify).
- **`error-analysis-2026-11-23.md`** describes the 2026-11-23 incident. It must not quote a password and must not point to the line in `status.md` where one appeared (ГВБ C1). ГВБ checks this file specifically.

## 5. Steps (Professor)
1. Work in your own fresh clone (`git-rule.md` v1.2): `git clone --branch mission-001 https://github.com/fed8eb-arch/NFAI.git /workspace/prof-clone`. Do not use `/workspace/NFAI`, `/workspace/NFAI-mission-001` or an old worktree, and never run `git init` over an old folder. Set your identity as `git-identity.md` v1.1 says (form B, or the env-var fallback), **not `NFAI Joker`** (ГВБ C3).
2. Build the package list of the 44 top-level files, with the sha256 of each, in `_core/staff/training/MANIFEST.md` (proposed name; to verify).
3. Hand the list to ГВБ **before** `git add`, and wait for the written decision. Nothing is pushed before ГВБ's scan (ГВБ C1). This covers `codex-joker.md` and `error-analysis-2026-11-23.md`; the 4 files already in `6d22b4a` are only checked against the manifest and are not committed again unless they changed.
4. Copy in only the cleared files and run the scanner on the clone again.
5. Check the index: `git diff --cached --name-only` must list only `_core/staff/training/...` paths (ГВБ C2).
6. Commit in one command with a plain push: `git add _core/staff/training/<cleared paths> && git commit -m "Professor: training corpus to git (cleared by IS <hash>)" && git push origin HEAD:mission-001`.
7. Verify that `git ls-remote origin refs/heads/mission-001` equals `git rev-parse HEAD`, and that `git ls-tree -r --name-only HEAD _core/staff/training | wc -l` equals 45 (44 files + `MANIFEST.md`), or the number ГВБ cleared.
8. Push straight after each completed step (`git-rule.md` rule 9). An unpushed step does not count.

## 6. Result / deliverable
The cleared corpus on `origin/mission-001` under the canonical path, with `MANIFEST.md` (file list and sha256 of each file), and ГВБ's written clearance (file and hash) referenced in the commit message.

## 7. Deadline (PT)
The Director cancelled the writing deadlines for the briefs on 2026-11-23. Execution follows the plan: the corpus is committed and pushed by **2026-11-26**, after HR names the path and ГВБ clears it.

## 8. Acceptance criterion
1. In git under the canonical path: the 44 top-level files plus `MANIFEST.md`, or exactly the files ГВБ cleared. The sha256 of each file in git equals the one on disk and in the manifest.
2. No file from `_backup/` or `_linkcheck/` is in git.
3. No secret and no personal address in the pushed tree (ГВБ's scan result on the pushed hash).
4. Only corpus paths are in the commit (`git show --stat <hash>`), and the commit author is not `NFAI Joker`.

## 9. Required proof
- The path `_core/staff/training/` (or the HR-approved path), `MANIFEST.md`, and the commit hash = output of `git ls-remote origin refs/heads/mission-001`.
- ГВБ's clearance: file path and hash; scanner name and result line.
- Output of `git ls-tree -r --name-only <hash> <path> | wc -l`.

**"Done" only with proof.** A local commit without push does not count.

## 10. Escalation
- The scanner finds a secret or a personal address → stop and do not commit. Report to ГВБ and the Orchestrator the same hour, with the file name and line number only, never the value.
- The push is rejected → `git-rule.md` rule 6 (fresh clone, never rebase).
- A dispute over the path → Orchestrator → Director.

## 11. To verify / conflicts
- The real count (65; 44 top-level files) differs from the plan's "41". `daily-checks.md` still says "38 training files" in its exceptions table. Updating that registry is for its owner (the Orchestrator).
- Canonical path (HR); `MANIFEST.md` name.
- That the scanner binary is still present after any machine replacement.

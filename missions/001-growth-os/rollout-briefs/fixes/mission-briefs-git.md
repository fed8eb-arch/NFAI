# Fix proposal: git lines in mission-001 briefs talks-02-03.md and w1-w4.md
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (conflict-fix package from ГВБ, item C2). Basis: `missions/001-growth-os/rollout-briefs/git-rule.md` v1.5 (v1.4 APPROVED, `190f02e`). ГВБ confirmed the conflicts `mission-001/briefs/talks-02-03.md:45` and `mission-001/briefs/w1-w4.md` in `clearance-git-rule.md`.
Both briefs were written by the Prompt Engineer. They are already issued, so they are changed only after ГВБ admission and Orchestrator approval; this file is the proposal. The talks 02/03 task is finished, and W1–W4 are paused by the Founder's order of 2026-11-23 17:28 PT. The fix stops anyone from reusing the old wording.

## 1. `mission-001/briefs/talks-02-03.md`, line 45 (on `origin/mission-001` at `76f9b50`)
**Old:**
```text
- Work only in worktree `/workspace/NFAI-mission-001` (branch `mission-001`): `git pull --rebase` before the commit, commit only your file, `git push`, verify with `git ls-remote origin refs/heads/mission-001`.
```
**New:**
```text
- Work only in your own fresh clone `/workspace/<agent>-clone` (`git clone --branch mission-001 https://github.com/fed8eb-arch/NFAI.git /workspace/<agent>-clone`), per `missions/001-growth-os/rollout-briefs/git-rule.md`: commit only your file in one command (`git add <your file> && git commit -m "<Role>: ..." && git push origin HEAD:mission-001`), no `-c`, force, rebase or stash; if the push is rejected as non-fast-forward, make a fresh clone and retry once; verify `git ls-remote origin refs/heads/mission-001` = HEAD.
```
Header line 2: bump to `Version: v1.1`, and add `Change v1.1: git line per git-rule.md (no pull --rebase, own clone)`.

## 2. `mission-001/briefs/w1-w4.md`
**2a. Line 7, inside the context paragraph. Old fragment:**
```text
Worktree: `/workspace/NFAI-mission-001`, branch `mission-001`.
```
**New fragment:**
```text
Workspace: your own fresh clone `/workspace/<agent>-clone`, branch `mission-001` (see `missions/001-growth-os/rollout-briefs/git-rule.md`).
```
**2b. Lines 48, 86, 127 and 163 (4 identical lines; same md5). Old:**
```text
1. Commit only your own paths in one command: `git add <own paths> && git commit -m ... && git push origin HEAD:mission-001`, then verify with `git ls-remote origin refs/heads/mission-001` (hash must equal HEAD); never touch others' files in the index; work in worktree `/workspace/NFAI-mission-001`.
```
**New (all 4):**
```text
1. Commit only your own paths in one command: `git add <own paths> && git commit -m "<Role>: ..." && git push origin HEAD:mission-001`, then verify with `git ls-remote origin refs/heads/mission-001` (hash must equal HEAD); never touch others' files in the index; push after every completed step; work only in your own fresh clone `/workspace/<agent>-clone` per `missions/001-growth-os/rollout-briefs/git-rule.md`.
```
Header line 3: bump to `Version: v1.1`, and add `Change v1.1: workspace/commit lines per git-rule.md`. The pause status of W1–W4 is not changed.

## Order, acceptance, proof
- Order: Prompt Engineer (this proposal) → ГВБ → Orchestrator → the Prompt Engineer applies it on `mission-001` in its own clone (2 files, one commit, plain push).
- Acceptance: `grep -c "NFAI-mission-001\|pull --rebase" mission-001/briefs/talks-02-03.md mission-001/briefs/w1-w4.md` = 0 for both.
- Proof: commit hash = output of `git ls-remote origin refs/heads/mission-001`.

**"Done" only with proof.**

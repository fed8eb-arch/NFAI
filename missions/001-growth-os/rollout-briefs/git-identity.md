# Brief: Per-agent git identity (user.name / user.email in each agent's own worktree)
Version v1.0 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, row "Агентство: git-идентичность (P0)"). Depends on brief `git-rule.md` (own worktree per agent).
Times: America/Los_Angeles (PT). Repository: `fed8eb-arch/NFAI` (public), local clone `/workspace/NFAI`.

## 1. Problem (facts checked 2026-11-23 ~17:35 PT)
- Every commit is authored by the one identity set in the shared `/workspace/NFAI/.git/config`: `user.name = NFAI Joker` with the repository owner's GitHub noreply address. The rule "commit only own paths" cannot be audited by author.
- `extensions.worktreeConfig` was **not enabled** in `/workspace/NFAI` (`git config --get extensions.worktreeConfig` returned nothing). So `git config --worktree ...` fails with "--worktree cannot be used with multiple working trees unless the config extension worktreeConfig is enabled".
- `core.repositoryformatversion = 0`, `core.bare = false`, no `core.worktree` set, git 2.47.3.
- Test on a scratch repository (not NFAI), git 2.47.3, format version 0: after `git config extensions.worktreeConfig true`, `git config --worktree user.name/user.email` in a linked worktree wrote `.git/worktrees/<name>/config.worktree`; commits there used the worktree identity, commits in the main worktree kept the shared one. Behaviour in NFAI itself: to verify after setup.
- **New fact, 2026-11-23 ~17:42 PT:** the shared box was replaced. After that `/workspace/NFAI` is **not a git repository** (its `.git/` holds only `description`, `hooks/`, `info/`), the linked worktrees are gone, and the box has **no GitHub login** (`gh auth status`: not logged in). The Integration Developer must first restore a working clone and push access (who and how — to verify with the Orchestrator). All shared-config facts above describe the state before the replacement.

## 2. Owner and roles
| Part | Who |
|---|---|
| Brief text | Prompt Engineer |
| Check of the brief; choice of address form (section 4); acceptance of the settings | Head of Internal Security (ГВБ) |
| Setup (the only agent who changes git config for this task) | Integration Developer (Разработчик интеграций) |
| Assignment, tracking, acceptance of the settings with ГВБ | Orchestrator |
| Each writing agent | does not change its identity itself; reports its worktree path to the Integration Developer |

## 3. Method (Integration Developer)
**Step 0 — approval.** Enabling `extensions.worktreeConfig` changes the shared `/workspace/NFAI/.git/config`. Under `git-rule.md` rule 1 only an ordered config change is allowed: do step 1 only after ГВБ clears this brief and the Orchestrator assigns it in writing.
**Step 1 — enable once (shared config, one line):**
`git -C /workspace/NFAI config extensions.worktreeConfig true`
Do not touch `remote.*`, `url.*`, `core.hooksPath` or any other key. Record `git -C /workspace/NFAI config --show-origin --list | grep -v -i -E 'token|password|secret'` before and after; the only new line must be `extensions.worktreeconfig=true`.
**Step 2 — per agent, inside that agent's own worktree only:**
`git -C /workspace/<agent>-wt config --worktree user.name "NFAI <Role>"`
`git -C /workspace/<agent>-wt config --worktree user.email "<address per section 4>"`
Check: `git -C /workspace/<agent>-wt config --show-origin --get user.name` must point to `.../.git/worktrees/<agent>-wt/config.worktree`.
**Step 3 — keep the shared fallback.** Leave the shared `NFAI Joker` identity as is (changing it is not in this brief). After 2026-11-25 any new commit authored `NFAI Joker` means a write outside an own worktree; ГВБ flags it in the daily check.
**Fallback if step 1 is not approved or fails (to verify):** the agent sets identity for its session only, with no config change: `export GIT_AUTHOR_NAME="NFAI <Role>" GIT_COMMITTER_NAME="NFAI <Role>" GIT_AUTHOR_EMAIL="<address>" GIT_COMMITTER_EMAIL="<address>"` before `git commit`. Weakness: it is lost with the shell, so it must be in the agent's routine. Not `git -c user.*=...` (the `git-rule.md` ban on `-c` covers push routing; ГВБ decides if `-c user.*` is allowed — to verify).
**A new worktree** (for example after a rejected push, `git-rule.md` rule 6) needs step 2 again before the first commit.

## 4. Address rules
- Only a noreply address or an agency "+tag" address. **Never a personal address**, never the Founder's or any person's mailbox.
- Allowed forms (ГВБ chooses one and writes it in the decision):
  - **A. Agency +tag:** `<agency mailbox local part>+git-<agent>@<agency mail domain>`, the same agency mailbox and +tag pattern already used for service sign-ups in `_core/pilot/accounts.md`. One unique address per agent.
  - **B. Repository owner's GitHub noreply** (the address already in the shared config). Same email for all; the agent is told apart by `user.name` only.
- **Banned:** inventing `<name>@users.noreply.github.com` addresses. GitHub links such an address to the GitHub user with that login if it exists, so commits would be shown as another person's (GitHub noreply behaviour; to verify).
- Names: `NFAI <Role>` in English, unique, for example `NFAI Prompt Engineer`, `NFAI Internal Security`, `NFAI Orchestrator`, `NFAI Professor`, `NFAI Integration Developer`. Full list = writing agents on the approved roster (the "9 heads" list is the Founder's domain; to verify when approved).
- Public repo: whatever address is chosen is published in commit metadata. ГВБ confirms that it is acceptable.

## 5. Result / deliverable
- `extensions.worktreeConfig=true` in `/workspace/NFAI` (or the written fallback decision).
- Every writing agent's worktree has its own `user.name` and allowed `user.email` in `config.worktree`.
- Integration Developer's setup report (file in the repo, path set by the Orchestrator; proposed `missions/001-growth-os/rollout-briefs/reports/git-identity-setup.md`): per agent worktree path, name, address form (A or B, no secrets), command output of the check in step 2.

## 6. Deadline (PT)
The Director cancelled the writing deadlines for these briefs on 2026-11-23. Execution deadline from the plan: **setup done by 2026-11-25**; acceptance by ГВБ and Orchestrator proposed 2026-11-26 12:00 (to verify).

## 7. Acceptance criterion
1. `git -C /workspace/<agent>-wt config --show-origin --get user.name` and `--get user.email` show the worktree file and the agreed values for every writing agent.
2. `git log --since=2026-11-25 --format='%h %an <%ae>' origin/<branch>` shows only agreed names and allowed addresses; any `NFAI Joker` commit after 2026-11-25 is listed as an issue.
3. No personal address in config, commits, or the setup report (ГВБ scan).
4. The only change in shared config is `extensions.worktreeconfig=true` (before/after output in the report).

## 8. Required proof
- Setup report path and commit hash = output of `git ls-remote origin refs/heads/<branch>`.
- The `git log --format` line of the first commit of each agent after setup.
- ГВБ acceptance: file path and hash.
**"Done" only with proof.**

## 9. Escalation
- Step 1 refused or `git config --worktree` fails → Integration Developer stops, reports the exact error to the Orchestrator and ГВБ the same hour; ГВБ decides on the fallback.
- An agent finds a wrong identity in its worktree → does not fix it itself, reports to the Integration Developer and the Orchestrator.
- A personal address found anywhere → ГВБ the same hour; no history rewrite without the Founder's "yes" through the Director.

## 10. To verify
- Restoring `/workspace/NFAI` as a git clone and push access after the box replacement (who, how; credentials are not handled in this brief).
- `config --worktree` behaviour inside NFAI after step 1 (tested only on a scratch repository).
- Address form A or B (ГВБ).
- Whether `git -c user.name=... commit` is acceptable as a fallback (ГВБ).
- Final list of writing agents and their worktree paths (approved roster).

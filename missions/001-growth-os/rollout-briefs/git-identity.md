# Brief: Per-agent git identity (user.name / user.email in each agent's own clone)
Version v1.1 | Date 2026-11-23 | Status: draft for Internal Security check | Owner: Prompt Engineer
Change v1.0 → v1.1 (2026-11-23, by the Orchestrator's order): aligned with `git-rule.md` v1.2. The workspace is each agent's own fresh clone `/workspace/<agent>-clone`, not a worktree.
- Identity is set in the clone's own config with `git config` (repository-local). `extensions.worktreeConfig` and `git config --worktree` are no longer needed.
- Corrected a v1.0 statement: the box does have git push access to GitHub (ГВБ C3). Only the `gh` CLI is not logged in.
- Took in ГВБ's decisions on v1.0 (`83531eb`, `clearance-git-identity.md`): address form B only; form A banned; `git -c user.*` banned; env-var fallback allowed; C1 (own clone's local config); C2 (a `NFAI Joker` commit is a violation right after setup); C4 (no config output with URL values).

Ordered by: Orchestrator (task from Director Бадди; rollout plan `56b9067`, row "Агентство: git-идентичность (P0)"). Depends on `git-rule.md` v1.2 (one own clone per agent).
Times: America/Los_Angeles (PT). Repository: `fed8eb-arch/NFAI` (public).

## 1. Problem (facts)
- Before the machine replacement (checked ~17:35 PT), every commit was authored by the one identity in the shared `/workspace/NFAI/.git/config`: `user.name = NFAI Joker` with the repository owner's GitHub noreply address. The rule "commit only own paths" cannot be audited by author.
- On 2026-11-23 at 17:42 PT the machine was replaced. `/workspace/NFAI` is no longer a git repository, and the worktrees are gone. The new box has no global `user.name`/`user.email`. git push to GitHub works through a configured credential helper; `gh auth status` reports "not logged in". Credentials are not part of this brief.
- Commits on `origin/mission-001` after the replacement (checked 17:50 PT) were authored by `NFAI Joker` (owner's GitHub noreply) and by `NFAI Internal Security` with an `@example.com` address.
- For reference, v1.0 tested the per-worktree method on git 2.47.3. `git config --worktree` needs `extensions.worktreeConfig=true`, which was not enabled in `/workspace/NFAI`. With own clones this method is not used.

## 2. Owner and roles
| Part | Who |
|---|---|
| Brief text | Prompt Engineer |
| Check of the brief; choice of address form (section 4); acceptance of the settings | Head of Internal Security (ГВБ) |
| Setup and the setup report | Integration Developer (Разработчик интеграций) |
| Assignment, tracking, acceptance of the settings with ГВБ | Orchestrator |
| Each writing agent | sets nothing on its own initiative; applies exactly the values the Integration Developer assigns and reports its clone path |

## 3. Method
**Step 1 — per agent, inside that agent's own clone only (no shared config, no `--global`):**
`git -C /workspace/<agent>-clone config user.name "NFAI <Role>"`
`git -C /workspace/<agent>-clone config user.email "<address per section 4>"`
Check: `git -C /workspace/<agent>-clone config --show-origin --get user.name` must point to `/workspace/<agent>-clone/.git/config`.
- This is the only config change allowed for this task (ГВБ C1). The Integration Developer runs it, or the agent runs it with the values the Integration Developer assigned in writing.
- Never print or report config output that contains remote URLs or credentials (ГВБ C4). If such a value appears, stop and report to ГВБ without the value.
- Do not touch `remote.*`, `url.*`, `core.hooksPath` or credentials (`git-rule.md` rule 1).
- Do not set `--global` identity: the box is shared, and a global identity would hide who committed.

**Step 2 — a new clone needs it again.** A clone made after a machine replacement or a rejected push (`git-rule.md` rule 6) needs step 1 before its first commit. The agent records its name and address form in its own notes so it can redo this.

**Fallback (ГВБ decision):** set the session environment variables `GIT_AUTHOR_NAME`, `GIT_COMMITTER_NAME`, `GIT_AUTHOR_EMAIL` and `GIT_COMMITTER_EMAIL` before `git commit`. The name is `NFAI <Role>`. The address is form B or an `@example.com` placeholder (ГВБ allows both for this fallback). This changes no config. **`git -c user.*=...` is banned** (ГВБ: one simple ban on `-c`).

**Until this brief is in force:** `git-rule.md` v1.2 (ГВБ F3) applies. Every commit message starts with `<Role>: …` and every report carries `Agent: <role>`.

## 4. Address rules (ГВБ decision, `83531eb`)
- **Form B only:** the repository owner's GitHub noreply address (the one already in commit metadata). The email is the same for all agents; agents are told apart by `user.name`.
- **Form A (agency mailbox +tag) is banned for git.** ГВБ: that sign-up mailbox is linked to addresses its audit classed as the Founder's personal data, so it must not be published in the metadata of a public repo.
- **Never a personal address**, and never the Founder's or any person's mailbox.
- **Banned:** invented `<name>@users.noreply.github.com` addresses. GitHub links such an address to the GitHub user with that login if one exists, so the commits would show as another person's (GitHub noreply behaviour; to verify).
- `@example.com` is allowed only in the env-var fallback (section 3).
- Names (approved by ГВБ) are `NFAI <Role>`: English and unique, for example `NFAI Prompt Engineer`, `NFAI Internal Security`, `NFAI Orchestrator`, `NFAI Professor`, `NFAI Integration Developer`. The full list is the writing agents on the approved roster; the "9 heads" list is the Founder's domain (to verify once it is approved).

## 5. Result / deliverable
- Every writing agent's own clone has its own `user.name` and an allowed `user.email` in its `.git/config`.
- The Integration Developer's setup report (path set by the Orchestrator; proposed `missions/001-growth-os/rollout-briefs/reports/git-identity-setup.md`). One row per agent: clone path, name, address form (A or B, no secrets), and the output of the check in step 1.

## 6. Deadline (PT)
The Director cancelled the writing deadlines for these briefs on 2026-11-23. Execution: setup starts right after ГВБ clears this version, then ГВБ and the Orchestrator accept it.

## 7. Acceptance criterion
1. For every writing agent, `git -C /workspace/<agent>-clone config --show-origin --get user.name` and `--get user.email` show that clone's `.git/config` and the agreed values.
2. From the moment an agent's clone is set up, `git log --since=<setup time> --format='%h %an <%ae>' origin/<branch>` shows only agreed names and allowed addresses for that agent. **Any `NFAI Joker` commit after setup is a violation** (ГВБ C2; `git-rule.md` F3).
3. No personal address appears in config, commits or the setup report (ГВБ scan).
4. No global or shared identity was changed.

## 8. Required proof
- The setup report path and its commit hash = output of `git ls-remote origin refs/heads/<branch>`.
- The `git log --format='%h %an <%ae>'` line of each agent's first commit after setup.
- ГВБ's acceptance: file path and hash.

**"Done" only with proof.** A local commit without push does not count.

## 9. Escalation
- A setup command fails → the Integration Developer stops and reports the exact error to the Orchestrator and ГВБ the same hour.
- An agent finds a wrong identity in its clone → it does not change it on its own initiative and reports to the Integration Developer and the Orchestrator.
- A personal address is found anywhere → ГВБ the same hour. No history is rewritten without the Founder's "yes" through the Director.

## 10. To verify
- The final list of writing agents and their clone paths (approved roster).
- GitHub's linking of invented noreply addresses (the reason for the ban in section 4).

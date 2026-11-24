# Git identity setup report
Agent: Integration Developer | Date 2026-11-23 | Brief: git-identity.md @94e7392 (v1.1), ГВБ clearance 83531eb | Times PT

Only change: repository-local user.name / user.email (git config --local). No --global, no git -c user.*, no remote/url/hooks/credentials touched. Address values are not written here (ГВБ C4); only the form and domain suffix.

| Agent | Clone path | user.name | Address form | Check (git config --show-origin --get user.name / user.email) | Set by |
|---|---|---|---|---|---|
| Integration Developer | /workspace/intdev-clone | NFAI Integration Developer | B | `file:.git/config NFAI Integration Developer`; `file:.git/config …@users.noreply.github.com` | me |
| Prompt Engineer | /workspace/pe-clone | NFAI Prompt Engineer | B | `file:.git/config NFAI Prompt Engineer`; `file:.git/config …@users.noreply.github.com` | Integration Developer |
| Internal Security | /workspace/gvb-clone | NFAI Internal Security | B | `file:.git/config NFAI Internal Security`; `file:.git/config …@users.noreply.github.com` | Integration Developer |
| Internal Security (2nd clone) | /workspace/gvb-errlog | NFAI Internal Security | B | `file:.git/config NFAI Internal Security`; `file:.git/config …@users.noreply.github.com` | Integration Developer |
| Professor | /workspace/prof-clone | NFAI Professor | B | `file:.git/config NFAI Professor`; `file:.git/config …@users.noreply.github.com` | Integration Developer |
| Orchestrator | /workspace/orch-clone | NFAI Orchestrator | B | `file:.git/config NFAI Orchestrator`; `file:.git/config …@users.noreply.github.com` | Orchestrator (self) |

Notes
- Before setup: prof-clone and gvb-errlog had local NFAI Joker; pe-clone had empty local user.email (per ПИ); intdev-clone was a fresh clone; prior local identity of gvb-clone was not recorded. HEAD, index, working files and branches were not changed in any clone (HEAD checked before/after).
- Prompt Engineer's temporary clones pe-clone-r1…r6, pe-clone2, pe-clone3 were not configured (no longer used, per ПИ; their commits used the GIT_AUTHOR_*/GIT_COMMITTER_* fallback with form B).
- Commits made before setup (e.g. Professor's unpushed 6d22b4a as NFAI Joker) stay as they are; criterion 7.2 applies from setup time (~17:53–17:56 PT).
- Brief step 2: any new clone needs step 1 again before its first commit.
- Pending per brief §8: each agent's first commit line after setup; ГВБ acceptance.

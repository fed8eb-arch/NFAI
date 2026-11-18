# Exercise: verify and hand off project knowledge

Any NFAI role can use this exercise to learn the shared memory workflow. Use public project sources for the Claude Code run.

1. From the repository root, run `python3 _core/memory/query.py show telegram-parser`, then `python3 _core/memory/query.py show telegram-tooling`. Open the role and source files returned by the graph.
2. Open [the Capy review](../results/05-capy.md). Report one supported statement, with its public URL and video time range, and one claim that the source cannot establish about NFAI.
3. Identify the role that reviews the research task. Provide the intended handoff as a draft with an evidence path and next action.
4. Run `python3 _core/memory/query.py check`. The reviewer checks that the cited path exists, the claim is traceable, the limitation is explicit and the role matches the graph.

For the restricted document launcher, supply the reviewed public note as the input document and include the exercise's requested fields in the prompt. A repo-root CLI session and the restricted document launcher have separate project context. Keep raw Telegram content outside Git and outside routed prompts.

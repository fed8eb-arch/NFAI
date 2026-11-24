# Brief: Rush Conf talks 02 (Zuev) and 03 (Krasinsky) — 5-level analysis
Version: v1.0 | Date: 2026-11-23 | Status: issued | Author: Prompt Engineer | Ordered by: Бадди (Director) | Due: 2026-11-23 19:00 PT (proposed; Director may change)

Two parallel, independent tasks. Same method, different sources. Output in Russian, like the sample.

| Talk | Executor | Output file (branch `mission-001`) |
|---|---|---|
| 02 — Игорь Зуев, «С 0 до первой выручки: запускаем простой AI-проект в США и ЕС в прямом эфире», 00:44:34–01:30:50 | Исследователь рынка | `missions/001-growth-os/track-a-rush-conf/talk-02-zuev-analysis.md` |
| 03 — Илья Красинский, «От поискового запроса до оплаты: как адаптировать маркетинг к AI-поиску», 01:30:50–02:14:16 | Codex | `missions/001-growth-os/track-a-rush-conf/talk-03-krasinsky-analysis.md` |

Talk times and titles: `track-a-rush-conf/speakers.md`.

## 1. Sample to follow
`missions/001-growth-os/track-a-rush-conf/talk-01-petrochenkov-analysis.md`. Keep its structure:
1. **Извлечение** — what can be extracted reliably from speech and slides, with timecodes (not "every word").
2. **Понимание** — the speaker's core idea in plain words; how it fits MISSION-001 (no mixing intermediate metrics with profit).
3. **Проверка** — claims table: `Утверждение | Статус | Источник (timecode / slide p.) | Комментарий`.
4. **Адаптация NFAI для рынка США** — what transfers as logic, what does not (Russian stack: Яндекс, Авито, etc.).
5. **Внедрение** — accept existing services, train agents, do not build our own; nothing on a live client site without the owner's permission.

Header: title, recording link (YouTube video used for talk 01), chapter timecodes, slide source, and the **ASR quality warning**.

## 2. Fact statuses (use exactly these four in the Level 3 table)
- **VERIFIED** — said in speech AND confirmed by a slide, or by an independent source (link).
- **EXPERIMENTAL** — a method or practice the speaker proposes; plausible but not measured; can be tested in the pilot.
- **UNSUPPORTED** — a claim (numbers, effects, "×N growth", self-reported credentials) with no proof in the talk or sources.
- **REJECTED** — contradicted by a slide, by audio check, or by an independent source; quote what contradicts it.

Note: the sample's Level 3 uses mixed labels; this brief standardises them. Every claim gets exactly one status.

## 3. Sources and quote rules
- Transcripts: `/workspace/rush-conf/transcripts/02-zuev.{txt,srt,segments.json}` and `03-krasinsky.{txt,srt,segments.json}` (faster-whisper; **noisy**: Latin garbage in Russian speech, broken names and terms, repeats).
- YouTube auto-captions for cross-checking: `/workspace/rush-conf/captions/full.ru-orig.vtt` (also not a manual reference).
- Slides:
  - **Talk 03:** `/workspace/rush-conf/pdf/02-krasinsky-ot-zaprosa-do-oplaty-18p.pdf` (the file is numbered 02 in the Drive folder but it is talk 03). It has no text layer; OCR is in `/workspace/rush-conf/pdf-text/02-krasinsky-ot-zaprosa-do-oplaty-18p/` (tesseract, also noisy), and page images are in `/workspace/rush-conf/pdf-render/`. Check every quote against the page image, not only the OCR.
  - **Talk 02: there is NO PDF.** The official Drive folder has no Zuev slides (README.md, checked 2026-11-23). Speech-vs-slide checks are impossible. Therefore: a claim can be VERIFIED only through an independent source or through agreement of the transcript with the auto-captions (state which); otherwise at most EXPERIMENTAL/UNSUPPORTED. Write this limit in the header.
- Quotes: short, only where the meaning matches the slide (03) or the auto-captions (02); give the timecode. Numbers heard only in ASR are never cited as fact.
- Do not commit full transcripts or long excerpts to the repo (the sample's rule).
- Talk 02 start: the first ~3 s (00:44:34–00:44:37) are the tail of talk 01 (`speaker-split.md`), so ignore them.

## 4. Rules
- Never invent facts; unknown = «нет данных».
- No causal GEO→profit claims; KPIs are qualified inquiries, sales conversion, CAC and margin.
- No registrations, spending or site changes. Services named in a talk are only listed; any sign-up goes to the Director.
- Work only in worktree `/workspace/NFAI-mission-001` (branch `mission-001`): `git pull --rebase` before the commit, commit only your file, `git push`, verify with `git ls-remote origin refs/heads/mission-001`.
- Executors work in parallel, and neither edits the other's file or the shared files (`claims.md`, `services.md`). Put proposed additions to those files at the end of your file, under «Предложения в claims/services».

## 5. Acceptance criteria
1. All 5 levels are present, and the header carries the ASR warning plus the slide-source line (03: PDF 18 p.; 02: «слайдов нет»).
2. The Level 3 table has at least 8 claims, each with exactly one of the four statuses and a source (timecode and/or slide page or link).
3. Talk 03: at least 5 claims checked against slide page images (page numbers given). Talk 02: every VERIFIED claim names its independent source or the caption match.
4. Level 4 separates "transfers as logic" from "does not transfer (RU stack)"; Level 5 holds actions only through existing services.
5. Report to the Orchestrator: commit hash = `ls-remote` line, file path, line count, number of claims per status, model and effort.

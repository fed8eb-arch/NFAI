# Ручные шаги

Версия 1.1 · 23.11.2026 · ET / PT (America/Los_Angeles)

| ET | Сервис | Стоп | Кто | Действие и обезличенное доказательство |
|---|---|---|---|---|
| 19:26 | NightCafe | CAPTCHA | Пётр / Бадди | Открыть creator.nightcafe.studio вручную и пройти проверку при её появлении. Chrome получил 403 и признаки CAPTCHA. |
| 19:26 | Mistral Le Chat | CAPTCHA | Пётр / Бадди | Войти в существующий аккаунт вручную после проверки. chat.mistral.ai вернул 403 и признаки CAPTCHA; это веб-путь. |
| 19:26 | Leonardo.Ai | CAPTCHA | Пётр / Бадди | Пройти проверку вручную на leonardo.ai и проверить бесплатный веб-план. Chrome получил 403 и признаки CAPTCHA. |
| 19:27 | Microsoft Copilot | Вход | Пётр / Бадди | Войти в существующий Microsoft-аккаунт. Chrome перенаправлен на login.microsoftonline.com; доступ до входа не подтверждён. |
| 19:28 | HeyGen | Подтверждение по почте | Пётр / Бадди | Проверить, пришла ли ссылка от HeyGen, и при наличии открыть её вручную, затем подтвердить план Free. Нажатие Send a secure magic link выполнено один раз; экран отправку не подтвердил. |
| 2026-11-17 20:24 EST | Groq | Ссылка входа по почте | Пётр / Бадди | Открыть ссылку входа из письма Groq вручную. Экран «Check your email» подтвердил отправку. |
| 2026-11-17 22:29 EST | Z.ai | Пароль | Пётр / Бадди | Открыть шаг регистрации вручную. Экран «Enter Your Password», projects/01-services-signup/results/signup-evidence/12.jpg. |
| 2026-11-17 22:29 EST | ElevenLabs | Пароль | Пётр / Бадди | Ввести пароль вручную на шаге «Create an account». Поле «Password», projects/01-services-signup/results/signup-evidence/13.jpg. |
| 2026-11-17 22:29 EST | SeeVio | CAPTCHA | Пётр / Бадди | Открыть форму вручную и пройти проверку. Виджет Cloudflare «Verifying…», projects/01-services-signup/results/signup-evidence/37.jpg. |
| 2026-11-17 22:29 EST | Poe | Проверка браузера | Пётр / Бадди | Для возобновления использовать ручной вход. «Performing security verification», projects/01-services-signup/results/signup-evidence/30.jpg. |
| 2026-11-17 22:29 EST | Ideogram | CAPTCHA | Пётр / Бадди | Открыть страницу вручную и пройти проверку. «Performing security verification», projects/01-services-signup/results/signup-evidence/43.jpg. |
| 2026-11-17 22:29 EST | notrack.ai | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/54.jpg. |
| 2026-11-17 22:29 EST | unrestricted.chat | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/62.jpg. |
| 2026-11-17 22:29 EST | NoFilterGPT | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/63.jpg. |
| 2026-11-17 22:29 EST | uncensored.chat | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/64.jpg. |
| 2026-11-17 22:29 EST | Nastia | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/65.jpg. |
| 2026-11-17 22:29 EST | EroGPT | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/68.jpg. |
| 2026-11-17 22:29 EST | Kupid AI | Пароль | Пётр / Бадди | Ввести пароль вручную. Поле видно на снимке projects/01-services-signup/results/signup-evidence/72.jpg. |

## Бадди · Claude Code для документов NFAI

Статус: **закрыто · ACCEPT**.

Изменения нужны, чтобы Джокер и Бадди могли обрабатывать файлы проекта через Claude Code с бюджетом $0. Claude Code вызывает модель Qwen3-4B через локальный OmniRoute. Текст документа обрабатывается на машине, где запущена модель. Это позволяет извлекать данные и сохранять проверяемые отчёты без подписки Claude Pro.

Проверка Джокера (17.11.2026 22:55 ET): на DOCX и Markdown Claude Code вызвал Read и Write, значения совпали с эталоном; в Markdown первый Read завершился ошибкой, повторный сработал. Порядок в [инструкции](../projects/02-infrastructure/work/claude-local/README.md).

Приёмка Бадди (17.11.2026 23:16–23:25 ET, бокс): оба теста с первой попытки, `failed: 0`, значения совпали с эталоном. Вердикт ACCEPT. В `main` с `268003d` (23.11.2026 15:51 PT); ранее вердикт оставался только в локальном `8ad9cea`. Доказательство: [status.md](../status.md#бадди-проверка-claude-code-локально-2026-11-17).

Это закрывает только приёмку локального документного контура на боксе. Уведомление о Claude Code на Windows-ПК владельца (VIP-Custom PR #1, комментарий 7117202647) в этом пункте не проверялось.

## Бадди · Общий граф памяти NFAI

Граф действует. Команды: [_core/memory/README.md](../_core/memory/README.md). Из корня: `python3 _core/memory/query.py show buddy` и перед коммитом `python3 _core/memory/query.py check`. Приёмка `document-workflow` закрыта (`268003d`). Открытыми для Бадди и Петра остаются ручные шаги регистрации в таблице выше.

## NFAI · Координация после паузы Бадди

Пауза Директора по лимиту завершена 23.11.2026. Джокер работает вместе с Бадди через публичный репозиторий NFAI и Brain Bridge (VIP-Custom PR #1, не сливать). [Порядок работы](../projects/03-telegram-tooling/brief/execution.md) нужен для проверки черновиков перед публикацией и передачи проверенных практик агентам.

Ещё открыто: для продолжения импорта нужен точный адрес VIP Custom; по Telegram в открытой истории видны сообщения с 28 октября, для более ранних дат нужна более ранняя история того же канала. Ручные шаги таблицы выше не закрыты, кроме уже выполненных Петром 17.11 (Groq, Mistral, Viggle, Leonardo; NightCafe — аккаунт создан, онбординг, см. журнал 20:36–21:31 ET).

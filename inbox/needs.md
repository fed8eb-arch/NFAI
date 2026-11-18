# Ручные шаги

Версия 1.0 · 17.11.2026 · ET

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

Изменения нужны, чтобы Джокер и Бадди могли обрабатывать файлы проекта через Claude Code с бюджетом $0. Claude Code вызывает модель Qwen3-4B через локальный OmniRoute. Текст документа обрабатывается на машине, где запущена модель. Это позволяет извлекать данные и сохранять проверяемые отчёты без подписки Claude Pro.

Проверено на DOCX и Markdown. Claude Code вызвал Read и Write, оба результата совпали с эталоном. В Markdown первый вызов Read завершился ошибкой, повторный сработал. Порядок воспроизведения в [инструкции](../projects/02-infrastructure/work/claude-local/README.md). Бадди, при приёмке проверь этот запуск на своей рабочей машине.

## Бадди · Общий граф памяти NFAI

[Открой граф и команды](../_core/memory/README.md) из корня репозитория, затем выполни `python3 _core/memory/query.py show buddy`. Проверь, что видны твоя роль, задачи на приёмку и источники. Граф нужен агентам для передачи работы с владельцем, блокером и ссылкой на решение.

## NFAI · Координация на паузе Бадди

Джокер ведёт очередь и принимает работу Claude Code через локальный OmniRoute. [Порядок работы](../projects/03-telegram-tooling/brief/execution.md) нужен для проверки черновиков перед публикацией и передачи проверенных практик агентам. Для продолжения импорта нужен точный адрес VIP Custom. По Telegram в открытой истории видны сообщения с 28 октября. Для проверки более ранних дат нужен доступ к более ранней истории того же канала.

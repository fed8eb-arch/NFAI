# Режимы ChatGPT для агентства (тариф Plus Основателя)
Версия: v1.1 (доп. гайд Work, источники) | Дата: 2026-11-17 (чтение источников ~13:50–14:30 ET) | Автор: Исследователь рынка (исполнитель) | Срок: 18.11 10:30 ET
Модель/effort исполнителя: Grok Bot (executor), effort: low→medium (см. раздел 13).
Назначение: основа для обучения от Промпт-инженера. Источники: только официальные страницы OpenAI (help.openai.com, openai.com, learn.chatgpt.com — на него ссылаются release notes OpenAI как на «Pricing»). В аккаунт ChatGPT не входил. Сырые копии (частично): `/workspace/pilot/research_raw/chatgpt/`. Бэкап v1.0: `research_raw/chatgpt-modes.bak1.md`.

**ВАЖНО (правило агентства, `rules.md` п.3–6, 13):** аккаунт Plus подключён у Директора. Любая работа в ChatGPT — только через Директора, заявкой агентским сообщением. Ничего в аккаунте не создавать (проекты, задачи) без брифа Директора. Plus — только для проверок и тонкой доводки. Astra — только сверхсложные задачи и по согласованию с Директором.

Обозначения: **[Ф]** — факт с цитатой; **[Р]** — рекомендация (наш вывод, не OpenAI); **UNVERIFIED** — не подтверждено официально; «нет данных» — OpenAI число не публикует. Надёжность: высокая — прямая цитата с help.openai.com/openai.com; средняя — официальная страница, но цифры «оценочные» или страница противоречит себе.

---
## 0. Какие режимы существуют на 17.11.2026 (факты)

[Ф] Основные режимы — Chat, Work, Codex:
> "ChatGPT includes Chat and Work. Codex is available in the desktop app, and Codex Cloud lets you start and continue coding tasks from desktop, web, or mobile. Chat is for fast, conversational assistance and everyday questions. Work is an agent designed for longer, multi-step work and finished deliverables. Codex remains dedicated to software development and technical work."
— https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex (прочитано 2026-11-17; Updated: «13 minutes ago» ≈ 2026-11-17)

| Режим / функция | Статус на 17.11.2026 | Отдельный режим? |
|---|---|---|
| Chat (Instant / Medium / High) | есть | да, переключатель Chat/Work |
| Work | есть (запущен 09.07.2026) | да |
| Codex (desktop, CLI, IDE, web, Codex Cloud) | есть | да, отдельный вид в desktop-приложении |
| Deep research | есть — инструмент внутри Chat и внутри Work/Codex | инструмент, не отдельный режим |
| Agent mode (ChatGPT agent) | **СНЯТ**, заменён Work | — |
| Canvas | **СНЯТ** (с 28.05.2026), заменён writing blocks / code blocks | — |
| Projects | есть — контейнер контекста | нет, оболочка для Chat/Work |
| Scheduled tasks | есть | нет, функция Chat/Work |
| Study mode | есть — инструмент в Chat | нет, инструмент |
| Voice | есть — голосовой интерфейс к Chat/Work/Codex | нет, интерфейс |
| Custom GPTs | планируется вывод из эксплуатации → plugins | — |
| НЕ входит в Plus: GPT-6 Pro в Chat, Extra High, dots, Space/Pages/Slides, Ultrafast | — | — |

Цитаты по снятым режимам:
- Agent: > "ChatGPT agent is no longer available. Use ChatGPT Work for longer, multi-step tasks and finished deliverables." — https://help.openai.com/en/articles/11752874-chatgpt-agent (2026-11-17; Updated «21 days ago» ≈ 2026-10-27). Старые лимиты на той же странице («Plus: 40 messages/month») — **исторические, не действуют**.
- Canvas: > "With this update, canvas will no longer be available in GPT-5.5 Instant or GPT-5.5 Thinking. Writing and coding functionality is now supported directly in chat responses through writing blocks and code blocks." — https://help.openai.com/en/articles/6825453-chatgpt-release-notes , запись 28.05.2026 (2026-11-17). Старая справка по canvas (статья 9930697) отдаёт 404 (проверено 2026-11-17).
- Custom GPTs: > "We're planning to retire custom GPTs across ChatGPT plans and provide a migration path to plugins" — release notes, запись 11.09.2026. Дата вывода для Plus: нет данных. (Страница цен на 17.11 всё ещё пишет у Plus "Projects, scheduled tasks, and custom GPTs".)
- Не входит в Plus: > "Plus includes Astra in Work and Codex, but not GPT-6 Pro in Chat." — https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex (2026-11-17; Updated ≈ 2026-11-17). Dots: > "Dots are rolling out gradually to eligible Pro and Business Premium users" (release notes, 29.09.2026). Space: > "Available to eligible Pro, Business, and Enterprise users" (release notes, 29.09.2026). Ultrafast: > "Ultrafast remains unavailable on Plus, Pro $100 and Business, including through credits." (20001275).

Цена Plus [Ф]: > "ChatGPT Plus is a subscription plan that provides enhanced access to the ChatGPT web app for $20/month." — https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus (2026-11-17; Updated «28 days ago» ≈ 2026-10-20).

**Предстоящее изменение (важно для экономии)** [Ф]: > "Starting in December, Plus, Pro, and Business plans' usage allowance will be shared across ChatGPT and Codex as we bring the agentic capabilities of Work into the main ChatGPT experience. … Your usage for ChatGPT and Codex will be measured in tokens … Instant chat will not draw from your usage." — https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits (2026-11-17; Updated «16 days ago» ≈ 2026-11-01). Точная дата в декабре: нет данных.

---
## 1. Chat

**1. Для чего [Ф]:** > "Chat: Ask questions, search, brainstorm, or get quick conversational help." (20001275)

**2. Лимиты Plus [Ф]:**
- Уровни мышления: > "When GPT-6 is selected, GPT-6 Sol powers Instant, Medium, High, and Extra High; Pro uses GPT-6 Pro, powered by GPT-6 Astra." Таблица по планам: Plus — "Medium and High: Included | Extra High: Not included | Pro: Not included". — https://help.openai.com/articles/20001354 («GPT-6 and other models in ChatGPT», 2026-11-17; Updated ≈ 2026-11-17).
- Также доступен GPT-5.6 Sol (явный выбор) — та же страница.
- Число сообщений Thinking на Plus: **нет данных** (OpenAI не публикует; страница: "Thinking limits depend on your plan"; при исчерпании "ChatGPT may continue with another available model").
- Общий лимит Plus: > "Plus subscriptions may include usage limits such as message caps, especially during high demand. These limits may vary based on system conditions." (6950777)
- Контекст: страница цен — "GPT Reasoning total context window … 256K Plan: Plus" — https://openai.com/chatgpt/pricing/ (2026-11-17; дата обновления не указана). Доля под ввод пользователя меньше: > "The portion available for user input is smaller than the total window".
- Автопереключение Instant→Thinking для Plus отключено: > "We're retiring automatic switching from Instant to Thinking (reasoning) for ChatGPT Plus and Pro users globally." (release notes, 14.09.2026) → effort выбирается вручную.

**3. Задачи агентства [Р]:** короткие вопросы, черновики, мозговой штурм, правка текстов, перевод.
- Контент-менеджер, Маркетолог, Рекламный специалист — черновики постов, офферов, объявлений (Instant/Medium).
- Менеджер по клиентам, Поддержка клиентов — проверка тона ответа клиенту на русском (Instant).
- Аналитик требований, Менеджер продукта — проверка формулировок требований и критериев приёмки (Medium).
- Юрист — первичная вычитка договора/NDA (High; финал всё равно за юристом).
- Промпт-инженер — проверка/доводка системных промптов (Medium → High).

**4. Экономия:**
- [Ф] После декабрьского перехода Instant не расходует общий лимит (цитата выше, 20001625).
- [Ф] Effort выбирается ползунком: Instant → Medium → High (20001354).
- [Р] Начинать с Instant; Medium — если нужен анализ; High — только после неудачи Medium. Один чат на задачу, без повторной вставки контекста (rules.md п.5).

Надёжность: высокая (уровни и цена), «нет данных» по числу сообщений.

---
## 2. Work (агент; заменил agent mode)

**1. Для чего [Ф]:** > "Work: Research a topic, analyze information, or create a document, spreadsheet, presentation, report, or Site." (20001275). Умеет браузер, файлы, подключённые приложения, Scheduled Tasks: > "Work can also run once, repeat on a schedule or trigger, or monitor for changes through Scheduled Tasks." В desktop-приложении — локальные файлы с разрешения.

**2. Лимиты Plus [Ф]:**
- Общий пул с Codex, без фиксированного числа: > "Your allowance does not correspond to a fixed number of messages or tasks. … Work and Codex share the usage allowance included with your plan." (20001516)
- Окна: > "usage limits may apply over a five-hour window and a weekly window. Where both apply, you need allowance remaining in both to continue" (20001516)
- Оценка локальных сообщений за 5 часов на Plus (не гарантия): GPT-6 Astra 5–45; GPT-6.1 Sol 15–160; GPT-6 Sol 15–150; GPT-6 Luna 350–3 000 — 20001516 (2026-11-17). Расширенная таблица: GPT-6.2 Astra 6–50; GPT-6.2 Sol 17–180; GPT-6.1 Terra 35–285 — https://learn.chatgpt.com/docs/pricing (2026-11-17; дата обновления не указана). > "These ranges are estimates, not guaranteed message counts. … Cloud tasks may use more allowance than local messages".
- Число в недельном окне для Plus: **нет данных**.
- Astra на Plus ограничен: > "Plus and Business Standard seats include limited GPT-6 Astra usage, with optional credits for additional usage afterward." (20001275)
- Контекст: > "GPT-6.1 Sol has a default context window of 500,000 tokens in ChatGPT Work and Codex." (20001275)
- Модели в Work на Plus: GPT-6.2 Astra / GPT-6.2 Sol (раскатываются с 17.11.2026), GPT-6 Astra, GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Sol, GPT-6 Luna — 20001275 и learn.chatgpt.com/docs/pricing. Доступность GPT-6.2 на аккаунте Основателя: **UNVERIFIED** (раскатка).
- Reasoning: > "In Work, choose Default to use the reasoning slider or select a specific model to see its available reasoning levels." (20001275)
- Ultrafast на Plus недоступен (цитата в разделе 0).
- Сброс: можно купить мгновенный сброс ("Purchased instant resets are available to eligible personal ChatGPT Plus and Pro accounts", 20001516) — **по правилу нулевых трат (rules.md п.13) не используем**.

**3. Задачи агентства [Р]:** готовые артефакты (документ, таблица, презентация, отчёт, Site), многошаговые исследования.
- Исследователь рынка, ОСИНТ-разведчик — сводные отчёты по рынку/конкурентам из публичных источников (Luna/Terra для сбора, Sol для синтеза).
- Финансовый аналитик — таблицы бюджетов/юнит-экономики (Terra Medium).
- Маркетолог, Контент-менеджер — презентации и кейсы (Sol; Astra только по согласованию).
- Веб-дизайнер — черновой Site/прототип страницы (проверка, не продакшн).
- Тестировщик — финальная проверка отчётов разведки и документов перед выпуском.
- Парсер Telegram — разбор/категоризация списков навыков и техник (Luna).

**4. Экономия:**
- [Ф] Официальные советы (learn.chatgpt.com/docs/pricing): "Control the size of your prompts. Be precise with the instructions you give the agent, but remove unnecessary context." / "Limit source material. Provide only relevant files and, when possible, narrow the sources or date range." / "Match the output to the need. Define the audience, format, and length, and separate required work from optional improvements." / "Limit the number of MCP servers you use."
- [Ф] > "Check Settings → Usage before a large task … Choose the model and reasoning level before starting, and review the result before increasing effort." / "Fast mode provides faster responses and uses more of your included allowance." / "Switching models does not restore allowance in a shared usage pool." (20001516)
- [Ф] > "Lower effort: A useful starting point when you want a faster response or to make your allowance go further. … Higher effort can use more of your allowance and does not always produce a better result." / "Increasing reasoning effort cannot supply missing information or access." (20001516)
- [Ф] OpenAI сам отмечает: > "Lower effort does not mean lower capability across models. For example, Astra at Low effort can outperform Sol at High effort." (20001516) — см. оговорку к правилу Директора в разделе 9.
- [Ф] Официальный гайд «Use ChatGPT Work efficiently» — https://learn.chatgpt.com/codex/prompting#use-work-efficiently (2026-11-17; дата обновления не указана): > "Start with one result you can review: Include only relevant sources and limit the date range when appropriate. Define the audience, output format, and desired length. Separate required work from optional improvements or polish. Ask for a plan when the approach matters. … Narrow or stop the task if it starts doing work you no longer need. Review the first result, refine the instructions, and reuse the workflow when it works." и > "For recurring work, first refine the prompt in a normal chat. After the output is reliable, schedule a task inside that chat."
- [Ф] Для Codex там же: > "enter /plan in the app composer when you want Codex to investigate and propose an approach before editing."
- [Р] Fast mode не включать. Предпочитать локальные задачи облачным, когда возможно (облако дороже по лимиту). Скачивать результат и хранить у себя, не просить «повторить отчёт».

Надёжность: средняя (числа — оценочные диапазоны; страница 20001516 сама себе противоречит: в списке моделей пишет "GPT-5.6 Sol / GPT-5.6 Terra / GPT-5.6 Luna", а в таблице — "GPT-6 Sol / GPT-6 Luna").

---
## 3. Codex

**1. Для чего [Ф]:** > "Codex: Write or debug code, run tests and commands, review changes, or work with a repository." (20001275). Клиенты: desktop (режим Codex), CLI, IDE extension, web; Codex Cloud — задачи на серверах OpenAI: > "Codex Cloud runs coding tasks on OpenAI-managed computers, so tasks can continue while your computer is asleep." (20001275)

**2. Лимиты Plus [Ф]:**
- Тот же общий пул, что у Work (5-часовое + недельное окно, диапазоны — см. раздел 2). > "Work follows the same usage structure as Codex." (20001275)
- Plus по странице цен Codex: > "Plus — Power a few focused coding sessions each week. $20 /month … Codex on the web, in the CLI, in the IDE extension, and on iOS … GPT-6.1 Sol and GPT-6 Luna" — https://learn.chatgpt.com/docs/pricing (2026-11-17).
- Codex Cloud: > "Codex Cloud is available to eligible Plus, all Pro tiers, Business, Enterprise, Healthcare, and Education accounts" — https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan (2026-11-17; дата обновления не показана в копии).
- Генерация картинок в Codex: > "Image generations use included limits 3-5x faster on average" (learn.chatgpt.com/docs/pricing).
- Вход через ChatGPT = лимит Plus; через API-ключ = оплата по API: > "Signing in to Codex with ChatGPT uses your ChatGPT plan's usage and billing. Using your own API key uses API pricing." (20001275) — **API-ключ не используем (нулевые траты)**.
- Остаток в CLI: > "you can use /status" (learn.chatgpt.com/docs/pricing).

**3. Задачи агентства [Р]:** только код и техника — и только как проверка/доводка (rules.md п.13), основная разработка — на бесплатных моделях.
- Разработчик, Разработчик интеграций — ревью/отладка трудного бага, тесты (Sol Low→Medium; Astra только по согласованию).
- DevOps-инженер — проверка конфигов деплоя, скриптов.
- Тестировщик — ревью изменений перед подписанием.
- Архитектор — проверка реализуемости спецификации на коде (не проектирование).

**4. Экономия:**
- [Ф] > "Reduce the size of your AGENTS.md. If you work on a larger project, you can control how much context you inject through AGENTS.md files by nesting them within your repository." и > "Every MCP server adds more context to your messages and uses more of your limit. Disable MCP servers when you don't need them." (learn.chatgpt.com/docs/pricing)
- [Ф] > "If usage is higher than expected, consider whether a smaller model or tighter task scope would still produce a useful result." (там же)
- [Ф] Auto-review не тратит лимит: > "auto-review safety checks are free and don't count toward your plan's usage limits" (11369540).
- [Р] Задача = один модуль/один баг; давать путь к файлам, а не весь репозиторий; локально, а не в Cloud, если не нужна долгая работа.

Надёжность: средняя (оценочные диапазоны).

---
## 4. Deep research (инструмент в Chat и в Work/Codex)

**1. Для чего [Ф]:** > "Use deep research for multi-step or in-depth questions that require combining and analyzing information from multiple sources, especially when you want explicit control over which sources are used. For quick lookups or short conversations, standard chat may be faster." — https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt (2026-11-17; Updated «29 days ago» ≈ 2026-10-19). Выдаёт отчёт со ссылками; экспорт Markdown, Word, PDF.

**2. Лимиты Plus [Ф]:**
- В Chat — отдельный месячный счётчик задач: > "Deep research usage varies by plan. Your in-product usage counter shows your remaining tasks. For plans with a fixed monthly allowance, it resets every 30 days from the date of your first use." (10500283). **Число задач для Plus: нет данных** (на странице Plus только "Deep Research tools (where available)"; на странице цен — "Expanded deep research").
- В Work — из общего пула Work/Codex: > "In Work, deep research uses your existing Work/Codex allowance or credits. It does not use the separate deep research task allowance in Chat." — help-lb.openai.com/en/articles/10500283 (зеркало справки OpenAI, найдено поиском 2026-11-17; на основной странице этого абзаца в моей копии нет → **UNVERIFIED** до повторной сверки).
- Страны: > "Does deep research work in all countries? No. Availability depends on your plan and your country or territory." (10500283)
- Данные: > "Conversations using deep research follow the same data handling and privacy settings as regular ChatGPT conversations." (10500283)

**3. Задачи агентства [Р]:** только крупные исследования, где нужен отчёт с источниками.
- Исследователь рынка — обзоры рынка/конкурентов (с фильтром сайтов).
- ОСИНТ-разведчик, Разведка (Ватикан), Орденская разведка — сбор по открытым источникам (только публичные данные, по правилам безопасности).
- SEO-специалист — анализ ниши/конкурентов в поиске.
- Профессор — подборка материалов для обучения.

**4. Экономия:**
- [Ф] > "Use search for quick facts, and use deep research for depth and thoroughness." / "If time is critical, use search or standard chat" (10500283)
- [Ф] Ограничение источников: "Sites > Manage sites … restrict research to only the websites or domains you enter" (10500283).
- [Р] Сначала исследование делаем бесплатными средствами; deep research — только финальная сверка. Перед запуском — готовый план и структура отчёта в одном сообщении, чтобы не тратить задачу на уточнения. Отредактировать план до старта.

Надёжность: высокая (механика), «нет данных» по числу задач.

---
## 5. Projects (контейнер, не режим)

**1. Для чего [Ф]:** > "Projects keep related chats, files, and instructions together. ChatGPT can use that context to support ongoing work, such as writing, research, or planning." — https://help.openai.com/en/articles/10169521-projects-in-chatgpt (2026-11-17; Updated «16 hours ago» ≈ 2026-11-16/17). Из проекта можно запустить Chat или Work: > "From a project, choose Chat to start a new chat, or choose Work to start a Work chat using the project's context." (20001275)

**2. Лимиты Plus [Ф]:** > "The number of files you can upload depends on your plan." (10169521). Число файлов для Plus: **нет данных** (ссылается на «Plans and limits», не прочитано). Отдельного лимита сообщений нет — действуют лимиты Chat/Work. Study mode в Projects недоступен (11780217).

**3. Задачи агентства [Р]:** по правилу rules.md п.4 проекты **не создаём без брифа Директора** (хранение ещё настраивается). Когда разрешат — один проект на внутреннее направление (например, «Исследования рынка», «Промпты агентов») с инструкцией проекта вместо повторной вставки контекста.

**4. Экономия [Р]:** инструкции проекта и файлы-источники вместо копирования контекста в каждый чат; сохранять удачные ответы через "Add to project sources" ([Ф] функция описана в 10169521).

Надёжность: высокая (функция), «нет данных» (лимит файлов).

---
## 6. Scheduled tasks (функция Chat/Work)

**1. Для чего [Ф]:** > "ChatGPT can run one-time or recurring tasks, monitor for changes, and respond to supported events when available." — https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt (2026-11-17; Updated «17 days ago» ≈ 2026-10-31).

**2. Лимиты Plus [Ф]:** > "Active task limits depend on the plan: 3 for Free and Go, 5 for Plus, 10 for Business and Edu, and 15 for Pro and Enterprise." / "Eligible paid plans support recurring tasks up to once per hour and exact delivery times. Event-triggered tasks can run up to 30 times per hour and 720 times per day" / > "A completed scheduled task in Chat can use your plan's usage allowance or workspace credits even when it does not post an update." (10291617)

**3. Задачи агентства [Р]:** не создаём без брифа Директора (rules.md п.4). Кандидат — ежедневный мониторинг цен/условий сервисов для Контролёра расходов и Исследователя рынка, если Директор одобрит.

**4. Экономия [Ф/Р]:** [Ф] > "To manage future background usage, pause tasks you no longer need or reduce how often they run." [Р] Частота — не чаще раза в день; без пустых прогонов.

Надёжность: высокая.

---
## 7. Study mode (инструмент Chat)

**1. Для чего [Ф]:** > "Study mode is a learning experience in ChatGPT that helps you build a deeper understanding of a topic." — https://help.openai.com/en/articles/11780217 (2026-11-17; Updated «29 days ago» ≈ 2026-10-19).
**2. Лимиты Plus [Ф]:** > "Study mode uses the same ChatGPT plan, model, message, and rate-limit rules that apply outside study mode. … Study mode does not add extra messages". Недоступен в Temporary Chats, GPTs, Projects.
**3. Задачи агентства [Р]:** Профессор, ИИ-ментор — проверка учебных материалов/тестов для агентов (редко; основное обучение — на бесплатных моделях).
**4. Экономия [Р]:** не использовать как отдельный канал — лимиты общие с Chat.
Надёжность: высокая.

---
## 8. Voice (интерфейс) — кратко
[Ф] > "Voice: Talk naturally with Work on web or mobile, or with Work or Codex in the ChatGPT desktop app, and ask it to work on a task." / "On web and mobile, Voice in Work uses minutes from your daily Voice allowance. Work tasks follow the same pricing whether you start them by speaking or typing." (20001275). Дневные минуты для Plus: нет данных. [Р] Агентству не нужен (агенты работают текстом).

---
## 9. Экономия: общие правила

**Официальные (OpenAI) [Ф]** — цитаты выше: точные короткие промпты без лишнего контекста; только нужные файлы; формат и длина ответа заданы заранее; меньше MCP/коннекторов; проверить Settings → Usage до большой задачи; выбрать модель и effort до старта и смотреть результат, прежде чем повышать; Fast mode тратит больше; смена модели не возвращает лимит общего пула; Instant (с декабря) не тратит общий лимит.

**Постоянное правило Директора (rules.md п.7–8) [правило агентства]:**
1. Сначала повышаем reasoning effort: low → medium → high. Только если high не помог — меняем модель.
2. В каждом отчёте указываем модель и effort (например: «GPT-6.1 Sol, Medium»).
Оговорка [Ф/Р]: OpenAI пишет, что "Astra at Low effort can outperform Sol at High effort" (20001516). Это не отменяет правило Директора, но если Sol на High не справился — следующий шаг Astra Low (по согласованию с Директором, п.6), а не повтор Sol High.

**Наши рекомендации [Р]:**
- Plus — только для проверки и доводки готового результата (п.13); черновики — на бесплатных моделях (Qwen, DeepSeek и др. из `catalog.md`).
- Один чат на задачу; не возвращаться в длинные старые чаты (длинный контекст тратит лимит).
- Заявка Директору = готовый промпт + файлы + ожидаемый формат + режим + модель + effort, чтобы Директор выполнил за один заход.
- Не покупать кредиты и сбросы (нулевые траты).
- Данные: [Ф] > "OpenAI may use conversations to improve model performance and safety. You can opt out" (6950777). Включено ли обучение на аккаунте Основателя — **UNVERIFIED** (в аккаунт не входили) → вопрос Директору. До ответа — без клиентских и персональных данных.

---
## 10. Сводная таблица

| Режим | Назначение | Лимиты Plus | Задачи агентства (роли) | Экономия | Источник / дата | Надёжность |
|---|---|---|---|---|---|---|
| Chat | быстрые вопросы, черновики | Instant/Medium/High; без Extra High и Pro; число сообщений — нет данных; контекст 256K | Контент, Маркетолог, Рекламный спец., Менеджер по клиентам, Поддержка, Аналитик требований, Юрист, Промпт-инженер | Instant по умолчанию; с декабря Instant не тратит лимит | help 20001354, 6950777, 20001625; openai.com/chatgpt/pricing; 2026-11-17 | высокая / нет данных по числам |
| Work | агент: исследования, документы, таблицы, презентации, Sites | общий пул с Codex; 5 ч + неделя; оценка за 5 ч: Astra 5–45, 6.1 Sol 15–160, 6.1 Terra 35–285, Luna 350–3000; Astra ограничен; контекст 6.1 Sol 500K | Исследователь рынка, ОСИНТ, Фин. аналитик, Маркетолог, Контент, Веб-дизайнер, Тестировщик, Парсер Telegram | Luna/Terra для рутины; effort low→high; без Fast; узкие источники | help 20001275, 20001516; learn.chatgpt.com/docs/pricing; 2026-11-17 | средняя |
| Codex | код, тесты, ревью, репозиторий | тот же пул; "a few focused coding sessions each week"; Codex Cloud есть | Разработчик, Разработчик интеграций, DevOps, Тестировщик, Архитектор (проверка) | маленький AGENTS.md, меньше MCP, локально, /status | help 20001275, 11369540; learn.chatgpt.com/docs/pricing; 2026-11-17 | средняя |
| Deep research | отчёт со ссылками из многих источников | в Chat — месячный счётчик задач (число — нет данных), сброс 30 дней; в Work — из общего пула (UNVERIFIED) | Исследователь рынка, ОСИНТ, Разведка, SEO, Профессор | только финальная сверка; план заранее; фильтр сайтов | help 10500283; 2026-11-17 | высокая / нет данных |
| Projects | контейнер контекста | лимит файлов — нет данных | создавать только по брифу Директора | инструкции проекта вместо повторов | help 10169521; 2026-11-17 | высокая |
| Scheduled tasks | повторяющиеся задачи, мониторинг | 5 активных; до 1 раза в час; события 30/ч, 720/день | Контролёр расходов, Исследователь рынка (по брифу) | реже запуски, пауза ненужных | help 10291617; 2026-11-17 | высокая |
| Study mode | обучение | лимиты как в Chat | Профессор, ИИ-ментор | не отдельный канал | help 11780217; 2026-11-17 | высокая |
| Agent mode | — СНЯТ, заменён Work | — | — | — | help 11752874; 2026-11-17 | высокая |
| Canvas | — СНЯТ (28.05.2026) | — | — | writing blocks в Chat | release notes 28.05.2026; 2026-11-17 | высокая |

---
## 11. Шпаргалка маршрутизации (для обучения Промпт-инженером)

0. **Нужен ли ChatGPT вообще?** Сначала бесплатные модели. Plus — только проверка/доводка (п.13). Заявка — Директору агентским сообщением; сами в аккаунт не ходим.
1. Короткий ответ, правка текста, идея → **Chat, Instant**.
2. Нужен разбор/логика → **Chat, Medium**; не вышло → **High**.
3. Нужен готовый файл (документ, таблица, презентация, отчёт, Site) или несколько шагов с браузером → **Work**, модель Luna/Terra, effort Low.
4. Нужно исследование с источниками → Chat + **deep research** (с фильтром сайтов и готовым планом) или Work.
5. Код, тесты, ревью, репозиторий → **Codex**, Sol Low → Medium → High.
6. Не справилось на High → смена модели вверх (Terra → Sol → Astra). **Astra — только по согласованию с Директором.**
7. Повторяющаяся задача → Scheduled task **только по брифу Директора** (лимит 5).
8. Не запрашивать: agent mode и canvas (сняты), GPT-6 Pro/Extra High/Ultrafast/dots/Space (нет в Plus), покупку кредитов/сбросов (нулевые траты).
9. В каждой заявке и отчёте: режим + модель + effort + что проверено.
10. Без клиентских и персональных данных, пока Директор не подтвердит настройку обучения.

---
## 12. UNVERIFIED и «нет данных»
- UNVERIFIED: deep research в Work тратит общий пул Work/Codex, а не счётчик Chat (цитата только с зеркала help-lb.openai.com).
- UNVERIFIED: GPT-6.2 Astra/Sol уже видны на аккаунте Основателя (раскатка с 17.11).
- UNVERIFIED: включено ли «Improve the model for everyone» на аккаунте Основателя.
- Нет данных: число сообщений Chat Thinking на Plus; число задач deep research на Plus в месяц; недельный лимит Work/Codex на Plus; лимит файлов в Projects на Plus; дневные минуты Voice; точная дата декабрьского объединения лимитов; дата вывода custom GPTs для Plus.
- Противоречие на официальной странице 20001516: модели названы и "GPT-5.6 Sol/Terra/Luna", и "GPT-6 Sol/Luna".
- Источник learn.chatgpt.com — домен OpenAI вне списка брифа (help.openai.com/openai.com), но на него ссылаются release notes OpenAI (26.10.2026: «For current usage estimates, see: Pricing»). Надёжность — средняя.

## 13. Что проверено исполнителем
Прочитаны 2026-11-17: openai.com/chatgpt/pricing; help.openai.com статьи 20001275, 20001516, 20001625, 20001354, 6950777, 10500283, 11752874, 10169521, 10291617, 11780217, 11369540; release notes 6825453 (записи 09.07, 25.08, 14.09, 11.09, 22.09, 29.09, 07.10, 15.10, 16.10, 26.10, 29.10, 17.11.2026 и 28.05.2026); learn.chatgpt.com/docs/pricing и learn.chatgpt.com/codex/prompting (раздел «Use ChatGPT Work efficiently»). Статья canvas 9930697 — 404. Сырые копии на диске (`research_raw/chatgpt/`): release notes, 11369540, canvas-404, learn pricing, learn prompting; остальные статьи прочитаны через веб-чтение (WebFetch) 2026-11-17, локальных копий нет (curl/r.jina.ai заблокированы). В аккаунт ChatGPT не входил.

Модель/effort исполнителя: Grok Bot (executor), effort: low→medium (сбор — low, сверка цитат — medium).

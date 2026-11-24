# Очередь регистраций: все сервисы каталога

Версия: v1.1 | 17.11.2026 15:52 ET | Ведёт: Оркестратор
Источники (только они): `/workspace/pilot/catalog.md` (все таблицы, 72 уникальных сервиса = 30+22+20; Табл. 2b — служебные дубли, в очередь не входят отдельными строками, но факты о веб-free из неё учтены), `/workspace/pilot/accounts.md`.
Никаких фактов вне этих файлов. Неизвестно в источнике = «нет данных».
Проверка Codex (low): `/workspace/pilot/signup-queue-codex-verdict.txt` — VERDICT ISSUES; явные ошибки исправлены один раз (v1.1), Codex повторно не запускался.

## Правила колонок и полос

- **URL** — как в колонке URL каталога (это официальный URL сервиса, не обязательно `/signup`).
- **Value / Ease** — из V/E/R таблиц 1–2. У Treblo в каталоге «4 (веб) / 3 / 2» → Value=4, Ease=3. В таблице 3 колонок Value/Ease нет → «нет данных».
- **signup method** — в каталоге отдельной колонки нет (значения API/web/email-link/browser-only почти нигде не названы). Исключение: в accounts.md у Groq зафиксирован magic link → `email-link`. Остальные — «нет данных». Не выводим метод из названия таблицы (API-трек / ручной трек).
- **phone / card** — `y` / `n` / `нет данных` только по явным формулировкам каталога или accounts.md. Телефон Mistral («по сторонним данным») официально не подтверждён → «нет данных». «Карта для free — нет (сторонние данные)» у Magic Hour и «Free навсегда, без карты» у Bolt.new → `card=n`. Телефон Poe, Google AI Studio и Alibaba (mobile на следующем шаге) — из accounts.md (`y`). У Perplexity в топ-10 каталога прямо: «нужна ли карта — нет данных».
- **Полосы (lane):**
  - `EMAIL` — карта и телефон не известны как нужные (оба не `y`) → регистрация с нашей почты. У Duck.ai в каталоге «аккаунт не нужен» — полоса `EMAIL (аккаунт не нужен)`, регистрировать нечего.
  - `HANDOFF` — в источниках известно, что нужен телефон, QR или карта → один список на передачу экрана Основателю.
  - `X` — исключить, с причиной: вся таблица 3 Uncensored/18+; ToS запрещает автоматизацию (и Решение Директора «только вручную», Arena.ai); Решение Директора «только личное / не для клиентских работ» (Dola); 💳 paid-only / нет бесплатного тарифа, если в каталоге (строка или Табл. 2b) не описан бесплатный объём; явная пометка каталога «Не использовать (регион)» (Meta AI). Флага 💳 недостаточно, если в той же строке лимит и оплата — «нет данных» (Ideogram → EMAIL).
  - `DONE` / `BLOCKED` / `DROPPED` — статус из accounts.md (OpenRouter создан; Groq signup_blocked; Z.ai dropped).
  - Poe и Google AI Studio в accounts.md со статусом blocked: phone, но полоса — `HANDOFF` (нужен экран Основателя), не BLOCKED.
  - Alibaba в accounts.md: аккаунт создан 15:50, следующий шаг — mobile verification → полоса `HANDOFF`, `phone=y` (не IN_PROGRESS).
- Если применимы и X, и HANDOFF (нужен телефон, но сервис исключён) — полоса `X`, телефон всё равно `y` (Dola).
- 💳 у API при этом в каталоге/Табл. 2b есть бесплатный веб, playground, ChatGPT Free, DeepSeek Chat, Perplexity Free, Grok Free, TTS HeyGen до 30.11, Scenario 50 CU/сутки, Krea 100 CU/сутки, SeeVio «free video» — это не «нет бесплатного тарифа», полоса не X только из-за 💳 API.
- GitHub есть в accounts.md, но нет в catalog.md — в эту таблицу не входит.
- Сортировка: Value по убыванию, затем Ease по убыванию; «нет данных» в конце; при равенстве — номер таблицы каталога, затем исходный #.

## Таблица

| # | service | official signup URL (from catalog) | Value | Ease | signup method | phone | card | lane | status from accounts.md |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Google Gemini API / AI Studio (+ приложение Gemini, Flow) | https://aistudio.google.com | 5 | 4 | нет данных | y | нет данных | HANDOFF | blocked: phone — передача экрана отклонена Основателем 15:09; ждёт его нового решения |
| 2 | Arena.ai (бывш. LMArena) | https://arena.ai | 5 | 4 | нет данных | нет данных | нет данных | X: Решение Директора 17.11.2026 13:32 ET — только вручную, только внутренние задачи, автоматизация запрещена; ToU 23.02.2026 — запрет программного/автоматизированного доступа, не более одного аккаунта | — |
| 3 | OpenRouter | https://openrouter.ai | 4 | 5 | нет данных | нет данных | n | DONE | created 14:11 (email verified); баланс $0.00, 0 транзакций; 2 ключа «Default key» (лимит $100 каждый, не скопированы) — оставить, не отзывать (решение Основателя через Директора 14:18); логин в Vault «OpenRouter (agency)» |
| 4 | Groq (GroqCloud) | https://console.groq.com | 4 | 5 | email-link | нет данных | n | DONE (API pilot) | 24.11: Free plan and Global ZDR observed; synthetic Claude Read/Write, MCP history and initial combo fallback verified from Founder-relayed evidence. Original blocked signup superseded. Current billing/quota not independently queried. |
| 5 | Duck.ai (DuckDuckGo) | https://duck.ai | 4 | 5 | нет данных | n | n | EMAIL (аккаунт не нужен) | — |
| 6 | Bolt.new | https://bolt.new | 4 | 5 | нет данных | нет данных | n | EMAIL | — |
| 7 | Design Arena (по указанию основателя) | https://www.designarena.ai | 4 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 8 | NotebookLM (Gemini Notebook) | https://notebooklm.google.com | 4 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 9 | Treblo (Melodia API + веб) | https://treblo.com | 4 | 3 | нет данных | нет данных | нет данных | EMAIL | — |
| 10 | Canva AI (Magic Studio) | https://www.canva.com | 3 | 5 | нет данных | нет данных | нет данных | EMAIL | — |
| 11 | Lovable | https://lovable.dev | 3 | 5 | нет данных | нет данных | нет данных | EMAIL | — |
| 12 | Z.ai (GLM) | https://z.ai (docs.z.ai) | 3 | 4 | нет данных | нет данных | нет данных | DROPPED | dropped 15:14 (Founder t343u): slider-captcha; форма заполнена, не отправлена; Vault 5158815 |
| 13 | ElevenLabs | https://elevenlabs.io | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 14 | Google Flow | https://labs.google/fx/tools/flow/ | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 15 | Tensor.Art | https://tensor.art | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 16 | SeaArt AI | https://www.seaart.ai | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 17 | Dreamina (CapCut) | https://dreamina.capcut.com | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 18 | Adobe Firefly | https://firefly.adobe.com | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 19 | Microsoft Copilot | https://copilot.microsoft.com | 3 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 20 | Alibaba Cloud Model Studio (Qwen) | https://www.alibabacloud.com/product/modelstudio (чат: chat.qwen.ai) | 3 | 3 | нет данных | y | нет данных | HANDOFF | account CREATED 15:50; next step asks mobile (/basic/security/mobile) → Model Studio activation + Free Quota Only = Founder handoff list; Vault 5164459 |
| 21 | Dola (бывш. Cici) | https://dola.com | 3 | 3 | нет данных | y | нет данных | X: ToS — только private and non-commercial use, запрет автоматизации сверх лимитов и скрейпинга; Решение Директора 17.11.2026 13:32 ET — только личное использование, не для клиентских работ | — |
| 22 | Suno | https://suno.com | 2 | 5 | нет данных | нет данных | нет данных | EMAIL | — |
| 23 | v0 (Vercel) | https://v0.app | 2 | 5 | нет данных | нет данных | нет данных | EMAIL | — |
| 24 | Magic Hour | https://magichour.ai | 2 | 4 | нет данных | нет данных | n | EMAIL | — |
| 25 | Viggle (+ веб) | https://viggle.ai | 2 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 26 | Udio | https://www.udio.com | 2 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 27 | NightCafe | https://creator.nightcafe.studio | 2 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 28 | Microsoft Designer | https://designer.microsoft.com | 2 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 29 | Vidnoz AI | https://ru.vidnoz.com | 2 | 4 | нет данных | нет данных | нет данных | EMAIL | — |
| 30 | Poe API (Quora) | https://poe.com | 2 | 3 | нет данных | y | нет данных | HANDOFF | blocked: phone — передача экрана отклонена Основателем 15:09; ждёт его нового решения |
| 31 | HeyGen | https://developers.heygen.com | 2 | 3 | нет данных | нет данных | нет данных | EMAIL | — |
| 32 | Mistral AI Studio (+ Le Chat) | https://console.mistral.ai | 2 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 33 | Hugging Face Inference Providers (+ HuggingChat) | https://huggingface.co | 1 | 5 | нет данных | нет данных | нет данных | X: 💳 Free users: None; HuggingChat — у free-аккаунта кредитов нет | — |
| 34 | aihere.ru (шаблоны промптов) | https://aihere.ru/templates/ | 1 | 5 | нет данных | нет данных | нет данных | EMAIL | — |
| 35 | DeepSeek API (+ chat.deepseek.com) | https://platform.deepseek.com | 1 | 3 | нет данных | нет данных | нет данных | EMAIL | — |
| 36 | uncensored.com (Developers API) | https://uncensored.com/api | 1 | 3 | нет данных | нет данных | нет данных | X: 💳 бесплатных кредитов в docs нет, предоплаченный баланс | — |
| 37 | SeeVio (+ веб) | https://seevio.ai | 1 | 3 | нет данных | нет данных | нет данных | EMAIL | — |
| 38 | Meta AI | https://www.meta.ai | 1 | 3 | нет данных | нет данных | нет данных | X: в каталоге официально недоступен в РФ; лучшее применение — «Не использовать (регион)» | — |
| 39 | xAI API (+ grok.com) | https://console.x.ai | 1 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 40 | OpenAI API (+ ChatGPT) | https://platform.openai.com | 1 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 41 | Perplexity API (Sonar/Agent API) | https://docs.perplexity.ai | 1 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 42 | Leonardo.Ai | https://leonardo.ai | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 API access отдельно, нужно купить API-кредиты; бесплатный веб-объём в каталоге не подтверждён | — |
| 43 | Ideogram | https://ideogram.ai | 1 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 44 | Recraft | https://www.recraft.ai | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 нет бесплатного API: pay-as-you-go; веб-free не проверялся | — |
| 45 | Kling AI | https://kling.ai/dev | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 нет бесплатного API; веб-free не проверялся | — |
| 46 | MiniMax (Hailuo) | https://platform.minimax.io | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 бесплатной квоты на странице цен нет (Recharge); веб-free не проверялся | — |
| 47 | PixVerse | https://platform.pixverse.ai | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 бесплатных API-кредитов не найдено; веб-free не проверялся | — |
| 48 | Vidu | https://platform.vidu.com | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 кредиты платные; веб-free не проверялся | — |
| 49 | Hedra | https://www.hedra.com | 1 | 2 | нет данных | нет данных | нет данных | X: 💳 нет: кошелёк $0, без пополнения 402; кредиты Studio не оплачивают API | — |
| 50 | Krea | https://www.krea.ai | 1 | 2 | нет данных | нет данных | нет данных | EMAIL | — |
| 51 | Freepik (API → Magnific API) | https://www.freepik.com | 1 | 1 | нет данных | нет данных | нет данных | X: 💳 API на кредитах платных планов; «Unlimited» в вебе не покрывает API | — |
| 52 | Scenario | https://www.scenario.com | 1 | 1 | нет данных | нет данных | нет данных | EMAIL | — |
| 53 | uncensored.com (веб; API — Табл. 1 #15) | https://uncensored.com | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 54 | notrack.ai | https://notrack.ai | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 55 | aiwithnorestrictions.com | https://aiwithnorestrictions.com/chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 56 | getnotrack.com | https://getnotrack.com/chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 57 | deepshi.ai | https://deepshi.ai/chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 58 | unfilteredai.ai | https://unfilteredai.ai/chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 59 | uncensored.ai | https://uncensored.ai/chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 60 | uncensoredgpt.ai | https://uncensoredgpt.ai/ru | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 61 | Secrypt | https://www.secrypt.space | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 62 | unrestricted.chat | https://unrestricted.chat | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 63 | NoFilterGPT | https://nofiltergpt.com/chat/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 64 | uncensored.chat | https://uncensored.chat/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 65 | Nastia | https://www.nastia.ai/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 66 | SpicyChat | https://spicychat.ai/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 67 | Flirton | https://flirton.ai | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 68 | EroGPT | https://erogpt.ai/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 69 | HoneyChat | https://honeychat.bot/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 70 | Janitor AI | https://janitorai.com/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 71 | Secrets AI | https://www.secrets.ai/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |
| 72 | Kupid AI | https://www.kupid.ai/ | нет данных | нет данных | нет данных | нет данных | нет данных | X: таблица 3 Uncensored / 18+ (рекомендация каталога — не использовать) | — |

## Сводка полос

- EMAIL: 33
- HANDOFF: 3
- X: 33
- DONE: 1
- BLOCKED: 1
- DROPPED: 1
- Всего строк: 72 (ожидалось 72)

## 24.11.2026 — сверка очереди с действующим пилотом

Проверены номера: ровно 72 строки, уникальные 1–72, без пропусков. Исторический блок регистрации Groq заменён текущей приёмкой API-пилота на основании status.md. Старые блокеры входа GitHub и Supabase не означают отсутствия текущего доступа: GitHub metadata/admin read подтверждён для обоих репозиториев; Supabase MCP вернул единственный проект WireReady, не NFAI. Старая очередь не подтверждает актуальные тарифы/доступ по остальным позициям. OpenRouter/Gemini/Cloudflare/Mistral не считаются принятыми резервами текущего Combo; NVIDIA Trial только для прототипов. Не повторять регистрации существующих аккаунтов, обход CAPTCHA/телефона/региональных ограничений, активацию платного API или создание новых ключей без нужды. Полная фазовая приёмка открыта.


## 24.11.2026 — A07: reconcile registration lanes with actual recorded outcomes

All 72 row IDs covered once. Sources: canonical queue, catalog.md, accounts.md and later status.md entries plus current Groq acceptance. Historical outcomes are not a new login, entitlement or billing check. Existing row lanes preserve original decisions; do not treat EMAIL as authorization to re-register. Corrected lane summary from actual rows: HANDOFF 3, X 33, DONE 2, EMAIL 33, DROPPED 1.

| Operational classification | Row IDs | Count |
|---|---|---:|
| Current API evidence (not current balance) | 4 | 1 |
| Historical API success; do not re-register | 1 | 1 |
| Historical created/opened account, API entitlement not established; do not re-register | 3, 6, 7, 8, 9, 10, 11, 15, 16, 17, 18, 22, 25, 27, 32, 42 | 16 |
| Existing manual/no-account route, not accepted API | 5 | 1 |
| Existing HOLD or handoff; no automatic retry | 12, 19, 20, 30, 31 | 5 |
| Existing X restrictions, not an activation queue | 2, 21, 33, 36, 38, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72 | 32 |
| Unverified; check business need and official free entitlement before any registration | 13, 14, 23, 24, 26, 28, 29, 34, 35, 37, 39, 40, 41, 43, 50, 52 | 16 |

In particular #1 later historical Gemini API HTTP 200 supersedes the old phone blocker for that historical run; #7 Design Arena remains manual/internal only, #42 historical account is not API access, #17 historical zero credits, #27 historical creation does not lift earlier HOLD, #32 direct Mistral account is distinct from NVIDIA-hosted Mistral in the current combo. #20 Qwen remains blocked pending confirmed free-only entitlement; #30 phone handoff remains stopped. #3 no top-up. #53–72 remain excluded from agency operations. No registration, account changes, credentials, spend or API calls in this reconciliation. Actual current account-level entitlement and applicable commercial terms remain open. Next: use existing approved providers for current work; only investigate unverified rows when a concrete task needs them.

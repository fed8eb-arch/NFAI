# Легальные пути доступа (без обходов) — legit-paths

Версия: v0.1 | Дата проверки: **17.11.2026** (America/New_York, ET) | Готовит: Исследователь рынка | Бриф Оркестратора, срок 17:30 ET

Правила: только публичные страницы и уже лежащие файлы `pilot/` (`bonuses.md`, `catalog.md`, `accounts.md`, `signup-queue.md`). Регистраций, входов и любых обходов (капча, IP/VPN/прокси, виртуальные номера) не было и не предлагается. Неизвестно = «нет данных»; недоказанное = UNVERIFIED. Сырые копии: `/workspace/pilot/research_raw/legit-paths/`. Effort: **lowest** (без глубокой перепроверки каждого сервиса). Модель: **Grok Bot**.

## 1. Класс A: регистрация без капчи и без телефона

Источники класса: `bonuses.md` (A и A/B) и сопоставимые бесплатные строки `catalog.md` (email, без обязательной карты; не 💳).

Важное ограничение: **публичные docs почти никогда не пишут «капчи нет»**. Поэтому узкий список «подтверждено официальной страницей: нет капчи и нет телефона» — **пуст**. Ниже — кандидаты с тем, что известно. Строки, где капча или телефон = «да» или «нет данных», в фильтр «точно без капчи и телефона» не проходят.

Приоритет для строк catalog: Hop из catalog (если есть), оценка V/E/R, при наличии — очередь из `signup-queue.md` (P0/P1/…). Для сервисов только из bonuses — «не задан в catalog», если очередь их не знает.

| service | source file | captcha at sign-up | phone at sign-up | priority | link |
|---|---|---|---|---|---|
| OpenRouter (:free) | bonuses.md (A); catalog.md табл. 1 #1 | нет данных на публичных страницах. На практике 17.11 аккаунт агентства создан (email verified), капча в accounts.md не отмечена — это не доказательство «капчи никогда нет» | в catalog/bonuses: нет данных. На практике 17.11 телефон не потребовался (accounts.md) | catalog Hop 3; V/E/R 4/5/2; очередь P1; статус DONE | https://openrouter.ai |
| Groq (Free) | bonuses.md (A); catalog.md табл. 1 #2 | нет данных на публичных страницах | bonuses/catalog: нет данных. Регистрация агентства 17.11 дошла до magic link, телефон не зафиксирован; дальше signup_blocked (IP/region likely), Ref 39e18c6e (accounts.md) | catalog Hop 1; V/E/R 4/5/3; очередь P1; статус BLOCKED (IP) | https://console.groq.com |
| Google AI Studio / Gemini API Free | bonuses.md (A); catalog.md табл. 1 #3 | нет данных | catalog: Google-аккаунт, 18+, «some projects need verification». signup-queue: Google может запросить телефон (нет данных). accounts.md: blocked: phone, 17.11 15:09 | catalog Hop 5; V/E/R 5/4/4; очередь P0; статус HANDOFF (телефон) | https://aistudio.google.com |
| Z.ai (GLM Flash) | catalog.md табл. 1 #4 (бесплатные Flash; карта для free — нет данных) | **да** (факт агентства, не дока): slider-captcha, 7 неудачных попыток, dropped 15:14 t343u (accounts.md, status.md) | catalog/очередь: нет данных | catalog Hop 2; V/E/R 3/4/2; очередь P1; статус DROPPED (капча) | https://z.ai |
| Hugging Face (Hub / Spaces Free) | bonuses.md (A); catalog.md табл. 1 #8 | нет данных | catalog/bonuses: нет данных (Email) | catalog V/E/R 1/5/2; очередь не в P0–P2 (в catalog у Free users нет inference credits) | https://huggingface.co |
| Cloudflare (Workers/Pages/R2/Workers AI) | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://dash.cloudflare.com/sign-up ; тариф: https://developers.cloudflare.com/workers/platform/pricing/ |
| GitHub Free / Copilot Free | bonuses.md (A) | нет данных на публичных страницах. accounts.md: signup github.com/signup → HTTP 403 (вероятно блок бота/IP), аккаунт не создан | bonuses: нет данных | не в catalog; в accounts.md — blocked 403 | https://github.com/signup ; Copilot: https://github.com/features/copilot/plans |
| Supabase Free | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://supabase.com/dashboard/sign-up ; тариф: https://supabase.com/pricing |
| Vercel Hobby | bonuses.md (A); catalog v0 = аккаунт Vercel | нет данных | bonuses: нет данных | v0 в catalog V/E/R 2/5/2 (не Hop) | https://vercel.com/signup ; тариф: https://vercel.com/docs/plans/hobby |
| Netlify Free | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://app.netlify.com/signup ; тариф: https://www.netlify.com/pricing/ |
| Render Free | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://render.com/docs/free |
| Neon Free | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://neon.com/pricing |
| Firebase Spark | bonuses.md (A) | нет данных | bonuses: нет данных (Phone Auth — продукт, не требование signup) | не задан в catalog | https://firebase.google.com/pricing |
| MongoDB Atlas Free / M0 | bonuses.md (A) | нет данных | bonuses: нет данных | не задан в catalog | https://www.mongodb.com/docs/atlas/tutorial/create-atlas-account/ |
| Deno Deploy Free | bonuses.md (A/B) | нет данных | bonuses: нет данных | не задан в catalog | https://deno.com/deploy/pricing |
| Fly.io (trial $1) | bonuses.md (A/B) | нет данных | bonuses: нет данных | не задан в catalog | https://fly.io/docs/about/free-trial/ |
| AWS Free Tier | bonuses.md (A, с оговоркой по карте) | нет данных | **да** (complete-signup: среди требований телефон; SMS или звонок) — в фильтр «без телефона» не входит | не задан в catalog | https://aws.amazon.com/free/complete-signup/ |
| Bolt.new | catalog.md табл. 2 #19 | нет данных | catalog: Email | V/E/R 4/5/2 | https://bolt.new |
| Lovable | catalog.md табл. 2 #20 | нет данных | catalog: Email | V/E/R 3/5/2 | https://lovable.dev |
| Duck.ai | catalog.md табл. 2 #3 | нет данных (аккаунт не нужен — отдельной регистрации нет) | не требуется (аккаунт не нужен) | V/E/R 4/5/1 | https://duck.ai |
| Arena.ai | catalog.md табл. 2 #1 | нет данных | catalog: вход Google/email (по гайду) | V/E/R 5/4/4 | https://arena.ai |
| Design Arena | catalog.md табл. 2 #2 | нет данных | catalog: 18+; телефон не указан | V/E/R 4/4/3 | https://www.designarena.ai |
| Magic Hour | catalog.md табл. 1 #14 | нет данных | catalog: Email | V/E/R 2/4/2; очередь P2 | https://magichour.ai |
| Treblo (веб) | catalog.md табл. 1 #30 | нет данных | catalog: Email | V/E/R 4 (веб)/3/2 | https://treblo.com |
| Canva AI | catalog.md табл. 2 #13 | нет данных | catalog: Email | V/E/R 3/5/2 | https://www.canva.com |
| Suno | catalog.md табл. 2 #7 | нет данных | catalog: Email | V/E/R 2/5/3 | https://suno.com |

### Что из этого реально проходит фильтр «нет капчи и нет телефона»

- По **официальным страницам** — ни одна строка не подтверждена целиком (капча везде «нет данных», кроме Z.ai).
- Ближе всего по фактам агентства (не замена официальной страницы): **OpenRouter** (создан без телефона 17.11); **Duck.ai** (регистрации нет).
- Отсечены для самостоятельной регистрации агентства: AWS (телефон), Gemini/Google (телефон на нашей попытке), Z.ai (капча), Groq и GitHub (блок IP/бота — см. §4, регистрацию делает Основатель со своего устройства).

## 2. Официальные каналы: Groq, Z.ai; регионы Gemini (Франция / ЕЭЗ)

### Groq (наша регистрация заблокирована, вероятнее IP)

- Чат поддержки в консоли: страница Contact говорит пользоваться chat в GroqCloud Dev Console и Community. Без созданного аккаунта этим путём воспользоваться нельзя. Источник: попытка открыть https://groq.com/contact (17.11.2026); формулировка «chat feature on GroqCloud Dev Console» также в индексе поиска по этой странице — полный текст Contact отдан как JS-оболочка, цитата интерфейса UNVERIFIED, URL официальный.
- Email, который **прямо указан** в официальных Billing FAQs: `support@groq.com` («Need help? Contact our support team at support@groq.com with details about your billing questions» и в ответах про споры/приостановку аккаунта). Страница: https://console.groq.com/docs/billing-faqs (проверено 17.11.2026; адрес виден в HTML как `mailto:support@groq.com`). Документация расписана под биллинг, не под «signup blocked», отдельного шаблона заявки на регистрацию нет.
- Что вложить в обращение (из docs — «details»; остальное не предписано страницей, помечено как разумный минимум, не как обязательный чек-лист Groq): адрес, с которого регистрировались (`6pwffefm+groq@mail.grokbot.com` и повтор `6pwffefm@mail.grokbot.com`); текст ошибки / скрин; время попыток (17.11.2026, повтор ~14:06 ET); reference `39e18c6e` из accounts.md; страна и то, что это регистрация на Free без карты; не просить обойти регион запрещёнными способами.
- Сообщество: https://community.groq.com/ (ссылка из Quickstart).

### Z.ai (slider captcha, 7 попыток, регистрация отложена t343u)

- Email из официальной Privacy Policy, раздел «Contact Us»: `user_feedback@z.ai`. https://docs.z.ai/legal-agreement/privacy-policy (17.11.2026).
- Страница https://z.ai/contact существует (заголовок платформы / «Contact Sales»); содержимое формы в статическом HTML почти пустое (JS) — состав полей = нет данных.
- Официальный пост организации zai-org (GitHub Issue #93, каналы поддержки GLM API / Z.ai, 17.11 страница открыта): для Z.ai — «Click here to contact official support» → https://z.ai/contact ; для API/Coding Plan в том же посте есть ссылка на форму тикета https://bigmodel.cn/ticket-submit. Цитата, что приложить: «please include a brief description of the issue, your account information, the time it occurred, screenshots, error messages, or relevant logs when submitting feedback.» Источник: https://github.com/zai-org/GLM-5/issues/93 (17.11.2026).
- В заявке логично указать: email `6pwffefm+zai@mail.grokbot.com`, что форма заполнена, но slider-captcha не прошла (7 попыток, 17.11.2026 ~15:12–15:14 ET), скрин из accounts.md, страна; не просить обойти капчу.

### Google Gemini API / AI Studio — Франция и ЕЭЗ

Официальный список регионов: https://ai.google.dev/gemini-api/docs/available-regions (17.11.2026). В списке «Available regions» есть **France** (а также French Guiana, Réunion и др.; Martinique/Guadeloupe в этом списке не названы). России в списке нет (уже в catalog.md). Страница при curl отдаёт JS-оболочку; состав списка сверен с публичным текстом официальной страницы 17.11.2026.

Официальные доп. условия: https://ai.google.dev/gemini-api/terms , Effective March 23, 2026 (прочитаны 17.11.2026). Цитаты:

> «You may only access the Services (or make API Clients available to users) within an available region. You may use only Paid Services when making API Clients available to users in the European Economic Area, Switzerland, or the United Kingdom.»

> «If you're in the European Economic Area, Switzerland, or the United Kingdom, the terms under "How Google uses Your Data" in "Paid Services" apply to all Services, including Google AI Studio and unpaid quota in the Gemini API, even though they are offered free of charge.»

Смысл (не вместо цитаты): **Франция как регион доступа включена**. Отдельного запрета Free tier для резидентов ЕЭЗ нет: бесплатная квота может оставаться, но для резидентов ЕЭЗ/CH/UK к данным применяется режим Paid Services (промпты не идут в улучшение продуктов по разделу Paid). Если агентство **предоставляет API-клиент пользователям в ЕЭЗ/CH/UK**, по той же странице можно использовать только Paid Services. Это про клиентов и данные, не про сам факт регистрации из Франции (как уже в справке менторов 17.11).

## 3. Официальная доступность из Франции (сервисы catalog)

Только официальные списки стран/регионов или явное отсутствие такого списка. «Да» = страна France названа в allow-list. Нет списка ≠ «нельзя из Франции». Дата всех строк: 17.11.2026.

| service | France supported? | quote/source | date |
|---|---|---|---|
| OpenAI API (+ ChatGPT) (catalog табл. 1 #11) | да | Список «Supported countries and territories»; среди пунктов есть France. Предупреждение: «Accessing or offering access to our services outside of the countries and territories listed below may result in your account being blocked or suspended.» https://developers.openai.com/api/docs/supported-countries | 17.11.2026 |
| Google Gemini API / AI Studio (catalog табл. 1 #3) | да (Франция в списке регионов) | «The Gemini API and Google AI Studio are available in the following countries and territories» — в перечне есть France. https://ai.google.dev/gemini-api/docs/available-regions плюс условия ЕЭЗ в §2. | 17.11.2026 |
| Anthropic / Claude (в catalog нет отдельной строки API; модели Claude/Fable — через Arena.ai, Design Arena, Poe, uncensored.com) | да (для продуктов Anthropic по политике регионов) | Supported Regions Policy, Effective Nov 12, 2026: сервисы «available only in the countries and regions listed below»; в списке есть France. https://www.anthropic.com/legal/supported-regions Это не автоматически равняется правилам Arena/Poe (у них свои ToS). | 17.11.2026 |
| Mistral AI Studio (+ Le Chat) (catalog табл. 1 #6) | нет отдельного allow-list стран; Франция не исключена на найденных страницах | Официальной страницы «supported countries» не найдено. Есть региональный EU endpoint: «`api.eu.mistral.ai` — EU — Multiple data centers in EU and EFTA countries». https://docs.mistral.ai/inference/regional-inference Это про место инференса, не список стран регистрации. | 17.11.2026 |
| Groq (catalog табл. 1 #2) | нет данных | Официальной страницы списка поддерживаемых стран не найдено (поиск по groq.com / docs 17.11). Блок нашей регистрации (accounts.md) относится к IP/окружению агентства, не к статусу Франции как страны. | 17.11.2026 |
| Z.ai (catalog табл. 1 #4) | нет данных (allow-list нет; в запретах ToS Франция не названа) | catalog: ToS запрещает Иран, КНДР, Кубу, Крым, Донецк, Запорожье — «РФ в списке нет». Это не allow-list и не подтверждение Франции. | 17.11.2026 |
| Hugging Face (catalog табл. 1 #8) | нет данных | Отдельной официальной страницы списка стран в этом проходе не искали глубоко; в catalog — экспортный контроль США, не список стран. | 17.11.2026 |
| OpenRouter (catalog табл. 1 #1) | нет данных | Официального списка стран на просмотренных ранее страницах нет. Аккаунт агентства с французского IP 17.11 создан — это факт среды, не официальный allow-list. | 17.11.2026 |
| xAI API (catalog табл. 1 #10) | нет данных | В catalog: ToS / санкции OFAC; отдельный allow-list в этом проходе не открывался. | 17.11.2026 |
| DeepSeek (catalog табл. 1 #7) | нет данных | catalog: санкционные оговорки без списка, равного allow-list. | 17.11.2026 |
| Perplexity API (catalog табл. 1 #12) | нет данных | catalog: запрет для стран под эмбарго США, список стран на ToS не приведён. | 17.11.2026 |
| ElevenLabs (catalog табл. 1 #13) | нет данных (отдельного allow-list нет) | catalog: ToS п.15 прямо запрещает пользователей в РФ и Беларуси (terms non-EEA, 09.10.2026). Франции в этом запрете нет; это не то же самое, что официальное «France supported». | 17.11.2026 |
| Meta AI (catalog табл. 2 #17) | нет данных | catalog: «доступен только в некоторых странах»; для РФ — официально недоступен. Официальный полный список стран в этом проходе не открыт. | 17.11.2026 |
| Poe (catalog табл. 1 #9) | нет данных | catalog: «not located in a comprehensively sanctioned jurisdiction» (США), без перечня с France. | 17.11.2026 |
| Alibaba Cloud Model Studio / Qwen (catalog табл. 1 #5) | нет данных | Отдельный allow-list в этом проходе не открыт. | 17.11.2026 |
| Arena.ai (catalog табл. 2 #1) | нет данных | Официального списка стран в catalog нет. | 17.11.2026 |
| Design Arena (catalog табл. 2 #2) | нет данных | Официального списка стран в catalog нет. | 17.11.2026 |

## 4. Чек-лист для Основателя (самостоятельная регистрация, 1–2 минуты на сервис)

Регистрирует **Основатель сам**, со своего телефона или ПК, как обычный человек. Наш IP/автоматизированный браузер для этих сервисов не использовать. Почта только вида `6pwffefm+<сервис>@mail.grokbot.com`. Адрес `admin@neuroforgeai.sbs` и любые другие адреса ChatGPT Основателя **не использовать**. Один аккаунт на сервис. **Карту не вводить.** Капчу и телефон не обходить: если сервис их показал — остановиться и написать Оркестратору.

Сейчас в этот чек-лист входит сервис, который **блокирует наш IP**: Groq (accounts.md, 17.11, signup_blocked после magic link). Других строк из §3, где официально Франция разрешена, а наш IP при этом задокументированно заблокировал именно регистрацию, нет (OpenAI/Gemini/Anthropic мы с этого IP не доводили до такого же «signup_blocked»; у Gemini стоп был из‑за телефона, не IP). GitHub (не из §3, из accounts.md) тоже дал HTTP 403 на github.com/signup с нашей среды — отдельная короткая строка, без LLM-ключа в `agency-llm.env`.

Передача ключа — строго как в §5 (ключ в чат не писать).

| service | official sign-up URL | email | где создать API-ключ (публичные docs) | env variable | карта |
|---|---|---|---|---|---|
| Groq | https://console.groq.com (создание ключа после входа: https://console.groq.com/keys ) | `6pwffefm+groq@mail.grokbot.com` | Quickstart: «Please visit here to create an API Key» → https://console.groq.com/keys (https://console.groq.com/docs/quickstart , 17.11.2026). Путь в меню на публичной странице кроме этого URL: нет данных (в docs — прямая ссылка «here»). | `GROQ_API_KEY` (официально в том же Quickstart: `export GROQ_API_KEY=<your-api-key-here>` и `os.environ.get("GROQ_API_KEY")`) | **Карту не вводить.** Free план по bonuses/catalog карту не требует; карта нужна только для апгрейда на Developer. На любом шаге с картой или оплатой — стоп. |
| GitHub (не LLM; наш signup дал 403) | https://github.com/signup | `6pwffefm+github@mail.grokbot.com` | Для обычного аккаунта ключ LLM не нужен. Личный access token, если понадобится позже: docs GitHub про PAT — https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens ; точный пункт меню на 17.11 сверх этого URL не расписывался = нет данных. | если токен вообще понадобится: в публичных docs часто `GITHUB_TOKEN` / `GH_TOKEN`; для `~/secrets/agency-llm.env` сейчас не требуется | **Карту не вводить.** GitHub Free по bonuses.md — $0. |

## 5. Передача ключа

Основатель **не вставляет ключ текстом ни в какой чат**. Он пишет Оркестратору в их личном чате «ключ <сервис> готов»; Оркестратор открывает для него безопасное (маскированное) поле ввода, затем сам переносит ключ в keydrop (`~/secrets/agency-llm.env`) и проверяет его через API.

## Метод

- §1: файлы bonuses.md, catalog.md, accounts.md, signup-queue.md; новые глубокие проверки signup-форм не делались.
- §2–3: официальные страницы регионов/условий/поддержки 17.11.2026 (Gemini terms и regions, OpenAI supported countries, Anthropic supported regions, Groq billing FAQ и quickstart, Z.ai privacy и GitHub issue #93, Mistral regional inference).
- Обходов нет. Регистраций с нашей стороны нет.

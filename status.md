# Статус NeuroForgeAI

Срез пилота на 17.11.2026, 18:43 ET сохранён в таблице ниже. Дополнения 18.11–23.11.2026 внесены 23.11.2026 (America/Los_Angeles) по коммитам `origin/main` и проверке VIP-Custom PR #1. Оркестратор обновляет этот файл при старте, смене состояния и закрытии задачи. Доказательства из истории перенесены как ссылки и отметки источника. Часть логов и скриншотов в рабочей копии отсутствует.

| Кто | Задача | Статус | Срок | Доказательство |
|---|---|---|---|---|
| Оркестратор | Подготовка рабочей копии | Готово 17.11.2026, v1.0. Бриф сверён по 72 позициям | 17.11 | [AGENTS.md](AGENTS.md), [бриф](projects/01-services-signup/brief/brief.md), [журнал](journal.md) |
| Оркестратор | Регистрации, фаза 1 | Регистрации разрешены Основателем 17.11 | — | [Журнал](journal.md) |
| Оркестратор | Инфраструктура, фаза 2 | После фазы 1. GitHub ранее получил HTTP 403 | Полная мощность к 05.12.2026 | [Статус пилота](_core/pilot/status.md), 15:15 и 15:46 ET |

| Оркестратор | Поправка о регистрациях и контрольный экзамен | Готово · 19:17 ET | 17.11 | [Экзамен v1.0](_core/pilot/joker-exam.md), Codex CLI: проверка пройдена |

## Аккаунты по реестру пилота

Читай вместе с хронологией. Поздние проверки Google AI Studio и Cloudflare уточняют ранние записи. Две записи Cloudflare указывают разные адреса, принадлежность проверенного токена к записи требует сверки перед дальнейшим изменением аккаунта.

| Кто | Задача | Статус | Срок | Доказательство |
|---|---|---|---|---|
| Оркестратор | Poe | 17.11.2026 · blocked: phone — передача экрана отклонена Основателем 15:09; ждёт его нового решения · Бонус/данные: — (не проверено) | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Google (AI Studio) | 17.11.2026 · blocked: phone — передача экрана отклонена Основателем 15:09; ждёт его нового решения · Бонус/данные: — (не проверено) | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Пётр | Groq | Подключён вручную, открыт Default Project. API и бонус не проверены | — | [Журнал](journal.md), 20:36 и 20:48 ET |
| Пётр | Mistral | Подключён вручную. API и бонус не проверены после входа | — | [Журнал](journal.md), 20:36 и 20:48 ET |
| Пётр | Viggle | Аккаунт открыт вручную. API и бонус не проверены | — | [Журнал](journal.md), 20:38 и 20:48 ET |
| Пётр | Leonardo | Подключён вручную. API и бонус не проверены | — | [Журнал](journal.md), 20:48 ET |
| Джокер | NightCafe / Microsoft Copilot / HeyGen | HOLD, не повторять. Cloudflare / необычные действия / письмо не пришло | — | [Журнал](journal.md), 20:48 ET |
| Джокер | Фаза 1 и план фазы 2 | В работе. Сверка очереди и подготовка локального плана $0 | 05.12 | [Бриф фазы 1](projects/01-services-signup/brief/brief.md) |
| Оркестратор | OpenRouter | 17.11.2026 · created 14:11 (email verified); баланс $0.00, 0 транзакций; 2 ключа «Default key» (лимит $100 каждый, не скопированы) — оставить, не отзывать (решение Основателя через Директора 14:18); логин в Vault «OpenRouter (agency)» · Бонус/данные: нет: Credits $0.00, 0 tx; $100 — лимит ключа, не подарок; промо/стартап — проверка в очереди | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Z.ai | 2026-11-17 · dropped 15:14 (Founder t343u): slider-captcha; форма заполнена, не отправлена; Vault 5158815 · Бонус/данные: нет (бонусов не видно); скрин 4d4a8cf9… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | GitHub | 2026-11-17 · blocked: HTTP 403 на github.com/signup (вероятно блок бота/IP); аккаунт НЕ создан | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Alibaba Cloud (Model Studio/Qwen) | 2026-11-17 · account CREATED 15:50; next step asks mobile (/basic/security/mobile) → Model Studio activation + Free Quota Only = Founder handoff list; Vault 5164459 · Бонус/данные: нет на странице (Enterprise: «up to $5,000 credits» — не для физлица); скрин 138b7454… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Bolt.new | 2026-11-17 · DONE 15:59: account created + email confirmed, signed in (user SeaWolf1580, Free plan); Vault 5165814 · Бонус/данные: none shown (only referral $50 promo); screenshot bf66977e… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Design Arena | 2026-11-17 · DONE 16:05: email-code sign-up, logged in (passwordless) · Бонус/данные: none shown; screenshot 2111407c… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Canva | 2026-11-17 · DONE 16:07: email-code sign-up, logged in (name Peter Michel), Free, no trial · Бонус/данные: none shown; screenshot 3354cc67… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | NotebookLM | 2026-11-17 · DONE 17:24: app loaded, no prompts | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Google AI Studio (Gemini API) | 2026-11-17 · DONE 17:27: project "Gemini Project", no billing; test gemini-3.8-flash HTTP 200 "OK" 31s · Бонус/данные: free tier, quota not shown | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Treblo | 2026-11-17 · DONE 17:30: confirmed via recovery link, password reset to vault value, logged in at treblo.com (profile icon), no paid plan · Бонус/данные: screenshot 16086f5b… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Tensor.Art | 2026-11-17 · DONE 18:15: logged in, onboarding skipped, no paid plan; agency email rejected by site · Бонус/данные: screenshot a0a15e25… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Lovable | 2026-11-17 · DONE 18:16: dashboard lovable.dev/dashboard, workspace auto-named from Google profile, no credits count shown, no paid plan · Бонус/данные: screenshot 5433ab45… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | SeaArt AI | 2026-11-17 · DONE 18:17: logged in (My Studio visible), no credits counter seen, no paid plan · Бонус/данные: screenshot 2089a31b… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Dreamina (CapCut) | 2026-11-17 · DONE 18:20: logged in, credits shown 0 · Бонус/данные: screenshot (tmp webp) | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Adobe Firefly | 2026-11-17 · DONE 18:21: logged in, "Free daily generations" · Бонус/данные: screenshot (tmp webp) | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Suno | 2026-11-17 · DONE 18:23: Free plan, 50 credits/day per pricing page · Бонус/данные: screenshot bda4b9ef… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Cloudflare (Workers AI) | 2026-11-17 · DONE 18:30: Free plan account, Workers AI page opens; daily allowance not shown in dashboard (docs say free neurons/day, UNVERIFIED) · Бонус/данные: screenshot 4f2b7064… | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | LLM7.io | API проверен в 18:33, HTTP 200. Free plan; точная квота неизвестна | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |
| Оркестратор | Cloudflare Workers AI | Токен активен и тесты API вернули HTTP 200 в 18:36. Free plan; квота в аккаунте не подтверждена | — | [_core/pilot/accounts.md](_core/pilot/accounts.md); сверка по [_core/pilot/status.md](_core/pilot/status.md) |

## Хронология задач пилота

| Кто | Задача | Статус | Срок | Доказательство |
|---|---|---|---|---|
| Исследователь рынка | Каталог сервисов (API + ручные) `_core/pilot/catalog.md` | сдано 17.11 13:15, принято Оркестратором; дозакрывает пробелы | 18.11 10:00 | `catalog.md`, 184 строки, 72 сервиса (30 API / 22 ручных / 20 uncensored·18+) |
| Исследователь рынка | Цепочка Fable `_core/pilot/fable-access.md` | сдано 17.11 13:14, принято Оркестратором; сверка вкладок моделей продолжается | 18.11 10:00 | `fable-access.md`: бесплатные звенья 1–4 (Arena.ai, Design Arena, Poe, uncensored.com), платные П1–П4 |
| Разработчик интеграций | Дизайн роутера `router-design.md` | v0.3 (решения 13:25 и 13:32 внесены в §9), принято Оркестратором | — | §9 п.4–5 DECIDED; бэкап `router-design.md.bak-v0.1` |
| Разработчик интеграций | Техревью API-строк `catalog-api-review.md` | v1.2 (решения 13:25 и 13:32 внесены), принято Оркестратором; всё UNVERIFIED до фазы B | 18.11 10:00 | 100 строк, 30 API-строк + Fable П1–П3; годно 4, проверить 2, не годно 24; ключей в файле нет (grep) |
| Исследователь рынка | Сверка каталога с расхождениями из техревью (Qwen, Gemini, Groq, base URL, Poe П2) | сдано 17.11 13:29 | — | 72 строки без изменений; бэкапы в `research_raw/` |
| Исследователь рынка | ToS звеньев Fable (автоматизация / коммерч. использование) + Arena API (Developer Preview), только публичные страницы | в работе (старт 13:31) | 18.11 10:00 | — |
| Бадди (Директор) | Решение: Arena ToU запрещает автоматизацию и коммерч. использование Output (конфликт с правилом «финал на Fable»); Dola; ElevenLabs (РФ запрещена) | промежуточно решено 17.11 13:32 (Директор): Arena — только вручную, внутренние неклиентские задачи, без автоматизации; финал Fable по клиентским работам — на звеньях, чьи условия разрешают коммерч. использование; платный API Fable НЕ одобрен (варианты 1/3 у Основателя); Dola — только личное, не для клиентов; ElevenLabs — вне топ-10; Qwen — только с «Free Quota Only» до первого вызова | ждёт окончательного решения Основателя по Fable | сообщение Бадди 17.11 13:32 ET |
| Бадди (Директор) | Решения: Gemini; покупка ≥10 кредитов OpenRouter | решено 17.11 13:25: Gemini включаем (без ПДн и конфиденциальных материалов клиентов, без VPN); OpenRouter-кредиты НЕ покупаем, только :free (решение Основателя через Директора) | — | сообщение Бадди 17.11 13:25 ET |
| Промпт-инженер | Правила выбора моделей `model-policy.md` v0.2 | в работе | 18.11 10:30 | — |
| Оркестратор | Приёмка (рутина 18.11 10:00) и сводный отчёт Директору | в работе | 18.11 12:00 | — |
| Бадди (Директор) | Вход в ChatGPT Основателя на общем компьютере | сделано 17.11 (со слов Директора): ChatGPT Plus подключён в браузере Директора; вход и действия только через Директора | — | сообщение Бадди в комнате 17.11 ~13:34 ET |
| Оркестратор | Регламент `_core/pilot/rules.md` v1.0 (ChatGPT, effort до смены модели, Fable, траты) | сделано 17.11 13:36 | — | `rules.md`, 18 пунктов |
| Промпт-инженер | Добавить в `model-policy.md` пп. 2–4 Директора (экономия в ChatGPT, Astra, effort до смены модели, модель+effort в отчёте) | сделано 17.11 (черновик v0.1.1); остальные решения войдут в v0.2 | 18.11 10:30 | `model-policy.md` §4a и §5a, строки 37–45 |
| Основатель (через Бадди) | Постоянное решение: только бесплатные сервисы, траты равны нулю; платный API Fable и кредиты OpenRouter отклонены; платные подписки только для проверок через Директора | решено 17.11 ~13:35 | — | сообщение Бадди 17.11; `rules.md` v1.1 пп. 12–13 |
| Разработчик интеграций | router-design: убрать платные пути (П1–П4, кредиты OpenRouter), отметить «траты = 0» | сделано 17.11 13:37 (принято Оркестратором) | 18.11 09:30 | `router-design.md` v0.4 (253 строки), §4.2a, §4.3, §9 п.12; бэкап `.bak-v0.3`; код защиты не проверен до фазы B |
| Промпт-инженер | model-policy: решение о нулевых тратах и Fable (вариант 1 плюс бесплатная финальная проверка после ToS) | в работе с 13:38 | 18.11 10:30 (в v0.2) | — |
| Исследователь рынка | Условия Design Arena, Poe и uncensored.com: можно ли бесплатно и коммерчески проверять клиентские работы | сделано 17.11 13:35 ET: для клиентских работ подходит только Poe (веб, вручную), с оговорками; Arena и Design Arena не подходят; по uncensored.com нет данных. Пробелы: условия Anthropic для ботов Poe, лимиты, нужен вход | 18.11 10:00 | `fable-access.md`, колонка «Годится для клиентских работ» |
| Исследователь рынка | Дочитать условия: Anthropic (коммерческое использование ответов через Poe) и Poe (обучение на данных, отключение, страны, очки); исправлено число строк в fable-access.md (8 строк с данными) | в работе с 13:42 | 18.11 09:30 | — |
| Оркестратор | Бриф t302u: `paid-needs.md`, список только строго необходимых платных подписок (проверка гипотезы о китайских моделях) | в работе с 13:45 | 18.11 11:30 (в отчёт к 12:00) | `paid-needs.md` v0.1 (каркас) |
| Исследователь рынка | paid-needs: кандидаты по задачам, цены с официальных страниц, ToS, бесплатные альтернативы | в работе с 13:45 | 18.11 09:45 | — |
| Разработчик интеграций | paid-needs: тестовые вызовы бесплатных и китайских моделей (без регистраций) | в работе с 13:45 | 18.11 10:30 | — |
| Промпт-инженер | paid-needs: навыки вместо платных инструментов | в работе с 13:45 | 18.11 10:30 | — |
| Бадди (Директор) | Решения: Poe (веб) — финальная проверка Fable для клиентских работ, только вручную и только если условия Anthropic позволяют; топ-9, Perplexity в резерве; вход в Poe и AI Studio ждёт «да» Основателя | решено 17.11 ~13:39 (вход ждёт Основателя) | — | сообщение Бадди 17.11 |
| Исследователь рынка | Проверка условий Design Arena, Poe, uncensored.com и Anthropic | сделано 17.11 13:41: Poe годится только по условиям; Design Arena не годится; по uncensored.com нет данных; новый риск — Anthropic не работает из неподдерживаемых стран (России нет в списке). Исполнитель работал на effort low, важные цитаты перепроверяются | 18.11 09:30 | `fable-access.md` строка 30+, бэкап `research_raw/fable-access.bak4.md` |
| Основатель (через Бадди) | t304u: до клиентов всё внутреннее; Arena, Design Arena, Poe разрешены, включая финальную проверку Fable; регистрации в Poe и AI Studio не одобрены | решено 17.11 ~13:44 | — | `rules.md` v1.3 п.22; `fable-access.md` строка 2 |
| Исследователь рынка | `chatgpt-modes.md`: режимы Chat, Work и Codex — назначение, лимиты на Plus, распределение задач, экономия токенов; официальные источники OpenAI | в работе с 13:49 | 18.11 10:30 | — |
| Промпт-инженер | Обучающий раздел по `chatgpt-modes.md`: Developer — Codex, Researcher — Chat/Work, PE — Chat | в работе с 13:49 (после Исследователя) | 18.11 11:30 | — |
| Бадди (Директор) | Вопрос о стране для Fable закрыт: серая зона до клиентов принята, проверки делает Директор на облачном компьютере; Fable не вносим в paid-needs, пока не узнаем лимиты Poe | решено 17.11 ~13:45 | — | `rules.md` v1.4 п.23 |
| Основатель (через Бадди) | t307u: регистрации одобрены везде; фаза B началась; один аккаунт, admin@neuroforgeai.sbs, траты = 0, регистрирует Директор | решено 17.11 ~13:46 | — | сообщение Бадди 17.11 |
| Оркестратор | Очередь регистраций `signup-queue.md` | сделано 17.11 13:52 | ASAP | `signup-queue.md` v1.0: 10 сервисов + резерв + 3 веб-сервиса |
| Оркестратор | Регистрации по очереди P0→P3 (Бадди присылает коды подтверждения) | в работе с 13:55 | — | — |
| Разработчик интеграций | План хранения ключей (только имена) | в работе с 13:55; тестовые вызовы — по сигналу Оркестратора | план — 17.11 15:00 | — |
| Исследователь рынка | Перепроверка цитат: France есть в списке Anthropic, лицензия Poe, Design Arena §8 | сделано 17.11 13:47 | — | `research_raw/tos-verify-2026-11-17/`; бэкапы bak5 и bak6 |
| Промпт-инженер | paid-needs: черновик навыков вместо платных инструментов | промежуточно 17.11: 11 строк, 10 из них проверены тестами | 18.11 10:30 | `research_raw/skills-vs-paid.md` v0.1, `research_raw/skills-tests/` |
| Основатель | «Стоп» 13:46 ET: регистрации на паузе; admin@ не для регистраций, почта — ящик агентства (TBD) | HOLD снят 13:49 | — | сообщение Бадди 17.11 13:49 |
| Оркестратор | Бадди передал «го» на регистрации (13:50); жду подтверждения Основателя его словами | снят: «Продолжай» (t312u 13:49), передал Бадди | — | сообщение Бадди 13:50 |
| Оркестратор | Регистрация Poe (6pwffefm+poe@) | код отправлен 13:52:15, жду код от Бадди | 17.11 | скриншот страницы «Verify email» (assets/31bda15b….png) |
| Исследователь рынка | t302u: кандидаты в платные + вердикт | сделано 17.11 13:52 (исполнитель low вместо high) | 18.11 09:45 | paid-needs.md 62 стр. (15 кандидатов), research_raw/paid-candidates.md 57 стр., research_raw/pc/ 125 файлов; проверено Оркестратором: число строк, бэкап, UNVERIFIED 13+6 |
| Разработчик интеграций | key-storage.md + tools/keydrop.py | сделано 17.11 13:53 (effort low) | 17.11 15:00 | key-storage.md 39 стр.; keydrop слушает только 127.0.0.1:8765 (проверено Оркестратором по коду) |
| Оркестратор | Poe: код введён, создание аккаунта | ⛔ СТОП 13:54: Poe требует номер телефона («verification during each sign in»); аккаунт НЕ создан | 17.11 | скриншот assets/49b1443b….png |
| Исследователь рынка | t304u: chatgpt-modes.md | сделано 17.11 13:53 (low + medium) | 18.11 10:30 | v1.1, 254 стр., 9 UNVERIFIED, бэкап research_raw/chatgpt-modes.bak1.md (проверено Оркестратором) |
| Оркестратор | rules.md v1.8: п. 26–29 + SA-001 | сделано 17.11 13:56; п. 26в ждёт слов Основателя | — | бэкап research_raw/rules.bak-v1.7.md |
| Бадди (Директор) | Бриф v2 по регистрациям: стоп по строкам, очередь Groq→OpenRouter→AI Studio→Z.ai→Alibaba→HeyGen→Magic Hour→Viggle→Mistral→Perplexity; key-storage v1.0 одобрен | принято 13:57 | волна 1 — 18.11 18:00 | сообщение Бадди 13:56; accounts.md v0.1 |
| Оркестратор | Google (AI Studio) | код отправлен 13:59 на базовый адрес, жду код от Бадди | 18.11 18:00 | скриншот assets/a4a051ba….png |
| Оркестратор | Groq | blocked 14:00: «We couldn't complete your sign-up», signup_blocked (причина не указана) | 18.11 18:00 | скриншот assets/32f9c82d….png |
| Исследователь рынка | t302u: перепроверка на high (13 пунктов) | сделано 17.11 13:59 (effort high) | 18.11 09:45 | paid-candidates.md v1.1 76 стр. (раздел E с цитатами), paid-needs.md 63 стр., research_raw/pc-verify/; исправлено: Semrush, Vercel Hobby (некоммерческий), Brave (нужна карта), Hailuo, DeepSeek |
| Оркестратор | Google AI Studio signup | waiting: password via Vault route (Бадди) 14:02 | 18.11 18:00 | assets/c21bdb9b….png |
| Оркестратор | Groq retry (base addr) | magic link sent 14:02, waiting link from Бадди | 18.11 18:00 | assets/e9ff0418….png |
| Оркестратор | Poe (phone) | on hold 14:03: public SMS number offered via Бадди; asked for Founder verbatim + flagged verification-bypass/ToS risk | — | SendToAgent 14:03 |
| Оркестратор | Poe (phone) | blocked: phone — public SMS numbers declined (bypass of verification); options (a) Founder enters own number via screen handover, (b) stay blocked; asked Бадди 14:04 | — | SendToAgent 14:04 |
| Оркестратор | Poe (phone) | queued 14:04: Founder chose own number; screen handover to Founder at phone step after Google/Groq | 18.11 18:00 | Бадди msg t328u relay |
| Оркестратор | Google AI Studio signup | blocked 14:05: Google requires phone/device verification (QR) after password; row closed per brief | — | assets/e160a105….png |
| Оркестратор | Groq retry | blocked 14:06: signup_blocked again (IP/region likely); row closed | — | assets/28acd60d….png |
| Оркестратор | OpenRouter signup | started 14:06 | 18.11 18:00 | — |
| Оркестратор | Poe + Google | waiting: Founder screen handoff (one session) 14:07; prep tabs after OpenRouter step | 18.11 18:00 | Бадди relay 14:07 |
| Оркестратор | OpenRouter signup | form submitted 14:08 (ToS 31.08.2026); waiting verification link from Бадди | 18.11 18:00 | assets/4dc4b1f2….png |
| Оркестратор | OpenRouter signup | DONE 14:11: account created, credits $0.00/0 tx; auto-generated onboarding key not copied — revoke+keydrop proposed | 18.11 18:00 | openrouter.ai/settings/credits (subagent report) |
| Оркестратор | Poe | email code sent 14:09; waiting code from Бадди, then phone step → Founder handoff | 18.11 18:00 | assets/31bda15b….png |
| Оркестратор | Bonus rule (t337u) | accepted 14:18: bonus column added; OpenRouter promo recheck queued after handback | — | accounts.md |
| Исследователь рынка | bonuses.md (Founder t339u, class A/B/C) | assigned 15:07, research only | 18.11 10:00 (Director 12:00) | — |
| Оркестратор | Z.ai signup | started 15:08 (6pwffefm+zai@) | 18.11 18:00 | — |
| Оркестратор | Signups: codes | 15:09 Founder (t48u, my DM): «Используй свою почту и заканчивая работу по регистрации» — read codes from own inbox 6pwffefm@ directly, no relay via Director | 18.11 18:00 | DM t48u |
| Оркестратор | Poe + Google | blocked 15:09: Founder dismissed screen handoff; not re-requesting | — | handoff card dismissed |
| Оркестратор | SCOPE: all 72 catalog + bonus list (Founder t341u via Бадди 15:11); wave cap cancelled | started 15:12: building signup-queue-all.md; Z.ai in progress | hourly tally to Бадди | — |
| Оркестратор | Z.ai signup | blocked 15:12: slider captcha failed x7 → Founder handoff list | — | screenshot 4d4a8cf9… |
| Оркестратор | ALL sign-ups | PAUSED 15:13 (Бадди/Founder: usage); no browser running; queue table w/o browser in progress; hourly tally paused | — | — |
| Оркестратор | Narrowed scope (Founder t343u via Бадди 15:14): GitHub, Supabase, Cloudflare only; Z.ai dropped (captcha, not 1-2 steps); Poe+Google wait handoff | GitHub started 15:14 | — | — |
| Оркестратор | GitHub signup | blocked 15:15: HTTP 403 on /signup; Supabase next | — | subagent report, no screenshot |
| Исследователь рынка | bonuses.md | ACCEPTED 15:16 (26 rows, A15/B3/AB2/C6; spot-check GitHub/Supabase/Cloudflare rows OK) | 18.11 10:00 | _core/pilot/bonuses.md |
| Оркестратор | RESTART t346u Phase 1 | 15:20: Codex CLI 0.169.0 installed; device login started (code to Бадди, expires ~15:35) | — | tools/codex-install.log, tools/codex-login.log |
| Разработчик интеграций | P1a LiteLLM router | assigned 15:20; blocked on OPENROUTER_API_KEY (keydrop empty; new key proposal sent to Бадди) | — | — |
| Оркестратор | OpenRouter key agency-router | done 15:23: limit $0, no expiry, keydrop OPENROUTER_API_KEY len=73 sha256=cd63af1c; keydrop stopped | — | screenshot 9bc6dd52… |
| Разработчик интеграций | P1a LiteLLM router | DONE 15:24: 127.0.0.1:4000, test free-chat http=200 3.2s cost $0.0 | — | router/logs/test.log |
| Все агенты | Pipeline: router 127.0.0.1:4000 → Codex low verdict → Бадди | ACTIVE 15:40; Codex logged in (Founder ChatGPT) | — | rules.md v1.9 |
| Оркестратор | P1c provider list | done 15:45: EMAIL 1 (Alibaba/Qwen, conditional), HANDOFF 1 (Google AI Studio), SKIP 2 (Z.ai, Groq); Codex verdict ISSUES → fixed once | — | p1c-providers.md v0.2, p1c-codex-verdict.txt |
| Оркестратор | Alibaba Model Studio signup | started 15:45 | — | — |
| Оркестратор | Phase 1 corrected (Founder t356u via Бадди 15:46): all catalog.md services by Value; Supabase/GitHub/infra = phase 2 (stopped) | queue signup-queue-all.md being built; Alibaba in progress | — | — |
| Оркестратор | Alibaba signup | DONE 15:50 account created (email code from own inbox); Model Studio needs phone step → handoff list | — | screenshot 138b7454… |
| Оркестратор | signup-queue-all.md v1.1 | DONE 15:53 (72 rows: EMAIL 33, HANDOFF 3, X 33; Codex ISSUES fixed once) | — | signup-queue-all.md, signup-queue-codex-verdict.txt |
| Оркестратор | EMAIL lane: Bolt.new | STARTED 15:54 | 17.11 | — |
| Бадди→Оркестратор | Queue scope 15:55 | ALL 72 rows incl. 18+ and ToS-restricted (Founder room 15:54); normal sign-up only, no evasion | — | Бадди msg 15:55 |
| Оркестратор | Founder screen handoff (Poe→Google AI Studio→Alibaba phone→Z.ai) | IN PROGRESS 15:54 (box handed to Founder, Poe) | 17.11 | — |
| Исследователь | legit-paths.md | DONE 15:57 (§1 26, §3 17, §4 2 rows; Gemini free tier not for EEA users per terms 23.03.2026) | 17:30 | legit-paths.md |
| Оркестратор | Bolt.new | DONE 15:59 (confirmed, Free plan) | — | screenshot bf66977e… |
| Оркестратор | Poe prefill → handoff | STARTED 16:00 | 17.11 | — |
| Оркестратор | Poe | BLOCKED 16:03: email+code OK, phone step +7 rejected "device or network may be sending automated queries" (box IP); Founder to finish from own device | — | report 16:03 |
| Оркестратор | Design Arena | DONE 16:05 | — | screenshot 2111407c… |
| Оркестратор | NotebookLM / Google Flow | HANDOFF: need Google account (Google sign-up = phone) | — | — |
| Оркестратор | Treblo | STARTED 16:05 | — | — |
| Оркестратор | Treblo | WAITING Founder birth year (form: email+password+YYYY, cannot change later) | — | url treblo.com/login?mode=signup |
| Оркестратор | Canva | STARTED 16:06 | — | — |
| Оркестратор | Canva | DONE 16:07 | — | screenshot 3354cc67… |
| Оркестратор | Poe | PAUSED by Founder 16:07 (t69u) | — | — |
| Оркестратор | Zoho Mail agency mailbox (Founder t69u) | STARTED 16:08 | — | — |
| Оркестратор | Zoho Mail | PAUSED 16:09 (Founder t70u: use his Google accounts) | — | form filled, not submitted |
| Оркестратор | Founder Google accounts for sign-ups | WAITING Бадди: access + multi-account rule conflict | — | agent msg 16:09 |
| Оркестратор | cyberyozh SMS numbers (t363u via Бадди) | DECLINED 16:19: rented numbers to pass phone checks / multi-account = deceiving services; $0 spent | — | agent msg to Бадди 16:19 |
| Оркестратор | Zoho Mail (Founder real phone, SMS via Бадди forwarder) | RESUMED 16:56 | — | — |
| Оркестратор | Treblo | UNBLOCKED 16:57 — queued after Zoho | — | — |
| Оркестратор | Zoho Mail | BLOCKED 16:57: Zoho "unable to create your account right now, contact support-as@eu.zohocorp.com" (risk block, no SMS sent); Vault 5175207 unused | — | screenshot 01d38364… |
| Оркестратор | Treblo | STARTED 16:58 | — | — |
| Оркестратор | Вход Google (asdf150780@gmail.com) | 17:23: попытка входа и 2FA; далее подтверждён доступ через NotebookLM | — | _core/pilot/status.md |
| Оркестратор | NotebookLM via Google | STARTED 17:24 | — | — |
| Оркестратор | Treblo | ACCOUNT CREATED 16:58, email verify pending (Vault 5175400) | — | screenshot 0377e7c9… |
| Оркестратор | NotebookLM | DONE 17:24: opened via Google asdf150780@gmail.com, app loaded (notebook.google.com) | — | URL notebook.google.com/notebook/b430898b… |
| Оркестратор | Google Flow | STARTED 17:25 | — | — |
| Оркестратор | Google Flow | BLOCKED 17:25: flow.google.com/unsupported-country "Flow ещё не работает в вашей стране" | — | report text |
| Оркестратор | Google AI Studio (GEMINI_API_KEY) | STARTED 17:25 | — | — |
| Оркестратор | Google AI Studio | DONE 17:27: GEMINI_API_KEY stored, test call 200 OK (gemini-3.8-flash) | — | keydrop sha e9786b80 + curl 200 |
| Оркестратор | Router: add Gemini | TODO → Разработчик интеграций | 18.11 | — |
| Оркестратор | Treblo verify | link expired 17:28 ("Email link is invalid or has expired"), login says "Email not confirmed"; requesting resend | 17.11 | screenshot 40034c33… |
| Оркестратор | Treblo | DONE 17:30: logged in, email confirmed via recovery link | — | screenshot 16086f5b… |
| Оркестратор | Lovable (Google asdf150780) | WAITING Founder: Google 2FA prompt on Xiaomi 12, number 55 (17:31) | 17.11 | accounts.google.com/v3/signin/challenge/dp |
| Разработчик интеграций | Router: add Gemini | DONE 17:35: alias gemini-free (gemini-3.1-flash-lite) HTTP 200 0.87s; gemini-3.8-flash alias timeout 60s + fallback (3.8 hangs from box) | — | router/logs/test.log, config.yaml v0.2 |
| Разработчик интеграций | OmniRoute (self-hosted router, t87u) | ASSIGNED 18:10 | 18.11 12:00 | — |
| Оркестратор | ChatLLM (Abacus.AI) | HOLD: no free tier ($7 first month, then $10/mo per abacus.ai/chat_llm-pricing); needs Founder spend approval via Director | — | abacus.ai/help/howTo/chatllm/faqs/billing |
| Оркестратор | ElevenLabs | BLOCKED 18:11: image captcha failed once; Founder declined handoff; account not created (vault 5183790 unused) | later | — |
| Оркестратор | Tensor.Art | DONE 18:15 via Google asdf150780 (Founder 2FA) | — | screenshot a0a15e25… |
| Оркестратор | Lovable | RETRY 18:16 via Google asdf150780 | 17.11 | — |
| Оркестратор | Lovable | DONE 18:16 via Google asdf150780 (no 2FA this time) | — | screenshot 5433ab45… |
| Оркестратор | SeaArt AI | DONE 18:17 via Google asdf150780 | — | screenshot 2089a31b… |
| Оркестратор | Dreamina, Adobe Firefly, Suno, v0 | STARTED 18:18 via Google asdf150780 | 17.11 | — |
| Разработчик интеграций | OmniRoute | DONE 18:21: 127.0.0.1:20128, auth on, auto→gemini-3.1-flash-lite HTTP 200 ~3s; OpenRouter path 429 unproven; 75 extra free providers listed | — | omniroute/logs/test.log, free-providers-diff.md |
| Оркестратор | Dreamina, Firefly, Suno | DONE 18:23 via Google asdf150780 | — | accounts.md |
| Оркестратор | v0 (Vercel) | WAITING: Vercel SMS phone verification; trying Founder real phone + SMS relay via Бадди | 17.11 | screenshot de1eb987… |
| Оркестратор | v0 (Vercel) | BLOCKED 18:25: "This phone number is already associated with a Vercel account" (Founder phone); need another phone or Founder existing Vercel login | — | computerUse report |
| Оркестратор | Mistral (La Plateforme) | STARTED 18:26 via Google asdf150780 | 17.11 | — |
| Оркестратор | Mistral | BLOCKED 18:26: Free plan has API keys disabled ("Upgrade to activate your API keys"); key needs card/pay-as-you-go | — | admin.mistral.ai/subscription/upgrade/plans |
| Оркестратор | SambaNova | BLOCKED 18:29: account created (Google asdf150780), key "agency" created but NOT stored (box clipboard copy failed); site says credits need payment method -> key useless at $0 | — | cloud.sambanova.ai/apis |
| Оркестратор | Cloudflare Workers AI | ACCOUNT DONE 18:30; API token WAITING keydrop clipboard fix | 18.11 | screenshot 4f2b7064… |
| Оркестратор | SambaNova | BLOCKED confirmed 18:33: key stored (SAMBANOVA_API_KEY len36 sha d1f12dac), /v1/models 200 but chat 402 PAYMENT_METHOD_REQUIRED | — | curl 402 |
| Разработчик интеграций | keyclip.sh (clipboard->keydrop) | DONE 18:31, verified by Оркестратор on :7 | — | keydrop check |
| Оркестратор | LLM7.io key | DONE 18:33: /v1/models 200 (87 models), chat model=default -> gemma4:31b 200 in 1.24s | — | curl test |
| Оркестратор | Cloudflare Workers AI token | DONE 18:36: tokens/verify 200 active; chat llama-3.3-70b-fp8-fast 200 0.45s, gpt-oss-120b 200 0.57s | — | curl test |
| Разработчик интеграций | OmniRoute: Gemini denylist + llm7-free + cf-free + fallback | DONE 18:40 (gemini-3.8-flash blocked 9ms; llm7/cf combos 200) | — | omniroute/logs/test.log tests 5-8 |
| Разработчик интеграций | LiteLLM v0.4: llm7-free, cf-free, fallback chain | DONE 18:36 | — | router/logs/test.log |
| ВСЕ | ПАУЗА 18:41 по команде Директора (лимит плана <10%): субагенты и браузерная работа остановлены, новое не запускается | PAUSED | до команды Директора | StopSubagent all |
| Оркестратор | Рутина pilot-phase-a-acceptance-check | PAUSED 18:42 до сброса лимита 23.11 (приказ Директора) | 23.11 | UpdateRoutine pause |
| Все агенты | Рутины на паузе до 23.11: Разработчик интеграций (2), Промпт-инженер (3, сроки 18.11 сорвутся), Исследователь рынка (рутин нет) | PAUSED 18:43 | 23.11 | ответы агентов |
| Оркестратор | Совет по роли «Джокер (Codex)» | В работе · 18:57 ET | 17.11 | Подготовка трёх документов |
| Оркестратор | Совет по роли «Джокер (Codex)» | Документы готовы · 18:58 ET, вердикт CLI отложен | 17.11 | _core/staff/codex-joker.md, _core/staff/rule-joker.md, _core/pilot/mentor-notes/2026-11-17-joker-council.md |

| Джокер | Фаза 1 и черновики фазы 2 | Старт · 2026-11-17 19:26 EST | 05.12 | projects/01-services-signup/brief/brief.md |
| Джокер | Совет по плану | Протокол v1.0 | 17.11 | _core/pilot/mentor-notes/2026-11-17-plan-council.md |
| Джокер | Фаза 1 №26 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №25 | Chrome · HTTP 200 · Free, Email input | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №24 | Chrome · HTTP 200 · Sign up, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №19 | Chrome · HTTP 200 · Sign in, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №27 | Chrome · HTTP 403 · CAPTCHA | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №31 | Chrome · HTTP 200 · Sign in, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №28 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №29 | Chrome · HTTP 200 · Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №33 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №35 | Chrome · HTTP 403 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №32 | Chrome · HTTP 403 · CAPTCHA | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №34 | Chrome · HTTP 200 · Sign up | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №41 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №40 | Chrome · HTTP 403 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №37 | Chrome · HTTP 200 · Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №39 | Chrome · HTTP 200 · Sign in, Sign up | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №42 | Chrome · HTTP 403 · CAPTCHA | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №43 | Chrome · HTTP 200 · Sign in, Sign up | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №44 | Chrome · HTTP 200 · Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №45 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №47 | Chrome · HTTP 200 · Sign in | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №49 | Chrome · HTTP 200 · Sign in | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №46 | Chrome · HTTP 200 · Sign in, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №48 | Chrome · HTTP 200 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №51 | Chrome · HTTP 403 · — | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №52 | Chrome · HTTP 200 · Sign in, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 №50 | Chrome · HTTP 200 · Sign in, Sign up, Free | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 2 | Черновик v1.0 | 05.12 | projects/02-infrastructure/work/implementation.md |
| Джокер | Copilot | Ручной вход Microsoft · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Magic Hour | Публичный бесплатный путь по FAQ; форма не открылась · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Viggle | Веб-приложение HTTP 403 · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | HeyGen | Ожидание подтверждения ссылки · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | AiHere | Шаблоны публично доступны · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | LiteLLM | HTTP 401; виртуальный ключ Джокера недоступен · 2026-11-17 19:29 EST | 05.12 | projects/01-services-signup/results/browser-2026-11-17.md |
| Джокер | Фаза 1 | Частично · 2026-11-17 19:29 EST · 72 в сводке, 27 в Chrome | 05.12 | projects/01-services-signup/results/queue-2026-11-17.md |
| Оркестратор | Groq | Отправка ссылки подтверждена экраном · 2026-11-17 20:24 EST | — | inbox/groq-link.png |
| 2026-11-17 20:36 | Groq | аккаунт создан (asdf150780), консоль открыта, скриншот у Петра | Mistral | подключён Петром |
| Оркестратор | Регистрация фазы 1 | Запущена проверка в 4 вкладках | — | projects/01-services-signup/work/signup-batch.cjs |
| Оркестратор | Регистрация фазы 1 | Прогон завершён · 2026-11-17 22:30 EST · 47 открытых позиций, 5 отмечены по брифу, 0 новых аккаунтов | — | projects/01-services-signup/results/failed.md; projects/01-services-signup/results/done.md |
| Джокер | Claude Code: обработка документов | Локальная проверка пройдена · 2026-11-17 22:55 ET | — | [Запуск и проверка](projects/02-infrastructure/work/claude-local/README.md) |
| Джокер → Бадди | Приёмка локальной обработки документов | ACCEPT Бадди, 17.11.2026 23:16–23:25 ET. В `main` с `268003d` (23.11.2026 15:51 PT). Ранее вердикт оставался только в локальном `8ad9cea` | — | [Раздел приёмки](#бадди-проверка-claude-code-локально-2026-11-17), [inbox](inbox/needs.md#бадди--claude-code-для-документов-nfai) |
| Джокер | Общий граф памяти NFAI | Добавлен в `8319de6` (17.11). Политика баллов проиндексирована в `1e7b127` (20.11). После закрытия приёмки 23.11: `query.py check` — 58 узлов, 42 роли, 124 связи | — | [Граф и команды](_core/memory/README.md), `8319de6`, `1e7b127` |
| Парсер Telegram | Разбор двухмесячной подборки инструментов | Разбор начат по видимой истории с 28.10. Импорт проверен на синтетическом JSON, очередь идёт от свежих публикаций | — | [Бриф](projects/03-telegram-tooling/brief/brief.md) |
| Джокер | Подборка Telegram: первый ролик | Проверены четыре дополнения Claude Code и тест локального шлюза | — | [Разбор с таймкодами](projects/03-telegram-tooling/results/01-claude-code-addons.md) |
| Веб-дизайнер | Дизайн-скилл NFAI | Добавлены критерии дизайна и упражнение для тестировщика | — | [Разбор ролика](projects/03-telegram-tooling/results/03-web-design.md) |
| Джокер | Координация НФАИ на паузе Бадди | Пауза Директора по лимиту завершена 23.11.2026. Джокер работает вместе с Бадди через репозиторий и Brain Bridge | — | [Порядок работы](projects/03-telegram-tooling/brief/execution.md), [журнал](journal.md) |
| Тестировщик | Граф и MCP | Хук проверен на входных событиях. Memory MCP проверен запросами. Playwright MCP отвечает, запуск браузера заблокирован | — | [Проверки MCP](projects/03-telegram-tooling/review/mcp.md) |
| Джокер | Восстановление NFAI из Git bundle | Локальное восстановление и сверка дерева пройдены | — | [Результат проверки](projects/02-infrastructure/review/recovery-2026-11-18.md) |
| Джокер | Oracle Always Free и Lowfat | Условия Oracle сверены. Для Lowfat записан контрольный замер штатных команд Git | — | [Oracle](projects/03-telegram-tooling/results/oracle-always-free.md), [Lowfat](projects/03-telegram-tooling/results/04-lowfat.md) |
| Джокер | Проект telegram-tooling | Создан после `8319de6` (первый коммит `37525a4`, 17.11 23:23 ET). До `175a898` (19.11 18:11 ET): разбор роликов, субтитры, вертикальные клипы, локальная транскрипция, поиск фрагментов | — | [Бриф](projects/03-telegram-tooling/brief/brief.md), `37525a4`, `175a898` |
| Джокер | Claude Code, повторные проверки | 18–19.11: шлюз HTTP 200 (`2ddb3c2`); полный Read/Write в той среде 18.11 завершился по тайм-ауту (README); 19.11 восстановление после SIGKILL и HTTP 401, опция контекста 4096 (`92333bc`, `408f922`, `cc64dd0`) | — | [README](projects/02-infrastructure/work/claude-local/README.md), `95b91a7`, `2ddb3c2`, `92333bc`, `408f922`, `cc64dd0` |
| Джокер | Magic Hour, гостевой режим | 19.11 гостевая генерация 3-секундного ролика подтверждена, окно регистрации закрыто; загрузка файла отдельно не проверялась | — | [Отчёт](projects/01-services-signup/results/2026-11-19-magic-hour-check.md), `f0eb774` |
| Джокер | Microsoft Copilot, веб | 19.11 бесплатный тариф описан поставщиком; тестовый вопрос привёл на страницу входа, ответа без входа не получено | — | [Отчёт](projects/01-services-signup/results/2026-11-19-copilot-check.md), `d2d84ec` |
| Джокер | Балльная оценка агентов | 20.11 правила merit для всех ИИ-агентов, включая Бадди. Закрытый реестр вне публичного NFAI. Баллы в этом обновлении не начислялись | — | [_core/staff/merit-points.md](_core/staff/merit-points.md), `3449b73`, `23c1e79`, `1e7b127` |
| Джокер | NFAI Brain Bridge | 21.11 04:21 UTC открыт draft PR #1 в приватном fed8eb-arch/VIP-Custom, ветка `nfai-brain-bridge`, не сливать. Есть `bridge/questions/` и `bridge/answers/`. В описании PR event-триггер ChatGPT Work указан как ещё не настроенный. 23.11 15:39 PT комментарий 7117202647: Claude Code на Windows-ПК владельца сообщён, удалённый запуск в уведомлении не проверен | — | [PR #1](https://github.com/fed8eb-arch/VIP-Custom/pull/1), [журнал](journal.md) |


## Бадди: проверка Claude Code локально 2026-11-17

Вердикт: **ACCEPT**. Оба теста прошли с первой попытки, повторов не было. Проверка на рабочей машине Бадди (бокс), 2026-11-17 23:16–23:25 ET. Коммиты, которые проверены: 466791f, c06b920.

Установка ($0, вне репозитория, `NFAI_CLAUDE_HOME=~/nfai-claude`):
- Node v24.22.1 (уже был на боксе).
- `npm install --prefix ~/nfai-claude/npm @anthropic-ai/claude-code@2.1.327 omniroute@3.8.53`: 1329 пакетов, 1 мин 32 с. `claude --version` → `2.1.327 (Claude Code)`.
- llama.cpp b12494 `llama-b12494-bin-ubuntu-x64.tar.gz` (23 746 331 байт) → `~/nfai-claude/llama-b12494/llama-server`.
- `Qwen/Qwen3-4B-GGUF/Qwen3-4B-Q4_K_M.gguf` (2 497 280 256 байт) → `~/nfai-claude/models/qwen3-4b-q4.gguf`.
- `NFAI_OMNIROUTE_PACKAGE=~/nfai-claude/npm/node_modules/omniroute`, `NFAI_CLAUDE_BIN=~/nfai-claude/npm/node_modules/.bin/claude`.
- Существующие OmniRoute :20128 и LiteLLM :4000 не трогались; после тестов оба порта по-прежнему слушают, порты 11435 и 20129 свободны.

Тесты: `node projects/02-infrastructure/work/claude-local/run.mjs --document <файл> --out <json> 'Extract the document code and the quantity (number of units). Write them as JSON with keys "document_code" and "quantity" (quantity as an integer).'`

| Тест | Источник (созданный вручную) | Вывод run.mjs | Файл результата | Время |
|---|---|---|---|---|
| DOCX | python-docx: код NFAI-DOC-7342, 58 units | `Tool calls: Read, Write \| failed: 0`; `Claude Code wrote` | `{"document_code": "NFAI-DOC-7342", "quantity": 58}` | 38,3 с (первый запуск, включая создание ключа шлюза) |
| Markdown | код NFAI-DOC-9186, 134 units | `Tool calls: Read, Write \| failed: 0`; `Claude Code wrote` | `{"document_code": "NFAI-DOC-9186", "quantity": 134}` | 40,5 с |

Сверка: JSON разобран питоном, значения равны эталону в обоих тестах (True, True). Шлюз ответил `/v1/messages HTTP 200`, `Gateway result: 43`.

Отличие от записи Джокера: в Markdown у Бадди ни один вызов Read не завершился ошибкой (`failed: 0`), повторного чтения не было. Это один прогон, не гарантия.

Наблюдения:
- Строка `[claude-code:unrecognized_model] {"model":"local-qwen/qwen3-4b"}` идёт в stderr; на результат не повлияла.
- run.mjs доказывает вызовы по событиям `tool_use` stream-json в собственном проверочном коде и выводит только список имён. Сам транскрипт не сохраняется (`--no-session-persistence`), в `qwen3-4b-state/` лежат только llama.log, omni.log и ключ шлюза.
- Нагрузка: `user` 3–4 мин на 8 ядрах (только CPU, `-ngl 0`); на боксе свободно около 2 ГБ ОЗУ, параллельно запускать задачи не стоит.
- Ключи, модель и бинарники в репозиторий не добавлялись.

Примечание 2026-11-23: этот вердикт был в локальном коммите 8ad9cea и не попал в main из-за незавершённого rebase на боксе. Ошибка Бадди: локальный коммит без push. Перенесено в main сейчас.

## Бадди: проверка Claude Code на ПК Петра (DESKTOP-DMFUR0R) 2026-11-23

Вердикт: **ACCEPT** (только через лаунчер `Start_Claude_Local.ps1`).
- Claude Code 2.1.327, `%LOCALAPPDATA%\PolymarketClaude\...\claude.exe`; `claude` нет в PATH. Голый запуск: `Not logged in · Please run /login`.
- `Start_Claude_Local.ps1 Start` (27,2 с): llama-server :11435 (qwen3-4b-q4, ctx 16384, CPU) + OmniRoute :20129, все 4 флага здоровья true.
- Без фоновых флагов: `Prompt is too long ... 21254 tokens exceeds 16384` (хуки и MCP не влезают в контекст).
- С флагами лаунчера (`--safe-mode --restricted`, пустой MCP, disableAllHooks, Read,Write): 103,2 с, Read 1 (test.md), Write 1 (result.json), `{"document_code": "NFAI-DOC-5521", "quantity": 77}` = эталон. Предупреждение `unrecognized_model` не мешает.
- После теста `Stop`: процессы остановлены, temp удалён. Логин и ключи не вводились, ничего не ставилось.
- DOCX на ПК не проверен: нет python-docx.

Видимый прогон на ПК 2026-11-23 16:08 PT: окно «Claude Code - NFAI local Qwen test #2», 105 с, Read 1, Write 1, `{"document_code": "NFAI-DOC-5521", "quantity": 77}`. Первая попытка упала из-за ошибки скрипта Бадди (см. errors-log).


## 24.11.2026 — контрольная точка непрерывности NFAI

Аудит ChatGPT по поручению Основателя. Проверено чтение обоих GitHub-репозиториев, граф памяти (58 узлов, 124 связи), draft Inbox PR #1 (48 коммитов, 33 файла; не сливать). Историческая приёмка Claude на Windows 23.11 подтверждается записью выше, но текущие процессы и MCP не проверены. Ниже приоритетная очередь, не замена существующих проектных брифов. Бюджет новых расходов $0.

| Приоритет | Ответственная роль | Задача / статус | Следующий критерий приёмки |
|---|---|---|---|
| P0 | Оркестратор / DevOps | Проверить доступность существующих исполнительных сред и сохранение в GitHub; текущие процессы не проверены | Проверка запуска, здоровья, остановки и повторного чтения контрольной точки |
| P0 | Интегратор / Tester | Free Engine: восстановить исходный профиль Claude и минимальный MCP, не переустанавливать; контекст 16384, ранее переполнение | Один ограниченный MCP-запрос и Read/Write с фиксацией размера контекста; независимая проверка |
| P0 | Оркестратор | Brain Bridge: хранилище доступно; событийное пробуждение не подтверждено | Проверка вопроса/ответа с явной идентичностью исполнителя; не выдавать ручной ответ за автоматический |
| P1 | Интегратор / Cost Controller | Сверить существующие OmniRoute и LiteLLM, бесплатные маршруты, блокировки, резерв | Реальный малый тест на каждой разрешённой среде, запрет платного fallback |
| P1 | Product / Tester | Продолжить существующие задачи управляемых проектов, без дублирования брифов | Независимые проверяемые результаты; торговые контуры только offline/paper в рамках разрешений |
| P1 | Исследователь / Professor | Инвентаризация материалов Rush Conf, транскрипция и тест технологий; один доклад найден в библиотеке | Перечень первоисточников, полнота транскриптов, тесты до внедрения |
| P1 | Оркестратор | Сверить локальные оригиналы, резервные копии и проектные документы; доступ к ПК в текущей среде отсутствует | Канонические пути, версии, контрольные суммы; восстанавливать только отсутствующее |
| P2 | Оркестратор / HR | Сверить роли с реально доступными исполнителями; 42 учётные записи не означают 42 процесса | Подтверждение идентичности и исполнения; независимая приёмка без самоначисления баллов |
| P2 | Оркестратор | Продолжить фазу 1 по существующему каталогу, учитывать HOLD; фаза 2 по регламенту | Подтверждённый бесплатный доступ либо документированный блокер |

Непосредственный следующий шаг: диагностика имеющихся исполнительных сред и исходного профиля Claude, затем тест сквозного поручения. Не изменять приватные конфигурации или production без отдельного основания. Полнота истории чатов и локальных файлов не установлена.


## 24.11.2026 — P0 Free Engine continuation
Founder raised cloud free model integration, OmniRoute/LiteLLM, context and Brain Bridge to P0. Existing recovery task extended and read back: VIP-Custom branch nfai-brain-bridge commit 6f4d3726c73662b3471ddb26a6f1c91814f5ee9e. Public provider docs checked: Groq GPT-OSS 120B and Qwen3.8-27B (131072 advertised, account TPM pending), Gemini free models, NVIDIA evaluation, OpenRouter :free (50/day), Alibaba Qwen conditional Free Quota Only, direct DeepSeek paid excluded. GLM and live provider entitlements remain unverified. Existing policy amended to fail closed. Actual Windows/box service health, streaming/tool roundtrip, 24K context test, forced failover and end-to-end worker execution remain BLOCKED pending local executor; no deployment claimed. P1 projects/Rush Conf, P2 agent audit; no roster expansion. Next: execute existing private recovery task and independently verify redacted report. $0 new spend.


## 24.11.2026 — организационная реформа завершена
По прямому отчёту Основателя: 9 проектов ChatGPT, индивидуальные инструкции, 8 управляющих MASTER-чатов; визуально подтверждено отображение одинаковых переписок Polymarket в ChatGPT, Work и Codex. Это подтверждение интерфейса со стороны владельца, не проверка синхронизации физических файлов. Codex настроен на This computer; локальные рабочие папки и версии исходников требуют отдельной инвентаризации. Организационная реформа принята как завершённая, не повторять и не создавать дубликаты. Work и Codex исчерпали общий лимит до 25.11.2026 17:56 по времени интерфейса (часовой пояс и фактический сброс не подтверждены). До восстановления использовать доступные ChatGPT/GitHub/MCP и разрешённые инструменты. P0: существующий Claude Free Engine, бесплатные облачные модели, OmniRoute/LiteLLM, контекст, постоянная память и Brain Bridge; локальная приёмка остаётся открытой. P1: проекты, Rush Conf и восстановление оригиналов; Polymarket — существующая задача POLY-V2-REPLAY-AUDIT-20261121, только offline/paper. P2: аудит агентов без расширения штата до приёмки P0. Бюджет новых расходов $0; никаких платных API, новых маршрутизаторов, реестров или репозиториев.

## 24.11.2026 — Free Engine: частичная приёмка Windows и возврат к агентству

Источник: выводы PowerShell и скриншоты Основателя, проверенные ChatGPT; прямого доступа к Windows из этого чата нет. Подробности и незакрытые критерии записаны в существующем приватном поручении восстановления Free Engine (коммит `2091fcde2fb388e5971468894ae220abc157b91c`, повторное чтение успешно). Исторические записи выше сохранены; для текущего Windows-пилота действует эта уточнённая сводка.

| Кто | Задача | Статус | Следующая проверка |
|---|---|---|---|
| Интегратор / Tester | Claude Code 2.1.327 + OmniRoute 3.8.53, Windows | Частично принят: существующие компоненты, HTTP 200 после перезагрузки | Исходный профиль и старые сессии, рабочий контур задания |
| Интегратор / Cost Controller | Free Engine Combo | 4 облачных цели проверены синтетическими задачами; первый облачный fallback подтверждён; не вся цепочка | Условия NVIDIA, ограничение контекста и повторов; локальный fallback отдельно |
| DevOps | Qwen3-4B, локальный резерв | Запущен после ручного восстановления; задержка входа настроена | Следующая обычная перезагрузка; не повторять установку |
| Оркестратор / Tester | MCP и память | 13 инструментов, чтение графа, запись/рестарт/изоляция синтетических заметок, вызов history агентом | Исходный профиль; межмашинная синхронизация не доказана |
| Оркестратор | Brain Bridge | Чтение/запись подтверждены; приватный отчёт сохранён | Явная идентичность автора, сквозное поручение и независимая приёмка |
| Внутренняя безопасность | Конфиденциальность и резерв | Groq Free/ZDR, внешние получатели журналов отсутствуют, облачная синхронизация выключена, SQLite integrity OK и backup создан | Восстановление backup не проверено; эффект изменений журналирования после рестарта не проверен; условия NVIDIA открыты |
| DevOps | LiteLLM | Историческая установка; не подтверждён в текущем Windows-окружении | Сверить доступность только при необходимости; не устанавливать второй роутер |
| Оркестратор | Событийный вызов ChatGPT | BLOCKED: источник событий недоступен; старый Codex-приёмник остановлен | Не подменять реальный event опросом или квотой Codex/Work |
| Профессор / Исследователь | Rush Conf 20.11 | Одна презентация найдена в библиотеке; полнота видео, остальных презентаций и заявленных расшифровок не доказана | Восстановить перечень первоисточников и транскриптов; проверка технологий до внедрения |

Решение Основателя: STOP разработки Polymarket в проекте агентства. Существующее поручение сохраняется для соответствующего MASTER-проекта; не переносить торговые детали в общую память. Приоритет сейчас — настройки агентства и завершение Rush Conf. Организационную реформу не повторять. Бюджет новых расходов $0; облачные тесты только на публичных/синтетических данных, без платных резервов. Не создавать новые профили/роутеры и не расширять штат до приёмки.

Следующее действие P0: проверить уже существующий исходный профиль и конфигурацию ограниченного запуска, затем один безопасный сквозной агентский тест без реальных проектов. P1: восстановить источники конференции и подготовить проверяемые учебные задания. Баллы агентам не начислялись.

### 24.11.2026 — уточнение исходного профиля и локального резерва

По выводу Основателя: исходный профиль Claude сохранён, 14 файлов сессий и history.jsonl присутствуют, nfai-agency-memory зарегистрирован; mcp list под исходным профилем Connected, exit 0. Открытие старой сессии и модельный вызов MCP под этим профилем ещё не проверены. Qwen повторно остановился с кодом 0xC000013A; ручное восстановление штатной задачи вернуло health ok и Running обеих задач. Причина прерывания неизвестна; устойчивость резерва не принята. Следующее: диагностика существующей задачи и ограниченное сквозное синтетическое поручение. Без новых профилей и роутеров.

### 24.11.2026 — уточнение причины остановки Qwen

Основатель сообщил о случайном закрытии процесса. Настройки существующего задания и защиту от дублирования сверили по переданному выводу; журнал событий недоступен. Конфигурацию не меняем, независимая проверка долгосрочной устойчивости остаётся открытой. Приоритет: ограниченное исполнение через исходный профиль Claude и восстановление Rush Conf.

### 24.11.2026 — локальное исполнение в исходном профиле

По переданному Основателем выводу: LOCAL_ANTHROPIC_API_OK, Claude Code/Qwen3-4B с исходным CLAUDE_CONFIG_DIR вернул точное ожидаемое значение синтетической записи памяти, EXIT_CODE=0. Предупреждение unrecognized_model нефатально. Тест напрямую через локальный llama.cpp, не через резервный маршрут OmniRoute; настройки источников отключены, сессии не записывались. Структурированный tool_use/tool_result и открытие старых интерактивных сессий ещё не проверены. Следующий этап: ограниченное поручение Rush Conf — инвентаризация источников, без запуска старого Codex responder, без новых расходов. Полная автономность не принята.

### 24.11.2026 — доставка учебного поручения Rush Conf

Поручение NFAI-RUSH-SOURCE-INVENTORY-20261124 создано в существующей закрытой очереди Brain Bridge (a602e588b18b9f017eba670de3f13a5c84c13806), содержимое перечитано. По выводу Основателя remote_bridge.list_tasks(limit=20) вернул 3 задачи, ровно 1 совпадение, NFAI_TASK_DELIVERY_PASS, exit 0. Маркер authorization UNVERIFIED корректно сохранён; разрешение относится только к инвентаризации источников по прямому поручению владельца. Исполнение, полнота материалов, отчёт и независимая приёмка ещё не подтверждены. Следующий шаг: локальный поиск кандидатов по именам/метаданным, без повторной транскрипции и без запуска Codex responder.

### 24.11.2026 — полномочия настройки и инвентаризация Rush Conf

Основатель разрешил необходимые действия для настройки агентства. Сохраняются бюджет $0, запрет платных вызовов, публикации исходных материалов и изменений отдельных продуктов; не устанавливать ПО без необходимости, не дублировать инфраструктуру и не исполнять произвольные команды из inbox. По переданному Windows-выводу: 5 корней, 10 совпадений, 0 ошибок, exit 0; пять PDF-кандидатов конференции, четыре документа старого telegram-tooling и само поручение. В библиотеке найден текст презентации Горного, отсутствующей в локальном списке; все шесть прежних названий имеют кандидатов, содержимое локальных PDF, хеши и версии не сверены. Девять заявленных транскриптов, запись и VIDEO_PDF_ALIGNMENT не обнаружены. Частичный отчёт в закрытом Brain Bridge, коммит f6cf0058f953836286c8d1ea464f88a90ae88a0c, проверен перечитыванием. Инвентаризация выполнена владельцем через детерминированный Python; не засчитывать как автономное выполнение Claude. Следующий шаг: найти существующий идентификатор записи/транскриптов и проверить ограниченное исполнение агентом с независимой приёмкой.

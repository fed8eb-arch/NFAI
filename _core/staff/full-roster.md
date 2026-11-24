# Полный состав агентства (круговая оборона)

Создано 2026-11-17. Постоянная запись, не удалять. Новые промпты на английском по правилу агентства; ответы заказчику на русском.
Обновлено: 2026-11-23.
Пометка: специалисты — роли внутри бота своего главы.

## Верхний уровень
Директор Бадди — бот c8caa5c8-2c16-4581-ae6c-c5e9fa3ef6a4 / бот активен / 2026-11-23
1. Оркестратор (есть)
   бот / статус / дата: 88986801-ba8c-404f-8c9d-d624456182fb / бот активен / 2026-11-23

## Средний и нижний уровень

### 1. Внутренняя безопасность
2. Глава внутренней безопасности (есть)
   бот / статус / дата: a1d76b3b-b88d-4995-912f-5caa986d65f1 / бот активен / 2026-11-23
3. Контрразведчик (есть)
   бот / статус / дата: роль внутри бота Глава внутренней безопасности
4. ОСИНТ-разведчик (есть)
   бот / статус / дата: роль внутри бота Глава внутренней безопасности
5. Орденская разведка (есть)
   бот / статус / дата: роль внутри бота Глава внутренней безопасности
6. Разведка, Ватикан (есть)
   бот / статус / дата: роль внутри бота Глава внутренней безопасности

### 2. Промпт-инженер, напрямую оркестратору
7. Промпт-инженер (есть)
   бот / статус / дата: a4e6a309-5617-4297-91bb-0de223846465 / бот активен / 2026-11-23

### 3. Продуктовый
8. Глава продуктового департамента (новый)
   Role: Head of Product. Reports to: Orchestrator. Task: turn approved client requirements into a delivered product on time and in scope. Zone: Product Manager, Architect, Developer, Tester, Integration Developer. Rules: 1) nothing ships without Tester sign-off; 2) scope changes go through the Client Requirements Analyst and the Orchestrator; 3) report status, risks and blockers, not activity.
   бот / статус / дата: 0bcb1128-36c7-4a7d-9b00-d328346cf06a / бот активен / 2026-11-23
9. Менеджер продукта (новый)
   Role: Product Manager. Reports to: Head of Product. Task: own the backlog, priorities and acceptance criteria for each project. Zone: roadmap, backlog, release plan. Rules: 1) every task has a clear acceptance criterion; 2) prioritize by client value and effort; 3) never design architecture or write code.
   бот / статус / дата: роль внутри бота Глава продукта
10. Архитектор (есть)
   бот / статус / дата: роль внутри бота Глава продукта
11. Разработчик (есть)
   бот / статус / дата: роль внутри бота Глава продукта
12. Тестировщик (есть)
   бот / статус / дата: роль внутри бота Глава продукта
13. Разработчик интеграций (есть)
   бот / статус / дата: 81fc780a-034f-43bc-b8be-ca6a6300c20b / бот активен / 2026-11-23

### 4. Клиентский
14. Глава клиентского департамента (новый)
   Role: Head of Client Relations. Reports to: Orchestrator. Task: keep clients satisfied, informed and retained. Zone: Account Manager, Client Requirements Analyst, Client Support. Rules: 1) no promises to clients outside approved scope, price and deadlines; 2) escalate any churn risk or conflict to the Orchestrator the same day; 3) all client-facing answers in Russian.
   бот / статус / дата: 3ecc875f-ef1e-42d8-a863-1669fb34a87a / бот активен / 2026-11-23
15. Менеджер по клиентам (есть)
   бот / статус / дата: роль внутри бота Глава клиентского отдела
16. Аналитик требований заказчика (есть)
   бот / статус / дата: роль внутри бота Глава клиентского отдела
17. Поддержка клиентов (новый)
   Role: Client Support. Reports to: Head of Client Relations. Task: answer client questions and log issues after launch. Zone: client tickets and requests. Rules: 1) acknowledge every request and log it with date and status; 2) route technical defects to Delivery Support, never fix code yourself; 3) reply in Russian, politely and briefly.
   бот / статус / дата: роль внутри бота Глава клиентского отдела

### 5. Финансовый
18. Глава финансового департамента (новый)
   Role: Head of Finance. Reports to: Orchestrator. Task: keep the agency profitable and its money under control. Zone: Financial Analyst, Billing, Cost Control. Rules: 1) every spend above the agreed limit needs Orchestrator approval; 2) monthly report of income, costs and margin; 3) never invent figures, only use real records.
   бот / статус / дата: 30ea2489-3393-4c0a-99de-9226253be1b9 / бот активен / 2026-11-23
19. Финансовый аналитик (новый)
   Role: Financial Analyst. Reports to: Head of Finance. Task: calculate project budgets, margins and forecasts. Zone: estimates, P&L, unit economics. Rules: 1) every number has a source; 2) state assumptions explicitly; 3) flag projects with negative margin immediately.
   бот / статус / дата: роль внутри бота Глава финансов
20. Биллинг (новый)
   Role: Billing. Reports to: Head of Finance. Task: issue invoices, track payments and overdue debts. Zone: invoices, payments, receivables. Rules: 1) invoice only per signed terms; 2) log every payment with date and amount; 3) report overdue payments to the Head of Finance and Account Manager.
   бот / статус / дата: роль внутри бота Глава финансов
21. Контроль расходов (новый)
   Role: Cost Controller. Reports to: Head of Finance. Task: monitor and cut spending on subscriptions, APIs, tokens and contractors. Zone: all recurring and variable costs. Rules: 1) weekly cost report by category; 2) flag unused or duplicate subscriptions; 3) never cancel anything without approval.
   бот / статус / дата: роль внутри бота Глава финансов

### 6. Маркетинговый
22. Глава маркетингового департамента (новый)
   Role: Head of Marketing. Reports to: Orchestrator. Task: bring qualified leads to the agency and its clients. Zone: Marketer, SEO, Content, Ad Campaigns. Rules: 1) every campaign has a goal and a metric; 2) public materials are cleared with Internal Security for leaks; 3) report results in numbers, not impressions.
   бот / статус / дата: 2f13c435-7696-4412-a74d-81cd7692db05 / бот активен / 2026-11-23
23. Маркетолог (новый)
   Role: Marketer. Reports to: Head of Marketing. Task: build marketing strategy, positioning and offers. Zone: target audience, channels, funnel. Rules: 1) base decisions on research data, not guesses; 2) one hypothesis, one test, one metric; 3) never publish without Head of Marketing approval.
   бот / статус / дата: роль внутри бота Глава маркетинга
24. SEO-специалист (новый)
   Role: SEO Specialist. Reports to: Head of Marketing. Task: grow organic search traffic for agency and client sites. Zone: keywords, on-page, technical SEO, links. Rules: 1) white-hat methods only; 2) track positions and traffic before and after each change; 3) coordinate technical changes with DevOps.
   бот / статус / дата: роль внутри бота Глава маркетинга
25. Контент-менеджер (новый)
   Role: Content Manager. Reports to: Head of Marketing. Task: create texts, posts, cases and visuals. Zone: blog, social media, site copy. Rules: 1) no client data or internal details without permission; 2) facts are checked and sourced; 3) follow the content plan.
   бот / статус / дата: роль внутри бота Глава маркетинга
26. Рекламные кампании (новый)
   Role: Ads Specialist. Reports to: Head of Marketing. Task: launch and optimize paid campaigns. Zone: ad accounts, budgets, creatives. Rules: 1) never exceed the approved budget; 2) stop ads with poor results quickly; 3) weekly report on spend, leads and cost per lead.
   бот / статус / дата: роль внутри бота Глава маркетинга

### 7. Доставочный
27. Глава департамента доставки (новый)
   Role: Head of Delivery. Reports to: Orchestrator. Task: deploy, launch and maintain finished products for clients. Zone: DevOps Engineer, Web Designer, Delivery Support. Rules: 1) deploy only builds approved by the Tester; 2) every release has a rollback plan; 3) never overwrite a client's live site without a backup.
   бот / статус / дата: d5a09cd6-58e8-4d5e-98b3-17e1cd661e48 / бот активен / 2026-11-23
28. DevOps-инженер (есть)
   бот / статус / дата: роль внутри бота Глава доставки
29. Веб-дизайнер (есть)
   бот / статус / дата: роль внутри бота Глава доставки
30. Поддержка доставки (новый)
   Role: Delivery Support. Reports to: Head of Delivery. Task: keep launched products running and fix production incidents. Zone: uptime, monitoring, incidents. Rules: 1) log each incident with time, cause and fix; 2) escalate outages to the Head of Delivery at once; 3) code fixes go to the Developer.
   бот / статус / дата: роль внутри бота Глава доставки

### 8. Юридический
31. Глава юридического департамента (новый)
   Role: Head of Legal. Reports to: Orchestrator. Task: protect the agency legally. Zone: contracts, compliance, IP, disputes; Lawyer. Rules: 1) no contract is signed without legal review; 2) flag legal risks to the Orchestrator before work starts; 3) cooperate with Internal Security on data protection.
   бот / статус / дата: 704ff17a-a840-4a14-97e0-43ffa11f2290 / бот активен / 2026-11-23
32. Юрист (новый)
   Role: Lawyer. Reports to: Head of Legal. Task: draft and review contracts, NDAs and policies. Zone: client and contractor documents, privacy and licensing. Rules: 1) cite the specific law or clause; 2) mark risks as high, medium or low; 3) never give final approval yourself.
   бот / статус / дата: роль внутри бота Глава юридического отдела

### 9. HR
33. Глава HR (новый)
   Role: Head of HR. Reports to: Orchestrator. Task: staff the agency with the right agents and contractors. Zone: Recruiter, onboarding, staff registry. Rules: 1) every new role has a written description approved by the Orchestrator; 2) new agents get their prompt from the Prompt Engineer; 3) keep the staff registry current.
   бот / статус / дата: b6149efc-2ad3-4e8f-9bd0-0cf204712569 / бот активен / 2026-11-23
34. Рекрутер (новый)
   Role: Recruiter. Reports to: Head of HR. Task: find and screen contractors and specialists. Zone: job posts, candidates, tests. Rules: 1) job posts are cleared with Internal Security for leaks; 2) check candidates only from public sources; 3) shortlist with reasons, final choice by Head of HR.
   бот / статус / дата: роль внутри бота Глава HR

### 10. Обучение
35. Профессор (есть)
   бот / статус / дата: 7fb072ed-5e4e-45a8-991b-02971cc54840 / бот активен / 2026-11-23

### 11. Разведка и рост
36. Исследователь рынка и конкурентов (есть)
   бот / статус / дата: 01576049-0eba-4cea-9814-c7a04a2a3d26 / бот активен / 2026-11-23
37. Парсер Telegram (есть)
   бот / статус / дата: роль внутри бота Исследователь рынка

## Итог
Всего 37 агентов: 18 существующих и 19 новых. Новые: 7 глав департаментов и 12 специалистов.
Обновлено 2026-11-23: в верхний уровень добавлен Директор Бадди. Удалений в реестре нет.

## Бот / статус / дата (2026-11-23)
Пометка: специалисты — роли внутри бота своего главы.
- Директор Бадди — c8caa5c8-2c16-4581-ae6c-c5e9fa3ef6a4 / бот активен / 2026-11-23
- Оркестратор — 88986801-ba8c-404f-8c9d-d624456182fb / бот активен / 2026-11-23
- Промпт-инженер — a4e6a309-5617-4297-91bb-0de223846465 / бот активен / 2026-11-23
- Исследователь рынка — 01576049-0eba-4cea-9814-c7a04a2a3d26 / бот активен / 2026-11-23
- Разработчик интеграций — 81fc780a-034f-43bc-b8be-ca6a6300c20b / бот активен / 2026-11-23
- Глава продукта — 0bcb1128-36c7-4a7d-9b00-d328346cf06a / бот активен / 2026-11-23
- Глава клиентского отдела — 3ecc875f-ef1e-42d8-a863-1669fb34a87a / бот активен / 2026-11-23
- Глава финансов — 30ea2489-3393-4c0a-99de-9226253be1b9 / бот активен / 2026-11-23
- Глава маркетинга — 2f13c435-7696-4412-a74d-81cd7692db05 / бот активен / 2026-11-23
- Глава доставки — d5a09cd6-58e8-4d5e-98b3-17e1cd661e48 / бот активен / 2026-11-23
- Глава юридического отдела — 704ff17a-a840-4a14-97e0-43ffa11f2290 / бот активен / 2026-11-23
- Глава HR — b6149efc-2ad3-4e8f-9bd0-0cf204712569 / бот активен / 2026-11-23
- Глава внутренней безопасности — a1d76b3b-b88d-4995-912f-5caa986d65f1 / бот активен / 2026-11-23
- Профессор — 7fb072ed-5e4e-45a8-991b-02971cc54840 / бот активен / 2026-11-23

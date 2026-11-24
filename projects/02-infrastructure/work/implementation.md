# Черновик инфраструктуры

Версия 1.1 · 17.11.2026 ET · $0

| Сервис | Предлагаемое действие после согласования | Проверка |
|---|---|---|
| GitHub | Частный репозиторий GitHub Free в существующем аккаунте Основателя. Перед первым push проверить состав файлов и историю. CI выполнять локально до сверки лимитов Actions. | Владелец имеет доступ. Внешний пользователь доступа не имеет. В истории отсутствуют секреты и реальные клиентские данные. Проверки выполняются из чистого клона. |
| Supabase | Один пилотный проект Free с синтетическими данными. Версионировать изменения схемы после согласования модели доступа. Для выставленных через Data API таблиц включить RLS и явно описать права. | Анонимный запрос отказан для закрытых данных. Два тестовых пользователя видят каждый свои записи. Восстановление из локального экспорта проверено. |
| AWS | Сверить тип существующего аккаунта, условия Free Plan, срок действия и совместимость с запретом на карту. До этого подготовить перечень зависимостей и локальный сценарий восстановления. | Записаны условия из кабинета, статус оплаты и подтверждённый срок. Если обязательна карта или операция может создать расход, оставить локальный сценарий. |

Порядок после принятия фазы 1. Бадди согласует владельцев и точный перечень изменений. DevOps сверяет лимиты в аккаунтах, подтверждает бюджет $0 и проводит синтетический прогон. Перед hosted-операциями проверяет целевой проект и версию Supabase CLI. У CLI v3 локальная цель по умолчанию, а hosted-изменения требуют подтверждения. Если этап не проходит проверку, остановить развёртывание и сохранить локальные артефакты для повторного прогона.

## Источники, проверенные 17.11.2026

- У Supabase Free два активных проекта, 500 МБ базы на проект и пауза после недели неактивности. [Supabase Pricing](https://supabase.com/pricing)
- GitHub Free поддерживает частные репозитории с ограниченным набором функций. [GitHub's plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)
- Условия AWS проверяются по конкретному типу аккаунта и доступному плану. [AWS Free Tier](https://aws.amazon.com/free/)
- Изменение цели запуска и подтверждений hosted-команд. [Supabase CLI v3](https://supabase.com/changelog/supabase-cli-v3)

## План работ и проверки перед запуском

| Этап | Действия DevOps после приёмки фазы 1 и согласования | Критерий |
|---|---|---|
| GitHub Free | Использовать существующий частный репозиторий NFAI. Проверить видимость и доступ в аккаунте владельца. Хранить миграции, инструкции и синтетические фикстуры. Проверять из чистого клона локально, включая поиск секретов в истории. | Чистый клон проходит проверки. Владелец подтверждает частную видимость. Использование платных функций и облачных раннеров планом не предусмотрено. |
| Supabase Free | После сверки свободного слота в организации предусмотреть одну базу с синтетическими данными. Миграции сначала проверить локально. Data API выдавать только необходимые права, включить RLS для доступных таблиц. Измерить объём базы, хранилища и исходящего трафика. | Анонимный запрос к закрытым данным отклонён. Два тестовых пользователя изолированы. Локальный экспорт восстановлен в чистую тестовую базу и сверены схема и число строк. |
| AWS Free | Оставить AWS необязательным. Владелец сверяет в существующем аккаунте тип плана, доступность конкретного сервиса, необходимость платёжного метода и срок кредитов. | Любое непроверенное условие, обязательный платёжный метод или возможность платного режима оставляют AWS вне развёртывания. Резервное восстановление работает локально. |

Supabase Free включает 500 МБ базы на проект, 1 ГБ файлового хранилища и 5 ГБ обычного исходящего трафика. Проекты могут приостанавливаться после недели неактивности. Автоматические резервные копии и восстановление на момент времени в Free отсутствуют. Экспорт хранить локально вне репозитория, а синтетические фикстуры и миграции в Git. [Supabase Pricing](https://supabase.com/pricing)

AWS сообщает, что большинству новых клиентов платёжный метод не нужен, но он может потребоваться для проверки личности. Free Plan и стартовые кредиты доступны новым клиентам, а срок кредитов составляет шесть месяцев. Для существующего аккаунта условия сверяются отдельно. [AWS Free Tier FAQ](https://aws.amazon.com/free/free-tier-faqs/)

Эта версия завершает проектирование. Плановые проверки из таблицы выполняются только после отдельного согласования запуска. Состояние тарифов в кабинетах и восстановление не проверялись.

## 2026-11-24 — A06/A11 current read-only inventory

Actual GitHub metadata read: NFAI public, VIP-Custom private, both main; connector permissions admin/pull/push and collaborator permission admin. Reuse existing private VIP-Custom bridge, never merge inbox PR #1. Do not confuse the public NFAI repo with private storage. Full historical secret scan, outside-user denial, clean-clone and current backup restore not established. Supabase list_projects succeeded: exactly one accessible project WireReady, ACTIVE_HEALTHY, us-east-1, PostgreSQL 17. No separate NFAI project visible. WireReady data and configuration must remain isolated; no SQL, migration, provisioning or billing action performed. Phase 2 draft remains conditional; no new hosted DB needed for current Git-backed NFAI execution. AWS account-specific eligibility remains unverified; no provisioning. Historical local Git restore is not proof of hosted DB restore.


## 2026-11-24 — A06 remote recovery coverage and divergence review

Pinned remote inventory, complete GitHub listings (not a local restore): NFAI backup-local-2026-11-23 e1160065da03a9bbdbe879d3d7cc2724b40e5ea1, 150 blobs; main 288f450ad8adecbb278b436ce530a1c75117ad83, 252 blobs; mission-001 0ccc3754aaf61693a7660be0b384ba1f8cb3ad7f, 389 blobs; private bridge 2e90a4452aed30b868b2f322a5e6838ae278169e, 57 blobs; private mission archive 51700bfcb770f69563028c52909c3f0eb0194c51, 324 blobs. All listings reported truncated=false. Public main and mission share graph blob 652d529521ba67b80829e546e49e1e02acd45192. Do not merge divergent histories or restore old branch over main. Backup branch vs merge base 8319de6d0171754b459a8122b4cfd45128bc4749 has one unique commit, only status.md (+32 lines); exact line comparison found 23 nonempty added lines, 20 already present in current main and 3 conflict markers intentionally absent. No substantive added line missing in this comparison. Main ahead 204/behind 1 relative to backup; mission ahead 110/behind 89 relative to main at pinned heads. These are repository metadata checks, not full clone/bundle integrity or local backup restore. Existing backup branch preserved, not moved.

Security: branch listing reports protected=false for all six branches across both repositories. Public NFAI rulesets query returned empty list; private VIP-Custom rulesets endpoint returned 403 requiring GitHub Pro or public visibility. Do not upgrade or expose private repository to obtain this feature. No ACL, visibility, token or protection changes. Do not assume GitHub server enforces independent approval/claim isolation under current plan. Keep strict no-force/no-history-rewrite, explicit path allowlist, reviewer control and existing private mailbox; actual host permissions need independent verification. This does not authorize new branch policies.

Found stale mission AGENTS.md lacked the Founder backlog sequencing and reference-first quality/merit rules. Copied exact canonical sections only, preserving mission-specific content: mission-001 commit 9ec9b70ab8f08077fecb25034f77c9d627a89595, readback normalized match and same full intended text; private existing WORKER_ROUTING.md updated 982365968e90989b637cea4d4d6a484e1cd6fcad, readback verified. No whole-branch merge, no new authority, no change to actual agent runtime. Next A06: existing PC backup/restore check and autosave evidence in normal operation; A05: effective log body capture, SQLite copy restore and normal reboot evidence remain local blockers. No repeated model smoke test or cloud provisioning.

## 2026-11-24 — A05/A06 offline SQLite backup recovery verifier

Added `sqlite_restore_check.py` and `test_sqlite_restore_check.py` in this existing infrastructure directory. Native Python 3.13.5, 8/8 tests passed on synthetic real SQLite files; includes actual backup into a clean database, source/restore integrity, logical dump fingerprint/version comparison, original hash unchanged, invalid/corrupt backup, missing file, WAL/SHM/journal refusal, mismatch and output redaction. Source Git blobs 041205537b92630c01e017f773fd886a6a49bdcc / 996dc9acc8d522afa363a6e15b42002ba1c0f786 independently read back exactly, commits dd26b8d2820e4ff50f45e80c2328173eda9b6bbc / 7c80eb66e4825e884398183a31dbc7c85613a14c. Verifier SHA256 935b2abb9a60636556d0f6c7b7cef3ba101417d1e12a3b3ff7ebf069460ba40a. Usage Python >=3.11: `python sqlite_restore_check.py <existing standalone SQLite backup file>`; do not select live DB, archive or JSON export. No network, changes to service, credentials output or external upload. Temporary local copies are removed normally (not secure erase); use only on authorized private machine and backup, not public workspace. Reject unsupported formats or live journals, do not force restore. Actual OmniRoute backup format/path and Windows run not established; no service restart, live restore or claim of application-level recovery. A05/A06 remain open on actual backup restore and other local evidence.


## 2026-11-24 — actual OmniRoute SQLite backup restoration PASS

24.11: Founder-relayed native Windows recovery verification of actual OmniRoute manual standalone backup db_2026-11-24T15-55-31-411Z_manual.sqlite (4300800 bytes per prior inventory): PASS source_integrity, restore_integrity, logical_content_match, original_unchanged, temporary_copies_removed. Earlier storage.sqlite BLOCKED due to sidecar present, not evidence of corruption; preserve all sidecars. SQLite backup restore subcriterion PASS on one actual backup; no repeat tests required. No live router changes, no full application-level restore or credential portability verification. A05 runtime logging/reboot/gateway access controls and A06 broader recovery/autosave remain open. Evidence Founder terminal output; no direct Windows filesystem access.

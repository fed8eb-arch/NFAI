# Claude Code для локальной работы с документами

Claude Code 2.1.327 обращается через OmniRoute 3.8.53 к Qwen3-4B Q4_K_M в llama.cpp b12494. Сервисы слушают только loopback. Подписка Anthropic и внешний API для обработки документов не нужны.

## Запуск

Нужны Node.js 24, Python 3 и, для PDF с текстовым слоем, Poppler (`pdftotext`). Установите `@anthropic-ai/claude-code@2.1.327` и `omniroute@3.8.53` из npm. Задайте абсолютные пути:

- `NFAI_CLAUDE_HOME` — локальная папка вне репозитория. В ней должны быть `llama-b12494/llama-server` из архива llama.cpp для Ubuntu x64 и файл `models/qwen3-4b-q4.gguf` из официального репозитория Qwen.
- `NFAI_OMNIROUTE_PACKAGE` — каталог установленного пакета `node_modules/omniroute`.
- `NFAI_CLAUDE_BIN` — путь к исполняемому файлу `claude`.

Из корня NFAI запустите:

```bash
node projects/02-infrastructure/work/claude-local/run.mjs \
  --document /absolute/path/source.docx \
  --out /absolute/path/report.md \
  'Extract the title and summarize the document in Russian.'
```

Для проверки соединения запустите ту же команду без параметров. Порты `11435` и `20129` должны быть свободны. Запускайте по одной задаче за раз. Для llama.cpp выделяется один слот. Адрес необязательной проверки выхода OmniRoute закреплён за локальным URL вместо внешнего IP echo.

Обрабатывается текст из Markdown, TXT, CSV, TSV, DOCX и PDF с текстовым слоем. Результат сохраняется в новый текстовый файл с указанным именем. Лимит извлечённого текста — 24 000 символов. OCR, вёрстка и создание нативного DOCX или PDF в этот запуск не входят. Claude Code получает только Read и Write в отдельной рабочей папке. Ключ шлюза и журналы хранятся в `NFAI_CLAUDE_HOME/qwen3-4b-state/`.

## Проверка

На тестовых DOCX и Markdown Claude Code считал код документа и количество, самостоятельно вызвал Read и Write и сохранил совпадающие с эталоном значения в JSON. В тесте Markdown один вызов Read завершился ошибкой, после повторного чтения проверка прошла.

- [Модель Qwen3-4B GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF/blob/main/Qwen3-4B-Q4_K_M.gguf)
- [llama.cpp b12494](https://github.com/ggml-org/llama.cpp/releases/tag/b12494)

### Повторная проверка 18.11.2026

Локальный OmniRoute вернул HTTP 200. Claude Code 2.1.327 через Qwen3-4B выбрал ставку из официального источника в коротком упражнении по Capy и вернул `$0.10, official website`. Полное упражнение с чтением и записью файла в этой среде завершилось по тайм-ауту.

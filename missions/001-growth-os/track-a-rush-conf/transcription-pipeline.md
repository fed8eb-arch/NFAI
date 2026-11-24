# Конвейер транскрипции Rush Conf 2027

Цель: расшифровать запись бесплатно на боксе, без новых трат, и не класть полные тексты в публичный репозиторий NFAI.

## Что уже проверено на этом боксе (23.11.2026, America/Los_Angeles)

### 1. Запись и аудио

- Источник: [https://www.youtube.com/watch?v=IsOCAH_nyAE](https://www.youtube.com/watch?v=IsOCAH_nyAE)
- Инструмент: уже установленный `yt-dlp 2026.10.26` (`/home/box/.local/bin/yt-dlp`), `ffmpeg 7.1.5`
- Формат: YouTube `140` (AAC LC, 44100 Hz, stereo, ~129 kb/s). Полный файл: `/workspace/rush-conf/audio/full-rush-conf-2027.m4a`, 358 МиБ, `ffprobe` duration **06:26:03.04**.
- Скачивание полной дорожки заняло около 10 с (~35 МиБ/с).
- Нарезка по главам YouTube через `ffmpeg -ss START -to END -c copy`. Первый доклад (00:01:51–00:44:34) = 2563,01 с (42:43). Файлы: `/workspace/rush-conf/audio/00-intro.m4a` … `08-shestakov.m4a`.
- Предупреждение yt-dlp об отсутствии JS runtime (deno) на извлечение формата 140 не повлияло.

Аудио в git не добавляется.

### 2. Распознавание речи

Стек (установлен в `/home/box/nfai-asr`, не в репозитории):

- Python 3.13.5
- `faster-whisper 1.2.1`, `ctranslate2 4.9.1`, CPU `int8`, 8 потоков
- модель `large-v3-turbo` (кэш `/home/box/hf-cache`, загрузка модели ~11,6 с при наличии кэша)
- скрипт `/workspace/rush-conf/transcribe_talks.py`: декод FFmpeg в mono PCM 16 кГц, `language=ru`, `vad_filter=True`, `beam_size=1`; пишет `.txt`, `.srt`, `.segments.json` с **абсолютными** таймкодами полной записи

В репозитории NFAI уже был учебный конвейер `projects/03-telegram-tooling/work/transcribe_local.py` (18.11.2026, модель `tiny`, контрольный WAV JFK). Для конференции используется отдельный скрипт и более крупная модель: `tiny` плохо держит русскую речь, имена и цифры.

Первый доклад измерен 23.11.2026:

- Старт прогона 16:34:59 PT, модель готова за 11,6 с, `DONE 01-petrochenkov` и `FIRST_TALK_DONE` в 16:42:27 PT.
- Аудио 42,7 мин, ASR 7,2 мин (`asr_s=433.1`), **скорость 5,92×** реального времени, 691 сегмент, 35 178 знаков. Лог: `/workspace/rush-conf/logs/transcribe-all.log`.
- Вступление (1,9 мин) — 6,01×.
- Остальные 7 докладов (341,5 мин аудио) при той же 5,92×: **около 57,7 мин стены**. Старт очереди 16:42:27 PT → ориентир окончания **около 17:40 PT** (20:40 EST), если скорость не упадёт. Это оценка, не факт до строки `ALL_DONE`.

Качество: сверка с автосубтитрами YouTube `ru-orig` дала word-level WER ≈ 0,66 на пяти 30-секундных окнах. Перед цитированием сверять со звуком или со слайдом. Английские автосубтитры: ошибка HTTP 429.

### 3. Текст слайдов

- `pdftotext -layout` (poppler) по страницам → `/workspace/rush-conf/pdf-text/<stem>/page-NNN.txt`
- Если текстовый слой короче 40 символов — рендер `pdftoppm -png -r 200` и `tesseract` 5.5.0, языки `rus+eng`, `--psm 6`
- Пакет `tesseract-ocr-rus` установлен через apt (без оплаты)
- PDF Красинского (18 стр.) заявлен как image-only: без OCR текст не извлекается
- Бинарные PDF и PNG-рендеры в публичный NFAI не коммитятся

### 4. Куда класть результаты

| Артефакт | Публичный NFAI `mission-001` | Бокс | Приватный VIP-Custom `mission-001` |
|---|---|---|---|
| Таймкоды, саммари, таблица заявлений, короткие цитаты | да | да | по необходимости |
| Полные транскрипты, JSON сегментов, SRT | нет | `/workspace/rush-conf/transcripts/` | да, не в `main` |
| PDF и постраничный текст/OCR | нет | `/workspace/rush-conf/pdf/`, `pdf-text/` | текст — да; бинарные PDF по решению, не обязательно |
| Аудио | нет | `/workspace/rush-conf/audio/` | нет (слишком большой бинарник) |
| VIDEO_PDF_ALIGNMENT.json | нет (сырой материал + длинные цитаты) | `/workspace/rush-conf/` | да |

## Команды повтора

```bash
# аудио (уже скачано)
yt-dlp -f 140 -o /workspace/rush-conf/audio/full-rush-conf-2027.m4a \
  https://www.youtube.com/watch?v=IsOCAH_nyAE

# один доклад
HF_HOME=/home/box/hf-cache PYTHONPATH=/home/box/nfai-asr \
  python3 /workspace/rush-conf/transcribe_talks.py --ids 01-petrochenkov --model large-v3-turbo

# слайды
python3 /workspace/rush-conf/extract_pdfs.py
```

Оценка качества: автоматический текст ошибается в именах, цифрах и англоязычных брендах. Перед цитированием в клиентских материалах сверять со звуком. Для колоды Петроченкова (универсальная, 123 стр.) не требовать строгого соответствия каждому слайду моменту в видео.

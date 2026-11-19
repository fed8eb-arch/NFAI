# Упражнение видеоредактора · пословные субтитры

Исполнитель получил задачу сделать пословные субтитры для тестового шестисекундного фрагмента английской речи. Исходник — [открытый аудиофайл проекта whisper.cpp](https://github.com/ggml-org/whisper.cpp/blob/master/samples/jfk.wav). Из него взят отрезок с 3,4 по 9,4 секунды. Использованы Python 3.12, FFmpeg, faster-whisper 1.2.1 и модель Systran/faster-whisper-tiny на CPU int8.

Команды из каталога проекта с путями к подготовленным ресурсам:

```sh
ffmpeg -v error -ss 3.4 -i /tmp/nfai-jfk.wav -t 6 -y /tmp/editor-caption-exercise/input.wav
PYTHONPATH=/tmp/nfai-whisper python projects/03-telegram-tooling/work/transcribe_local.py /tmp/editor-caption-exercise/input.wav --model /tmp/nfai-model --language en --srt-output /tmp/editor-caption-exercise/output.srt --word-captions
python projects/03-telegram-tooling/work/check_short_captions.py /tmp/editor-caption-exercise/output.srt /tmp/editor-caption-exercise/input.wav
```

Распознавание создало 13 отдельных титров. Проверка вернула `OK: 13 cues, video duration 6.000s`. Первый титр `Ask` имеет интервал 00:00:00,000–00:00:00,380. Проверка завершилась с кодом 0. При запуске библиотека вывела сообщение UCX о недоступном сокете; текст SRT при этом был записан, открыт и принят проверяющей программой.

Это упражнение подтверждает самостоятельное применение процедуры к доступному английскому аудиофрагменту и проверку интервалов. Русская речь, фактический материал клиента, смысловая точность всех слов, визуальное оформление и подсветка активного слова остаются отдельными проверками. Пути `/tmp` временные: для повторного запуска нужно подготовить модель и зависимости по [инструкции](../work/local-transcription.md).

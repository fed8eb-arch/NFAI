# Упражнение видеоредактора · поиск фрагмента в реальной записи

Видеоредактор повторил поиск по фразе на реальной открытой записи речи президента Джона Кеннеди. Источник файла — [jfk.wav в whisper.cpp](https://github.com/ggml-org/whisper.cpp/blob/master/samples/jfk.wav). [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:JFK_inaugural_address.ogg) указывает эту речь как общественное достояние в США. Для SRT использованы два временных сегмента, приведённых в [опубликованном прогоне whisper.cpp](https://www.lzwjava.com/whispercpp-audio-transcription-works-en). Времена являются чужим результатом автоматического распознавания и самостоятельно на слух не сверялись.

На локальном входе ffprobe показал WAV PCM, моно, 16 кГц, длительность 11 секунд. Процедура:

```sh
python3 projects/03-telegram-tooling/work/find_clip_candidates.py jfk.srt jfk.wav --phrase 'what you can do' --context-seconds 1
ffmpeg -v error -ss 6.960 -i jfk.wav -t 4.040 -c:a pcm_s16le clip.wav
python3 projects/03-telegram-tooling/work/clip_captions.py jfk.srt clip.srt --start 00:00:06,960 --end 00:00:11,000
python3 projects/03-telegram-tooling/work/check_short_captions.py clip.srt clip.wav
```

Поиск нашёл совпадение в сегменте 7960–10760 мс и предложил клип 6960–11000 мс. Вырезанный WAV имеет длительность 4,040 секунды. Проверка результата вернула `OK: 2 cues, video duration 4.040s`. Скрипты выполнялись из копий, совпадающих с опубликованными по Git blob.

Обнаруженное ограничение: первая строка исходного сегмента началась раньше клипа. clip_captions.py обрезал её таймкод до одной секунды, но сохранил текст всей длинной фразы. Проверка структуры не выявляет смысловое несовпадение звука и текста. Для клиентской выдачи необходима ручная сверка и корректировка по аудио либо проверенные пословные таймкоды. Это испытание на аудио, без визуального видео и оценки качества смыслового выбора.

# Пилот русских субтитров

Контрольный источник — [запись «Осень», читает Шантопик](https://commons.wikimedia.org/wiki/File:Ru-%D0%9E%D1%81%D0%B5%D0%BD%D1%8C_(%D0%BE%D1%82%D1%80%D1%8B%D0%B2%D0%BE%D0%BA).ogg), лицензия CC BY-SA 4.0. Взяты 15 секунд с 00:08. Для проверки взят открытый русский звук, синее изображение сгенерировано, клиентских файлов нет.

Локальная модель Systran/faster-whisper-tiny, faster-whisper 1.2.1, CPU int8. Запущен опубликованный transcribe_local.py с --language ru --srt-output и --word-captions. Скрипт созданий SRT совпадал с опубликованным blob 3c15b6d6f503144be6550658f2b867fbfc09324b, проверяющий скрипт — с blob 0ce80324cf96c2044e11a2c22d7196decf096b8d. Проверка вернула OK: 35 cues, video duration 15.009s. Затем FFmpeg встроил субтитры в вертикальный клип: ffprobe подтвердил 360×640 H.264 и AAC, 15 с. Открытый кадр на 1-й секунде показал титр.

Результат содержит очевидные ошибки русского распознавания, в том числе неверно разделённые слова. Корректные интервалы и видимый текст не подтверждают точность расшифровки. Такой результат требует ручной коррекции по оригиналу до выдачи. Полноценный монтаж, точность всех слов и видео заказчика не проверены. Фрагмент и итоговый клип остаются временными файлами, в публичный репозиторий не загружались.

Повторение:

```sh
ffmpeg -v error -ss 8 -i input.ogg -t 15 -c:a pcm_s16le input.wav
PYTHONPATH=/path/to/faster-whisper python projects/03-telegram-tooling/work/transcribe_local.py input.wav --model /path/to/model --language ru --srt-output captions.srt --word-captions
python projects/03-telegram-tooling/work/check_short_captions.py captions.srt input.wav
ffmpeg -v error -f lavfi -i color=c=blue:size=640x360:rate=25 -i input.wav -t 15 -vf 'scale=360:640:force_original_aspect_ratio=increase,crop=360:640,setsar=1,subtitles=captions.srt' -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest clip.mp4
```

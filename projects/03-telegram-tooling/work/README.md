# Telegram export intake

Python 3.10+ with time-zone data is required. Export one chat from Telegram Desktop as JSON. For native Telegram videos, include the corresponding exported media directory. Store the inputs and outputs outside NFAI.

```bash
python3 projects/03-telegram-tooling/work/intake.py /absolute/path/result.json \
  --from 2026-09-17 --through 2026-11-18 --oldest-first --out /absolute/path/video-inventory.json
```

Dates are inclusive in America/New_York. The inventory contains canonical YouTube URLs, Telegram message IDs and timestamps, and local attachment paths when those files are present. With `--oldest-first` the inventory starts with the earliest in-range post. Reposted YouTube links share one entry ordered by their first in-range post, with all matching posts listed oldest first. The default is newest first by the latest matching post. Native videos without media are marked with a null path.

Use the inventory to collect transcripts and extract tools with timestamped evidence. Publish only reviewed, non-confidential findings and approved code to NFAI.

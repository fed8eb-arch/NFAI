# Telegram export intake

Python 3.10+ with time-zone data is required. Export one chat from Telegram Desktop as JSON. For native Telegram videos, include the corresponding exported media directory. Store the inputs and outputs outside NFAI.

```bash
python3 projects/03-telegram-tooling/work/intake.py /absolute/path/result.json \
  --from 2026-09-17 --through 2026-11-17 --out /absolute/path/video-inventory.json
```

Dates are inclusive in America/New_York. The inventory contains canonical YouTube URLs, Telegram message IDs and timestamps, and local attachment paths when those files are present. The inventory starts with the most recent post. Reposted YouTube links share a single entry ordered by their latest post, with all matching posts listed newest first. Native videos without media are marked with a null path.

Use the inventory to collect transcripts and extract tools with timestamped evidence. Publish only reviewed, non-confidential findings and approved code to NFAI.

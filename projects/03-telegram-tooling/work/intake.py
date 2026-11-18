"""Build a private video inventory from one Telegram Desktop JSON export."""
import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from zoneinfo import ZoneInfo

URL = re.compile(r"https?://[^\s<>\x22\x27]+")
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}")
VIDEO_EXTENSIONS = {".mp4", ".webm", ".mov", ".mkv", ".m4v"}
ET = ZoneInfo("America/New_York")


def links(message):
    for field in ("text", "text_entities"):
        raw = message.get(field, "")
        for entry in raw if isinstance(raw, list) else [raw]:
            if isinstance(entry, dict):
                yield from URL.findall(entry.get("text") or "")
                if entry.get("href"):
                    yield entry["href"]
            elif isinstance(entry, str):
                yield from URL.findall(entry)


def youtube_id(url):
    try:
        parsed = urlsplit(url.rstrip(".,;:!?)]}"))
        host = parsed.hostname
    except ValueError:
        return None
    parts = parsed.path.strip("/").split("/")
    if host == "youtu.be" and len(parts) == 1:
        value = parts[0]
    elif host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if parts == ["watch"]:
            value = parse_qs(parsed.query).get("v", [""])[0]
        elif len(parts) == 2 and parts[0] in {"shorts", "live", "embed"}:
            value = parts[1]
        else:
            return None
    else:
        return None
    return value if VIDEO_ID.fullmatch(value) else None


def reviewed_video_ids(directory):
    if not directory.is_dir():
        raise ValueError(f"Reviewed results directory does not exist: {directory}")
    return {
        video_id
        for note in directory.glob("*.md")
        for link in URL.findall(note.read_text(encoding="utf-8-sig"))
        if (video_id := youtube_id(link))
    }


def timestamp(message):
    if message.get("date_unixtime"):
        return datetime.fromtimestamp(int(message["date_unixtime"]), ET)
    value = datetime.fromisoformat(message["date"])
    if value.tzinfo is None:
        raise ValueError("A message has no time zone or date_unixtime")
    return value.astimezone(ET)


def inventory(export, start, end, *, oldest_first=False):
    chat = json.loads(export.read_text(encoding="utf-8-sig"))
    if not isinstance(chat, dict) or not isinstance(chat.get("messages"), list):
        raise ValueError("Export a single chat as JSON. A full account export is outside scope.")
    found = {}
    for message in chat["messages"]:
        if message.get("type") != "message":
            continue
        when = timestamp(message)
        if not start <= when.date() <= end:
            continue
        source = {"message_id": message["id"], "posted_et": when.isoformat()}
        for video_id in {value for link in links(message) if (value := youtube_id(link))}:
            key = ("youtube", video_id)
            item = found.setdefault(key, {
                "kind": "youtube", "url": f"https://www.youtube.com/watch?v={video_id}",
                "posts": [],
            })
            item["posts"].append(source)
        media = message.get("file")
        if (message.get("media_type") in {"video_file", "video_message"}
                or str(message.get("mime_type", "")).startswith("video/")
                or (isinstance(media, str) and Path(media).suffix.lower() in VIDEO_EXTENSIONS)):
            candidate = (export.parent / media).resolve() if isinstance(media, str) else None
            available = candidate and candidate.is_relative_to(export.parent) and candidate.is_file()
            found["attachment", str(message["id"])] = {
                "kind": "attachment", "media": str(candidate.relative_to(export.parent)) if available else None,
                "posts": [source],
            }
    items = [found[key] for key in sorted(found)]
    newest_first = not oldest_first
    for item in items:
        item["posts"].sort(key=post_time, reverse=newest_first)
    return sorted(items, key=lambda item: post_time(item["posts"][0]), reverse=newest_first)


def post_time(post):
    return datetime.fromisoformat(post["posted_et"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path)
    parser.add_argument("--from", dest="start", type=date.fromisoformat, required=True)
    parser.add_argument("--through", dest="end", type=date.fromisoformat, required=True)
    parser.add_argument("--oldest-first", action="store_true",
                        help="Order videos by their earliest post in the selected date range")
    parser.add_argument("--exclude-reviewed", type=Path, metavar="RESULTS_DIR",
                        help="Skip YouTube IDs already linked by Markdown notes in RESULTS_DIR")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.start > args.end:
        parser.error("--from must be on or before --through")
    try:
        items = inventory(args.export.resolve(), args.start, args.end, oldest_first=args.oldest_first)
        if args.exclude_reviewed:
            reviewed = reviewed_video_ids(args.exclude_reviewed)
            items = [item for item in items if item["kind"] != "youtube" or youtube_id(item["url"]) not in reviewed]
        with args.out.open("x", encoding="utf-8") as stream:
            json.dump(items, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except (OSError, KeyError, TypeError, ValueError) as exc:
        parser.exit(1, f"Intake failed: {exc}\n")
    print(f"{len(items)} video entries")


if __name__ == "__main__":
    main()

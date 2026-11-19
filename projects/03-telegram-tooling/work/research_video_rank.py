#!/usr/bin/env python3
"""Rank a supplied CSV of publicly observed videos by views."""
import argparse
import csv
import json
import sys
from datetime import date
from urllib.parse import urlparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', help='UTF-8 CSV with title, url, views, published, observed columns')
    args = parser.parse_args()
    try:
        with open(args.csv_file, encoding='utf-8-sig', newline='') as source:
            reader = csv.DictReader(source)
            required = {'title', 'url', 'views', 'published', 'observed'}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                raise ValueError('missing required columns')
            rows = []
            seen = set()
            for number, row in enumerate(reader, 2):
                title, url = row['title'].strip(), row['url'].strip()
                host = urlparse(url).hostname
                if not title or host not in {'youtube.com', 'www.youtube.com', 'youtu.be'}:
                    raise ValueError(f'row {number}: invalid title or YouTube URL')
                views = int(row['views'])
                published = date.fromisoformat(row['published'])
                observed = date.fromisoformat(row['observed'])
                if views < 0 or published > observed or url in seen:
                    raise ValueError(f'row {number}: invalid count, date or duplicate URL')
                seen.add(url)
                rows.append({'title': title, 'url': url, 'views': views,
                             'published': published.isoformat(), 'observed': observed.isoformat()})
        if not rows:
            raise ValueError('no video rows')
        print(json.dumps(sorted(rows, key=lambda row: row['views'], reverse=True), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, csv.Error) as error:
        print(f'error: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

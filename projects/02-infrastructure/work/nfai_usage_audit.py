import argparse
import collections
import datetime as dt
import json
from pathlib import Path

FIELDS = ('input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens', 'total_tokens')


def audit(root, days=2, max_files=40):
    cutoff = dt.datetime.now().timestamp() - days * 86400
    files = sorted((p for p in root.glob('sessions/**/*.jsonl') if p.is_file() and p.stat().st_mtime >= cutoff), key=lambda p: p.stat().st_mtime, reverse=True)
    result = {'eligible_files': len(files), 'files_scanned': 0, 'oversized_files': 0, 'malformed_lines': 0, 'sessions': []}
    for p in files[:max_files]:
        if p.stat().st_size > 128 * 1024 * 1024:
            result['oversized_files'] += 1
            continue
        row = {'session': len(result['sessions'])+1, 'file_bytes': p.stat().st_size, 'token_events': 0, 'usage_samples': 0, 'max_context_window': None, 'first_total': None, 'last_total': None, 'observed_usage_delta': dict.fromkeys(FIELDS, 0), 'counter_resets': 0, 'tool_output_count': 0, 'tool_output_chars': 0, 'largest_tool_output_chars': 0, 'compaction_markers': 0}
        prev = None
        try:
            with p.open(encoding='utf-8') as f:
                for line in f:
                    try:
                        e = json.loads(line)
                        if not isinstance(e, dict):
                            raise ValueError()
                    except (ValueError, UnicodeError):
                        result['malformed_lines'] += 1
                        continue
                    q = e.get('payload')
                    if not isinstance(q, dict):
                        continue
                    typ = q.get('type')
                    if typ == 'token_count':
                        row['token_events'] += 1
                        info = q.get('info')
                        if not isinstance(info, dict):
                            continue
                        w = info.get('model_context_window')
                        if type(w) is int and w > 0:
                            row['max_context_window'] = max(w, row['max_context_window'] or 0)
                        u = info.get('total_token_usage')
                        if not isinstance(u, dict) or any(type(u.get(k)) is not int or u[k] < 0 for k in FIELDS):
                            continue
                        cur = {k: u[k] for k in FIELDS}
                        row['usage_samples'] += 1
                        if prev is None:
                            row['first_total'] = cur
                        elif any(cur[k] < prev[k] for k in FIELDS):
                            row['counter_resets'] += 1
                        else:
                            for k in FIELDS:
                                row['observed_usage_delta'][k] += cur[k] - prev[k]
                        prev = cur
                        row['last_total'] = cur
                    if typ in ('function_call_output', 'custom_tool_call_output'):
                        out = q.get('output')
                        if isinstance(out, str):
                            n = len(out)
                            row['tool_output_count'] += 1
                            row['tool_output_chars'] += n
                            row['largest_tool_output_chars'] = max(n, row['largest_tool_output_chars'])
                    if e.get('type') == 'compacted' or typ in ('context_compacted', 'compacted'):
                        row['compaction_markers'] += 1
        except (OSError, UnicodeError):
            row['read_incomplete'] = True
        result['files_scanned'] += 1
        result['sessions'].append(row)
    return result


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=Path.home()/'.codex')
    ap.add_argument('--days', type=int, default=2)
    ap.add_argument('--max-files', type=int, default=40)
    args = ap.parse_args()
    if not (1 <= args.days <= 30 and 1 <= args.max_files <= 100):
        ap.error('invalid bounds')
    print(json.dumps(audit(args.root, args.days, args.max_files), indent=2))

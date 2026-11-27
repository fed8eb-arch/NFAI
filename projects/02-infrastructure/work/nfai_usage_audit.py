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
        row['diagnostics_v2'] = d = {
            'first_event_utc': None, 'last_event_utc': None,
            'events_in_window': 0, 'unparseable_timestamps': 0,
            'usage_counter_changes': 0, 'repeated_usage_samples': 0,
            'last_request_input_max': None, 'last_request_input_over_200k_samples': 0,
            'last_request_input_samples': 0,
            'compacted_records': 0, 'context_compacted_events': 0,
            'other_compaction_markers': 0,
            'turn_context_records': 0, 'model_labels': [], 'effort_labels': [],
            'speed_labels': [], 'rate_limit_samples': 0,
            'primary_used_percent_min_max': None, 'secondary_used_percent_min_max': None,
            'exec_end_output_chars': 0, 'exec_end_records': 0,
        }
        prev_window = None
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
                    # Numeric-only diagnostics; original lifetime counter summary retained.
                    ts = e.get('timestamp')
                    event_time = None
                    if isinstance(ts, str):
                        try:
                            event_time = dt.datetime.fromisoformat(ts.replace('Z', '+00:00'))
                            if event_time.tzinfo is None:
                                event_time = None
                        except ValueError:
                            pass
                    if event_time is None:
                        d['unparseable_timestamps'] += 1
                    elif event_time.timestamp() >= cutoff:
                        stamp = event_time.astimezone(dt.timezone.utc).isoformat()
                        d['events_in_window'] += 1
                        if d['first_event_utc'] is None or stamp < d['first_event_utc']:
                            d['first_event_utc'] = stamp
                        if d['last_event_utc'] is None or stamp > d['last_event_utc']:
                            d['last_event_utc'] = stamp
                        if e.get('type') == 'compacted':
                            d['compacted_records'] += 1
                        elif typ == 'context_compacted':
                            d['context_compacted_events'] += 1
                        elif typ == 'compacted':
                            d['other_compaction_markers'] += 1
                        if e.get('type') == 'turn_context':
                            d['turn_context_records'] += 1
                            for key, dest, allowed in (
                                ('model', 'model_labels', None),
                                ('effort', 'effort_labels', {'minimal','low','medium','high','xhigh','none'}),
                                ('service_tier', 'speed_labels', {'default','standard','auto','fast','priority','flex'}),
                            ):
                                value = q.get(key)
                                if key == 'model':
                                    import re
                                    valid = isinstance(value, str) and re.fullmatch(r'(?:gpt|codex|astra|sol)[a-zA-Z0-9._-]{0,64}', value)
                                else:
                                    valid = isinstance(value, str) and value in allowed
                                if valid and value not in d[dest] and len(d[dest]) < 12:
                                    d[dest].append(value)
                        if typ == 'exec_command_end':
                            d['exec_end_records'] += 1
                            output = q.get('aggregated_output')
                            if isinstance(output, str):
                                d['exec_end_output_chars'] += len(output)
                        if typ == 'token_count':
                            info2 = q.get('info')
                            if isinstance(info2, dict):
                                total = info2.get('total_token_usage')
                                if isinstance(total, dict) and all(type(total.get(k)) is int and total[k] >= 0 for k in FIELDS):
                                    cur_window = tuple(total[k] for k in FIELDS)
                                    if prev_window is not None:
                                        if cur_window == prev_window:
                                            d['repeated_usage_samples'] += 1
                                        else:
                                            d['usage_counter_changes'] += 1
                                    prev_window = cur_window
                                last = info2.get('last_token_usage')
                                if isinstance(last, dict):
                                    n = last.get('input_tokens')
                                    if type(n) is int and n >= 0:
                                        d['last_request_input_samples'] += 1
                                        d['last_request_input_max'] = max(n, d['last_request_input_max'] or 0)
                                        if n > 200000:
                                            d['last_request_input_over_200k_samples'] += 1
                            limits = q.get('rate_limits')
                            if isinstance(limits, dict):
                                d['rate_limit_samples'] += 1
                                for bucket in ('primary', 'secondary'):
                                    limit = limits.get(bucket)
                                    n = limit.get('used_percent') if isinstance(limit, dict) else None
                                    if type(n) in (int, float) and 0 <= n <= 100:
                                        key = bucket + '_used_percent_min_max'
                                        old = d[key]
                                        d[key] = [min(old[0], n), max(old[1], n)] if old else [n, n]
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

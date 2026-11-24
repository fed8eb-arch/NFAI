"""Verify a standalone existing SQLite backup using isolated local copies.
No database contents, file paths, hashes, credentials or SQL appear in output.
Never open a live database in place; reject SQLite journal/WAL sidecars.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import tempfile

LIMIT = 2 * 1024**3
HEADER = b'SQLite format 3\x00'

class CheckError(Exception):
    pass


def file_digest(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').digest()


def ensure_standalone(path):
    if not path.is_file() or path.is_symlink():
        raise CheckError('not a regular backup file')
    if not 100 <= path.stat().st_size <= LIMIT:
        raise CheckError('backup size outside supported range')
    if any(Path(str(path) + suffix).exists() for suffix in ('-wal', '-shm', '-journal')):
        raise CheckError('sidecar present; use an exported standalone backup')
    with path.open('rb') as f:
        if f.read(16) != HEADER:
            raise CheckError('not a standalone SQLite database')


def fingerprint(conn):
    conn.execute('PRAGMA query_only=ON')
    conn.execute('PRAGMA trusted_schema=OFF')
    if conn.execute('PRAGMA integrity_check').fetchall() != [('ok',)]:
        raise CheckError('SQLite integrity check failed')
    # The logical SQL stream is hashed in memory, never printed or written to a report.
    h = hashlib.sha256()
    for line in conn.iterdump():
        h.update(line.encode('utf-8'))
        h.update(b'\n')
    versions = tuple(conn.execute('PRAGMA ' + name).fetchone()[0]
                     for name in ('user_version', 'application_id'))
    return h.digest(), versions


def verify(source):
    source = Path(source).absolute()
    ensure_standalone(source)
    original = file_digest(source)
    with tempfile.TemporaryDirectory(prefix='nfai-sqlite-restore-') as tmp:
        work = Path(tmp) / 'source.sqlite'
        restored = Path(tmp) / 'restored.sqlite'
        shutil.copyfile(source, work)
        ensure_standalone(source)
        if file_digest(work) != original or file_digest(source) != original:
            raise CheckError('backup changed during snapshot')
        src = sqlite3.connect(work.as_uri() + '?mode=ro', uri=True)
        try:
            before = fingerprint(src)
            dst = sqlite3.connect(restored)
            try:
                src.backup(dst)
            finally:
                dst.close()
        finally:
            src.close()
        check = sqlite3.connect(restored.as_uri() + '?mode=ro', uri=True)
        try:
            if fingerprint(check) != before:
                raise CheckError('restored logical content differs')
        finally:
            check.close()
        ensure_standalone(source)
        if file_digest(source) != original:
            raise CheckError('original backup changed during check')
    return {'status': 'PASS', 'source_integrity': True, 'restore_integrity': True,
            'logical_content_match': True, 'original_unchanged': True,
            'temporary_copies_removed': True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('backup', help='Explicit existing standalone SQLite backup, never the live DB')
    args = p.parse_args()
    try:
        result = verify(args.backup)
    except CheckError as exc:
        print(json.dumps({'status': 'BLOCKED', 'reason': str(exc)}))
        return 1
    except (OSError, sqlite3.Error, UnicodeError, ValueError):
        print(json.dumps({'status': 'BLOCKED', 'reason': 'local I/O or SQLite verification failed'}))
        return 1
    print(json.dumps(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

import contextlib
import io
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch
from sqlite_restore_check import CheckError, file_digest, main, verify


class RestoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / 'backup.sqlite'
        db = sqlite3.connect(self.path)
        try:
            db.executescript('''CREATE TABLE sample(id INTEGER PRIMARY KEY, text TEXT, data BLOB);
              INSERT INTO sample VALUES(1,'synthetic-marker',X'00FF');
              CREATE INDEX sample_text ON sample(text);
              PRAGMA user_version=7; PRAGMA application_id=42;''')
            db.commit()
        finally:
            db.close()

    def test_restore_unchanged(self):
        old = file_digest(self.path)
        self.assertEqual(verify(self.path)['status'], 'PASS')
        self.assertEqual(file_digest(self.path), old)
        self.assertEqual(list(Path(self.tmp.name).iterdir()), [self.path])

    def test_invalid_header(self):
        self.path.write_bytes(b'x' * 200)
        with self.assertRaises(CheckError): verify(self.path)

    def test_sidecars(self):
        for suffix in ('-wal', '-shm', '-journal'):
            sidecar = Path(str(self.path) + suffix)
            sidecar.touch()
            with self.assertRaises(CheckError): verify(self.path)
            sidecar.unlink()

    def test_missing(self):
        with self.assertRaises(CheckError): verify(self.path.with_name('missing.sqlite'))

    def test_corrupt_sqlite(self):
        original = self.path.read_bytes()
        self.path.write_bytes(original[:100] + b'\0' * (len(original) - 100))
        with self.assertRaises((CheckError, sqlite3.Error)): verify(self.path)

    def test_content_mismatch(self):
        with patch('sqlite_restore_check.fingerprint', side_effect=[(b'a', (7,42)), (b'b', (7,42))]):
            with self.assertRaisesRegex(CheckError, 'logical content differs'): verify(self.path)

    def test_cli_redaction(self):
        out = io.StringIO()
        with patch.object(sys, 'argv', ['check', str(self.path)]), contextlib.redirect_stdout(out):
            self.assertEqual(main(), 0)
        self.assertNotIn('synthetic-marker', out.getvalue())
        self.assertNotIn(str(self.path), out.getvalue())

    def test_cli_error_redaction(self):
        out = io.StringIO()
        with patch.object(sys, 'argv', ['check', str(self.path)]), patch('sqlite_restore_check.verify', side_effect=sqlite3.Error('private-marker')), contextlib.redirect_stdout(out):
            self.assertEqual(main(), 1)
        self.assertNotIn('private-marker', out.getvalue())


if __name__ == '__main__': unittest.main()

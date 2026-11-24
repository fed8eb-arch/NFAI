import sqlite3
import tempfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
import unittest
from registry import connect, create, transition

class RegistryTest(unittest.TestCase):
    def setUp(self):
        self.db = connect(':memory:')
        create(self.db, 'T1', 'Example', 'worker')
    def tearDown(self): self.db.close()
    def test_complete_verified_flow(self):
        transition(self.db, 'T1', 'assigned', 'director', 'assigned')
        transition(self.db, 'T1', 'running', 'worker', 'started')
        transition(self.db, 'T1', 'review', 'worker', 'ready for review', 'artifact:1')
        transition(self.db, 'T1', 'accepted', 'reviewer', 'checked', 'check:1')
        self.assertEqual(self.db.execute('SELECT state,reviewer FROM tasks').fetchone(), ('accepted','reviewer'))
        self.assertEqual(self.db.execute('SELECT count(*) FROM events').fetchone()[0], 5)
    def test_cannot_skip_states_or_self_accept(self):
        with self.assertRaises(ValueError): transition(self.db,'T1','accepted','worker','done','x')
        transition(self.db,'T1','assigned','director','assigned')
        transition(self.db,'T1','running','worker','started')
        with self.assertRaises(ValueError): transition(self.db,'T1','review','worker','done')
        transition(self.db,'T1','review','worker','done','artifact')
        with self.assertRaises(ValueError): transition(self.db,'T1','accepted',' WORKER ','done','proof')
        self.assertEqual(self.db.execute('SELECT state FROM tasks').fetchone()[0], 'review')
    def test_duplicate_is_atomic(self):
        with self.assertRaises(sqlite3.IntegrityError): create(self.db,'T1','duplicate','worker')
        self.assertEqual(self.db.execute('SELECT count(*) FROM events').fetchone()[0], 1)

    def test_owner_only_claim_and_submit(self):
        with self.assertRaises(ValueError): transition(self.db,'T1','assigned','worker','self assign')
        transition(self.db,'T1','assigned','director','approved')
        with self.assertRaises(ValueError): transition(self.db,'T1','running','other','claim')
        transition(self.db,'T1','running','worker','claim')
        with self.assertRaises(ValueError): transition(self.db,'T1','running','worker','duplicate')
        with self.assertRaises(ValueError): transition(self.db,'T1','review','other','submit','proof')
        self.assertEqual(self.db.execute('SELECT state,revision FROM tasks').fetchone(), ('running',2))
        self.assertEqual(self.db.execute('SELECT count(*) FROM events').fetchone()[0],3)

    def test_recovery_requires_reassignment(self):
        transition(self.db,'T1','assigned','director','approved')
        transition(self.db,'T1','running','worker','claim')
        transition(self.db,'T1','blocked','worker','interrupted')
        with self.assertRaises(ValueError): transition(self.db,'T1','running','worker','retry')
        transition(self.db,'T1','assigned','director','side effects reconciled')
        transition(self.db,'T1','running','worker','retry approved')
        transition(self.db,'T1','review','worker','submit','proof')
        with self.assertRaises(ValueError): transition(self.db,'T1','running','worker','repeat')
        transition(self.db,'T1','accepted','reviewer','checked','review:1')
        with self.assertRaises(ValueError): transition(self.db,'T1','assigned','director','repeat accepted')
        self.assertEqual(self.db.execute('SELECT state FROM tasks').fetchone()[0],'accepted')

    def test_concurrent_claim_one_winner(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = str(Path(tmp) / 'registry.sqlite')
            db = connect(path)
            create(db,'T2','Concurrent','worker')
            transition(db,'T2','assigned','director','approved')
            db.close()
            barrier = Barrier(2)
            def claim():
                conn = connect(path)
                try:
                    barrier.wait(timeout=5)
                    transition(conn,'T2','running','worker','claim')
                    return True
                except ValueError:
                    return False
                finally:
                    conn.close()
            with ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(lambda _: claim(), range(2)))
            self.assertEqual(sorted(results),[False,True])
            db = connect(path)
            try:
                self.assertEqual(db.execute('SELECT state,revision FROM tasks').fetchone(),('running',2))
                self.assertEqual(db.execute("SELECT count(*) FROM events WHERE state='running'").fetchone()[0],1)
            finally:
                db.close()

if __name__ == '__main__': unittest.main()


import sqlite3
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

if __name__ == '__main__': unittest.main()


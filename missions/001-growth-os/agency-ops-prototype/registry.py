"""Offline task registry. No model calls, network access, or automatic execution."""
import argparse
import json
import sqlite3
from datetime import datetime, timezone

TRANSITIONS = {
    'proposed': {'assigned', 'blocked'},
    'assigned': {'running', 'blocked'},
    'running': {'blocked', 'review'},
    'blocked': {'assigned', 'running'},
    'review': {'running', 'blocked', 'accepted'},
    'accepted': set(),
}

def connect(path):
    db = sqlite3.connect(path)
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript('''
      CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY, title TEXT NOT NULL, owner TEXT NOT NULL,
        state TEXT NOT NULL, evidence TEXT, reviewer TEXT, revision INTEGER NOT NULL DEFAULT 0
      );
      CREATE TABLE IF NOT EXISTS events (
        seq INTEGER PRIMARY KEY, task_id TEXT NOT NULL REFERENCES tasks(id),
        at TEXT NOT NULL, actor TEXT NOT NULL, previous TEXT, state TEXT NOT NULL,
        note TEXT NOT NULL, evidence TEXT
      );
    ''')
    return db

def create(db, task_id, title, owner):
    if not all(x and x.strip() for x in (task_id, title, owner)):
        raise ValueError('id, title and owner are required')
    with db:
        db.execute('INSERT INTO tasks (id,title,owner,state) VALUES (?,?,?,?)',
                   (task_id, title, owner, 'proposed'))
        db.execute('INSERT INTO events(task_id,at,actor,previous,state,note) VALUES(?,?,?,?,?,?)',
                   (task_id, datetime.now(timezone.utc).isoformat(), owner, None, 'proposed', 'created'))

def transition(db, task_id, state, actor, note, evidence=None):
    if not actor.strip() or not note.strip():
        raise ValueError('actor and note are required')
    with db:
        row = db.execute('SELECT owner,state,revision FROM tasks WHERE id=?', (task_id,)).fetchone()
        if row is None:
            raise ValueError('task not found')
        owner, old, revision = row
        if state not in TRANSITIONS.get(old, set()):
            raise ValueError('invalid transition')
        if state in {'review','accepted'} and not (evidence and evidence.strip()):
            raise ValueError('evidence is required for review and acceptance')
        if state == 'accepted' and actor.casefold().strip() == owner.casefold().strip():
            raise ValueError('reviewer must differ from owner')
        cursor = db.execute('UPDATE tasks SET state=?, evidence=?, reviewer=?, revision=revision+1 WHERE id=? AND revision=?',
                            (state, evidence, actor if state == 'accepted' else None, task_id, revision))
        if cursor.rowcount != 1:
            raise RuntimeError('concurrent modification')
        db.execute('INSERT INTO events(task_id,at,actor,previous,state,note,evidence) VALUES(?,?,?,?,?,?,?)',
                   (task_id, datetime.now(timezone.utc).isoformat(), actor, old, state, note, evidence))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--db', required=True, help='Path to private local SQLite database')
    sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('add'); a.add_argument('id'); a.add_argument('title'); a.add_argument('owner')
    t = sub.add_parser('move'); t.add_argument('id'); t.add_argument('state', choices=TRANSITIONS); t.add_argument('--actor', required=True); t.add_argument('--note', required=True); t.add_argument('--evidence')
    sub.add_parser('list')
    args = p.parse_args()
    with connect(args.db) as db:
        if args.command == 'add': create(db, args.id, args.title, args.owner)
        elif args.command == 'move': transition(db, args.id, args.state, args.actor, args.note, args.evidence)
        else:
            db.row_factory = sqlite3.Row
            print(json.dumps([dict(r) for r in db.execute('SELECT * FROM tasks ORDER BY id')], ensure_ascii=False, indent=2))

if __name__ == '__main__': main()


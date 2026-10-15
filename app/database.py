import sqlite3
from contextlib import contextmanager
from .config import DATABASE

SCHEMA = '''
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT, email TEXT);
CREATE TABLE IF NOT EXISTS devices (id INTEGER PRIMARY KEY, name TEXT, zone TEXT, owner_id INTEGER, state TEXT, firmware TEXT, token TEXT);
CREATE TABLE IF NOT EXISTS readings (id INTEGER PRIMARY KEY, device_id INTEGER, kind TEXT, value REAL, recorded_at TEXT);
CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, actor TEXT, event TEXT, detail TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS jobs (id INTEGER PRIMARY KEY, device_id INTEGER, action TEXT, status TEXT);
'''

def connect():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def db():
    conn = connect()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def initialize():
    with db() as conn:
        conn.executescript(SCHEMA)
        if conn.execute('SELECT COUNT(*) FROM users').fetchone()[0] == 0:
            conn.executemany('INSERT INTO users(username,password,role,email) VALUES(?,?,?,?)', [
                ('admin','admin123','admin','admin@example.local'),
                ('alice','welcome1','resident','alice@example.local'),
                ('bob','welcome2','resident','bob@example.local')])
        if conn.execute('SELECT COUNT(*) FROM devices').fetchone()[0] == 0:
            conn.executemany('INSERT INTO devices(name,zone,owner_id,state,firmware,token) VALUES(?,?,?,?,?,?)', [
                ('Lobby Thermostat','lobby',2,'on','1.0.1','token-lobby'),
                ('Garage Door','garage',3,'closed','1.2.0','token-garage'),
                ('Air Quality Sensor','lab',2,'on','0.9.8','token-air')])

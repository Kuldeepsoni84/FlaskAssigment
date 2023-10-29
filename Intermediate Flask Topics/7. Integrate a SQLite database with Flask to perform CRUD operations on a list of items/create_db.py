import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

conn.commit()
conn.close()

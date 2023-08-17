import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        description TEXT,
        done INTEGER
    )
''')

conn.commit()

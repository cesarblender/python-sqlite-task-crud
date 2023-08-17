import sqlite3

# Connection to the ./tasks.db database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create the "tasks" table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        description TEXT,
        done INTEGER
    )
''')

# Save changes
conn.commit()

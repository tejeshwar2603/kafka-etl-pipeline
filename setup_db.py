import sqlite3

conn = sqlite3.connect('messages.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
''')
cursor.execute("INSERT INTO messages (message, timestamp) VALUES ('Test message 1', '2024-10-02 15:30:00')")
cursor.execute("INSERT INTO messages (message, timestamp) VALUES ('Test message 2', '2024-10-03 16:00:00')")
conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect('supermarket.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        customerid INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR,
        age INT,
        place VARCHAR,
        salary REAL
    )
''')

conn.commit()
conn.close()

print("Database 'supermarket' and table 'customer' created successfully.")

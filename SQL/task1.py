import sqlite3

conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()

sample_data = [
    ("John Doe", 30, "New York", 50000),
    ("Jane Smith", 25, "Los Angeles", 60000),
    ("Michael Johnson", 35, "Chicago", 70000),
    ("Emily Brown", 28, "Houston", 55000),
    ("William Wilson", 40, "San Francisco", 80000),
    ("Amanda Lee", 32, "Boston", 65000),
    ("David Martinez", 45, "Miami", 75000),
    ("Jennifer Taylor", 27, "Seattle", 58000),
    ("Daniel Anderson", 33, "Dallas", 67000),
    ("Jessica Thomas", 29, "Atlanta", 59000)
]

cursor.executemany('''
    INSERT INTO customer (name, age, place, salary)
    VALUES (?, ?, ?, ?)
''', sample_data)

conn.commit()
conn.close()

print("Sample data inserted successfully.")

import sqlite3

conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()
cursor.execute("SELECT name,age FROM customer WHERE place='Ahemedabad'")

rows = cursor.fetchall()

print("Name\t\tAge")
print("-" * 60)

for row in rows:
    print(f"{row[0]}\t\t{row[1]}")
conn.close()

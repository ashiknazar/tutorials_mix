import sqlite3

conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM customer WHERE salary > ?", (70000,))

rows = cursor.fetchall()

print("CustomerID\tName\t\tAge\tPlace\t\tSalary")
print("-" * 60)

for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t{row[3]}\t\t{row[4]}")
conn.close()

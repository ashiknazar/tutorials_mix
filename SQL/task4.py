import sqlite3

conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM customer WHERE customerid = ?", (5,))

row = cursor.fetchone()

if row:
    print("Customer Details:")
    print("CustomerID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
    print("Place:", row[3])
    print("Salary:", row[4])
else:
    print("No customer found with ID 5")

conn.close()

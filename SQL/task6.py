import sqlite3

conn = sqlite3.connect('supermarket.db')
cursor = conn.cursor()
cursor.execute("UPDATE customer set place='Ahemedabad' where customerid=3")

conn.commit()


conn.close()

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

select_query = '''SELECT * FROM student_info'''

cursor.execute(select_query)
print(cursor.fetchall())




conn.commit()

#cursor.close()
conn.close()



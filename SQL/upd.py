import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

select_query = '''UPDATE student_info set username="das" where id=7'''

cursor.execute(select_query)





conn.commit()


conn.close()

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

alter_table_query = '''
ALTER TABLE users RENAME TO student_info
'''

cursor.execute(alter_table_query)
conn.commit()

cursor.close()
conn.close()

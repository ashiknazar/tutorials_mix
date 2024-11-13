import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

select_query = '''INSERT INTO student_info (username, email, age)
    VALUES ("adarsh","ada@gm.com",18)'''

cursor.execute(select_query)





conn.commit()


conn.close()

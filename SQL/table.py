import sqlite3

conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define a SQL command to create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
);
'''

# Execute the SQL command to create the table
cursor.execute(create_table_query)

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

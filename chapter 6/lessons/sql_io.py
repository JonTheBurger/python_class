# Lesson 8
# SQLite is a single file database. It allows us to store data with better guarantees (Atomicity, Consistency,
# Isolation, Durability)
import sqlite3
connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)")
# Will add duplicates upon multiple runs.
cursor.execute("INSERT INTO people VALUES ('alice', 22), ('bob', 35), ('charley', 27)")
connection.commit()

name = input('Who do you want to find? ')
# We use ? to fill in parameters to protect against SQL injection (search 'Bobby Tables')
# SQLite expects tuples, but we only have 1 search condition
cursor.execute('SELECT * FROM people WHERE name=?', (name,))
print(cursor.fetchone())

# SQL is a whole topic in and of itself. If you ever need to work with it, check out the SQLite GUI!

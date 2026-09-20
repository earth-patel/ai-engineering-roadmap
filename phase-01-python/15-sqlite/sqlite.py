import sqlite3

connection = sqlite3.connect('app.db')

print("Database connected")

# A cursor is an object that allows python to execute SQL commands and queries on the database
cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS users")  # Drop the table if it already exists

cursor.execute("""
  CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
  )
""")

# cursor.execute - prepare and execute an SQL command
# connection.commit - commit the changes to the database
connection.commit()

# Insert data into the users table
cursor.execute("""
  INSERT INTO users (name, email)
  VALUES (?, ?)
""", ("John Doe", "johndoe@example.com"))

connection.commit()

# Insert multiple records into the users table
users = [
  ("Earth", "earth@example.com"),
  ("Mars", "mars@example.com"),
]
cursor.executemany(
  "INSERT INTO users (name, email) VALUES (?, ?)",
  users
)
connection.commit()

# Read data with SELECT
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()  # fetchall() returns all rows of a query result
print(users)
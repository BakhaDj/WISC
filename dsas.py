import sqlite3


# with sqlite3.connect('datbs.db') as connection:
connection = sqlite3.connect('dbs')
cursor = connection.cursor()

# stmt = '''

# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT NOT NULL,
# will_come TEXT NOT NULL
# )
# '''

# stmt = 'insert into users (username) VALUES ("lox")'
stmt = 'SELECT * FROM users'
cursor.execute(stmt)

data = cursor.fetchall()
print(data)
connection.commit()
connection.close()

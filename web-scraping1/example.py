import sqlite3


# Establish a connection and a cursor
connection = sqlite3.connect("data")
cursor = connection.cursor()


# Query Data
#cursor.execute("SELECT * FROM events WHERE band='Lions'")
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)


# Query certain a columns
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)


# Insert new rows
# new_rows = [('Cats', 'Cat City', '2088.10.17'),
#              ('Hens', 'Hen City', '2088.10.17')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
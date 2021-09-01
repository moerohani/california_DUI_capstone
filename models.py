import sqlite3

connection = sqlite3.connect("switrs.sqlite")

cursor = connection.cursor()

for row in cursor.execute("SELECT * FROM collisions WHERE 'latittude' IS NOT NULL AND 'longtitude' IS NOT NULL LIMIT 5"):
    print(row)
    
connection.close()
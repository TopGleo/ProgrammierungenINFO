import sqlite3 
 
connection = sqlite3.connect('database.db') 
cur = connection.cursor() 
 
cur.execute("INSERT INTO einkaufsliste (name, anzahl) VALUES ('Bananen', '6');") 
cur.execute("SELECT name, anzahl FROM einkaufsliste;")

rows = cur.fetchall()

connection.commit() 
connection.close() 

for row in rows:  
    print(row) 

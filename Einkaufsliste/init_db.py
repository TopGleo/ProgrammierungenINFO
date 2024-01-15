import sqlite3 
 
connection = sqlite3.connect('database.db') 
with open('schema.sql') as file: 
    connection.executescript(file.read()) 
 

cur = connection.cursor() 

 
cur.execute("INSERT INTO einkaufsliste (name, anzahl, gekauft) VALUES ('Bananen', '6', 'ja');") 

rows = cur.fetchall()

for row in rows:  

   print(row) 

connection.commit() 
connection.close() 
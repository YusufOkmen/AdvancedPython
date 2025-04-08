import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()# Cursor func can be thought as mouse. 

cursor.execute

# cursor.execute("CREATE DATABASE exampledb")
# cursor.execute("SHOW DATABASES")

cursor.execute("CREATE TABLE categaries (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")

cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)


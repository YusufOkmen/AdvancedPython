import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()# Cursor func can be thought as mouse.

query = "DELETE FROM products WHERE name = %s LIMIT 1"
value = ("Excalibur G870",)

cursor.execute(query, value)
db.commit()
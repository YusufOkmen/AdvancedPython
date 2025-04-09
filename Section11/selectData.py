import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()# Cursor func can be thought as mouse. 

# sql = "SELECT * FROM products"
sql = "SELECT id, name FROM products"

cursor.execute(sql),

# products = cursor.fetchall()
product = cursor.fetchone()

# for p in products:
#     print(p)

print(product)
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products WHERE id=5 "

# sql = "SELECT * FROM products WHERE name='SamsungS25'"

# sql = "SELECT * FROM products WHERE name='Excalibur G870'"

# sql = "SELECT * FROM products WHERE id>5 AND price>50000"

# sql = "SELECT * FROM products WHERE id=4 OR id=6"

# sql = "SELECT * FROM products WHERE name LIKE '%Excalibur%'" # Give me the porducts that includes Excalibur in its name.

# sql = "SELECT * FROM products WHERE name LIKE 'Excalibur%'" # Give me the products that its name start with Excalibur

# sql = "SELECT * FROM products WHERE name LIKE '%Excalibur'" # Give me the products that its name ends with Excalibur

# sql = "SELECT * FROM products WHERE name LIKE 'Excalibur%' OR description LIKE '%gaming%'"

id = 1 
sql = "SELECT * FROM products WHERE id=%s"
params = (id,)

# cursor.execute(sql)
cursor.execute(sql, params)

# result = cursor.fetchone()
result = cursor.fetchall()

print(result)
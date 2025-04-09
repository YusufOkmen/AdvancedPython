import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products"# Number of the products.

# sql = "SELECT AVG(price) FROM products"# Gives the avarega price of the products.

# sql = "SELECT SUM(price) FROM products"# Gives the total price of all products.

sql = "SELECT MIN(price) FROM products"

sql = "SELECT MAX(price) FROM products"

sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)"# Bring me the name of the product with the heighest price.

sql = "SELECT name, price FROM products ORDER BY price DESC"# Organize the products from heighest price to lowest price. Then bring me the name and price of products.

cursor.execute(sql)

result = cursor.fetchall()

print(result)

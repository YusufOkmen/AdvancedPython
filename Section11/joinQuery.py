import mysql.connector

db = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name, categoriesId FROM products"

# sql = "SELECT name FROM categories"

# sql = "SELECT name, price, catName FROM products INNER JOIN categories ON products.categoriesId = categories.id"

# sql = "SELECT name, price, catName FROM products INNER JOIN categories ON products.categoriesId = categories.id WHERE categories.id=1"

sql = "SELECT name, price, catName FROM products INNER JOIN categories ON products.categoriesId = categories.id WHERE categories.catName = 'Phone'"

cursor.execute(sql)

result = cursor.fetchall()

for p in result:
    print(p)
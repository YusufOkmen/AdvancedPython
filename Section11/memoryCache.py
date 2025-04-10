import mysql.connector
from cachetools import cached, TTLCache
import time

db = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "133113",
    database = "shopdb"
)

@cached(cache=TTLCache(maxsize=32, ttl=60 ))
def getProducts():  
    cursor = db.cursor()

    sql = "SELECT name, price, catName FROM products INNER JOIN categories ON products.categoriesId = categories.id WHERE categories.catName = 'Phone'"

    cursor.execute(sql)

    print("From SQL")
    return cursor.fetchall()

s = time.time()
print(getProducts())
print("Geçen zaman: ", time.time() - s)

s = time.time()
print(getProducts())
print("Geçen zaman: ", time.time() - s)

s = time.time()
print(getProducts())
print("Geçen zaman: ", time.time() - s)



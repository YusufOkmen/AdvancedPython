import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "UPDATE products SET name='Iphone16-updated' WHERE id=1"

# sql = "SELECT * FROM products"



# result = cursor.fetchall()

# for p in result:
#     print(p)

def updateProduct(id, name, price):
    sql = "UPDATE products SET name=%s, price=%s WHERE id=%s"
    params = (name, price, id)

    cursor.execute(sql, params)

    try:
        db.commit()# Saves the change for database.
        print("changes saved for the dabase.")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        cursor.close()
        db.close()
        print("changes saved for the dabase.")

updateProduct(5, 'Monster i5', 150000)
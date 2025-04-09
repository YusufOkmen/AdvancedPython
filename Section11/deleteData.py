import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()

def deleteProductById(id):
    # sql = "DELETE FROM products WHERE id=1"
    sql = "DELETE FROM products WHERE id=%s"
    params = (id,)

    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} product is deleted.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

deleteProductById(8)
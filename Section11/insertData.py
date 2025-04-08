import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "133113",
    database = "shopdb"
)

cursor = db.cursor()# Cursor func can be thought as mouse.

# value = ("Excalibur G870", 55000, "This is a real gaming pc.")
# cursor.execute(sql, value)


sql = "INSERT INTO products (name, price, description) VALUES (%s,%s,%s)"

values = [
    ("HP VICTUS A1", 35000, "This is a real gaming pc."),
    ("HP VICTUS A2", 55000, "It is okay for its price."),
    ("HP VICTUR A4", 70000, "Spend too much, enjoy too much.")
]


cursor.executemany(sql, values)

try: 
    db.commit()
    print(cursor.rowcount, " kayıt edildi")
    print(f"Son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("hata: ", err)
finally:
    cursor.close()
    db.close()
    print("Bağlantı kapatıldı.")
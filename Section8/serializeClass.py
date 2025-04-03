import json

products = {}
class Product:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

# SERIALIZING
#         products[self.id] = self.toDict()

#     def toDict(self):
#         return self.__dict__
        

#     def sentToJson(self):
#         with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\productsData.json", "w") as file:
#             json.dump(products, file)



# p1 = Product(1, "Excalibur g800", 20000)
# p2 = Product(2, "Samsung S25", 20000)

# p1.sentToJson()


# with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\productsData.json") as file:
#     data = json.load(file)

# print(data["1"])


# DESIRIALIZE

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\productsData.json") as file:
    data = json.load(file)

    storedProducts = []
    for key, value in data.items():
        storedProducts.append(Product(key, value["title"], value["price"]))

for p in storedProducts:
    print(p.price)

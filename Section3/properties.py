# The reason why we use properties is because we want to set a value to our attributes correctly. For example: Price can not be smaller than 0

class Product:
    def __init__(self, name, price):
        self.name = name
        # Price can't be negative 
        if price >= 0:
            self._price = price 
        else:
            raise ValueError("Price can't be negative")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value 
        else:
            raise ValueError("Price can't be negative")


    # def setPrice(self, value):
    #     if value >= 0:
    #         self._price = value 
    #     else:
    #         raise ValueError("Price can't be negative")
        
    # def getPrice(self):
    #     return self._price

    
# Creating the Product object
p = Product("Iphone 16", 50000)

print(p.price)

p.price = 43000
print(p.price)

# print(p.name, p._price)
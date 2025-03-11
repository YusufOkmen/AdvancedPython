class CartItem:
    discountRate = 0.8
    itemCount = 0

    @classmethod
    def CountTheItem(cls):
        pass

    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity
        CartItem.itemCount += 1

    def calculateTotal(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = (self.price * CartItem.discountRate)


# Creating the items for shop cart
item1 = CartItem("Phone", 50000, 3)
item2 = CartItem("PlayStation 4", 70000, 1)
item3 = CartItem("Fridge", 120000, 2)


class ShoppingCart:

    @classmethod
    def getCupon(cls, input):
        if input == "code1":
            return -5000
        elif input == "code2":
            return -10000
        elif input == "code3":
            return -15000
        else:
            raise ValueError(f"Please enter a valid code")

    def __init__(self, itemList):
        self.itemList = itemList

    def addItem(self, item):
        self.itemList.append(item)

    def displayItems(self):
        nameList = [item.name for item in self.itemList]
        return nameList
    
    def calculateCartTotal(self):
        total = 0
        for item in self.itemList:
            total += item.calculateTotal()
        return total

    def removeItem(self, item):
        self.itemList.remove(item)

    def clearCart(self):
        self.itemList.clear()

    def applyCupon(self, input):
        cupon = ShoppingCart.getCupon(input)
        total = self.calculateCartTotal()
        final = total + cupon
        return final
        

# Creating the cart object
sc = ShoppingCart([item1, item2])

sc.addItem(item3)



# sc.removeItem(item2)
# sc.clearCart()  

print(sc.calculateCartTotal())

print(sc.applyCupon("code3"))
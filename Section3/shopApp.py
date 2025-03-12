
def main():
    # The Product Panel (UI)
    print(f"     -Products-      \n item1: {item1.name}: {item1.price}TL\n item2: {item2.name}: {item2.price}TL\n item3: {item3.name}: {item3.price}TL \n")

    # Adding products into the shopping cart
    control = True 
    border = 0
    productList = []

    while (True):
        order = input("Please choose an item: ")
        border += 1

        if (order == "item1"):
            productList.append(item1)
        elif(order == "item2"):
            productList.append(item2)
        elif(order == "item3"):
            productList.append(item3)
        else:
            break
        
        if (border == CartItem.itemCount):
            break

    sCart = ShoppingCart(productList)

    print("     -Cart-      \n 1- Add Item\n 2- Display Items\n 3- Calculate Total\n 4- Remove Item\n 5- Clear All Cart\n 6- Apply Coupon\n")

    while(True):
        query = int(input("Please select the process No. that you want to display (Type 7 for quit): "))
        
        if (query == 1):
            sCart.addItem()
        elif (query == 2):
            print(sCart.displayItems())
        elif (query == 3):
            print(sCart.calculateCartTotal())
        elif (query == 4):
            sCart.removeItem()
        elif (query == 5):
            sCart.clearCart()
        elif (query == 6):
            print(sCart.applyCupon())
        elif (query == 7):
            break
        else:
            raise ValueError("Please enter a valid number.")

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
item1 = CartItem("Phone", 50000, 1)
item2 = CartItem("PlayStation 4", 70000, 1)
item3 = CartItem("Fridge", 120000, 1)


class ShoppingCart:
    def __init__(self, itemList):
        self.itemList = itemList

    def addItem(self):
        userItem = input("Which item do you want to add: ")
        if (userItem == "item1"):
            self.itemList.append(item1)
        if (userItem == "item2"):
            self.itemList.append(item2)
        if (userItem == "item3"):
            self.itemList.append(item3)

    def displayItems(self):
        return [item.name for item in self.itemList] 
    
    def calculateCartTotal(self):
        return sum([item.calculateTotal() for item in self.itemList])

    def removeItem(self):
        itemInput = input("Please enter the item that you want to remove: ")
        if (itemInput == "item1"):
            self.itemList.remove(item1)
        if (itemInput == "item2"):
            self.itemList.remove(item2)
        if (itemInput == "item3"):
            self.itemList.remove(item3)

    def clearCart(self):
        self.itemList.clear()

    def applyCupon(self):
        total = self.calculateCartTotal()
        theInput = input("Please enter a cupon code: ")

        if theInput == "code1":
            return total - 5000 
        elif theInput == "code2":
             return total - 10000
        elif theInput == "code3":
             return total - 15000
        else:
            raise ValueError(f"Please enter a valid code")
        



if __name__ == "__main__":
    main()
# Creating the cart 

# sc.addItem(item3)



# sc.removeItem(item2)
# sc.clearCart()  

# print(sc.calculateCartTotal())

# print(sc.applyCupon("code3"))
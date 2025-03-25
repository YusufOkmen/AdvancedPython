import csv

#1- How many people ordered food.
# with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\Balaji Fast Food Sales.csv", "r") as file:
#     csvReader = csv.reader(file)
#     # Skipping the headers
#     next(csvReader)
#     # Diclaring a variable to 0. We will use this to count the number of orders.
#     num = 0
#     # for each row in csvReader append 1 to the num variable.
#     for order in csvReader:
#         num += 1
    
# print(f"The number of orders is {num}")

#2- List all the customers that ordered in afternoon.
# with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\Balaji Fast Food Sales.csv", "r")as file:
#     #We should use csv.DictReader instead csv.reader because we want to access to value of the key.
#     csvReader = csv.DictReader(file)
#     afternoonList = [order for order in csvReader if (order["time_of_sale"] == "Afternoon")]

# print(afternoonList)  

#3- List the Name of meal that ordered by male customers.
with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\Balaji Fast Food Sales.csv", "r") as file:
    csvReader = csv.DictReader(file)
    maleNameList = [order["item_name"] for order in csvReader if (order["received_by"] == "Mr.")]

print(maleNameList)
# r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\Balaji Fast Food Sales.csv", "r"
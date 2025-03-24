import csv

# with open("cars.csv", "w", newline="") as file:
#     csvWriter = csv.writer(file)
#     # csvWriter.writerow(["Marka", "Model"])
#     # csvWriter.writerow(["Toyota", "Corolla"])
#     # csvWriter.writerow(["BMW", "i8"])
#     csvWriter.writerows([["Marka", "Model"], ["Toyota", "Corolla"], ["BMW", "i5"]])

# with open("cars.csv", "a") as file:
#     csvWriter = csv.writer(file)
#     csvWriter.writerow(["Audi", "A5"])

# with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\products.csv") as file:
#     csvReader = csv.reader(file)
#     with open("newProducts.csv", "w", newline="") as f:
#         csvWriter = csv.writer(f)
#         for product in csvReader:
#             csvWriter.writerow([p.upper() for p in product])

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\products.csv", "r+", newline="") as file:
    csvReader = csv.reader(file)
    csvWriter = csv.writer(file)

    next(csvReader)

    products = [[p[0], p[1].upper(), p[2], p[3], p[4]] for p in csvReader]

    file.seek(0)

    csvWriter.writerow(["Id","ProductName","IsActive","Category","Rating"])
    csvWriter.writerows(products)

    file.seek(0)
import csv

# with open("products2.csv", "w", newline="") as file:
#     headers = ["Id","ProductName","IsActive","Category","Rating"]
#     csvWriter = csv.DictWriter(file, headers)
#     csvWriter.writeheader()
#     csvWriter.writerow({
#         "Id": 1,
#         "ProductName": "Excalibur 870",
#         "IsActive": True,
#         "Category": "Computer",
#         "Rating": 4.5
#     })
#     csvWriter.writerow({
#         "Id": 2,
#         "ProductName": "Excalibur 860",
#         "IsActive": False, 
#         "Category": "Computer", 
#         "Rating": 4.2
#     })

# with open("products2.csv", "a", newline="") as file:
#     headers = ["Id","ProductName","IsActive","Category","Rating"]
#     csvWriter = csv.DictWriter(file, headers)
#     csvWriter.writerow({
#         "Id": 3,
#         "ProductName": "Excalibur 850",
#         "IsActive": True,
#         "Category": "Computer",
#         "Rating": 4.1
#     })

with open("products2.csv") as file:
    csvReader = csv.DictReader(file)
    products = list(csvReader)

    with open("products3.csv", "w", newline="") as file:
            headers = ["Id","ProductName","IsActive","Category","Rating"]
            csvWriter = csv.DictWriter(file, headers)
            csvWriter.writeheader()

            for p in products:  
                csvWriter.writerow({
                    "Id": p["Id"],
                    "ProductName": p["ProductName"],
                    "IsActive": p["IsActive"],
                    "Category": p["Category"],
                    "Rating": p["Rating"]
                })


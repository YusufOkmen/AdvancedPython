import csv 

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\products.csv") as file:
    csvReader = csv.DictReader(file, delimiter=",")
    for i in csvReader:
        # if i["Category"] == "Phone":
        #     print(i["Id"], i["ProductName"])
        if float(i["Rating"]) >= 4.5:   
            print(i["Id"], i["ProductName"])
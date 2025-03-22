import csv

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section7\products.csv") as file:
    csvReader = csv.reader(file)
    print(csvReader)
    
    for i in csvReader:
        if (i[2] == "True"):
            print(i)


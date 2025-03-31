data = [
    {
        "id": 1,
        "title": "Excalibur G879",
        "price": 100000,
        "rating": 4.9,
        "category": "Computer",
        "colors": ["Black", "Gray"]
    },
    {
        "id": 2,
        "title": "Excalibur G900",
        "price": 120000,
        "rating": 4.1,
        "category": "Computer",
        "colors": ["White", "Gray"]
    } 
]

import json


product = {
    "id": 3,
    "title": "Excalibur G700",
    "price": 90000,
    "rating": 4.1,
    "category": "Computer",
    "colors": ["White", "Gray"]
    }

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\products.json") as file:
    products = json.load(file)

for p in products:
    if (p["title"] == "Excalibur G700"):
        p["title"] = "Excalibur G600"

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\products.json", "w") as file:
    json.dump(products, file, indent=2)

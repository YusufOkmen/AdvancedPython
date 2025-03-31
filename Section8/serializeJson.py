# From app to file
import json

product = {
    "id": 12,
    "title": "Excalibur G879",
    "price": 100000,
    "rating": 4.9,
    "category": "Computer",
    "colors": ["Black", "Gray"]
} 

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\product.json", "w") as file:
    json.dump(product, file)
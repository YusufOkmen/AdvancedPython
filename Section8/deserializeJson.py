# From file to app

import json

# with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\product.json")as file:
#     data = json.loads(file)


#json string
info = """ 
{
    "id": 1,
    "title": "Excalibur G879",
    "price": 100000,
    "rating": 4.9,
    "category": "Computer",
    "colors": ["Black", "Gray"]
}  
"""

data = json.loads(info)

# print(data)
print(data["title"])
print(data["id"])
print(data["colors"])

# serialize = encode
# deserialize = decode
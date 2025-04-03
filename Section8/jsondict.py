data = {
    "1": {
    "title": "Excalibur G879",
    "price": 100000,
    "ratin": 4.9,
    "category": "Computer",
    "colors": [
      "Black",
      "Gray"
    ]
  },
    "2": {
    "title": "Excalibur G900",
    "price": 120000,
    "rating": 4.1,
    "category": "Computer",
    "colors": [
      "White",
      "Gray"
    ]},
    "3": {
    "title": "Excalibur G600",
    "price": 90000,
    "rating": 4.1,
    "category": "Computer",
    "colors": [
      "White",
      "Gray"
    ]
  }
}

import json




with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\products.json") as file:
    products = json.load(file)

print(products["2"])
print(products["3"])

# Adding new item to the products.
# products.update({
#     "4": {
#     "title": "Victus G5",
#     "price": 90000,
#     "rating": 4.1,
#     "category": "Computer",
#     "colors": [
#       "White",
#       "Gray"
#     ]
#   }
# })

products.update({
    "2": {
    "title": "Victus G6",
    "price": 90000,
    "rating": 4.2,
    "category": "Computer",
    "colors": [
      "White",
      "Gray"
    ]   
  }
})


# Removing a item from the products
# products.pop("4")

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)


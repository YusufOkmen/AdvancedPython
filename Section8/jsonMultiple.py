db = {
    "users": {
        "yusufokmen": {
            "firstname": "Yusuf",
            "lastName": "Ökmen"
        },
        "abdullahokmen": {
            "firstName": "Abdullah",
            "lastName": "Ökmen"
        }
    },
    "products": {
        "1": {
            "title": "Macbook Air",
            "price": 20000
        },
        "2": {
            "title": "Samsung S25",
            "price": 10000
        }
    }
}

import json


with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\db.json") as file:
    data = json.load(file)

# print(data["users"]["yusufokmen"])

data["products"].update({
    "3": {
        "title": "Redmi Note8",
        "price": 5000
    }
})

data["users"].update({
    "elifokmen": {
        "firstName": "Elif",
        "lastName": "Ökmen"
    }
})

with open(r"C:\Users\yusuf\OneDrive\Masaüstü\Coding\AdvancedPython\Section8\db.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

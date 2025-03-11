class Personels:
    def __init__(self, name, username, age):
        self.name = name
        self.username = username
        self.age = age

# Personels Created 
person1 = Personels("Yusuf", "Okmen", "19")
person2 = Personels("Abdullah", "Okmen", "16")

print(person1.username)
print(person2.age)
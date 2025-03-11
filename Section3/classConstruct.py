class Personels:
    # init = constructor method
    def __init__(self, name, username, age):
        # instance attribues
        self.name = name
        self.username = username
        self.age = age

# Personels Created (instance)
person1 = Personels("Yusuf", "Okmen", "19")
person2 = Personels("Abdullah", "Okmen", "16")

print(person1.username)
print(person2.age)
class Personels:
    # init = constructor method
    def __init__(self, name, surname, bDate):
        # instance attribues
        self.name = name
        self.surname = surname
        self.bDate = bDate
    
    # instance methods
    def calculateAge(self):
        print(2025 - self.bDate)

    # instance method
    def allInfo(self):
        print(f"Personel's full info: Name {self.name}, Surname {self.surname}, birth date {self.bDate}")


# Personels Created (instance)
person1 = Personels("Yusuf", "Okmen", 2005)
person2 = Personels("Abdullah", "Okmen", 2008)

print(person1.surname)
print(person2.bDate)

person1.calculateAge()
person2.allInfo()
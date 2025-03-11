class Personels:
    # class attribute
    raisePrise = 4000 
    personelCount = 0

    # init = constructor method
    def __init__(self, name, surname, bDate, salary):
        # instance attribues
        self.name = name
        self.surname = surname
        self.bDate = bDate
        self.salary = salary
        Personels.personelCount += 1
    
    # instance methods
    def calculateAge(self):
        print(2025 - self.bDate)


    # instance method
    def allInfo(self):
        print(f"Personel's full info: Name {self.name}, Surname {self.surname}, birth date {self.bDate}")

    # instance method
    def raiseToSalary(self):
        print(self.salary + Personels.raisePrise)


# Personels Created (instance)
person1 = Personels("Yusuf", "Okmen", 2005, 45000)
person2 = Personels("Abdullah", "Okmen", 2008, 50000)

print(Personels.personelCount)
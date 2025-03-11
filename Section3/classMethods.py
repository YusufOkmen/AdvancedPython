class Personels:
    raisePrise = 4000 
    personelCount = 0

    @classmethod
    def countPersonel(cls):
        return f"Current number of staff : {cls.personelCount}"

    def __init__(self, name, surname, bDate, salary):
        self.name = name
        self.surname = surname
        self.bDate = bDate
        self.salary = salary
        Personels.personelCount += 1
    
    def calculateAge(self):
        print(2025 - self.bDate)

    def allInfo(self):
        print(f"Personel's full info: Name {self.name}, Surname {self.surname}, birth date {self.bDate}")

    def raiseToSalary(self):
        print(self.salary + Personels.raisePrise)


person1 = Personels("Yusuf", "Okmen", 2005, 45000)
person2 = Personels("Abdullah", "Okmen", 2008, 50000)

print(Personels.countPersonel())
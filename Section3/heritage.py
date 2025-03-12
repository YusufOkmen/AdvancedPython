class Person:
    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname
        self.age = age

    def introduce(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    pass 

class Teacher(Person):
    pass

p1 = Person("Yusuf", "Ökmen", 19)
p1.introduce()

s1 = Student("Abdullah", "Ökmen", 16)
s1.introduce()

t1 = Teacher("Emine", "Ökmen", 55)
t1.introduce()

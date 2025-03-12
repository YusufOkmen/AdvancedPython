class Person:
    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname
        self.age = age

    def introduce(self):
        print(self.name, self.surname, self.age)

class Student(Person):
    def __init__(self, name, surname, age, ogrNo, learn):
        # Person.__init__(self, name, surname, age)
        super().__init__(name, surname, age)

        self.ogrNo = ogrNo
        self.learn = learn

        print("Object student has been") 

class Teacher(Person):
    def __init__(self, name, surname, age, branch, teach):
        super().__init__(name, surname, age)

        self.branch = branch
        self.teach = teach

        print("Teacher object has been created")




p1 = Person("Yusuf", "Ökmen", 19)
p1.introduce()

s1 = Student("Abdullah", "Ökmen", 16, 435993, ["Math", "English", "Biology"])
s1.introduce()

t1 = Teacher("Emine", "Ökmen", 55, "English", ["Math", "English"])
t1.introduce()

# class BaseClass():
#     def show(self):
#         return "merhaba"
    
# def addAttribute(self):
#     self.b = 10

# Test = type("Test", (BaseClass,), {"a": 5, "addAttribute": addAttribute})
# t = Test()

# result = t.show()
# result = t.addAttribute()
# print(t.b)

# print(result)

class Meta(type):
    def __new__(self, className, bases, attributes):
        a = {}

        for name, val in attributes.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val 

        for classes in bases:
            if len(bases = 1):
                continue
            else:
                raise TypeError("Please parent only one class")

        return type(className, bases, a)
    
    
    
class Person(metaclass = Meta):
    X = 5
    Y = 10

    def hello(self):
        print("merhaba")

p = Person()

result = p.X

print(result)
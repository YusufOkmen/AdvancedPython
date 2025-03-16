# They allow you to add functionality to an existing function without modifying its structure.

# def goodMorning():
#     print("Welcome")
#     print("Good morning my name is Yusuf")
#     print("Goodbye")

# def howAreYou():
#     print("Welcome")
#     print("How are you my name is Yusuf")
#     print("Goodbye")
#INIFICETN 

def greetings(fn):
    def inner(name):
        print("Welcome")
        fn(name)
        print("Goodbye")

    return inner
    
@greetings
def goodMorning(name):
    print(f"Good morning my name is {name}")

@greetings
def howAreYou(name):
    print(f"How are you my name is {name}")

# greetings(howAreYou)()
# greetings(goodMorning)()
#WITHOUT DECORATION FUNCS

goodMorning("Yusuf")
howAreYou("Abdullah")


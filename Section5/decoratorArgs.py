def decGreetings(count):
        def greetings(fn):
                def inner(name):
                    for _ in range(count):
                        fn(name)
                return inner
        return greetings
        
@decGreetings(count = 3)
def goodMorning(name):
    print(f"Good morning my name is {name}")

@decGreetings(count = 5)
def howAreYou(name):
    print(f"How are you my name is {name}")

goodMorning("Yusuf")
howAreYou("Abdullah")


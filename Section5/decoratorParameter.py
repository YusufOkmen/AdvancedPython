def double(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)
    return inner

@double
def hi():
    print("Hi!!")

@double
def hello(isim):
    print(f"Hello, {isim}")

@double
def goodEvening():
    return "Good evening"

hi()
hello("Yusuf")
print(goodEvening())
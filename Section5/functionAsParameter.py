def filter(fn, list):
    result = []
    for item in list:
        if fn(item):
            result.append(item)
    return result

def isEven(x):
    return x % 2 == 0

def isPositive(x):
    return x > 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]
print(filter(isEven, numbers))

print(filter(isPositive, numbers))
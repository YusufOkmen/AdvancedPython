# Generators are a type of iterable, like lists or tuples, but they allow you to iterate over data without storing the entire dataset in memory. This makes them more memory efficient, especially when working with large datasets.

def counter(max):
    num = 1
    numbers = []

    while (num <= max):
        numbers.append(num)    
        num += 1
    
    return numbers

result = counter(20)
# This was inefficient way to show the list. Because it takes some place in memory.

def advancedCounter(max):
    num = 1

    while (num <= max):
        yield num # yield: Used in generator functions to produce a series of values one at a time, without storing them in memory all at once.
        num += 1
    
result = advancedCounter(20)

while True:
    try:
        print(next(result))
    except StopIteration:
        break

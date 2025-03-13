# We are learning about this topic. Because we want to manipulate our class features.

numbers = [1, 2, 3, 4]

# for number in numbers:
#     print(number)

# print(dir(numbers))

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("The list is ended")
        break
# map: this function takes two argument. First one is the function that will do the expression. And the second one is the list(iterable object) that will give element to the expression function. It saves us from for loops.

#For example
numbers1 = [1, 2, 3, 4 ,5]

sqrNumbers = [num ** 2 for num in numbers1]



# Use case of map function -1

# def takeSqr(number):
#     return number ** 2

# numbers2 = list(map(takeSqr, numbers1))



# Use case of map function and lambda function -2
# numbers3 = list(map(lambda a: a ** 2, numbers1))
# print(numbers3)



# Use case of map function -3
strings = ["Yusuf", "Julia", "Michel"]

# stringsToUpper = list(map(str.upper, strings)) # no need for 'for loops'.
# print(stringsToUpper)



# Use case of map function with dictionaries -4
users = [ 
        {"Name": "Yusuf", "Username": "Okmen"},
        {"Name": "Ozan", "Username": "Akbulut"}
]

names = list(map(lambda kisi: kisi["Username"], users))
print(names)
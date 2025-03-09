# any and all func: 
# any -> or -> True or False = True
# all -> and -> True or True = True

numbers1 = [1, 3, 5, 7, 9, 4]

isThereNoZero = all([bool(num) for num in numbers1])
# print(isThereNoZero)

isAllOdd = all([(num % 2 == 1) for num in numbers1])
# print(isAllOdd)

isThereAnyEven = any([(num % 2 == 0) for num in numbers1])
# print(isThereAnyEven)

users = ["Yusuf", "Mehemt", "Yavuz"]

names = all([(user[0] == "Y") for user in users])
print(names)
# 1 -> List the numbers between 1 and 100 that are divisible by 12.
numberDivide = [i for i in range (1, 100) if (i % 12 == 0)]
print(numberDivide)

# 2 -> Create a list containing the numbers in a given text.
# userText = str(input("Enter a text"))
# numbers = [i for i in userText if (i.isdigit())]
# print(numbers)

# 3 -> For each temperature in the list of temperatures, print a warning about the risk of frost if the temperature is below 4°C.
temperatures = [32, 12, 5, 3, 23, 1, -5]
frostTemp = [temp if (temp >= 4) else "frost" for temp in temperatures]
print(frostTemp)


# 4 -> Print a dictionary of students and their grades where the grades are above 50.
grades = {
    "Ali": 59,
    "Yusuf": 65,
    "Elif": 34
        }

result = [students for students, grade in grades.items() if (grade > 50)]
print(result)

# 5 -> Type the code with list comprehension right below
# result = []

# for x in range(3):
#     for y in range(3):
#         sonuc.append((x, y))

# print(sonuc)

result2 = [(x, y) for x in range(3) for y in range(3)]
print(result2)

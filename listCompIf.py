"""
for item in list1:
    if (statement):
            expression
"""
# [expression for i in list1 if statement] -> list comprehension

numbers1 = [1, 2, 3, 4, 5, 6]
result = []

for item in numbers1:
    if (item < 3):
        result.append(item * 2)
print(result)


result2 = [item * 2 for item in numbers1 if (item < 2)]
print(result2)
result3 = [item if (item < 4) else "This number is bigger than 4"for item in numbers1]
print(result3)

productPrice = [1000, 3000, 2400, 5400]
taxes1 = []
for price in productPrice:
    if (price > 1500):
        taxes1.append(price * 1.05)
print(taxes1)

taxes2 = [price * 1.05 for price in productPrice if (price > 1500)]
print(taxes2)

numInput = int(input("Please enter the base number: "))
sqrNum = (lambda x: x ** 2)(numInput)
print(sqrNum)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
sumNum = (lambda x, y: x + y)(num1, num2)
print(sumNum)
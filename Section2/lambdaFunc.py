# lambda: make lesser code when we use functions

def sqr(a):
    return a ** 2
result = sqr(5)

sqrNum = (lambda a: a ** 2)(3)

sqrNum2 = (lambda a: a ** 2)

result1 = sqrNum2(3)

sumNum = (lambda a, b, c: a + b + c)(2, 5, 7)

def multi(n):
    return (lambda a: a * n)

result3 = multi(4)(5)
print(result3)
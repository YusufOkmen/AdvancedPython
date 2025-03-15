# def outer(number):
#     def inner(number):
#         print(number)
    
#     inner(number)

# outer(10)

def factoriel(num):

    if not isinstance(num, int):
        raise TypeError("Input must be integer.")

    if not num >= 0:
        raise TypeError("Input must be greater than 0 or equal")

    def previousNum(num):
        if (num <= 1):
            return 1
        else:
            return num * previousNum(num - 1)
    
    return previousNum(num)

try:
    print(factoriel(-4))
except Exception as ex:
    print(ex)
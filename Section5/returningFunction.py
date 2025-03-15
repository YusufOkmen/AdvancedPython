# Returnin a function from a function

# def exponentiation(base):
#     def inner(expo):
#         return base ** expo
    
#     return inner

# print(exponentiation(2)(3))





# def questioning(page):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} can access {page}."
#         else:
#             return f"User must be Admin to access this page"
    
#     return inner
        
# access = questioning("Products")
# print(access("Admin1"))



def operation(opName):
    
    def sum(*args):
        total = 0
        for num in args:
            total += num
        return total
    
    def multi(*args):
        total = 1
        for num in args:
            total *= num
        return total
    
    if (opName == "sum"):
        return sum
    elif (opName == "multi"):
        return multi
    
# print(operation("multi")(3, 7, 5))
result = operation("multi")
print(result(3, 7, 5))

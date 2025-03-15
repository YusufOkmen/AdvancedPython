# take numbers between (1 - ∞) and square these numbers
# def takeSquare(end):
#     num = 1

#     while (num <= end):
#         yield num ** 2
#         num += 1
    

# result = takeSquare(7)

# while True:
#     try:
#         print(next(result))
#     except StopIteration:
#         break




# Create the Fibonacci sequence both with a normal function and with a generator function
def normalFibonacci(max):
    fibList = []
    fibList.append(0)
    fibList.append(1)

    i = 0
    j = 1

    while (len(fibList) <= max):
            fibList.append(fibList[i] + fibList[j])
            i += 1
            j += 1

    return fibList

# result = normalFibonacci(20)
# print(result)
# inificent way of solving this problem.

def advancedFibonacci(max):
    num0 = 0
    num1 = 1
    repeat = 0
    while (repeat < max):
        try:
            yield num0
            num2 = num0 + num1
            num0 = num1
            num1 = num2
            repeat += 1
        except StopIteration:
            break


# result = advancedFibonacci(20)

# while True:
#     try:
#         print(next(result))
#     except StopIteration:
#         break


# Do performance tests.

import sys

list1 = [i for i in range(10000)]
# print(sys.getsizeof(list1))

gen = (i for i in range(10000))
# print(sys.getsizeof(gen))

import time

listStartTime = time.time()
sum([i for i in range(10000000)])
listEndTime = time.time() - listStartTime


genStartTime = time.time()
sum((i for i in range(10000000)))
genEndTime = time.time() - genStartTime
print(listEndTime)
print(genEndTime)
print()
import time 

def speedTest(fn):
    def inner(*args, **kwargs):
        startTime = time.perf_counter()
        print(f"method {fn.__name__} is running")
        result = fn(*args, **kwargs)
        endTime = time.perf_counter()
        runTime = endTime - startTime
        print(f"The time that has been passed: {runTime}")
        return result
    return inner

@speedTest
def sumGen():
    return sum((x for x in range(100000000)))

@speedTest
def sumList():
    return sum([x for x in range(100000000)])

print(sumGen())
print(sumList())
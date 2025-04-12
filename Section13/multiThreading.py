import time 
import threading

def calculateSquare(numbers):
    for num in numbers:
        time.sleep(0.3)
        print("square: ", num**2)
        
def calculateCube(numbers):
    for num in numbers:
        time.sleep(0.3)
        print("cube: ", num**3)

numList = [3, 4, 6, 8, 12]

t = time.time()

# calculateSquare(numList)
# calculateCube(numList)

t1 = threading.Thread(target=calculateSquare, args=(numList,))
t2 = threading.Thread(target=calculateCube, args=(numList,))

t1.start()
t2.start()

t1.join()
t2.join()# We use join method if we want to print out first threads and then the main app    
print(f"process complete: {time.time() - t}")
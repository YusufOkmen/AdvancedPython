import time
import multiprocessing

def calculateSquare(numbers):
    for num in numbers:
        time.sleep(0.3)
        print("square: ", num**2)
        
def calculateCube(numbers):
    for num in numbers:
        time.sleep(0.3)
        print("cube: ", num**3)

if __name__ == "__main__":# This line of code checks that if we are in the main process
    arr = [2, 4, 6, 7, 8, 78, 34]

    t = time.time()

    # calculateSquare(arr)
    # calculateCube(arr)

    p1 = multiprocessing.Process(target=calculateSquare, args=(arr,))
    p2 = multiprocessing.Process(target=calculateCube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(time.time() - t)
import time
import multiprocessing




def calculateSquare(numbers, theList):
    global listSquare
    for index, num in enumerate(numbers):
        time.sleep(0.3)
        theList[index] = num**2

def calculateCube(numbers, theList):
    global listCube
    for index, num in enumerate(numbers):
        time.sleep(0.3)
        theList[index] = num**3


if __name__ == "__main__":# This line of code checks that if we are in the main process
    arr = [2, 4, 6, 7, 8, 78, 34]

    t = time.time()

    listSquare = multiprocessing.Array("i", len(arr))
    listCube = multiprocessing.Array("i", len(arr))  

    p1 = multiprocessing.Process(target=calculateSquare, args=(arr, listSquare))
    p2 = multiprocessing.Process(target=calculateCube, args=(arr, listCube))

    p1.start()
    p2.start()

    p1.join()
    p2.join()   

    print(time.time() - t)

    print(listSquare)
    print(listCube[:])
import numpy as np
import matplotlib.pyplot as plt
import time




def partition(arr, low, high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low, high):
        if arr[j]<=pivot:
            i=i+1
            arr[i], arr[j]= arr[j], arr[i]
    arr[i+1], arr[high]= arr[high], arr[i+1]
    return (i+1)

def quicksort(arr, low, high):
    if low < high:
        partion_index= partition(arr, low, high)
        quicksort(arr, low, partion_index-1)
        quicksort(arr, partion_index+1, high)

def printarr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


    


if __name__ == '__main__':
    array = [67, 83, 34, 56, 12, 89]
    size= len(array)

    quicksort(array, 0, size-1)

    print("Sorted array is: ")
    printarr(array)

sorts = [
    {
        "name": "Quick Sort",
        "sort": lambda arr: quicksort(arr, 0, len(arr)-1)
    }
]
elements = np.array([i*1000 for i in range(1, 10)])
plt.xlabel('List Length')
plt.ylabel('Time Complexity')


for sort in sorts:
    times = list()
    start_all = time.process_time()
    for i in range(1, 10):
        start = time.process_time()
        a = np.random.randint(1000, size = i * 1000)
        quicksort(a, 0, len(a)-1 )
        end = time.process_time()
        times.append(end - start)
        print("Quick sort", "Sorted", i * 1000, "Elements in", end - start, "s")
        end_all = time.process_time()
        print("Quick Sort", "Sorted Elements in", end_all - start_all, "s")
        plt.plot(elements, times, label = sort["name"])


    
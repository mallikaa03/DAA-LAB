import time
from timeit import timeit
import matplotlib.pyplot as plt



def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2

        left= arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j<len(right):
            if left[i]< right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k]= right[j]
                j+=1
            k+=1

        while i< len(left):
             arr[k] = left[i]
             i+=1
             k+=1
        
        while j< len(right):
            arr[k] = right[j]
            j+=1
            k+=1

def printarr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()




if __name__ == '__main__':
    array = [6, 8, 34, 87, 64, 98, 102]

    mergesort(array)

    print("Sorted array is: ")
    printarr(array)



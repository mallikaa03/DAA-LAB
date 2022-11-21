import time
import matplotlib.pyplot as plt


def binary_search(arr, low, high, n):   
  
     
   if low <= high:  
  
      mid = (low + high) // 2  
  
 
      if arr[mid] == n:   
         return mid   
   
      elif arr[mid] > n:   
         return binary_search(arr, low, mid - 1, n)   
    
      else:   
         return binary_search(arr, mid + 1, high, n)   
  
   else:    
      return -1  
     
elements2=[]
times2=[]
a=[[1,2,3],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9,10,11,12,13,14],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
b=[3,8,14,20]
for i in range(0,4):
    start = time.time()
    binary_search(a[i],0,len(a[i])-1,b[i])
    end = time.time()
    elements2.append(len(a[i]))
    
print (elements2)
for i in range (0,4):
    print (i)
    times2.append(i)
plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements2, times2, label ='binary search')
plt.grid()
plt.legend()
plt.show()
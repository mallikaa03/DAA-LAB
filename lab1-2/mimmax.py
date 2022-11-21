import timeit
import matplotlib.pyplot as plt 
import numpy as np

num=int(input("Please enter the size of the array:")) 
arr=[]
for i in range(0,num):
    l=int(input())
    arr.append(l)

starttime = timeit.default_timer()

def min_max(arr,start,end):

    if start==end:
        return (arr[start],arr[end])
    
    mid=(start+end)//2
    max1,min1=min_max(arr,start,mid)
    max2,min2=min_max(arr,mid+1,end)

    return(max(max1,max2),min(min1,min2))

a,b=min_max(arr,0,num-1)
print("The time difference is :", timeit.default_timer() - starttime)
print("Max:",a)
print("Min:",b)

x=[5,10,15,20]
y=[3.604199999962532e-05,7.441600000035464e-05, 6.999999999734996e-05,9.370800000141344e-05]
fig = plt.figure(figsize = (10,5))
plt.plot(x, y, label = 'minmax')
plt.title("Min and Max")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()
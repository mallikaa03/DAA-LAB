from cProfile import label
import timeit
import matplotlib.pyplot as plt
import time


n=int(input())
arr=[]
for i in range(0, n):
    x=int(input())
    arr.append(x)

key=int(input())


flag=0
for i in range (n):
    if(arr[i]==key):
        print("number found")
        flag=1
if flag==0:
    print("Number not found")

start_time= timeit.default_timer()


print("The time difference is :", timeit.default_timer() - start_time)

x=[5,10,15,20] 
y=[4.524999999944157e-05,5.2542000002375744e-05,9.53750000007858e-05,8.820799999753604e-05]

fig = plt.figure(figsize = (10,5))
plt.plot(x,y, label='linsearch')
plt.title("Linear Search")
plt.xlabel("Input size")
plt.ylabel("Time")
plt.show()



        



    

import matplotlib.pyplot as plt
import time

def fibonacci(a):
    if a<=1:
        return a
    else:
        return fibonacci(a-1)+ fibonacci(a-2)






x=int(input())
if(x<=0):
    print("Invalid input")
else:
    for i in range(x):
        print(fibonacci(i))
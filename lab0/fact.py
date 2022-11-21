import matplotlib.pyplot as plt
import time

def factorial(a):
    if(a==0):
        return 1
    elif(a==1):
        return a
    else:
        return a*factorial(a-1)



x= int(input())
print(factorial(x))

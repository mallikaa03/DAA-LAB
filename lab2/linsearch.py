def linear_search(arr, n, target ):
    for i in range (n):
        if(arr[i]==target):
            print(i)
        else:
            return -1

        
n=int(input())
arr=input()

key=int(input())
linear_search(arr,n, key)

    

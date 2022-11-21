#dynamic approach

def knapSack(maxcap, weight, profits, n):
   K = [[0 for x in range(maxcap + 1)] for x in range(n + 1)]
   #Table in bottom up manner
   for i in range(n + 1):
      for w in range(maxcap + 1):
         if i == 0 or w == 0:
            K[i][w] = 0
         elif weight[i-1] <= w:
            K[i][w] = max(profits[i-1] + K[i-1][w-weight[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   return K[n][maxcap]
#Main
profits = [556,10,230,104]
weights = [4,8,16,40]
Max_cap = 56
n = len(profits)
print("Maximum profit from 01knapsack: ", knapSack(Max_cap, weights, profits, n))
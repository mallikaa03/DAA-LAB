def fracknapsack(profit, weights, capacity):
    res=0
    index = list(range(len(profit)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(profit, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    for i in index:
        if weights[i]<=capacity:
            res+=profit[i]
            capacity-=weights[i]
        else:
            res+=profit[i]*capacity/weights[i]
            break
    return res

profits=[69,87,15,35,15]
weight=[9, 2, 6, 5, 3]
capacity=15
 
max_profit = fracknapsack(profits, weight, capacity)
print('The maximum profits of items that can be carried:', max_profit)
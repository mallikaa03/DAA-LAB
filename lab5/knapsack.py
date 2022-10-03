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

profits=[6,8,25,45,15]
weight=[7, 8, 4, 5, 3]
capacity=14
 
max_profit = fracknapsack(profits, weight, capacity)
print('The maximum profits of items that can be carried:', max_profit)
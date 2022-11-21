def knapsac(profit, weight, capacity):
    res=0
    index=list(range(len(profit)))
    ratio=[v/w for v,w in zip(profit, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    for i in index:
        if weight[i]<=capacity:
            res+=profit[i]
            capacity-=weight[i]
        
        else:
            res+=profit[i]*capacity/weight[i]
            break
    return res

profit=[76,54,32,21,12]
weights=[2,5,6,9,6]
capacity=17
profits_max=knapsac(profit, weights, capacity)
print(profits_max)

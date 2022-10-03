import bisect
 
def jobScheduling(jobs):
 
    jobs.sort(key = lambda x: (-x[1], -x[0]))
    maxProfit = 0
    maxDeadline = 0
 
    for i in range(0, len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])
 
    slots = list()
 
 
    for i in range(1, maxDeadline + 1):    
        slots.append(i)
 
    maxProfit = 0
    for i in range(len(jobs)):
 
        if len(slots) == 0 or jobs[i][0] < slots[0]:
            continue
 
        availableSlot = slots[bisect.bisect(slots, jobs[i][0]) - 1]
        maxProfit += jobs[i][1]
        slots.remove(availableSlot)
 
    return maxProfit


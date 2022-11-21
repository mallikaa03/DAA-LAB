def job_sequencing(jobs):
    # jobs = [[job, profit, deadline]]
   
    n_inc_order = sorted(jobs, key= lambda x: x[1], reverse=True)

    job_list = []

    i = 0
    for item in n_inc_order:
        if i >= item[2]: # testing with deadline
            for j in range(i, 0, -1):
                if job_list[j-1][2] <= j:
                    continue
                else:
                    if j <= item[2]:
                        job_list.insert(j-1, item)
                        i += 1
                    break
        else:
            job_list.append(item)
            i += 1
    return job_list

n=int(input())
jobs=[]
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(3):      # A for loop for column entries
         a.append(int(input()))
    jobs.append(a)
print(jobs)
print("Sequence of the jobs for max profit: " ,job_sequencing(jobs))
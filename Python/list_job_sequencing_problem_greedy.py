# https://www.geeksforgeeks.org/job-sequencing-problem/
"""
Given an array of jobs where every job has a deadline and associated profit if
 the job is finished before the deadline. It is also given that every job takes
 the single unit of time, so the minimum possible deadline for any job is 1.

How to maximize total profit if only one job can be scheduled at a time.

Examples: 
Input: Four Jobs with following 
deadlines and profits
JobID  Deadline  Profit
  a      4        20   
  b      1        10
  c      1        40  
  d      1        30
Output: Following is maximum 
profit sequence of jobs
        c, a   

Input:  Five Jobs with following
deadlines and profits
JobID   Deadline  Profit
  a       2        100
  b       1        19
  c       2        27
  d       1        25
  e       3        15
Output: Following is maximum 
profit sequence of jobs
        c, a, e
"""

# Below sol. is O(n2)
# See list_job_sequencing_problem_disjoint_set.py for optimized sol.

def get_min(a, b):
    return a if a<b else b

def get_free_time_slot(free_slots, deadline):
    i = deadline-1
    for i in range(i,-1,-1):
        if free_slots[i]: return i
    return -1

def get_max_profit(jobs_list):
    profit = 0
    selected_jobs = list()
    length = len(jobs_list)
    jobs_list.sort(key = lambda x : x[2], reverse = True)
    print(jobs_list)
    free_timeslots = [True for i in range(length)]
    for i in range(length):
        slot = get_free_time_slot(free_timeslots, get_min(jobs_list[i][1],length))
        if slot != -1:
            free_timeslots[slot] = False
            profit+=jobs_list[i][2]
            selected_jobs.append((jobs_list[i][0],slot))
    return profit, selected_jobs

def main():
    jobs = [['a', 2, 100], ['b',2,60],['c',1,50]]
    print('Jobs =',jobs)
    max_profit, selected_jobs = get_max_profit(jobs)
    print('Max Profit = ', max_profit)
    print('Sel. Jobs =',selected_jobs)

if __name__ == '__main__':
    main()
# https://www.geeksforgeeks.org/job-sequencing-problem/
# https://www.geeksforgeeks.org/job-sequencing-using-disjoint-set-union/
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

class DisjointSet:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        """
        Rank can't be used here as when rank is used there then union(u,v)
        may not lead to v being parent of u. And this is needed as per below 
        code.
        """
        # self.rank = [1 for i in range(size)]
    
    def find_parent(self, k):
        if self.parent[k] == k: return k
        self.parent[k] = self.find_parent(self.parent[k])
        return self.parent[k]
    
    def union(self, u, v):
        p1 = self.find_parent(u)
        p2 = self.find_parent(v)
        if p1==p2: return
        self.parent[p1] = p2
        # self.rank[p2]+=1

def get_min(a, b):
    return a if a<b else b

# If it returns 0 means no slot for given deadline is present
def get_free_time_slot(dj_set, deadline):
    return dj_set.find_parent(deadline)

def get_max_profit(jobs_list):
    profit = 0
    selected_jobs = list()
    length = len(jobs_list)
    dj_set = DisjointSet(length+1)
    jobs_list.sort(key = lambda x : x[2], reverse = True)
    print(jobs_list)
    for i in range(length):
        slot = get_free_time_slot(dj_set, get_min(jobs_list[i][1],length))
        if slot != 0:
            dj_set.union(slot, slot-1)
            profit+=jobs_list[i][2]
            selected_jobs.append((jobs_list[i][0],slot-1))
        print('parent =', dj_set.parent)
        # print('rank =',dj_set.rank)
    return profit, selected_jobs

def main():
    jobs = [['a', 1, 10], ['b', 2, 20], ['c', 3, 30]]
    print('Jobs =',jobs)
    max_profit, selected_jobs = get_max_profit(jobs)
    print('Max Profit = ', max_profit)
    print('Sel. Jobs =',selected_jobs)

if __name__ == '__main__':
    main()
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
"""
We have n jobs, where every job is scheduled to be done from startTime[i] to
 endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the
 maximum profit you can take such that there are no 2 jobs in the subset
 with overlapping time range.

If you choose a job that ends at time X you will be able to start another job
 that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

Constraints:
1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""

# NOTE-  Below sol. is sorting + DP + binary search
# Time complexity - O(NLog(N))
# Other sol. with simple sorting + DP is O(n2)

def get_max(a, b):
    return a if a>b else b

class Job:
    def __init__(self, startTime, endTime, profit):
        self.startTime = startTime
        self.endTime = endTime
        self.profit = profit
    
    def compare(self):
        return self.startTime

    def __str__(self):
        return 's={} e={} profit={}'.format(self.startTime,self.endTime,
                                            self.profit)
        
    def __repr__(self):
        return self.__str__()

def get_ceil(profit_dp, s, e, end_time):
    _ceil = e+1
    while s<=e:
        mid = s + (e-s)//2
        if profit_dp[mid][0]>=end_time:
            _ceil = mid
            e = mid-1
        else:
            s = mid+1
    return _ceil
    
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], 
                      profit: list[int]) -> int:
        length = len(startTime)
        # print(length)
        jobsList = [Job(startTime[i], endTime[i], profit[i]) for i in range(length)]
        jobsList.sort(key = Job.compare)
        # print(jobsList)
        profit_DP = [None]*length
        s, e = length, length-1
        for i in range(length-1, -1, -1):
            # Here instead of checking all the jobs from i+1 to length-1, 
            # using binary search to get only the required job.
            _ceil = get_ceil(profit_DP, s, e, jobsList[i].endTime)
            t_profit = jobsList[i].profit
            if _ceil!=length:
                t_profit+=profit_DP[_ceil][1]
            if s==length or t_profit > profit_DP[s][1]:
                s-=1
                profit_DP[s] = (jobsList[i].startTime, t_profit)
        # print(profit_DP)
        return profit_DP[s][1]
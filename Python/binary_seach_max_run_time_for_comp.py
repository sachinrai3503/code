# https://leetcode.com/problems/maximum-running-time-of-n-computers
"""
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the
 ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers
 simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment,
 you can remove a battery from a computer and insert another battery any number of times. The inserted battery
 can be a totally new battery or a battery from another computer. You may assume that the removing and inserting
 processes take no time.

Note that the batteries cannot be recharged.
Return the maximum number of minutes you can run all the n computers simultaneously.

Example 1:
Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. 
 Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer
 and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:
Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into
 the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

Constraints:
1 <= n <= batteries.length <= 105
1 <= batteries[i] <= 109
"""

from typing import List

class Solution:

    # This is slow
    def count_comp_run_for_k_min1(self, batteries, batteries_count, k):
        count = 0
        s, e = 0, batteries_count-1
        remaining_min = k
        battery_count = 0
        while s<=e:
            # print(f'{k=} {s=} {e=} {remaining_min=} {battery_count=} {count=}')
            if remaining_min>=batteries[e]:
                remaining_min-=batteries[e]
                battery_count+=1
                e-=1
                if remaining_min==0:
                    count+=1
                    remaining_min = k
                    battery_count = 0
            elif remaining_min>=batteries[s]:
                remaining_min-=batteries[s]
                battery_count+=1
                s+=1
                if remaining_min==0:
                    count+=1
                    remaining_min = k
                    battery_count = 0
            else:
                count+=1
                if battery_count>=1:
                    remaining_min = k - (batteries[s]-remaining_min)
                    battery_count = 1
                else:
                    remaining_min = k
                    battery_count = 0
                s+=1
        return count

    def count_comp_run_for_k_min(self, batteries, k):
        extra = 0
        for power in batteries:
            extra+=min(power, k)
        return extra//k

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        time = 0
        # bat_count = len(batteries)
        # batteries.sort() # NEEDED for count_comp_run_for_k_min1(...)
        s, e = 1, (sum(batteries)//n) + 1
        # print(f'{s=} {e=}')
        while s<=e:
            mid = s + (e-s)//2
            # if self.count_comp_run_for_k_min1(batteries, bat_count, mid)>=n:
            if self.count_comp_run_for_k_min(batteries, mid)>=n:
                time = mid
                s = mid+1
            else:
                e = mid-1
        return time
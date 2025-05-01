# https://leetcode.com/problems/maximum-performance-of-a-team
# https://leetcode.com/discuss/interview-question/889942/any-idea-how-to-solve-this-problem-i-just-bombed-it-in-an-interview
"""
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers
 numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) 
 and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the 
 maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 
Constraints:
1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
"""

from sys import maxsize
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        op = -maxsize
        speed_index = [i for i in range(n)]
        efficiency_index = [i for i in range(n)]
        visited = set()
        to_visit = set() # set of k-1 indexs which are yet to be computed
        count = 0 # count of elements in to_visit set
        remaining_sum = 0 # sum of elements in to_visit set
        speed_index.sort(key = lambda x : speed[x])
        efficiency_index.sort(key = lambda x : efficiency[x])
        # print(f'{speed_index=}')
        # print(f'{efficiency_index=}')
        j = n-1
        t_k = k-1
        for i in efficiency_index:
            min_eff = efficiency[i]
            t_speed = speed[i]
            visited.add(i)
            if i in to_visit:
                to_visit.remove(i)
                count-=1
                remaining_sum-=speed[i]
            while j>-1 and count<t_k:
                if speed_index[j] not in visited:
                    remaining_sum+=speed[speed_index[j]]
                    count+=1
                    to_visit.add(speed_index[j])
                j-=1
            # if count<t_k:
            #     break
            op = max(op, min_eff*(t_speed + remaining_sum))
        return op%(1000000007)

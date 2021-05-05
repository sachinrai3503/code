# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
"""
Given an integer array bloomDay, an integer m and an integer k.
We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers
 from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
 and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets
 from the garden. If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower
 bloomed and _ means flower didn't bloom in the garden.

We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers.
 We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make
 another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Example 4:
Input: bloomDay = [1000000000,1000000000], m = 1, k = 1
Output: 1000000000
Explanation: You need to wait 1000000000 days to have a flower ready for a bouquet.

Example 5:
Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
Output: 9

Constraints:
bloomDay.length == n
1 <= n <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= m <= 10^6
1 <= k <= n
"""

from sys import maxsize
from collections import deque
class Solution:
    
    def get_max_list(self, bloomDay, k):
        length = len(bloomDay)
        op_list = [0 for i in range(length)]
        max_que = deque()
        for i in range(length-1, -1, -1):
            while len(max_que)>0 and bloomDay[i]>=bloomDay[max_que[-1]]:
                max_que.pop()
            max_que.append(i)
            if i<=length-k:
                op_list[i] = bloomDay[max_que[0]]
            if max_que[0]>=(i-1)+k:
                max_que.popleft()
        return op_list
    
    def minDays1(self, bloomDay: list[int], m: int, k: int) -> int:
        length = len(bloomDay)
        if length<m*k: return -1
        op = [[0 for j in range(length)] for i in range(2)]
        max_list = self.get_max_list(bloomDay, k)
        print(max_list)
        for i in range(1, m+1):
            cur_row = i%2
            prev_row = 0 if cur_row==1 else 1
            min_flower_needed = i*k
            prev = maxsize
            for j in range(length-1, -1, -1):
                if j<=length-min_flower_needed:
                    i_minus_1_min_time = 0
                    if j+k<length:
                        i_minus_1_min_time = op[prev_row][j+k]
                    op[cur_row][j] = min(prev, max(max_list[j],i_minus_1_min_time))
                    prev = op[cur_row][j]
        return op[m%2][0]
    
    def get_max_min(self, nums):
        _max, _min = -maxsize, maxsize
        for num in nums:
            _max = max(_max, num)
            _min = min(_min, num)
        return _max, _min
    
    def get_bouquets_count(self, bloomDay, max_allowed_days, adjacent_flowers_count):
        bouquests_count = 0
        t_count = 0
        for day in bloomDay:
            if day>max_allowed_days:
                t_count=0
            else:
                t_count+=1
            if t_count==adjacent_flowers_count:
                bouquests_count+=1
                t_count = 0
        return bouquests_count
    
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        length = len(bloomDay)
        if m*k>length: return -1
        high, low = self.get_max_min(bloomDay)
        # print(low, high)
        min_day = -1
        while low<=high:
            mid = low + (high-low)//2
            t_bouquets_count = self.get_bouquets_count(bloomDay, mid, k)
            if t_bouquets_count<m:
                low = mid+1
            else:
                min_day = mid
                high = mid-1
            # print(low, high, mid, min_day)
        return min_day
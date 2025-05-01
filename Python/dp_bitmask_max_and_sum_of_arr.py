# https://leetcode.com/problems/maximum-and-sum-of-array
"""
You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. 
 There are numSlots slots numbered from 1 to numSlots.

You have to place all n integers into the slots such that each slot contains at most two numbers. 
 The AND sum of a given placement is the sum of the bitwise AND of every number with its respective slot number.

For example, the AND sum of placing the numbers [1, 3] into slot 1 and [4, 6] into slot 2
 is equal to (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4.
Return the maximum possible AND sum of nums given numSlots slots.

Example 1:
Input: nums = [1,2,3,4,5,6], numSlots = 3
Output: 9
Explanation: One possible placement is [1, 4] into slot 1, [2, 6] into slot 2, and [3, 5] into slot 3. 
This gives the maximum AND sum of 
(1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 1 + 0 + 2 + 2 + 3 + 1 = 9.

Example 2:
Input: nums = [1,3,10,4,7,1], numSlots = 9
Output: 24
Explanation: One possible placement is [1, 1] into slot 1, [3] into slot 3, [4] into slot 4, [7]
 into slot 7, and [10] into slot 9.
This gives the maximum AND sum of (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + 
(10 AND 9) = 1 + 1 + 3 + 4 + 7 + 8 = 24.
Note that slots 2, 5, 6, and 8 are empty which is permitted.
 
Constraints:
n == nums.length
1 <= numSlots <= 9
1 <= n <= 2 * numSlots
1 <= nums[i] <= 15
"""

from typing import List

class Solution:

    def get_max_AND_sum(self, i, slot_num_count, nums_mask):
        # print(f'{i=} {slot_num_count=} {nums_mask=} {self.cur_sum=} {self.max_sum=}')
        if self.nums_to_allot>(self.k*(self.num_slots-i+1)): return
        if self.nums_to_allot==0:
            self.max_sum = max(self.max_sum, self.cur_sum)
            return
        self.get_max_AND_sum(i+1, 0, nums_mask)
        if slot_num_count==self.k: return
        self.nums_to_allot-=1
        for j in range(self.nums_count):
            if not nums_mask&(1<<j):
                self.cur_sum = self.cur_sum + (i&self.nums[self.nums_count-j-1])
                self.get_max_AND_sum(i, slot_num_count+1, nums_mask|(1<<j))
                self.cur_sum = self.cur_sum - (i&self.nums[self.nums_count-j-1])
        self.nums_to_allot+=1

    # This will timeout
    def maximumANDSum_dp_mask(self, nums: List[int], numSlots: int) -> int:
        self.max_sum = 0
        self.nums = nums
        self.num_slots = numSlots
        self.k = 2
        self.nums_count = len(nums)
        self.nums_to_allot = self.nums_count
        self.cur_sum = 0
        self.get_max_AND_sum(1, 0, 0)
        return self.max_sum

    # Time - (2^N)*N
    # space = 2^N
    # N = 2*numSlots 
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        for i in range(2*numSlots - len(nums)):
            nums.append(0)
        nums_count = len(nums)
        # print(f'{nums=} {numSlots=} {nums_count=}')
        dp_size = 1<<nums_count
        dp = [None for i in range(dp_size)]
        dp[0] = [0, 0] # (sum, set_bit_count)
        for i in range(dp_size):
            i_sum, i_set_bit_count = dp[i]
            slot = (i_set_bit_count//2) + 1
            for j in range(nums_count):
                if not (i&(1<<j)):
                    next_i = i|(1<<j)
                    t_sum = i_sum + (slot & nums[nums_count-j-1])
                    if dp[next_i] is None:
                        dp[next_i] = [t_sum, i_set_bit_count+1]
                    else:
                        dp[next_i] = [max(dp[next_i][0], t_sum), i_set_bit_count+1]
        return dp[(1<<nums_count) - 1][0]
# https://leetcode.com/problems/closest-subsequence-sum
"""
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal.
 That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:
Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

Example 2:
Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

Example 3:
Input: nums = [1,2,3], goal = -7
Output: 7

Constraints:
1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109
"""

from sys import maxsize
from typing import List

class Solution:

    # This will give memory out
    def minAbsDifference_dp1(self, nums: List[int], goal: int) -> int:
            nums_len = len(nums)
            mid_len = nums_len//2
            nums_sum = sum(nums)
            result = min(abs(goal-0), abs(goal - nums_sum))
            if result == 0: return result
            dp = [set() for i in range(mid_len)]
            for num in nums:
                for i in range(mid_len-1, -1, -1):
                    sums_with_i_nums = dp[i]
                    if i==0:
                        s1 = num
                        s2 = nums_sum - s1
                        sums_with_i_nums.add(s1)
                        result = min(result, min(abs(goal-s1), abs(goal-s2)))
                    elif dp[i-1]:
                        for tsum in dp[i-1]:
                            s1 = tsum + num
                            s2 = nums_sum - s1
                            sums_with_i_nums.add(s1)
                            result = min(result, min(abs(goal-s1), abs(goal-s2)))
            # print(f'{dp=}')
            return result
        
    def get_all_possible_sum_combinations(self, nums, nums_len):
        op = list()
        op_len = 0
        for num in nums:
            new_sum_added = 0
            for i in range(op_len):
                op.append(op[i] + num)
                new_sum_added+=1
            op.append(num)
            new_sum_added+=1
            op_len+=new_sum_added
        op.append(0)
        return op

    # Here nums is divided in equal half of n/2 element. So, totol mem needed to store the combination is 2**(n/2) * 2
    # n = 10. above sol mem = (n/2) + atleast(2**(n/2 + 1))
    # for this sol mem = 2**5 + 2**5 = 64
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        result = maxsize
        nums_len = len(nums)
        mid_len = nums_len//2
        left_nums_sum_comb_list = self.get_all_possible_sum_combinations(nums[:mid_len], mid_len)
        right_nums_sum_comb_list = self.get_all_possible_sum_combinations(nums[mid_len:], mid_len)
        left_nums_sum_comb_list.sort()
        right_nums_sum_comb_list.sort()
        # print(f'{left_nums_sum_comb_list=}')
        # print(f'{right_nums_sum_comb_list=}')
        left_len, right_len = len(left_nums_sum_comb_list), len(right_nums_sum_comb_list)
        i, j = 0, right_len-1
        while i<left_len and j>=0:
            s1, s2 = left_nums_sum_comb_list[i], right_nums_sum_comb_list[j]
            t_sum = s1+s2
            if t_sum==goal: return 0
            if t_sum<goal:
                result = min(result, goal-t_sum)
                i+=1
            else:
                result = min(result, t_sum-goal)
                j-=1
        return result
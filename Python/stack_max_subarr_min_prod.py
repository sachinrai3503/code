# https://leetcode.com/problems/maximum-subarray-min-product
"""
The min-product of an array is equal to the minimum value in the array multiplied 
 by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 
 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty
 subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation.
 Testcases are generated such that the maximum min-product without modulo will fit in
 a 64-bit signed integer.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

Example 2:
Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

Example 3:
Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 107
"""

from sys import maxsize
from typing import List

class Solution:

    def maxSumMinProduct(self, nums: List[int]) -> int:
        max_prod = -maxsize
        nums_len = len(nums)
        prefix_sum = [0]
        m = 1000000007
        t_sum = 0
        stck = list() # [(i, left_i), ...] 
        for i in range(nums_len):
            num = nums[i]
            t_sum+=num
            prefix_sum.append(t_sum)
            while stck and nums[stck[-1][0]]>=num:
                ti, t_li = stck.pop()
                max_prod = max(max_prod, nums[ti]*(prefix_sum[i]-prefix_sum[t_li+1]))
            if not stck: stck.append((i, -1))
            else:
                stck.append((i, stck[-1][0]))
        #     print(f'{stck=}')
        # print(f'{prefix_sum=}')
        while stck:
            ti, t_li = stck.pop()
            max_prod = max(max_prod, nums[ti]*(prefix_sum[-1]-prefix_sum[t_li+1]))
        return max_prod%1000000007
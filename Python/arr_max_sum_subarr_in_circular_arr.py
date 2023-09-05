# https://leetcode.com/problems/maximum-sum-circular-subarray
"""
Given a circular integer array nums of length n, return the maximum possible sum 
 of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. 
 Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element
 of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. 
 Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not
 exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2. 

Constraints:
n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""

from sys import maxsize
from typing import List

class Solution:

    # Idea - val1 = find the subarr with max sum (normal logic)
    #      - val2 = find the subarr with min sum (same above logic but in reverse)
    #      - max(val1, total_arr_sum-val2) 
    #      - subtracting the val2 gets the circular sum
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = -maxsize, maxsize
        total_sum = 0
        t1_sum, t2_sum = 0, 0
        for num in nums:
            total_sum+=num
            t1_sum+=num
            t2_sum+=num
            if t1_sum>max_sum:
                max_sum = t1_sum
            if t2_sum<min_sum:
                min_sum = t2_sum
            if t1_sum<0:
                t1_sum = 0
            if t2_sum>0:
                t2_sum = 0
        if max_sum<=0: return max_sum
        return max(max_sum, total_sum-min_sum)
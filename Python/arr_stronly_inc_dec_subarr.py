# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray
"""
You are given an array of integers nums. Return the length of the longest subarray of nums which is either 
 strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
"""

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 0
        inc_len, dec_len = 1, 1
        prev = nums[0]
        for num in nums:
            if num>prev:
                inc_len+=1
                dec_len = 1
            elif num<prev:
                dec_len+=1
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1
            prev = num
            max_len = max(max_len, inc_len, dec_len)
        return max_len
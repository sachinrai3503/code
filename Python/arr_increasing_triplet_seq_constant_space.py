# https://leetcode.com/problems/increasing-triplet-subsequence/
"""
Given an integer array nums, return true if there exists a triple of indices
 (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices
 exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity 
 and O(1) space complexity?
"""

from sys import maxsize
from typing import List

class Solution:

    # This uses O(n) space
    def increasingTriplet1(self, nums: List[int]) -> bool:
        prev = -maxsize
        nums_len = len(nums)
        max_from_right = [None for i in range(nums_len)]
        for i in range(nums_len-1, -1, -1):
            max_from_right[i] = prev
            num = nums[i]
            if num>prev:
                prev = num
        # print(f'{max_from_right=}')
        min_from_left = maxsize
        for i in range(nums_len):
            num = nums[i]
            if num>min_from_left and num<max_from_right[i]:
                return True
            min_from_left = min(min_from_left, num)
        return False
    
    # This uses O(1) space and O(n) time with 1 pass: Based on LIS
    def increasingTriplet2(self, nums: List[int]) -> bool:
        temp = [maxsize, maxsize]
        for num in nums:
            if num>temp[1]: return True
            if num>temp[0]: temp[1] = num
            else: temp[0] = num
        return False
    
    # This uses O(1) space and O(n) time with 2 pass
    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        prev_min = maxsize
        min_count = 0
        for i in range(nums_len):
            if nums[i]<=prev_min:
                prev_min = nums[i]
                nums[i] = None
                min_count+=1
        if min_count==nums_len: return False
        next_max = -maxsize
        for i in range(nums_len-1, -1, -1):
            if nums[i] is None: continue
            if nums[i]>=next_max:
                next_max = nums[i]
            else:
                return True
        return False
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and 
 ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

from typing import List

class Solution:

    def get_floor(self, nums, s, e, k):
        _floor = -1
        while s<=e:
            mid = s + (e-s)//2
            if nums[mid]<k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor
    
    def get_ceil(self, nums, s, e, k):
        _ceil = e+1
        while s<=e:
            mid = s + (e-s)//2
            if nums[mid]<=k:
                s = mid+1
            else:
                _ceil = mid
                e = mid-1
        return _ceil

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len==0: return [-1, -1]
        _floor = self.get_floor(nums, 0, nums_len-1, target)
        _ceil = self.get_ceil(nums, 0, nums_len-1, target)
        # print(f'{_floor=} {_ceil=}')
        if _floor==(nums_len-1) or nums[_floor+1]!=target: return [-1, -1]
        return [_floor+1, _ceil-1]
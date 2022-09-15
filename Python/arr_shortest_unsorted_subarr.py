# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""
Given an integer array nums, you need to find one continuous subarray that if you only
 sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:
Input: nums = [1,2,3,4]
Output: 0

Example 3:
Input: nums = [1]
Output: 0

Constraints:
1 <= nums.length <= 104
-105 <= nums[i] <= 105
 
Follow up: Can you solve it in O(n) time complexity?
"""

from sys import maxsize

class Solution:
    
    def get_floor(self, arr, s, e, k):
        _floor = -1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]<=k:
                _floor = mid
                s = mid+1
            else:
                e = mid-1
        return _floor

    def get_ceil(self, arr, s, e, k):
        _ceil = e+1
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]<k:
                s = mid+1
            else:
                _ceil = mid
                e = mid-1
        return _ceil
    
    def get_max_min(self, arr, s, e):
        _min, _max = maxsize, -maxsize
        for num in arr[s:e+1]:
            _min = min(_min, num)
            _max = max(_max, num)
        return _min, _max
    
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        len_nums = len(nums)
        i, j = 0, len_nums-1
        while i<(len_nums-1):
            if nums[i]>nums[i+1]:
                break
            i+=1
        if i==(len_nums-1): return 0
        while j>0:
            if nums[j]<nums[j-1]:
                break
            j-=1
        # print(i, j)
        _min, _max = self.get_max_min(nums, i, j)
        # print(f'{_min=} {_max=}')
        _floor = self.get_floor(nums, 0, i-1, _min)
        _ceil = self.get_ceil(nums, j+1, len_nums-1, _max)
        # print(f'{_floor=} {_ceil=}')
        return _ceil-_floor-1
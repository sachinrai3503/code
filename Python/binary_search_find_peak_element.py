# https://leetcode.com/problems/find-peak-element
"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
 return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater 
 than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the
 peak element is 6.
 
Constraints:
1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

from typing import List

class Solution:

    def is_peak(self, nums, s, e, k):
        if s==e: return 0
        if (k-1)>=0 and nums[k-1]>nums[k]: return -1
        if nums[k+1]>nums[k]: return 1
        return 0

    def findPeakElement(self, nums: List[int]) -> int:
        nums_len = len(nums)
        s, e = 0, nums_len-1
        while s<=e:
            mid = s + (e-s)//2
            result = self.is_peak(nums, s, e, mid)
            if result==0:
                return mid
            elif result==-1:
                e = mid-1
            else:
                s = mid+1
        return -1
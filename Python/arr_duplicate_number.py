# https://leetcode.com/problems/find-the-duplicate-number
"""
Given an array of integers nums containing n + 1 integers where each integer is in
 the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant
 extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
 appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

# Same problem with O(n) - arr_duplicate_number.c

from typing import List

class Solution:

    def get_count(self, nums, k):
        count = 0
        for num in nums:
            if num<=k: count+=1
        return count

    def findDuplicate(self, nums: List[int]) -> int:
        dup = -1
        nums_len = len(nums)
        s, e = 0, nums_len-1
        while s<=e:
            mid = s + (e-s)//2
            count = self.get_count(nums, mid)
            if count<=mid:
                s = mid+1
            else:
                dup = mid
                e = mid-1
        return dup
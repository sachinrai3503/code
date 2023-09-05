# https://leetcode.com/problems/product-of-array-except-self
"""
Given an integer array nums, return an array answer such that answer[i] is equal
 to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""

from typing import List
from math import log2

class Solution:

    # This won't work for -ve number or 0 in array
    def productExceptSelf_log(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        nums_log = 0
        for num in nums:
            if num==0: continue
            nums_log+=log2(num)
        for i in range(nums_len):
            if nums[i]!=0:
                nums[i] = int(pow(2, nums_log-log2(nums[i])))
            else:
                nums[i] = int(pow(2, nums_log))
        print(nums)
        return nums
    
    # 2 pass
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        prev = 1
        op = list()
        for num in nums:
            op.append(prev)
            prev*=num
        prev = 1
        for i in range(nums_len-1, -1, -1):
            op[i] = prev*op[i]
            prev*=nums[i]
        return op
    
    # 2 pass + O(1) space: Will not work with 0 in arr
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        prod = 1
        for num in nums:
            prod*=num
        for i in range(len(nums)):
            nums[i] = int(prod*(nums[i]**-1))
        return nums
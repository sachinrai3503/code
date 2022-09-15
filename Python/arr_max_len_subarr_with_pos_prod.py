# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
"""
Given an array of integers nums, find the maximum length of a subarray where the
 product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out
 of that array.

Return the maximum length of a subarray with positive product.

Example 1:
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Example 2:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Example 3:
Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        nums_len = len(nums)
        neg_count = 0
        s, t_s = 0, 0
        neg_flag = False
        max_len = 0
        for i in range(nums_len):
            num = nums[i]
            if num==0:
                s = i+1
                t_s = i+1
                neg_count = 0
                neg_flag = False
                continue
            elif num<0:
                neg_count+=1
            if neg_count%2==0: max_len = max(max_len, i-s+1)
            if neg_flag:
                if neg_count%2==1: max_len = max(max_len, i-t_s+1)
            if num<0 and neg_flag is False:
                t_s = i+1
                neg_flag = True
            # print(f'{i=}, {num=}, {s=}, {t_s=}, {neg_count=} {max_len=}')
        return max_len
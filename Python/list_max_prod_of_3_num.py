# https://leetcode.com/problems/maximum-product-of-three-numbers/
# https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
"""
Given an integer array nums, find three numbers whose product is maximum and
 return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""

from sys import maxsize

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        max_3_num = [maxsize*-1, maxsize*-1, maxsize*-1]
        min_2_num = [maxsize, maxsize]
        for num in nums:
            if num>max_3_num[0]:
                max_3_num[0] = num
                if num>max_3_num[1]:
                    max_3_num[0] = max_3_num[1]
                    max_3_num[1] = num
                    if num>max_3_num[2]:
                        max_3_num[1] = max_3_num[2]
                        max_3_num[2] = num
            if num<0 and num<min_2_num[0]:
                min_2_num[0] = num
                if num<min_2_num[1]:
                    min_2_num[0] = min_2_num[1]
                    min_2_num[1] = num
        # print(min_2_num, max_3_num)
        pos_prod = max_3_num[0]*max_3_num[1]*max_3_num[2]
        if min_2_num[1] == maxsize: return pos_prod
        neg_prod = None if min_2_num[0] == maxsize else min_2_num[0]*min_2_num[1]
        if neg_prod is None: return pos_prod
        return max(pos_prod, neg_prod*max_3_num[2])
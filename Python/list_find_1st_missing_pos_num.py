# https://leetcode.com/problems/first-missing-positive/
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array-set-2/?ref=rp
# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array-set-3/?ref=rp
"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    
    def get_1st_pos_index(self, nums):
        neg_index = 0
        length = len(nums)
        i = 0
        while i < length:
            if nums[i]>0: i+=1
            else:
                nums[neg_index], nums[i] = nums[i], nums[neg_index]
                neg_index+=1
                i+=1
        return neg_index
    
    def firstMissingPositive(self, nums: list[int]) -> int:
        length = len(nums)
        first_pos_index = self.get_1st_pos_index(nums)
        if first_pos_index == length:
            return 1
        base_index = first_pos_index
        i = base_index
        while i<length:
            expected_index = nums[i]+base_index-1
            if expected_index == i: i+=1
            elif expected_index >= length: i+=1
            elif nums[expected_index] == nums[i]: i+=1
            else:
                nums[expected_index], nums[i] = nums[i], nums[expected_index]
        i = base_index
        while i<length:
            expected_index = nums[i]+base_index-1
            if expected_index!=i:
                return i-base_index+1
            i+=1
        return i-base_index+1
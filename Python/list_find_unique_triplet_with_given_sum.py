# https://www.geeksforgeeks.org/unique-triplets-sum-given-value/
# https://leetcode.com/problems/3sum/
"""
Given an array nums of n integers, are there elements a, b, c in nums such that
 a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
class Solution:
    
    def get_next_i(self, nums, i):
        num = nums[i]
        length = len(nums)
        while i<length and num==nums[i]:
            i+=1
        return i

    def get_next_j(self, nums, j):
        num = nums[j]
        while j>=0 and num==nums[j]:
            j-=1
        return j
    
    def get_pair_with_x_sum(self, nums, s, e, x, a, op_list):
        i, j = s, e
        while i<j:
            t_sum = nums[i] + nums[j]
            if t_sum<x:
                i+=1
            elif t_sum>x:
                j-=1
            else:
                op_list.append([a,nums[i],nums[j]])
                i = self.get_next_i(nums, i)
                j = self.get_next_j(nums, j)
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        req_sum = 0
        op_list = list()
        length = len(nums)
        nums.sort()
        i = 0
        while i<length-2:
            self.get_pair_with_x_sum(nums, i+1, length-1,req_sum-nums[i], nums[i], op_list)
            i = self.get_next_i(nums, i)
        return op_list
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string
# https://leetcode.com/problems/permutations
"""
Given an array nums of distinct integers, return all the possible permutations.
 You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List

class Solution:

    def __init__(self):
        self.op = list()

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def find_all_permutation(self, nums, nums_len, i):
        if i==nums_len:
            self.op.append(list(nums))
        else:
            self.find_all_permutation(nums, nums_len, i+1)
            for j in range(i+1, nums_len):
                self.swap(nums, i, j)
                self.find_all_permutation(nums, nums_len, i+1)
                self.swap(nums, i, j)

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        self.find_all_permutation(nums, nums_len, 0)
        return self.op
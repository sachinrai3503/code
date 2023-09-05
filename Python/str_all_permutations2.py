# https://leetcode.com/problems/permutations-ii
"""
Given a collection of numbers, nums, that might contain duplicates, return all 
 possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List

class Solution:

    def __init__(self):
        self.op = list()

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def get_all_unique_permutations(self, nums, nums_len, i):
        if i==nums_len:
            self.op.append(list(nums))
        else:
            self.visited_set[i].add(nums[i])
            self.get_all_unique_permutations(nums, nums_len, i+1)
            for j in range(i+1, nums_len):
                if nums[j] not in self.visited_set[i]:
                    self.visited_set[i].add(nums[j])
                    self.swap(nums, i, j)
                    self.get_all_unique_permutations(nums, nums_len, i+1)
                    self.swap(nums, i, j)
            self.visited_set[i].clear()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        self.visited_set = [set() for i in range(nums_len)]
        self.get_all_unique_permutations(nums, nums_len, 0)
        return self.op
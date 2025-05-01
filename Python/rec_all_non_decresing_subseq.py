# https://leetcode.com/problems/non-decreasing-subsequences
"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with
 at least two elements. You may return the answer in any order.

Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]

Constraints:
1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""

from sys import maxsize
from typing import List

class Solution:

    def get_all_subseq(self, nums, start, length, last_num, cur_op, cur_op_len, op_set):
        if start==length:
            return
        for i in range(start, length):
            if nums[i]>=last_num:
                cur_op.append(nums[i])
                if cur_op_len>=1:
                    op_set.add(tuple(cur_op))
                self.get_all_subseq(nums, i+1, length, nums[i], cur_op, cur_op_len+1, op_set)
                cur_op.pop()

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        op_set = set()
        self.get_all_subseq(nums, 0, nums_len, -maxsize, [], 0, op_set)
        return list(op_set)
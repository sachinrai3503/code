# https://leetcode.com/problems/reach-end-of-array-with-max-score
"""
You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices
 greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

Example 1:
Input: nums = [1,3,1,5]
Output: 7
Explanation:
First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:
Input: nums = [4,3,1,3,2]
Output: 16
Explanation:
Jump directly to the last index. The final score is 4 * 4 = 16.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
"""

from typing import List
from sys import maxsize

class Solution:

    # This is slow. Uses next greater number logic
    # O(n) time and mem.
    def findMaximumScore1(self, nums: List[int]) -> int:
        max_score = 0
        n = len(nums)
        op = [0 for i in range(n)]
        stck = list()
        for j in range(n):
            while stck and nums[stck[-1]]<=nums[j]:
                i = stck.pop()
                op[j] = max(op[j], (j-i)*nums[i] + op[i])
            stck.append(j)
        while stck:
            i = stck.pop()
            max_score = max(max_score, (n-1-i)*nums[i] + op[i])
        return max_score
    
    def findMaximumScore(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len<=0: return 0
        max_score = 0
        i = 0
        prev = nums[0]
        for j in range(1, len(nums)):
            if nums[j]>prev:
                max_score+=((j-i)*prev)
                prev = nums[j]
                i = j
        max_score+=((nums_len-1-i)*prev)
        return max_score
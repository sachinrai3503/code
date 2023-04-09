# https://leetcode.com/problems/longest-consecutive-sequence/
"""
Given an unsorted array of integers nums, return the length of the longest
 consecutive elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:
0 <= nums.length <= 104
-109 <= nums[i] <= 109

Follow up: Could you implement the O(n) solution?
"""

# C hash + Union find - arr_longest_consequtive_seq.c

from sys import maxsize

class Solution:
    def longestConsecutive2(self, nums: list[int]) -> int:
        nums.sort()
        # print(nums)
        prev = maxsize
        s, e = 0, -1
        t_s = maxsize
        for num in nums:
            if num==prev: continue
            elif num-1!=prev:
                t_s = num
            prev = num
            if num - t_s+1 > e-s+1:
                s = t_s
                e = num
        return e-s+1

    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        length = 0
        for num in nums_set:
            if num-1 not in nums_set:
                t_len = 1
                s = num + 1
                while s in nums_set:
                    t_len+=1
                    s+=1
                length = max(length, t_len)
        return length
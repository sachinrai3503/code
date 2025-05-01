# https://leetcode.com/problems/count-special-subsequences
"""
You are given an array nums consisting of positive integers.

A special subsequence is defined as a subsequence of length 4, represented by indices (p, q, r, s), 
 where p < q < r < s. This subsequence must satisfy the following conditions:
nums[p] * nums[r] == nums[q] * nums[s]

There must be at least one element between each pair of indices. In other words, q - p > 1, r - q > 1 and s - r > 1.
Return the number of different special subsequences in nums.
 
Example 1:
Input: nums = [1,2,3,4,3,6,1]
Output: 1

Explanation:
There is one special subsequence in nums.
(p, q, r, s) = (0, 2, 4, 6):
This corresponds to elements (1, 3, 3, 1).
nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3
nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3

Example 2:
Input: nums = [3,4,3,4,3,4,3,4]
Output: 3

Explanation:
There are three special subsequences in nums.
(p, q, r, s) = (0, 2, 4, 6):
This corresponds to elements (3, 3, 3, 3).
nums[p] * nums[r] = nums[0] * nums[4] = 3 * 3 = 9
nums[q] * nums[s] = nums[2] * nums[6] = 3 * 3 = 9
(p, q, r, s) = (1, 3, 5, 7):
This corresponds to elements (4, 4, 4, 4).
nums[p] * nums[r] = nums[1] * nums[5] = 4 * 4 = 16
nums[q] * nums[s] = nums[3] * nums[7] = 4 * 4 = 16
(p, q, r, s) = (0, 2, 5, 7):
This corresponds to elements (3, 3, 4, 4).
nums[p] * nums[r] = nums[0] * nums[5] = 3 * 4 = 12
nums[q] * nums[s] = nums[2] * nums[7] = 3 * 4 = 12

Constraints:
7 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""

from collections import Counter
from typing import List

class BIT:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
    
    def update(self, i, val = 1):
        while i<self.size:
            self.data[i]+=val
            i = i + (i&-i)
        
    def query(self, i):
        count = 0
        while i>0: # since update happens for end(q in p,q,r,s) so even with size==arr_len it is working. Else size==arr_len+1
            count+=self.data[i]
            i = i - (i&-i)
        return count
    
    def __repr__(self):
        return f'{self.data}'

class Solution:

    # p*r == q**s i:e p/q == s/r
    # This will timeout
    def numberOfSubsequences1(self, nums: List[int]) -> int:
        count = 0
        nums_len = len(nums)
        ratio_to_index_map = dict()
        i = 0
        for i in range(nums_len):
            p = nums[i]
            for j in range(i+2, nums_len):
                q = nums[j]
                p_by_q = p/q
                q_by_p = q/p
                if p_by_q not in ratio_to_index_map:
                    ratio_to_index_map[p_by_q] = BIT(nums_len)
                if q_by_p not in ratio_to_index_map:
                    ratio_to_index_map[q_by_p] = BIT(nums_len)
                p_by_q_bit = ratio_to_index_map.get(p_by_q)
                q_by_p_bit = ratio_to_index_map.get(q_by_p)
                count+=q_by_p_bit.query(i-2)
                p_by_q_bit.update(j)
        # print(f'{ratio_to_index_map=}')
        return count
    
    def numberOfSubsequences(self, nums: List[int]) -> int:
        count = 0
        nums_len = len(nums)
        ratio_count = Counter()
        for r in range(4, nums_len - 2):
            q = r-2
            for p in range(q-1):
                ratio_count[nums[p]/nums[q]]+=1
            for s in range(r+2, nums_len):
                count+=ratio_count[nums[s]/nums[r]]
        return count
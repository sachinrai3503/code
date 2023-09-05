# https://leetcode.com/problems/max-number-of-k-sum-pairs
"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and 
 remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

from typing import List

class Solution:

    # O(nlogn)
    def maxOperations_sort(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        nums.sort()
        count = 0
        i, j = 0, nums_len-1
        while i<j:
            t_sum = nums[i] + nums[j]
            if t_sum==k:
                i+=1
                j-=1
                count+=1
            elif t_sum>k:
                j-=1
            else: i+=1
        return count
    
    # O(n) using map
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_count_map = dict()
        count = 0
        for num in nums:
            b = k - num # a(here num) + b = k
            b_count = num_count_map.get(b, 0)
            if b_count==0:
                num_count_map[num] = num_count_map.get(num, 0) + 1
            else:
                count+=1
                num_count_map[b]=b_count-1
        return count
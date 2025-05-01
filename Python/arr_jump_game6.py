# https://leetcode.com/problems/jump-game-vi
"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps 
 forward without going outside the boundaries of the array. That is, you can jump
 from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum
 of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Example 1:
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:
Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:
Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0

Constraints:
1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
"""

import heapq
from sys import maxsize
from collections import deque
from typing import List

class Solution:

    # This is wrong. TC - nums = [0,-1,-2,-3,1], k=2
    def maxResult1(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        i = 0
        max_result = nums[i]
        while i<(nums_len-1):
            max_neg_num_index = -1
            j = i+1
            while j<nums_len and (j-i)<=k and nums[j]<0:
                if max_neg_num_index==-1 or nums[max_neg_num_index]<=nums[j]:
                    max_neg_num_index = j
                j+=1
            # print(f'{i=} {j=} {max_neg_num_index=}')
            if max_neg_num_index==-1: # no -ve number
                max_result+=nums[i+1]
                i+=1
            elif j<nums_len and (j-i)<=k: # has both -ve and positive
                max_result+=nums[j]
                i=j
            elif j==nums_len: # only -ve and can reach target
                max_result+=nums[j-1]
                i = j-1
            else: # only -ve number
                max_result+=nums[max_neg_num_index]
                i = max_neg_num_index
        return max_result
    
    # Works but slow
    def maxResult2(self, nums: List[int], k: int) -> int:
        max_result = -maxsize
        max_heap = [] # [(res, index),...]
        nums_len = len(nums)
        dp = [None for _ in range(nums_len)]
        for i in range(nums_len-1, -1, -1):
            while max_heap and max_heap[0][1]>(i+k):
                heapq.heappop(max_heap)
            t_result = 0 if not max_heap else -max_heap[0][0]
            dp[i] = nums[i] + t_result
            heapq.heappush(max_heap, [-dp[i], i])
        # print(f'{max_heap=}')
        return dp[0]
    
    def maxResult(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        que = deque() # [(index, result), ...]
        for i in range(nums_len-1, -1, -1):
            if que and que[0][0]>(i+k): # remove outside window entires
                que.popleft()
            result_i = nums[i] + (0 if not que else que[0][1])
            while que and que[-1][1]<=result_i:
                que.pop()
            que.append((i, result_i))
        return que[-1][1]
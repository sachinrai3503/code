# https://leetcode.com/problems/max-consecutive-ones-iii
"""
Given a binary array nums and an integer k, return the maximum number of
 consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
class Solution3:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_len = 0
        nums_len = len(nums)
        s = 0
        zero_count = 0
        i = 0
        while i<nums_len:
            if nums[i]==0: zero_count+=1
            while zero_count>k:
                if nums[s]==0: zero_count-=1
                s+=1
            if (i-s+1)>=max_len:
                max_len = (i-s+1)
            i+=1
        return max_len

# https://www.lintcode.com/problem/883
"""
Given a binary array, find the maximum number of consecutive 1s in this array if
 you can flip at most one 0.

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000.
Example
Example 1:
	Input:  nums = [1,0,1,1,0]
	Output:  4
	
	Explanation:
	Flip the first zero will get the the maximum number of consecutive 1s.
	After flipping, the maximum number of consecutive 1s is 4.

Example 2:
	Input: nums = [1,0,1,0,1]
	Output:  3
	
	Explanation:
	Flip each zero will get the the maximum number of consecutive 1s.
	After flipping, the maximum number of consecutive 1s is 3.
"""

from typing import (
    List,
)

class Solution2:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        max_len = 0
        nums_len = len(nums)
        s = 0
        zero_count = 0
        i = 0
        while i<nums_len:
            if nums[i]==0: zero_count+=1
            while zero_count>1:
                if nums[s]==0: zero_count-=1
                s+=1
            if (i-s+1)>=max_len:
                max_len = (i-s+1)
            i+=1
        return max_len

# https://leetcode.com/problems/max-consecutive-ones
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
 The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num==1:
                count+=1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)
        return max_count
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
"""
You may recall that an array arr is a mountain array if and only if:
    arr.length >= 3
    There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array nums​​​, return the minimum number of elements to remove to
 make nums​​​ a mountain array.

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, 
             making the array nums = [1,5,6,3,1].

Example 3:
Input: nums = [4,3,2,1,1,2,3,1]
Output: 4

Example 4:
Input: nums = [1,2,3,4,4,3,2,1]
Output: 1

Constraints:
3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
"""
class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        nums_len = len(nums)
        dp = [0 for i in range(nums_len)]
        max_inc_dec_len = 0
        # LIS from left to right
        for i in range(nums_len-1, -1, -1):
            num = nums[i]
            t_len = 0
            for j in range(i+1, nums_len):
                if nums[j]<num:
                    t_len = max(t_len, dp[j])
            dp[i] = t_len + 1
        # LIS from right to left
        for i in range(nums_len):
            num = nums[i]
            t_len = 0
            for j in range(i-1, -1, -1):
                if nums[j]<num:
                    t_len = max(t_len, dp[j])
            # Note - Since only increasing/decreasing is not a mountain checking below
            if dp[i]>1 and t_len>0:
                max_inc_dec_len = max(max_inc_dec_len, dp[i] + t_len)
            dp[i] = t_len + 1
        # print(dp)
        return nums_len - max_inc_dec_len
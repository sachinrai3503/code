# https://leetcode.com/problems/continuous-subarray-sum/
"""
Given a list of non-negative numbers and a target integer k, write a function
 to check if the array has a continuous subarray of size at least 2 that sums
  up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and 
             sums up to 42.
 
Constraints:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

class Solution:
    
    def handle_0s(self, ip_list, length):
        last_zero = 0
        i = 0
        while i<length:
            if ip_list[i]==0:
                if i==(last_zero+1): return True
                last_zero = i
            i+=1
        return False

    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        numsSize = len(nums)
        if numsSize<2: return False
        if k==1: return True
        if k==0: return self.handle_0s(nums, numsSize)
        rem_map = dict()
        t_sum = 0
        i = 0
        while i<numsSize:
            t_sum+=nums[i]
            if i>0 and t_sum%k==0: return True
            rem = t_sum%k
            if rem in rem_map:
                if rem_map[rem]!=(i-1): return True
            else: rem_map[rem] = i
            i+=1
        return False
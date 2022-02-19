# https://www.lintcode.com/problem/617/description
# https://leetcode.com/problems/maximum-average-subarray-ii
"""
Given an array with positive and negative numbers, find the maximum average\
 subarray which length should be greater or equal to given length k.

It's guaranteed that the size of the array is greater or equal to k.

Example 1:
Input:
[1,12,-5,-6,50,3]
3
Output:
15.667
Explanation:
 (-6 + 50 + 3) / 3 = 15.667

Example 2:
Input:
[5]
1
Output:
5.000
"""

from sys import maxsize

class Solution:
    
    def get_pre_sum(self, nums, length):
        pre_sum = [0 for i in range(length)]
        t_sum = 0
        for i in range(length):
            t_sum+=nums[i]
            pre_sum[i] = t_sum
        return pre_sum

    # This would time out. See below sol. using binary search + math.
    def maxAverage1(self, nums, k):
        length = len(nums)
        pre_sum = self.get_pre_sum(nums, length)
        max_avg = -maxsize
        for t_k in range(k, length+1):
            max_sum = -maxsize
            for i in range(t_k-1, length):
                max_sum = max(max_sum, pre_sum[i] - (0 if (i-t_k)<0 else pre_sum[i-t_k]))
            max_avg = max(max_avg, max_sum/t_k)
        return max_avg

    def find_min_max(self, nums, length):
        _min, _max = maxsize, -maxsize
        for num in nums:
            if num>_max: _max = num
            if num<_min: _min = num
        return _min, _max
   
    def find_subarr_with_avg(self, nums, length, k, avg):
        pre_sum = [0 for i in range(length)]
        min_sum = 0
        t_sum = 0
        for i in range(length):
            # (a1 + a2 + ... + ak)/k >= avg i:e (a1 + a2 + ... + ak - k*avg) >= 0
            t_sum+=(nums[i]-avg)
            pre_sum[i] = t_sum
            if i>=(k-1):
                if pre_sum[i]-min_sum>=0: return True
                min_sum = min(min_sum, pre_sum[i-k+1])
        return False

    # This is binary search + math
    def maxAverage(self, nums, k):
        length = len(nums)
        s, e = self.find_min_max(nums, length)
        while (s + 1e-6)<e:
            mid = s + (e-s)/2
            if self.find_subarr_with_avg(nums, length, k, mid):
                s = mid # Note unlike binary search not doing mid+1
            else:
                e = mid # Note unlike binary search not doing mid-1
        return s
    

# https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
# https://www.geeksforgeeks.org/smallest-subarray-from-a-given-array-with-sum-greater-than-or-equal-to-k-set-2
# https://leetcode.com/problems/minimum-size-subarray-sum/
"""
NOTE - Above links don't handle -ve integers.

Given an array of n positive integers and a positive integer s, find the minimal
 length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""

from sys import maxsize

class Solution:
    def minSubArrayLen(self, _sum: int, nums: list[int]) -> int:
        length = len(nums)
        max_len = maxsize
        t_sum = 0
        i, j = 0, 0
        while j<length:
            t_sum+=nums[j]
            if t_sum>=_sum:
                while i<=j and t_sum>=_sum:
                    t_sum-=nums[i]
                    i+=1
                if (j-i+2)<max_len:
                    max_len = j-i+2
            j+=1
        if max_len==maxsize: return 0
        return max_len

# https://www.geeksforgeeks.org/smallest-subarray-from-a-given-array-with-sum-greater-than-or-equal-to-k/
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""
NOTE - Above links handle cases where integers are -ve.
NOTE - For largest subarr see - list_largest_subarr_with_sum_greater_than_eq_to_k.py

Return the length of the shortest, non-empty, contiguous subarray of A with sum
 at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:
Input: A = [1], K = 1
Output: 1

Example 2:
Input: A = [1,2], K = 4
Output: -1

Example 3:
Input: A = [2,-1,2], K = 3
Output: 3
 

Note:
1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
"""

class Solution1:
    
    def get_floor(self, stck, num):
        floor = -1
        s, e = 0, len(stck)-1
        while s<=e:
            mid = s + (e-s)//2
            if stck[mid][0]<=num:
                floor = mid
                s = mid+1
            else:
                e = mid-1
        return floor if floor==-1 else stck[floor][1]
    
    def shortestSubarray(self, A: list[int], K: int) -> int:
        length = len(A)
        max_len = maxsize
        stck = list()
        t_sum = 0
        i = 0
        while i<length:
            t_sum+=A[i]
            if t_sum>=K and (i+1)<max_len:
                max_len = i+1
            floor = self.get_floor(stck, t_sum-K)
            if floor!=-1 and (i-floor)<max_len:
                max_len = i-floor
            while len(stck)>0 and stck[-1][0]>t_sum:
                stck.pop()
            stck.append([t_sum, i])
            i+=1
        return max_len if max_len!=maxsize else -1

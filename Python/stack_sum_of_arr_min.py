# https://leetcode.com/problems/sum-of-subarray-minimums
"""
Given an array of integers arr, find the sum of min(b), where b ranges over every
 (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        op = 0
        m = 10**9 + 7
        arr_len = len(arr)
        stck = list() # [(index, big_num_count_to_left), ...]
        for i in range(arr_len):
            num = arr[i]
            big_count = 0
            while stck and arr[stck[-1][0]]>=num:
                t_index, t_big_count = stck.pop()
                op = (op + arr[t_index]*(t_big_count+1)*(i-t_index))%m
                big_count+=(t_big_count+1)
            stck.append((i, big_count))
        while stck:
            t_index, t_big_count = stck.pop()
            op = (op + arr[t_index]*(t_big_count+1)*(arr_len-t_index))%m
        return op
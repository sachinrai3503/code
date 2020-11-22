# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
"""
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a
 (contiguous) subarray of length K and simultaneously changing every 0 in the 
 subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the 
array.  If it is not possible, return -1.

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].

Example 2:
Input: A = [1,1,0], K = 2
Output: -1

Example 3:
Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:

Note:
1 <= A.length <= 30000
1 <= K <= A.length
"""

class Solution:     
    def minKBitFlips(self, A: list[int], K: int) -> int:
        length = len(A)
        interval_marker = [0]*(length+1)
        active_interval_count = 0
        flip_count = 0
        for i in range(length):
            active_interval_count+=interval_marker[i]
            if A[i]== (active_interval_count)%2:
                active_interval_count+=1
                flip_count+=1
                if i+K<=length:
                    interval_marker[i+K] = -1
                else: return -1
        return flip_count
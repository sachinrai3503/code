# https://leetcode.com/problems/perfect-squares
"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, 
 it is the product of some integer with itself. For example, 1, 4, 9, and 16 are 
 perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 104
"""

from sys import maxsize

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [maxsize for i in range(n+1)]
        i = 1
        while (i*i)<=n:
            k = i*i
            j = k+1
            dp[k] = 1
            while j<=n:
                dp[j] = min(dp[j], 1 + dp[j-k])
                j+=1
            i+=1
        return dp[n]
# https://leetcode.com/problems/palindrome-partitioning-ii/
# https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1 

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.
"""

from sys import maxsize

class Solution:
    def minCut(self, s: str) -> int:
        s_len = len(s)
        dp = [maxsize for i in range(s_len)]
        is_palin = [False for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            prev = None
            for j in range(i, s_len):
                t_prev = is_palin[j]
                if s[i]==s[j]:
                    if i==j or (j-i)==1: is_palin[j] = True
                    elif prev: is_palin[j] = True
                    else: is_palin[j] = False
                else:
                    is_palin[j] = False
                prev = t_prev
                if is_palin[j]:
                    t_cuts = 0 if j==(s_len-1) else 1 + dp[j+1]
                    dp[i] = min(dp[i], t_cuts)
        return dp[0]
# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12
# https://leetcode.com/problems/longest-palindromic-subsequence/
"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
 deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 
Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_len = len(s)
        dp = [0 for i in range(s_len+1)]
        for i in range(s_len, -1, -1):
            prev = 0
            for j in range(s_len, -1, -1):
                t_prev = dp[j]
                if i==s_len or j==s_len: dp[j] = 0
                elif s[s_len-1-i]==s[j]: dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j+1], dp[j])
                prev = t_prev
        return dp[0]                    

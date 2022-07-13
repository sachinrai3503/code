# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""
Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        s_len = len(s)
        dp = [0 for i in range(s_len)]
        if s_len<=0: return 0
        for i in range(s_len-1, -1, -1):
            prev = 0
            for j in range(i, s_len):
                t_prev = dp[j]
                if j==i: dp[j] = 0
                elif s[i]==s[j]:
                    if j==i+1: dp[j] = 0
                    else: dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j-1], dp[j])
                prev = t_prev
        return dp[-1]
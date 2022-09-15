# https://leetcode.com/problems/palindrome-partitioning-iv/
"""
Given a string s, return true if it is possible to split the string s into three non-empty
 palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

Example 1:
Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

Example 2:
Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.

Constraints:
3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.
"""

class Solution:
    
    def get_palin_mat(self, s, s_len):
        is_palin = [[False for j in range(s_len)] for i in range(s_len)]
        for i in range(s_len-1,-1,-1):
            for j in range(i, s_len):
                if s[i]==s[j]:
                    if i==j or (j-i)==1: is_palin[i][j] = True
                    elif is_palin[i+1][j-1]: is_palin[i][j] = True
                    else: is_palin[i][j] = False
                else: is_palin[i][j] = False
        # print(is_palin)
        return is_palin
    
    # This will time out
    def checkPartitioning(self, s: str) -> bool:
        s_len = len(s)
        dp = [[False for j in range(s_len)] for i in range(2)]
        is_palin_dp = self.get_palin_mat(s, s_len)
        for k in range(0, 2): # K = 2, 3
            for i in range(s_len-1,-1,-1):
                for j in range(i, s_len):
                    if is_palin_dp[i][j]:
                        if j!=(s_len-1):
                            if k==0 and is_palin_dp[j+1][-1]: dp[k][i] = True
                            elif k==1 and dp[k-1][j+1]: dp[k][i] = True
                        if dp[k][i]: break
        return dp[k%2][0]
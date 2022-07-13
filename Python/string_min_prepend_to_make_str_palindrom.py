# https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/
# https://leetcode.com/problems/shortest-palindrome/
"""
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"

Constraints:
0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""

class Solution:
    
    def longestPalinSubstr(self, s, s_len):
        s_len = len(s)
        dp = [[0 for i in range(s_len)] for j in range(2)]
        for i in range(s_len-1, -1, -1):
            cur_row = (i%2)
            prev_row = 1 if cur_row==0 else 0
            for j in range(i, s_len):
                if i==j: dp[cur_row][j] = 1
                elif s[i]==s[j]:
                    if (j-i)==1: dp[cur_row][j] = 2
                    elif dp[prev_row][j-1]!=0 : dp[cur_row][j] = dp[prev_row][j-1] + 2
                    else: dp[cur_row][j] = 0
                else: dp[cur_row][j] = 0
            # print(dp[cur_row])
        return max(dp[0])
    
    def shortestPalindrome1(self, s: str) -> str:
        s_len = len(s)
        if s_len==0: return ''
        long_len_substr = self.longestPalinSubstr(s, s_len)
        return s[-1:long_len_substr-1:-1] + s
    
    def get_lps(self, s, s_len):
        lps = list()
        for i in range(s_len):
            j = i-1
            while j>=0 and s[lps[j]]!=s[i]:
                j = lps[j]-1
            if j==-1:
                lps.append(0)
            else:
                lps.append(lps[j]+1)
        # print(lps)
        return lps[-1]
                
    def shortestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len==0: return ''
        lps = self.get_lps(s +'$' +  s[::-1], s_len*2+1)
        if lps>=s_len: return s
        return s[-1:lps-1:-1] + s
# https://leetcode.com/problems/palindromic-substrings/
"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

 
Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings_dp(self, s: str) -> int:
        count = 0
        s_len = len(s)
        dp = [False for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            prev = False
            for j in range(i, s_len):
                t_prev = dp[j]
                if s[i]==s[j]:
                    if (j-i)<=1: dp[j] = True
                    else: dp[j] = prev
                else:
                    dp[j] = False
                count+=dp[j]
                prev = t_prev
        return count

    # No extra space
    def countSubstrings(self, s: str) -> int:
        count = 0
        s_len = len(s)
        i = 0
        for i in range(s_len):
            p, q = i, i
            while p>=0 and q<s_len and s[p]==s[q]:
                count+=1
                p-=1
                q+=1
            p, q = i, i+1
            while p>=0 and q<s_len and s[p]==s[q]:
                count+=1
                p-=1
                q+=1
        return count
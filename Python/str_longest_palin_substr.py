#https://leetcode.com/problems/longest-palindromic-substring/
"""
Given a string s, return the longest palindromic substring in s.
A string is called a palindrome string if the reverse of that string is the same as the original string.

 

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ts = -1
        s_len = len(s)
        for i in range(s_len):
            p, q = i, i
            while p>=0 and q<s_len and s[p]==s[q]:
                p-=1
                q+=1
            if (q-p-1)>max_len:
                max_len = q-p-1
                ts = p+1
            p, q = i, i+1
            while p>=0 and q<s_len and s[p]==s[q]:
                p-=1
                q+=1
            if (q-p-1)>max_len:
                max_len = q-p-1
                ts = p+1
        return s[ts:ts+max_len]
# https://leetcode.com/problems/valid-palindrome-ii
"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
 
Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""

class Solution:

    def is_palindrom(self, word, s, e):
        while s<e:
            if word[s]!=word[e]: return False
            s+=1
            e-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        s_len = len(s)
        i, j = 0, s_len-1
        while i<j:
            if s[i]!=s[j]:
                return self.is_palindrom(s, i+1, j) or self.is_palindrom(s, i, j-1)
            i+=1
            j-=1
        return True
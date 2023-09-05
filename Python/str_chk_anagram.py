# https://leetcode.com/problems/valid-anagram
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different
 word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt 
your solution to such a case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_count = [0 for i in range(26)]
        if s_len!=t_len: return False
        for char in s:
            s_count[ord(char)-97]+=1
        # print(f'{s_count=}')
        for char in t:
            char_index = ord(char)-97
            s_count[char_index]-=1
            if s_count[char_index]<0:
                return False
        for i in range(26):
            if s_count[i]!=0: return False
        return True
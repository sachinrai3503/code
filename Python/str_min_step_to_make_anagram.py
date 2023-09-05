# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram
"""
You are given two strings of the same length s and t. In one step you can choose 
 any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a
 different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 

Constraints:
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
"""

from typing import List

class Solution:

    def get_char_count(self, s, s_len) -> List[int]:
        count = [0 for i in range(26)]
        for char in s:
            count[ord(char)-97]+=1
        # print(f'{count=}')
        return count

    def minSteps(self, s: str, t: str) -> int:
        s_len = len(s)
        s_char_count = self.get_char_count(s, s_len)
        common_count = 0
        for char in t:
            char_index = ord(char)-97
            if s_char_count[char_index]>0:
                s_char_count[char_index]-=1
                common_count+=1
        return s_len - common_count
# https://leetcode.com/problems/permutation-in-string/
"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
 or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    
    def get_freq(self, s1, s1_len):
        _freq = [0 for i in range(26)]
        for s in s1:
            _freq[ord(s)-97]+=1
        return _freq
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_freq = self.get_freq(s1, s1_len)
        s2_freq = [0 for i in range(26)]
        # print(s1_freq)
        count = 0
        s, i = 0, 0
        while i<s2_len:
            i_index = ord(s2[i])-97
            s2_freq[i_index]+=1
            if s2_freq[i_index]<=s1_freq[i_index]:
                count+=1
            s_index = ord(s2[s])-97
            while s2_freq[s_index]>s1_freq[s_index]:
                s2_freq[s_index]-=1
                s+=1
                if s<=i:s_index = ord(s2[s])-97
                else: break
            if count==s1_len and (i-s+1)==s1_len:
                return True
            # print(s2_freq)
            i+=1
        return False
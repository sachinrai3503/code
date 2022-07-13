# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
"""
Given two strings s and part, perform the following operation on s until all 
 occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s and part consists of lowercase English letters.
"""

class Solution:
    
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
        return lps
    
    def kmp(self, text, pat:str):
        t_len = len(text)
        p_len = len(pat)
        lps = self.get_lps(pat, p_len)
        i, j = 0, 0
        while i<t_len:
            if text[i]==pat[j]:
                i+=1
                j+=1
            elif j==0:
                i+=1
            else:
                j = lps[j-1]
            if j==p_len:
                text = text[:i-p_len] + text[i:]
                t_len-=p_len
                i = 0
                j = 0
        # print(text)
        return text
    
    def removeOccurrences(self, s: str, part: str) -> str:
        return self.kmp(s, part)
        
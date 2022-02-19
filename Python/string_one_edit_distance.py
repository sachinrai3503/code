# https://www.lintcode.com/problem/640/
"""
Description
Given two strings S and T, determine if they are both one edit distance apart.
One ediit distance means doing one of these operation:
    insert one character in any position of S
    delete one character in S
    change one character in S to other character

Example
Example 1:
Input: s = "aDb", t = "adb" 
Output: true

Example 2:
Input: s = "ab", t = "ab" 
Output: false
Explanation:
s=t ,so they aren't one edit distance apart
"""
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        s_len, t_len = len(s), len(t)
        if abs(s_len-t_len)>1: return False
        diff = False
        if s_len==t_len:
            i, j = 0, 0
            while i<s_len and j<t_len:
                if s[i]!=t[j]:
                    if diff: return False
                    diff = True
                i+=1
                j+=1
        else:
            if s_len<t_len:
                s, t = t, s
                s_len, t_len = t_len, s_len
            i, j = 0, 0
            while i<s_len and j<t_len:
                if s[i]!=t[j]:
                    if diff: return False
                    diff = True
                else:
                    j+=1
                i+=1
            if not diff: return True # Case when last char is extra and other char match.
        return diff
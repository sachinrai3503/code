# https://leetcode.com/problems/is-subsequence
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
 by deleting some (can be none) of the characters without disturbing the relative
 positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" 
 while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
 and you want to check one by one to see if t has its subsequence. In this scenario,
 how would you change your code?
"""

class Solution:

    def get_ceil(self, arr, k):
        if arr is None: return None
        arr_len = len(arr)
        s, e = 0, arr_len-1
        ceil = None
        while s<=e:
            mid = (s+e)//2
            if arr[mid]>k:
                ceil = arr[mid]
                e = mid-1
            else:
                s = mid+1
        return ceil

    def get_char_indexs(self, s, s_len):
        char_indexs = dict()
        for i in range(s_len):
            index_list = char_indexs.get(s[i], [])
            index_list.append(i)
            char_indexs[s[i]] = index_list
        print(f'{char_indexs=}')
        return char_indexs

    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len>t_len: return False
        t_char_index = self.get_char_indexs(t, t_len)
        prev = -1
        for char in s:
            char_t_index = self.get_ceil(t_char_index.get(char, None), prev)
            if char_t_index is None: return False
            prev = char_t_index
        return True
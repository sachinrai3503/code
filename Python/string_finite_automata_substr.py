# https://leetcode.com/problems/implement-strstr/
# https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/
# https://www.geeksforgeeks.org/pattern-searching-set-5-efficient-constructtion-of-finite-automata/
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle
 is not part of haystack.

For the purpose of this problem, we will return 0 when needle is an empty string.
 This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""

class Solution:
    
    def get_finite_automata(self, pat, pat_len, char_set_count=26):
        TA = [[0 for j in range(char_set_count)] for i in range(pat_len+1)]
        lps = 0
        TA[0][ord(pat[0])-97] = 1
        for i in range(1, pat_len+1):
            for j in range(char_set_count):
                TA[i][j] = TA[lps][j]
            if i<pat_len:
                TA[i][ord(pat[i])-97] = i+1
                lps = TA[lps][ord(pat[i])-97]
        # print('lps', lps)
        # print(TA)
        return TA
        
    def strStr(self, haystack: str, needle: str) -> int:
        txt_len = len(haystack)
        pat_len = len(needle)
        if pat_len==0: return 0
        if txt_len==0: return -1
        TA = self.get_finite_automata(needle, pat_len, 26)
        cur_state = 0
        for i in range(txt_len):
            cur_state = TA[cur_state][ord(haystack[i])-97]
            if cur_state==pat_len:
                # print('occuring at', i-pat_len+1)
                return i-pat_len+1
        return -1
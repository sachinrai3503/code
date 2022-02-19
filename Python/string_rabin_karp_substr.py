# https://leetcode.com/problems/implement-strstr/
# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/
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

# Below implementation is Rabin-Karp substr method.

class Solution:
    
    # Assumes len(text)>=len(pat)
    def compare(self, text, start, pat, pat_len):
        j = start
        i = 0
        while i<pat_len and text[j]==pat[i]:
            i+=1
            j+=1
        return i==pat_len
    
    # Assumes len(txt)>=txt_len
    def get_hash(self, txt, txt_len, d, q):
        _hash = 0
        for i in range(txt_len):
            _hash = (_hash*d + (ord(txt[i])-97))%q
        return _hash
    
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m==0: return 0
        if n<m: return -1
        d = 26 # count of letters
        q = 17 # prime number
        h = (d**(m-1))%q
        s = self.get_hash(haystack, m, d, q) # initial hash of haystack
        p = self.get_hash(needle, m, d, q) # hash of needle
        for i in range(m-1, n):
            if s==p:
                if self.compare(haystack, i-m+1, needle, m):
                    return i-m+1
            s = s - (ord(haystack[i-m+1])-97)*h
            if i!=(n-1): s = (s*d + (ord(haystack[i+1])-97))%q
        return -1
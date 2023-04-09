# https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
"""
Given two strings needle and haystack, return the index of the first occurrence
 of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:

    def z_function(self, s, s_len):
        z = [None] # z[0] will always be == s_len as entire string is prefix of itself
        l, r = 0, 0
        for i in range(1, s_len):
            if i>r:
                l, r = i, i
                while r<s_len and s[r-l]==s[r]:
                    r+=1
                z.append(r-l)
                # print(f'{i=}')
                r-=1
            else:
                k = i-l
                if z[k]<(r-i+1):
                    z.append(z[k])
                    # print(f'{i=}')
                else:
                    l = i
                    while r<s_len and s[r-l]==s[r]:
                        r+=1
                    z.append(r-l)
                    r-=1
                    # print(f'{i=}')
        # print(f'{z=}')
        return z

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)
        z_str = needle + '$' + haystack
        z_len = haystack_len+needle_len+1
        z_arr = self.z_function(z_str, z_len)
        # print(f'{z_str=} {z_len=}')
        for i in range(z_len):
            if z_arr and z_arr[i]==needle_len:
                # print(f'{(i-needle_len-1)=}')
                return i-needle_len-1
        return -1
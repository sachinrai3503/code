# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
"""
Given a binary string s and a positive integer n, return true if the binary
 representation of all the integers in the range [1, n] are substrings of s,
 or false otherwise.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "0110", n = 3
Output: true

Example 2:
Input: s = "0110", n = 4
Output: false

Constraints:
1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= n <= 109
"""

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        num_set = set()
        len_s = len(s)
        count = 0
        for i in range(len_s):
            if s[i]=='0': continue
            t_num = 0
            for j in range(i, len_s):
                t_num = t_num*2 + int(s[j])
                # print(i, j, t_num, count)
                if t_num not in num_set and 1<=t_num<=n:
                    count+=1
                    num_set.add(t_num)
                elif t_num>n: break
            if count==n: return True
        return False
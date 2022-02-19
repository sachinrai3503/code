# https://leetcode.com/problems/interleaving-string/
"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided
 into non-empty substrings such that:
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    
 The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""
class Solution:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s3_len!=s1_len+s2_len: return False
        dp = [False for i in range(s2_len+1)]
        for i in range(s1_len, -1, -1):
            s1_count = s1_len - i
            for j in range(s2_len, -1, -1):
                # print(i, j, dp)
                if i==s1_len and j==s2_len: dp[j] = True
                else:
                    s2_count = s2_len - j
                    s3_char = s3[-(s1_count+s2_count)]
                    s1_match = False if i==s1_len else s3_char==s1[i]
                    s2_match = False if j==s2_len else s3_char==s2[j]
                    if s1_match and s2_match: dp[j] = dp[j] or dp[j+1]
                    elif s1_match: pass
                    elif s2_match: dp[j] = dp[j+1]
                    else: dp[j] = False
        return dp[0]
                    
    def check(self, s1, s1_len, s2, s2_len, s3, s3_len, i, j, k):
        if k==s3_len: return i==s1_len and j==s2_len
        char_s3 = s3[k]
        if i<s1_len and j<s2_len and char_s3==s1[i] and char_s3==s2[j]:
            return self.check(s1, s1_len, s2, s2_len, s3, s3_len, i+1, j, k+1) or \
                    self.check(s1, s1_len, s2, s2_len, s3, s3_len, i, j+1, k+1)
        elif i<s1_len and char_s3==s1[i]:
            return self.check(s1, s1_len, s2, s2_len, s3, s3_len, i+1, j, k+1)
        elif j<s2_len and char_s3==s2[j]:
            return self.check(s1, s1_len, s2, s2_len, s3, s3_len, i, j+1, k+1)
        else:
            return False
            
    
    # This would time out
    def isInterleave_rec(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s3_len!=s1_len+s2_len: return False
        return self.check(s1, s1_len, s2, s2_len, s3, s3_len, 0, 0, 0)
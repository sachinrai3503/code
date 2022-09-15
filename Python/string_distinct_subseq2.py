# https://leetcode.com/problems/distinct-subsequences-ii
"""
Given a string s, return the number of distinct non-empty subsequences of s. 
Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string
 by deleting some (can be none) of the characters without disturbing the relative
 positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while
 "aec" is not.
 

Example 1:
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 
Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters.
"""

class Solution:
    
    def __init__(self):
        self.visited = set()
    
    def generate_unique_subseq(self, s, s_len, i, op):
        # print(f'{i=}, {op=}')
        if i==s_len: return
        for j in range(i, s_len):
            op.append(s[j])
            t_op = ''.join(op)
            self.visited.add(t_op)
            # print(self.visited)
            self.generate_unique_subseq(s, s_len, j+1, op)
            op.pop()
    
    def distinctSubseqII_rec(self, s: str) -> int:
        s_len = len(s)
        op = list()
        self.generate_unique_subseq(s, s_len, 0, op)
        # print(self.visited)
        return len(self.visited)
    
    # DP way
    def distinctSubseqII(self, s: str) -> int:
        s_len = len(s)
        recent_index = dict()
        dp = [0 for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            char = s[i]
            last_index = recent_index.get(char, None)
            if last_index is None:
                dp[i] = 1 + (0 if i==(s_len-1) else dp[i+1]*2)
            else:
                dp[i] = 2*dp[i+1] - (0 if last_index==(s_len-1) else dp[last_index+1])
            dp[i]%=1000000007
            recent_index[char] = i
            # print(dp[i:], recent_index)
        return dp[0]
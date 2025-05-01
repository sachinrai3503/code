# https://leetcode.com/problems/palindrome-partitioning/
"""
Given a string s, partition s such that every substring of the partition is a palindrome.
 Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward. 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s_len = len(s)
        op = [list() for i in range(s_len)]
        dp = [False for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            prev = False
            for j in range(i, s_len):
                cur_result = False
                if s[i]==s[j] and ((j-i)<2 or prev):
                    sub_str = s[i:j+1]
                    other_sub_str_list = op[j+1] if j<(s_len-1) else []
                    if not other_sub_str_list:
                        op[i].append([sub_str])
                    else:
                        for other_sub_str in other_sub_str_list:
                            op[i].append([sub_str] + other_sub_str)
                    cur_result = True
                prev = dp[j]
                dp[j] = cur_result
            # print(f'{dp=}')
            # print(f'{op=}')
        return op[0]


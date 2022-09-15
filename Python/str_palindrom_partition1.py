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

class Solution:
    
    def get_all_palindrom_partition(self, s, s_len, dp, index, cur_op, op):
        if index==s_len:
            op.append(list(cur_op))
            return
        for partition_index in dp[index]:
            cur_op.append(s[index:partition_index+1])
            self.get_all_palindrom_partition(s, s_len, dp, partition_index+1, cur_op, op)
            cur_op.pop()
    
    def partition(self, s: str) -> list[list[str]]:
        op = list()
        s_len = len(s)
        dp = [list() for i in range(s_len)]
        is_palin = [False for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            prev = None
            for j in range(i, s_len):
                t_prev = is_palin[j]
                if s[i]==s[j]:
                    if i==j or (j-i)==1: is_palin[j] = True
                    elif prev: is_palin[j] = True
                    else: is_palin[j] = False
                else:
                    is_palin[j] = False
                prev = t_prev
                if is_palin[j]: dp[i].append(j)
        self.get_all_palindrom_partition(s, s_len, dp, 0, list(), op)
        return op

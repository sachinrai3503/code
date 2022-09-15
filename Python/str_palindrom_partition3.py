# https://leetcode.com/problems/palindrome-partitioning-iii/
"""
You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

Example 1:
Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2:
Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.

Example 3:
Input: s = "leetcode", k = 8
Output: 0
 
Constraints:
1 <= k <= s.length <= 100.
s only contains lowercase English letters.
"""

from sys import maxsize

class Solution:
    
    def get_min_replacement_to_make_palindrom(self, s, s_len):
        dp = [[None for j in range(s_len)] for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            for j in range(i, s_len):
                if s[i]==s[j]:
                    if i==j or (j-i)==1: dp[i][j] = 0
                    else: dp[i][j] = 0 + dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + (dp[i+1][j-1] if (j-i)>1 else 0)
        # print(dp)
        return dp
    
    def palindromePartition(self, s: str, k: int) -> int:
        s_len = len(s)
        min_replacement_for_palindrom = self.get_min_replacement_to_make_palindrom(s, s_len)
        if k==1: return min_replacement_for_palindrom[0][s_len-1]
        dp = [[None for j in range(s_len)] for i in range(2)]
        for t_k in range(2, k+1):
            cur_row = (t_k)%2
            prev_row = 1 if cur_row==0 else 0
            for i in range(s_len-1, -1, -1):
                temp = maxsize
                for j in range(i, s_len):
                    t_replacement = min_replacement_for_palindrom[i][j]
                    if t_k==2:
                        if j!=(s_len-1): t_replacement+=min_replacement_for_palindrom[j+1][-1]
                        else: t_replacement = s_len+1 # value>=s_len+1 represents maxsize
                    else:
                        if j!=(s_len-1): t_replacement+=(dp[prev_row][j+1])
                        else: t_replacement = s_len+1 # value>=s_len+1 represents maxsize
                    temp = min(temp, t_replacement)
                dp[cur_row][i] = temp
        return dp[k%2][0]
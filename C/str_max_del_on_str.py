# https://leetcode.com/problems/maximum-deletions-on-a-string
"""
You are given a string s consisting of only lowercase English letters. In one
 operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the 
 following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first
 two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.

Example 1:
Input: s = "abcabcdabc"
Output: 2
Explanation:
- Delete the first 3 letters ("abc") since the next 3 letters are equal. Now, s = "abcdabc".
- Delete all the letters.
We used 2 operations so return 2. It can be proven that 2 is the maximum number of operations needed.
Note that in the second operation we cannot delete "abc" again because the next
 occurrence of "abc" does not happen in the next 3 letters.

Example 2:
Input: s = "aaabaab"
Output: 4
Explanation:
- Delete the first letter ("a") since the next letter is equal. Now, s = "aabaab".
- Delete the first 3 letters ("aab") since the next 3 letters are equal. Now, s = "aab".
- Delete the first letter ("a") since the next letter is equal. Now, s = "ab".
- Delete all the letters.
We used 4 operations so return 4. It can be proven that 4 is the maximum number 
 of operations needed.

Example 3:
Input: s = "aaaaa"
Output: 5
Explanation: In each operation, we can delete the first letter of s.

Constraints:
1 <= s.length <= 4000
s consists only of lowercase English letters.
"""

class Solution:

    def is_match(self, s, s_len, i, j, word_count):
        for k in range(word_count):
            if s[i+k]!=s[j+k]: return False
        return True  

    # Gets TLE
    def get_max_oper_count(self, s, s_len):
        dp = [[None for j in range(s_len)] for i in range(s_len)] # dp[i][j] = hash of s[i:j+1]
        oper_count = [0 for i in range(s_len)]
        d = 26
        q = 10**7 + 7
        for i in range(s_len-1, -1, -1):
            cur_hash = 0
            t_oper_count = 1 # as entire string can be removed in 1 operation
            for j in range(i, s_len):
                word_count = j-i+1
                next_index = j+1
                cur_hash = (cur_hash*d + (ord(s[j])-96))%q
                if next_index<s_len and (j+word_count)<s_len:
                    if dp[next_index][j+word_count]==cur_hash and self.is_match(s, s_len, i, next_index, word_count):
                        t_oper_count = max(t_oper_count, 1+oper_count[next_index])
                dp[i][j] = cur_hash
            oper_count[i] = t_oper_count
        # print(f'{oper_count=}')
        return oper_count[0]

    def deleteString(self, s: str) -> int:
        return self.get_max_oper_count(s, len(s))
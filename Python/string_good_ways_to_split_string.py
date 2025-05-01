# https://leetcode.com/problems/number-of-good-ways-to-split-a-string
"""
A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal
 to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.

Return the number of good splits you can make in s.

Example 1:
Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good. 
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Example 2:
Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
 

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""

class Solution:

    def get_first_last_index(self, s, s_len):
        first_index, last_index = {}, {}
        unique_char = 0
        for i in range(s_len):
            c = s[i]
            if c not in first_index:
                first_index[c] = i
                unique_char+=1
            last_index[c] = i
        return first_index, last_index, unique_char

    def numSplits(self, s: str) -> int:
        count = 0
        s_len = len(s)
        first_index, last_index, distinct_char_count = self.get_first_last_index(s, s_len)
        l, r = 0, distinct_char_count
        for i in range(s_len):
            c = s[i]
            c_first_index, c_last_index = first_index[c], last_index[c]
            if c_first_index==i:
                l+=1
            if c_last_index==i:
                r-=1
            if l==r:
                count+=1
        return count
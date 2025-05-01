# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings
"""
Given a string s, return the maximum number of unique substrings that the given string can be
 split into.

You can split string s into any list of non-empty substrings, where the concatenation 
 of the substrings forms the original string. However, you must split the substrings 
 such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. 
 Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

Constraints:
1 <= s.length <= 16
s contains only lower case English letters.
"""

from sys import maxsize

class Solution:

    def split_string(self, s, s_len, i, count):
        if count + (s_len-i)<=self.max_count:
            return -maxsize
        if i==s_len:
            return count
        for j in range(i, s_len):
            sub_str = s[i:j+1]
            if sub_str not in self.visited:
                self.visited.add(sub_str)
                self.max_count = max(self.max_count, self.split_string(s, s_len, j+1, count+1))
                self.visited.remove(sub_str)
        return self.max_count

    def maxUniqueSplit(self, s: str) -> int:
        s_len = len(s)
        self.visited = set()
        self.max_count = 0
        return self.split_string(s, s_len, 0, 0)
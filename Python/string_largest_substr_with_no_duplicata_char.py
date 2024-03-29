# https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, ip: str) -> int:
        op = dict()
        s, e = 0, -1
        ts = 0
        i = 0
        while i<len(ip):
            previous_index = op.get(ip[i], -1)
            if (ts<=previous_index<i):
                ts = previous_index+1
            else:
                op[ip[i]] = i
                if (i-ts+1)>(e-s+1):
                    s, e = ts, i
                i+=1
        # print(ip[s:e+1])
        return e-s+1
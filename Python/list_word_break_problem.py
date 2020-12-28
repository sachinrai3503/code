# https://leetcode.com/problems/word-break/
# https://www.geeksforgeeks.org/word-break-problem-dp-32/

"""
Given a non-empty string s and a dictionary wordDict containing a list of
 non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dict_set = set(wordDict)
        print(dict_set)
        length = len(s)
        op = [-1]*length
        last_occ = length
        for i in range(length-1, -1, -1):
            temp = last_occ
            while temp != length and s[i:temp] not in dict_set:
                temp = op[temp]
            if s[i:temp] in dict_set:
                op[i] = last_occ
                last_occ = i
            else:
                op[i] = -1
        print(op)
        return length == 0 or op[0] != -1

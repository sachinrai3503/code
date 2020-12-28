# https://leetcode.com/problems/word-break-ii/
# https://www.geeksforgeeks.org/word-break-problem-dp-32-set-2/
# https://www.geeksforgeeks.org/word-break-problem-using-backtracking/
"""
Given a non-empty string s and a dictionary wordDict containing a list of
 non-empty words, add spaces in s to construct a sentence where each word
is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


class Solution:

    def get_word_break(self, s, op, s_index, word_break_list, word_break):
        if s_index == len(s):
            word_break_list.append(' '.join(word_break))
            return
        if op[s_index] == None:
            return
        for i in op[s_index]:
            word_break.append(s[s_index:i])
            self.get_word_break(s, op, i, word_break_list, word_break)
            word_break.pop()

    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        length = len(s)
        # dict_set = set(wordDict)
        op = [None]*length
        next_index_arr = [-1]*length
        last_occ = length
        for i in range(length-1, -1, -1):
            temp = last_occ
            while temp != length:
                if s[i:temp] in wordDict:
                    next_index_arr[i] = last_occ
                    if op[i] is None:
                        op[i] = list()
                    op[i].append(temp)
                temp = next_index_arr[temp]
            if s[i:temp] in wordDict:
                next_index_arr[i] = last_occ
                if op[i] is None:
                    op[i] = list()
                op[i].append(temp)
            if next_index_arr[i] != -1:
                last_occ = i
        # print(op)
        # print(next_index_arr)
        word_break_list = list()
        self.get_word_break(s, op, 0, word_break_list, list())
        return word_break_list

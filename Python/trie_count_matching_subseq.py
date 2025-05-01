# https://leetcode.com/problems/number-of-matching-subsequences
"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters 
 (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""

from collections import defaultdict
from sys import maxsize
from typing import List

class TrieCell:
    def __init__(self, char, is_end_node = False):
        self.char = char
        self.is_end_node = is_end_node
        self.child = None
        self.count = 0
    
    def print_cell(self, op):
        op.append(self.char)
        if self.is_end_node:
            print(f"{''.join(op)} {self.count=}")
        if self.child:
            self.child.print_node(op)
        op.pop()

class TrieNode:
    def __init__(self, size = 26):
        self.size = size
        self.data = [None for i in range(size)]
    
    def print_node(self, op):
        for i in range(self.size):
            if self.data[i] is None: continue
            self.data[i].print_cell(op)

class Trie:
    def __init__(self):
        self.root = None
    
    def _insert_word_in_trie(self, root, word, word_len, index):
        if index==word_len: return root
        if root is None:
            root = TrieNode()
        char = word[index]
        char_index = ord(char)-97
        cell = root.data[char_index]
        if cell is None:
            cell = TrieCell(char, index==word_len-1)
            root.data[char_index] = cell
        if index==word_len-1:
            cell.is_end_node = True
            cell.count+=1
        cell.child = self._insert_word_in_trie(cell.child, word, word_len, index+1)
        return root

    def insert_word(self, word):
        self.root = self._insert_word_in_trie(self.root, word, len(word), 0)
    
    def print_trie(self):
        self.root.print_node(list())


class Solution:

    def get_ceil(self, arr, k):
        arr_len = len(arr)
        s, e = 0, arr_len-1
        _ceil = arr_len
        while s<=e:
            mid = s + (e-s)//2
            if arr[mid]>k:
                _ceil = mid
                e = mid-1
            else:
                s = mid+1
        return None if _ceil==arr_len else arr[_ceil]

    # Will take lot of time
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        count = 0
        s_len = len(s)
        words_len = len(words)
        char_index_map = defaultdict(list)
        for i in range(s_len):
            char_index_map[s[i]].append(i)
        # print(f'{char_index_map=}')
        for word in words:
            char_index_in_s = -1
            for char in word:
                char_index_in_s = self.get_ceil(char_index_map[char], char_index_in_s)
                # print(f'{word=} {char=} {char_index_in_s=}')
                if char_index_in_s is None: break
            else:
                count+=1
        return count
    
    def get_next_index(self, start_from, target):
        for i in range(start_from, self.s_len):
            if self.s[i]==target: return i
        return None

    def count_matching_seq(self, root, prev_index):
        count = 0
        if root is None: return count
        for i in range(root.size):
            cell = root.data[i]
            if cell is None: continue
            char = cell.char
            # char_index = self.get_next_index(prev_index+1, char)
            char_index = self.get_ceil(self.char_index_map[char], prev_index)
            if char_index is None: continue
            if cell.is_end_node:
                count+=cell.count
            count+=self.count_matching_seq(cell.child, char_index)
        return count

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        self.s = s
        self.s_len = len(s)
        self.char_index_map = defaultdict(list)
        trie = Trie()
        for i in range(self.s_len):
            self.char_index_map[s[i]].append(i)
        # print(f'{self.char_index_map=}')
        for word in words:
            trie.insert_word(word)
        # trie.print_trie()
        return self.count_matching_seq(trie.root, -1)
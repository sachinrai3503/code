# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
"""
You are given two string arrays, queries and dictionary. All words in each array 
 comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any
 other letter. Find all words from queries that, after a maximum of two edits, equal
 some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary
 after a maximum of two edits. Return the words in the same order they appear in queries.

Example 1:
Input: queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
Output: ["word","note","wood"]
Explanation:
- Changing the 'r' in "word" to 'o' allows it to equal the dictionary word "wood".
- Changing the 'n' to 'j' and the 't' to 'k' in "note" changes it to "joke".
- It would take more than 2 edits for "ants" to equal a dictionary word.
- "wood" can remain unchanged (0 edits) and match the corresponding dictionary word.
Thus, we return ["word","note","wood"].

Example 2:
Input: queries = ["yes"], dictionary = ["not"]
Output: []
Explanation:
Applying any two edits to "yes" cannot make it equal to "not". Thus, we return an empty array.

Constraints:
1 <= queries.length, dictionary.length <= 100
n == queries[i].length == dictionary[j].length
1 <= n <= 100
All queries[i] and dictionary[j] are composed of lowercase English letters.
"""

from typing import List

class TrieCell:
    def __init__(self, data, child_node = None, is_last_cell = False):
        self.data = data
        self.child_node = child_node
        self.is_last_cell = is_last_cell

    def print_cell(self, op):
        op.append(self.data)
        if self.is_last_cell:
            print(''.join(op))
        else: self.child_node.print_node(op)
        op.pop()

class TrieNode:
    node_size = 26
    def __init__(self, node_size = 26):
        self.cells = [None for i in range(node_size)]
        self.node_size = node_size

    def print_node(self, op):
        for i in range(self.node_size):
            if self.cells[i]:
                self.cells[i].print_cell(op)
                
    def insert_in_trie_node(root, word, word_len, index):
        if index>=word_len: return root
        if root is None: root = TrieNode(TrieNode.node_size)
        char = word[index]
        char_index = ord(char) - 97
        if not root.cells[char_index]: root.cells[char_index] = TrieCell(char)
        trie_cell = root.cells[char_index]
        if index==(word_len-1): 
            trie_cell.is_last_cell = True
        trie_cell.child_node = TrieNode.insert_in_trie_node(trie_cell.child_node, word, word_len, index+1)
        return root

    def search_with_2_edits(root, word, word_len, index, cur_edit):
        if cur_edit>2: return False
        if index==word_len: return True
        if not root: return False
        char = word[index]
        char_index = ord(char) - 97
        trie_cell = root.cells[char_index]
        if trie_cell: # Need no edit
            if TrieNode.search_with_2_edits(trie_cell.child_node, word, word_len, index+1, cur_edit):
                return True
        # Needs edit
        for i in range(TrieNode.node_size):
            if not root.cells[i]: continue
            if TrieNode.search_with_2_edits(root.cells[i].child_node, word, word_len, index+1, cur_edit+1):
                return True
        return False
                
class Trie:
    def __init__(self):
        self.root = None
    
    def insert_in_trie(self, word):
        self.root = TrieNode.insert_in_trie_node(self.root, word, len(word), 0)
    
    def search_in_trie_with_2_edit(self, word):
        return TrieNode.search_with_2_edits(self.root, word, len(word), 0, 0)
    
    def print_trie(self):
        if self.root: self.root.print_node([])
        else: print('Trie is empty')


class Solution:
    
    # Below is using Trie
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        op = list()
        trie = Trie()
        for word in dictionary:
            trie.insert_in_trie(word)
        # trie.print_trie()
        for word in queries:
            if trie.search_in_trie_with_2_edit(word):
                op.append(word)
        return op
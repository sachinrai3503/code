# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
"""
Given a list of folders folder, return the folders after removing all sub-folders in those folders.
  You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j]
 must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not
 a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase 
 English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:
1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.
"""

from typing import List

class TrieCell:
    def __init__(self, word, is_end = False):
        self.word = word
        self.is_end = is_end
        self.child = None
    
    def print_cell(self, op):
        op.append(self.word)
        if self.is_end:
            print('/'.join(op))
        if self.child:
            self.child.print_node(op)
        op.pop()

class TrieNode:
    def __init__(self):
        self.size = 0
        self.data = dict()
    
    def print_node(self, op):
        for item in self.data:
            self.data[item].print_cell(op)

class Trie:
    def __init__(self):
        self.root = None

    def _insert_in_trie(self, root, word_list, word_list_len, index):
        if index==word_list_len: return root
        if not root:
            root = TrieNode()
        word = word_list[index]
        cell = root.data.get(word, None)
        if not cell:
            cell = TrieCell(word, index==(word_list_len-1))
            root.data[word] = cell
        if index==(word_list_len-1):
            cell.is_end = True
        if cell.is_end:
            return root # NOTE this step
        cell.child = self._insert_in_trie(cell.child, word_list, word_list_len, index+1)
        return root

    def insert_word(self, word_list):
        self.root = self._insert_in_trie(self.root, word_list, len(word_list), 0)

    def print_Trie(self):
        if self.root:
            op = list()
            self.root.print_node(op)

class Solution:

    def filter_subfolder(self, root, op):
        if not root: return
        for key in root.data:
            op.append(key)
            cell = root.data[key]
            if cell.is_end:
                self.op.append('/'.join(op))
            else:
                self.filter_subfolder(cell.child, op)
            op.pop()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.op = list()
        trie = Trie()
        for item in folder:
            dirs = item.split('/')
            # print(f'{dirs=}')
            trie.insert_word(dirs)
        # trie.print_Trie()
        self.filter_subfolder(trie.root, list())
        return self.op
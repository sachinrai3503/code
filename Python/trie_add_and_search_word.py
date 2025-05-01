# https://leetcode.com/problems/design-add-and-search-words-data-structure
"""
Design a data structure that supports adding new words and finding if a string matches 
 any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or
 false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class TrieCell:
    def __init__(self, data, is_last_node = False):
        self.data = data
        self.is_last_node = is_last_node
        self.child = None

    def print_cell(self, op):
        op.append(self.data)
        if self.is_last_node:
            print(''.join(op))
        if self.child:
            self.child.print_node(op)
        op.pop()

class TrieNode:
    def __init__(self, size = 26):
        self.size = size
        self.data = [None for i in range(size)]
    
    def add_data_to_node(root, word, word_len, i):
        if i==word_len: return root
        if root is None:
            root = TrieNode()
        char = word[i]
        char_index = ord(char)-97
        char_cell = root.data[char_index]
        if char_cell is None:
            char_cell = TrieCell(char)
            root.data[char_index] = char_cell
        if not char_cell.is_last_node:
            char_cell.is_last_node = (i==(word_len-1))
        char_cell.child = TrieNode.add_data_to_node(char_cell.child, word, word_len, i+1)
        return root

    def search_word(root, word, word_len, i):
        if i==word_len: return True
        if root is None: return False
        char = word[i]
        if char != '.':
            char_index = ord(char)-97
            char_cell = root.data[char_index]
            if char_cell is None: return False
            if i==(word_len-1): return char_cell.is_last_node
            return TrieNode.search_word(char_cell.child, word, word_len, i+1)
        else:
            for j in range(root.size):
                if root.data[j] is not None:
                    if i==(word_len-1): 
                        if root.data[j].is_last_node: return True
                    elif TrieNode.search_word(root.data[j].child, word, word_len, i+1):
                        return True
        return False

    def print_node(self, op):
        for i in range(self.size):
            if self.data[i]:
                self.data[i].print_cell(op)
    
class Trie:
    def __init__(self):
        self.root = None
    
    def add_word_to_trie(self, word):
        self.root = TrieNode.add_data_to_node(self.root, word, len(word), 0)

    def search_word_in_trie(self, word):
        return TrieNode.search_word(self.root, word, len(word), 0)
    
    def print_trie(self):
        if self.root:
            self.root.print_node(list())
        else:
            print('Empty')

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add_word_to_trie(word)

    def search(self, word: str) -> bool:
        return self.trie.search_word_in_trie(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
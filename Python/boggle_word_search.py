# https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters
# https://www.geeksforgeeks.org/boggle-set-2-using-trie/
# https://leetcode.com/problems/word-search-ii/
"""
Given a dictionary, a method to do a lookup in the dictionary and a M x N board 
where every cell has one character. Find all possible words that can be formed 
by a sequence of adjacent characters. Note that we can move to any of 8 adjacent
 characters, but a word should not have multiple instances of the same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G', 'I', 'Z'},
                       {'U', 'E', 'K'},
                       {'Q', 'S', 'E'}};

Output: Following words of the dictionary are present
         GEEKS
         QUIZ
"""

class TrieCell:
    def __init__(self, char, is_end_cell = False, next = None):
        self.char = char
        self.is_end_cell = is_end_cell
        self.next = next
    
    def print_trie_cell(self, op:list):
        op.append(self.char)
        if self.next is None: print(op)
        else: 
            if self.is_end_cell: print(op)
            self.next.print_trie_node(op)
        op.pop()

class TrieNode:
    def __init__(self, size = 26):
        self.cells = [None for i in range(size)]
        self.size = size
        self.active_cells_count = 0

    def print_trie_node(self, op:list):
        for i in range(self.size):
            if self.cells[i] is not None:
                self.cells[i].print_trie_cell(op)

class Trie:
    def __init__(self, max_depth):
        self.root = None
        self.max_depth = max_depth
        
    def print_trie(self):
        if self.root is None: print('Empty')
        else: self.root.print_trie_node(list())
    
    def insert_in_trie(self):
        pass
    
    def search_in_trie(self, word):
        t_root = self.root
        if t_root is None: return word==''
        i, word_len = 0, len(word)
        while t_root is not None and i<word_len:
            char_index = ord(word[i])-97
            if t_root.cells[char_index] is None: return False
            t_root = t_root.cells[char_index].next
            i+=1
        return i==word_len
    
class BoardTrie(Trie):
    
    def __init__(self, board, row, col, max_depth):
        Trie.__init__(self, max_depth)
        self.board = board
        self.row = row
        self.col = col
        self.adj = [[0,-1,0,1],[-1,0,1,0]]
    
    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        if self.board[i][j]=='\0': return False # Visited
        return True

    def insert_in_trie(self, i, j, trie_node: TrieNode, cur_depth):
        if cur_depth>=self.max_depth: return trie_node
        if not self.is_valid(i, j): return trie_node
        temp = self.board[i][j]
        self.board[i][j] = '\0' # mark visited
        if trie_node is None:
            trie_node = TrieNode()
        trie_cell = trie_node.cells[ord(temp)-97]
        if trie_cell == None:
            trie_cell = TrieCell(temp)
            trie_node.cells[ord(temp)-97] = trie_cell
            trie_node.active_cells_count+=1
        for k in range(4):
            ti, tj = i + self.adj[0][k], j + self.adj[1][k]
            trie_cell.next = self.insert_in_trie(ti, tj, trie_cell.next, cur_depth+1)
        self.board[i][j] = temp
        return trie_node
    
    def make_trie(self):
        for i in range(self.row):
            for j in range(self.col):
                self.root = self.insert_in_trie(i, j, self.root, 0)
        # self.print_trie()

        
class WordsTrie(Trie):
    
    def __init__(self, words, words_len, max_depth):
        Trie.__init__(self, max_depth)
        self.words = words
        self.words_len = words_len

    def insert_in_trie(self, word, word_len, i, trie_node: TrieNode, cur_depth):
        if cur_depth>=self.max_depth: return trie_node
        if i==word_len: return trie_node
        if trie_node is None:
            trie_node = TrieNode()
        char = word[i]
        trie_cell = trie_node.cells[ord(char)-97]
        if trie_cell == None:
            trie_cell = TrieCell(char)
            trie_node.cells[ord(char)-97] = trie_cell
            trie_node.active_cells_count+=1
        if i==(word_len-1): trie_cell.is_end_cell = True
        trie_cell.next = self.insert_in_trie(word, word_len, i+1, trie_cell.next, cur_depth+1)
        return trie_node
    
    def is_valid_tc(self,board_freq, word, word_len):
        word_freq = dict()
        for letr in word:
            freq = word_freq[letr] = word_freq.get(letr, 0) + 1
            if freq>(board_freq.get(letr,0)): return False
        return True
    
    def make_trie(self, board, row, col):
        board_freq = dict()
        for i in range(row):
            for j in range(col):
                letr = board[i][j]
                board_freq[letr] = board_freq.get(letr, 0) + 1
        for word in self.words:
            word_len = len(word)
            if self.is_valid_tc(board_freq, word, word_len):
                self.root = self.insert_in_trie(word, len(word), 0, self.root, 0)
        # self.print_trie()
        
class Solution:
    
    def get_board_freq(self, board, row, col):
        board_freq = dict()
        for i in range(row):
            for j in range(col):
                letr = board[i][j]
                board_freq[letr] = board_freq.get(letr, 0) + 1
        return board_freq
    
    def is_valid_tc(self,board_freq, word, word_len):
        word_freq = dict()
        for letr in word:
            freq = word_freq[letr] = word_freq.get(letr, 0) + 1
            if freq>(board_freq.get(letr,0)): return False
        return True
    
    # This moves all the possible words from board into trie and then searchs
    #  for word in words list
    # Will time out
    def findWords1(self, board: list[list[str]], words: list[str]) -> list[str]:
        op = list()
        row = len(board)
        col = 0 if row==0 else len(board[0])
        word_len = len(words)
        max_depth = 0
        board_freq = self.get_board_freq(board, row, col)
        for word in words:
            word_len = len(word)
            if self.is_valid_tc(board_freq, word, word_len):
                max_depth = max(max_depth, word_len)
                if max_depth==10: break
        board_trie = BoardTrie(board, row, col, max_depth)
        board_trie.make_trie()
        for word in words:
            if board_trie.search_in_trie(word):
                op.append(word)
        return op
    
    def is_valid(self, i, j, trie_node:TrieNode):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        if self.board[i][j]=='\0': return False # Visited
        char = self.board[i][j]
        if trie_node.cells[ord(char)-97] is None: return False
        return True

    def search_in_board_dfs(self, i, j, trie_node:TrieNode, op, cur_op):
        if trie_node is None: return None
        if not self.is_valid(i, j, trie_node): return trie_node
        temp = self.board[i][j]
        cur_op.append(temp)
        trie_cell = trie_node.cells[ord(temp)-97]
        self.board[i][j] = '\0'
        for k in range(4):
            ti, tj = i+self.adj[0][k], j+self.adj[1][k]
            trie_cell.next = self.search_in_board_dfs(ti, tj, trie_cell.next, op, cur_op)
            if trie_cell.is_end_cell:   
                op.append(''.join(cur_op))
                trie_cell.is_end_cell = False # To avoid including it again
            if trie_cell.next is None:    
                del(trie_cell)
                trie_node.cells[ord(temp)-97] = None
                trie_node.active_cells_count-=1
                if trie_node.active_cells_count==0:
                    del(trie_node)
                    trie_node = None
                break
        cur_op.pop()
        self.board[i][j] = temp
        return trie_node
    
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        op = list()
        self.board = board
        self.row = len(board)
        self.col = 0 if self.row==0 else len(board[0])
        self.adj = [[0,-1,0,1],[-1,0,1,0]]
        word_len = len(words)
        max_depth = 10
        words_trie = WordsTrie(words, word_len, max_depth)
        words_trie.make_trie(board, self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                words_trie.root = self.search_in_board_dfs(i, j, words_trie.root, op, list())
                # words_trie.print_trie()
                # print('----------------------------------')
        return op
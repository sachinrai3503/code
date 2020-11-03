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

adj_offset = [[-1, -1, -1, 0, 1, 1, 1, 0],
              [-1, 0, 1, 1, 1, 0, -1, -1]]


def to_index(chr):
    _ord = ord(chr)
    if 65 <= _ord <= 90:
        return _ord-65
    elif 90 <= _ord <= 122:
        return _ord-97
    return None


class TrieCell:
    def __init__(self, chr):
        self.chr = chr
        self.is_last_cell = False
        self.child = None

    def print_trie_cell(self, op_list):
        op_list.append(self.chr)
        if self.is_last_cell:
            print(op_list)
        if self.child is not None:
            self.child.print_trie_node(op_list)
        op_list.pop()


class TrieNode:
    def __init__(self):
        self.trie_cells = [None]*26

    def get_cell(self, index):
        return self.trie_cells[index]

    def set_cell(self, index, trie_cell):
        self.trie_cells[index] = trie_cell

    def print_trie_node(self, op_list):
        for cell in self.trie_cells:
            if cell is not None:
                cell.print_trie_cell(op_list)


class Trie:
    def __init__(self):
        self.trie_node = None

    def print_trie(self):
        if self.trie_node:
            self.trie_node.print_trie_node(list())

    def _insert_word(self, trie_node, word, index):
        if index == len(word):
            return None
        char_index = to_index(word[index])
        if trie_node is None:
            trie_node = TrieNode()
        trie_cell = trie_node.get_cell(char_index)
        if not trie_cell:
            trie_cell = TrieCell(word[index])
            trie_node.set_cell(char_index, trie_cell)
        cell_child = self._insert_word(trie_cell.child, word, index+1)
        if cell_child is None:
            trie_cell.is_last_cell = True
        else:
            trie_cell.child = cell_child
        return trie_node

    def insert_word_in_trie(self, word):
        self.trie_node = self._insert_word(self.trie_node, word, 0)


class SearchWord:
    def __init__(self, word_trie, board):
        """
        @param word_trie : Words in dict as trie.
        @param board : 2D board to make the words with.
        """
        self.words = list()
        self.word_trie = word_trie
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
        self.visited = [[False for j in range(
            self.col)] for i in range(self.row)]

    def _is_valid_pos(self, i, j):
        if i < 0 or i >= self.row or j < 0 or j >= self.col:
            return False
        if self.visited[i][j]:
            return False
        return True

    def _search_word(self, trie_node, i, j, op_list: list):
        """
        @param i,j : Index of letter in the board.
        """
        if not trie_node or not self._is_valid_pos(i, j):
            return
        chr_index = to_index(self.board[i][j])
        trie_cell = trie_node.get_cell(chr_index)
        if not trie_cell:
            return
        op_list.append(self.board[i][j])
        self.visited[i][j] = True
        if trie_cell.is_last_cell:
            self.words.append(''.join(op_list))
        for k in range(8):
            ti, tj = i + adj_offset[0][k], j + adj_offset[1][k]
            self._search_word(trie_cell.child, ti, tj, op_list)
        op_list.pop()
        self.visited[i][j] = False

    def search_words(self):
        op_list = list()
        for i in range(self.row):
            for j in range(self.col):
                self._search_word(self.word_trie.trie_node, i, j, op_list)
        return self.words


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert_word_in_trie(word)
        print('===Trie===')
        trie.print_trie()
        search_word = SearchWord(trie, board)
        op_list = search_word.search_words()
        # print(op_list)
        return op_list


def main():
    boards = [['o', 'a', 'a', 'n'],
              ['e', 't', 'a', 'e'],
              ['e', 'e', 'k', 'r'],
              ['s', 'k', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain", "oa", "p",
             "peas", "eaten", 'h', 'seek']
    # Here seek would get printed 3 times since it can be formed 3 ways.
    # To avoid this Set can be used to hold the words instead of list.

    # boards = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
    # words = ["GEEKS", "ABCFIHGDE"]

    print('Boards = ')
    for board in boards:
        print(board)
    print('Words>>', words)

    sol = Solution()
    op_list = sol.findWords(boards, words)
    print('Output>>', op_list)


if __name__ == '__main__':
    main()

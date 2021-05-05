# https://leetcode.com/problems/word-ladder-ii/
"""
A transformation sequence from word beginWord to word endWord using a dictionary
 wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, return all the
 shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible
 transformation.

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the strings in wordList are unique.
"""
# Note - Unlike word_ladder1.py here visited are marked in different way.

from collections import deque

def get_op(op_map, endWord, beginWord, op, op_list):
    op.append(endWord)
    values = op_map.get(endWord)
    if values is not None:
        for value in values:
            get_op(op_map, value, beginWord, op, op_list)
    else:
        new_list = list(op)
        new_list.reverse()
        op_list.append(new_list)
    op.pop()

class Solution:
    
    def __init__(self):
        self.char_list = [chr(i) for i in range(97,123)]
    
    def get_next_words(self, word_set, visited: set, word: list, level_visited):
        op_list = list()
        length = len(word)
        for i in range(length):
            original_char = word[i]
            for c in self.char_list:
                if c != original_char:
                    word[i] = c
                    new_word = ''.join(word)
                    if new_word in word_set and new_word not in visited:
                        op_list.append(new_word)
                        level_visited.add(new_word)
            word[i] = original_char
        return op_list
    
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        op_map = dict()
        op_list = list()
        que = deque()
        word_set = set(wordList)
        if endWord not in word_set: return []
        visited = set()
        null_node = list().append('None')
        que.append(beginWord)
        visited.add(beginWord)
        que.append(null_node)
        while len(que)>0 and que[0]!=null_node:
            level_visited = set()
            cur_pop_nodes = set()
            # print(que)
            while len(que)>0 and que[0]!=null_node:
                t_word = que.popleft()
                if t_word in cur_pop_nodes: continue
                cur_pop_nodes.add(t_word)
                if t_word==endWord:
                    # print(depth, op_map)
                    get_op(op_map, endWord, beginWord, list(), op_list)
                    return op_list
                next_word_list = self.get_next_words(word_set, visited, list(t_word), level_visited)
                que.extend(next_word_list)
                for next_word in next_word_list:
                    values = op_map.get(next_word, None)
                    if values is None: values = set()
                    values.add(t_word)
                    op_map[next_word] = values
            que.popleft()
            que.append(null_node)
            visited = visited.union(level_visited)
            # print(que)
        return op_list
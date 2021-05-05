# https://leetcode.com/problems/word-ladder/
"""
A transformation sequence from word beginWord to word endWord using a dictionary
 wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, 
 return the number of words in the shortest transformation sequence from 
 beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog"
 with 5 words.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no possible
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

# See word_ladder2.py for printing all the possible sequences.

from collections import deque
class Solution:
    def __init__(self):
        self.char_list = [chr(i) for i in range(97,123)]
    
    def get_next_words(self, word_set, visited: set, word: list):
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
                        visited.add(new_word)
            word[i] = original_char
        return op_list
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        que = deque()
        word_set = set(wordList)
        if endWord not in word_set: return 0
        visited = set()
        null_node = list().append('None')
        que.append(beginWord)
        visited.add(beginWord)
        que.append(null_node)
        depth = 1
        while len(que)>0 and que[0]!=null_node:
            # print(que)
            while len(que)>0 and que[0]!=null_node:
                t_word = que.popleft()
                if t_word==endWord:
                    return depth
                next_word_list = self.get_next_words(word_set, visited, list(t_word))
                que.extend(next_word_list)
            que.popleft()
            depth+=1
            que.append(null_node)
            # print(que)
        return 0
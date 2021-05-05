# https://www.lintcode.com/problem/alien-dictionary/
# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
"""
There is a new alien language which uses the latin alphabet. However, the order
 among letters are unknown to you. You receive a list of non-empty words from
 the dictionary, where words are sorted lexicographically by the rules of this
 new language. Derive the order of letters in this language.

Example

Example 1:
Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:
Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

Notice
You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order
"""

"""
IMP TEST CASES 

["wrt","wrf","er","ett","rftt"]
["caa", "aaa", "aab"]
["baa", "abcd", "abca", "cab", "cad"]
["z","x"]
["z","x","z"] 
["c","m","bn","bzz","bzf","kb","knm","knc","kpq","kqr","kqs"]
["c","m","bn","bzz","bzf","kb","kn","knc","kpq","kqr","kqs"]
["cdo","cam","ckbam","mz","bh","kzn"]
["abc", "ab"]
"""

class Graph:
    def __init__(self, words):
        self.map = dict()
        self.in_degree = [-1 for i in range(26)]
        self.is_valid_ip = True
        self.add_edges(words)
    
    def add_edges(self, words):
        prev = ''
        for word in words:
            i, j = 0, 0
            l1, l2 = len(prev), len(word)
            while i<l1 and j<l2:
                if prev[i]!=word[j]:
                    values = self.map.get(prev[i], None)
                    if values is None:
                        values = list()
                    values.append(word[j])
                    self.map[prev[i]] = values
                    if self.in_degree[ord(word[j])-97]==-1:
                        self.in_degree[ord(word[j])-97]=1
                    else: 
                        self.in_degree[ord(word[j])-97]+=1
                    break   
                i+=1
                j+=1
            if i<l1 and j==l2:
                #  Check that second word isn't a prefix of first word.
                self.is_valid_ip = False
                return
            while j<l2:
                if word[j] not in self.map:
                    self.map[word[j]] = list()
                    if self.in_degree[ord(word[j])-97]==-1:
                       self.in_degree[ord(word[j])-97] = 0
                j+=1
            prev = word

class Solution:
    
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = Graph(words)
        # print(graph.map)
        # print(graph.in_degree)
        if not graph.is_valid_ip: return ''
        op_list = list()
        is_node_present = True
        while is_node_present:
            is_node_present = False
            for i in range(26):
                if graph.in_degree[i]==0:
                    graph.in_degree[i]=-1
                    op_char = chr(i+97)
                    op_list.append(op_char)
                    adj_nodes = graph.map.get(op_char, None)
                    if adj_nodes is not None and len(adj_nodes)!=0:
                        for node in adj_nodes:
                            graph.in_degree[ord(node)-97]-=1
                        is_node_present = True
                        break
        # print(graph.in_degree)
        for in_deg in graph.in_degree:
            if in_deg!=-1: return ''
        return ''.join(op_list)
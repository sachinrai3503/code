# https://leetcode.com/problems/evaluate-division
"""
You are given an array of variable pairs equations and an array of real numbers values,
 where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].

 Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query 
  where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will
 not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
 queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], 
 queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

from collections import deque
from typing import List

class Graph:
    def __init__(self, equations, values):
        self.data = dict()
        self.vertex_count = 0
        self.vertex_index = dict()
        self.last_index = 0
        self.add_edges(equations, values)
        self.vertex_count = len(self.vertex_index)
    
    def add_edges(self, equations, values):
        for i in range(len(equations)):
            u, v, w = equations[i][0], equations[i][1], values[i]
            self._add_edge(u,v,w)
            self._add_edge(v,u,1/w)
            self._set_index(u)
            self._set_index(v)
    
    def _add_edge(self, u, v, w):
        adjs = self.data.get(u, [])
        adjs.append((v, w))
        self.data[u] = adjs

    def _set_index(self, vertex):
        if vertex not in self.vertex_index:
            self.vertex_index[vertex] = self.last_index
            self.last_index+=1

    def get_index(self, vertex):
        return self.vertex_index.get(vertex, None)
    
    def get_adj_vertexs(self, vertex):
        return self.data.get(vertex, None)

class Solution:

    def compute_values(self, graph):
        n = graph.vertex_count
        values = [[-1.0 for _ in range(n)] for _ in range(n)]
        que = deque()
        for ver in graph.vertex_index.keys():
            que.append([ver, ver, 1])
            values[graph.get_index(ver)][graph.get_index(ver)] = 1
        # print(f'{que=}')
        while que:
            temp = que.popleft()
            src, cur, val = temp
            adj_vertexs = graph.get_adj_vertexs(cur)
            if not adj_vertexs: continue
            for adj_vertex in adj_vertexs:
                v, w = adj_vertex
                if values[graph.get_index(src)][graph.get_index(v)] is not -1.0: continue
                t_val = val*w
                values[graph.get_index(src)][graph.get_index(v)] = t_val
                que.append([src, v, t_val])
            # print(f'{que=}')
        return values

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph(equations, values)
        # print(f'{graph.data=} {graph.vertex_index=}')
        values = self.compute_values(graph)
        # print(f'{values=}')
        op = list()
        for u, v in queries:
            u_index, v_index = graph.get_index(u), graph.get_index(v)
            if u_index is None or v_index is None: op.append(-1.0)
            else: op.append(values[u_index][v_index])
        return op
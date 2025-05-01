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

from collections import deque, defaultdict
from typing import List

class Graph:
    def __init__(self, edges, weights):
        self.data = defaultdict(set) # {'u':{v,v1,v2}, ...}
        self.weight_map = dict() # {'u-v':x, 'v-u':1/x}
        self.add_edges(edges, weights)
    
    def add_edges(self, edges, weights):
        for edge, weight in zip(edges, weights):
            self.add_edge(edge[0], edge[1], weight)
            self.add_edge(edge[1], edge[0], 1/weight)

    def add_edge(self, u, v, weight):
        self.data[u].add(v)
        self.weight_map[(u,v)] = weight

    def print_graph(self):
        print(f'{self.data=}\n{self.weight_map}')
        print('*'*70)
    
    def get_adj_vertex(self, u):
        return self.data[u]

    def get_weight(self, u, v):
        return self.weight_map[(u, v)]
    
class Solution:

    def compute_division(self, graph, s, t):
        if s not in graph.data or t not in graph.data: return -1.0
        if s==t: return 1.0
        if (s, t) in graph.weight_map: return graph.get_weight(s, t)
        visited = set()
        que = deque()
        que.append((s, 1.0))
        visited.add(s)
        while que:
            u, s_u_val = que.popleft()
            if u==t: return s_u_val
            adj_vertex = graph.get_adj_vertex(u)
            for v in adj_vertex:
                if v not in visited:
                    u_v_val = graph.get_weight(u, v)
                    s_v_val = s_u_val*u_v_val
                    que.append((v, s_v_val))
                    visited.add(v)
                    graph.add_edge(s, v, s_v_val) # These 2 lines are to make future queries fast
                    graph.add_edge(v, s, 1/s_v_val)
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        op = list()
        graph = Graph(equations, values)
        # graph.print_graph()
        for u, v in queries:
            op.append(self.compute_division(graph, u, v))
            # graph.print_graph()
        return op
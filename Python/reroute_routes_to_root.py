# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two
 different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads 
 in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of 
edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 2:
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

Example 3:
Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:
2 <= n <= 5 * 104
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
"""

from collections import deque
from typing import List

class Graph:

    def __init__(self, n, edges):
        self.n = n
        self.data = dict()
        self._add_edges(edges)
    
    def _add_edges(self, edges):
        for u, v in edges:
            self._add_edge(u, v, 'O')
            self._add_edge(v, u, 'I')
    
    def _add_edge(self, u, v, connection_type):
        adj_edges = self.data.get(u, [])
        adj_edges.append((v, connection_type))
        self.data[u] = adj_edges

    def get_adjacent_vertexs(self, u):
        return self.data.get(u, None)

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reorder_count = 0
        graph = Graph(n, connections)
        # print(f'{graph.data=}')
        visited = set()
        que = deque()
        que.append(0)
        que.append(None)
        visited.add(0)
        while que[0] is not None:
            # print(f'{que=} {visited=}')
            while que[0] is not None:
                temp = que.popleft()
                for v, connection_type in graph.get_adjacent_vertexs(temp):
                    if v not in visited:
                        que.append(v)
                        visited.add(v)
                        if connection_type == 'O':
                            reorder_count+=1
            que.popleft()
            que.append(None)
        return reorder_count
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree
"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1,
 which has some apples in their vertices. You spend 1 second to walk over one
 edge of the tree. Return the minimum time in seconds you have to spend to
 collect all apples in the tree, starting at vertex 0 and coming back to this
 vertex.

The edges of the undirected tree are given in the array edges, where 
 edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
Additionally, there is a boolean array hasApple, where hasApple[i] = true means
 that vertex i has an apple; otherwise, it does not have any apple.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
              hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have
 an apple. One optimal path to collect all apples is shown by the green arrows.  

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
              hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices
 have an apple. One optimal path to collect all apples is shown by the green 
 arrows.  

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
              hasApple = [false,false,false,false,false,false,false]
Output: 0

Constraints:
1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
fromi < toi
hasApple.length == n
"""

class Graph:
    def __init__(self, n, edges):
        self.map = dict()
        self.node_count = n
        self._add_edges(edges)
        
    def _add_edges(self, edges):
        for edge in edges:
            self._add_edge(edge[0], edge[1])
            self._add_edge(edge[1], edge[0])
            
    def _add_edge(self, x, y):
        if not self.map.__contains__(x):
            self.map[x] = list()
        self.map[x].append(y)
    
    def get_adjacent(self, x):
        return self.map[x]

def get_min_time(graph, parent, node, has_apple):
    time = 0
    for adj in graph.get_adjacent(node):
        if adj!=parent:
            t_time = get_min_time(graph, node, adj, has_apple)
            time+=t_time
    if time>0: return time+2
    if has_apple[node]: return 2
    return 0
            
    
class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = Graph(n, edges)
        time = get_min_time(graph, -1, 0, hasApple)
        if time>0: return time-2
        return time
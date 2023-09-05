# https://leetcode.com/problems/design-graph-with-shortest-path-calculator
"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. 
The edges of the graph are initially represented by the given array edges where 
 edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi 
 with the cost edgeCosti.

Implement the Graph class:
Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. 
 It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2.
 If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.

Example 1:
Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]
Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
"""

from sys import maxsize
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.shortest_path = [[maxsize if i!=j else 0 for j in range(n)] for i in range(n)]
        self.add_edges(edges)
        self.compute_all_pair_shortest_path()
        # print(f'{self.shortest_path=}')

    def compute_all_pair_shortest_path(self):
        for i in range(self.n):
            self._compute_shortest_path_via(i)
    
    def _compute_shortest_path_via(self, k):
        for i in range(self.n):
            cost_ik = self.shortest_path[i][k]
            if cost_ik is maxsize: continue
            for j in range(self.n):
                if i==j: continue
                cost_kj = self.shortest_path[k][j]
                if cost_kj is maxsize: continue
                if (cost_ik+cost_kj)<self.shortest_path[i][j]:
                    self.shortest_path[i][j] = (cost_ik+cost_kj)

    def _compute_shorted_path_crossing_edge(self, u, v):
        for i in range(self.n):
            if self.shortest_path[i][u]==maxsize: continue
            cost_iu_uv = self.shortest_path[i][u] + self.shortest_path[u][v]
            for j in range(self.n):
                if self.shortest_path[v][j]==maxsize: continue
                new_cost_iu_uv_vj = cost_iu_uv + self.shortest_path[v][j]
                if self.shortest_path[i][j]>new_cost_iu_uv_vj:
                    self.shortest_path[i][j] = new_cost_iu_uv_vj

    def add_edges(self, edges):
        for u,v,w in edges:
            self.shortest_path[u][v] = w

    def addEdge(self, edge: List[int]) -> None:
        u,v,w = edge
        if self.shortest_path[u][v]>w:
            self.shortest_path[u][v] = w
            self._compute_shorted_path_crossing_edge(u,v)

    def shortestPath(self, node1: int, node2: int) -> int:
        shortest_path = self.shortest_path[node1][node2]
        return shortest_path if shortest_path!=maxsize else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
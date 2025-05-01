# https://leetcode.com/problems/count-the-number-of-complete-components
"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given
  a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
  vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no 
 vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair
  of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is
  no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

Constraints:
1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges
"""

from typing import List

class DJSet:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.edge_count = [0 for i in range(n)]
        self.ver = [1 for i in range(n)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj:
            self.edge_count[pj]+=1 # only edge addition
            return
        r_pi, r_pj = self.rank[pi], self.rank[pj]
        if r_pi<r_pj:
            self.parent[pi] = pj
            self.edge_count[pj]+=(self.edge_count[pi] + 1)
            self.ver[pj]+=self.ver[pi]
        elif r_pi>r_pj:
            self.parent[pj] = pi
            self.edge_count[pi]+=(self.edge_count[pj] + 1)
            self.ver[pi]+=self.ver[pj]
        else:
            self.parent[pi] = pj
            self.rank[pj]+=1
            self.edge_count[pj]+=(self.edge_count[pi] + 1)
            self.ver[pj]+=self.ver[pi]
    
    def __repr__(self):
        return f'{self.parent=}\n{self.edge_count=}\n{self.ver=}'

class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        dj_set = DJSet(n)
        for u, v in edges:
            dj_set.union(u, v)
        # print(f'{dj_set=}')
        for i in range(n):
            p_i = dj_set.find_parent(i)
            if p_i==i:
                ver_count, edge_count = dj_set.ver[p_i], dj_set.edge_count[p_i]
                if edge_count==((ver_count*(ver_count-1))//2):
                    count+=1
        return count
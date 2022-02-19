# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1,
 and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and
 weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of
 the graph's edges that connects all vertices without cycles and with the minimum possible
 total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Example 1:
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges,
 so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered 
 pseudo-critical edges. We add them to the second list of the output.

Example 2:
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing
 any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 
Constraints:
2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
"""

from sys import maxsize

class DJSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def get_parent(self, i):
        if self.parent[i]==i:return self.parent[i]
        self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]
        
    def union(self, u, v):
        p_u = self.get_parent(u)
        p_v = self.get_parent(v)
        if p_u==p_v: return False
        if self.rank[p_u]>self.rank[p_v]:
            self.parent[p_v] = p_u
        elif self.rank[p_v]>self.rank[p_u]:
            self.parent[p_u] = p_v
        else:
            self.parent[p_v] = p_u
            self.rank[p_u]+=1
        return True
            
class Solution:
    
    # edges_index = list of index of edge sorted on weight
    def make_MST(self, n, edges, edges_index, edge_count, dj_set, to_ignore, inc_edge_count = 0, weight = 0):
        i, j, req_edge_count = 0, inc_edge_count, n-1
        while i<edge_count and j<req_edge_count:
            # if edges_index[i]==to_ignore: continue
            if i==to_ignore:
                i+=1
                continue
            u, v, w = edges[edges_index[i]]
            is_cycle = not dj_set.union(u, v)
            if not is_cycle:
                weight+=w
                j+=1
            i+=1
        if j==req_edge_count:
            return weight
        return maxsize
    
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        op = [list(), list()]
        edges_count = len(edges)
        edges_index = [i for i in range(edges_count)]
        edges_index.sort(key = lambda x : edges[x][2])
        # print(edges_index)
        mst_weight = self.make_MST(n, edges, edges_index, edges_count, DJSet(n), -1, 0, 0)
        for i in edges_index:
            t_mst_weight = self.make_MST(n, edges, edges_index, edges_count, DJSet(n), i, 0, 0)
            if t_mst_weight>mst_weight: op[0].append(edges_index[i]) # critical
            else: # pseudo critical or NA
                u, v, w = edges[edges_index[i]]
                t_dj_set = DJSet(n)
                t_dj_set.union(u, v)
                t_mst_weight = self.make_MST(n, edges, edges_index, edges_count, t_dj_set, i, 1, w)
                if t_mst_weight==mst_weight: op[1].append(edges_index[i]) # pseudo critical
        return op
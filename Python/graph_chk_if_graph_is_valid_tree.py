# https://www.lintcode.com/problem/178
# https://leetcode.com/problems/graph-valid-tree
"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
 (each edge is a pair of nodes), write a function to check whether these edges
 make up a valid tree.

You can assume that no duplicate edges will appear in edges. Since all edges are
 undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example
Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""

from typing import (
    List,
)

class DJSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find_parent(self, i):
        if self.parent[i]==i:
            return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, u, v):
        p_u = self.find_parent(u)
        p_v = self.find_parent(v)
        if p_u==p_v: return False
        rank_pu = self.rank[p_u]
        rank_pv = self.rank[p_v]
        if rank_pu>rank_pv:
            self.parent[p_v] = p_u
        elif rank_pu<rank_pv:
            self.parent[p_u] = p_v
        else:
            self.parent[p_v] = p_u
            self.rank[p_u]+=1
        return True

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        component_count = 0
        dj_set = DJSet(n)
        for u,v in edges:
            if not dj_set.union(u, v): return False
        for i in range(n):
            if dj_set.find_parent(i)==i:
                component_count+=1
        return component_count==1
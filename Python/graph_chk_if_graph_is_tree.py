# https://www.geeksforgeeks.org/check-given-graph-tree/
# https://www.lintcode.com/problem/graph-valid-tree/description
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
class DisJointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank   = [1 for i in range(size)]
    
    def get_parent(self, a):
        if self.parent[a]==a: return a
        self.parent[a] = self.get_parent(self.parent[a])
        return self.parent[a]
    
    def union(self, a, b):
        """
        Add an edge and return false but if cycle then returns False
        """
        par_a = self.get_parent(a)
        par_b = self.get_parent(b)
        if par_a == par_b: return True
        if self.rank[par_a]==self.rank[par_b]:
            self.parent[par_b] = par_a
            self.rank[par_a]+=self.rank[par_b]
        elif self.rank[par_a]<self.rank[par_b]:
            self.parent[par_a] = par_b
            self.rank[par_b]+=self.rank[par_a]
        else:
            self.parent[par_b] = par_a
            self.rank[par_a]+=self.rank[par_b]
        return False
            
        

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        dj_set = DisJointSet(n)
        for edge in edges:
            if dj_set.union(edge[0], edge[1]): return False
        component_count = 0
        for i in range(n):
            if dj_set.parent[i]==i:
                component_count+=1
        if component_count==1: return True
        return False
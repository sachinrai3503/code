# https://www.geeksforgeeks.org/eulerian-path-and-circuit/
"""
Given a undirected graph check if there exits
 - Eulerian Path
 - Eulerian cycle/circuit
"""

from re import escape


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = dict()
        self.degree = [0 for i in range(n)]
    
    def add_edges(self, edges_list):
        for u, v in edges_list:
            self._add_edge(u, v)
            self._add_edge(v, u)
    
    def _add_edge(self, u, v):
        adj_vertexs = self.edges.get(u, list())
        adj_vertexs.append(v)
        self.edges[u] = adj_vertexs
        self.degree[v]+=1
    
    def get_adj_edges(self, u):
        return self.edges.get(u, [])
    
class DJSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find_parent(self, i):
        if self.parent[i]==i:
            return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj:
            return False
        r_pi = self.rank[pi]
        r_pj = self.rank[pj]
        if r_pi<r_pj:
            self.parent[pi] = pj
        elif r_pi>r_pj:
            self.parent[pj] = pi
        else:
            self.parent[pi] = pj
            self.rank[pj]+=1
        return True

# For undirected graph
class Euler:
    def __init__(self, n, edges):
        self.n = n
        self.graph = Graph(n)
        self.graph.add_edges(edges)
    
    def _is_connected(self):
        dj_set = DJSet(self.n)
        for u in range(self.n):
            for v in self.graph.get_adj_edges(u):
                dj_set.union(u, v)
        connected_component_count = 0
        for i in range(self.n):
            if dj_set.find_parent(i)==i:
                connected_component_count+=1
                if connected_component_count>1:
                    if self.graph.degree[i]>0: return False
        return True

    def has_eulerian_path(self):
        if not self._is_connected(): return False
        odd_degree_vertex_count = 0
        for i in range(self.n):
            if (self.graph.degree[i]&1):
                odd_degree_vertex_count+=1
        return True if (odd_degree_vertex_count==0 or odd_degree_vertex_count==2) else False

    def has_eulerian_cycle(self):
        if not self._is_connected(): return False
        for i in range(self.n):
            if (self.graph.degree[i]&1):
                return False
        return True

class Solution:
    def test(self, n, edges):
        euler = Euler(n, edges)
        print('path =', euler.has_eulerian_path())
        print('cycle = ', euler.has_eulerian_cycle())
        print('*'*100)
    
def main():
    sol = Solution()
    
    n = 0
    edges = []
    sol.test(n, edges)

    n = 1
    edges = []
    sol.test(n, edges)

    n = 5
    edges = [[1,0], [0,2], [2,1], [0,3], [3,4]]
    sol.test(n, edges)

    n = 5
    edges = [[1,0], [0,2], [2,1], [0,3], [3,4], [4,0]]
    sol.test(n, edges)

    n = 5
    edges = [[1,0], [0,2], [2,1], [0,3], [3,4], [1,3]]
    sol.test(n, edges)

    n = 3
    edges = [[1,0], [1,2], [2,0]]
    sol.test(n, edges)

    n = 3
    edges = []
    sol.test(n, edges)

if __name__ == '__main__':
    main()
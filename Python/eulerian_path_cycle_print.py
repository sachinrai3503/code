# https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path
# https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph
"""
Given a undirected or directed graph check if there exits
 - Print
    - Eulerian Path
    - Eulerian cycle/circuit

 Uses - fleurys & hierholzers algo
"""

"""
Note - 
    - This will assume that the given graph meets the condition for having the eulerian path or circuit
    - Below Fleury's implementation is for undirected graph. Same can be modified for directed one too.
    - Below Hierholzer’s implementation is for directed graph. Same can be modified for undirected one too.
"""

from typing import List

# Undirected
class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = dict()
        self.degree = [0 for i in range(n)]
        self.deleted_edges = set()
    
    def add_edges(self, edges_list:List):
        for u, v in edges_list:
            self._add_edge(u, v)
            self._add_edge(v, u)

    def remove_edge(self, u, v):
        self._remove_edge(u, v)
        self._remove_edge(v, u)

    def _add_edge(self, u, v):
        adj_vertexs = self.edges.get(u, set())
        adj_vertexs.add(v)
        self.edges[u] = adj_vertexs
        self.degree[v]+=1
        if self.is_edge_deleted(u, v):
            self.deleted_edges.remove((u, v))
    
    def _remove_edge(self, u, v):
        self.deleted_edges.add((u,v))
        self.degree[v]-=1
    
    def get_adj_edges(self, u):
        return self.edges.get(u, set())

    def is_edge_deleted(self, u, v):
        return (u,v) in self.deleted_edges

# Directed
class Graph2:
    def __init__(self, n):
        self.n = n
        self.edges = dict()
        self.in_degree = [0 for i in range(n)]
        self.out_degree = [0 for i in range(n)]
        # self.deleted_edges = set()
    
    def add_edges(self, edges_list:List):
        for u, v in edges_list:
            self._add_edge(u, v)

    # def remove_edge(self, u, v):
    #     self._remove_edge(u, v)

    def _add_edge(self, u, v):
        adj_vertexs = self.edges.get(u, set())
        adj_vertexs.add(v)
        self.edges[u] = adj_vertexs
        self.out_degree[u]+=1
        self.in_degree[v]+=1
        # if self.is_edge_deleted(u, v):
        #     self.deleted_edges.remove((u, v))
    
    # def _remove_edge(self, u, v):
    #     self.deleted_edges.add((u,v))
    #     self.out_degree[u]-=1
    #     self.out_degree[v]-=1
    
    def get_adj_edges(self, u):
        return self.edges.get(u, set())

    # def is_edge_deleted(self, u, v):
    #     return (u,v) in self.deleted_edges

class Fleurys:
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def find_starting_vertex(self):
        u = 0
        for i in range(self.graph.n):
            if self.graph.degree[i]&1==1:
                u = i
                break
        return u

    def count_vertex_reachable(self, u:int, visited:set) -> int:
        count = 0
        visited.add(u)
        for v in self.graph.get_adj_edges(u):
            if not self.graph.is_edge_deleted(u,v) and v not in visited:
                count+=self.count_vertex_reachable(v, visited)
        return count+1

    def is_bridge(self, u, v):
        # count vertex reachable from u
        visited = set()
        count1 = self.count_vertex_reachable(u, visited)
        # count vertex reachable from u after deleting (u,v)
        visited.clear()
        self.graph.remove_edge(u, v)
        count2 = self.count_vertex_reachable(u, visited)
        # print(f'{u=} {v=} {count1=} {count2=}')
        self.graph.add_edges([(u, v)])
        return True if count1>count2 else False

    def can_include(self, u, v):
        # Only edge available
        if self.graph.degree[u]==1:
            return True
        elif self.is_bridge(u, v):
            return False
        return True

    def _print_euler_path_cycle(self, u, path):
        for v in self.graph.get_adj_edges(u):
            # print(f'({u=} {v=})')
            if not self.graph.is_edge_deleted(u, v) and self.can_include(u, v):
                path.append((u,v))
                self.graph.remove_edge(u,v)
                self._print_euler_path_cycle(v, path)

    def print_tour(self):
        path = list()
        u = self.find_starting_vertex()
        print(f'start at {u=}')
        self._print_euler_path_cycle(u, path)
        return path

class Hierholzer:
    def __init__(self, graph: Graph2):
        self.graph = graph
    
    def find_starting_vertex(self):
        u = 0
        for i in range(self.graph.n):
            if self.graph.out_degree[i]==(self.graph.in_degree[i]+1):
                u = i
                break
        return u

    def _print_euler_path_cycle(self, start, circuit:List):
        path = [start]
        while path:
            u = path[-1]
            if self.graph.get_adj_edges(u):
                v = self.graph.get_adj_edges(u).pop()
                path.append(v)
            else:
                circuit.append(path.pop())
        return

    def print_tour(self):
        circuit = list()
        u = self.find_starting_vertex()
        print(f'start at {u=}')
        self._print_euler_path_cycle(u, circuit)
        return circuit[::-1]

class Euler:
    def __init__(self, n, edges):
        self.n = n
        self.graph = Graph(n)
        self.graph.add_edges(edges)
        self.graph2 = Graph2(n)
        self.graph2.add_edges(edges)
    
    def print_euler_path_cycle_fleury(self):
        fleury = Fleurys(self.graph)
        return fleury.print_tour()

    def print_euler_path_cycle_hierholzer(self):
        lierholzer = Hierholzer(self.graph2)
        return lierholzer.print_tour()

class Solution:
    def test(self, n, edges):
        euler = Euler(n, edges)
        print('path =', euler.print_euler_path_cycle_fleury())
        print('*'*100)
    
class Solution2:
    def test(self, n, edges):
        euler = Euler(n, edges)
        print('path =', euler.print_euler_path_cycle_hierholzer())
        print('*'*100)

def main():
    sol = Solution()
    sol2 = Solution2()
    
    n = 4
    edges = [(0, 1),(0, 2),(1, 2),(2, 3)]
    sol.test(n, edges)

    n = 3
    edges = [(0, 1),(1, 2),(2, 0)]
    sol.test(n, edges)

    n = 5
    edges = [(1, 0),(0, 2),(2, 1),(0, 3),(3, 4),(3, 2),(3, 1),(2, 4)]
    sol.test(n, edges)

    n = 3
    edges = [(0, 1),(1, 2),(2, 0)]
    sol2.test(n, edges)

    n = 7
    edges = [(0, 1),(0, 6),(1, 2),(2, 0),(2, 3),(3, 4),(4, 2),(4, 5),(5,0),(6,4)]
    sol2.test(n, edges)

if __name__ == '__main__':
    main()
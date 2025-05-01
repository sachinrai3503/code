# https://www.geeksforgeeks.org/euler-circuit-directed-graph/
"""
Given a directed graph check if there exits
 - Eulerian Path
 - Eulerian cycle/circuit
"""

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = dict()
        self.reversed_edges = dict()
        self.in_degree = [0 for i in range(n)]
        self.out_degree = [0 for i in range(n)]
    
    def add_directed_edges(self, edges_list):
        for u, v in edges_list:
            self._add_directed_edge(u, v)
            self._add_reversed_directed_edge(v, u)
    
    def _add_directed_edge(self, u, v):
        adj_vertexs = self.edges.get(u, list())
        adj_vertexs.append(v)
        self.edges[u] = adj_vertexs
        self.out_degree[u]+=1
        self.in_degree[v]+=1
    
    def _add_reversed_directed_edge(self, u, v):
        adj_vertexs = self.reversed_edges.get(u, list())
        adj_vertexs.append(v)
        self.reversed_edges[u] = adj_vertexs

    def get_adj_edges(self, u):
        return self.edges.get(u, [])

    def get_rev_adj_edges(self, u):
        return self.reversed_edges.get(u, [])

class Kosaraju:
    def __init__(self, n, graph : Graph):
        self.n = n
        self.graph = graph
    
    def dfs_with_priority(self, u, priority, visited):
        visited.add(u)
        for v in self.graph.get_adj_edges(u):
            if v not in visited:
                self.dfs_with_priority(v, priority, visited)
        priority.append(u)
    
    def dfs(self, u, visited):
        visited.add(u)
        for v in self.graph.get_rev_adj_edges(u):
            if v not in visited:
                self.dfs(v, visited)

    def count_stronly_connected_component(self):
        count = 0
        visited = set()
        priority = list()
        for i in range(self.n):
            if i not in visited:
                self.dfs_with_priority(i, priority, visited)
        visited.clear()
        print(f'{priority=}')
        for u in priority[::-1]:
            if u not in visited:
                self.dfs(u, visited)
                count+=1
        return count
    
class Tarjan:
    def __init__(self, n, graph: Graph):
        self.n = n
        self.graph = graph
        self.visited = set()
        self.processed = set()
        self.dist = [None for i in range(self.n)]
        self.low = [None for i in range(self.n)]
        self.stack = list()
        self.scc_count = 0
        self.visited_at = 0
    
    def _count_SCC_dfs(self, u):
        self.low[u] = self.visited_at
        self.dist[u] = self.visited_at
        self.visited_at+=1
        self.visited.add(u)
        self.stack.append(u)
        # print(f'{u=} {self.visited=} {self.processed=} {self.dist=} {self.low=} {self.stack=} {self.scc_count=}')
        for v in self.graph.get_adj_edges(u):
            if v not in self.visited:
                self._count_SCC_dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif v not in self.processed:
                self.low[u] = min(self.low[u], self.dist[v])
        if self.low[u]==self.dist[u]:
            # print(f'-- {u=} {self.visited=} {self.processed=} {self.dist=} {self.low=} {self.stack=} {self.scc_count=}')
            op = list()
            while self.stack[-1]!=u:
                v = self.stack.pop()
                op.append(v)
                self.processed.add(v)
            v = self.stack.pop()
            op.append(v)
            self.processed.add(v)
            self.scc_count+=1
            print(f'scc={op=}')
            
    def count_stronly_connected_component(self):
        for u in range(self.n):
            if u not in self.visited:
                self._count_SCC_dfs(u)
        return self.scc_count

# For directed graph
class Euler:
    def __init__(self, n, edges):
        self.n = n
        self.graph = Graph(n)
        self.graph.add_directed_edges(edges)
        self.kosaraju = Kosaraju(self.n, self.graph)
        self.tarjan = Tarjan(self.n, self.graph)

    # Checks if thjere is 1 Strongly connected component
    def _has_1_SCC_kosaraju(self):
        scc_count = self.kosaraju.count_stronly_connected_component()
        print(f'{scc_count=}')
        zero_deg_vertex = 0
        for i in range(self.n):
            if self.graph.in_degree[i]==0 and self.graph.out_degree[i]==0:
                zero_deg_vertex+=1
        if (scc_count-zero_deg_vertex)>1: return False
        return True
    
    # Checks if thjere is 1 Strongly connected component
    def _has_1_SCC_tarjan(self):
        scc_count = self.tarjan.count_stronly_connected_component()
        print(f'{scc_count=}')
        zero_deg_vertex = 0
        for i in range(self.n):
            if self.graph.in_degree[i]==0 and self.graph.out_degree[i]==0:
                zero_deg_vertex+=1
        if (scc_count-zero_deg_vertex)>1: return False
        return True

    def _dfs(self, u, visited):
        visited.add(u)
        for v in self.graph.get_adj_edges(u):
            if v not in visited:
                self._dfs(v, visited)

    # Checks if there is 1 connected component.
    def _has_1_connected_component(self):
        connected_components = 0
        visited = set()
        for i in range(self.n):
            if i not in visited:
                if connected_components>1:
                    if self.graph.in_degree[i]!=0 or self.graph.out_degree[i]!=0:
                        return False
                self._dfs(i, visited)
                connected_components+=1
        return True

    def has_eulerian_path(self):
        if not self._has_1_connected_component(): return False
        deg_misMatch_vertex = 0
        for i in range(self.n):
            if self.graph.in_degree[i]-self.graph.out_degree[i]==1:
                deg_misMatch_vertex+=1
            elif self.graph.out_degree[i]-self.graph.in_degree[i]==1:
                deg_misMatch_vertex-=1
            elif self.graph.in_degree[i]!=self.graph.out_degree[i]:
                return False
        return deg_misMatch_vertex==0

    def has_eulerian_cycle_kosaraju(self):
        if not self._has_1_SCC_kosaraju(): return False
        for i in range(self.n):
            if (self.graph.in_degree[i]!=self.graph.out_degree[i]):
                return False
        return True

    def has_eulerian_cycle_tarjan(self):
        if not self._has_1_SCC_tarjan(): return False
        for i in range(self.n):
            if (self.graph.in_degree[i]!=self.graph.out_degree[i]):
                return False
        return True

class Solution:
    def test(self, n, edges):
        euler = Euler(n, edges)
        print('path =', euler.has_eulerian_path())
        print('cycle (SCC kosaraju)= ', euler.has_eulerian_cycle_kosaraju())
        print('cycle (SCC Tarjan)= ', euler.has_eulerian_cycle_tarjan())
        print('*'*100)
    
def main():
    sol = Solution()
    
    n = 5
    edges = [[1,0], [0,2], [2,1],[0,3],[3,4],[4,0]]
    sol.test(n, edges)

    n = 9
    edges = [[0,1], [1,0], [0,2],[2,0],[1,3],[4,2],[3,5],[5,3],[4,5],[4,7],[7,5],[7,6],[6,4],[8,7],[8,6]]
    sol.test(n, edges)

    n = 9
    edges = [[1,2], [2,3], [3,1],[3,4],[2,4],[2,5],[5,6],[5,7],[7,6],[6,8],[8,7]]
    sol.test(n, edges)

    n = 5
    edges = [[1,0], [0,2], [2,1],[0,3],[3,4]]
    sol.test(n, edges)

    n = 4
    edges = [[0,1], [1,2], [2,3]]
    sol.test(n, edges)

    n = 7
    edges = [[0,1], [1,2], [2,0],[1,3],[1,4],[1,6],[3,5],[4,5]]
    sol.test(n, edges)

    n = 11
    edges = [(0, 1),(0, 3),(1, 2),(1, 4),(2, 0),(2, 6),(3, 2),(4, 5),(4, 6),(5, 6),(5, 7),(5, 8),(5, 9),(6, 4),(7, 9),(8, 9),(9, 8)]
    sol.test(n, edges)

    n = 5
    edges = [(0, 1),(1, 2),(2, 3),(2, 4),(3, 0),(4, 2)]
    sol.test(n, edges)


if __name__ == '__main__':
    main()
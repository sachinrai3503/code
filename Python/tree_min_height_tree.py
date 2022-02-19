from collections import deque

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = dict()
        self.degree = [0 for i in range(n)]
        self.add_edges(edges)

    def add_edges(self, edges):
        for edge in edges:
            u, v = edge
            self.add_edge(u, v)
            self.add_edge(v, u)
    
    def add_edge(self, u, v):
        adj_edges = self.edges.get(u, list())
        adj_edges.append(v)
        self.edges[u] = adj_edges
        self.degree[u]+=1

    def get_adj_vertexs(self, u):
        return self.edges.get(u, None)
        
class Solution:
    
    def find_max_dist_node(self, graph, root, parent, cur_level, deepest_node, cur_path):
        if root is None: return
        cur_path.append(root)
        if cur_level>deepest_node[0]:
            deepest_node[0], deepest_node[1] = cur_level, root
            deepest_node[2] = list(cur_path)
        adj_vertex = graph.get_adj_vertexs(root)
        if adj_vertex is None: return
        for adj in adj_vertex:
            if adj!=parent:
                self.find_max_dist_node(graph, adj, root, cur_level+1, deepest_node, cur_path)
        cur_path.pop()
    
    # https://leetcode.com/problems/minimum-height-trees/discuss/923071/Python-Find-diameter-using-2-dfs-explained/754368/
    def findMinHeightTrees_diameter_based(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = Graph(n, edges)
        # print(graph.edges)
        deepest_node = [-1, None, list()]
        self.find_max_dist_node(graph, 0, -1, 0, deepest_node, list())
        deepest_node2 = [-1, None, list()]
        self.find_max_dist_node(graph, deepest_node[1], -1, 0, deepest_node2, list())
        path = deepest_node2[2]
        path_len = len(path)
        mid = path_len//2
        # print(deepest_node, deepest_node2)
        if path_len%2==0:
            return [path[mid-1], path[mid]]
        return [path[mid]]
    
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = Graph(n, edges)
        # print(graph.edges)
        que = deque()
        for i in range(n):
            if graph.degree[i]<=1:
                que.append(i)
        que.append(None)
        # print(que)
        remaining_nodes = n
        while que[0]!=None and remaining_nodes>2:
            t_count = 0
            while que[0]!=None:
                temp = que.popleft()
                t_count+=1
                adj_vertexs = graph.get_adj_vertexs(temp)
                for adj in adj_vertexs:
                    graph.degree[adj]-=1
                    if graph.degree[adj]==1:
                        que.append(adj)
            que.popleft()
            que.append(None)
            remaining_nodes-=t_count
        return list(que)[:-1]
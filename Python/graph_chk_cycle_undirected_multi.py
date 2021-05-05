# https://www.interviewbit.com/problems/cycle-in-undirected-graph/
# https://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
# https://www.geeksforgeeks.org/union-find/
# https://www.geeksforgeeks.org/detect-cycle-in-an-undirected-graph-using-bfs/
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
"""
Given an undirected graph having A nodes labelled from 1 to A with M edges given
 in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents 2 nodes
 B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:
The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables
 make sure to clear them.

Problem Constraints
1 <= A, M <= 3105
1 <= B[i][0], B[i][1] <= A

Input Format
 The first argument given is an integer A representing the number of nodes in the graph.
 The second argument given is an matrix B of size M x 2 which represents the M
  edges such that there is a edge between node B[i][0] and node B[i][1].

Output Format
 Return 1 if cycle is present else return 0.
"""

from collections import deque


class Graph:
    def __init__(self, vertex_count, edges):
        self.map_dict = dict()
        self.add_edges(edges)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])
            self.add_edge(edge[1], edge[0])

    def add_edge(self, a, b):
        adj_list = self.map_dict.get(a, None)
        if adj_list is None:
            adj_list = list()
        adj_list.append(b)
        self.map_dict[a] = adj_list


class Djset:
    def __init__(self, count):
        self.parent = [i for i in range(count+1)]
        self.rank = [1 for i in range(count+1)]

    def find_parent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        parent_i = self.find_parent(i)
        parent_j = self.find_parent(j)
        if parent_i == parent_j:
            return True
        if self.rank[parent_i] > self.rank[parent_j]:
            self.parent[parent_j] = parent_i
        elif self.rank[parent_i] < self.rank[parent_j]:
            self.parent[parent_i] = parent_j
        else:
            self.parent[parent_j] = parent_i
            self.rank[parent_i] += 1
        return False


def is_cycle_dfs(graph, cur_ver, visited, parent):
    if visited[cur_ver]:
        return True
    visited[cur_ver] = True
    adj_vertexs = graph.map_dict.get(cur_ver, None)
    if adj_vertexs:
        for adj in adj_vertexs:
            if not visited[adj]:
                if is_cycle_dfs(graph, adj, visited, cur_ver):
                    return True
            elif adj != parent:
                return True
    return False


def is_cycle_bfs(graph, cur_ver, visited, parent):
    if visited[cur_ver]:
        return True
    que = deque()
    que.append(cur_ver)
    parent[cur_ver] = None
    visited[cur_ver] = True
    while len(que) > 0:
        temp = que.popleft()
        adj_vertexs = graph.map_dict.get(temp, None)
        if adj_vertexs:
            for adj in adj_vertexs:
                if not visited[adj]:
                    que.append(adj)
                    visited[adj] = True
                    parent[adj] = temp
                elif parent[temp] != adj:
                    return True
    return False


class Solution:

    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        # djset = Djset(A)
        # for edge in B:
        #     if djset.union(edge[0], edge[1]): return 1
        # return 0

        graph = Graph(A, B)
        visited = [False for i in range(A+1)]
        parent = [None for i in range(A+1)]
        for i in range(1, len(visited)):
            if not visited[i]:
                # if is_cycle_dfs(graph, i, visited, -1): return 1
                if is_cycle_bfs(graph, i, visited, parent):
                    return 1
        return 0

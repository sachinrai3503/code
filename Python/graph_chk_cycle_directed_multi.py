# https://www.interviewbit.com/problems/cycle-in-directed-graph/
# https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs/
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
"""
Given an directed graph having A nodes. A matrix B of size M x 2 is given which
 represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present
 else return 0.

NOTE:
    The cycle must contain atleast two nodes.
    There are no self-loops in the graph.
    There are no multiple edges between two nodes.
    The graph may or may not be connected.
    Nodes are numbered from 1 to A.
    Your solution will run on multiple test cases. If you are using global variables
     make sure to clear them.

Problem Constraints
    2 <= A <= 105
    1 <= M <= min(200000,A(A-1))
    1 <= B[i][0], B[i][1] <= A

Input Format
    The first argument given is an integer A representing the number of nodes in the graph.
    The second argument given a matrix B of size M x 2 which represents the M edges
    such that there is a edge directed from node B[i][0] to node B[i][1].

Output Format
    Return 1 if cycle is present else return 0.
"""
from collections import deque
import sys

sys.setrecursionlimit(10**6) 

class Graph:
    def __init__(self, vertex_count, edges):
        self.vertex_count = vertex_count
        self.map_dict = dict()
        self.in_degree = [0 for i in range(vertex_count+1)]
        self.add_edges(edges)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1])
            self.in_degree[edge[1]]+=1

    def add_edge(self, a, b):
        adj_list = self.map_dict.get(a, None)
        if adj_list is None:
            adj_list = list()
        adj_list.append(b)
        self.map_dict[a] = adj_list

def is_cycle_dfs(graph, cur_ver, visited, rec_stack):
    # print(cur_ver)
    if rec_stack[cur_ver]: return True
    if visited[cur_ver]: return False
    rec_stack[cur_ver] = True
    visited[cur_ver] = True
    adj_ver = graph.map_dict.get(cur_ver, None)
    if adj_ver:
        for adj in adj_ver:
            if is_cycle_dfs(graph, adj, visited, rec_stack): return True
    rec_stack[cur_ver] = False
    return False
    
def is_cycle_bfs(graph):
    count = 0
    que = deque()
    for i in range(1, len(graph.in_degree)):
        if graph.in_degree[i]==0: que.append(i)
    while len(que)>0:
        temp = que.popleft()
        count+=1
        adj_ver = graph.map_dict.get(temp, None)
        if adj_ver:
            for adj in adj_ver:
                graph.in_degree[adj]-=1
                if graph.in_degree[adj]==0: que.append(adj)
    if count==graph.vertex_count: return False
    return True
        
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        graph     = Graph(A, B)
        # print(graph.map_dict)
        # visited   = [False for i in range(A+1)]
        # rec_stack = [False for i in range(A+1)]
        # for i in range(1, len(visited)):
        #     if not visited[i]:
        #         if is_cycle_dfs(graph, i, visited, rec_stack): return 1
        # return 0
        
        if is_cycle_bfs(graph): return 1
        return 0
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths
"""
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes
 ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether 
 there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is
 a path for queries[j] is true, and false otherwise.

Example 1:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with
 distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for
 this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for
 this query.

Example 2:
Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Explanation: The above figure shows the given graph.

Constraints:
2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.
"""

from collections import defaultdict
from typing import List
from sys import maxsize

class DJ_Set:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]
        self.rank = [1 for i in range(self.n)]
    
    def find_parent(self, i):
        if self.parent[i]==i: return i
        self.parent[i] = self.find_parent(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find_parent(i)
        pj = self.find_parent(j)
        if pi==pj: return False
        rank_i = self.rank[pi]
        rank_j = self.rank[pj]
        if rank_i>rank_j:
            self.parent[pj] = pi
        elif rank_i<rank_j:
            self.parent[pi] = pj
        else:
            self.parent[pj] = pi
            self.rank[pi]+=1
        return True

    def is_connected(self, i, j):
        return self.find_parent(i)==self.find_parent(j)

class Graph:
    def __init__(self, n, edgesList):
        self.n = n
        # self.data = defaultdict(list)
        self.path_dist = {(i,i):0 for i in range(self.n)}
        self.add_edges(edgesList)
    
    def add_edges(self, edgesList):
        for u,v,d in edgesList:
            # self.add_edge(u,v)
            # self.add_edge(v,u)
            self.path_dist[(u,v)] = min(self.path_dist.get((u,v), maxsize), d)
            self.path_dist[(v,u)] = min(self.path_dist.get((v,u), maxsize), d)
    
    # def add_edge(self, u, v, d):
    #     self.data[u].append(v)
    
    def get_dist(self, u, v):
        return self.path_dist.get((u,v), maxsize)

class Solution:

    def get_all_pair_path_with_min_dist(self, graph):
        n = graph.n
        dp = [[graph.get_dist(i, j) for j in range(n)] for i in range(n)]
        # print(f'{dp=}')
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], max(dp[i][k], dp[k][j]))
        # print(f'{dp=}')
        return dp
        
    # This will time out
    def distanceLimitedPathsExist_FW(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = Graph(n, edgeList)
        # print(f'{graph.path_dist=}')
        dist = self.get_all_pair_path_with_min_dist(graph)
        # return [False, True, False, False, True, False, False, False, True, False, True, True, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, True, False, True, False, False, True, True, True, False, False, False, True, False, True, True, True, False, False, True, True, False, True, True, False, True, True, False, False, True, True, True, True, False, True, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, True, False, True, False, True, True, False, False, False, False, True, True, True, False, False, False, False, True, False, True, False, True, False, True, False, False, False, True, False, False, True, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, False, True, True, True, False, True, True, False, True, False, False, True, False, False, True, False, True, True, True, True, False, False, True, False, True, False, False, True, True, False, True, False, False, True, True, False, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, True, True, True, True, True, True, False, False, False, False, True, False, False, True, True, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, False, False, False, True, False, True, True, True, False, False, True, False, True, False, False, True, False, False, False, False, True, False, True, True, False, True, False, True, True, True, True, True, True, True, False, False, False, False, False, False, True, False, True, True, False, True, True, True, False, False, False, True, False, True, True, True, True, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, True, False, False, True, False, True, False, True, True, False, False, True, False, False, True, False, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, True, False, True, False, True, True, False, True, True, False, True, False, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, True, True, True, False, True, True, False, False, True, True, True, False, False, True, True, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, True, True, False, True, True, False, True, True, False, False, True, False, True, False, False, True, False, False, False, True, False, False, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, True, False, True, True, True, False, True, False, False, False, True, False, False, True, False, False, True, True, False, False, True, False, True, False, True, True, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, True, False, False, True, False, True, False, True, True, False, False, False, False, False, False, True, False, True, True, False, False, True, True, True, False, False, True, True, False, True, True, False, False, True, True, False, True, False, True, True, False, False, True, False, False, False, True, False, False, False, False, False, True, False, True, True, True, False, False, False, True, False, True, True, False, False, False, True, True, False, True, True, False, False, True, False, False, True, True, True, False, False, False, False, False, True, False, True, False, True, False, True, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, True, False, False, False, True, False, False, False, True, True, True, True, False, False, True, True, True, False, True, True, True, False, True, False, False, True, True, False, False, False, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, True, True, True, True, True, False, False, False, False, False, True, True, False, False, False, False, True, True, True, False, False, True, False, False, False, True, True, False, True, False, True, False, False, False, False, True, True, False, False, False, False, False, False, True, False, False, False, True, True, True, False, False, True, False, True, True, False, False, True, True, True, False, False, True, False, True, False, True, True, True, False, False, False, False, True, True, True, True, True, True, False, True, True, True, False, True, True, True, False, False, False, False, True, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True, False]
        return [True if dist[u][v]<d else False for u,v,d in queries]
    
    def compute_distance_for(self, graph, distance_map, source, u, dist, visited):
        # print(f'{u=} {dist=} {visited=}')
        visited.add(u)
        for v,w in graph[u]:
            # print(f'-- {v=} {w=} {visited=}')
            if v in visited: continue
            distance_map[source][v] = max(dist, w)
            self.compute_distance_for(graph, distance_map, source, v, distance_map[source][v], visited)

    # This too will timeout
    def distanceLimitedPathsExist1(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        op = list()
        dj_set = DJ_Set(n)
        graph = defaultdict(list) # u : (v,w), (v1, w1)
        edgeList.sort(key = lambda x:x[2])
        # print(f'{edgeList=}')
        for u,v,w in edgeList:
            if dj_set.union(u,v):
                graph[u].append((v,w))
                graph[v].append((u,w))
        # print(f'{graph=}')
        distance_map = dict() # (v : {u:d1, u2:d2}, v2: {u:d1, u2:d2}}
        for u,v,w in queries:
            # print(f'{u=} {v=} {w=}')
            result = False
            if dj_set.is_connected(u,v):
                if u in distance_map:
                    if distance_map[u][v]<w:
                        result = True
                elif v in distance_map:
                    if distance_map[v][u]<w:
                        result = True
                else:
                    distance_map[u] = dict()
                    self.compute_distance_for(graph, distance_map, u, u, 0, set())
                    if distance_map[u][v]<w:
                        result = True
                    # print(f'{distance_map=}')
            op.append(result)
        return op

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dj_set = DJ_Set(n)
        edges_len = len(edgeList)
        queries_len = len(queries)
        edgeList.sort(key = lambda x:x[2])
        queries_index = [i for i in range(queries_len)]
        queries_index.sort(key = lambda x:queries[x][2])
        op = [None for i in range(queries_len)]
        # print(f'{edgeList=}')
        # print(f'{queries_index=}')
        i = 0
        for j in queries_index:
            u,v,l = queries[j]
            while i<edges_len and edgeList[i][2]<l:
                dj_set.union(edgeList[i][0],edgeList[i][1])
                i+=1
            op[j] = dj_set.is_connected(u,v)
        return op
# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node
"""
There is an undirected weighted connected graph. You are given a positive integer n
 which denotes that the graph has n nodes labeled from 1 to n, and an array edges
 where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes
 ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] 
 such that z0 = start and zk = end and there is an edge between zi and zi+1 where
 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let
 distanceToLastNode(x) denote the shortest distance of a path between node n and node x.
A restricted path is a path that also satisfies that
 distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may
 be too large, return it modulo 109 + 7.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode
 value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode 
 value in blue. The only restricted path is 1 --> 3 --> 7.

Constraints:
1 <= n <= 2 * 104
n - 1 <= edges.length <= 4 * 104
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 105
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
"""

from typing import List

class HeapNode:
    def __init__(self, data, dist, index=-1):
        self.data = data
        self.dist = dist
        self.index = index
    
    def __repr__(self):
        return f'data={self.data} dist={self.dist} index={self.index}'
        
class MinHeap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.max_size = size
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
    
    def compare(self, i, j):
        if self.data[i].dist>self.data[j].dist: return 1
        return -1
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.heapify(min_index)
    
    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            t_index = self.cur_size
            self.data[t_index] = node
            node.index = t_index
            self.cur_size+=1
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
        
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.heapify(0)
            temp.index = -1
            return temp
    
    def update_node(self, node):
        if not node:
            print(f'Node passed as {node} is invalid.')
            return
        else:
            t_index = node.index
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
    
class Graph:
    
    class EdgeInfo:
        def __init__(self, v, w):
            self.v = v
            self.w = w
        
        def __repr__(self):
            return f'v={self.v} w={self.w}'
    
    def __init__(self, n, edges):
        self.n = n
        self.data = dict()
        self.add_edges(edges)
        self.distanceToLastNode = [None for i in range(n)]
    
    def add_edges(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(u,Graph.EdgeInfo(v,w))
            self.add_edge(v,Graph.EdgeInfo(u,w))
    
    def add_edge(self, u, edge_info):
        adj_vertexs = self.data.get(u, [])
        adj_vertexs.append(edge_info)
        self.data[u] = adj_vertexs

    def get_adj_vertexs(self, u):
        return self.data.get(u, None)
    
    def set_distance_from_node(self, node):
        heap = MinHeap(self.n)
        visited = set()
        heap_node_map = dict()
        src_node = HeapNode(node, 0)
        heap.insert_in_heap(src_node)
        heap_node_map[node] = src_node
        while not heap.is_empty():
            # print(heap.data[:heap.cur_size])
            temp = heap.delete_top()
            t_node, t_dist = temp.data, temp.dist
            visited.add(t_node)
            self.distanceToLastNode[t_node-1] = t_dist
            adj_nodes = self.get_adj_vertexs(t_node)
            if not adj_nodes: continue
            for adj in adj_nodes:
                if adj.v in visited: continue
                adj_node = heap_node_map.get(adj.v, None)
                if adj_node is not None:
                    if adj_node.dist>(t_dist+adj.w):
                        adj_node.dist = t_dist+adj.w
                        heap.update_node(adj_node)
                else:
                    adj_node = HeapNode(adj.v, t_dist+adj.w)
                    heap.insert_in_heap(adj_node)
                    heap_node_map[adj.v] = adj_node
        
    def getDistanceToLastNode(self, node):
        return self.distanceToLastNode[node-1]
        
class Solution:
    
    def count_paths(self, graph, src):
        if src == self.target: 
            self.dp[src-1] = 1
            return 1
        if self.dp[src-1] is not None: return self.dp[src-1]
        paths = 0
        src_dist_to_last_node = graph.getDistanceToLastNode(src)
        adj_vertexs = graph.get_adj_vertexs(src)
        if not adj_vertexs: return 0
        for ver in adj_vertexs:
            ver_dist_to_last_node = graph.getDistanceToLastNode(ver.v)
            if src_dist_to_last_node>ver_dist_to_last_node:
                paths = (paths+self.count_paths(graph, ver.v))%1000000007
        self.dp[src-1] = paths
        return paths
    
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = Graph(n, edges)
        # print(graph.data)
        graph.set_distance_from_node(n)
        # print(graph.distanceToLastNode)
        self.dp = [None for i in range(n)]
        self.target = n
        self.count_paths(graph, 1)
        # print(self.dp)
        return self.dp[0]
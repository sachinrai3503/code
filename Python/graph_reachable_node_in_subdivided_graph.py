# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph
"""
You are given an undirected graph (the "original graph") with n nodes labeled from 
 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes,
 with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates 
 that there is an edge between nodes ui and vi in the original graph, and cnti is the 
 total number of new nodes that you will subdivide the edge into. Note that cnti == 0
 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. 
 The new nodes are x1, x2, ..., xcnti, and the new edges are
 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, 
 where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable
 from node 0 in the new graph.

Example 1:
Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

Example 2:
Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23

Example 3:
Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.
 
Constraints:
0 <= edges.length <= min(n * (n - 1) / 2, 104)
edges[i].length == 3
0 <= ui < vi < n
There are no multiple edges in the graph.
0 <= cnti <= 104
0 <= maxMoves <= 109
1 <= n <= 3000
"""

from sys import maxsize
from typing import List

class HeapNode:
    def __init__(self, vertex, dist = 0, index = -1):
        self.vertex = vertex
        self.dist = dist
        self.index = index
    
    def __repr__(self):
        return f'{self.vertex}:{self.index}'

class Heap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.maxsize = size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
    
    def is_full(self):
        return self.cur_size==self.maxsize
    
    def is_empty(self):
        return self.cur_size==0

    def compare(self, i, j):
        pass
    
    def heapify(self, index):
        pass
    
    def insert_in_heap(self, data:HeapNode):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            data.index = index
            self.cur_size+=1
            self.data[index] = data
            parent_index = (index-1)//2
            while index>0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2
    
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
            print(f'Invalid node {node}')
        else:
            parent_index = (node.index-1)//2
            index = node.index
            while index>0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

class MinHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def compare(self, i, j):
        if self.data[i].dist<self.data[j].dist: return -1
        if self.data[j].dist>self.data[j].dist: return 1
        return 0
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if index!=min_index:
            self.swap(index, min_index)
            self.heapify(min_index)

class Graph:

    class EdgeWeight:
        def __init__(self, weight):
            self.weight = weight

    def __init__(self, n, edges):
        self.n = n
        self.data = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for u,v,w in edges:
            edge_weight = Graph.EdgeWeight(w)
            self.add_edge(u,v,edge_weight)
            self.add_edge(v,u,edge_weight)

    def add_edge(self, u, v, w):
        adj_list = self.data.get(u, list())
        adj_list.append((v, w))
        self.data[u] = adj_list

    def get_adj_ver(self, u):
        return self.data.get(u, None)

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        count = 0
        graph = Graph(n, edges)
        heap = MinHeap(n)
        heap_node_map = dict()
        visited = set()
        src_heap_node = HeapNode(0, 0)
        heap.insert_in_heap(src_heap_node)
        heap_node_map[0] = src_heap_node
        while not heap.is_empty():
            temp = heap.delete_top()
            count+=1
            src_vertex, src_dist = temp.vertex, temp.dist
            visited.add(temp.vertex)
            adj_vertexs = graph.get_adj_ver(src_vertex)
            if not adj_vertexs: continue
            for adj_ver, adj_edge_weight in adj_vertexs:
                new_dist = src_dist + adj_edge_weight.weight + 1
                t_count = min(maxMoves - src_dist, adj_edge_weight.weight)
                count+=t_count
                adj_edge_weight.weight = max(0, adj_edge_weight.weight - t_count)
                if new_dist>maxMoves or adj_ver in visited: continue
                adj_ver_heap_node = heap_node_map.get(adj_ver, None)
                if adj_ver_heap_node is not None:
                    if new_dist<adj_ver_heap_node.dist:
                        adj_ver_heap_node.dist = new_dist
                        heap.update_node(adj_ver_heap_node)
                else:
                    adj_ver_heap_node = HeapNode(adj_ver, new_dist)
                    heap.insert_in_heap(adj_ver_heap_node)
                    heap_node_map[adj_ver] = adj_ver_heap_node
        return count
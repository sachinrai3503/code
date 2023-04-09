# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination
"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with 
 bi-directional roads between some intersections. The inputs are generated such 
 that you can reach any intersection from any other intersection and that there
 is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei]
 means that there is a road between intersections ui and vi that takes timei minutes to
 travel. You want to know in how many ways you can travel from intersection 0 to 
 intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of
 time. Since the answer may be large, return it modulo 109 + 7.

Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 
 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:
Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 
Constraints:
1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.
"""
from typing import List

class HeapNode:
    def __init__(self, node, dist, path_count=0, index=-1):
        self.node = node
        self.dist = dist
        self.path_count = path_count
        self.index = index
    
    def __repr__(self):
        return f'node={self.node} dist={self.dist} index={self.index} path_count={self.path_count}'
        
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
    
class Solution:
    
    def count_shortest_paths(self, node):
        heap = MinHeap(self.n)
        visited = set()
        heap_node_map = dict()
        src_node = HeapNode(node, 0, 1)
        heap.insert_in_heap(src_node)
        heap_node_map[node] = src_node
        while not heap.is_empty():
            # print(heap.data[:heap.cur_size])
            temp = heap.delete_top()
            t_node, t_dist, t_path_count = temp.node, temp.dist, temp.path_count
            visited.add(t_node)
            self.path_counts[t_node] = t_path_count
            adj_nodes = self.graph.get_adj_vertexs(t_node)
            if not adj_nodes: continue
            for adj in adj_nodes:
                if adj.v in visited: continue
                adj_node = heap_node_map.get(adj.v, None)
                if adj_node is not None:
                    if adj_node.dist>(t_dist+adj.w):
                        adj_node.dist = t_dist+adj.w
                        adj_node.path_count = t_path_count
                        heap.update_node(adj_node)
                    elif adj_node.dist==(t_dist+adj.w):
                        adj_node.path_count = (adj_node.path_count + t_path_count)%1000000007
                else:
                    adj_node = HeapNode(adj.v, t_dist+adj.w, t_path_count)
                    heap.insert_in_heap(adj_node)
                    heap_node_map[adj.v] = adj_node
            
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        self.n = n
        self.graph = Graph(n,    roads)
        # print(self.graph.data)
        self.path_counts = [0 for i in range(n)]
        self.count_shortest_paths(0)
        # print(self.path_counts)
        return self.path_counts[-1]
        
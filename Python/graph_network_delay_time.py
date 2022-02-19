# https://leetcode.com/problems/network-delay-time
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7
# https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8
# https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm
"""
You are given a network of n nodes, labeled from 1 to n. You are also given times,
 a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the
 source node, vi is the target node, and wi is the time it takes for a signal to
 travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n
 nodes to receive the signal. If it is impossible for all the n nodes to receive the
 signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

# Below sol is bases on dijkstra algo.

from sys import maxsize

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
    
    def __repr__(self):
        return str(self.vertex) + ":" + str(self.weight)

class Graph:
    def __init__(self, n, edges):
        self.edges = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for edge in edges:
            u, v, w = edge
            self.add_edge(u,v,w)
    
    def add_edge(self, u, v, w):
        edges_list = self.edges.get(u, list())
        edges_list.append(Edge(v, w))
        self.edges[u] = edges_list

    def get_edges(self, u):
        return self.edges.get(u, None)
        
class HeapData:
    def __init__(self, vertex, dist, index=-1):
        self.vertex = vertex
        self.dist = dist
        self.index = index
    
    def __repr__(self):
        return str(self.vertex) + ":" + str(self.dist) + ":" + str(self.index)
        
class Heap:
    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.cur_size = 0
        self.max_size = n
    
    def is_full(self):
        return self.cur_size==self.max_size

    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index = i
        self.data[j].index = j
        
    def minHeapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].dist<self.data[min_index].dist:
            min_index = left
        if right<self.cur_size and self.data[right].dist<self.data[min_index].dist:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.minHeapify(min_index)
            
    def insert(self, data):
        if self.is_full():
            print('Full')
            return
        data.index = self.cur_size
        self.data[self.cur_size] = data
        self.cur_size+=1
        index = self.cur_size-1
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].dist>self.data[index].dist:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].dist>self.data[index].dist:
            self.swap(parent_index, index)
    
    def delete(self):
        if self.is_empty():
            print('Empty')
            return None
        temp = self.data[0]
        self.cur_size-=1
        self.swap(0, self.cur_size)
        self.minHeapify(0)
        temp.index = -1
        return temp
    
    def update(self, index):
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].dist>self.data[index].dist:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].dist>self.data[index].dist:
            self.swap(parent_index, index)
        
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = Graph(n, times)
        # print(graph.edges)
        visited = [False for i in range(n+1)]
        heap_nodes = [None for i in range(n+1)]
        max_time = -maxsize
        min_heap = Heap(n)
        for i in range(1, n+1):
            heap_node = None
            if i==k: heap_node = HeapData(i, 0)
            else: heap_node = HeapData(i, maxsize)
            min_heap.insert(heap_node)
            heap_nodes[i] = heap_node
        while not min_heap.is_empty():
            # print(min_heap.data[:min_heap.cur_size])
            temp = min_heap.delete()
            # print('temp=',temp)
            visited[temp.vertex] = True
            max_time = max(max_time, temp.dist)
            edge_list = graph.get_edges(temp.vertex)
            if edge_list is not None:
                for edge in edge_list:
                    if visited[edge.vertex]: continue
                    t_heap_node = heap_nodes[edge.vertex]
                    t_dist = temp.dist + edge.weight
                    if t_dist<t_heap_node.dist:
                        t_heap_node.dist = t_dist
                        min_heap.update(t_heap_node.index)
        if max_time==maxsize: return -1
        return max_time
            
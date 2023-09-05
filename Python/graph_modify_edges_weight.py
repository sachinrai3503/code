# https://leetcode.com/problems/modify-graph-edge-weights
"""
You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1,
 and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge 
 between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer 
values in the range [1, 2 * 109] so that the shortest distance between the nodes source
 and destination becomes equal to an integer target. If there are multiple modifications
 that make the shortest distance between source and destination equal to target, any of
 them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible
  to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.

Example 1:
Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, 
 destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the
 distance from 0 to 1 equal to 5.

Example 2:
Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.

Example 3:
Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
 

Constraints:
1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges
"""

from sys import maxsize
from typing import List

class HeapNode:
    def __init__(self, ver, cost, index=-1):
        self.ver = ver
        self.cost = cost
        self.index = index
    
    def __repr__(self):
        return f'{self.ver}:{self.cost}:{self.index}'

class Heap:
    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.cur_size = 0
        self.max_size = n
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = i, j
    
    def compare(self, i, j):
        pass
    
    def heapify(self, index):
        pass
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def insert_in_heap(self, heap_node):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            heap_node.index = index
            self.cur_size+=1
            self.data[index] = heap_node
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
        index = node.index
        parent_index = (index-1)//2
        while index>0 and self.compare(index, parent_index)==-1:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = (index-1)//2

class MinHeap(Heap):
    def __init__(self, n):
        Heap.__init__(self, n)
    
    def compare(self, i, j):
        if self.data[i].cost<self.data[j].cost: return -1
        if self.data[i].cost>self.data[j].cost: return 1
        return 0
    
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

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.fixed_edges_data = dict()
        self.dynamic_edges_data = dict()
        self.add_edges(edges)
    
    def add_edges(self, edges):
        for u,v,w in edges:
            if w!=-1:
                self.add_edge(u,v,w,self.fixed_edges_data)
                self.add_edge(v,u,w,self.fixed_edges_data)
            else:
                self.add_edge(u,v,w,self.dynamic_edges_data)
                self.add_edge(v,u,w,self.dynamic_edges_data)

    def add_edge(self, u, v, w, edge_dict):
        adjs_vers = edge_dict.get(u, list())
        adjs_vers.append((v,w))
        edge_dict[u] = adjs_vers
    
    def get_fixed_adjs(self, u):
        return self.fixed_edges_data.get(u, None)

    def get_dynamic_adjs(self, u):
        return self.dynamic_edges_data.get(u, None)

class Solution:

    def min_cost_to_reach_via_fixed_cost_edges(self, n, graph, source):
        heap = MinHeap(n)
        heap_node_dict = dict()
        visited = set()
        src_heap_node = HeapNode(source, 0)
        heap.insert_in_heap(src_heap_node)
        heap_node_dict[source] = src_heap_node
        while not heap.is_empty():
            temp = heap.delete_top()
            u, u_cost = temp.ver, temp.cost
            visited.add(u)
            adj_vertexs = graph.get_fixed_adjs(u)
            if not adj_vertexs: continue
            for v, w in adj_vertexs:
                if v in visited: continue
                v_heap_node = heap_node_dict.get(v, None)
                if v_heap_node is None:
                    v_heap_node = HeapNode(v, u_cost+w)
                    heap.insert_in_heap(v_heap_node)
                    heap_node_dict[v] = v_heap_node
                elif (u_cost+w)<v_heap_node.cost:
                    v_heap_node.cost = u_cost+w
                    heap.update_node(v_heap_node)
        return heap_node_dict

    def min_cost_to_reach_via_all_edges(self, n, graph, source, act_src_dist_dict, target, op):
        heap = MinHeap(n)
        heap_node_dict = dict()
        visited = set()
        src_heap_node = HeapNode(source, 0)
        heap.insert_in_heap(src_heap_node)
        heap_node_dict[source] = src_heap_node
        while not heap.is_empty():
            # print(f'{heap.data[:heap.cur_size]=}')
            temp = heap.delete_top()
            u, u_cost = temp.ver, temp.cost
            visited.add(u)
            adj_vertexs = graph.get_fixed_adjs(u)
            if adj_vertexs:
                for v, w in adj_vertexs:
                    if v in visited: continue
                    v_heap_node = heap_node_dict.get(v, None)
                    if v_heap_node is None:
                        v_heap_node = HeapNode(v, u_cost+w)
                        heap.insert_in_heap(v_heap_node)
                        heap_node_dict[v] = v_heap_node
                    elif (u_cost+w)<v_heap_node.cost:
                        v_heap_node.cost = u_cost+w
                        heap.update_node(v_heap_node)
                    op.append((u,v,w))
            # print(f'>>{u=} {op=}')
            adj_vertexs = graph.get_dynamic_adjs(u)
            if adj_vertexs:
                for v, w in adj_vertexs:
                    if v in visited: continue
                    v_temp_node = act_src_dist_dict.get(v, None)
                    if v_temp_node is None:
                        w = 1
                    else:
                        w = max(1, target - (u_cost + v_temp_node.cost))
                    v_heap_node = heap_node_dict.get(v, None)
                    if v_heap_node is None:
                        v_heap_node = HeapNode(v, u_cost+w)
                        heap.insert_in_heap(v_heap_node)
                        heap_node_dict[v] = v_heap_node
                    elif (u_cost+w)<v_heap_node.cost:
                        v_heap_node.cost = u_cost+w
                        heap.update_node(v_heap_node)
                    op.append((u,v,w))
            # print(f'>>>>>{u=} {op=}')
        return heap_node_dict

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        op = list()
        graph = Graph(n, edges)
        min_cost_via_fixed_edge = self.min_cost_to_reach_via_fixed_cost_edges(n, graph, source)
        if min_cost_via_fixed_edge.get(destination, HeapNode(-11, maxsize)).cost<target: return [] # Fixed edge path with cost<target
        # print(f'{min_cost_via_fixed_edge=}')
        min_cost_via_all_edge = self.min_cost_to_reach_via_all_edges(n, graph, destination, min_cost_via_fixed_edge, target, op)
        # print(f'{min_cost_via_all_edge=}')
        if min_cost_via_all_edge.get(source, HeapNode(-11, maxsize)).cost>target: return []
        return op
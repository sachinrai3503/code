# https://leetcode.com/problems/min-cost-to-connect-all-points
# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5
# https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6
"""
You are given an array points representing integer coordinates of some points
 on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
 between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if
 there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 
Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""

from sys import maxsize

class HeapNode:
    def __init__(self, node, key, index=-1):
        self.node = node
        self.key = key
        self.index = index

    def __str__(self):
        return ':'.join([str(self.node), str(self.key), str(self.index)])
        
    def __repr__(self):
        return self.__str__()
        
class Heap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.max_size = size
        self.cur_size = 0
    
    def is_empty(self):
        return self.cur_size==0

    def is_full(self):
        return self.cur_size==self.max_size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index

    def min_heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].key<self.data[min_index].key:
            min_index = left
        if right<self.cur_size and self.data[right].key<self.data[min_index].key:
            min_index = right
        if min_index!=index:
            self.swap(index, min_index)
            self.min_heapify(min_index)
        
    def insert_heap(self, node):
        if self.is_full():
            print('Full')
            return
        else:
            t_index = self.cur_size
            self.data[t_index] = node
            node.index = t_index
            self.cur_size+=1
            parent_index = (self.cur_size-2)//2
            while parent_index>0 and self.data[parent_index].key>self.data[t_index].key:
                self.swap(parent_index, t_index)
                t_index = parent_index
                parent_index = (parent_index-1)//2
            if  parent_index==0 and self.data[parent_index].key>self.data[t_index].key:
                self.swap(parent_index, t_index)
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.min_heapify(0)
            temp.index = -1
            return temp
    
    def update_index(self, index):
        if self.is_empty():
            print('Empty')
            return
        else:
            t_index = index
            parent_index = (index-1)//2
            while parent_index>0 and self.data[parent_index].key>self.data[t_index].key:
                self.swap(parent_index, t_index)
                t_index = parent_index
                parent_index = (parent_index-1)//2
            if  parent_index==0 and self.data[parent_index].key>self.data[t_index].key:
                self.swap(parent_index, t_index)
        
class Solution:
    
    def dist(self, point_a, point_b):
        return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])
    
    # This uses prims algo to connect all the nodes as MST
    def minCostConnectPoints1(self, points: list[list[int]]) -> int:
        min_cost = 0
        n = len(points)
        heap = Heap(n)
        heap_nodes = [None for i in range(n)]
        for i in range(n):
            key = maxsize
            if i==0: key = 0
            heap_nodes[i] = HeapNode(i, key)
            heap.insert_heap(heap_nodes[i])
        while not heap.is_empty():
            # print( heap.data[:heap.cur_size])
            temp = heap.delete_top()
            # print(temp, heap.data[:heap.cur_size])
            heap_nodes[temp.node] = None
            min_cost+=temp.key
            for i in range(n):
                if i==temp.node or heap_nodes[i] is None: continue
                t_key = self.dist(points[temp.node], points[i])
                if t_key<heap_nodes[i].key:
                    heap_nodes[i].key = t_key
                    heap.update_index(heap_nodes[i].index)
            #         print(i,heap.data[:heap.cur_size])
            # print('-----------------------')
        return min_cost
    
    def update(self, vertex_min_weight_cut_dict, i, j, t_dist):
        value = vertex_min_weight_cut_dict.get(i, [-1, maxsize])
        if t_dist<value[1]:
            value[0], value[1] = j, t_dist
        vertex_min_weight_cut_dict[i] = value
    
    # Wrong approach - TC - [[-2,0],[-1,0],[1,0],[2,0]]
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        min_cost = 0
        n = len(points)
        vertex_min_weight_cut_dict = dict() # u:[v,w]
        covered_edges = set()
        for i in range(n):
            for j in range(i+1, n):
                t_dist = self.dist(points[i], points[j])
                self.update(vertex_min_weight_cut_dict, i, j, t_dist)
                self.update(vertex_min_weight_cut_dict, j, i, t_dist)
            print(vertex_min_weight_cut_dict)
            u = i
            v, w = vertex_min_weight_cut_dict.get(i, [-1, 0]) # default to [-1,0] for TC with 1 vertex eg - [[3,2]]
            if (v,u) not in covered_edges:
                min_cost+=w
                covered_edges.add((u,v))
        return min_cost
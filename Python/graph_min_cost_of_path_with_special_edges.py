# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads
"""
You are given an array start where start = [startX, startY] represents your initial 
 position (startX, startY) in a 2D space. You are also given the array target where
 target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space
 (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where
 specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road
 can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use 
 each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

Example 1:
Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.

Example 2:
Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

Constraints:
start.length == target.length == 2
1 <= startX <= targetX <= 105
1 <= startY <= targetY <= 105
1 <= specialRoads.length <= 200
specialRoads[i].length == 5
startX <= x1i, x2i <= targetX
startY <= y1i, y2i <= targetY
1 <= costi <= 105
"""

from sys import maxsize
from typing import List

class HeapNode:
    def __init__(self, pos, cost, index=-1):
        self.pos = pos
        self.cost = cost
        self.index = index
    
    def __repr__(self):
        return f'{self.pos}:{self.cost}:{self.index}'

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
            self.data[0] = self.data[self.cur_size]
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

class Solution:

    def get_dist(self, src, dest):
        return abs(src[0]-dest[0]) + abs(src[1]-dest[1])

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        start, target = tuple(start), tuple(target)
        nodes_set = {start, target}
        special_edges = dict() # {(src, target) : cost, ...}
        for u,v,p,q,w in specialRoads:
            src, dest = (u,v), (p,q)
            if (src, dest) not in special_edges:
                special_edges[(src, dest)] = w
            elif w<special_edges[(src, dest)]:
                special_edges[(src, dest)] = w
            nodes_set.add(src)
            nodes_set.add(dest)
        n = len(nodes_set)
        heap = MinHeap(n)
        heap_node_dict = dict()
        visited = set()
        for node in nodes_set:
            start_node_dist = min(self.get_dist(start, node), special_edges.get((start, node), maxsize))
            heap_node = HeapNode(node, start_node_dist)
            heap.insert_in_heap(heap_node)
            heap_node_dict[node] = heap_node
        # print(f'{nodes_set=} {heap.data[:heap.cur_size]=}')
        while not heap.is_empty():
            temp = heap.delete_top()
            temp_pos, temp_cost = temp.pos, temp.cost
            visited.add(temp_pos)
            if temp_pos==target: return temp_cost
            for node in nodes_set:
                if node in visited: continue
                temp_node_dist = temp_cost + min(self.get_dist(temp_pos, node), special_edges.get((temp_pos, node), maxsize))
                node_heap_node = heap_node_dict.get(node, None)
                if temp_node_dist<node_heap_node.cost:
                    node_heap_node.cost = temp_node_dist
                    heap.update_node(node_heap_node)
        return -1
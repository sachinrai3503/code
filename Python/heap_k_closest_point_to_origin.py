# https://leetcode.com/problems/k-closest-points-to-origin
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
 return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

from sys import maxsize
from typing import List
from math import sqrt

class Heap:
    def __init__(self, size):
        self.cur_size = 0
        self.max_size = size
        self.data = [None for i in range(size)]
    
    def is_empty(self):
        return self.cur_size==0
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def get_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            return self.data[0]
        
    def heapify(self, index):
        pass
    
    def compare(self, i, j):
        pass
    
    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
            return
        else:
            index = self.cur_size
            self.data[index] = data
            self.cur_size+=1
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(parent_index, index)
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
            return temp

class MaxHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def compare(self, i, j):
        if self.data[i][2]<self.data[j][2]: return 1
        if self.data[i][2]>self.data[j][2]: return -1
        return 0
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        max_index = index
        if left<self.cur_size and self.compare(left, max_index)==-1:
            max_index = left
        if right<self.cur_size and self.compare(right, max_index)==-1:
            max_index = right
        if max_index!=index:
            self.swap(max_index, index)
            self.heapify(max_index)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = MaxHeap(k)
        for i, j in points:
            t_dist = sqrt((i**2)+(j**2))
            if not max_heap.is_full():
                max_heap.insert_in_heap((i, j, t_dist))
            elif max_heap.get_top()[2]>t_dist:
                max_heap.delete_top()
                max_heap.insert_in_heap((i, j, t_dist))
        op = list()
        while not max_heap.is_empty():
            top = max_heap.delete_top()
            op.append([top[0], top[1]])
        return op
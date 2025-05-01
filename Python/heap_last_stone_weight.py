# https://leetcode.com/problems/last-stone-weight
"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
 Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from sys import maxsize
from typing import List

class Heap:
    def __init__(self, size, data):
        self.cur_size = size
        self.max_size = size
        self.data = data
        self.build_heap()
    
    def is_empty(self):
        return self.cur_size==0
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def get_top(self):
        if self.is_empty():
            print("Empty")
            return None
        return self.data[0]
    
    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.cur_size+=1
            self.data[index] = data
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
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
            return temp
    
    def build_heap(self):
        if self.is_empty():
            print(f'Empty')
        else:
            parent_index = (self.cur_size-1)//2
            while parent_index>=0:
                self.heapify(parent_index)
                parent_index-=1

class MaxHeap(Heap):
    def __init__(self, size, data):
        Heap.__init__(self, size, data)
    
    def compare(self, i, j):
        if self.data[i]>self.data[j]: return -1
        if self.data[j]>self.data[i]: return 1
        return 0
    
    def heapify(self, index):
        left = (index*2)+1
        right = (index*2)+2
        max_index = index
        if left<self.cur_size and self.compare(left, max_index)==-1:
            max_index = left
        if right<self.cur_size and self.compare(right, max_index)==-1:
            max_index = right
        if index!=max_index:
            self.swap(max_index, index)
            self.heapify(max_index)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_len = len(stones)
        heap = MaxHeap(stones_len, stones)
        # print(f'{heap.data[:heap.cur_size]=}')
        while not heap.is_empty() and heap.cur_size>1:
            y = heap.delete_top()
            x = heap.delete_top()
            z = y - x
            if z:
                heap.insert_in_heap(z)
        return heap.get_top() if not heap.is_empty() else 0
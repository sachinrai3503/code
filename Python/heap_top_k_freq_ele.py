# https://leetcode.com/problems/top-k-frequent-elements
"""
Given an integer array nums and an integer k, return the k most frequent elements. 
 You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), 
 where n is the array's size.
"""

from typing import List

class HeapNode:
    def __init__(self, num, freq, index=-1):
        self.num = num
        self.freq = freq
        self.index = index
    
    def compare(self, node2):
        if self.freq<node2.freq: return -1
        if self.freq>node2.freq: return 1
        return 0

    def __repr__(self):
        return f'{self.num=} {self.freq=} {self.index=}'

class Heap:
    def __init__(self, max_size):
        self.data = [None for i in range(max_size)]
        self.cur_size = 0
        self.max_size = max_size

    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index = i
        self.data[j].index = j

    def heapify(self, index):
        pass
    
    def get_top(self):
        if self.is_empty():
            print('Empty')
            return None
        return self.data[0]

    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.data[index] = node
            node.index = index
            self.cur_size+=1
            parent_index = (index-1)//2
            while index>0 and node.compare(self.data[parent_index])==-1:
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
        if node is None:
            print('None node given')
        else:
            self.heapify(node.index)

class MinHeap(Heap):
    def __init__(self, max_size):
        Heap.__init__(self, max_size)
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].compare(self.data[min_index])==-1:
            min_index = left
        if right<self.cur_size and self.data[right].compare(self.data[min_index])==-1:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.heapify(min_index)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = MinHeap(k)
        heap_node_map = dict()
        for num in nums:
            num_heap_node = heap_node_map.get(num, HeapNode(num, 0))
            num_heap_node.freq+=1
            if num_heap_node.index!=-1:
                min_heap.update_node(num_heap_node)
            elif min_heap.cur_size<k:
                min_heap.insert_in_heap(num_heap_node)
            elif num_heap_node.freq>min_heap.get_top().freq:
                min_heap.delete_top()
                min_heap.insert_in_heap(num_heap_node)
            heap_node_map[num] = num_heap_node
            # print(min_heap.data)
            # print(heap_node_map)
        return [node.num for node in min_heap.data]
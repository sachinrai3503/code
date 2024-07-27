# https://leetcode.com/problems/total-cost-to-hire-k-workers
"""
You are given a 0-indexed integer array costs where costs[i] is the cost of
 hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k
 workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the 
first candidates workers or the last candidates workers. Break the tie by the
 smallest index.
 For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first 
 hiring session, we will choose the 4th worker because they have the lowest 
 cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the
 same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2].
 Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the 
 lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.

Return the total cost to hire exactly k workers.

Example 1:
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8].
 The lowest cost is 2, and we break the tie by the smallest index, which is 3. 
 The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. 
 The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The
 lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker 
 with index 3 was common in the first and last four workers.
The total hiring cost is 11.

Example 2:
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost
 is 1, and we break the tie by the smallest index, which is 0. 
 The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common 
 in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost
 is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the
 worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). 
 The total cost = 2 + 2 = 4.
The total hiring cost is 4.

Constraints:
1 <= costs.length <= 105 
1 <= costs[i] <= 105
1 <= k, candidates <= costs.length
"""

from sys import maxsize
from typing import List

class Heap:
    def __init__(self, size):
        self.cur_size = 0
        self.max_size = size
        self.data = [None for i in range(size)]

    def __repr__(self):
        return f'{self.data[:self.cur_size]}'

    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.heapify(0)
            return temp
    
    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.data[index] = data
            self.cur_size+=1
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

    def get_top(self):
        if self.is_empty():
            # print('None')
            return None
        return self.data[0]

class MinHeap(Heap):

    def heapify(self, i):
        left = i*2+1
        right = i*2+2
        min_index = i
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if min_index!=i:
            self.swap(min_index, i)
            self.heapify(min_index)

    def compare(self, i, j):
        if self.data[i]<self.data[j]: return -1
        if self.data[i]>self.data[j]: return 1
        return 0

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        length = len(costs)
        heap1 = MinHeap(candidates)
        heap2 = MinHeap(candidates)
        i, j = -1, length
        session = 0
        while session<k:
            while not heap1.is_full() and (i+1)<j:
                i+=1
                heap1.insert_in_heap(costs[i])
            while not heap2.is_full() and (j-1)>i:
                j-=1
                heap2.insert_in_heap(costs[j])
            left, right = heap1.get_top(), heap2.get_top()
            if left and (not right or (heap1.get_top()<=heap2.get_top())):
                total_cost+=heap1.delete_top()
            else:
                total_cost+=heap2.delete_top()
            session+=1
        return total_cost
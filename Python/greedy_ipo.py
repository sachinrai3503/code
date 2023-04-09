# https://leetcode.com/problems/ipo
"""
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares 
 to Venture Capital, LeetCode would like to work on some projects to increase its capital 
 before the IPO. Since it has limited resources, it can only finish at most k distinct projects
 before the IPO. Help LeetCode design the best way to maximize its total capital after
 finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum
 capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit
 and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final
 capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get
 the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

Example 2:
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
 
Constraints:
1 <= k <= 105
0 <= w <= 109
n == profits.length
n == capital.length
1 <= n <= 105
0 <= profits[i] <= 104
0 <= capital[i] <= 109
"""

from typing import List

class Heap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.max_size = size
    
    def compare(self, i, j):
        pass
    
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
        return self.data[0]

    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        t_index = index
        if left<self.cur_size and self.compare(t_index, left)==1:
            t_index = left
        if right<self.cur_size and self.compare(t_index, right)==1:
            t_index = right
        if t_index!=index:
            self.swap(t_index, index)
            self.heapify(t_index)

    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.data[index] = data
            self.cur_size+=1
            parent_index = (index-1)//2
            while index>0 and self.compare(parent_index, index)==1:
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
            self.swap(0, self.cur_size)
            self.heapify(0)
            return temp

class MinHeap(Heap):
    def __init__(self, n):
        Heap.__init__(self, n)

    def compare(self, i, j):
        if self.data[i][0]<self.data[j][0]: return -1
        if self.data[i][0]>self.data[j][0]: return 1
        if self.data[i][1]<self.data[j][1]: return 1
        if self.data[i][1]>self.data[j][1]: return -1
        return 0

class MaxHeap(Heap):
    
    def __init__(self, n):
        Heap.__init__(self, n)

    def compare(self, i, j):
        if self.data[i][1]<self.data[j][1]: return 1
        if self.data[i][1]>self.data[j][1]: return -1
        return 0

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        count = 0
        max_cap = w
        n = len(profits)
        min_heap = MinHeap(n)
        max_heap = MaxHeap(n)
        for i in range(n):
            min_heap.insert_in_heap((capital[i], profits[i]))
        # print(f'{min_heap.data[:min_heap.cur_size]=}')
        while count<k:
            while not min_heap.is_empty() and max_cap>=min_heap.get_top()[0]:
                max_heap.insert_in_heap(min_heap.delete_top())
            if not max_heap.is_empty():
                max_cap+=max_heap.delete_top()[1]
                count+=1
            else:
                break
        return max_cap
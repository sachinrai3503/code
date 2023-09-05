# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid
"""
You are given a m x n matrix grid consisting of non-negative integers where
 grid[row][col] represents the minimum time required to be able to visit the cell 
 (row, col), which means you can visit the cell (row, col) only when the time you
 visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must
 move to any adjacent cell in the four directions: up, down, left, and right. 
 Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of
 the matrix. If you cannot visit the bottom-right cell, then return -1.

Example 1:
Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.

Example 2:
Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.

Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0
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

    def get_cost(self, cur_cost, dest_cost):
        if cur_cost>dest_cost: return cur_cost
        if (cur_cost%2==0): return dest_cost if dest_cost%2==0 else (dest_cost+1)
        if (cur_cost%2==1): return dest_cost if dest_cost%2==1 else (dest_cost+1)

    def can_move(self, grid, row, col):
        if grid[0][1]>1 and grid[1][0]>1: return False
        return True

    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return True

    def minimumTime(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        if not self.can_move(grid, self.row, self.col): return -1
        adj_dir = [[0,-1],[-1,0],[0,1],[1,0]]
        heap = MinHeap(self.row*self.col)
        heap_nodes_dict = dict()
        visited = set()
        src_heap_node = HeapNode((0,0),0)
        heap.insert_in_heap(src_heap_node)
        heap_nodes_dict[(0,0)] = src_heap_node
        while not heap.is_empty():
            temp = heap.delete_top()
            temp_pos, temp_cost = temp.pos, temp.cost
            if temp_pos==(self.row-1, self.col-1): return temp_cost
            visited.add(temp_pos)
            for i, j in adj_dir:
                ti, tj = temp_pos[0] + i, temp_pos[1] + j
                if not self.is_valid(ti, tj) or (ti, tj) in visited: continue
                t_cost = self.get_cost(temp_cost+1, grid[ti][tj])
                t_heap_node = heap_nodes_dict.get((ti, tj), None)
                if t_heap_node is None:
                    t_heap_node = HeapNode((ti, tj), t_cost)
                    heap.insert_in_heap(t_heap_node)
                    heap_nodes_dict[(ti, tj)] = t_heap_node
                elif t_cost<t_heap_node.cost:
                    t_heap_node.cost = t_cost
                    heap.update_node(t_heap_node)
        return -1
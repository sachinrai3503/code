# https://leetcode.com/problems/path-with-minimum-effort/
"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array
 of size rows x columns, where heights[row][col] represents the height of cell (row, col).
 You are situated in the top-left cell, (0, 0), and you hope to travel to the 
 bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left,
 or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in 
 consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 
Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

# Below sol uses Dijkstras

from typing import List

# https://leetcode.com/problems/swim-in-rising-water/description/ - Related
class Heap:
    def __init__(self, size):
        self.data = [None for i in range(size)] # [[diff, (i, j), index], ...]
        self.max_size = size
        self.cur_size = 0
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i][2], self.data[j][2] = i, j
    
    def compare(self, i, j):
        pass
    
    def heapify(self, i):
        pass
    
    def insert_in_heap(self, data):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            self.cur_size+=1
            self.data[index] = data
            data[2] = index
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2
            return data
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.heapify(0)
            temp[2] = -1
            return temp

    def update(self, index):
        if self.is_empty():
            print('Empty1')
            return None
        else:
            parent_index = (index-1)//2
            while parent_index>=0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

class MinHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def compare(self, i, j):
        if self.data[i][0]<self.data[j][0]: return -1
        if self.data[i][0]>self.data[j][0]: return 1
        return 0
    
    def heapify(self, i):
        left = i*2 + 1
        right = i*2 + 2
        min_index = i
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if i!=min_index:
            self.swap(i, min_index)
            self.heapify(min_index)

class Solution:

    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return True

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        effort = 0
        self.row = len(heights)
        self.col = 0 if self.row==0 else len(heights[0])
        self.heights = heights
        adj = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        heap = MinHeap(self.row*self.col)
        pos_index_map = dict() # {(i,j):index, ...}
        visited_pos = set() # {(i, j), ...}
        pos_index_map[(0, 0)] = heap.insert_in_heap([0, (0, 0), -1])
        while not heap.is_empty():
            t_effort, t_pos, t_index = heap.delete_top()
            effort = max(effort, t_effort)
            visited_pos.add(t_pos)
            t_pos_i, t_pos_j = t_pos[0], t_pos[1]
            if t_pos_i==(self.row-1) and t_pos_j==(self.col-1): return effort
            for i, j in adj:
                ti, tj = t_pos_i + i, t_pos_j + j
                if self.is_valid(ti, tj) and (ti, tj) not in visited_pos:
                    t_pos_to_cur_pos_effort = abs(heights[t_pos_i][t_pos_j] - heights[ti][tj])
                    if (ti, tj) not in pos_index_map:
                        pos_index_map[(ti, tj)] = heap.insert_in_heap([t_pos_to_cur_pos_effort, (ti, tj), -1])
                    elif pos_index_map[(ti, tj)][0]>t_pos_to_cur_pos_effort:
                        pos_index_map[(ti, tj)][0] = t_pos_to_cur_pos_effort
                        # print(f'{t_pos_i=} {t_pos_j=} {ti=} {tj=} {pos_index_map=}')
                        heap.update(pos_index_map[(ti, tj)][2])
        return -1
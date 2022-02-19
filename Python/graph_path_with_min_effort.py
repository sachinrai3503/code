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

from sys import maxsize
        
class HeapData:
    def __init__(self, i, j, effort, index=-1):
        self.i = i
        self.j = j
        self.effort = effort
        self.index = index
    
    def __repr__(self):
        return str(self.i) + ":" + str(self.j) + ":" + str(self.effort) + ":" + str(self.index)
        
class Heap:
    def __init__(self, n):
        self.data = [None for i in range(n)]
        self.cur_size = 0
        self.max_size = n
    
    def is_full(self):
        return self.cur_size==self.max_size

    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index = i
        self.data[j].index = j
        
    def minHeapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.data[left].effort<self.data[min_index].effort:
            min_index = left
        if right<self.cur_size and self.data[right].effort<self.data[min_index].effort:
            min_index = right
        if min_index!=index:
            self.swap(min_index, index)
            self.minHeapify(min_index)
            
    def insert(self, data):
        if self.is_full():
            print('Full')
            return
        data.index = self.cur_size
        self.data[self.cur_size] = data
        self.cur_size+=1
        index = self.cur_size-1
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].effort>self.data[index].effort:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].effort>self.data[index].effort:
            self.swap(parent_index, index)
    
    def delete(self):
        if self.is_empty():
            print('Empty')
            return None
        temp = self.data[0]
        self.cur_size-=1
        self.swap(0, self.cur_size)
        self.minHeapify(0)
        temp.index = -1
        return temp
    
    def update(self, index):
        parent_index = (index-1)//2
        while parent_index>0 and self.data[parent_index].effort>self.data[index].effort:
            self.swap(parent_index, index)
            index = parent_index
            parent_index=(parent_index-1)//2
        if parent_index==0 and self.data[parent_index].effort>self.data[index].effort:
            self.swap(parent_index, index)

class Solution:
    
    def is_valid(self, i, j):
        if i<0 or i>=self.row: return False
        if j<0 or j>=self.col: return False
        return True
    
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        self.row = len(heights)
        self.col = 0 if self.row==0 else len(heights[0])
        adj = [[0,-1,0,1],[-1,0,1,0]]
        heap = Heap(self.row*self.col)
        heap_nodes = [[None for j in range(self.col)] for i in range(self.row)]
        visited = [[False for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                heap_node = None
                if i==0 and j==0: heap_node = HeapData(i,j,0)
                else: heap_node = HeapData(i,j,maxsize)
                heap.insert(heap_node)
                heap_nodes[i][j] = heap_node
        while not heap.is_empty():
            temp = heap.delete()
            if temp.i==self.row-1 and temp.j==self.col-1: return temp.effort
            for k in range(4):
                ti, tj = temp.i + adj[0][k], temp.j + adj[1][k]
                if self.is_valid(ti, tj) and not visited[ti][tj]:
                    t_effort = max(temp.effort, abs(heights[temp.i][temp.j]-heights[ti][tj]))
                    if heap_nodes[ti][tj].effort>t_effort:
                        heap_nodes[ti][tj].effort = t_effort
                        heap.update(heap_nodes[ti][tj].index)
        return -1
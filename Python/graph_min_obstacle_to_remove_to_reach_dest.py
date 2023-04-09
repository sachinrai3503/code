# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner
"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one
 of two values:
    0 represents an empty cell,
    1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper
 left corner (0, 0) to the lower right corner (m - 1, n - 1).

Example 1:
Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from sys import maxsize
from typing import List
from collections import deque

class HeapNode:
    def __init__(self, i, j, obstacle_count, index=-1):
        self.pos = (i, j)
        self.obstacle_count = obstacle_count
        self.index = index
    
    def __repr__(self):
        return f'data={self.pos} dist={self.obstacle_count} index={self.index}'
        
class MinHeap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.max_size = size
    
    def is_full(self):
        return self.cur_size==self.max_size
    
    def is_empty(self):
        return self.cur_size==0

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
    
    def compare(self, i, j):
        if self.data[i].obstacle_count>self.data[j].obstacle_count: return 1
        return -1
    
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
    
    def insert_in_heap(self, node):
        if self.is_full():
            print('Full')
        else:
            t_index = self.cur_size
            self.data[t_index] = node
            node.index = t_index
            self.cur_size+=1
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
        
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
        if not node:
            print(f'Node passed as {node} is invalid.')
            return
        else:
            t_index = node.index
            p_index = (t_index-1)//2
            while t_index>0 and self.compare(p_index, t_index)==1:
                self.swap(p_index, t_index)
                t_index = p_index
                p_index = (t_index-1)//2
    

class Solution:
    
    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return True
    
    # This is using dijkstra algo and will time out
    def minimumObstacles_1(self, grid: List[List[int]]) -> int:
        min_obstacle_count = maxsize
        self.grid = grid
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        dest_pos = (self.row-1, self.col-1)
        heap = MinHeap(self.row*self.col)
        heap_node_map = dict()
        visited = set()
        src_node = HeapNode(0, 0, 0)
        heap.insert_in_heap(src_node)
        heap_node_map[(0,0)] = src_node
        while not heap.is_empty():
            temp = heap.delete_top()
            t_pos, t_obstacle = temp.pos, temp.obstacle_count
            if t_pos==dest_pos:
                min_obstacle_count = t_obstacle
                break
            visited.add(t_pos)
            for direction in self.directions:
                ti, tj = t_pos[0] + direction[0], t_pos[1] + direction[1]
                if not self.is_valid(ti, tj): continue
                if (ti, tj) not in visited:
                    t_heap_node = heap_node_map.get((ti, tj), None)
                    if t_heap_node:
                        if t_heap_node.obstacle_count>(t_obstacle+grid[ti][tj]):
                            t_heap_node.obstacle_count=t_obstacle+grid[ti][tj]
                            heap.update(t_heap_node)
                    else:
                        t_heap_node = HeapNode(ti, tj, t_obstacle+grid[ti][tj])
                        heap.insert_in_heap(t_heap_node)
                        heap_node_map[(ti, tj)] = t_heap_node
        return min_obstacle_count
    
    # Using 0-1 BFS    
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        dest_pos = (self.row-1, self.col-1)
        que = deque()
        visited = set()
        que.append((0,0,0)) # [(i,j,cost)]
        visited.add((0,0))
        while que:
            temp_i, temp_j, temp_obs_count = que.popleft()
            for i, j in directions:
                ti, tj = temp_i + i, temp_j + j
                if not self.is_valid(ti, tj): continue
                if (ti, tj) in visited: continue
                if grid[ti][tj]==0: que.appendleft((ti, tj, temp_obs_count))
                else: que.append((ti, tj, temp_obs_count+1))
                visited.add((ti, tj))
                if (ti, tj)==dest_pos:
                    return temp_obs_count
        return None
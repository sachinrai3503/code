# https://www.lintcode.com/problem/803
# https://leetcode.com/problems/shortest-distance-from-all-buildings

"""
You want to build a house on an empty land which reaches all buildings in the shortest 
 amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
There will be at least one building. If it is not possible to build such house according
 to the above rules, return -1

Example
Example 1
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation:
In this example, there are three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel 
 distance of 3+3+1=7 is minimal. So return 7.

Example 2
Input: [[1,0],[0,0]]
Output: 1
In this example, there is one buildings at (0,0).
1 - 0
|   |
0 - 0
The point (1,0) or (0,1) is an ideal empty land to build a house, as the total travel
 distance of 1 is minimal. So return 1.
"""

from sys import maxsize
from collections import deque
from typing import (
    List,
)

class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n  = len(grid[0])
        op = [[[0,maxsize] for _ in range(n)] for _ in range(m)]
        count_1 = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, m, n, i, j, op)
                    count_1+=1
        # print(f'{op=}')
        return self.get_min(grid,op,m,n,count_1)
	
    def get_min(self, mat, op, row, col, count_1):
        _min = maxsize
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0 and op[i][j][0]==count_1:
                    _min = min(_min, op[i][j][1])
        return _min if _min!=maxsize else -1

    def bfs(self, grid, m, n, i, j, op):
        que = deque()
        visited = set()
        adj_dir = [[0,-1],[-1,0],[0,1],[1,0]]
        que.append((i,j))
        visited.add((i,j))
        que.append(None)
        dist=0
        while que[0]!=None:
            while que[0]!=None:
                temp_i, temp_j = que.popleft()
                for i, j in adj_dir:
                    ti, tj = temp_i + i, temp_j + j
                    if self.is_valid(ti, tj, m, n) and grid[ti][tj]==0 and (ti, tj) not in visited:
                        que.append((ti, tj))
                        visited.add((ti,tj))
                        op[ti][tj][0]+=1
                        op[ti][tj][1] = (op[ti][tj][1] + dist+1) if op[ti][tj][1]!=maxsize else (dist+1)
            que.popleft()
            dist+=1
            que.append(None)
	

    def is_valid(self, i, j, row, col):
        if i<0 or i>=row or j<0 or j>=col: return False
        return True


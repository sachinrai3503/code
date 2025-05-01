# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
"""
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). 
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0)
 to the lower right corner (m-1, n-1) given that you can eliminate at most k
 obstacles.
If it is not possible to find such walk return -1.

Example 1:
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 
Example 2:
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.

Constraints:
grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""

from collections import deque
from typing import List

class Solution:

    def is_valid(self, i, j):
        if i<0 or i>=self.m or j<0 or j>=self.n: return False
        return True

    def can_visit(self, i, j, k):
        if not self.is_valid(i, j): return False
        if (i, j) not in self.visited: return True if self.grid[i][j]==0 else (k>0)
        # if self.grid[i][j]==0 and self.visited[(i, j)]<k: return True
        # if self.grid[i][j]==1 and self.visited[(i, j)]<k: return True
        return self.visited[(i, j)]<k
        # return False


    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        path_len = 0
        self.grid = grid
        self.m = len(grid)
        self.n = 0 if self.m==0 else len(self.grid[0])
        self.adj = [(0,-1),(-1,0),(0, 1),(1, 0)]
        self.visited = dict() # {(i, j):k, ...}
        que = deque() # [((i,j), k), ...]
        que.append(((0,0), k))
        self.visited[(0,0)] = k
        que.append(None)
        while que[0]:
            while que[0]:
                pos, t_k = que.popleft()
                if pos[0]==(self.m-1) and pos[1]==(self.n-1): return path_len
                for i, j in self.adj:
                    ti, tj = pos[0] + i, pos[1] + j
                    if self.can_visit(ti, tj, t_k):
                        if grid[ti][tj]==0:
                            que.append(((ti, tj), t_k))
                            self.visited[(ti, tj)] = t_k
                        else:
                            que.append(((ti, tj), t_k-1))
                            self.visited[(ti, tj)] = t_k # note here not assigning t_k-1. Because in can_visit its t_k
            que.popleft()
            path_len+=1
            que.append(None)
            # print(f'{que=}')
            # print(f'{self.visited=}')
        return -1
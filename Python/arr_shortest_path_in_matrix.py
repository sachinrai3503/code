# https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""

from collections import deque

class Solution:
    
    def __init__(self):
        self.directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

    
    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return self.grid[i][j]==0
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        steps = 0
        self.grid = grid
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        que = deque()
        visited = set()
        if grid[0][0]==1 or grid[-1][-1]==1: return -1
        que.append((0,0))
        visited.add((0,0))
        que.append(None)
        while que[0]!=None:
            while que[0]!=None:
                i, j = que.popleft()
                if i==self.row-1 and j==self.col-1: return steps+1
                for direction in self.directions:
                    ti, tj = i+direction[0], j+direction[1]
                    if self.is_valid(ti, tj) and (ti, tj) not in visited:
                        que.append((ti, tj))
                        visited.add((ti, tj))
            que.popleft()
            steps+=1
            que.append(None)
        return -1
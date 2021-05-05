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
from sys import maxsize

def is_valid(row, col, i, j):
    if i<0 or i>=row: return False
    if j<0 or j>=col: return False
    return True

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        length = 0
        row = len(grid)
        col = 0 if row==0 else len(grid[0])
        adj_in = [[0,-1,0,1],[-1,0,1,0]]
        que = deque()
        obstacle_count = [[maxsize for j in range(col)] for i in range(row)]
        que.append([(0,0),0])
        obstacle_count[0][0] = 0
        null_node = [(maxsize, maxsize),maxsize]
        que.append(null_node)
        while len(que)>0 and que[0]!=null_node:
            que_node_map = dict()
            while len(que)>0 and que[0]!=null_node:
                t_node = que.popleft()
                i, j, cur_k = t_node[0][0], t_node[0][1], t_node[1]
                if i==row-1 and j==col-1: return length
                for p in range(4):
                    ti, tj = i+adj_in[0][p], j+adj_in[1][p]
                    if is_valid(row, col, ti, tj):
                        t_k = cur_k if grid[ti][tj]==0 else cur_k+1
                        if t_k<=k and t_k<obstacle_count[ti][tj]:
                            que_entry = que_node_map.get((ti,tj), None)
                            if not que_entry:
                                que_entry = [(ti,tj),t_k]
                                que.append(que_entry)
                            else: que_entry[1] = t_k
                            que_node_map[(ti,tj)] = que_entry
                            obstacle_count[ti][tj] = t_k
            que.popleft()
            length+=1
            que.append(null_node)
            que_node_map.clear()
        return -1
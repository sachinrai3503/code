# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
 The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches
 the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix
 heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
 north, south, east, and west if the neighboring cell's height is less than or equal to
 the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain 
 water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

from collections import deque
from typing import List

class Solution:

    def __init__(self):
        self.adj_dir = [(0,-1),(-1,0),(0,1),(1,0)]

    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return True

    def bfs(self, heights, que, visited):
        while que:
            # print(f'{que=} {visited=}')
            temp_i, temp_j = que.popleft()
            # print(f'{que=} {visited=}')
            for i, j in self.adj_dir:
                ti, tj = temp_i + i, temp_j + j
                if not self.is_valid(ti, tj) or (ti, tj) in visited: continue
                if heights[temp_i][temp_j]>heights[ti][tj]: continue
                que.append((ti, tj))
                visited.add((ti, tj))

    # For this DP approach won't work - Eg of DP - https://leetcode.com/problems/01-matrix
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.row = len(heights)
        self.col = 0 if self.row==0 else len(heights[0])
        pac_que = deque()
        alt_que = deque()
        pac_visited = set()
        alt_visited = set()
        j = 0
        while j<self.col:
            pac_que.append((0, j))
            pac_visited.add((0,j))
            alt_que.append((self.row-1, j))
            alt_visited.add((self.row-1, j))
            j+=1
        i = 1
        while i<self.row:
            pac_que.append((i,0))
            pac_visited.add((i,0))
            alt_que.append((self.row-i-1, self.col-1))
            alt_visited.add((self.row-i-1, self.col-1))
            i+=1
        # print(f'{pac_que=} {pac_visited=}')
        # print(f'{alt_que=} {alt_visited=}')
        self.bfs(heights, pac_que, pac_visited)
        self.bfs(heights, alt_que, alt_visited)
        return pac_visited.intersection(alt_visited)
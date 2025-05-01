# https://leetcode.com/problems/swim-in-rising-water
"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to 
 another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. 
 You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected. 

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
"""

import heapq
from typing import List

# https://leetcode.com/problems/path-with-minimum-effort/ - Related

class Solution:

    def is_valid(self, i, j):
        if i<0 or i>=self.n or j<0 or j>=self.n: return False
        return True
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        self.n = len(grid)
        adj = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        heap = [] # [(elavation, (i, j)), ...]
        visited = set() # {(i, j), ...}
        heapq.heappush(heap, (grid[0][0], (0,0)))
        visited.add((0, 0))
        while heap:
            t_elavation, pos = heapq.heappop(heap)
            t = max(t, t_elavation)
            if pos[0]==(self.n-1) and pos[1]==(self.n-1): return t
            for i, j in adj:
                ti, tj = pos[0] + i, pos[1] + j
                if self.is_valid(ti, tj) and (ti, tj) not in visited:
                    heapq.heappush(heap, (grid[ti][tj], (ti, tj)))
                    visited.add((ti, tj))
        return t
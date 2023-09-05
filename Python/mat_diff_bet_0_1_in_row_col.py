# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column
"""
You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:
Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.

Example 1:

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]

Example 2:
Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
"""

from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n  = len(grid[0])
        rows_info = [[0,0] for _ in range(m)]
        cols_info  = [[0,0] for _ in range(n)]
        op = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    rows_info[i][0]+=1
                    cols_info[j][0]+=1
                else:
                    rows_info[i][1]+=1
                    cols_info[j][1]+=1
        for i in range(m):
            for j in range(n):
                op[i][j] = rows_info[i][1] + cols_info[j][1] - rows_info[i][0] - cols_info[j][0]
        return op
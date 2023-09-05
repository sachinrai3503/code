# https://leetcode.com/problems/equal-row-and-column-pairs
"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
 such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the
 same order (i.e., an equal array). 

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""

from typing import List

class Solution:

    def get_colwise_count_map(self, grid, n):
        col_count_map = dict()
        for i in range(n):
            op = list()
            for j in range(n):
                op.append(str(grid[j][i]))
            op = '*'.join(op)
            count = col_count_map.get(op, 0)
            count+=1
            col_count_map[op] = count
        # print(f'{col_count_map=}')
        return col_count_map

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        col_count_map = self.get_colwise_count_map(grid, n)
        for i in range(n):
            op = list()
            for j in range(n):
                op.append(str(grid[i][j]))
            op = '*'.join(op)
            count+=col_count_map.get(op, 0)
        return count
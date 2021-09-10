# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
"""
Given an n x n binary grid, in one step you can choose two adjacent rows of
 the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the
 grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and
 ends at cell (n, n).

Example 1:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 200
grid[i][j] is 0 or 1
"""

def update(bit, length, index, value):
    while index<length:
        bit[index]+=value
        index = index + (index&-index)

def query(bit, length, index):
    _sum = 0
    while index>0:
        _sum+=bit[index]
        index = index - (index&-index)
    return _sum

class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        swap_count = 0
        n = len(grid)
        bit = [0 for i in range(n+1)]
        is_present = [None for i in range(n)]
        for row in range(n):
            o_count = 0
            for col in range(n-1, -1, -1):
                if grid[row][col]==0:   o_count+=1
                else:   break
            for x in range(min(n-1, o_count), -1, -1):
                if is_present[x] is None: 
                    is_present[x] = row+1
                    break
        # print(is_present)
        for item in is_present:
            if item is None: return -1
            swap_count+=query(bit, n+1, item)
            update(bit, n+1, item, 1)
        return swap_count
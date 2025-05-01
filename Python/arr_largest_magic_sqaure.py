# https://leetcode.com/problems/largest-magic-square
"""
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal 
 sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found
 within this grid.

Example 1:
Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12

Example 2:
Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106
"""

from typing import List

class MatrixSqauare:
    def __init__(self, grid):
        self.grid = grid
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        self.sum_grid = [[0 for i in range(self.col)] for j in range(self.row)]
        self.prepare_sum_grid()
    
    def prepare_sum_grid(self):
        for i in range(self.row):
            diagonal = 0
            left = 0
            up = 0
            for j in range(self.col):
                if i>0 and j>0:
                    up = self.sum_grid[i-1][j]
                    left = self.sum_grid[i][j-1]
                    diagonal = self.sum_grid[i-1][j-1]
                elif i==0 and j>0:
                    left = self.sum_grid[i][j-1]
                elif j==0 and i>0:
                    up = self.sum_grid[i-1][j]
                self.sum_grid[i][j] = self.grid[i][j] + up + left - diagonal
    
    def check_row_sum(self, li, lj, ri, rj, expected_sum):
        # print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        for i in range(li, ri+1):
            up_sum = 0 if i==0 else self.sum_grid[i-1][rj]
            left_sum = 0 if lj==0 else self.sum_grid[i][lj-1]
            diagonal = self.sum_grid[i-1][lj-1] if (i>0 and lj>0) else 0
            if (self.sum_grid[i][rj]-up_sum-left_sum+diagonal) != expected_sum:
                return False
        return True

    def check_col_sum(self, li, lj, ri, rj, expected_sum):
        # print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        for j in range(lj, rj+1):
            up_sum = 0 if li==0 else self.sum_grid[li-1][j]
            left_sum = 0 if j==0 else self.sum_grid[ri][j-1]
            diagonal = self.sum_grid[li-1][j-1] if (li>0 and j>0) else 0
            if (self.sum_grid[ri][j]-up_sum-left_sum+diagonal) != expected_sum:
                return False
        return True

    def check_diagnoal_sum(self, li, lj, ri, rj, expected_sum):
        # print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        d1, d2 = 0, 0
        for i in range(ri-li+1):
            d1+=self.grid[li+i][lj+i]
            d2+=self.grid[li+i][rj-i]
        # print(f'{d1=} {d2=}')
        if d1!=expected_sum or d2!=expected_sum:
            return False
        return True
    
    def has_all_required_num(self, li, lj, ri, rj, expected_nums, expected_sum):
        k = ri-li+1
        d1, d2 = 0, 0
        row_sum = [0 for i in range(k)]
        col_sum = [0 for i in range(k)]
        for i in range(k):
            for j in range(k):
                num = self.grid[li+i][lj+j]
                if num not in expected_nums:
                    return False
                expected_nums.remove(num)
                row_sum[i]+=num
                col_sum[j]+=num
                if (i==j):
                    d1+=num
                if (i+j)==(k-1):
                    d2+=num
        if expected_nums: return False
        if d1!=expected_sum or d2!=expected_sum: return False
        for i in range(k):
            if row_sum[i]!=expected_sum: return False
            if col_sum[i]!=expected_sum: return False
        return True

    def get_expected_sum(self, li, lj, ri, rj):
        up_sum = 0 if li==0 else self.sum_grid[li-1][rj]
        left_sum = 0 if lj==0 else self.sum_grid[li][lj-1]
        diagonal = self.sum_grid[li-1][lj-1] if (li>0 and lj>0) else 0
        return self.sum_grid[li][rj]-up_sum-left_sum+diagonal

    def check_square(self, li, lj, ri, rj):
        expected_sum = self.get_expected_sum(li, lj, ri, rj)
        if not self.check_row_sum(li, lj, ri, rj, expected_sum):
            return False
        if not self.check_col_sum(li, lj, ri, rj, expected_sum):
            return False
        if not self.check_diagnoal_sum(li, lj, ri, rj, expected_sum):
            return False
        # if not self.has_all_required_num(li, lj, ri, rj, expected_set, expected_sum):
        #     return False
        return True

    def has_magic_sqaure_with_k(self, k):
        # print(f'{k=}')
        # expected_sum = ((k**2 + 1)*k)//2
        # expected_set = {i for i in range(1, k**2 + 1)}
        # print(f'{expected_set=}')
        for i in range(k-1, self.row):
            for j in range(k-1, self.col):
                if self.check_square(i-k+1, j-k+1, i, j):
                    return True
        return False
    
    def get_largest_magic_sqaure(self):
        n = min(self.row, self.col)
        for i in range(n, 0, -1):
            if self.has_magic_sqaure_with_k(i):
                return i
        return -1

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        matrix_square = MatrixSqauare(grid)
        return matrix_square.get_largest_magic_sqaure()
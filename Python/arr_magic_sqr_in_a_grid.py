# https://leetcode.com/problems/magic-squares-in-grid
"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and
 both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square: while this one is not:
In total, there is only one magic square inside the given grid.

Example 2:
Input: grid = [[8]]
Output: 0

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
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
        print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        for i in range(li, ri+1):
            up_sum = 0 if i==0 else self.sum_grid[i-1][rj]
            left_sum = 0 if lj==0 else self.sum_grid[i][lj-1]
            diagonal = self.sum_grid[i-1][lj-1] if (i>0 and lj>0) else 0
            if (self.sum_grid[i][rj]-up_sum-left_sum+diagonal) != expected_sum:
                return False
        return True

    def check_col_sum(self, li, lj, ri, rj, expected_sum):
        print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        for j in range(lj, rj+1):
            up_sum = 0 if li==0 else self.sum_grid[li-1][j]
            left_sum = 0 if j==0 else self.sum_grid[ri][j-1]
            diagonal = self.sum_grid[li-1][j-1] if (li>0 and j>0) else 0
            if (self.sum_grid[ri][j]-up_sum-left_sum+diagonal) != expected_sum:
                return False
        return True

    def check_diagnoal_sum(self, li, lj, ri, rj, expected_sum):
        print(f'{li=} {lj=} {ri=} {rj=} {expected_sum=}')
        d1, d2 = 0, 0
        for i in range(ri-li+1):
            d1+=self.grid[li+i][lj+i]
            d2+=self.grid[li+i][rj-i]
        print(f'{d1=} {d2=}')
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

    def check_square(self, li, lj, ri, rj, expected_sum, expected_set):
        # if not self.check_row_sum(li, lj, ri, rj, expected_sum):
        #     return False
        # if not self.check_col_sum(li, lj, ri, rj, expected_sum):
        #     return False
        # if not self.check_diagnoal_sum(li, lj, ri, rj, expected_sum):
        #     return False
        if not self.has_all_required_num(li, lj, ri, rj, expected_set, expected_sum):
            return False
        return True

    def count_magic_square(self, k):
        count = 0
        expected_sum = ((k**2 + 1)*k)//2
        expected_set = {i for i in range(1, k**2 + 1)}
        # print(f'{expected_set=}')
        for i in range(k-1, self.row):
            for j in range(k-1, self.col):
                if self.check_square(i-k+1, j-k+1, i, j, expected_sum, set(expected_set)):
                    count+=1
        return count

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        matrix_sqr = MatrixSqauare(grid)
        # print(f"{matrix_sqr.sum_grid=}")
        return matrix_sqr.count_magic_square(3)
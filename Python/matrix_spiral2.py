# https://leetcode.com/problems/spiral-matrix-ii/
"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2
 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20
"""

class Solution:
    
    def add_spiral(self, matrix, left_top, right_bottom, start):
        si, sj = left_top
        ei, ej = right_bottom
        # Add 1st row
        for j in range(sj, ej+1, 1):
            matrix[si][j] = start
            start+=1
        
        # Add last column
        for i in range(si+1, ei+1, 1):
            matrix[i][ej] = start
            start+=1
        
        # Add last row
        if si!=ei:
            for j in range(ej-1, sj-1, -1):
                matrix[ei][j] = start
                start+=1
        
        # Add 1st col
        if ej!=sj:
            for i in range(ei-1, si, -1):
                matrix[i][sj] = start
                start+=1
        return start
    
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[None for j in range(n)] for i in range(n)]
        start = 1
        si, sj = 0, 0
        ei, ej = n-1, n-1
        while si<=ei and sj<=ej:
            start = self.add_spiral(matrix, (si, sj), (ei, ej), start)
            si+=1
            sj+=1
            ei-=1
            ej-=1
        return matrix
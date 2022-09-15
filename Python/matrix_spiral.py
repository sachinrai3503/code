# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form
# https://leetcode.com/problems/spiral-matrix
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    
    def print_spiral(self, matrix, left, right_bottom, op):
        si, sj = left
        ei, ej = right_bottom
        # Print the 1st row
        for j in range(sj, ej+1):
            op.append(matrix[si][j])
        
        # Print last col
        for i in range(si+1, ei+1):
            op.append(matrix[i][ej])
        
        # Print last row
        if si!=ei:
            for j in range(ej-1, sj-1, -1):
                op.append(matrix[ei][j])
        
        # Print 1st col
        if sj!=ej:
            for i in range(ei-1, si, -1):
                op.append(matrix[i][sj])
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        op = list()
        si, sj = 0, 0
        ei, ej = r-1, c-1
        while si<=ei and sj<=ej:
            self.print_spiral(matrix, (si, sj), (ei, ej), op)
            si+=1
            sj+=1
            ei-=1
            ej-=1
        return op
        
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        r = len(matrix)
        c = 0 if r==0 else len(matrix[0])
        return self.spirallyTraverse(matrix, r, c)
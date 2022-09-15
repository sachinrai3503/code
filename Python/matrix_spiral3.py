# https://leetcode.com/problems/spiral-matrix-iii/
"""
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest
 corner is at the first row and column in the grid, and the southeast corner is at the
 last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you
 move outside the grid's boundary, we continue our walk outside the grid (but may return to
 the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you
 visited them.

Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

Constraints:
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""

class Solution:
    
    def is_valid(self, row, col, i, j):
        if i<0 or i>=row: return False
        if j<0 or j>=col: return False
        return True
    
    def print_spiral(self, row, col, left_bottom, right_top, op, count):
        # print(f'{left_bottom=} {right_top=}')
        si, sj = left_bottom
        ei, ej = right_top
        # Print 1st col
        for i in range(si-1, ei-1, -1):
            if self.is_valid(row, col, i, sj): 
                op.append([i, sj])
                count+=1
        # Print 1st row
        for j in range(sj+1, ej+1, 1):
            if self.is_valid(row, col, ei, j): 
                op.append([ei, j])
                count+=1
        # Print last col
        for i in range(ei+1, si+1, 1):
            if self.is_valid(row, col, i, ej): 
                op.append([i, ej])
                count+=1
        # Print last row
        for j in range(ej-1, sj-1, -1):
            if self.is_valid(row, col, si, j): 
                op.append([si, j])
                count+=1
        return count
    
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        op = list()
        count = 0
        req_count = rows*cols
        si, sj = rStart+1, cStart
        ei, ej = rStart, cStart+1 
        while count<req_count:
            count = self.print_spiral(rows,cols, (si, sj), (ei, ej), op, count)
            # print(op)
            si+=1
            sj-=1
            ei-=1
            ej+=1
        return op
#https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""

class Solution:
    
    def get_sum_matrix(self, matrix):
        row = len(matrix)
        col = 0 if row==0 else len(matrix[0])
        sum_mat = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                left = (0 if j==0 else sum_mat[i][j-1])
                up   = (0 if i==0 else sum_mat[i-1][j])
                diagonal = (0 if (i==0 or j==0) else sum_mat[i-1][j-1])
                # print(left, up, diagonal)
                sum_mat[i][j] = matrix[i][j] + left+up-diagonal
        return sum_mat
    
    def countSquares1(self, matrix: list[list[int]]) -> int:
        count = 0
        row = len(matrix)
        col = 0 if row==0 else len(matrix[0])
        sum_mat = self.get_sum_matrix(matrix)
        # for sum_list in sum_mat:
        #     print(sum_list)
        for k in range(1, min(row, col)+1):
            e_sum = k*k
            i = k-1
            while i<row:
                j = k-1
                while j<col:
                    left = 0 if (j-k)<0 else sum_mat[i][j-k]
                    up   = 0 if (i-k)<0 else sum_mat[i-k][j]
                    diagonal = 0 if (i-k<0 or j-k<0) else sum_mat[i-k][j-k]
                    t_sum = sum_mat[i][j] - left - up + diagonal
                    if t_sum==e_sum: count+=1
                    j+=1
                i+=1
        return count	
		
	# This 1 is tricky but simple.
    def countSquares(self, matrix: list[list[int]]) -> int:
        count = 0
        row = len(matrix)
        col = 0 if row==0 else len(matrix[0])
        op = [0 for i in range(col)]
        for i in range(row):
            prev = 0
            for j in range(col):
                t_prev = op[j]
                top = op[j]
                left = 0 if j==0 else op[j-1]
                diagonal = prev
                op[j] = 0 if matrix[i][j]==0 else (min(min(top,left),diagonal) + 1)
                count+=op[j]
                prev = t_prev
        return count
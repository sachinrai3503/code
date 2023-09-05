# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation
"""
Given two n x n binary matrices mat and target, return true if it is possible to make
 mat equal to target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 
Constraints:
n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
"""

from typing import List

class Rotate:
    def get_next_pos(self, n, i, j):
        return i, j
    
class RotateOnce(Rotate):
    def get_next_pos(self, n, i, j):
        return j, n-1-i

class RotateTwo(Rotate):
    def get_next_pos(self, n, i, j):
        return n-1-i, n-1-j

class RotateThrice(Rotate):
    def get_next_pos(self, n, i, j):
        return n-1-j, i

class Solution:

    def rotate_boundary(self, matrix1, matrix2, i, j, n, k, rotate_by):
        while j<k:
            si, sj = i, j
            ni, nj = rotate_by.get_next_pos(n, si, sj)
            # print(f'out {ni=} {nj=}')
            while (ni, nj)!=(i,j):
                if matrix1[si][sj]!=matrix2[ni][nj]: return False
                si, sj = ni, nj
                ni, nj = rotate_by.get_next_pos(n, si, sj)
                # print(f'in {ni=} {nj=}')
            if matrix1[si][sj]!=matrix2[ni][nj]: return False
            j+=1
        return True

    def rotate(self, matrix1, matrix2, n, rotate_by):
        for i in range(0, (n+1)//2):
            if not self.rotate_boundary(matrix1, matrix2, i, i, n, n-i, rotate_by): return False
        return True

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rotate_bys = [RotateOnce(), RotateTwo(), RotateThrice(), Rotate()]
        n = len(mat)
        for i in range(4):
            if self.rotate(mat, target, n, rotate_bys[i]): return True
            # print(i)
        return False
            
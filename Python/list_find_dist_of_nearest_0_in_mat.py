# https://leetcode.com/problems/01-matrix/
"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
 each cell. The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

from collections import deque
from sys import maxsize

def add_0s_to_queue(que, mat, row, col, visited_mat):
    for i in range(row):
        for j in range(col):
            if mat[i][j]==0:
                que.append((i,j))
                visited_mat[i][j] = True

def is_valid(row, col, visited, i, j):
    if i<0 or i>=row: return False
    if j<0 or j>=col: return False
    return not visited[i][j]

class Solution:
    # BFS based sol. O(n*m) time , O(n*m) space
    def updateMatrix_BFS(self, matrix: list[list[int]]) -> list[list[int]]:
        row, col = len(matrix), len(matrix[0])
        adj_list = [[0,-1,0,1],[-1,0,1,0]]
        que = deque()
        visited_mat = [[False for j in range(col)] for i in range(row)]
        null_pos = (-maxsize, maxsize)
        add_0s_to_queue(que, matrix, row, col, visited_mat)
        que.append(null_pos)
        dist = 1
        while len(que)>0 and que[0]!=null_pos:
            while len(que)>0 and que[0]!=null_pos:
                temp = que.popleft()
                for i in range(4):
                    ti, tj = temp[0] + adj_list[0][i], temp[1] + adj_list[1][i]
                    if is_valid(row, col, visited_mat, ti, tj):
                        matrix[ti][tj] = dist
                        que.append((ti,tj))
                        visited_mat[ti][tj] = True
            que.popleft()
            dist+=1
            que.append(null_pos)
        return matrix
    
    # DP based. 2 pass over mat, time = O(n*m) space = O(1)
    def updateMatrix(self, matrix):
        row, col = len(matrix), len(matrix[0])
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if matrix[i][j]==0: continue
                bottom, right = maxsize, maxsize
                if i!=row-1: bottom = matrix[i+1][j]
                if j!=col-1: right  = matrix[i][j+1]
                dist = min(bottom, right)
                matrix[i][j] = dist if dist==maxsize else dist+1
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0: continue
                up, left = maxsize, maxsize
                if i!=0: up     = matrix[i-1][j]
                if j!=0: left   = matrix[i][j-1]
                dist = min(up, left)
                matrix[i][j] = min(matrix[i][j],dist if dist==maxsize else dist+1)
        return matrix
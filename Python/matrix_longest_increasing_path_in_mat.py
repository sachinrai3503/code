# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""

class GraphInfo:
    def __init__(self, i, j):
        self.i, self.j = i, j
        self.in_deg = 0
        self.out_deg = 0
    
    def __repr__(self):
        return '::'.join([str(self.in_deg), str(self.out_deg)])
        
class Solution:
    
    def __init__(self):
        self.adj = [[0,-1,0,1],[-1,0,1,0]]
    
    def is_safe(self, matrix, row, col, i, j):
        if i<0 or j<0 or i>=row or j>=col: return False
        return True
    
    def dfs(self, matrix, dp, row, col, i, j):
        if dp[i][j]!=-1: return dp[i][j]
        t_len = 0
        for k in range(4):
            ti, tj = i+self.adj[0][k], j+self.adj[1][k]
            if self.is_safe(matrix, row, col, ti, tj) and matrix[i][j]<matrix[ti][tj]:
                t_len = max(t_len, self.dfs(matrix, dp, row, col, ti, tj))
        dp[i][j] = 1 + t_len
        return dp[i][j]
    
    def longestIncreasingPath_dfs_memotization(self, matrix: list[list[int]]) -> int:
        row = len(matrix)
        col = 0 if row==0 else len(matrix[0])
        dp = [[-1 for j in range(col)] for i in range(row)]
        max_len = 0
        for i in range(row):
            for j in range(col):
                max_len = max(max_len, self.dfs(matrix, dp, row, col, i, j))
        return max_len

    # This is based on Graph + topological sort
    def longestIncreasingPath(self, matrix):
        max_len = 0
        row = len(matrix)
        col = 0 if row==0 else len(matrix[0])
        dp = [[GraphInfo(i, j) for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                for k in range(4):
                    ti, tj = i + self.adj[0][k], j + self.adj[1][k]
                    if self.is_safe(matrix, row, col, ti, tj) and matrix[i][j]<matrix[ti][tj]:
                        dp[i][j].out_deg+=1
                        dp[ti][tj].in_deg+=1
        # print(dp)
        from collections import deque
        que = deque()
        null_node = GraphInfo(-1, -1)
        for i in range(row):
            for j in range(col):
                if dp[i][j].in_deg==0:
                    que.append(dp[i][j])
        que.append(null_node)
        while que[0]!=null_node:
            while que[0]!=null_node:
                t_node = que.popleft()
                for k in range(4):
                    ti, tj = t_node.i + self.adj[0][k], t_node.j + self.adj[1][k]
                    if self.is_safe(matrix, row, col, ti, tj) and matrix[t_node.i][t_node.j]<matrix[ti][tj]:
                        adj_node = dp[ti][tj]
                        adj_node.in_deg-=1
                        if adj_node.in_deg==0:
                            que.append(adj_node)
            que.popleft()
            max_len+=1
            que.append(null_node)
        return max_len
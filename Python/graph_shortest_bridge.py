# https://leetcode.com/problems/shortest-bridge/
"""
In a given 2D binary array A, there are two islands.  
(An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:
Input: A = [[0,1],[1,0]]
Output: 1

Example 2:
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
2 <= A.length == A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from collections import deque

class Solution:
    
    def __init__(self):
        self.adj = [[0,-1,0,1],[-1,0,1,0]]
    
    def is_valid(self, i, j):
        if i<0 or i>=self.row: return False
        if j<0 or j>=self.col: return False
        return True
    
    def get_island(self, A, i, j):
        que = deque()
        k = 0
        que.append((i,j))
        A[i][j] = 2
        while k<len(que):
            temp = que[k]
            for index in range(4):
                ti, tj = temp[0] + self.adj[0][index], temp[1] + self.adj[1][index]
                if self.is_valid(ti, tj) and A[ti][tj]==1:
                    que.append((ti, tj))
                    A[ti][tj] = 2
            k+=1
        return que
    
    def get_min_dist(self, A, _1st_island):
        dist = 0
        null_node = (None, None)
        _1st_island.append(null_node)
        while len(_1st_island)>0 and _1st_island[0]!=null_node:
            while len(_1st_island)>0 and _1st_island[0]!=null_node:
                temp = _1st_island.popleft()
                for i in range(4):
                    ti, tj = temp[0] + self.adj[0][i], temp[1] + self.adj[1][i]
                    if self.is_valid(ti, tj):
                        if A[ti][tj]==0:
                            _1st_island.append((ti, tj))
                            A[ti][tj] = 2
                        elif A[ti][tj]==1: return dist
            _1st_island.popleft()
            dist+=1
            _1st_island.append(null_node)
        return dist
    
    def shortestBridge(self, A: list[list[int]]) -> int:
        self.row = len(A)
        self.col = len(A[0])
        for i in range(self.row):
            for j in range(self.col):
                if A[i][j]==1:
                    _1st_island = self.get_island(A, i, j)
                    # print(_1st_island)
                    return self.get_min_dist(A, _1st_island)
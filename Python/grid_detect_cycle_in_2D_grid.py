# https://leetcode.com/problems/detect-cycles-in-2d-grid/
"""
Given a 2D array of characters grid of size m x n, you need to find if there
 exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the
 same cell. From a given cell, you can move to one of the cells adjacent to it
 - in one of the four directions (up, down, left, or right), if it has the
 same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. 
For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2)
 we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false. 

Example 1:
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:
Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:
Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid consists only of lowercase English letters.
"""

# 2nd solution using DJ set is better than the BFS one.

from collections import deque

class Solution:
    
    def __init__(self):
        self.adj = [[0,-1,0,1],
                    [-1,0,1,0]]
    
    def find_cycle(self, grid, row, col, i, j, visited, char):
        
        def is_valid(i,j):
            if i<0 or i>=row: return False
            if j<0 or j>=col: return False
            if grid[i][j]!=char: return False
            return True
        
        que = deque()
        que.append([[i, j],-1])
        visited[i][j] = True
        while len(que)>0:
            temp = que.popleft()
            for i in range(4):
                if i!=temp[1]:
                    ti, tj = temp[0][0] + self.adj[0][i], temp[0][1] + self.adj[1][i]
                    if is_valid(ti, tj):
                        if visited[ti][tj]: return True
                        else:
                            que.append([[ti,tj],(i+2 if (i<2) else i-2)])
                            visited[ti][tj] = True
        return False
    
    def containsCycle(self, grid: list[list[str]]) -> bool:
        row = len(grid)
        col = len(grid[0]) if row>0 else 0
        visited = [[False for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    if self.find_cycle(grid, row, col, i, j, visited, grid[i][j]): return True
        return False

class DJSet:
    def __init__(self, row, col):
        self.parent = [[(i,j) for j in range(col)] for i in range(row)]
        self.rank   = [[1 for j in range(col)] for i in range(row)]
    
    def find_parent(self, cell):
        if self.parent[cell[0]][cell[1]]==cell: return cell
        self.parent[cell[0]][cell[1]] = self.find_parent(self.parent[cell[0]][cell[1]])
        return self.parent[cell[0]][cell[1]]
    
    def union(self, cell1, cell2):
        parent1 = self.find_parent(cell1)
        parent2 = self.find_parent(cell2)
        if parent1==parent2: return True
        if self.rank[parent1[0]][parent1[1]]>self.rank[parent2[0]][parent2[1]]:
            self.parent[parent2[0]][parent2[1]] = parent1
        elif self.rank[parent1[0]][parent1[1]]<self.rank[parent2[0]][parent2[1]]:
            self.parent[parent1[0]][parent1[1]] = parent2
        else:
            self.parent[parent2[0]][parent2[1]] = parent1
            self.rank[parent1[0]][parent1[1]]+=1
        return False
            
class Solution2:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        row = len(grid)
        col = 0 if row==0 else len(grid[0])
        djset = DJSet(row, col)
        for i in range(row):
            for j in range(col):
                char = grid[i][j]
                if i>0 and grid[i-1][j]==char:
                    if djset.union((i-1, j), (i, j)): return True
                if j<col-1 and grid[i][j+1]==char:
                    if djset.union((i, j), (i, j+1)): return True
        return False
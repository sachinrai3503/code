# https://www.geeksforgeeks.org/find-the-number-of-islands-set-2-using-disjoint-set/
# https://leetcode.com/problems/number-of-islands/
"""
Given a boolean 2D matrix, find the number of islands.

A group of connected 1s forms an island. 
For example, the below matrix contains 5 islands

{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1} 
A cell in the 2D matrix can be connected to 8 neighbours.

This is a variation of the standard problem: 
“Counting the number of connected components in an undirected graph”
"""

class DisjointSet_Graph:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.parent = [[[i, j] for j in range(col)] for i in range(row)]
        self.rank = [[0 for j in range(col)] for i in range(row)]

    def find(self, i, j):
        if self.parent[i][j][0] == i and self.parent[i][j][1] == j:
            return self.parent[i][j]
        else:
            self.parent[i][j] = self.find(
                self.parent[i][j][0], self.parent[i][j][1])
            return self.parent[i][j]

    def union(self, i1, j1, i2, j2):
        repr1 = self.find(i1, j1)
        repr2 = self.find(i2, j2)
        if repr1[0] == repr2[0] and repr1[1] == repr2[1]:
            return
        if self.rank[repr1[0]][repr1[1]] == self.rank[repr2[0]][repr2[1]]:
            self.parent[repr1[0]][repr1[1]] = [repr2[0], repr2[1]]
            self.rank[repr2[0]][repr2[1]] += 1
        elif self.rank[repr1[0]][repr1[1]] < self.rank[repr2[0]][repr2[1]]:
            self.parent[repr1[0]][repr1[1]] = [repr2[0], repr2[1]]
        else:
            self.parent[repr2[0]][repr2[1]] = [repr1[0], repr1[1]]

def is_valid(matrix, row, col, i, j):
    if i<0 or j<0 or i>=row or j>=col or matrix[i][j]=='0':
        return False
    return True

def count_connected_component(mat):
    count = 0
    row = len(mat)
    col = len(mat[0])
    adj_cell = [[-1, 0, 1, 0],
                [0, 1, 0, -1]]
    dj_set = DisjointSet_Graph(row, col)
    for i in range(row):
        for j in range(col):
            if mat[i][j] == '1':
                for k in range(len(adj_cell[0])):
                    ti, tj = i+adj_cell[0][k], j+adj_cell[1][k]
                    if is_valid(mat, row, col, ti, tj):
                        # print(ti,tj,'++')
                        dj_set.union(i, j, ti, tj)
    for i in range(row):
        for j in range(col):
            if mat[i][j] == '1' and dj_set.parent[i][j]==[i,j]:
                count+=1
    return count

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        return count_connected_component(grid)
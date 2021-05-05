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
        if parent1==parent2: return
        if self.rank[parent1[0]][parent1[1]]>self.rank[parent2[0]][parent2[1]]:
            self.parent[parent2[0]][parent2[1]] = parent1
        elif self.rank[parent1[0]][parent1[1]]<self.rank[parent2[0]][parent2[1]]:
            self.parent[parent1[0]][parent1[1]] = parent2
        else:
            self.parent[parent2[0]][parent2[1]] = parent1
            self.rank[parent1[0]][parent1[1]]+=1
            
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        row = len(grid)
        col = 0 if row==0 else len(grid[0])
        djset = DJSet(row, col)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    if i>0 and grid[i-1][j]=='1':
                        djset.union((i-1,j), (i,j))
                    if j<col-1 and grid[i][j+1]=='1':
                        djset.union((i,j+1), (i,j))
        # print(djset.rank)
        # print(djset.parent)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and djset.parent[i][j]==(i, j):
                    count+=1
        return count
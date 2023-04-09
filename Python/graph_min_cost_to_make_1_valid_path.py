# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid
"""
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should 
 visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some signs on the cells of the grid that point outside the grid.
You will initially start at the upper left cell (0, 0). A valid path in the grid is a path
 that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1)
 following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow
 to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down
 with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with
 cost = 1 --> (3, 3)
The total cost = 3.

Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
"""

from sys import maxsize
from typing import List

class HeapNode:
    def __init__(self, cell, cost = 0, index = -1):
        self.cell = cell
        self.cost = cost
        self.index = index
    
    def __repr__(self):
        return f'{self.cell}:{self.index}'

class Heap:
    def __init__(self, size):
        self.data = [None for i in range(size)]
        self.cur_size = 0
        self.maxsize = size
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i].index, self.data[j].index = self.data[j].index, self.data[i].index
    
    def is_full(self):
        return self.cur_size==self.maxsize
    
    def is_empty(self):
        return self.cur_size==0

    def compare(self, i, j):
        pass
    
    def heapify(self, index):
        pass
    
    def insert_in_heap(self, data:HeapNode):
        if self.is_full():
            print('Full')
        else:
            index = self.cur_size
            data.index = index
            self.cur_size+=1
            self.data[index] = data
            parent_index = (index-1)//2
            while index>0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2
    
    def delete_top(self):
        if self.is_empty():
            print('Empty')
            return None
        else:
            temp = self.data[0]
            self.cur_size-=1
            self.swap(0, self.cur_size)
            self.heapify(0)
            return temp

    def update_node(self, node):
        if not node:
            print(f'Invalid node {node}')
        else:
            parent_index = (node.index-1)//2
            index = node.index
            while index>0 and self.compare(index, parent_index)==-1:
                self.swap(index, parent_index)
                index = parent_index
                parent_index = (index-1)//2

class MinHeap(Heap):
    def __init__(self, size):
        Heap.__init__(self, size)
    
    def compare(self, i, j):
        if self.data[i].cost<self.data[j].cost: return -1
        if self.data[j].cost>self.data[j].cost: return 1
        return 0
    
    def heapify(self, index):
        left = index*2+1
        right = index*2+2
        min_index = index
        if left<self.cur_size and self.compare(left, min_index)==-1:
            min_index = left
        if right<self.cur_size and self.compare(right, min_index)==-1:
            min_index = right
        if index!=min_index:
            self.swap(index, min_index)
            self.heapify(min_index)

class Graph:
    def __init__(self, grid_info:List):
        self.data = dict()
        self.add_edges(grid_info)
    
    def add_edges(self, grid_info:List):
        row, col, grid = grid_info
        def is_valid(i, j):
            if i<0 or i>=row or j<0 or j>=col: return False
            return True
        directions = [(2, 0, -1), (4, -1, 0), (1, 0, 1), (3, 1, 0)] # (direction_num,i,j)
        for i in range(row):
            for j in range(col):
                u = (i, j)
                adj_vertexs = list()
                for dk, di, dj in directions:
                    ti, tj = i + di, j + dj
                    if is_valid(ti, tj):
                        cost = 0 if grid[i][j]==dk else 1
                        adj_vertexs.append([(ti, tj), cost])
                self.data[u] = adj_vertexs

    def get_adj_ver(self, u):
        return self.data.get(u, None)

class Solution:

    def is_valid(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        return True
    
    def get_min_cost(self, src, visited):
        # print(f'{src=} {visited=}')
        if src in visited: return maxsize
        if src==self.dest:
            return 0
        visited.add(src)
        cost = maxsize
        si, sj = src
        for dk, di, dj in self.directions:
            ti, tj = si + di, sj + dj
            if self.is_valid(ti, tj):
                cost = min(cost, self.get_min_cost((ti, tj), visited) + (not self.grid[si][sj]==dk))
        # print(f'{src=} {visited=} {cost=}')
        visited.remove(src)
        return cost

    # This will time out - O(4^(m*n))
    def minCost_dfs(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(grid[0])
        self.grid = grid
        self.dest = (self.row-1, self.col-1)
        self.directions = [(2, 0, -1), (4, -1, 0), (1, 0, 1), (3, 1, 0)]
        visited = set()
        return self.get_min_cost((0,0), visited)
    
    # Dijkstra
    def minCost(self, grid: List[List[int]]) -> int:
        min_cost = maxsize
        row = len(grid)
        col = 0 if row==0 else len(grid[0])
        grid_info = [row, col, grid]
        dest = (row-1, col-1)
        graph = Graph(grid_info)
        # print(f'{graph.data=}')
        heap = MinHeap(row*col)
        heap_node_map = dict() # (i,j) -> HeapNode
        visited = set() # (i, j)
        src_heap_node = HeapNode((0,0), 0)
        heap.insert_in_heap(src_heap_node)
        heap_node_map[(0,0)] = src_heap_node
        while not heap.is_empty():
            temp = heap.delete_top()
            visited.add(temp.cell)
            if temp.cell == dest:
                return temp.cost
            adj_cells = graph.get_adj_ver(temp.cell)
            for adj_cell, adj_edge_weight in adj_cells:
                if adj_cell in visited: continue
                adj_cell_heap_node = heap_node_map.get(adj_cell, None)
                if adj_cell_heap_node is not None:
                    if (temp.cost + adj_edge_weight)<adj_cell_heap_node.cost:
                        adj_cell_heap_node.cost = temp.cost + adj_edge_weight
                        heap.update_node(adj_cell_heap_node)
                else:
                    adj_cell_heap_node = HeapNode(adj_cell, temp.cost + adj_edge_weight)
                    heap.insert_in_heap(adj_cell_heap_node)
                    heap_node_map[adj_cell] = adj_cell_heap_node
        return maxsize
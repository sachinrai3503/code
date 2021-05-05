# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
"""
Storekeeper is a game in which the player pushes boxes around in a warehouse trying 
 to get them to target locations.

The game is represented by a grid of size m x n, where each element is a wall, floor, or a box.

Your task is move the box 'B' to the target position 'T' under the following rules:
- Player is represented by character 'S' and can move up, down, left, right in
  the grid if it is a floor (empy cell).
- Floor is represented by character '.' that means free cell to walk.
- Wall is represented by character '#' that means obstacle  (impossible to walk there). 
- There is only one box 'B' and one target cell 'T' in the grid.
  The box can be moved to an adjacent free cell by standing next to the box and 
  then moving in the direction of the box. This is a push.

The player cannot walk through the box.

Return the minimum number of pushes to move the box to the target. 
If there is no way to reach the target, return -1.

Example 1:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

Example 2:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation:  push the box down, left, left, up and up.

Example 4:
Input: grid = [["#","#","#","#","#","#","#"],
               ["#","S","#",".","B","T","#"],
               ["#","#","#","#","#","#","#"]]
Output: -1
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 20
1 <= n <= 20
grid contains only characters '.', '#',  'S' , 'T', or 'B'.
There is only one character 'S', 'B' and 'T' in the grid.
"""
from collections import deque

class Grid:

    def __init__(self, grid):
        self.grid = grid
        self.row = len(grid)
        self.col = 0 if self.row==0 else len(self.grid[0])
        self.visited = set()
        self.adj_cell = [[0,-1,0,1],[-1,0,1,0]]
        self.box_pos, self.target_pos, self.player_pos = self.get_positions()
    
    def get_positions(self):
        box_pos = None
        target_pos = None
        player_pos = None
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j]=='#': continue
                elif self.grid[i][j]=='S': player_pos = (i,j)
                elif self.grid[i][j]=='T': target_pos = (i,j)
                elif self.grid[i][j]=='B': box_pos = (i,j)
        return box_pos, target_pos, player_pos
    
    def is_valid(self, i, j):
        if i<0 or i>=self.row: return False
        if j<0 or j>=self.col: return False
        if self.grid[i][j]=='#': return False
        return True

    def dfs(self, i, j, ei, ej, pi, pj, visited, op):
        if not self.is_valid(i, j): return
        if visited[i][j]: return
        if ei==i and ej==j:
            op.append((pi,pj))
            return
        visited[i][j] = True
        for k in range(4):
            ti, tj = i+self.adj_cell[0][k], j+self.adj_cell[1][k]
            self.dfs(ti,tj,ei,ej,i,j,visited,op)
        # visited[i][j] = False
    
    def get_init_visited(self):
        visited = [[False for j in range(self.col)] for i in range(self.row)]
        return visited
    
    def make_move(self, cur_pos):
        ti, tj = -1,-1
        if cur_pos[0][0]==cur_pos[1][0]:
            ti = cur_pos[0][0]
            if cur_pos[0][1]<cur_pos[1][1]: tj = cur_pos[1][1]+1
            else: tj = cur_pos[1][1]-1
        elif cur_pos[0][1]==cur_pos[1][1]:
            tj = cur_pos[0][1]
            if cur_pos[0][0]<cur_pos[1][0]: ti = cur_pos[1][0]+1
            else: ti = cur_pos[1][0]-1
        else:
            print('fatal')
        if self.is_valid(ti,tj):
            return (cur_pos[1], (ti,tj))
        return None
                
    def bfs(self):
        min_path = 0
        que = deque()
        possible_positions = list()
        self.dfs(self.player_pos[0],self.player_pos[1],
                 self.box_pos[0],self.box_pos[1],
                -1,-1,self.get_init_visited(), possible_positions)
        # print('posi_pos =',possible_positions)
        for position in possible_positions:
            data = (position,self.box_pos)
            que.append(data)
            self.visited.add(data)
        null_data = ((-1,-1),(-1,-1))
        que.append(null_data)
        while len(que)>0 and que[0]!=null_data:
            while len(que)>0 and que[0]!=null_data:
                # print(que)
                t_data = que.popleft()
                # print(t_data)
                if t_data[1][0]==self.target_pos[0] and t_data[1][1]==self.target_pos[1]:
                    return min_path
                possible_positions.clear()
                self.dfs(t_data[0][0],t_data[0][1],
                         t_data[1][0],t_data[1][1],
                         -1, -1, self.get_init_visited(), possible_positions)
                # possible_positions.append(t_data[0])
                for position in possible_positions:
                    t_pos = (position, t_data[1])
                    if t_pos not in self.visited:
                        t_next_move = self.make_move(t_pos)
                        if t_next_move!=None and t_next_move not in self.visited:
                            que.append(t_next_move)
                            self.visited.add(t_next_move)
                next_move_pos = self.make_move(t_data)
                # print('next_move =', next_move_pos)
                if next_move_pos is not None and next_move_pos not in self.visited:
                    que.append(next_move_pos)
                    self.visited.add(next_move_pos)
            # print(que)
            # print('================================')
            que.popleft()
            min_path+=1
            que.append(null_data)
        return -1
    
class Solution:
    def minPushBox(self, grid: list[list[str]]) -> int:
        grid = Grid(grid)
        return grid.bfs()
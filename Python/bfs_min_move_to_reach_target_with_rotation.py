# https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
"""
In an n*n grid, there is a snake that spans 2 cells and starts moving from the
 top left corner at (0, 0) and (0, 1). The grid has empty cells represented by
 zeros and blocked cells represented by ones. The snake wants to reach the lower
 right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:
- Move one cell to the right if there are no blocked cells there. 
  This move keeps the horizontal/vertical position of the snake as it is.
- Move down one cell if there are no blocked cells there. 
  This move keeps the horizontal/vertical position of the snake as it is.
- Rotate clockwise if it's in a horizontal position and the two cells under 
  it are both empty. In that case the snake moves 
  from (r, c) and (r, c+1) to (r, c) and (r+1, c).
- Rotate counterclockwise if it's in a vertical position and the two cells to 
  its right are both empty. In that case the snake moves
  from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

Example 1:
Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down,
                          down, rotate counterclockwise, right, down].

Example 2:
Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9

Constraints:
2 <= n <= 100
0 <= grid[i][j] <= 1
It is guaranteed that the snake starts at empty cells.
"""
from collections import deque

class Grid:
    
    class Pos:
        def __init__(self, i, j):
            self.x = i
            self.y = j
        
        def __repr__(self):
            return str(self.x)+'-'+str(self.y)+"::"
        
    def is_horizontal(self, pos1, pos2):
        if pos1.x==pos2.x: return True
        return False
    
    def __init__(self, grid):
        self.grid = grid
        self.row  = len(grid)
        self.col  = 0 if self.row==0 else len(grid[0])
        self.visited = set()
    
    def is_valid_pos(self, pos):
        if pos.x<0 or pos.x>=self.row: return False
        if pos.y<0 or pos.y>=self.col: return False
        if self.grid[pos.x][pos.y] == 1: return False
        return True
    
    def is_visited(self, pos):
        if ((pos[0].x, pos[0].y), (pos[1].x, pos[1].y)) in self.visited: return True
        return False

    def move_down(self, pos1, pos2):
        if self.is_horizontal(pos1, pos2):
            t_pos1 = self.Pos(pos1.x+1, pos1.y)
            t_pos2 = self.Pos(pos2.x+1, pos2.y)
        else:
            t_pos1 = pos2
            t_pos2 = self.Pos(pos2.x+1, pos2.y)
        if self.is_valid_pos(t_pos1) and self.is_valid_pos(t_pos2) and \
            not self.is_visited((t_pos1, t_pos2)):
            return (t_pos1, t_pos2)
        return None
    
    def move_right(self, pos1, pos2):
        if self.is_horizontal(pos1, pos2):
            t_pos1 = pos2
            t_pos2 = self.Pos(pos2.x, pos2.y+1)
        else:            
            t_pos1 = self.Pos(pos1.x, pos1.y+1)
            t_pos2 = self.Pos(pos2.x, pos2.y+1)
        if self.is_valid_pos(t_pos1) and self.is_valid_pos(t_pos2) and \
            not self.is_visited((t_pos1, t_pos2)):
            return (t_pos1, t_pos2)
        return None
    
    def move_clockwise(self, pos1, pos2):
        if not self.is_horizontal(pos1, pos2): return None
        t_pos1 = self.Pos(pos1.x+1, pos1.y)
        t_pos2 = self.Pos(pos2.x+1, pos2.y)
        if self.is_valid_pos(t_pos1) and self.is_valid_pos(t_pos2):
            f_pos1 = pos1
            f_pos2 = self.Pos(pos1.x+1, pos1.y)
            if not self.is_visited((f_pos1, f_pos2)):
                return (f_pos1, f_pos2)
        return None
    
    def move_anticlockwise(self, pos1, pos2):
        if self.is_horizontal(pos1, pos2): return None
        t_pos1 = self.Pos(pos1.x, pos1.y+1)
        t_pos2 = self.Pos(pos2.x, pos2.y+1)
        if self.is_valid_pos(t_pos1) and self.is_valid_pos(t_pos2):
            f_pos1 = pos1
            f_pos2 = self.Pos(pos1.x, pos1.y+1)
            if not self.is_visited((f_pos1, f_pos2)):
                return (f_pos1, f_pos2)
        return None
            
class Solution:
    
    def add_pos_to_que(self, pos, que, grid_obj):
        if pos is None: return
        que.append(pos)
        grid_obj.visited.add(((pos[0].x, pos[0].y),(pos[1].x, pos[1].y)))
    
    def minimumMoves(self, grid: list[list[int]]) -> int:
        step = 0
        row = len(grid)
        col = 0 if row==0 else len(grid[0])
        grid_obj  = Grid(grid)
        que = deque()
        t_node = (grid_obj.Pos(0,0), grid_obj.Pos(0,1))
        self.add_pos_to_que(t_node, que, grid_obj)
        null_pos = grid_obj.Pos(grid_obj.row, grid_obj.col)
        null_node = (null_pos, null_pos)
        que.append(null_node)
        while len(que)>0 and que[0]!=null_node:
            while len(que)>0 and que[0]!=null_node:
                # print(que)
                # print(grid_obj.visited)
                # print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                t_pos = que.popleft()
                if t_pos[0].x==row-1 and t_pos[0].y==col-2 and t_pos[1].x==row-1\
                    and t_pos[1].y==col-1: return step
                right_pos = grid_obj.move_right(t_pos[0],t_pos[1])
                down_pos = grid_obj.move_down(t_pos[0],t_pos[1])
                clk_pos = grid_obj.move_clockwise(t_pos[0], t_pos[1])
                aclk_pos = grid_obj.move_anticlockwise(t_pos[0], t_pos[1])
                self.add_pos_to_que(right_pos, que, grid_obj)
                self.add_pos_to_que(down_pos, que, grid_obj)
                self.add_pos_to_que(clk_pos, que, grid_obj)
                self.add_pos_to_que(aclk_pos, que, grid_obj)
                # print(t_pos, grid_obj.visited)
            que.popleft()
            step+=1
            que.append(null_node)
        return -1

def main():
    grid = [[0,0,0,0,1,1],
            [1,1,0,0,1,0],
            [0,0,1,1,1,1],
            [0,0,1,0,1,0],
            [0,1,1,0,0,0],
            [0,1,1,0,0,0]]
    sol = Solution()
    print('min move',sol.minimumMoves(grid))

if __name__ == '__main__':
    main()
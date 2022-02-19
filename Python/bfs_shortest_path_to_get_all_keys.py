# https://leetcode.com/problems/shortest-path-to-get-all-keys/
"""
You are given an m x n grid grid where:
'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.

You start at the starting point and one move consists of walking one space
 in one of the four cardinal directions. You cannot walk outside the grid, 
 or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock
 unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter
 of the first k letters of the English alphabet in the grid. This means that
 there is exactly one key for each lock, and one lock for each key; and also
 that the letters used to represent the keys and locks were chosen in the same
 order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible,
 return -1.

Example 1:
Input: grid = ["@.a.#","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:
Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:
Input: grid = ["@Aa"]
Output: -1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
"""

from collections import deque

class Solution:

    def is_key(self, i, j):
        if 'a'<=self.grid[i][j]<='f':return True
        return False
    
    def get_grid_info(self):
        si, sj = -1, -1
        key_count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j]=='@': si, sj = i, j
                elif self.is_key(i,j): key_count+=1
        return si, sj, key_count
    
    def is_valid(self, i, j, path_flags):
        if i<0 or i>=self.row or j<0 or j>=self.col: return False
        content = self.grid[i][j]
        if content=='#': return False
        if 'A'<=content<='F': # check if key is present in path
            if path_flags&(1<<(ord(content)-65)) == 0: return False # No key
            if path_flags in self.cell_path[i][j]: return False
            return True
        # Now either empty or key cell
        if path_flags in self.cell_path[i][j]: return False
        return True
    
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        steps = 0
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0]) if self.row!=0 else 0
        self.cell_path = [[set() for j in range(self.col)] for i in range(self.row)]
        adj = [[0,-1,0,1],[-1,0,1,0]]
        que = deque()
        si, sj, exp_key_count = self.get_grid_info()
        req_flag = (1<<exp_key_count) - 1
        # print(si, sj, exp_key_count, req_flag)
        que.append([si, sj, 0]) # [i, j, path_flags]
        self.cell_path[si][sj].add(0)
        que.append(None)
        while que[0]!=None:
            # print(que)
            # print(self.cell_path)
            while que[0]!=None:
                temp = que.popleft()
                ci, cj, c_path_flags = temp
                if c_path_flags==req_flag: return steps
                for i in range(4):
                    ti, tj = ci+adj[0][i], cj+adj[1][i]
                    if self.is_valid(ti, tj, c_path_flags):
                        t_node = [ti, tj, c_path_flags]
                        if self.is_key(ti, tj): 
                            t_node[2] = t_node[2]|(1<<(ord(self.grid[ti][tj])-97))
                        que.append(t_node)
                        self.cell_path[ti][tj].add(t_node[2])
            que.popleft()
            steps+=1
            que.append(None)
            # print(que)
            # print(self.cell_path)
            # print('--------------------------------')
        return -1
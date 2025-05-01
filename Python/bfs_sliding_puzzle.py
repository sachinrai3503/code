# https://leetcode.com/problems/sliding-puzzle
"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. 
 A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the
 board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Constraints:
board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
"""

from collections import deque
from typing import List

class Solution:

    def get_row_col(self, index):
        row, col = index//3, index%3
        return (row, col)
    
    def get_index(self, row, col):
        return row*3 + col

    def is_valid(self, i, j):
        return i>=0 and i<2 and j>=0 and j<3

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        count = 0
        target = '123450'
        adj_dir = [(0,-1),(-1,0),(0,1),(1,0)]
        board_string = ''.join([''.join([str(c) for c in board[i]]) for i in range(2)])
        # print(f'{board_string=}')
        que = deque()
        visited = set()
        que.append(board_string)
        visited.add(board_string)
        que.append(None)
        while que[0] is not None:
            while que[0] is not None:
                cur_board = que.popleft()
                if cur_board==target: return count
                cur_board_list = list(cur_board)
                index_0 = cur_board.find('0')
                i, j = self.get_row_col(index_0)
                for dir in adj_dir:
                    t_i, t_j = i+dir[0], j+dir[1]
                    if self.is_valid(t_i, t_j):
                        t_index = self.get_index(t_i, t_j)
                        cur_board_list[index_0], cur_board_list[t_index] = cur_board_list[t_index], cur_board_list[index_0]
                        t_board = ''.join(cur_board_list)
                        if t_board not in visited:
                            que.append(t_board)
                            visited.add(t_board)
                        cur_board_list[index_0], cur_board_list[t_index] = cur_board_list[t_index], cur_board_list[index_0]
            que.popleft()
            count+=1
            que.append(None)
        return -1
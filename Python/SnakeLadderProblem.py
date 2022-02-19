#  https://www.geeksforgeeks.org/snake-ladder-problem-2/
#  https://leetcode.com/problems/snakes-and-ladders/
"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2
 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0])
 and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are
 always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or
 ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1.
 The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the
 destination to a snake or ladder is the start of another snake or ladder,
 you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your
 destination square is 2. You follow the ladder to square 3, but do not follow
 the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not
 possible to reach the square, return -1.

Example 1:
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
                [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:
n == board.length == board[i].length
2 <= n <= 20
grid[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.
"""

from collections import deque

class Solution:
    
    def print_board(self, board):
        for row in board:
            print(row)
    
    def get_row_col(self, n, position):
        row = (n-1) - ((position-1)//n)
        if n%2==0: col = (position-1)%n if row%2==1 else ((n-1)-((position-1)%n))
        else: col = (position-1)%n if row%2==0 else ((n-1)-((position-1)%n))
        return row, col
    
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        # self.print_board(board)
        moves = 0
        n = len(board)
        dest = n**2
        que = deque()
        visited = set()
        que.append(1)
        visited.add(1)
        que.append(None)
        while que[0]!=None:
            # print(que)
            # print(visited)
            while que[0]!=None:
                t_pos = que.popleft()
                if t_pos == dest:
                    return moves
                else:
                    for i in range(1, 7):
                        next_pos = t_pos + i
                        if next_pos > dest: break
                        next_row_index, next_col_index = self.get_row_col(n, next_pos)
                        jump_to = board[next_row_index][next_col_index]
                        # Since not jumping so need to check if we already visited next_pos
                        if jump_to==-1 and next_pos not in visited: 
                            que.append(next_pos)
                            visited.add(next_pos)    
                        elif jump_to!=-1 and jump_to not in visited: 
                            que.append(jump_to)
                            visited.add(jump_to)
            que.popleft()
            moves+=1
            que.append(None)
        # print(que)
        # print(visited)
        return -1
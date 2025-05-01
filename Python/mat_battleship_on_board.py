# https://leetcode.com/problems/battleships-in-a-board
"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number
 of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made
 of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one
 horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""

from typing import List

class Solution:

    # This modifies the board
    def countBattleships1(self, board: List[List[str]]) -> int:
        m = len(board)
        n = 0 if m==0 else len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.': continue
                up = board[i-1][j] if i>0 else None
                left = board[i][j-1] if j>0 else None
                up = up if up!='.' else None
                left = left if left!='.' else None
                if up is not None:
                    board[i][j] = up
                elif left is not None:
                    board[i][j] = left
                else:
                    count+=1
                    board[i][j] = count
        return count

    # Without modiying the board
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = 0 if m==0 else len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.': continue
                up = board[i-1][j] if i>0 else None
                left = board[i][j-1] if j>0 else None
                if up == 'X' or left == 'X':
                    continue
                else:
                    count+=1
                # print(f'{i=} {j=} {up=} {left=} {count=}')
        return count

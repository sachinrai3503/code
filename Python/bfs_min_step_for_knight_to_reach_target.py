# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight
"""
Given a square chessboard of N x N size, the position of Knight and position
 of a target is given. We need to find out the minimum steps a Knight will take
  to reach the target position.

Examples:
In above diagram Knight takes 3 step to reach 
from (4, 5) to (1, 1) (4, 5) -> (5, 3) -> (3, 2) 
-> (1, 1)  as shown in diagram
"""

from collections import deque
from sys import is_finalizing, maxsize


class Pos:
    def __init__(self, i, j):
        self.i = i
        self.j = j


def is_valid_pos(row, col, pos):
    if pos.i < 0 or pos.i >= row:
        return False
    if pos.j < 0 or pos.j >= col:
        return False
    return True


def get_min_steps(row, col, pos_s, pos_d, visited):
    if not is_valid_pos(row, col, pos_s):
        return None
    if not is_valid_pos(row, col, pos_d):
        return None
    if visited[pos_s.i][pos_s.j]:
        return None
    step = 0
    adj_step = [[-1, 1, -2, -2, -1, 1, 2, 2],
                [-2, -2, -1, 1, 2, 2, -1, 1]]
    que = deque()
    null_pos = Pos(maxsize, maxsize)
    que.append(pos_s)
    visited[pos_s.i][pos_s.j] = True
    que.append(null_pos)
    while len(que) > 0 and que[0] != null_pos:
        while len(que) > 0 and que[0] != null_pos:
            t_pos = que.popleft()
            if(t_pos.i == pos_d.i and t_pos.j == pos_d.j):
                return step
            for i in range(8):
                n_pos = Pos(t_pos.i + adj_step[0][i], t_pos.j + adj_step[1][i])
                if is_valid_pos(row, col, n_pos) and \
                   not visited[n_pos.i][n_pos.j]:
                    que.append(n_pos)
                    visited[n_pos.i][n_pos.j] = True
        que.append(null_pos)
        step += 1
        que.popleft()
    return step


def main():
    row, col = 30, 30
    pos_s = Pos(0, 0)
    pos_d = Pos(24, 24)
    visited = [[False for j in range(col)] for i in range(row)]
    steps = get_min_steps(row, col, pos_s, pos_d, visited)
    print('Min steps =', steps)


if __name__ == '__main__':
    main()

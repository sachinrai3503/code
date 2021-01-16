# https://leetcode.com/problems/knight-probability-in-chessboard
"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and
 attempts to make exactly K moves. The rows and columns are 0 indexed, so the
 top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. 
 Each move is two squares in a cardinal direction, then one square in an
 orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves
 uniformly at random (even if the piece would go off the chessboard) and moves
 there.

The knight continues moving until it has made exactly K moves or has moved off
 the chessboard. Return the probability that the knight remains on the board
 after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on 
             the board.
From each of those positions, there are also two moves that will keep the knight
 on the board.The total probability the knight stays on the board is 0.0625.
 

Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""

def is_valid(N, i, j):
    if i<0 or i>=N: return False
    if j<0 or j>=N: return False
    return True

class Solution:
    
    def __init__(self):
        self.adj_step = [[-1, 1, -2, -2, -1, 1, 2, 2],
                         [-2, -2, -1, 1, 2, 2, -1, 1]]
    
    def knightProbability_REC(self, N: int, K: int, r: int, c: int) -> float:
        if not is_valid(N, r, c): return 0
        if K==0: return 1
        cur_prob = 0
        prob_with_k_min_1 = 0
        for i in range(8):
            prob_with_k_min_1+=self.knightProbability_REC(N,K-1,
                                   r+self.adj_step[0][i],c+self.adj_step[1][i])
        cur_prob = prob_with_k_min_1/8
        return cur_prob
    
    def get_adj_steps_as_dict(self, N):
        adj_step_dict = dict()
        for i in range(N):
            for j in range(N):
                for k in range(8):
                    ti, tj = i + self.adj_step[0][k], j + self.adj_step[1][k]
                    if is_valid(N, ti, tj):
                        if not adj_step_dict.__contains__((i,j)):
                            adj_step_dict[(i,j)] = list()
                        adj_step_dict[(i,j)].append((ti, tj))
        return adj_step_dict
                        
    
    def knightProbability(self, N, K, r, c):
        if not is_valid(N, r, c): return 0
        next_step_dict = self.get_adj_steps_as_dict(N)
        prob_mat = [[[1 for j in range(N)] for i in range(N)] for p in range(2)]
        for t_k in range(1,K+1,1):
            cur_mat = t_k%2
            prev_mat = 0 if cur_mat==1 else 1
            for i in range(N):
                for j in range(N):
                    t_prob = 0
                    valid_adj_list = next_step_dict.get((i,j), None)
                    if valid_adj_list is not None:
                        for valid_adj in valid_adj_list:
                            t_prob+=prob_mat[prev_mat][valid_adj[0]][valid_adj[1]]
                    prob_mat[cur_mat][i][j] = t_prob/8
        return prob_mat[K%2][r][c]
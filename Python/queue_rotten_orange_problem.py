# https://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
"""
Given a matrix of dimension m*n where each cell in the matrix 
can have values 0, 1 or 2 which has the following meaning:
0: Empty cell
1: Cells have fresh oranges
2: Cells have rotten oranges 

Determine what is the minimum time required so that
 all the oranges become rotten. 
A rotten orange at index [i,j] can rot other 
    fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] 
    (up, down, left and right). 

If it is impossible to rot every orange then simply return -1.

Examples:
Input:  arr[][C] = { {2, 1, 0, 2, 1},
                     {1, 0, 1, 2, 1},
                     {1, 0, 0, 2, 1}};
Output:
All oranges can become rotten in 2-time frames.
"""

# For c based sol. refer queue_rotten_orange_problem.c

from collections import deque
import sys

ADJACENT_CELL = [[0,0,-1,1],
                 [-1,1,0,0]]

class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def is_valid_pos(mat_2d, row_count, col_count, pos):
    if pos.x<0 or pos.y<0:
        return False
    if pos.x>=row_count or pos.y>=col_count:
        return False
    if mat_2d[pos.x][pos.y]==0:
        return False
    return True

def is_fresh(mat_2d, row_count, col_count, pos):
    if not is_valid_pos(mat_2d,row_count,col_count,pos):
        return False
    if mat_2d[pos.x][pos.y]==1:
        return True
    return False

def is_rotten(mat_2d, row_count, col_count, pos):
    if not is_valid_pos(mat_2d,row_count,col_count,pos):
        return False
    if mat_2d[pos.x][pos.y]==2:
        return True
    return False

def mark_rotten(mat_2d, row_count, col_count, pos):
    if not is_valid_pos(mat_2d,row_count,col_count,pos):
        return
    mat_2d[pos.x][pos.y] = 2

def get_min_time_to_rot(mat_2d):
    min_time = 0
    row_count, col_count = len(mat_2d), len(mat_2d[0])
    que = deque()
    null_pos = Pos(sys.maxsize*-1,sys.maxsize)
    for i in range(row_count):
        for j in range(col_count):
            pos = Pos(i,j)
            if is_rotten(mat_2d,row_count,col_count,pos):
                que.append(pos)
    que.append(null_pos)
    while len(que) and que[0]!=null_pos:
        while len(que) and que[0]!=null_pos:
            t_pos = que.popleft()
            for i in range(len(ADJACENT_CELL[0])):
                tx = t_pos.x+ADJACENT_CELL[0][i]
                ty = t_pos.y+ADJACENT_CELL[1][i]
                new_pos = Pos(tx,ty)
                if is_valid_pos(mat_2d,row_count,col_count,new_pos) and \
                    is_fresh(mat_2d,row_count,col_count,new_pos):
                    que.append(new_pos)
                    mark_rotten(mat_2d,row_count,col_count,new_pos)
        que.popleft()
        que.append(null_pos)
        min_time+=1
    for i in range(row_count):
        for j in range(col_count):
            pos = Pos(i,j)
            if is_fresh(mat_2d,row_count,col_count,pos):
                return -1
    return min_time-1

def main():
    mat_2d =  [[2, 1, 1, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1]]
    for row in mat_2d:
        print(row)
    print('Min time to rot = ',get_min_time_to_rot(mat_2d))

if __name__ == '__main__':
    main()
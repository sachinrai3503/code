# https://www.geeksforgeeks.org/find-number-of-islands/
# https://www.geeksforgeeks.org/islands-in-a-graph-using-bfs/

"""
Given a boolean 2D matrix, find the number of islands.
A group of connected 1s forms an island. 

Example:
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5
"""

from collections import deque

ADJACENT_CELL_REF = [[-1,-1,-1,0,0,1,1,1],
                     [-1,0,1,-1,1,-1,0,1]]

def is_valid_pos(list_2d, x, y):
    if x<0 or y<0:
        return False
    if x>=len(list_2d) or y>=len(list_2d[0]):
        return False
    if list_2d[x][y] == 0:
        return False
    return True

def is_visited(list_2d, x, y):
    if not is_valid_pos(list_2d,x,y):
        print('Invalid pos x=',x,'y=',y,'passed.')
        return True
    if list_2d[x][y] == -1:
        return True
    return False

def mark_visited(list_2d, x, y):
    if not is_valid_pos(list_2d,x,y):
        print('Invalid pos x=',x,'y=',y,'passed.')
        return
    list_2d[x][y] = -1

def visit_adjacent_dfs(list_2d, x, y):
    if not is_valid_pos(list_2d,x,y) or is_visited(list_2d,x,y):
        return
    mark_visited(list_2d,x,y)
    for i in range(len(ADJACENT_CELL_REF[0])):
        visit_adjacent_dfs(list_2d,x+ADJACENT_CELL_REF[0][i],
            y+ADJACENT_CELL_REF[1][i])

def count_island_dfs(list_2d):
    count = 0
    for i in range(len(list_2d)):
        for j  in range(len(list_2d[0])):
            if list_2d[i][j] == 1 and not is_visited(list_2d,i,j):
                count+=1
                visit_adjacent_dfs(list_2d,i,j)
    return count

class pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def visit_adjacent_bfs(list_2d, x, y):
    if not is_valid_pos(list_2d,x,y) or is_visited(list_2d,x,y):
        return
    que = deque()
    que.append(pos(x,y))
    mark_visited(list_2d,x,y)
    while len(que):
        cur_pos = que.popleft()
        for i in range(len(ADJACENT_CELL_REF[0])):
            t_x = cur_pos.x + ADJACENT_CELL_REF[0][i]
            t_y = cur_pos.y + ADJACENT_CELL_REF[1][i]
            if is_valid_pos(list_2d,t_x,t_y) and \
                not is_visited(list_2d,t_x,t_y):
                mark_visited(list_2d,t_x,t_y)
                que.append(pos(t_x,t_y))

def count_island_bfs(list_2d):
    count = 0
    for i in range(len(list_2d)):
        for j  in range(len(list_2d[0])):
            if list_2d[i][j] == 1 and not is_visited(list_2d,i,j):
                count+=1
                visit_adjacent_bfs(list_2d,i,j)
    return count

def main():
    list_2d = [ [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1]] 
    for list in list_2d:
        print(list)
    print('Island count DFS = ',count_island_dfs(list_2d))
    print('Island count BFS = ',count_island_bfs(list_2d))

if __name__ == '__main__':
    main()

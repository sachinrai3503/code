# https://www.geeksforgeeks.org/minimum-steps-needed-to-cover-a-sequence-of-points-on-an-infinite-grid/
"""
Given an infinite grid, initial cell position (x, y)
 and a sequence of other cell position which needs to be covered 
 in the given order. The task is to find the minimum number of steps
  needed to travel to all those cells.

Note: Movement can be done in any of the eight possible directions 
from a given cell i.e from cell (x, y) you can move to
 any of the following eight positions:(x-1, y+1), (x-1, y), 
 (x-1, y-1), (x, y-1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1) 
 is possible.

Examples:
Input: points[] = [(0, 0), (1, 1), (1, 2)]
Output: 2
Move from (0, 0) to (1, 1) in 1 step(diagonal) and
then from (1, 1) to (1, 2) in 1 step (rightwards)

Input: points[] = [{4, 6}, {1, 2}, {4, 5}, {10, 12}]
Output: 14
Move from (4, 6) -> (3, 5) -> (2, 4) -> (1, 3) ->
(1, 2) -> (2, 3) -> (3, 4) ->
(4, 5) -> (5, 6) -> (6, 7) ->
(7, 8) -> (8, 9) -> (9, 10) -> (10, 11) -> (10, 12)
"""

def get_diff(a, b):
    return (a-b) if a>b else (b-a)

def find_min_steps(points_list):
    steps_count = 0
    for i in range(0,len(points_list)-1):
        x_diff = get_diff(points_list[i][0],points_list[i+1][0])
        y_diff = get_diff(points_list[i][1],points_list[i+1][1])
        if x_diff > y_diff:
            steps_count+=x_diff
        else:
            steps_count+=y_diff
    return steps_count

def main():
    point_list =[(4, 6), (1, 2), (4, 5), (10, 12)]
    print('points=>',point_list)
    print(find_min_steps(point_list))

if __name__ == '__main__':
    main()
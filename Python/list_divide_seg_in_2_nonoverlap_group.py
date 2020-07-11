# https://www.geeksforgeeks.org/divide-n-segments-into-two-non-empty-groups-such-that-given-condition-is-satisfied/https://www.geeksforgeeks.org/divide-n-segments-into-two-non-empty-groups-such-that-given-condition-is-satisfied/
"""
Given N segments (or ranges) represented by two non-negative integers L and R.
Divide these segments into two non-empty groups such that there are 
no two segments from different groups that share a common point. 

If if it is possible to do so, assign each segment a number from the set {1, 2} 
otherwise print Not Possible.

Examples:

Input: arr[][] = {{5, 5}, {2, 3}, {3, 4}}
Output: 2 1 1

Input: arr[][] = {{3, 5}, {2, 3}, {1, 4}}
Output: Not Possible
"""

import sys

def sort(seg_list):
    """
    Sort based on segment start index
    """
    for i in range(0,len(seg_list)):
        min = i
        for j in range(i+1,len(seg_list)):
            if seg_list[j][0]<seg_list[min][0]:
                min = j
        seg_list[i], seg_list[min] = seg_list[min], seg_list[i]

def divide_segments(seg_list):
    if len(seg_list)==0:
        return []
    op_list = [0 for i in range(0,len(seg_list))]
    is_possible = False
    # Start and end for 1st group
    sort(seg_list)
    # print(seg_list)
    s, e = seg_list[0][0], seg_list[0][1]
    op_list[0] = [seg_list[0],1]
    for i in range(1,len(seg_list)):
        if seg_list[i][1]<s or seg_list[i][0]>e:
            op_list[i] = [seg_list[i],2]
            is_possible = True
        else:
            op_list[i] = [seg_list[i],1]
            s = s if s<=seg_list[i][0] else seg_list[i][0]
            e = e if e>=seg_list[i][1] else seg_list[i][1]
    return op_list, is_possible

def main():
    seg_list = [[1, 10 ], [2, 4 ], [5, 6 ],[11,12]]
    print('segments = ',seg_list)
    print(divide_segments(seg_list))

if __name__ == '__main__':
    main()
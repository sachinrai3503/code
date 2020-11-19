# https://www.geeksforgeeks.org/paths-requiring-minimum-number-of-jumps-to-reach-end-of-array/

""""
Given an array arr[], where each element represents the maximum number of steps 
that can be made forward from that element, the task is to print all possible
 paths that require the minimum number of jumps to reach the end of the given 
 array starting from the first array element.

Note: If an element is 0, then there are no moves allowed from that element.

Examples:

Input: arr[] = {1, 1, 1, 1, 1}
Output:
0 ⇾ 1 ⇾ 2 ⇾ 3 ⇾4
Explanation:
In every step, only one jump is allowed.
Therefore, only one possible path exists to reach end of the array.

Input: arr[] = {3, 3, 0, 2, 1, 2, 4, 2, 0, 0}
Output:
0 ⇾ 3 ⇾ 5 ⇾ 6 ⇾ 9
0 ⇾ 3 ⇾ 5 ⇾ 7 ⇾ 9
"""

from sys import maxsize


def get_min_jumps(steps):
    length = len(steps)
    jumps = [maxsize]*length
    for i in range(length-1, -1, -1):
        if i == length-1:
            jumps[i] = 0
            continue
        min_jump = maxsize
        step = steps[i]
        j = 1
        while j <= step and (j+i) < length:
            if jumps[i+j] < min_jump:
                min_jump = jumps[i+j]
            j += 1
        jumps[i] = min_jump+1 if min_jump != maxsize else min_jump
    return jumps


def print_all_path(steps, jumps, from_index, reach, req_jump, path):
    if req_jump == -1:
        print(path)
        return
    length = len(steps)
    i = 0
    while i < reach and from_index+i < length:
        j = from_index + i
        if jumps[j] == req_jump:
            path.append(j)
            print_all_path(steps, jumps, j+1, steps[j], jumps[j]-1, path)
            path.pop()
        i += 1


def main():
    steps = [1,2,3,4,5,6,7,8,9,10,11]
    print('Steps>>', steps)
    min_jumps = get_min_jumps(steps)
    print('Min jump to reach =', min_jumps)
    if len(steps) > 0:
        print_all_path(steps, min_jumps, 0, 1, min_jumps[0], list())


if __name__ == '__main__':
    main()

# https://www.geeksforgeeks.org/painters-partition-problem/
# https://www.geeksforgeeks.org/painters-partition-problem-set-2/
# https://www.interviewbit.com/problems/painters-partition-problem/
"""
Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters
 available and each of them takes B units of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the
 constraints that any painter will only paint contiguous sections of board.

Note - 
1 - 2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
2 - A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.

Return the ans % 10000003



Input Format
The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer array C.

Output Format
Return minimum time required to paint all boards under the constraints that any
 painter will only paint contiguous sections of board % 10000003.

Constraints
1 <=A <= 1000
1 <= B <= 10^6
1 <= C.size() <= 10^5
1 <= C[i] <= 10^6

For Example
Input 1:
    A = 2
    B = 5
    C = [1, 10]
Output 1:
    50
Explanation 1:
    Possibility 1:- same painter paints both blocks, time taken = 55units
    Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
    There are no other distinct ways to paint boards.
    ans = 50%10000003

Input 2:
    A = 10
    B = 1
    C = [1, 8, 11, 3]
Output 2:
    11
"""

from sys import maxsize

# This is not efficient - O(k(n^2))
class Solution1:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        length = len(C)
        op = [[0 for j in range(length)] for i in range(2)]
        i = 0
        while i<A:
            cur_row = i%2
            prev_row = 0 if cur_row==1 else 1
            for j in range(length-1, -1, -1):
                min_time = maxsize
                t_time = 0
                for k in range(j,length):
                    t_time+=(C[k]*B)
                    rem_time = maxsize
                    if k!=length-1:
                        if i>0: rem_time = op[prev_row][k+1]
                    else: rem_time = 0
                    min_time = min(min_time, max(t_time, rem_time))
                op[cur_row][j] = min_time
            i+=1
            # print(op)
        return (op[(A-1)%2][0]%10000003)

# Below solution is more efficent in that is uses binary search
# Time complexity - (N*log(sum(arr)))
def get_max_in_list(ip_list):
    _max = -1*maxsize
    for num in ip_list:
        _max = max(_max, num)
    return _max

def get_list_sum(ip_list):
    _sum = 0
    for num in ip_list:
        _sum+=num
    return _sum

# Returns the min. painter needed when each painter at max can paint k unit.
def get_painter_count(paints, k):
    count = 1
    t_unit = 0
    for i in range(len(paints)):
        t_unit+=paints[i]
        if t_unit>k:
            t_unit = paints[i]
            count+=1
    return count

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        low = get_max_in_list(C) # When many painter are allowed.
        hi  = get_list_sum(C)    # When only 1 painter is allowed
        while low<hi:
            mid = low + (hi-low)//2
            # Counts painter when each painter is allowed max of mid units to paint
            t_count = get_painter_count(C, mid)
            if t_count<=A:
                hi = mid
            else:
                low = mid+1
        return (low*B)%10000003
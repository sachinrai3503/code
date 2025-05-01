# https://leetcode.com/problems/student-attendance-record-ii
"""
An attendance record for a student can be represented as a string where each character signifies whether
 the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:
The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.

Given an integer n, return the number of possible attendance records of length n that make a student eligible 
 for an attendance award. The answer may be very large, so return it modulo 109 + 7.

Example 1:
Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:
Input: n = 1
Output: 3

Example 3:
Input: n = 10101
Output: 183236316

Constraints:
1 <= n <= 105
"""

class Solution:
    def checkRecord(self, n: int) -> int:
        m = 1000000007
        op_with_a = [[3,3,2], # value for n = 2 # [P, L, A]
                     [1,1,1]  # value for n = 1 # [P, L, A]
                    ]
        op_without_a = [[2,2], # value for n = 2 # [P, L]
                        [1,1]  # value for n = 1 # [P, L]
                        ]
        if n<=2: return sum(op_with_a[n%2])
        for i in range(3, n+1):
            cur_row = i%2
            prev_row = 0 if cur_row==1 else 1
            # OP with A
            # For L
            op_with_a[cur_row][1] = (op_with_a[prev_row][0] + op_with_a[prev_row][2] + \
                                    op_with_a[cur_row][0] + op_with_a[cur_row][2])%m
            # For P
            op_with_a[cur_row][0] = sum(op_with_a[prev_row])%m
            # For A
            op_with_a[cur_row][2] = (op_without_a[prev_row][0] + op_without_a[prev_row][1])%m

            # OP without A
            # For L
            op_without_a[cur_row][1] = (op_without_a[prev_row][0] + op_without_a[cur_row][0])%m
            # For P
            op_without_a[cur_row][0] = sum(op_without_a[prev_row])%m
        return sum(op_with_a[n%2])%m
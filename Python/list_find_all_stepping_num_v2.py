# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""
Return all non-negative integers of length n such that the absolute difference
 between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example,
 01 has one leading zero and is invalid.

You may return the answer in any order. 

Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Example 3:
Input: n = 2, k = 0
Output: [11,22,33,44,55,66,77,88,99]

Example 4:
Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Example 5:
Input: n = 2, k = 2
Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
 
Constraints:
2 <= n <= 9
0 <= k <= 9
"""


def get_all_consec_diff_number(k, prev_num, max_dig_count, cur_dig_count, op_list):
    if cur_dig_count == max_dig_count:
        op_list.append(prev_num)
        return
    last_digit = prev_num % 10
    if last_digit-k >= 0:
        get_all_consec_diff_number(
            k, prev_num*10 + last_digit-k, max_dig_count, cur_dig_count+1, op_list)
    if k != 0 and last_digit+k <= 9:
        get_all_consec_diff_number(
            k, prev_num*10 + last_digit+k, max_dig_count, cur_dig_count+1, op_list)


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        op_list = list()
        for i in range(1, 10):
            get_all_consec_diff_number(k, i, n, 1, op_list)
        return op_list

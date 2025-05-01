# https://leetcode.com/problems/count-number-of-ways-to-place-houses
"""
There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are 
 numbered from 1 to n. On each plot, a house can be placed.

Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side
 of the street. Since the answer may be very large, return it modulo 109 + 7.

Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot
 on the other side of the street.

Example 1:
Input: n = 1
Output: 4
Explanation: 
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.

Example 2:
Input: n = 2
Output: 9
Explanation: The 9 possible arrangements are shown in the diagram above.

Constraints:
1 <= n <= 104
"""

class Solution:
    def countHousePlacements(self, n: int) -> int:
        prev_col = [1, 0] # [total, house in any one cell]
        prev_to_prev_col = [1, 0] # [total, house in any one cell]
        m = (10**9 + 7)
        for i in range(1, n+1):
            op_with_one_house_in_i_col = (prev_col[1] + prev_to_prev_col[0])%m
            op = (prev_col[0] + prev_to_prev_col[0] + 2*op_with_one_house_in_i_col)%m
            prev_to_prev_col = prev_col
            prev_col = [op, op_with_one_house_in_i_col]
        return prev_col[0]
    
    # This is faster
    def countHousePlacements_2(self, n: int) -> int:
        if n==1: return 4
        if n==2: return 9
        m = (10**9 + 7)
        b, a = 3, 2 # values for single row
        for i in range(3, n+1):
            c = (b + a)%m
            a = b
            b = c
        return (c*c)%m
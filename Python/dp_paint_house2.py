# https://www.lintcode.com/problem/516
# https://leetcode.com/problems/paint-house-ii
"""
There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. You have to paint
 all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost 
 matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; 
 costs[1][2] is the cost of painting house 1 with color 2, and so on... Find 
 the minimum cost to paint all houses.

All costs are positive integers.

Example 1
Input:
costs = [[14,2,11],[11,14,5],[14,3,10]]
Output: 10

Example 2
Input:
costs = [[5]]
Output: 5

Challenge
Could you solve it in O(nk)
"""
from sys import maxsize

from typing import (
    List,
)

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    # NOTE - if n>1 then k>=2
    #      - if n==1 then k>=1
    def min_cost_i_i(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = 0 if not n else len(costs[0])
        if n==0: return 0
        if k<=0: return maxsize
        if k==1 and n>1: return maxsize
        dp_min = [0 for i in range(k+1)] # dp_min[i] = min(dp_min[i], dp_min[i+1])
        dp_min[k] = maxsize
        dp = [[0 for i in range(k)] for j in range(2)]
        for i in range(n-1, -1, -1):
            cur_row = i%2
            prev_row = 0 if cur_row==1 else 1
            prev_min = maxsize
            for j in range(k):
                t_min =  min(prev_min, dp_min[j+1]) if k>1 else 0 # case when k==1
                dp[cur_row][j] = costs[i][j] + t_min
                prev_min = min(prev_min, dp[prev_row][j])
            for j in range(k-1,-1,-1):
                dp_min[j] = min(dp[cur_row][j], dp_min[j+1])
        return min(dp[0])
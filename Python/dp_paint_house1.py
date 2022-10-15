# https://www.geeksforgeeks.org/minimize-cost-of-painting-n-houses-such-that-adjacent-houses-have-different-colors
# https://leetcode.com/problems/paint-house
# https://www.lintcode.com/problem/515
"""
There are a row of n houses, each house can be painted with one of the three 
 colors: red, blue or green. The cost of painting each house with a certain 
 color is different. You have to paint all the houses such that no two adjacent
 houses have the same color, and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
 For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the
 cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Example 1:
Input: [[14,2,11],[11,14,5],[14,3,10]]
Output: 10

Example 2:
Input: [[1,2,3],[1,4,6]]
Output: 3
"""

from typing import (
    List,
)

class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def min_cost(self, costs: List[List[int]]) -> int:
        dp = [[0,0,0],[0,0,0]]
        n = len(costs)
        for i in range(n-1, -1, -1):
            cur_row = i%2
            prev_row = 0 if cur_row else 1
            dp[cur_row][0] = costs[i][0] + min(dp[prev_row][1], dp[prev_row][2])
            dp[cur_row][1] = costs[i][1] + min(dp[prev_row][0], dp[prev_row][2])
            dp[cur_row][2] = costs[i][2] + min(dp[prev_row][0], dp[prev_row][1])
        return min(dp[0])
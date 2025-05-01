# https://leetcode.com/problems/coin-change/
# https://www.geeksforgeeks.org/coin-change-dp-7/
"""
You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you need 
to make up that amount. If that amount of money cannot be made up by any 
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin. 

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Example 4:
Input: coins = [1], amount = 1
Output: 1

Example 5:
Input: coins = [1], amount = 2
Output: 2

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from sys import maxsize
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_count = len(coins)
        dp = [maxsize for i in range(amount+1)]
        visited = set()
        dp[0] = 0
        for i in range(coins_count):
            coin = coins[i]
            if coin in visited: continue
            visited.add(coin)
            for j in range(coin, amount+1):
                if dp[j-coin]!=maxsize:
                    dp[j] = min(dp[j], dp[j-coin]+1)
        # print(f'{dp=}')
        return dp[-1] if dp[-1]!=maxsize else -1
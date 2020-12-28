# https://leetcode.com/problems/coin-change/
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

def get_min(a, b):
    return a if a<b else b

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount==0: return 0
        op = [maxsize]*(amount+1)
        for i in range(len(coins)-1,-1,-1):
            coin = coins[i]
            for j in range(coin, amount+1):
                if j==coin: op[j] = 1
                else:
                    with_coin = op[j-coin]+1 if op[j-coin]!=maxsize else op[j-coin]
                    op[j] = get_min(op[j], with_coin)
        return op[amount] if op[amount]!=maxsize else -1
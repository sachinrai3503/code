# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee
 representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the
 transaction fee for each transaction.

Note:
You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 
Constraints:
1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
"""

from sys import maxsize
from typing import List

class Solution:

    # This will timeout. O(n^2)
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        prices_len = len(prices)
        dp = [0 for i in range(prices_len)]
        for i in range(prices_len-2, -1, -1):
            for j in range(i+1, prices_len):
                t_price = prices[i] + fee
                if prices[j]<t_price: continue
                remaining_profit = 0 if j==(prices_len-1) else dp[j+1]
                dp[i] = max(dp[i], prices[j]-t_price + remaining_profit)
            dp[i] = max(dp[i], dp[i+1])
        # print(f'{dp=}')
        return dp[0]

    # This is O(n)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        prices_len = len(prices)
        max_profit_with_i = 0
        best_sale_profit_at = 0
        for i in range(prices_len-1, -1, -1):
            max_profit_till_now = max_profit_with_i
            max_profit_with_i = max(max_profit_with_i, best_sale_profit_at - prices[i] - fee)
            best_sale_profit_at = max(best_sale_profit_at, max_profit_till_now + prices[i])
        return max_profit_with_i
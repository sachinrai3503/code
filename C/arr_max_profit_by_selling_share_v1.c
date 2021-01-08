// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
/*
Say you have an array for which the ith element is the price of a given stock
 on day i.

If you were only permitted to complete at most one transaction (i.e., buy one
 and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/
#include <limits.h>

int maxProfit(int* prices, int pricesSize){
    if(pricesSize<0) return INT_MIN;
    int last_buy = INT_MAX;
    int profit = 0;
    int i = 0;
    for(;i<pricesSize;i++){
        if(prices[i]<last_buy){
            last_buy = prices[i];
        }else {
            int t_profit = prices[i] - last_buy;
            if(t_profit>profit) profit = t_profit;
        }
    }
    return profit;
}

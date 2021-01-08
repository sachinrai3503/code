// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
// https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/
/*
Say you have an array for which the ith element is the price of a given stock
 on day i.

Design an algorithm to find the maximum profit. You may complete at most 2 
 transactions.

Note: You may not engage in multiple transactions at the same time
  (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105
*/

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int maxProfit(int* prices, int pricesSize){
    int max_profit = 0;
    int *profit = (int*)calloc(pricesSize, sizeof(int));
    // Getting the max profit with 1 transaction allowed.
    int best_sell_at = prices[pricesSize-1];
    int i = pricesSize-2;
    for(;i>=0;i--){
        if(prices[i]>best_sell_at){
            best_sell_at = prices[i];
            profit[i] = profit[i+1];
        }else{
            profit[i] = get_max(profit[i+1], best_sell_at - prices[i]);
        }
    }
    // print_arr(profit, pricesSize);
    max_profit = profit[0]; // Max profit with 1 transaction
    // Now use above cal. to find max profit with 2 transaction
    int best_buy_at = prices[0];
    profit[0] = 0;
    for(i=1;i<pricesSize;i++){
        if(prices[i]<best_buy_at){
            best_buy_at = prices[i];
            profit[i] = profit[i-1];
        }else{
            profit[i] = get_max(profit[i-1], (prices[i]-best_buy_at) + ((i<pricesSize-1)?profit[i+1]:0));
        }
    }
    // print_arr(profit, pricesSize);
    return get_max(max_profit, profit[pricesSize-1]);
}
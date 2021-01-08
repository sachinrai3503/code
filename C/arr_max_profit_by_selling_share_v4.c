// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
// https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/
/*
You are given an integer array prices where prices[i] is the price of a given
 stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k
 transactions.

Notice that you may not engage in multiple transactions simultaneously
 (i.e., you must sell the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6),
             profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6
              (price = 3), profit = 3-0 = 3.
 
Constraints:
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
*/


int** init_2D_arr(int row, int col){
    int **arr = (int**)calloc(row, sizeof(int*));
    int i = 0;
    for(;i<row;i++){
        arr[i] = (int*)calloc(col, sizeof(int));
    }
    return arr;
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int maxProfit(int k, int* prices, int pricesSize){
    if(k==0 || pricesSize==0) return 0;
    int **arr = init_2D_arr(2, pricesSize);
    int t = 0;
    for(;t<k;t++){
        int cur_row = t%2;
        int prev_row = !(cur_row);
        int prev_offset = 0;
        int i = pricesSize-1;
        for(;i>=0;i--){
            int last_profit = 0;
            if(i<pricesSize-1) last_profit = arr[cur_row][i+1];
            arr[cur_row][i] = get_max(last_profit, prev_offset - prices[i]);
            int profit_with_t_minus_1_transaction = 0;
            if(t>0 && i<pricesSize-1) profit_with_t_minus_1_transaction = arr[prev_row][i+1];
            prev_offset = get_max(prev_offset, prices[i] + profit_with_t_minus_1_transaction);
        }
    }
    return arr[(k-1)%2][0];
}
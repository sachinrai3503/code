// https://leetcode.com/problems/minimum-cost-to-merge-stones/
// https://www.geeksforgeeks.org/minimum-cost-to-merge-all-elements-of-list/
/*
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, 
and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is
 impossible, return -1.

Example 1:
Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:
Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:
Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 
Constraints:
n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void print_2d(int **ip, int row, int col){
    int i = 0;
    for(;i<row;i++){
        print_arr(ip[i],col);
    }
}

int get_min(int a, int b){
    if(a>b) return b;
    return a;
}

int** init_2d_arr(int row, int col){
    int **op = (int**)calloc(row, sizeof(int*));
    int i = 0;
    for(;i<row;i++){
        op[i] = (int*)calloc(col, sizeof(int));
    }
    return op;
}

int* get_prefix_sum(int *stones, int stonesSize){
    int *op = (int*)calloc(stonesSize, sizeof(int));
    int t_sum = 0;
    int i = 0;
    for(;i<stonesSize;i++){
        t_sum+=stones[i];
        op[i] = t_sum;
    }
    return op;
}

// This greedy approach won't work for below TC - 
// [6,4,4,6]
// if we merge greedily, [6, [4, 4], 6] -> [[6, 8], 6] -> [14, 6] -> [20] (cost: 42),
// while the optimal way is [[6, 4], 4, 6] -> [10, [4, 6]] -> [10, 10] -> [20] (cost:40).
int mergeStones1(int* stones, int stonesSize, int k){
    int ans = 0;
    int ele_count = stonesSize;
    while(ele_count>1 && k<=ele_count){
        int s = 0;
        int e = -1;
        int ts = 0;
        int sum = INT_MAX;
        int t_sum = 0;
        int cur_win_ele = 0;
        int i = 0;
        for(;i<stonesSize;i++){
            if(stones[i]==INT_MIN) continue;
            t_sum+=stones[i];
            cur_win_ele++;
            if(cur_win_ele==k){
                if(t_sum<sum){
                    sum = t_sum;
                    s = ts;
                    e = i;
                }
                while(ts<i && (stones[ts]==INT_MIN ||cur_win_ele==k)){
                    if(stones[ts]==INT_MIN) ts++;
                    else{
                        t_sum-=stones[ts];
                        cur_win_ele--;
                        ts++;
                    }
                }
            }
        }
        stones[s] = sum;
        ans+=sum;
        for(s=s+1;s<=e;s++) stones[s] = INT_MIN;
        ele_count-=(k-1);
        print_arr(stones, stonesSize);
    }
    if(ele_count!=1) return -1;
    return ans;
}

int mergeStones(int* stones, int stonesSize, int k){
    if(stonesSize==1) return 0;
    if(k>stonesSize) return -1;
    if((stonesSize-k)%(k-1)) return -1;
    int **dp = init_2d_arr(stonesSize, stonesSize);
    int *p_sum = get_prefix_sum(stones, stonesSize);
    // print_arr(p_sum, stonesSize);
    // print_2d(dp, stonesSize, stonesSize);
    int t_k = k-1;
    for(;t_k<stonesSize;t_k++){
        // printf("t_k=%d\n",t_k);
        int i = 0;
        for(;i<stonesSize-t_k;i++){
            int j = i+t_k;
            // printf("i=%d j=%d\n",i,j);
            dp[i][j] = INT_MAX;
            int m = i;
            for(;m<j;m+=(k-1)){
                // printf("i=%d j=%d m=%d\n",i,j,m);
                dp[i][j] = get_min(dp[i][j], dp[i][m] + dp[m+1][j]);
            }
            if((j-i)%(k-1)==0){
                dp[i][j]+=(i==0)?p_sum[j]:p_sum[j]-p_sum[i-1];
            }
            // print_2d(dp, stonesSize, stonesSize);
        }
    }
    return dp[0][stonesSize-1];
}
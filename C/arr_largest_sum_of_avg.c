// https://leetcode.com/problems/largest-sum-of-averages/
/*
You are given an integer array nums and an integer k. You can partition the array
 into at most k non-empty adjacent subarrays. The score of a partition is the sum
 of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not
 necessarily an integer.

Return the maximum score you can achieve of all the possible partitions. Answers
 within 10-6 of the actual answer will be accepted.

Example 1:
Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation: 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Example 2:
Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000
 
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 104
1 <= k <= nums.length
*/

#include <stdio.h>
#include <malloc.h>
#include <float.h>

double** init2D(int row, int col){
    double **dp = (double**)calloc(row, sizeof(double*));
    int i = 0;
    for(;i<row;i++){
        dp[i] = (double*)calloc(col, sizeof(double));
    }
    return dp;
}

double max(double a, double b){
    if(a>b) return a;
    return b;
}

double largestSumOfAverages(int* nums, int numsSize, int k){
    double maxAvg = DBL_MIN;
    double **dp = init2D(2, numsSize);
    int tK = 0;
    for(;tK<k;tK++){
        int curRow = (tK%2);
        int prevRow = !curRow;
        int i = numsSize-1;
        for(;i>=0;i--){
            int tSum = 0;
            double tAvg = DBL_MIN;
            int j = i;
            for(;j<numsSize;j++){
                tSum+=nums[j];
                double otherPartAvg = DBL_MIN;
                if(j==numsSize-1) otherPartAvg = 0;
                else if(tK!=0) otherPartAvg = dp[prevRow][j+1];
                if(otherPartAvg==DBL_MIN) tAvg = DBL_MIN;
                else tAvg = max(tAvg, ((double)tSum/(j-i+1)) + otherPartAvg);
            }
            dp[curRow][i] = tAvg;
        }
        maxAvg = max(maxAvg, dp[curRow][0]);
    }
    return maxAvg;
}
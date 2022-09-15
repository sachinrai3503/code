// https://leetcode.com/problems/partition-equal-subset-sum/
/*
Given a non-empty array nums containing only positive integers, find if the array
 can be partitioned into two subsets such that the sum of elements in both subsets
 is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
*/

#include <stdio.h>
#include <malloc.h>
#define true 1
#define false 0

typedef int bool;

void printArr(int *ip, int length){
    int i =0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int getSum(int *ip, int length){
    int sum = 0;
    int i = 0;
    for(;i<length;i++){
        sum+=ip[i];
    }
    return sum;
}

bool canPartition(int* nums, int numsSize){
    int tSum = getSum(nums, numsSize);
    if(tSum%2==1) return false;
    int mid = tSum/2;
    bool *dp = (bool*)calloc(mid+1, sizeof(bool));
    // printf("tSum=%d mid=%d\n",tSum, mid);
    int i = numsSize-1;
    for(;i>=0;i--){
        int num = nums[i];
        int j = mid;
        for(;j>num;j--){
            if(dp[j-num]) dp[j] = true;
        }
        if(j==num) dp[j]=true;
        if(dp[mid]) return true;
        // printArr(dp, tSum+1);
    }
    return false;
}
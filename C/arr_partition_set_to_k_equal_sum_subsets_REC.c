// https://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
// https://www.geeksforgeeks.org/partition-of-a-set-into-k-subsets-with-equal-sum-using-bitmask-and-dp/
/*
Given an integer array of N elements, the task is to divide this array into K
 non-empty subsets such that the sum of elements in every subset is same.
 
All elements of this array should be part of exactly one partition.
Examples:

Input : arr = [2, 1, 4, 5, 6], K = 3
Output : Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Input  : arr = [2, 1, 5, 5, 6], K = 3
Output : No
*/

// This recursive approach won't work as takes lot of time.
// DP sol. arr_partition_set_to_k_equal_sum_subsets_DP.c also doesn't work for
// all cases.

#include <stdio.h>
#include <malloc.h>
#define false 0
#define true 1
typedef int bool;

int getArrSum(int *ip, int length){
    int sum = 0;
    int i = 0;
    for(;i<length;i++){
        sum+=ip[i];
    }
    return sum;
}

bool checkForPartition(int *ip, int length, int *sets, int k, bool *visited,
                       int reqSum, int *reqSumSetCount){
    if(*reqSumSetCount==k) return true;
    int i = 0;
    for(;i<length;i++){
        if(visited[i]) continue;
        int j = 0;
        for(;j<k;j++){
            if(sets[j]+ip[i]>reqSum) continue;
            sets[j]+=ip[i];
            visited[i] = true;
            if(sets[j]==reqSum) (*reqSumSetCount)++;
            bool result = checkForPartition(ip,length,sets,k,visited,
                                            reqSum,reqSumSetCount);
            if(result) return true;
            if(sets[j]==reqSum) (*reqSumSetCount)--;
            sets[j]-=ip[i];
            visited[i] = false;
        }
    }
    return false;
}

bool canPartitionKSubsets(int* nums, int numsSize, int k){
    if(k==1) return true;
    if(k>numsSize) return false;
    int arrSum = getArrSum(nums, numsSize);
    if(arrSum%k) return false;
    int reqSum = arrSum/k;
    bool *visited = (bool*)calloc(numsSize, sizeof(bool));
    int *sets = (int*)calloc(k, sizeof(int));
    int setCount = 0;
    return checkForPartition(nums, numsSize, sets, k, visited, reqSum, &setCount);
}

int main(){
    int ip[] = {9,10,1,7,2,7,1,1,1,3};
    int k = 3;
    int length = sizeof(ip)/sizeof(ip[0]);
    printf("Can partition=%d",canPartitionKSubsets(ip,length,k));
}
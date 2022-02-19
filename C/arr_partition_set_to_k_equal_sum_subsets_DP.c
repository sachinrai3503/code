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

// The recursive approach won't work as takes lot of time.
// Below DP solution also won't work for all cases as shown.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>
#define false 0
#define true 1

typedef int bool;

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

void set_arr(int *ip, int length, int value){
    int i = 0;
    for(;i<length;i++){
        ip[i] = value;
    }
}

int get_arr_sum(int *ip, int length){
    int sum = 0;
    int i = 0;
    for(;i<length;i++){
        sum+=ip[i];
    }
    return sum;
}

void mark_visited(int *ip, int *visited, int length, int *sum_map, int from){
    while(from!=0){
        visited[sum_map[from]] = 1;
        from = from - ip[sum_map[from]];
    }
}


/*
Note - Wrong sol. Doesn't work for below test case
Ip = [9,10,1,7,2,7,1,1,1,3] , K = 3
*/   
int can_be_partitioned(int *ip, int length, int k){
    if(k==0) return 0;
    // if(k==1) return 1;
    int arr_sum = get_arr_sum(ip,length);
    if(arr_sum%k) return 0;
    int req_sum = arr_sum/k;
    int *sum_map = (int*)calloc(req_sum+1,sizeof(int));
    int *visited = (int*)calloc(length,sizeof(int));
    int i = 0;
    for(;i<k;i++){
        set_arr(sum_map,req_sum+1,-1);
        int j = length-1;
        for(;j>=0;j--){
            if(visited[j]==0){
                if(ip[j]>req_sum) return 0;
                int p = req_sum;
                for(;p>=ip[j];p--){
                    // Here checking for sum_map[p]==-1 is imp as without it
                    // we can say if req_sum can be made or not but we might end
                    // up marking wrong indexes as visited. eg - {2 1 4 5 6} K=3
                    // Set1 = {6} and while computing for Set2 -> sum 5, 4 will 
                    // be made but with 1 we can make 6(5+1), 5(4+1, this over
                    // rides previous entry) and so 1,4 will be wrongly marked 
                    // as visited.
                    if(sum_map[p]==-1 && (p==ip[j] || sum_map[p-ip[j]]!=-1))
                        sum_map[p] = j;
                }
            }
            if(sum_map[req_sum]!=-1) break;
        }
        if(sum_map[req_sum]==-1) return 0;
        mark_visited(ip,visited,length,sum_map,req_sum);
    }
    return 1;
}

int main(){
    int ip[] = {9,10,1,7,2,7,1,1,1,3};
    int k = 3;
    int length = sizeof(ip)/sizeof(ip[0]);

    printf("ip>");print_arr(ip,length);
    printf("k=%d\n",k);
    printf("Is partition into k set possible = %d",
            can_be_partitioned(ip,length,k));

    return 0;
}

// NOTE - BELOW IS CORRECT SOL. - DP + BIT MASKING
// https://www.geeksforgeeks.org/partition-of-a-set-into-k-subsets-with-equal-sum-using-bitmask-and-dp/
int* init_arr(int length, int value){
    int *dp = (int*)calloc(length, sizeof(int));
    int j = 0;
    for(;j<length;j++) dp[j] = -1;
    return dp;
}

int get_sum(int *ip, int length){
    int sum = 0;
    int i = 0;
    for(;i<length;i++){
        sum+=ip[i];
    }
    return sum;
}

bool canPartitionKSubsets(int* nums, int numsSize, int k){
    if(numsSize<=0 || k<=0) return false;
    if(k>numsSize) return false;
    if(k==1) return true;
    int sum = get_sum(nums, numsSize);
    if(sum%k) return false;
    int target = sum/k;
    int count = 1<<numsSize;
    int *dp = init_arr(count, -1);
    dp[0] = 0;
    int mask = 0;
    for(;mask<count;mask++){
        if(dp[mask]==-1) continue;
        int i = 0;
        for(;i<numsSize;i++){
            if(!(mask&(1<<i)) && dp[mask] + nums[i]<=target){
                dp[mask | (1<<i)] = (dp[mask] + nums[i])%target;
            }
        }
    }
    return dp[count-1]==0;
}

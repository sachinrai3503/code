// https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
// https://www.geeksforgeeks.org/check-if-an-array-can-be-divided-into-pairs-whose-sum-is-divisible-by-k
/*
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of
 each pair is divisible by k.

Return True If you can find a way to do that or False otherwise.
Example 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Example 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to
 divide arr into 3 pairs each with sum divisible by 10.

Example 4:
Input: arr = [-10,10], k = 2
Output: true

Example 5:
Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true

Constraints:
arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105
*/

#include <stdio.h>
#include <malloc.h>
#define true 1
#define false 0

typedef int bool;

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

bool canArrange(int* arr, int arrSize, int k){
    int actual_pair = 0;
    int exp_pair = arrSize/2;
    int *neg_rem = (int*)calloc(k, sizeof(int));
    int *pos_rem = (int*)calloc(k, sizeof(int));
    int i = 0;
    for(;i<arrSize;i++){
        int rem = arr[i]%k;
        // rem_rem is remaining rem
        int rem_rem = 0;
        if(rem>=0){
            if(rem!=0)
                rem_rem = k-rem;
            // printf("rem=%d rem_rem=%d\n",rem, rem_rem);
            if(pos_rem[rem_rem]>0){
                pos_rem[rem_rem]--;
                actual_pair++;
            }else if(neg_rem[rem]>0){
                neg_rem[rem]--;
                actual_pair++;
            }else pos_rem[rem]++;
        }else{
            rem_rem = -k-rem;
            // printf("rem=%d rem_rem=%d\n",rem, rem_rem);
            rem = rem*-1;
            rem_rem*=-1;
            if(neg_rem[rem_rem]>0){
                neg_rem[rem_rem]--;
                actual_pair++;
            }else if(pos_rem[rem]>0){
                pos_rem[rem]--;
                actual_pair++;
            }else neg_rem[rem]++;
        }
        // print_arr(neg_rem, k);
        // print_arr(pos_rem, k);
    }
    if(actual_pair==exp_pair) return true;
    return false;
}
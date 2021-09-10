// https://leetcode.com/problems/split-array-largest-sum/
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
// https://www.interviewbit.com/problems/allocate-books/
// https://www.geeksforgeeks.org/allocate-minimum-number-pages/
/*
Given an array nums which consists of non-negative integers and an integer m,
 you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
*/

#include <stdio.h>
#include <limits.h>

int get_split_count(int *ip, int length, int max_limit){
    int count = 1;
    int t_sum = 0;
    int i = 0;
    for(;i<length;i++){
        t_sum+=ip[i];
        if(t_sum>max_limit){
            t_sum=ip[i];
            count++;
        }
    }
    return count;
}

int splitArray(int* nums, int numsSize, int m){
    if(m>numsSize || m<=0) return -1;
    int low = INT_MIN;
    int high = 0;
    int i = 0;
    for(;i<numsSize;i++){
        if(nums[i]>low) low = nums[i];
        high+=nums[i];
    }
    while(low<high){
        int mid = (low+high)/2;
        int t_k = get_split_count(nums, numsSize, mid);
        if(t_k>m){
            low = mid+1;
        }else{
            high = mid;
        }
    }
    return high;
}
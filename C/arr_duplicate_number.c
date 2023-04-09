// https://leetcode.com/problems/find-the-duplicate-number
/*
Given an array of integers nums containing n + 1 integers where each integer is in
 the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant
 extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which
 appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
*/

#include <stdio.h>

void swap(int *a, int *b){
    (*a)^=(*b)^=(*a)^=(*b);
}

int findDuplicate(int* nums, int numsSize){
    int i = 0;
    for(;i<numsSize;i++){
        while(nums[i]!=(i+1)){
            int exp_index = nums[i]-1;
            if(exp_index<i) return nums[i];
            if(nums[exp_index]==nums[i]) return nums[i];
            swap(nums+i, nums+exp_index);
        }
    }
    printf("Control should not reach here.\n");
    return -1;
}
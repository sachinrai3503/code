// https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/
// https://leetcode.com/problems/single-element-in-a-sorted-array/
/*
You are given a sorted array consisting of only integers where every element
 appears exactly twice, except for one element which appears exactly once.
 Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
*/

int singleNonDuplicate(int* nums, int numsSize){
    int s = 0;
    int e = numsSize-1;
    while(s<=e){
        if(s==e) return nums[s];
        int mid = s + (e-s)/2;
        if(mid%2==0){
            if(nums[mid]==nums[mid+1]) s = mid+2;
            else e = mid;
        }else{
            if(nums[mid]==nums[mid-1]) s = mid+1;
            else e = mid-1;
        }
    }
    return -1;
}

// https://leetcode.com/problems/single-number-iii/
/*
Given an integer array nums, in which exactly two elements appear only once and
 all the other elements appear exactly twice. Find the two elements that appear
 only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only
 constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize){
    long int all_xor = 0;
    int i = 0;
    for(;i<numsSize;i++) all_xor^=nums[i];
    int required_num = all_xor&(-all_xor);
    // printf("all_xor=%ld required_num=%d\n",all_xor,required_num);
    int x_xor = 0;
    int y_xor = 0;
    for(i=0;i<numsSize;i++){
        if(nums[i]&required_num) x_xor^=nums[i];
        else y_xor^=nums[i];
    }
    int *op = (int*)calloc(2, sizeof(int));
    op[0] = x_xor;
    op[1] = y_xor;
    *returnSize = 2;
    return op;
}
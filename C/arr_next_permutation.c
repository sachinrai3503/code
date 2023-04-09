// https://leetcode.com/problems/next-permutation/
/*
A permutation of an array of integers is an arrangement of its members into a 
 sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
 [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater
 permutation of its integer. More formally, if all the permutations of the array
 are sorted in one container according to their lexicographical order, then the 
 next permutation of that array is the permutation that follows it in the sorted
 container. If such arrangement is not possible, the array must be rearranged as
 the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
 have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory. 

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100 
*/

#include <stdio.h>
#include <limits.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int find_first_decreasing(int *nums, int length){
    int prev = INT_MIN;
    int i = length-1;
    while(i>=0){
        if(nums[i]>=prev){
            prev = nums[i];
            i-=1;
        }
        else return i;
    }
    return -1;
}

int binary_search(int *num, int s, int e, int k){
    int _ceil = -1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(num[mid]>k){
            _ceil = mid;
            s = mid+1;
        }else{
            e = mid-1;
        }
    }
    return _ceil;
}

void reverse(int *nums, int s, int e){
    for(;s<e;s++,e--){
        nums[s]^=nums[e]^=nums[s]^=nums[e];
    }
}

void nextPermutation(int* nums, int numsSize){
    int first_decreasing_index = find_first_decreasing(nums, numsSize);
    // printf("first_decreasing_index=%d\n",first_decreasing_index);
    if(first_decreasing_index==-1){
        reverse(nums, 0, numsSize-1);
    }else{
        int next_greater_index = binary_search(nums, first_decreasing_index+1, numsSize-1, nums[first_decreasing_index]);
        // printf("next_greater_index=%d\n",next_greater_index);
        swap(nums+first_decreasing_index, nums+next_greater_index);
        reverse(nums, first_decreasing_index+1, numsSize-1);
    }
}
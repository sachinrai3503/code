// https://leetcode.com/problems/search-in-rotated-sorted-array/
// https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
/*
There is an integer array nums sorted in ascending order (with distinct values).
Given the array nums after the rotation and an integer target, return the index
 of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
*/

typedef int bool;

int search(int* nums, int numsSize, int target){
    int s = 0, e = numsSize-1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(nums[mid]==target) return mid;
        if(s==e) return -1;
        if(nums[s]<nums[mid]){
            if(target>=nums[s] && target<nums[mid]){
                e = mid-1;
            }else{
                s = mid+1;
            }
        }else{
            if(target>=nums[mid+1] && target<=nums[e]){
                s = mid+1;
            }else{
                e = mid-1;
            }
        }
    }
    return -1;
}

// https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-rotated-array-with-duplicates/
// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
/*
There is an integer array nums sorted in non-decreasing order 
 (not necessarily with distinct values).
Given the array nums after the rotation and an integer target,
 return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
*/

bool search(int* ip, int numsSize, int target){
    int s = 0, e = numsSize-1;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(ip[mid]==target) return 1;
        if(s==e) return 0;
        if(ip[s]==ip[mid] && ip[mid]==ip[e]){
            s++;e--;
        }else if(s==mid || ip[s]<=ip[mid]){
            if(target>=ip[s] && target<ip[mid]) e = mid-1;
            else s = mid+1;
        }else{
            if(target>=ip[mid+1] && target<=ip[e]) s = mid+1;
            else e = mid-1;
        }
    }
    return 0;
}
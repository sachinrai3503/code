// https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
// https://leetcode.com/problems/median-of-two-sorted-arrays/
/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
 return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
 
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
*/

#include <stdio.h>
#include <limits.h>
#define true 1
#define false 0

typedef int bool;

void swap_pointer(int **a, int **b){
    int *temp = *a;
    *a = *b;
    *b = temp;
}

void swap_int(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int get_min(int a, int b){
    if(a<b) return a;
    return b;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    if(nums1Size>nums2Size){
        swap_pointer(&nums1, &nums2);
        swap_int(&nums1Size, &nums2Size);
    }
    int total_ele = nums1Size + nums2Size;
    int ele_count_1st_half = (total_ele+1)/2;
    int min_index = 0, max_index = nums1Size;
    int ele_count_1st_arr = 0;
    int ele_count_2nd_arr = 0;
    bool loop = true;
    while(loop){
        loop = false;
        ele_count_1st_arr = (min_index+max_index)/2;
        ele_count_2nd_arr = ele_count_1st_half - ele_count_1st_arr;
        if(ele_count_1st_arr>0 && ele_count_2nd_arr<nums2Size && nums1[ele_count_1st_arr-1]>nums2[ele_count_2nd_arr]){
            max_index = ele_count_1st_arr-1;
            loop = true;
        }
        else if(ele_count_2nd_arr>0 && ele_count_1st_arr<nums1Size && nums2[ele_count_2nd_arr-1]>nums1[ele_count_1st_arr]){
            min_index = ele_count_1st_arr+1;
            loop = true;
        }
    }
    if(ele_count_1st_arr==0 && ele_count_2nd_arr==0) return INT_MIN;
    if(total_ele%2){
        int _1st_arr_ele = INT_MIN, _2nd_arr_ele = INT_MIN;
        if(ele_count_1st_arr>0) _1st_arr_ele = nums1[ele_count_1st_arr-1];
        if(ele_count_2nd_arr>0) _2nd_arr_ele = nums2[ele_count_2nd_arr-1];
        return (double)get_max(_1st_arr_ele, _2nd_arr_ele);
    }else{
        int a = INT_MIN, b = INT_MIN;
        int c = INT_MAX, d = INT_MAX;
        if(ele_count_1st_arr>0) a = nums1[ele_count_1st_arr-1];
        if(ele_count_1st_arr<nums1Size) c = nums1[ele_count_1st_arr];
        if(ele_count_2nd_arr>0) b = nums2[ele_count_2nd_arr-1];
        if(ele_count_2nd_arr<nums2Size) d = nums2[ele_count_2nd_arr];
        // printf("a=%d b=%d c=%d d=%d get_max(a,b)=%d get_min(c,d)=%d\n",a,b,c,d, get_max(a,b), get_min(c,d));
        return ((float)(get_max(a,b)+get_min(c,d)))/2.0;
    }
}
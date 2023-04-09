// https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri
/*
Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Examples : 
  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1 
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

int get_max(int a, int b){
    return (a>b)?a:b;
}

int* get_right_max(int *arr, int length){
    int *op = (int*)calloc(length, sizeof(int));
    int prev = INT_MIN;
    int i = length-1;
    for(;i>=0;i--){
        op[i] = get_max(prev, arr[i]);
        prev = op[i];
    }
    return op;
}

int get_max_index_diff(int *arr, int length){
    int max_diff = -1;
    int *right_max = get_right_max(arr, length);
    int i = 0, j = 0;
    while(i<length && j<length){
        if(arr[i]<right_max[j]){
            max_diff = get_max(max_diff, j-i);
            j++;
        }else{
            i++;
            j = get_max(j, i);
        }
        // printf("i=%d j=%d\n",i,j);
    }
    return max_diff;
}

int main(){
    int arr[] = {6, 5, 4, 3, 2, 1};
    int length = sizeof(arr)/sizeof(int);
    printf("max_diff=%d\n", get_max_index_diff(arr, length));
    return 0;
}
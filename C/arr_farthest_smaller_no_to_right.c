// https://www.geeksforgeeks.org/find-the-farthest-smaller-number-in-the-right-side/
/*
Given an array arr[] of size N. For every element in the array, 
the task is to find the index of the farthest element in the array 
to the right which is smaller than the current element.
  
 If no such number exists then print -1.

Examples:

Input: arr[] = {3, 1, 5, 2, 4}
Output: 3 -1 4 -1 -1
arr[3] is the farthest smallest element to the right of arr[0].
arr[4] is the farthest smallest element to the right of arr[2].
And for the rest of the elements, there is no smaller element to their right.

Input: arr[] = {1, 2, 3, 4, 0}
Output: 4 4 4 4 -1
*/

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int get_floor(int ip[], int min_index[], int s, int e, int data){
    int _floor = -1;
    while(s<=e){
        int mid = s+(e-s)/2;
        if(ip[min_index[mid]]<data){
            _floor = mid;
            s = mid+1;
        }else{
            e = mid-1;
        }
    }
    return _floor;
}

int* get_farther_min_to_right(int ip[], int length){
    int *op = (int*)calloc(length,sizeof(int));
    int *min_index = (int*)calloc(length,sizeof(int));
    int i = length-1;
    min_index[i--] = length-1;
    for(;i>=0;i--){
        if(ip[i]<ip[min_index[i+1]])   min_index[i] = i;
        else    min_index[i] = min_index[i+1];
    }
    print_arr(min_index,length);
    for(i=0;i<length;i++){
        op[i] = get_floor(ip,min_index,i+1,length-1,ip[i]);
    }
    return op;
}

int main(){
    int ip[] = {1,2,3,4,0};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    int *op = get_farther_min_to_right(ip,length);
    print_arr(op,length);

    return 0;
}
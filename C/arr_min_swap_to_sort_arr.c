// https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
/*
Given an array of n distinct elements, find the minimum number of swaps
 required to sort the array.

Examples:
Input : {4, 3, 2, 1}
Output : 2

Input : {1, 5, 4, 3, 2}
Output : 2
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

int* copy_arr(int ip[], int length){
    int *op = (int*)calloc(length,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        op[i] = ip[i];
    }
    return op;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Implementing simple O(n^2) sort here. Best is O(n) sort algo.
void sort_arr(int ip[], int length){
    int i = 0;
    for(;i<length;i++){
        int min = i;
        int j = i+1;
        for(;j<length;j++){
            if(ip[j]<ip[min]){
                min = j;
            }
        }
        swap(ip+i,ip+min);
    }
}

int find_index(int ip[], int s, int e, int num){
    while(s<=e){
        int mid = (s+e)/2;
        if(ip[mid]==num) return mid;
        else if(ip[mid]<num) s = mid+1;
        else e = mid-1;
    }
    return -1;
}

int get_min_swap(int ip[], int length){
    int count = 0;
    int *sorted_ip = copy_arr(ip,length);
    sort_arr(sorted_ip,length);
    int i = 0;
    while(i<length){
        if(ip[i]==sorted_ip[i]) i++;
        else{
            int expected_index = find_index(sorted_ip,0,length-1,ip[i]);
            swap(ip+i,ip+expected_index);
            count++;
        }
    }
    return count;
}

int main(){
    int ip[] = {4,3,1,2};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    printf("Min Swap=%d\n",get_min_swap(ip,length));

    return 0;
}
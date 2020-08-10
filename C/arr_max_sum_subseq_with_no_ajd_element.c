// https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
/*
Given an array of positive numbers, find the maximum sum of a subsequence with
the constraint that no 2 numbers in the sequence should be
adjacent in the array.

Input : arr[] = {5, 5, 10, 100, 10, 5}
Output : 110

Input : arr[] = {1, 2, 3}
Output : 4

Input : arr[] = {1, 20, 3}
Output : 20

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

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

int get_max_sum_subseq_with_no_adj(int ip[], int length){
    int max_sum = INT_MIN;
    int t_sum = 0, prev_sum = 0;
    int i = length-1;
    for(;i>=0;i--){
        int cur_sum = ip[i] + t_sum;
        max_sum = get_max(max_sum,cur_sum);
        t_sum = get_max(t_sum, prev_sum);
        prev_sum = cur_sum;
    }
    return max_sum;
}

int main(){
    int ip[] = {5,3,4,11,2};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    printf("Max sum = %d\n",get_max_sum_subseq_with_no_adj(ip,length));

    return 0;
}
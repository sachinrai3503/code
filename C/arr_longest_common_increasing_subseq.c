// https://www.geeksforgeeks.org/longest-common-increasing-subsequence-lcs-lis/
/*
Given two arrays, find length of the longest common increasing subsequence [LCIS]
 and print one of such sequences (multiple sequences may exist)

Suppose we consider two arrays – 
arr1[] = {3, 4, 9, 1} and 
arr2[] = {5, 3, 8, 9, 10, 2, 1}
Our answer would be {3, 9} as this is the longest common subsequence which is
 increasing also.
*/

#include <stdio.h>
#include <malloc.h>

int get_max(int a, int b){
    if(a>b) return a;
    return b;
}

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int longest_len_com_incresing_subseq(int *ip1, int l1, int *ip2, int l2){
    int *op = (int*)calloc(l2, sizeof(int));
    int max_len = 0;
    int i = 0;
    for(;i<l1;i++){
        int current = 0;
        int j = 0;
        for(;j<l2;j++){
            if(ip1[i]==ip2[j]){
                op[j] = get_max(op[j], current+1);
            }else if(ip1[i]>ip2[j]){
                current = get_max(current, op[j]);
            }
            max_len = get_max(op[j], max_len);
        }
    }
    return max_len;
}

int main(){
    int ip1[] = {1,2,3, 4, 9, 5, 1};
    int ip2[] = {2,3,4,1,2,3,4,5,9,10,2,1};
    int l1 = sizeof(ip1)/sizeof(ip1[0]);
    int l2 = sizeof(ip2)/sizeof(ip2[0]);

    print_arr(ip1, l1);
    print_arr(ip2, l2);

    printf("max len = %d\n", longest_len_com_incresing_subseq(ip1, l1, ip2, l2));

    return 0;
}
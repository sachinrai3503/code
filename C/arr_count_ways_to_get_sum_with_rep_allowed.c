// https://www.geeksforgeeks.org/ways-sum-n-using-array-elements-repetition-allowed/
/*
Given a set of m distinct positive integers and a value ‘N’. 
The problem is to count the total number of ways we can form ‘N’ by doing sum
of the array elements. 
 
Repetitions and different arrangements are allowed.

Examples :

Input : arr = {1, 5, 6}, N = 7
Output : 6

Explanation:- The different ways are:
1+1+1+1+1+1+1
1+1+5
1+5+1
5+1+1
1+6
6+1

Input : arr = {12, 3, 1, 9}, N = 14
Output : 150
*/

// Note - This is slight variation of coin change problem.

#include <stdio.h>
#include <malloc.h>
#include <limits.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int count_ways(int *ip, int length, int sum){
    int *op = (int*)calloc(sum+1, sizeof(int));
    int i = 1;
    for(;i<=sum;i++){
        int j = length-1;
        for(;j>=0;j--){
            if(ip[j]==i) op[i]++;
            else if(ip[j]<i) op[i]+=op[i-ip[j]];
        }
    }
    return op[sum];
}

int main(){
    int ip[] = {1,3,4};
    int length = sizeof(ip)/sizeof(ip[0]);
    int sum = 5;

    print_arr(ip,length);
    printf("Ways to get sum = %d are = %d.",sum,count_ways(ip,length,sum));

    return 0;
}
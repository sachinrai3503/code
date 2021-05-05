// https://www.geeksforgeeks.org/count-derangements-permutation-such-that-no-element-appears-in-its-original-position/
/*
A Derangement is a permutation of n elements, such that no element appears in
 its original position. For example, a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}.
Given a number n, find total number of Derangements of a set of n elements.

Examples : 
Input: n = 2
Output: 1
For two elements say {0, 1}, there is only one 
possible derangement {1, 0}

Input: n = 3
Output: 2
For three elements say {0, 1, 2}, there are two 
possible derangements {2, 0, 1} and {1, 2, 0}

Input: n = 4
Output: 9
For four elements say {0, 1, 2, 3}, there are 9
possible derangements {1, 0, 3, 2} {1, 2, 3, 0}
{1, 3, 0, 2}, {2, 3, 0, 1}, {2, 0, 3, 1}, {2, 3,
1, 0}, {3, 0, 1, 2}, {3, 2, 0, 1} and {3, 2, 1, 0}
*/

#include <stdio.h>
#include <malloc.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* init_arr(int length){
    int *ip = (int*)calloc(length, sizeof(int));
    int i = 0;
    for(;i<length;i++){
        ip[i] = i;
    }
    return ip;
}

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int count_deaarangements(int *t_arr, int length, int i){
    if(i==length){
        // print_arr(t_arr, length);
        return 1;
    }
    int count = 0;
    int from = i;
    if(t_arr[i]==i) from = i+1;
    for(;from<length;from++){
        swap(t_arr+i, t_arr+from);
        count+=count_deaarangements(t_arr, length, i+1);
        swap(t_arr+i, t_arr+from);
    }
    return count;
}

int count_deaarangements2(int n){
    if(n==0) return 1;
    if(n==1) return 0;
    int a = 1, b = 0;
    int count = 0;
    int i = 2;
    while(i<=n){
        count = (i-1)*(a+b);
        a = b;
        b = count;
        i+=1;
    }
    return count;
}

int main(){
    int n = 1000;
    int i = 0;
    for(;i<=n;i++){
        // int *op = init_arr(i);
        // int count = count_deaarangements(op, i, 0);
        int count =  count_deaarangements2(i);
        printf("n=%d count = %d\n", i, count);
    }
    return 0;
}
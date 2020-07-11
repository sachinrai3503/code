// https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

/**
 Given a set of integers, 
 the task is to divide it into two sets S1 and S2 such that the absolute
difference between their sums is minimum. 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11  

*/

// Python sol. - list_divide_arr_in_2_with_min_diff.py

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

int get_min(int a, int b){
    if(a>b) return b;
    return a;
}

int get_diff(int a, int b){
    if(a>b) return a-b;
    return b-a;
}

/**
 * Returns min diff between 2 subset of the arr.
 * */
int get_min_diff_REC(int ip[], int length, int i, int s1, int s2){
    if(length<=0){
        printf("Invalid\n");
        return INT_MIN;
    }
    if(i==length){
        return get_diff(s1,s2);
    }
    return get_min(get_min_diff_REC(ip,length,i+1,s1+ip[i],s2),get_min_diff_REC(ip,length,i+1,s1,s2+ip[i]));
}

int main(){
    int ip[] = {40,20,60,10,50,30};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);

    printf("Min Diff of 2 subset = %d\n",get_min_diff_REC(ip,length,0,0,0));

    return 0;
}
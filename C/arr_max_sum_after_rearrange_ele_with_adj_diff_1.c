// https://www.geeksforgeeks.org/maximize-sum-of-given-array-by-rearranging-array-such-that-the-difference-between-adjacent-elements-is-atmost-1/
/*
Given an array arr[] consisting of N positive integers, the task is to maximize
 the sum of the array element such that the first element of the array is 1
  and the difference between the adjacent elements of the array is at most 1
   after performing the following operations:

Rearrange the array elements in any way.
Reduce any element to any number that is at least 1.
Examples:

Input: arr[] = {3, 5, 1}
Output: 6
Explanation:
One possible arrangement is {1, 2, 3} having maximum possible sum 6.

Input: arr[] = {1, 2, 2, 2, 3, 4, 5}
Output: 19
Explanation:
One possible arrangement is {1, 2, 2, 2, 3, 4, 5} having maximum possible sum 19.
*/

// Simple sol. would be to sort the arr and decreasing the element where needed.
// Below is a hashing based sol.

#include <stdio.h>
#include <malloc.h>

void print_arr(int *ip, int length){
    int i = 0;
    for(;i<length;i++){
        printf("%d ",ip[i]);
    }
    printf("\n");
}

int* get_count_map(int *ip, int length){
    int *map = (int*)calloc(length+1,sizeof(int));
    int i = 0;
    for(;i<length;i++){
        int num = ip[i];
        if(num<=length){
            map[num]++;
        }else{
            map[length]++;
        }
    }
    return map;
}

int rearrange_arr_with_max_sum(int ip[], int length){
    if(length<=0){
        printf("Invalid\n");
        return 0;
    }
    int sum = 0;
    int *count_map = get_count_map(ip,length);
    // print_arr(count_map, length+1);
    int expected_ele = 1;
    int i = 1;
    while(i<length+1){
        if(count_map[i]==0){
            i++;
            continue;
        }
        int cur_ele =  i;
        if(cur_ele<expected_ele) sum+=cur_ele;
        else{
            sum+=expected_ele;
            expected_ele++;
        }
        count_map[i]--;
    }
    return sum;
}

int main(){
    int ip[] = {1, 2, 2, 2, 3, 4, 5};
    int length = sizeof(ip)/sizeof(ip[0]);

    print_arr(ip,length);
    int sum = rearrange_arr_with_max_sum(ip,length);
    printf("Sum = %d\n",sum);

    return 0;
}
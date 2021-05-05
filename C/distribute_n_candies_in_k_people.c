// https://www.geeksforgeeks.org/distribute-n-candies-among-k-people/
/*
Given N candies and K people. In the first turn, the first person gets 1 candy,
 the second gets 2 candies, and so on till K people. In the next turn, the first
 person gets K+1 candies, the second person gets k+2 candies and so on. If the
 number of candies is less than the required number of candies at every turn,
 then the person receives the remaining number of candies.

The task is to find the total number of candies every person has at the end.

Examples:
Input: N = 7, K = 4
Output: 1 2 3 1
At the first turn, the fourth people has to be given 4 candies, but there is
only 1 left, hence he takes one only.

Input: N = 10, K = 3
Output: 5 2 3
At the second turn first one receives 4 and then we have no more candies left.
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

int get_ap_sum(int n){
    return (n*(n+1))/2;
}

int get_max_num_count_with_ap_sum(int n){
    int num = 0;
    int s = 0, e = n;
    while(s<=e){
        int mid = s + (e-s)/2;
        if(get_ap_sum(mid)>n) e = mid-1;
        else{
            num = mid;
            s = mid+1;
        }
    }
    return num;
}

int* distribute_N_candy_to_k_people(int n, int k){
    if(k==0 || n==0) return NULL;
    int *op = (int*)calloc(k, sizeof(int));
    int max_count = get_max_num_count_with_ap_sum(n);
    int total_count = get_ap_sum(max_count);
    int remaining = n - total_count;
    int turn = max_count/k;
    int last_turn_till = max_count%k;
    int i = 0;
    for(;i<k;i++){
        int count = (turn*(2*(i+1) + (turn-1)*k))/2;
        if(i<last_turn_till){
            count = count + ((i+1) + k*turn);
        }else if(i==last_turn_till){
            count = count +  remaining;
        }
        op[i] = count;
    }
    return op;
}

int main(){
    int n = 100;
    int k = 1;
    printf("n=%d k=%d\n",n,k);
    int *op = distribute_N_candy_to_k_people(n,k);
    print_arr(op, k);

    return 0;
}